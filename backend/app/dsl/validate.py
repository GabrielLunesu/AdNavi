"""
DSL Validation Module
=====================

Validates and repairs DSL queries with helpful error messages.

Related files:
- app/dsl/schema.py: Defines the Pydantic models being validated
- app/nlp/translator.py: Calls this after LLM translation
- app/services/qa_service.py: Uses this in the validation pipeline

Design:
- Phase 1 (MVP): Simple Pydantic validation with clear error messages
- Phase 2: One repair pass by re-asking LLM with the error
- Phase 3: Rule-based fallback for common intents
"""

from __future__ import annotations

from typing import Dict, Any, Optional
from pydantic import ValidationError

from app.dsl.schema import MetricQuery


class DSLValidationError(Exception):
    """
    Raised when a DSL query fails validation.
    
    Attributes:
        message: Human-readable error description
        raw_dict: The invalid DSL dict that failed validation
        pydantic_errors: Original Pydantic validation errors
    """
    def __init__(
        self, 
        message: str, 
        raw_dict: Optional[Dict[str, Any]] = None,
        pydantic_errors: Optional[list] = None
    ):
        super().__init__(message)
        self.message = message
        self.raw_dict = raw_dict
        self.pydantic_errors = pydantic_errors


def validate_dsl(dsl_dict: Dict[str, Any]) -> MetricQuery:
    """
    Validate a DSL dictionary and return a MetricQuery model.
    
    Args:
        dsl_dict: Dictionary representing a metrics query (from LLM or user)
        
    Returns:
        Validated MetricQuery Pydantic model
        
    Raises:
        DSLValidationError: If validation fails with helpful error message
        
    Examples:
        >>> validate_dsl({"metric": "roas", "time_range": {"last_n_days": 7}})
        MetricQuery(metric='roas', time_range=TimeRange(last_n_days=7), ...)
        
        >>> validate_dsl({"metric": "invalid"})
        DSLValidationError: Invalid metric 'invalid'. Must be one of: ...
    
    Design notes:
    - Uses Pydantic's built-in validation
    - Wraps errors in domain-specific exception for better error handling
    - Preserves original error details for debugging and repair
    """
    # Check for empty DSL (critical check before validation)
    # WHY: Catches translation failures early with helpful error message
    if not dsl_dict or dsl_dict == {}:
        raise DSLValidationError(
            message="Translation failed: Empty DSL returned. The question may be too complex or unclear. Please try rephrasing your question.",
            raw_dict=dsl_dict,
            pydantic_errors=None
        )
    
    try:
        return MetricQuery(**dsl_dict)
    except ValidationError as e:
        # Extract user-friendly error messages from Pydantic errors
        error_messages = []
        for error in e.errors():
            field = " → ".join(str(loc) for loc in error["loc"])
            msg = error["msg"]
            error_messages.append(f"{field}: {msg}")
        
        # Build comprehensive error message
        full_message = "DSL validation failed:\n" + "\n".join(f"  • {msg}" for msg in error_messages)
        
        raise DSLValidationError(
            message=full_message,
            raw_dict=dsl_dict,
            pydantic_errors=e.errors()
        )


def validate_or_raise(dsl_dict: Dict[str, Any]) -> MetricQuery:
    """
    Alias for validate_dsl for backward compatibility.
    
    Args:
        dsl_dict: Dictionary representing a metrics query
        
    Returns:
        Validated MetricQuery Pydantic model
        
    Raises:
        DSLValidationError: If validation fails
    """
    return validate_dsl(dsl_dict)


def get_validation_summary(dsl_dict: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate a DSL and return a summary (valid/invalid + errors).
    
    Useful for telemetry and debugging.
    
    Args:
        dsl_dict: Dictionary representing a metrics query
        
    Returns:
        Dictionary with:
            - valid: bool
            - errors: list of error messages (empty if valid)
            - validated_query: MetricQuery if valid, None otherwise
            
    Examples:
        >>> get_validation_summary({"metric": "roas", "time_range": {"last_n_days": 7}})
        {"valid": True, "errors": [], "validated_query": MetricQuery(...)}
        
        >>> get_validation_summary({"metric": "bad"})
        {"valid": False, "errors": ["metric: Input should be ..."], "validated_query": None}
    """
    try:
        validated = validate_dsl(dsl_dict)
        return {
            "valid": True,
            "errors": [],
            "validated_query": validated
        }
    except DSLValidationError as e:
        return {
            "valid": False,
            "errors": [e.message],
            "validated_query": None
        }


# Phase 2 enhancement: Repair logic
# This will be implemented in Phase 5 after the basic pipeline is working
def repair_dsl(
    dsl_dict: Dict[str, Any], 
    error_message: str,
    llm_client=None
) -> Optional[MetricQuery]:
    """
    Attempt to repair an invalid DSL by re-asking the LLM.
    
    THIS IS A PLACEHOLDER FOR PHASE 5.
    
    Args:
        dsl_dict: The invalid DSL dictionary
        error_message: Validation error message
        llm_client: OpenAI client for repair pass
        
    Returns:
        Repaired and validated MetricQuery, or None if repair failed
    """
    # TODO: Implement in Phase 5
    # Strategy:
    # 1. Build repair prompt with original DSL + validation error
    # 2. Ask LLM to fix the error
    # 3. Validate the repaired DSL
    # 4. Return repaired query or None
    return None


# Phase 3 enhancement: Rule-based fallback
# This will be implemented in Phase 5 for common intents
def fallback_dsl(question: str) -> Optional[MetricQuery]:
    """
    Generate a simple DSL using rule-based fallback for basic intents.
    
    THIS IS A PLACEHOLDER FOR PHASE 5.
    
    Args:
        question: Canonicalized question text
        
    Returns:
        Simple MetricQuery for basic intents, or None if no match
        
    Examples:
        "what is my spend" → MetricQuery(metric="spend", time_range={last_n_days: 7})
        "show me revenue" → MetricQuery(metric="revenue", time_range={last_n_days: 7})
    
    Design notes:
    - Only handles simple single-metric questions
    - Uses default time range (last 7 days)
    - No filters or breakdown
    - Serves as last-resort fallback when LLM fails
    """
    # TODO: Implement in Phase 5
    # Strategy:
    # 1. Simple keyword matching for metric names
    # 2. Default to last 7 days
    # 3. No comparison or breakdown
    # 4. Return basic MetricQuery
    return None
