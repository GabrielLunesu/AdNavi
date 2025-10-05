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
    # Original examples
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
    
    # Derived Metrics v1: New cost/efficiency examples
    {
        "question": "What was my CPC last week?",
        "dsl": {
            "metric": "cpc",
            "time_range": {"last_n_days": 7},
            "compare_to_previous": False,
            "group_by": "none",
            "breakdown": None,
            "top_n": 5,
            "filters": {}
        }
    },
    {
        "question": "Compare CPM by campaign for the last 7 days",
        "dsl": {
            "metric": "cpm",
            "time_range": {"last_n_days": 7},
            "compare_to_previous": False,
            "group_by": "campaign",
            "breakdown": "campaign",
            "top_n": 10,
            "filters": {}
        }
    },
    {
        "question": "Show me cost per lead for my lead gen campaigns",
        "dsl": {
            "metric": "cpl",
            "time_range": {"last_n_days": 30},
            "compare_to_previous": False,
            "group_by": "campaign",
            "breakdown": "campaign",
            "top_n": 5,
            "filters": {"status": "active"}
        }
    },
    {
        "question": "What's my app install cost this month?",
        "dsl": {
            "metric": "cpi",
            "time_range": {"last_n_days": 30},
            "compare_to_previous": False,
            "group_by": "none",
            "breakdown": None,
            "top_n": 5,
            "filters": {}
        }
    },
    {
        "question": "Cost per purchase for Meta ads yesterday",
        "dsl": {
            "metric": "cpp",
            "time_range": {"last_n_days": 1},
            "compare_to_previous": False,
            "group_by": "none",
            "breakdown": None,
            "top_n": 5,
            "filters": {"provider": "meta"}
        }
    },
    
    # Derived Metrics v1: New value metric examples
    {
        "question": "What's my profit on ad spend this month?",
        "dsl": {
            "metric": "poas",
            "time_range": {"last_n_days": 30},
            "compare_to_previous": False,
            "group_by": "none",
            "breakdown": None,
            "top_n": 5,
            "filters": {}
        }
    },
    {
        "question": "Show me average order value for the last 2 weeks",
        "dsl": {
            "metric": "aov",
            "time_range": {"last_n_days": 14},
            "compare_to_previous": False,
            "group_by": "none",
            "breakdown": None,
            "top_n": 5,
            "filters": {}
        }
    },
    {
        "question": "Revenue per visitor by campaign",
        "dsl": {
            "metric": "arpv",
            "time_range": {"last_n_days": 7},
            "compare_to_previous": False,
            "group_by": "campaign",
            "breakdown": "campaign",
            "top_n": 5,
            "filters": {}
        }
    },
    
    # Derived Metrics v1: New engagement metric examples
    {
        "question": "What's my click-through rate this week?",
        "dsl": {
            "metric": "ctr",
            "time_range": {"last_n_days": 7},
            "compare_to_previous": False,
            "group_by": "none",
            "breakdown": None,
            "top_n": 5,
            "filters": {}
        }
    },
    {
        "question": "Compare CTR by campaign last month",
        "dsl": {
            "metric": "ctr",
            "time_range": {"last_n_days": 30},
            "compare_to_previous": False,
            "group_by": "campaign",
            "breakdown": "campaign",
            "top_n": 10,
            "filters": {}
        }
    },
    
    # "Highest by X" queries (top_n=1 with breakdown)
    {
        "question": "Which campaign had highest ROAS?",
        "dsl": {
            "metric": "roas",
            "time_range": {"last_n_days": 7},
            "compare_to_previous": False,
            "group_by": "campaign",
            "breakdown": "campaign",
            "top_n": 1,
            "filters": {}
        }
    },
    {
        "question": "Which ad had the best CPC last month?",
        "dsl": {
            "metric": "cpc",
            "time_range": {"last_n_days": 30},
            "compare_to_previous": False,
            "group_by": "ad",
            "breakdown": "ad",
            "top_n": 1,
            "filters": {}
        }
    },
    {
        "question": "What campaign drove the highest CTR yesterday?",
        "dsl": {
            "metric": "ctr",
            "time_range": {"last_n_days": 1},
            "compare_to_previous": False,
            "group_by": "campaign",
            "breakdown": "campaign",
            "top_n": 1,
            "filters": {}
        }
    },
    {
        "question": "Which active campaign has the lowest CPA?",
        "dsl": {
            "metric": "cpa",
            "time_range": {"last_n_days": 7},
            "compare_to_previous": False,
            "group_by": "campaign",
            "breakdown": "campaign",
            "top_n": 1,
            "filters": {"status": "active"}
        }
    },
    
    # Provider breakdown examples
    {
        "question": "Which platform had the highest ROAS last week?",
        "dsl": {
            "metric": "roas",
            "time_range": {"last_n_days": 7},
            "compare_to_previous": False,
            "group_by": "provider",
            "breakdown": "provider",
            "top_n": 1,
            "filters": {}
        }
    },
    {
        "question": "Compare CPC by platform this month",
        "dsl": {
            "metric": "cpc",
            "time_range": {"last_n_days": 30},
            "compare_to_previous": False,
            "group_by": "provider",
            "breakdown": "provider",
            "top_n": 10,
            "filters": {}
        }
    },
    
    # Threshold examples (filtering out insignificant entities)
    {
        "question": "Which campaign had the highest ROAS this month? Ignore tiny ones.",
        "dsl": {
            "metric": "roas",
            "time_range": {"last_n_days": 30},
            "compare_to_previous": False,
            "group_by": "campaign",
            "breakdown": "campaign",
            "top_n": 1,
            "filters": {},
            "thresholds": {"min_spend": 50.0, "min_conversions": 5}
        }
    },
    {
        "question": "Best performing campaign by CTR with meaningful traffic",
        "dsl": {
            "metric": "ctr",
            "time_range": {"last_n_days": 7},
            "compare_to_previous": False,
            "group_by": "campaign",
            "breakdown": "campaign",
            "top_n": 1,
            "filters": {},
            "thresholds": {"min_clicks": 100}
        }
    },
    
    # Non-metrics queries
    {
        "question": "Which platforms am I running ads on?",
        "dsl": {
            "query_type": "providers"
        }
    },
    {
        "question": "List my active campaigns",
        "dsl": {
            "query_type": "entities",
            "filters": {"level": "campaign", "status": "active"},
            "top_n": 10
        }
    },
]

