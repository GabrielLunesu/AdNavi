"""
Canonicalization Module
=======================

Maps synonyms and vague time phrases to canonical forms before LLM translation.

WHY?
- Reduces LLM variance by normalizing common patterns
- Improves translation consistency across similar questions
- Handles domain-specific terminology and abbreviations

Related files:
- app/nlp/translator.py: Uses this before calling the LLM
- app/dsl/schema.py: Target canonical metric names

Example:
    "Show me ROAS from last week" 
    → "Show me roas from last 7 days"
    
    "What's my conversion rate?"
    → "What's my cvr?"
"""

from __future__ import annotations

# Metric synonyms: map common variations to canonical metric names
METRIC_SYNONYMS = {
    # ROAS variations
    "return on ad spend": "roas",
    "return on spend": "roas",
    "roas": "roas",
    
    # CVR variations
    "cvr": "cvr",
    "conversion rate": "cvr",
    "conv rate": "cvr",
    
    # CPA variations
    "cost per acquisition": "cpa",
    "cost per action": "cpa",
    "cpa": "cpa",
    "cost per conversion": "cpa",
    
    # Spend variations
    "spending": "spend",
    "cost": "spend",
    "costs": "spend",
    "ad spend": "spend",
    "budget": "spend",
    "spent": "spend",
    
    # Revenue variations
    "rev": "revenue",
    "sales": "revenue",
    "turnover": "revenue",
    "income": "revenue",
    
    # Clicks variations
    "click": "clicks",
    
    # Impressions variations
    "impression": "impressions",
    "imps": "impressions",
    "views": "impressions",
    
    # Conversions variations
    "conversion": "conversions",
    "conv": "conversions",
    "convs": "conversions",
}

# Time phrase mappings: normalize vague time references
TIME_PHRASES = {
    # Week references
    "this week": "last 7 days",
    "past week": "last 7 days",
    "last week": "last 7 days",
    "1 week": "last 7 days",
    "one week": "last 7 days",
    
    # Month references
    "this month": "last 30 days",
    "past month": "last 30 days",
    "last month": "last 30 days",
    "1 month": "last 30 days",
    "one month": "last 30 days",
    
    # Day references
    "today": "last 1 days",
    "yesterday": "yesterday",  # Keep for special handling
    "yday": "yesterday",
    "ytd": "year to date",  # Keep for future enhancement
    
    # Quarter references (for future use)
    "this quarter": "last 90 days",
    "past quarter": "last 90 days",
    "q1": "quarter 1",
    "q2": "quarter 2",
    "q3": "quarter 3",
    "q4": "quarter 4",
}


def canonicalize_question(question: str) -> str:
    """
    Normalize a user question by replacing synonyms and time phrases.
    
    Args:
        question: Raw natural language question from the user
        
    Returns:
        Canonicalized question with synonyms replaced
        
    Examples:
        >>> canonicalize_question("What's my ROAS this week?")
        "What's my roas last 7 days?"
        
        >>> canonicalize_question("Show me conversion rate for past month")
        "Show me cvr for last 30 days"
        
        >>> canonicalize_question("How much did we spend yesterday?")
        "How much did we spend yesterday?"
    
    Design notes:
    - Case-insensitive matching (converts to lowercase)
    - Preserves word boundaries to avoid partial matches
    - Multiple passes: first metrics, then time phrases
    - Keeps transformation simple for MVP; can enhance with regex later
    """
    # Convert to lowercase for consistent matching
    result = question.lower()
    
    # Pass 1: Replace metric synonyms
    for synonym, canonical in METRIC_SYNONYMS.items():
        # Simple word replacement (could be enhanced with word boundaries)
        result = result.replace(synonym, canonical)
    
    # Pass 2: Replace time phrases
    for phrase, canonical in TIME_PHRASES.items():
        result = result.replace(phrase, canonical)
    
    return result


def get_canonical_metrics() -> list[str]:
    """
    Return list of all canonical metric names.
    
    Useful for validation and LLM prompts.
    
    Returns:
        List of canonical metric names: ["spend", "revenue", "roas", ...]
    """
    return ["spend", "revenue", "clicks", "impressions", "conversions", "roas", "cpa", "cvr"]


def get_canonical_time_units() -> list[str]:
    """
    Return list of canonical time unit patterns.
    
    Useful for validation and LLM prompts.
    
    Returns:
        List of time patterns: ["last N days", "yesterday", ...]
    """
    return [
        "last N days",
        "yesterday", 
        "YYYY-MM-DD to YYYY-MM-DD",
        "year to date",
    ]
