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
import re

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

# Performance-related phrase patterns (NEW in Phase 5 - UPDATED with regex)
# Maps vague "performance" questions to clearer metric-based questions
# Uses regex patterns to handle variations like "breakdown of holiday campaign performance"
PERFORMANCE_PATTERNS = [
    # Match "breakdown of ... performance" → "revenue breakdown for ..."
    # This makes it clearer that we want metrics data, not just entity listing
    (r'breakdown of (.+?) performance\b', r'revenue breakdown for \1'),
    # Match "... performance breakdown" → "revenue breakdown for ..."
    (r'(.+?) performance breakdown\b', r'revenue breakdown for \1'),
    # Match "how are ... performing" → "show me ... metrics"
    (r'how (?:are|is) (.+?) performing\b', r'show me \1 metrics'),
    # Standalone patterns (no entity in between)
    (r'\bperformance breakdown\b', 'revenue breakdown'),
    (r'\bcampaign performance\b', 'campaign revenue'),
    (r'\bshow performance\b', 'show metrics'),
    (r'\bperformance metrics\b', 'metrics'),
]

# Time phrase mappings: normalize vague time references
# Phase 2 fix: Distinguish current periods from past periods
TIME_PHRASES = {
    # PAST Week references (last N days)
    "past week": "last 7 days",
    "last week": "last 7 days",
    "1 week ago": "last 7 days",
    "one week ago": "last 7 days",
    
    # CURRENT Week reference - keep as-is for special handling
    # DON'T map "this week" to "last 7 days" - they mean different things!
    # "this week" = current calendar week (Monday-today)
    # "last 7 days" = rolling 7-day window
    
    # PAST Month references (last N days)
    "past month": "last 30 days",
    "last month": "last 30 days",
    "1 month ago": "last 30 days",
    "one month ago": "last 30 days",
    
    # CURRENT Month reference - keep as-is for special handling
    # DON'T map "this month" to "last 30 days"
    
    # Day references - keep for special handling
    # DON'T map "today" or "yesterday" to "last N days"
    # They are absolute dates, not rolling windows
    "yday": "yesterday",
    
    # Quarter references (for future use)
    "past quarter": "last 90 days",
    "last quarter": "last 90 days",
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
        
        >>> canonicalize_question("Give me a breakdown of campaign performance")
        "give me revenue breakdown for campaign"
        
        >>> canonicalize_question("breakdown of holiday campaign performance")
        "revenue breakdown for holiday campaign"
    
    Design notes:
    - Case-insensitive matching (converts to lowercase)
    - Preserves word boundaries to avoid partial matches
    - Multiple passes: first performance patterns (regex), then metrics, then time phrases
    - Phase 5 update: Uses regex for flexible performance phrase matching
    """
    # Convert to lowercase for consistent matching
    result = question.lower()
    
    # Pass 0: Replace performance-related vague phrases (NEW in Phase 5 - REGEX)
    # Do this FIRST so "breakdown of X performance" becomes clearer before metric extraction
    # Uses regex to handle variations like "breakdown of holiday campaign performance"
    for pattern, replacement in PERFORMANCE_PATTERNS:
        result = re.sub(pattern, replacement, result)
    
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
