# DSL Specification v1.2

## Overview

The AdNavi DSL (Domain-Specific Language) is a JSON-based query language for marketing analytics. It provides a safe, validated way to query data without exposing SQL or database internals.

**DSL v1.2** extends the original metrics-only DSL to support structural queries:
- **Metrics queries**: Aggregate metrics data (ROAS, spend, revenue, etc.)
- **Providers queries**: List distinct ad platforms in workspace
- **Entities queries**: List entities (campaigns, adsets, ads) with filters

## Why DSL?

1. **Safety**: Prevents SQL injection and arbitrary code execution
2. **Validation**: Pydantic models ensure type safety and constraints
3. **Consistency**: Single source of truth for metrics calculations
4. **Observability**: All queries are logged and traceable
5. **LLM-Friendly**: Structured output format for AI translation

## Core Concepts

### Metrics

Metrics are either **base** (directly stored) or **derived** (computed from base metrics).

**Base Metrics:**
- `spend`: Ad spend amount ($)
- `revenue`: Revenue generated ($)
- `clicks`: Number of clicks
- `impressions`: Number of ad impressions
- `conversions`: Number of conversions

**Derived Metrics:**
- `roas`: Return on Ad Spend (revenue / spend)
- `cpa`: Cost per Acquisition (spend / conversions)
- `cvr`: Conversion Rate (conversions / clicks)

### Time Ranges

Time ranges can be specified in two ways:

1. **Relative** (recommended for most cases):
   ```json
   {"last_n_days": 7}
   ```

2. **Absolute** (for specific date ranges):
   ```json
   {"start": "2025-09-01", "end": "2025-09-30"}
   ```

### Filters

Optional filters to scope queries:

- `provider`: Ad platform (google, meta, tiktok, other, mock)
- `level`: Entity level (account, campaign, adset, ad)
- `status`: Entity status (active, paused)
- `entity_ids`: Specific entity UUIDs

All filters are ANDed together.

### Breakdowns

Break down results by dimension to identify top performers:

- `campaign`: Break down by campaign
- `adset`: Break down by ad set
- `ad`: Break down by individual ad

The `top_n` parameter controls how many items to return (default: 5, max: 50).

## JSON Schema

```json
{
  "metric": "spend" | "revenue" | "clicks" | "impressions" | "conversions" | "roas" | "cpa" | "cvr",
  "time_range": {
    "last_n_days": number,  // OR
    "start": "YYYY-MM-DD",
    "end": "YYYY-MM-DD"
  },
  "compare_to_previous": boolean,  // default: false
  "group_by": "none" | "campaign" | "adset" | "ad",  // default: "none"
  "breakdown": "campaign" | "adset" | "ad" | null,  // default: null
  "top_n": number,  // default: 5, range: 1-50
  "filters": {
    "provider": string | null,
    "level": string | null,
    "status": "active" | "paused" | null,
    "entity_ids": [string] | null
  }
}
```

## Examples

### Example 1: Simple Aggregate

**Question**: "What's my ROAS this week?"

```json
{
  "metric": "roas",
  "time_range": {"last_n_days": 7},
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "filters": {}
}
```

### Example 2: Comparison

**Question**: "How did conversions change vs last month?"

```json
{
  "metric": "conversions",
  "time_range": {"last_n_days": 30},
  "compare_to_previous": true,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "filters": {}
}
```

### Example 3: Breakdown

**Question**: "Which campaigns drove the most revenue?"

```json
{
  "metric": "revenue",
  "time_range": {"last_n_days": 7},
  "compare_to_previous": false,
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 10,
  "filters": {}
}
```

### Example 4: Filtered Query

**Question**: "What's my Google Ads CPA for active campaigns?"

```json
{
  "metric": "cpa",
  "time_range": {"last_n_days": 14},
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "filters": {
    "provider": "google",
    "status": "active"
  }
}
```

## Response Format

The executor returns a `MetricResult` with:

