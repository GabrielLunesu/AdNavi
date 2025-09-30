"""
Prompt Engineering Module
==========================

System prompts and few-shot examples for LLM-based DSL translation.

Related files:
- app/nlp/translator.py: Uses these prompts
- app/dsl/examples.md: Human-readable examples documentation
- app/dsl/schema.py: DSL structure being generated

Design principles:
- Keep prompts in code (not external files) for versioning
- Include JSON schema + few-shot examples for best results
- Temperature=0 for deterministic outputs
- Use structured outputs / JSON mode when available
"""

from __future__ import annotations

# Few-shot examples embedded in the prompt
# These are condensed from dsl/examples.md for efficiency
FEW_SHOT_EXAMPLES = [
    {
        "question": "What's my ROAS this week?",
        "dsl": {
            "metric": "roas",
            "time_range": {"last_n_days": 7},
            "compare_to_previous": False,
            "group_by": "none",
            "breakdown": None,
            "top_n": 5,
            "filters": {}
        }
    },
    {
        "question": "How did conversions change vs last month?",
        "dsl": {
            "metric": "conversions",
            "time_range": {"last_n_days": 30},
            "compare_to_previous": True,
            "group_by": "none",
            "breakdown": None,
            "top_n": 5,
            "filters": {}
        }
    },
    {
        "question": "Which campaigns drove the most revenue last week?",
        "dsl": {
            "metric": "revenue",
            "time_range": {"last_n_days": 7},
            "compare_to_previous": False,
            "group_by": "campaign",
            "breakdown": "campaign",
            "top_n": 10,
            "filters": {}
        }
    },
    {
        "question": "What's my Google Ads CPA for the past 14 days?",
        "dsl": {
            "metric": "cpa",
            "time_range": {"last_n_days": 14},
            "compare_to_previous": False,
            "group_by": "none",
            "breakdown": None,
            "top_n": 5,
            "filters": {"provider": "google"}
        }
    },
    {
        "question": "Show me revenue from active campaigns this month",
        "dsl": {
            "metric": "revenue",
            "time_range": {"last_n_days": 30},
            "compare_to_previous": False,
            "group_by": "campaign",
            "breakdown": "campaign",
            "top_n": 5,
            "filters": {"status": "active"}
        }
    },
]


def build_system_prompt() -> str:
    """
    Build the system prompt for DSL translation.
    
    This prompt:
    - Explains the task (translate question → DSL JSON)
    - Provides JSON schema constraints
    - Includes few-shot examples
    - Sets expectations for output format
    
    Returns:
        Complete system prompt string
    """
    return """You are an expert at translating marketing analytics questions into structured JSON queries.

Your job is to convert natural language questions into a specific JSON format (DSL) that our backend uses to fetch metrics.

RULES:
1. Output ONLY valid JSON matching the schema below
2. No explanations, no markdown, no commentary
3. All fields are required unless marked optional
4. Use exact metric names (no variations)
5. Default to last 7 days if time not specified
6. Only set compare_to_previous=true if user asks for comparison/change
7. Set group_by and breakdown to the same value when breaking down data
8. Only include filters if explicitly mentioned

METRICS (choose one):
- spend: Ad spend amount
- revenue: Revenue generated
- clicks: Number of clicks
- impressions: Number of impressions
- conversions: Number of conversions
- roas: Return on ad spend (derived: revenue/spend)
- cpa: Cost per acquisition (derived: spend/conversions)
- cvr: Conversion rate (derived: conversions/clicks)

TIME RANGE (choose one format):
- Relative: {"last_n_days": <number>}  (e.g., 7, 30, 90)
- Absolute: {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"}

FILTERS (optional, only if mentioned):
- provider: "google" | "meta" | "tiktok" | "other" | "mock"
- level: "account" | "campaign" | "adset" | "ad"
- status: "active" | "paused"
- entity_ids: ["uuid1", "uuid2", ...]

JSON SCHEMA:
{
  "metric": string (required),
  "time_range": object (required),
  "compare_to_previous": boolean (default: false),
  "group_by": "none" | "campaign" | "adset" | "ad" (default: "none"),
  "breakdown": "campaign" | "adset" | "ad" | null (default: null),
  "top_n": number (default: 5, range: 1-50),
  "filters": object (default: {})
}

Remember: Output ONLY the JSON object, nothing else."""


def build_few_shot_prompt() -> str:
    """
    Build the few-shot examples section of the prompt.
    
    Returns:
        Few-shot examples formatted for the prompt
    """
    import json
    
    examples_text = "\n\nEXAMPLES:\n"
    for i, example in enumerate(FEW_SHOT_EXAMPLES, 1):
        examples_text += f"\n{i}. Question: \"{example['question']}\"\n"
        examples_text += f"   DSL: {json.dumps(example['dsl'], indent=None)}\n"
    
    return examples_text


def build_full_prompt(question: str) -> str:
    """
    Build the complete prompt for a specific question.
    
    Args:
        question: User's natural language question (canonicalized)
        
    Returns:
        Complete prompt including system instructions + few-shots + question
    """
    system = build_system_prompt()
    examples = build_few_shot_prompt()
    
    return f"""{system}

{examples}

Now translate this question:
"{question}"

Output the JSON DSL:"""


def get_dsl_json_schema() -> dict:
    """
    Export JSON Schema for MetricQuery for structured outputs.
    
    This is used with OpenAI's structured output mode to ensure
    the LLM response conforms to our schema.
    
    Returns:
        JSON Schema dict for MetricQuery
    """
    from app.dsl.schema import MetricQuery
    return MetricQuery.model_json_schema()
