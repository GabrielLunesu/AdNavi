"""
NLP Translator
==============

Converts natural language questions into validated DSL queries using LLMs.

Related files:
- app/nlp/prompts.py: System prompts and few-shot examples
- app/dsl/canonicalize.py: Pre-processing (synonym mapping)
- app/dsl/validate.py: Post-processing (validation)
- app/dsl/schema.py: Target DSL structure
- app/services/qa_service.py: High-level orchestrator

Design:
- Temperature=0 for deterministic outputs
- JSON mode for structured responses
- Canonicalization before LLM call
- Validation after LLM response
- Clear error handling and logging
"""

from __future__ import annotations

import json
import time
from typing import Optional

from openai import OpenAI

from app.dsl.schema import MetricQuery
from app.dsl.canonicalize import canonicalize_question
from app.dsl.validate import validate_dsl, DSLValidationError
from app.nlp.prompts import build_system_prompt, build_few_shot_prompt
from app.deps import get_settings


class TranslationError(Exception):
    """
    Raised when translation fails (LLM error, JSON parse error, etc.).
    
    Attributes:
        message: Human-readable error description
        question: Original user question
        raw_response: Raw LLM response (if available)
    """
    def __init__(self, message: str, question: str = "", raw_response: str = ""):
        super().__init__(message)
        self.message = message
        self.question = question
        self.raw_response = raw_response


class Translator:
    """
    Translates natural language questions into validated MetricQuery DSL.
    
    Usage:
        translator = Translator()
        dsl = translator.to_dsl("What's my ROAS this week?")
        # Returns: MetricQuery(metric="roas", time_range={"last_n_days": 7}, ...)
    
    Design:
    - Uses OpenAI GPT-4o-mini for cost efficiency
    - Temperature=0 for consistency
    - JSON mode for structured outputs
    - Canonicalization reduces LLM variance
    - Validation ensures safety
    
    Related:
    - app/dsl/schema.py: Output type (MetricQuery)
    - app/dsl/canonicalize.py: Pre-processing
    - app/dsl/validate.py: Post-processing
    """
    
    def __init__(self, client: Optional[OpenAI] = None):
        """
        Initialize translator with OpenAI client.
        
        Args:
            client: Optional OpenAI client (for testing/mocking)
                    If None, creates client from settings
        """
        if client is None:
            settings = get_settings()
            if not settings.OPENAI_API_KEY:
                raise ValueError(
                    "OPENAI_API_KEY not configured. "
                    "Set it in your .env file or environment."
                )
            self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        else:
            self.client = client
    
    def to_dsl(
        self, 
        question: str,
        log_latency: bool = False
    ) -> tuple[MetricQuery, Optional[int]]:
        """
        Translate a natural language question into a validated DSL query.
        
        Args:
            question: User's natural language question
            log_latency: Whether to track translation latency
            
        Returns:
            Tuple of (MetricQuery, latency_ms)
            - MetricQuery: Validated DSL query
            - latency_ms: Translation time in milliseconds (None if not logged)
            
        Raises:
            TranslationError: If LLM call fails or returns invalid JSON
            DSLValidationError: If LLM output doesn't match DSL schema
            
        Examples:
            >>> translator = Translator()
            >>> dsl, latency = translator.to_dsl("What's my spend today?")
            >>> print(dsl.metric, dsl.time_range)
            spend TimeRange(last_n_days=1)
        
        Process:
        1. Canonicalize question (map synonyms, normalize time phrases)
        2. Build prompt with system instructions + few-shots + question
        3. Call OpenAI with JSON mode
        4. Parse JSON response
        5. Validate via Pydantic
        6. Return validated MetricQuery
        """
        start_time = time.time() if log_latency else None
        
        # Step 1: Canonicalize to reduce LLM variance
        canonical_question = canonicalize_question(question)
        
        # Step 2: Build prompt
        system_prompt = build_system_prompt()
        few_shots = build_few_shot_prompt()
        user_message = f"{few_shots}\n\nNow translate this question:\n\"{canonical_question}\"\n\nOutput the JSON DSL:"
        
        # Step 3: Call OpenAI
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",  # Cost-effective for structured tasks
                temperature=0,         # Deterministic outputs
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message},
                ],
                response_format={"type": "json_object"}  # Force JSON output
            )
        except Exception as e:
            raise TranslationError(
                message=f"OpenAI API call failed: {str(e)}",
                question=question,
                raw_response=""
            )
        
        # Step 4: Parse JSON
        raw_content = response.choices[0].message.content.strip()
        
        try:
            dsl_dict = json.loads(raw_content)
        except json.JSONDecodeError as e:
            raise TranslationError(
                message=f"Failed to parse JSON from LLM response: {str(e)}",
                question=question,
                raw_response=raw_content
            )
        
        # Step 5: Validate via Pydantic
        # This will raise DSLValidationError if invalid
        validated_dsl = validate_dsl(dsl_dict)
        
        # Step 6: Calculate latency if requested
        latency_ms = None
        if log_latency and start_time is not None:
            latency_ms = int((time.time() - start_time) * 1000)
        
        return validated_dsl, latency_ms
    
    def to_dsl_simple(self, question: str) -> MetricQuery:
        """
        Simplified interface that returns just the DSL (no latency).
        
        Args:
            question: User's natural language question
            
        Returns:
            Validated MetricQuery
            
        Raises:
            TranslationError: If translation fails
            DSLValidationError: If validation fails
        """
        dsl, _ = self.to_dsl(question, log_latency=False)
        return dsl