# Follow-up examples (demonstrating context usage)
# These show how to handle pronouns and implicit references
FOLLOW_UP_EXAMPLES = [
    {
        "context": "Previous: 'How many conversions this week?' → Metric Used: conversions",
        "question": "And the week before?",
        "dsl": {
            "metric": "conversions",  # INHERITED - DO NOT change to different metric!
            "time_range": {"last_n_days": 14},
            "compare_to_previous": False,
            "group_by": "none",
            "breakdown": None,
            "top_n": 5,
            "filters": {}
        }
    },
    {
        "context": "Previous: 'What's my ROAS this week?' → Metric Used: roas",
        "question": "And yesterday?",
        "dsl": {
            "metric": "roas",  # INHERITED from context
            "time_range": {"last_n_days": 1},
            "compare_to_previous": False,
            "group_by": "none",
            "breakdown": None,
            "top_n": 5,
            "filters": {}
        }
    },
    {
        "context": "Previous: 'Which campaigns are live?' → Entity Names: Campaign 1, Campaign 2",
        "question": "Which one performed best?",
        "dsl": {
            "query_type": "metrics",
            "metric": "roas",  # Default performance metric
            "time_range": {"last_n_days": 7},
            "breakdown": "campaign",
            "top_n": 1,  # "which one" + "best" = top 1
            "filters": {"status": "active"}  # inherited from "live"
        }
    },
    {
        "context": "Previous: 'Which campaigns are live?' → First Entity: 'Campaign 1 - Holiday Promotion'",
        "question": "How many conversions did that campaign deliver?",
        "dsl": {
            "metric": "conversions",
            "time_range": {"last_n_days": 7},
            "compare_to_previous": False,
            "group_by": "none",
            "breakdown": None,
            "top_n": 5,
            "filters": {"level": "campaign"}  # filter to campaign level to narrow down
            # Note: We can't filter by entity name in DSL v1.2, but level helps
        }
    },
    {
        "context": "Previous: 'List my campaigns' → Entity Names: Summer Sale, Winter Promo",
        "question": "Give me more details",
        "dsl": {
            "query_type": "entities",
            "filters": {"level": "campaign"},
            "top_n": 10  # Show more entities for details
        }
    },
]