```json
{
  "summary": 2.45,           // Main metric value
  "previous": 2.10,          // Previous period value (if compare_to_previous=true)
  "delta_pct": 0.167,        // Percentage change (16.7%)
  "timeseries": [            // Daily values
    {"date": "2025-09-24", "value": 2.30},
    {"date": "2025-09-25", "value": 2.45},
    ...
  ],
  "breakdown": [             // Top items (if breakdown specified)
    {"label": "Summer Sale", "value": 3.20},
    {"label": "Winter Campaign", "value": 2.80},
    ...
  ]
}
```

## Validation Rules

1. **Metric**: Must be one of the valid metric names
2. **Time Range**: Either `last_n_days` (1-365) OR both `start` and `end`
3. **Dates**: End date must be >= start date
4. **Breakdown**: Must match `group_by` (or group_by must be "none")
5. **Top N**: Between 1 and 50
6. **Filters**: Optional but must use valid enum values

## Derived Metric Calculations

### ROAS (Return on Ad Spend)
```
ROAS = revenue / spend
Returns None if spend = 0
```

### CPA (Cost per Acquisition)
```
CPA = spend / conversions
Returns None if conversions = 0
```

### CVR (Conversion Rate)
```
CVR = conversions / clicks
Returns None if clicks = 0
```

## Workspace Scoping

**All queries are automatically scoped to a workspace.**

The executor enforces this at the SQL level:
```sql
JOIN entities ON entities.id = metric_facts.entity_id
WHERE entities.workspace_id = :workspace_id
```

This prevents cross-workspace data leaks.

## Future Enhancements

- Support for custom date ranges (quarters, fiscal years)
- Multi-metric queries (compare ROAS vs CPA)
- Nested breakdowns (campaign → adset → ad)
- Cohort analysis
- Forecasting and trend detection

## DSL v1.2 Extensions

### Query Types

DSL v1.2 introduces the `query_type` field to support three types of queries:

1. **metrics** (default): Aggregate metrics data
   - Requires: `metric`, `time_range`
   - Example: "What's my ROAS this week?"
   
2. **providers**: List distinct ad platforms
   - Requires: (none, all fields optional)
   - Example: "Which platforms am I advertising on?"
   
3. **entities**: List entities with filters
   - Requires: (none, but filters recommended)
   - Example: "List my active campaigns"

### Providers Queries

Providers queries return a list of distinct ad platforms (providers) configured in the workspace.

**Example Query:**
```json
{
  "query_type": "providers"
}
```

**Example Response:**
```json
{
  "providers": ["google", "meta", "tiktok"]
}
```

**Use Cases:**
- "Which platforms am I advertising on?"
- "What ad channels do I have?"
- "List my providers"

### Entities Queries

Entities queries return a list of entities (campaigns, adsets, ads) with optional filters.

**Example Query:**
```json
{
  "query_type": "entities",
  "filters": {
    "level": "campaign",
    "status": "active"
  },
  "top_n": 10
}
```

**Example Response:**
```json
{
  "entities": [
    {"name": "Summer Sale", "status": "active", "level": "campaign"},
    {"name": "Winter Promo", "status": "active", "level": "campaign"}
  ]
}
```

**Use Cases:**
- "List my active campaigns"
- "Show me all adsets"
- "What campaigns do I have?"

**Filters:**
- `level`: Filter by entity type (campaign, adset, ad)
- `status`: Filter by entity status (active, paused)
- `entity_ids`: Filter by specific UUIDs

**Limit:**
- `top_n`: Controls how many entities to return (default: 5, max: 50)

### Backward Compatibility

DSL v1.2 is fully backward compatible with v1.1:
- Existing metrics queries work unchanged
- `query_type` defaults to `"metrics"` if not specified
- All v1.1 fields and behaviors preserved

## Version History

- **v1.2** (2025-09-30): Added query_type field for providers and entities queries; made metric/time_range optional
- **v1.1** (2025-09-30): Enhanced DSL with proper Pydantic models, canonicalization, validation
- **v1.0** (2025-09-30): Initial DSL with basic metrics and filters
