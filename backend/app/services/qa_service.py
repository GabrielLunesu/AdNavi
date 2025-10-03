"""
QA Service
==========

High-level orchestrator for question-answering using the DSL v1.1 architecture.

Related files:
- app/nlp/translator.py: Natural language → DSL
- app/dsl/planner.py: DSL → execution plan
- app/dsl/executor.py: Plan → database results
- app/telemetry/logging.py: Structured logging
- app/routers/qa.py: HTTP endpoint

Design:
- Clean pipeline: question → canonicalize → translate → plan → execute → answer
- Comprehensive error handling at each stage
- Telemetry for observability
- Simple answer generation (deterministic, no LLM)

Usage:
    service = QAService(db)
    result = service.answer(question="What's my ROAS?", workspace_id="...")
"""

from __future__ import annotations

import time
from typing import Dict, Any, Optional

from sqlalchemy.orm import Session

from app.nlp.translator import Translator, TranslationError
from app.dsl.planner import build_plan
from app.dsl.executor import execute_plan
from app.dsl.validate import DSLValidationError
from app.telemetry.logging import log_qa_run
from app.answer.answer_builder import AnswerBuilder, AnswerBuilderError
from app import state  # Import shared application state


class QAService:
    """
    High-level QA orchestrator using the DSL v1.2 pipeline with conversation context.
    
    This service:
    1. Retrieves conversation history for context
    2. Translates questions to DSL via LLM (context-aware)
    3. Plans the query execution
    4. Executes against the database
    5. Builds human-readable answers
    6. Stores conversation history for follow-ups
    7. Logs everything for telemetry
    
    Related:
    - Uses: Translator, build_plan, execute_plan, ContextManager
    - Called by: app/routers/qa.py
    """
    
    def __init__(self, db: Session):
        """
        Initialize QA service.
        
        Args:
            db: SQLAlchemy database session
        
        Components:
        - translator: Converts natural language → DSL (app/nlp/translator.py)
        - answer_builder: Converts results → natural language (app/answer/answer_builder.py)
        - context_manager: SHARED singleton for conversation history (app/state.py)
        
        WHY separation:
        - Translator: Question → structured query
        - Executor: Structured query → numbers
        - AnswerBuilder: Numbers → natural answer
        - ContextManager: Multi-turn conversation support (shared across requests)
        
        WHY shared context_manager:
        - Each HTTP request creates a new QAService instance
        - If each instance had its own ContextManager, context would be lost between requests
        - Using shared singleton from app.state ensures context persists
        """
        self.db = db
        self.translator = Translator()
        self.answer_builder = AnswerBuilder()
        # Use SHARED context manager from application state (not a new instance)
        # WHY: Context must persist across HTTP requests
        self.context_manager = state.context_manager
    
    def answer(
        self, 
        question: str, 
        workspace_id: str,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Answer a natural language question about metrics.
        
        Args:
            question: User's natural language question
            workspace_id: Workspace UUID for scoping
            user_id: User UUID for logging (optional)
            
        Returns:
            Dict with:
                - answer: Human-readable answer text
                - executed_dsl: Validated MetricQuery that was executed
                - data: MetricResult with summary/timeseries/breakdown
                
        Raises:
            TranslationError: If LLM translation fails
            DSLValidationError: If DSL validation fails
            Exception: If execution fails
            
        Examples:
            >>> service = QAService(db)
            >>> result = service.answer(
            ...     question="What's my ROAS this week?",
            ...     workspace_id="123e4567..."
            ... )
            >>> print(result["answer"])
            "Your ROAS for the selected period is 2.45."
        
        Pipeline:
        1. Retrieve conversation history (context)
        2. Translate question → DSL (via LLM, with context)
        3. Build execution plan
        4. Execute plan → results
        5. Format human-readable answer
        6. Store in conversation history
        7. Log run for telemetry
        """
        start_time = time.time()
        error_message = None
        dsl = None
        answer_text = None
        
        try:
            # Step 1: Fetch prior context (last N Q&A for this user+workspace)
            # WHY: Enables follow-up questions like "Which one performed best?"
            context = self.context_manager.get_context(
                user_id or "anon", 
                workspace_id
            )
            
            # Step 2: Translate to DSL with context awareness
            # WHY context: LLM can resolve pronouns ("that", "this", "which one")
            dsl, translation_latency = self.translator.to_dsl(
                question, 
                log_latency=True,
                context=context  # NEW: Pass conversation history
            )
            
            # Step 3: Plan execution (may return None for non-metrics queries)
            plan = build_plan(dsl)
            
            # Step 4: Execute plan (pass both plan and query for DSL v1.2)
            result = execute_plan(
                db=self.db,
                workspace_id=workspace_id,
                plan=plan,
                query=dsl
            )
            
            # Step 5: Build human-readable answer (hybrid approach)
            # WHY hybrid: LLM rephrases deterministic facts → natural + safe
            # WHY fallback: If LLM fails, use template-based answer
            answer_generation_ms = None
            try:
                # Try hybrid answer builder (LLM-based rephrasing)
                answer_text, answer_generation_ms = self.answer_builder.build_answer(
                    dsl=dsl,
                    result=result,
                    log_latency=True
                )
            except AnswerBuilderError as e:
                # Fallback to template-based answer if LLM fails
                # WHY fallback: Ensures we always return something, even if LLM is down
                print(f"⚠️  Answer builder failed, using template fallback: {e.message}")
                answer_text = self._build_answer_template(dsl, result)
                answer_generation_ms = None  # Not measured for fallback
            
            # Step 6: Save to conversation context for follow-ups
            # WHY: Enables next question to reference this query
            # Example: User asks "Which one performed best?" → needs this result
            # Serialize result based on type
            if hasattr(result, 'model_dump'):
                result_data = result.model_dump()
            else:
                result_data = result  # Already a dict
            
            self.context_manager.add_entry(
                user_id=user_id or "anon",
                workspace_id=workspace_id,
                question=question,
                dsl=dsl.model_dump(),
                result=result_data
            )
            
            # Step 7: Build context summary for response (for debugging in Swagger)
            # WHY: Makes it visible what context was used for this query
            # Useful for testing follow-up questions in Swagger UI
            context_summary = self._build_context_summary_for_response(context)
            
            # Step 8: Log success (including answer generation latency)
            total_latency_ms = int((time.time() - start_time) * 1000)
            log_qa_run(
                db=self.db,
                workspace_id=workspace_id,
                question=question,
                dsl=dsl.model_dump(),
                success=True,
                latency_ms=total_latency_ms,
                user_id=user_id,
                answer_text=answer_text
            )
            
            return {
                "answer": answer_text,
                "executed_dsl": dsl.model_dump(),  # Convert Pydantic model to dict
                "data": result_data,
                "context_used": context_summary  # NEW: Show what context was available
            }
            
        except TranslationError as e:
            error_message = f"Translation failed: {e.message}"
            total_latency_ms = int((time.time() - start_time) * 1000)
            
            # Log failure
            log_qa_run(
                db=self.db,
                workspace_id=workspace_id,
                question=question,
                dsl=None,
                success=False,
                latency_ms=total_latency_ms,
                user_id=user_id,
                error_message=error_message
            )
            
            raise
            
        except DSLValidationError as e:
            error_message = f"Validation failed: {e.message}"
            total_latency_ms = int((time.time() - start_time) * 1000)
            
            # Log failure
            log_qa_run(
                db=self.db,
                workspace_id=workspace_id,
                question=question,
                dsl=None,
                success=False,
                latency_ms=total_latency_ms,
                user_id=user_id,
                error_message=error_message
            )
            
            raise
            
        except Exception as e:
            error_message = f"Execution failed: {str(e)}"
            total_latency_ms = int((time.time() - start_time) * 1000)
            
            # Log failure
            log_qa_run(
                db=self.db,
                workspace_id=workspace_id,
                question=question,
                dsl=dsl.model_dump() if dsl else None,
                success=False,
                latency_ms=total_latency_ms,
                user_id=user_id,
                error_message=error_message
            )
            
            raise
    
    def _build_answer_template(self, dsl, result) -> str:
        """
        Build a template-based answer (FALLBACK ONLY).
        
        WHY this exists:
        - Fallback when AnswerBuilder (LLM) fails
        - Ensures we always return an answer
        - Deterministic, safe, but less natural than LLM version
        
        DSL v1.2 changes:
        - Handles providers queries: "You are running ads on Google, Meta, TikTok."
        - Handles entities queries: "Here are your campaigns: Summer Sale, Winter Promo, ..."
        - Handles metrics queries: existing logic (ROAS, CPA, etc.)
        
        Args:
            dsl: MetricQuery that was executed
            result: MetricResult (metrics) or dict (providers/entities) from execution
            
        Returns:
            Human-readable answer text (template-based, robotic)
            
        Design:
        - Deterministic (no LLM, no randomness)
        - Template-based (predictable format)
        - Includes comparison delta if available (metrics only)
        - Mentions breakdown if present (metrics only)
        
        Related:
        - Primary: app/answer/answer_builder.py (LLM-based, preferred)
        - Used when: AnswerBuilder raises AnswerBuilderError
        """
        # DSL v1.2: Handle providers queries
        # Example: "Which platforms am I advertising on?"
        # Result: {"providers": ["google", "meta", "tiktok"]}
        if dsl.query_type == "providers":
            providers = result.get("providers", [])
            if not providers:
                return "No active ad platforms found for this workspace."
            
            # Format provider names nicely (capitalize first letter)
            formatted = [p.capitalize() for p in providers]
            
            if len(formatted) == 1:
                return f"You are running ads on {formatted[0]}."
            elif len(formatted) == 2:
                return f"You are running ads on {formatted[0]} and {formatted[1]}."
            else:
                # Oxford comma for 3+
                all_but_last = ", ".join(formatted[:-1])
                return f"You are running ads on {all_but_last}, and {formatted[-1]}."
        
        # DSL v1.2: Handle entities queries
        # Example: "List my active campaigns"
        # Result: {"entities": [{"name": "...", "status": "...", "level": "..."}, ...]}
        if dsl.query_type == "entities":
            entities = result.get("entities", [])
            if not entities:
                return "No entities matched your filters."
            
            # Determine what we're listing (campaigns, adsets, ads)
            level = dsl.filters.level if dsl.filters and dsl.filters.level else "entities"
            level_plural = level if level.endswith("s") else f"{level}s"
            
            # List entity names
            names = [e["name"] for e in entities]
            
            if len(names) <= 3:
                # Short list: enumerate all
                names_str = ", ".join(names)
                return f"Here are your {level_plural}: {names_str}."
            else:
                # Long list: show first 3 and count
                first_three = ", ".join(names[:3])
                remaining = len(names) - 3
                return f"Here are your {level_plural}: {first_three}, and {remaining} more."
        
        # METRICS: Original logic (DSL v1.1)
        # Existing answer building for metrics queries
        metric_display = dsl.metric.upper() if dsl.metric else "METRIC"
        
        # For metrics, result is a MetricResult or dict with .summary
        if isinstance(result, dict):
            value = result.get("summary")
        else:
            value = result.summary
        
        # Format value based on metric type
        if value is None:
            value_str = "N/A (insufficient data)"
        elif dsl.metric in ("roas", "cvr"):
            value_str = f"{value:.2f}"  # 2 decimals for ratios
        elif dsl.metric == "cpa":
            value_str = f"${value:.2f}"  # Currency for CPA
        elif dsl.metric in ("spend", "revenue"):
            value_str = f"${value:,.2f}"  # Currency with commas
        else:
            value_str = f"{value:,.0f}"  # Whole numbers for clicks/impressions/conversions
        
        # Build base answer
        answer = f"Your {metric_display} for the selected period is {value_str}."
        
        # Add comparison if available
        delta_pct = result.get("delta_pct") if isinstance(result, dict) else getattr(result, "delta_pct", None)
        if delta_pct is not None:
            delta_display = f"{delta_pct * 100:+.1f}%"
            answer += f" That's a {delta_display} change vs the previous period."
        
        # Mention breakdown if available
        breakdown = result.get("breakdown") if isinstance(result, dict) else getattr(result, "breakdown", None)
        if breakdown and len(breakdown) > 0:
            top_item = breakdown[0]
            answer += f" Top performer: {top_item['label']}."
        
        return answer
    
    def _build_context_summary_for_response(self, context: list) -> list:
        """
        Build a simplified context summary for API response.
        
        WHY this exists:
        - Makes context visible in Swagger UI responses
        - Helps users debug follow-up question behavior
        - Shows what information was available when translating the query
        
        Args:
            context: Full context list from context_manager.get_context()
                     Each entry: {"question": str, "dsl": dict, "result": dict}
        
        Returns:
            Simplified list of dicts with only key info for debugging
            Empty list if no context available
        
        Examples:
            >>> context = [{"question": "how much revenue?", "dsl": {"metric": "revenue"}, "result": {...}}]
            >>> summary = self._build_context_summary_for_response(context)
            >>> summary
            [{"question": "how much revenue?", "metric": "revenue"}]
        
        Design decisions:
        - Only include question + key DSL fields (metric, query_type)
        - Omit full result data to keep response size small
        - Empty list (not null) when no context for consistent typing
        
        Related:
        - Used in: answer() method to populate response
        - Visible in: Swagger UI /qa endpoint responses
        - Helps debug: Follow-up questions ("and the week before?")
        """
        if not context or len(context) == 0:
            return []
        
        summary = []
        for entry in context:
            question = entry.get("question", "")
            dsl = entry.get("dsl", {})
            
            # Extract only the most relevant DSL fields for debugging
            context_item = {
                "question": question,
                "query_type": dsl.get("query_type", "metrics"),
            }
            
            # Add metric if present (helps debug metric inheritance)
            if "metric" in dsl and dsl["metric"]:
                context_item["metric"] = dsl["metric"]
            
            # Add time range if present (helps debug time period changes)
            if "time_range" in dsl and dsl["time_range"]:
                time_range = dsl["time_range"]
                if isinstance(time_range, dict) and "last_n_days" in time_range:
                    context_item["time_period"] = f"last_{time_range['last_n_days']}_days"
            
            summary.append(context_item)
        
        return summary
