"""
Answer Builder (Hybrid)
========================

Generates human-readable answers from DSL + execution results.

WHY Hybrid Approach:
- **Deterministic facts**: Extract numbers/data from results (no hallucinations)
- **LLM rephrasing**: Make answers sound natural and conversational (not robotic)
- **Safety**: LLM cannot invent numbers, only rephrase provided facts

CHANGES IN v2.0.1:
- Use extract_rich_context() instead of basic fact extraction
- Enhanced GPT prompt with structured context
- Better system instructions for using rich context

Design Principles:
- Separation of concerns: This module handles ONLY answer generation
- QAService orchestrates the pipeline (translate → plan → execute → answer)
- Executor computes numbers, this class handles presentation

Related files:
- app/dsl/schema.py: Defines MetricQuery + MetricResult (facts source)
- app/services/qa_service.py: Calls this builder to generate answers
- app/nlp/translator.py: Similar LLM usage pattern for DSL translation
- app/answer/context_extractor.py: Rich context extraction (NEW in v2.0.1)
"""

from __future__ import annotations

import time
import json
import logging
from typing import Dict, Any, Union, Optional
from datetime import date
from openai import OpenAI

from app.dsl.schema import MetricQuery, MetricResult
from app.deps import get_settings
from app.answer.formatters import format_metric_value, format_delta_pct, fmt_currency, fmt_count
from app.answer.context_extractor import extract_rich_context  # NEW in v2.0.1
from app.nlp.prompts import ANSWER_GENERATION_PROMPT  # NEW in v2.0.1

logger = logging.getLogger(__name__)


def _format_date_range(start: date, end: date) -> str:
    """
    Format a date range as human-readable string.
    
    WHY this exists:
    - Provides trust and transparency in answers
    - Users want to know exactly what time window the data covers
    - Compact format saves tokens in LLM prompts
    
    Args:
        start: Start date (inclusive)
        end: End date (inclusive)
        
    Returns:
        Formatted date range string
        
    Examples:
        >>> _format_date_range(date(2025, 9, 29), date(2025, 10, 5))
        "Sep 29–Oct 05, 2025"
        
        >>> _format_date_range(date(2025, 10, 1), date(2025, 10, 1))
        "Oct 01, 2025"
    
    Format decisions:
    - Use abbreviated month names (Sep, Oct) for compactness
    - Use en-dash (–) between dates (not hyphen)
    - Include year at end only (avoid repetition)
    - Single day: Show just one date
    
    Related:
    - Used by: build_answer() to include date window in answers
    - Alternative: ISO format (YYYY-MM-DD) is more precise but less friendly
    """
    # Single day: don't show range
    if start == end:
        return start.strftime("%b %d, %Y")
    
    # Same month: "Sep 29–30, 2025"
    if start.year == end.year and start.month == end.month:
        return f"{start.strftime('%b %d')}–{end.strftime('%d, %Y')}"
    
    # Different months, same year: "Sep 29–Oct 05, 2025"
    if start.year == end.year:
        return f"{start.strftime('%b %d')}–{end.strftime('%b %d, %Y')}"
    
    # Different years: "Dec 29, 2024–Jan 05, 2025"
    return f"{start.strftime('%b %d, %Y')}–{end.strftime('%b %d, %Y')}"


class AnswerBuilderError(Exception):
    """
    Raised when answer generation fails.
    
    This signals to QAService to use the fallback template-based builder.
    """
    def __init__(self, message: str, original_error: Exception = None):
        self.message = message
        self.original_error = original_error
        super().__init__(message)