def build_system_prompt() -> str:
    """
    Build the system prompt for DSL translation.
    
    This prompt:
    - Explains the task (translate question → DSL JSON)
    - Provides JSON schema constraints
    - Includes context-awareness instructions (for follow-ups)
    - Includes few-shot examples
    - Sets expectations for output format
    
    Returns:
        Complete system prompt string
    """
    return """You are an expert at translating marketing analytics questions into structured JSON queries.

Your job is to convert natural language questions into a specific JSON format (DSL) that our backend uses to fetch data.

DSL v1.2 supports three types of queries:
1. METRICS: Aggregate metrics data (ROAS, spend, revenue, etc.) — DEFAULT
2. PROVIDERS: List distinct ad platforms in the workspace
3. ENTITIES: List entities (campaigns, adsets, ads) with filters

CONVERSATION CONTEXT (CRITICAL - READ CAREFULLY):
When a CONVERSATION HISTORY section is provided:

1. METRIC INHERITANCE (MOST IMPORTANT):
   - Look at the "Metric Used:" line in the previous question
   - If the current question asks about a TIME PERIOD (yesterday, last week, this month) but doesn't mention a NEW metric
   - YOU MUST USE THE SAME METRIC from the previous question
   - Example: Previous had "Metric Used: conversions", user asks "and the week before?" → USE "conversions" again
   - DO NOT randomly switch metrics (conversions → roas, spend → revenue, etc.)

2. ENTITY REFERENCE:
   - Look for "Top Items:" or "Entity Names:" or "First Entity:" markers in context
   - Questions like "which one?", "that campaign", "it", "them" → reference those entities
   - If user asks "which one performed best?" → use query_type "entities" with top_n=1 and the entity level from context

3. PRONOUNS ("that", "it", "this", "those"):
   - "that campaign" → use the campaign name from "First Entity:" marker
   - "how many X did that deliver?" → apply filters for the entity mentioned in previous context
   - ALWAYS check context before generating a generic query

4. FOLLOW-UP SIGNALS:
   - Questions starting with "and..." → inherit previous metric AND filters
   - "more details" → generate entities query with info from previous context
   - "what about..." → keep metric, change only what's explicitly mentioned

RULES:
1. Output ONLY valid JSON matching the schema below
2. No explanations, no markdown, no commentary
3. Identify the query type from the question intent
4. For metrics queries: metric and time_range are REQUIRED (inherit from context if not explicit)
5. For providers/entities queries: metric and time_range are optional
6. Only set compare_to_previous=true if user asks for comparison/change
7. Set group_by and breakdown to the same value when breaking down data
8. Only include filters if explicitly mentioned
9. For "which/what X had highest Y" questions: Set top_n=1 and appropriate breakdown
10. For "ignore tiny/small", "meaningful", "significant" qualifiers: Add thresholds

QUERY TYPES:
- "metrics": For metric aggregations (ROAS, spend, revenue, etc.) — DEFAULT if not clear
- "providers": For listing ad platforms ("Which platforms?", "What channels?")
- "entities": For listing campaigns/adsets/ads ("List my campaigns", "Show me adsets")

METRICS (for metrics queries):
Base measures (stored):
- spend: Ad spend amount ($)
- revenue: Revenue generated ($)
- clicks: Number of clicks
- impressions: Number of impressions
- conversions: Number of conversions (generic)
- leads: Lead form submissions
- installs: App installations
- purchases: Purchase events
- visitors: Landing page visitors
- profit: Net profit (revenue - costs, $)

Derived metrics (computed):
Cost/Efficiency:
- cpc: Cost per click ($/click)
- cpm: Cost per mille ($/1000 impressions)
- cpa: Cost per acquisition ($/conversion)
- cpl: Cost per lead ($/lead)
- cpi: Cost per install ($/install)
- cpp: Cost per purchase ($/purchase)

Value:
- roas: Return on ad spend (revenue/spend, ratio)
- poas: Profit on ad spend (profit/spend, ratio)
- arpv: Average revenue per visitor ($/visitor)
- aov: Average order value ($/order)

Engagement:
- ctr: Click-through rate (clicks/impressions, %)
- cvr: Conversion rate (conversions/clicks, %)

TIME RANGE (for metrics queries):
- Relative: {"last_n_days": <number>}  (e.g., 7, 30, 90)
- Absolute: {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"}
- Default: {"last_n_days": 7} if not specified

FILTERS (optional, only if mentioned):
- provider: "google" | "meta" | "tiktok" | "other" | "mock"
- level: "account" | "campaign" | "adset" | "ad"  (use for entities queries)
- status: "active" | "paused"
- entity_ids: ["uuid1", "uuid2", ...]

BREAKDOWN DIMENSIONS:
- "provider": Group by platform (google, meta, tiktok)
- "campaign": Group by campaign
- "adset": Group by adset
- "ad": Group by ad

THRESHOLDS (optional, for filtering outliers):
- min_spend: Minimum spend ($) to include in breakdown
- min_clicks: Minimum clicks to include in breakdown
- min_conversions: Minimum conversions to include in breakdown
Use when user says: "ignore tiny/small", "meaningful traffic", "significant volume", etc.

JSON SCHEMA:
{
  "query_type": "metrics" | "providers" | "entities" (default: "metrics"),
  "metric": string (required for metrics, optional otherwise),
  "time_range": object (required for metrics, optional otherwise),
  "compare_to_previous": boolean (default: false),
  "group_by": "none" | "provider" | "campaign" | "adset" | "ad" (default: "none"),
  "breakdown": "provider" | "campaign" | "adset" | "ad" | null (default: null),
  "top_n": number (default: 5, range: 1-50),
  "filters": object (default: {}),
  "thresholds": object (optional, default: null)
}

Remember: Output ONLY the JSON object, nothing else."""


def build_few_shot_prompt(include_followups: bool = False) -> str:
    """
    Build the few-shot examples section of the prompt.
    
    Args:
        include_followups: Whether to include follow-up examples (only when context is provided)
    
    Returns:
        Few-shot examples formatted for the prompt
    """
    import json
    
    examples_text = "\n\nEXAMPLES:\n"
    for i, example in enumerate(FEW_SHOT_EXAMPLES, 1):
        examples_text += f"\n{i}. Question: \"{example['question']}\"\n"
        examples_text += f"   DSL: {json.dumps(example['dsl'], indent=None)}\n"
    
    # Add follow-up examples when context is available
    if include_followups:
        examples_text += "\n\nFOLLOW-UP EXAMPLES (with context):\n"
        for i, example in enumerate(FOLLOW_UP_EXAMPLES, 1):
            examples_text += f"\n{i}. Context: {example['context']}\n"
            examples_text += f"   Question: \"{example['question']}\"\n"
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
