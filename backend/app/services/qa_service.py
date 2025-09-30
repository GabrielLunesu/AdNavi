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


class QAService:
    """
    High-level QA orchestrator using the DSL v1.1 pipeline.
    
    This service:
    1. Translates questions to DSL via LLM
    2. Plans the query execution
    3. Executes against the database
    4. Builds human-readable answers
    5. Logs everything for telemetry
    
    Related:
    - Uses: Translator, build_plan, execute_plan
    - Called by: app/routers/qa.py
    """
    
    def __init__(self, db: Session):
        """
        Initialize QA service.
        
        Args:
            db: SQLAlchemy database session
        """
        self.db = db
        self.translator = Translator()
    
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
        1. Translate question → DSL (via LLM)
        2. Build execution plan
        3. Execute plan → results
        4. Format human-readable answer
        5. Log run for telemetry
        """
        start_time = time.time()
        error_message = None
        dsl = None
        answer_text = None
        
        try:
            # Step 1: Translate to DSL
            dsl, translation_latency = self.translator.to_dsl(
                question, 
                log_latency=True
            )
            
            # Step 2: Plan execution (may return None for non-metrics queries)
            plan = build_plan(dsl)
            
            # Step 3: Execute plan (pass both plan and query for DSL v1.2)
            result = execute_plan(
                db=self.db,
                workspace_id=workspace_id,
                plan=plan,
                query=dsl
            )
            
            # Step 4: Build human-readable answer
            answer_text = self._build_answer(dsl, result)
            
            # Step 5: Log success
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
            
            # Step 6: Serialize result based on type
            # For metrics queries: result is a MetricResult (Pydantic model)
            # For providers/entities queries: result is already a dict
            if hasattr(result, 'model_dump'):
                result_data = result.model_dump()
            else:
                result_data = result  # Already a dict
            
            return {
                "answer": answer_text,
                "executed_dsl": dsl.model_dump(),  # Convert Pydantic model to dict
                "data": result_data
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
    
    def _build_answer(self, dsl, result) -> str:
        """
        Build a human-readable answer from DSL + results.
        
        DSL v1.2 changes:
        - Handles providers queries: "You are running ads on Google, Meta, TikTok."
        - Handles entities queries: "Here are your campaigns: Summer Sale, Winter Promo, ..."
        - Handles metrics queries: existing logic (ROAS, CPA, etc.)
        
        Args:
            dsl: MetricQuery that was executed
            result: MetricResult (metrics) or dict (providers/entities) from execution
            
        Returns:
            Human-readable answer text
            
        Design:
        - Deterministic (no LLM)
        - Template-based for consistency
        - Includes comparison delta if available (metrics only)
        - Mentions breakdown if present (metrics only)
        
        Future enhancement:
        - Could use LLM to generate more natural answers
        - For now, keep it simple and predictable
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