class AnswerBuilder:
    """
    Hybrid Answer Builder
    ---------------------
    
    Responsible ONLY for answer generation.
    
    WHY separation from QAService:
    - QAService orchestrates the pipeline (translate → plan → execute → answer)
    - Executor computes the numbers (deterministic, safe)
    - This class handles presentation (natural language)
    
    Process:
    1. Extract deterministic facts from results (no hallucinations possible)
    2. Build structured fact payload
    3. Call GPT-4o-mini with strict instructions:
       - "Do NOT invent numbers"
       - "Use only provided facts"
       - "Keep it conversational"
    4. Return rephrased natural language
    
    Fallback:
    - If LLM call fails, raise AnswerBuilderError
    - QAService will catch and use template-based fallback
    
    Examples:
        >>> builder = AnswerBuilder()
        >>> # Metrics query
        >>> dsl = MetricQuery(query_type="metrics", metric="roas")
        >>> result = MetricResult(summary=2.45, delta_pct=0.19)
        >>> answer = builder.build_answer(dsl, result)
        >>> print(answer)
        "Your ROAS is currently 2.45, which represents a 19% improvement 
         over the previous period. Great work!"
        
        >>> # Providers query
        >>> dsl = MetricQuery(query_type="providers")
        >>> result = {"providers": ["google", "meta", "tiktok"]}
        >>> answer = builder.build_answer(dsl, result)
        >>> print(answer)
        "You're running ads across three platforms: Google, Meta, and TikTok."
    
    Related:
    - Used by: app/services/qa_service.py
    - Input: app/dsl/schema.py (MetricQuery, MetricResult or dict)
    """
    
    def __init__(self):
        """
        Initialize Answer Builder with OpenAI client.
        
        Uses the same API key and client pattern as the Translator
        for consistency.
        
        Related:
        - app/nlp/translator.py: Similar initialization pattern
        - app/deps.py: get_settings() provides OpenAI API key
        """
        settings = get_settings()
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
    
    def build_answer(
        self, 
        dsl: MetricQuery, 
        result: Union[MetricResult, Dict[str, Any]],
        window: Optional[Dict[str, date]] = None,
        log_latency: bool = False
    ) -> tuple[str, Optional[int]]:
        """
        Build a natural language answer from query + results.
        
        CHANGES IN v2.0.1:
        - Uses extract_rich_context() for metrics queries (instead of basic facts)
        - Enhanced GPT prompt with structured context
        - Workspace average comparison included when available
        
        Args:
            dsl: The MetricQuery that was executed (user intent)
            result: Execution results (MetricResult for metrics, dict for providers/entities)
            window: Optional date window {"start": date, "end": date} for including date range in answer
            log_latency: Whether to return latency in ms (for telemetry)
            
        Returns:
            tuple: (answer_text, latency_ms) if log_latency=True, else (answer_text, None)
            
        Raises:
            AnswerBuilderError: If LLM call fails (QAService will fallback to template)
            
        Examples:
            >>> builder = AnswerBuilder()
            >>> dsl = MetricQuery(query_type="metrics", metric="roas", time_range=TimeRange(last_n_days=7))
            >>> result = MetricResult(summary=2.45, previous=2.06, workspace_avg=2.30)
            >>> answer, latency = builder.build_answer(dsl, result, log_latency=True)
            >>> print(answer)
            "Your ROAS jumped to 2.45× last week—19% higher than before. This is slightly above your workspace average of 2.30×."
            
        Process (v2.0.1):
        1. For metrics queries: Extract rich context (trends, comparisons, outliers)
        2. For other queries: Extract basic facts (providers, entities)
        3. Build GPT prompt with context-aware instructions
        4. Call GPT-4o-mini for natural language generation
        5. Return answer (or raise error for fallback)
        
        Related:
        - Called by: app/services/qa_service.py
        - Context extraction: app/answer/context_extractor.py (NEW in v2.0.1)
        - System prompt: app/nlp/prompts.py::ANSWER_GENERATION_PROMPT
        """
        start_time = time.time() if log_latency else None
        
        try:
            # Step 1: Extract context or facts based on query type
            # WHY v2.0.1 change: Metrics queries now use rich context for better answers
            if dsl.query_type == "metrics":
                # NEW v2.0.1: Use rich context extractor for metrics
                context = extract_rich_context(
                    result=result,
                    query=dsl,
                    workspace_avg=result.workspace_avg if isinstance(result, MetricResult) else None
                )
                
                logger.info(
                    "Extracted rich context for answer generation",
                    extra={
                        "metric": context.metric_name,
                        "performance": context.performance_level,
                        "has_comparison": context.comparison is not None,
                        "has_workspace_comparison": context.workspace_comparison is not None,
                        "has_trend": context.trend is not None,
                        "has_outliers": len(context.outliers) > 0
                    }
                )
                
                # Build prompt with rich context
                user_prompt = self._build_rich_context_prompt(context, dsl)
                system_prompt = ANSWER_GENERATION_PROMPT  # NEW in v2.0.1
                
            elif dsl.query_type == "providers":
                facts = self._extract_providers_facts(result)
                system_prompt = self._build_system_prompt()
                user_prompt = self._build_user_prompt(dsl, facts)
                
            else:  # entities
                facts = self._extract_entities_facts(dsl, result)
                system_prompt = self._build_system_prompt()
                user_prompt = self._build_user_prompt(dsl, facts)
            
            # Step 2: Call GPT-4o-mini
            # WHY gpt-4o-mini: Cost-effective, good at instruction-following
            # WHY temperature=0.3: Some naturalness, but still deterministic
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                temperature=0.3,  # Slightly creative for natural flow, but controlled
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=200  # Increased from 150 to allow for richer answers (2-4 sentences)
            )
            
            answer_text = response.choices[0].message.content.strip()
            
            # Step 3: Calculate latency if requested
            latency_ms = None
            if log_latency and start_time:
                latency_ms = int((time.time() - start_time) * 1000)
            
            logger.info(f"Generated natural answer ({len(answer_text)} chars) in {latency_ms}ms")
            
            return answer_text, latency_ms
            
        except Exception as e:
            logger.error(f"Answer generation failed: {e}", exc_info=True)
            # Raise custom error so QAService knows to use fallback
            raise AnswerBuilderError(
                message=f"Answer generation failed: {str(e)}",
                original_error=e
            )
    
    def _extract_metrics_facts(
        self, 
        dsl: MetricQuery, 
        result: Union[MetricResult, Dict],
        window: Optional[Dict[str, date]] = None
    ) -> Dict[str, Any]:
        """
        Extract deterministic facts from metrics query results.
        
        WHY deterministic extraction:
        - Prevents LLM from inventing numbers
        - All facts come from validated execution results
        - Safe to pass to LLM for rephrasing only
        
        FORMATTING STRATEGY:
        - Provide BOTH raw and formatted values
        - Instruct GPT to prefer formatted values
        - This prevents GPT from inventing formatting (e.g., "$0" for CPC)
        
        NEW (v2.0): Date windows and denominators
        - Include date range for transparency ("Sep 29–Oct 05, 2025")
        - Include denominators (spend, clicks, conversions) for context
        
        Args:
            dsl: MetricQuery with query intent
            result: MetricResult or dict with summary, delta_pct, breakdown
            window: Optional date window {"start": date, "end": date}
            
        Returns:
            Dict with extracted facts ready for LLM prompt (includes formatted values, date range, denominators)
            
        Example:
            >>> facts = _extract_metrics_facts(dsl, result)
            >>> facts
            {
                "metric": "cpc",
                "value_raw": 0.4794,
                "value_formatted": "$0.48",
                "previous_value_raw": 0.3912,
                "previous_value_formatted": "$0.39",
                "change_formatted": "+22.5%",
                "top_performer": "Summer Sale"
            }
        
        Related:
        - Input: app/dsl/schema.py (MetricResult)
        - Formatters: app/answer/formatters.py (format_metric_value, format_delta_pct)
        - Used by: build_answer()
        """
        # Handle both MetricResult objects and dicts
        if isinstance(result, dict):
            summary = result.get("summary")
            previous = result.get("previous")
            delta_pct = result.get("delta_pct")
            breakdown = result.get("breakdown")
        else:
            summary = result.summary
            previous = result.previous
            delta_pct = result.delta_pct
            breakdown = result.breakdown
        
        # Format the main value
        # WHY both raw and formatted: GPT gets correct formatting, fallback has raw for math
        formatted_summary = format_metric_value(dsl.metric, summary)
        
        facts = {
            "metric": dsl.metric,
            "value_raw": summary,
            "value_formatted": formatted_summary,  # GPT should use this
        }
        
        # Add date window for transparency (NEW v2.0)
        # WHY: Users trust answers more when they know the exact time period
        # Example: "Summer Sale had highest ROAS at 3.20× from Sep 29–Oct 05, 2025"
        if window and "start" in window and "end" in window:
            date_range_str = _format_date_range(window["start"], window["end"])
            facts["date_range"] = date_range_str
        
        # Add comparison if available (with formatting)
        if previous is not None:
            formatted_previous = format_metric_value(dsl.metric, previous)
            facts["previous_value_raw"] = previous
            facts["previous_value_formatted"] = formatted_previous  # GPT should use this
        
        if delta_pct is not None:
            # Format percentage change with sign
            formatted_delta = format_delta_pct(delta_pct)
            facts["change_raw"] = delta_pct
            facts["change_formatted"] = formatted_delta  # GPT should use this
        
        # Add top performer if breakdown exists
        # WHY: Gives context for "which campaign drove this?"
        if breakdown and len(breakdown) > 0:
            top = breakdown[0]
            facts["top_performer"] = top.get("label")
            # Also format the top performer's value
            if "value" in top:
                facts["top_performer_value_formatted"] = format_metric_value(
                    dsl.metric, 
                    top.get("value")
                )
            
            # NEW v2.0: Include denominators for context
            # WHY: Helps explain results in natural language
            # Example: "Summer Sale had ROAS 3.20× (Spend $1,234, Revenue $3,948)"
            denominators = []
            if "spend" in top and top.get("spend"):
                denominators.append(f"Spend {fmt_currency(top['spend'])}")
            if "revenue" in top and top.get("revenue"):
                denominators.append(f"Revenue {fmt_currency(top['revenue'])}")
            if "clicks" in top and top.get("clicks"):
                denominators.append(f"{fmt_count(top['clicks'])} clicks")
            if "conversions" in top and top.get("conversions"):
                denominators.append(f"{fmt_count(top['conversions'])} conversions")
            
            if denominators:
                facts["top_performer_context"] = ", ".join(denominators)
            
            # Special handling for top_n=1 queries (e.g., "Which campaign had highest ROAS?")
            # This makes the answer focus on the specific entity rather than overall summary
            if dsl.top_n == 1 and dsl.breakdown:
                facts["query_intent"] = "highest_by_metric"
                facts["breakdown_level"] = dsl.breakdown  # e.g., "campaign"
                facts["metric_display"] = dsl.metric.upper()  # e.g., "ROAS"
        
        return facts
    
    def _extract_providers_facts(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract facts from providers query results.
        
        Args:
            result: Dict with "providers" list
            
        Returns:
            Dict with provider facts for LLM
            
        Example:
            >>> facts = _extract_providers_facts({"providers": ["google", "meta"]})
            >>> facts
            {"platforms": ["Google", "Meta"], "count": 2}
        
        Related:
        - Input: app/dsl/executor.py (providers query result)
        - Used by: build_answer()
        """
        providers = result.get("providers", [])
        
        # Capitalize provider names for display
        formatted_providers = [p.capitalize() for p in providers]
        
        return {
            "platforms": formatted_providers,
            "count": len(formatted_providers)
        }
    
    def _extract_entities_facts(
        self, 
        dsl: MetricQuery, 
        result: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Extract facts from entities query results.
        
        Args:
            dsl: MetricQuery with filters (level, status)
            result: Dict with "entities" list
            
        Returns:
            Dict with entity facts for LLM
            
        Example:
            >>> facts = _extract_entities_facts(dsl, result)
            >>> facts
            {
                "entity_type": "campaigns",
                "status": "active",
                "entity_names": ["Summer Sale", "Winter Promo"],
                "count": 2
            }
        
        Related:
        - Input: app/dsl/executor.py (entities query result)
        - Used by: build_answer()
        """
        entities = result.get("entities", [])
        
        # Determine entity type from filters
        level = dsl.filters.level if dsl.filters and dsl.filters.level else "entities"
        level_plural = level if level.endswith("s") else f"{level}s"
        
        # Extract entity names
        entity_names = [e.get("name") for e in entities if e.get("name")]
        
        facts = {
            "entity_type": level_plural,
            "entity_names": entity_names,
            "count": len(entity_names)
        }
        
        # Add status filter if present
        if dsl.filters and dsl.filters.status:
            facts["status"] = dsl.filters.status
        
        return facts
    
    def _build_system_prompt(self) -> str:
        """
        Build system prompt with strict safety instructions.
        
        WHY strict instructions:
        - Prevent LLM from inventing numbers
        - Ensure only provided facts are used
        - Keep answers conversational but accurate
        
        FORMATTING INSTRUCTIONS:
        - Always prefer *_formatted fields over *_raw fields
        - This prevents GPT from inventing formatting (e.g., "$0" for CPC = 0.48)
        - Formatted fields come from app/answer/formatters.py (single source of truth)
        
        Returns:
            System prompt string
            
        Instructions prioritized by importance:
        1. No number invention (CRITICAL for trust)
        2. Use formatted values when available (prevents formatting errors)
        3. Use only provided facts (prevents hallucinations)
        4. Natural tone (user experience)
        5. Concise (2-3 sentences)
        
        Related:
        - Pattern inspired by: app/nlp/prompts.py (DSL translation prompt)
        - Used by: build_answer()
        """
        return """You are a helpful marketing analytics assistant.

Your job is to rephrase data facts into natural, conversational answers.

CRITICAL RULES:
1. Do NOT invent numbers or make up facts
2. Use ONLY the facts provided in the user message
3. ALWAYS prefer *_formatted fields over *_raw fields (e.g., use "value_formatted" not "value_raw")
4. If a fact is missing or None, gracefully omit it
5. Keep answers concise (2-3 sentences maximum)
6. Sound like a helpful colleague, not a robot
7. Do NOT apply your own formatting - the formatted values are already correct

WHY formatted fields matter:
- They come from our formatting system (currency, ratios, percentages)
- Using raw values causes errors like "$0" when the value is "$0.48"
- Always trust the formatted values

Examples:
- Given: {"metric": "cpc", "value_formatted": "$0.48", "change_formatted": "+15.5%"}
  Answer: "Your CPC is $0.48, up 15.5% from the previous period."
  
- Given: {"metric": "roas", "value_formatted": "2.45×", "top_performer": "Summer Sale"}
  Answer: "Your ROAS is 2.45×, with Summer Sale as the top performer."
  
- Given: {"platforms": ["Google", "Meta"], "count": 2}
  Answer: "You're running ads on Google and Meta."
  
- Given: {"query_intent": "highest_by_metric", "breakdown_level": "campaign", "metric_display": "ROAS", 
           "top_performer": "Summer Sale", "top_performer_value_formatted": "3.20×", "date_range": "Sep 29–Oct 05, 2025"}
  Answer: "Summer Sale had the highest ROAS at 3.20× from Sep 29–Oct 05, 2025."
  
- Given: {"query_intent": "highest_by_metric", "breakdown_level": "provider", "metric_display": "CPC",
           "top_performer": "Google", "top_performer_value_formatted": "$0.32", "date_range": "Oct 01–07, 2025",
           "top_performer_context": "Spend $1,234.56, 3,850 clicks", "value_formatted": "$0.45"}
  Answer: "Google had the best CPC at $0.32 from Oct 01–07, 2025 (Spend $1,234.56, 3,850 clicks). Overall CPC was $0.45."

INTENT-FIRST RULE for "highest_by_metric":
- When query_intent is "highest_by_metric", LEAD with the top_performer and their value
- Include date_range for transparency
- Optionally mention top_performer_context (spend, clicks, etc.) in parentheses
- Optionally mention overall value_formatted as context at the end

Remember: Be helpful and natural, but never invent data or formatting."""
    
    def _build_rich_context_prompt(self, context, dsl: MetricQuery) -> str:
        """
        Build user prompt with rich context (NEW in v2.0.1).
        
        WHY this exists:
        - Provides GPT with all context in organized format
        - Enables natural language generation from deterministic insights
        - Performance level guides tone selection
        
        Args:
            context: RichContext object from context_extractor
            dsl: MetricQuery (for original question if available)
            
        Returns:
            Structured prompt with JSON context + instructions
            
        Example output:
            Generate a natural language answer for this marketing metric query.
            
            CONTEXT:
            {
              "metric_name": "ROAS",
              "metric_value": "2.45×",
              "comparison": {...},
              "workspace_comparison": {...},
              "performance_level": "good"
            }
            
            USER QUESTION: "What's my ROAS this week?"
            
            INSTRUCTIONS: ...
        
        Related:
        - Uses: context.to_dict() from RichContext
        - Used by: build_answer() for metrics queries
        """
        context_json = json.dumps(context.to_dict(), indent=2)
        
        # Try to extract original question if available
        original_question = getattr(dsl, 'question', None) or f"What is my {context.metric_name}?"
        
        return f"""Generate a natural language answer for this marketing metric query.

CONTEXT:
{context_json}

USER QUESTION: "{original_question}"

INSTRUCTIONS:
- Lead with the main metric value and what it means
- If comparison data exists, describe how the metric changed
- If workspace_comparison exists, mention how this compares to average
- If trend data exists, describe the pattern over time
- If top_performer exists, highlight which entity performed best
- If outliers exist, mention notable anomalies
- Match tone to performance_level: {context.performance_level}
  - EXCELLENT/GOOD: Positive, encouraging tone
  - AVERAGE: Neutral, factual tone
  - POOR/CONCERNING: Constructive, problem-solving tone
- Use formatted values (not raw numbers) from the context
- Keep answer concise: 2-4 sentences maximum
- Be conversational but professional
- DO NOT invent any numbers or data not in the context

EXAMPLE TONE FOR PERFORMANCE LEVELS:
- EXCELLENT: "Your ROAS is performing excellently at..."
- GOOD: "Your ROAS is doing well at..."
- AVERAGE: "Your ROAS is stable at..."
- POOR: "Your ROAS has room for improvement at..."
- CONCERNING: "Your ROAS needs attention—it's currently at..."
"""
    
    def _build_user_prompt(self, dsl: MetricQuery, facts: Dict[str, Any]) -> str:
        """
        Build user prompt with extracted facts (legacy for providers/entities).
        
        NOTE: Metrics queries now use _build_rich_context_prompt() (v2.0.1)
        
        Args:
            dsl: MetricQuery (for context)
            facts: Extracted facts dict
            
        Returns:
            User prompt with facts and request
            
        Format:
        - Clear fact presentation
        - Simple request ("rephrase these facts")
        - No ambiguity
        
        Related:
        - Facts from: _extract_*_facts() methods
        - Used by: build_answer() for providers/entities queries
        """
        return f"""Here are the facts about this query:

Query type: {dsl.query_type}
Facts: {facts}

Please rephrase these facts into a natural, helpful answer for a marketer.
Remember: Use only the provided facts, do not invent any numbers."""

