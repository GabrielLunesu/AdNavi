# QA System Architecture & DSL Specification

**Version**: DSL v1.3 (Derived Metrics v1) + Formatters  
**Last Updated**: 2025-10-05  
**Status**: Production Ready

---

## Table of Contents

1. [Overview](#overview)
2. [System Flow Diagram](#system-flow-diagram)
3. [Pipeline Stages](#pipeline-stages-explained)
4. [DSL Specification](#dsl-specification)
5. [Metrics System](#metrics-system-derived-metrics-v1)
6. [Answer Formatting](#answer-formatting)
7. [Security Guarantees](#security-guarantees)
8. [Performance Metrics](#performance-metrics)
9. [File Reference](#file-reference)
10. [Testing](#testing)
11. [Future Enhancements](#future-enhancements)

---

## Overview

The AdNavi QA (Question-Answering) system translates natural language questions into validated database queries using a **DSL (Domain-Specific Language)**.

### Why This Architecture?

**Safety First:**
- LLM outputs JSON DSL (never raw SQL)
- Backend validates and executes (single source of truth)
- Workspace scoping prevents data leaks
- Divide-by-zero guards for derived metrics

**Deterministic & Testable:**
- Clear pipeline: question → DSL → plan → execution → answer
- Each stage is testable independently
- Reproducible results (temperature=0 for LLM)
- Comprehensive unit tests (100+ tests)

**Observable:**
- Every query logged with DSL, latency, validity
- Success/failure metrics tracked
- Error analytics for continuous improvement
- Structured telemetry

---

## System Flow Diagram

```mermaid
graph TD
    Start([User asks question]) --> Router["/qa endpoint<br/>app/routers/qa.py"]
    
    Router --> Service["QA Service<br/>app/services/qa_service.py"]
    
    Service --> Context["Get Context<br/>app/context/context_manager.py<br/><br/>Retrieve last N queries<br/>for follow-up resolution"]
    
    Context --> Canon["Canonicalize<br/>app/dsl/canonicalize.py<br/><br/>Map synonyms:<br/>'return on ad spend' → 'roas'<br/>'this week' → 'last 7 days'"]
    
    Canon --> Translate["Translator<br/>app/nlp/translator.py<br/><br/>LLM: OpenAI GPT-4o-mini<br/>Temperature: 0<br/>Mode: JSON<br/>Context-aware"]
    
    Translate --> Prompt["Build Prompt<br/>app/nlp/prompts.py<br/><br/>System prompt +<br/>Conversation history +<br/>17 few-shot examples +<br/>User question"]
    
    Prompt --> LLM["OpenAI API Call<br/><br/>Returns JSON"]
    
    LLM --> Validate["Validate DSL<br/>app/dsl/validate.py<br/><br/>Pydantic validation<br/>Type checking<br/>Constraints"]
    
    Validate -->|Invalid| Error1["DSLValidationError<br/><br/>Log to telemetry<br/>Return 400"]
    Validate -->|Valid| Plan["Build Plan<br/>app/dsl/planner.py<br/><br/>Resolve dates<br/>Map derived metrics<br/>Plan breakdown"]
    
    Plan --> Execute["Execute Plan<br/>app/dsl/executor.py<br/><br/>Uses metrics/registry<br/>Workspace-scoped<br/>÷0 guards"]
    
    Execute --> Query["Database Queries<br/><br/>1. Summary aggregation<br/>2. Previous period<br/>3. Timeseries (daily)<br/>4. Breakdown (top N)"]
    
    Query --> Result["MetricResult<br/>app/dsl/schema.py<br/><br/>- summary: 2.45<br/>- delta_pct: 0.19<br/>- timeseries: [...]<br/>- breakdown: [...]"]
    
    Result --> Format["Format Values<br/>app/answer/formatters.py<br/><br/>Currency: $0.48<br/>Ratio: 2.45×<br/>Percent: 4.2%"]
    
    Format --> AnswerBuilder["Answer Builder (Hybrid)<br/>app/answer/answer_builder.py<br/><br/>1. Extract facts<br/>2. Format values<br/>3. LLM rephrase"]
    
    AnswerBuilder -->|Success| Answer["Natural Answer<br/><br/>Conversational<br/>Fact-based<br/>LLM-rephrased"]
    AnswerBuilder -->|LLM Fails| Fallback["Template Fallback<br/>app/services/qa_service.py<br/><br/>Uses same formatters<br/>Robotic but safe"]
    
    Answer --> SaveContext["Save to Context<br/>app/context/context_manager.py<br/><br/>Store question + DSL + result<br/>for next follow-up"]
    Fallback --> SaveContext
    
    SaveContext --> Log["Log to Telemetry<br/>app/telemetry/logging.py<br/><br/>Success/failure<br/>Latency<br/>DSL validity"]
    
    Log --> Response["HTTP Response<br/><br/>{<br/>  answer: '...',<br/>  executed_dsl: {...},<br/>  data: {...}<br/>}"]
    
    Error1 --> Log
    
    style Start fill:#e1f5fe
    style Response fill:#c8e6c9
    style Error1 fill:#ffcdd2
    style LLM fill:#fff9c4
    style Query fill:#f3e5f5
    style Service fill:#e3f2fd
    style Format fill:#fff3e0
```

---

## Pipeline Stages Explained

### 1️⃣ **Entry Point** (`app/routers/qa.py`)
- HTTP POST endpoint `/qa`
- Accepts: `{ "question": "What's my ROAS this week?" }`
- Requires: `workspace_id` query param + auth token (JWT cookie)
- Returns: `{ answer, executed_dsl, data, context_used }`

### 2️⃣ **Orchestration** (`app/services/qa_service.py`)
- Main coordinator for the entire pipeline
- Retrieves conversation context for follow-ups
- Saves conversation history after execution
- Handles error propagation and logging
- Measures total latency

### 3️⃣ **Context Retrieval** (`app/context/context_manager.py`)
- **Purpose**: Enable multi-turn conversations and follow-up questions
- **Retrieves**: Last N queries (default 5) for this user+workspace
- **Scoping**: User + workspace isolated (no cross-tenant leaks)
- **Storage**: In-memory (fast, <1ms operations)
- **Thread-safe**: Uses locks for concurrent request safety
- **Examples**:
  - "Show me ROAS by campaign" → "Which one performed best?"
  - "What's my ROAS this week?" → "And yesterday?"

### 4️⃣ **Canonicalization** (`app/dsl/canonicalize.py`)
- **Purpose**: Reduce LLM variance by normalizing inputs
- **Synonym mapping**:
  - `"return on ad spend"` → `"roas"`
  - `"cost per acquisition"` → `"cpa"`
  - `"click-through rate"` → `"ctr"`
  - `"cost per click"` → `"cpc"`
- **Time phrase normalization**:
  - `"this week"` → `"last 7 days"`
  - `"this month"` → `"last 30 days"`
  - `"yesterday"` → `"last 1 day"`

### 5️⃣ **Translation** (`app/nlp/translator.py`)
- **LLM**: OpenAI GPT-4o-mini (cost-effective, fast)
- **Settings**: Temperature=0 (deterministic), JSON mode
- **Input**: Canonicalized question + conversation context
- **Output**: Raw JSON DSL (validated in next step)
- **Context handling**: Includes last 1-2 queries for follow-up resolution
- **Few-shot learning**: 17 examples covering all query types

### 6️⃣ **Prompting** (`app/nlp/prompts.py`)
- **System Prompt**: Task explanation, constraints, schema
- **Few-Shot Examples**: 17 question → DSL pairs
  - 5 original examples (ROAS, conversions, revenue, CPA)
  - 10 new examples (Derived Metrics v1: CPC, CPM, CPL, CPI, CPP, POAS, AOV, ARPV, CTR)
  - 2 non-metrics examples (providers, entities)
- **Follow-up Examples**: 5 examples for context-aware queries
- **Format**: System prompt + examples + context (if available) + user question

### 7️⃣ **Validation** (`app/dsl/validate.py`)
- **Engine**: Pydantic v2
- **Validates**:
  - Query type (metrics, providers, entities)
  - Metric is valid (24 metrics supported)
  - Time range constraints (1-365 days or valid date range)
  - Filters match schema
  - `top_n` is 1-50
- **Errors**: Raises `DSLValidationError` with helpful messages

### 8️⃣ **Planning** (`app/dsl/planner.py`)
- **Resolves**:
  - Relative dates → Absolute dates (`last_n_days: 7` → `2025-09-24 to 2025-09-30`)
  - Derived metrics → Base measures (uses `app/metrics/registry`)
  - Comparison windows (previous period dates)
  - Breakdown requirements
- **Output**: `Plan` object with execution details
- **Optimization**: Returns None for non-metrics queries (handled directly by executor)

### 9️⃣ **Execution** (`app/dsl/executor.py`)
- **Derived Metrics v1 changes**:
  - Uses `compute_metric()` from `app/metrics/registry` (single source of truth)
  - Aggregates ALL base measures (including new ones: leads, installs, purchases, visitors, profit)
  - No local formula duplication
- **Queries**:
  1. **Metrics queries**: Summary, previous period, timeseries, breakdown
  2. **Providers queries**: Distinct ad platforms in workspace
  3. **Entities queries**: List campaigns/adsets/ads with filters
- **Safety**:
  - All queries workspace-scoped (tenant isolation)
  - Divide-by-zero guards in `app/metrics/formulas`
  - SQLAlchemy ORM (no raw SQL, no injection)

### 🔟 **Database Queries**

Example metrics query (workspace-scoped):
```sql
SELECT 
  SUM(spend) as spend,
  SUM(revenue) as revenue,
  SUM(clicks) as clicks,
  SUM(impressions) as impressions,
  SUM(conversions) as conversions,
  -- Derived Metrics v1: New base measures
  SUM(leads) as leads,
  SUM(installs) as installs,
  SUM(purchases) as purchases,
  SUM(visitors) as visitors,
  SUM(profit) as profit
FROM metric_facts mf
JOIN entities e ON e.id = mf.entity_id
WHERE e.workspace_id = :workspace_id
  AND CAST(mf.event_date AS DATE) BETWEEN :start AND :end
```

### 1️⃣1️⃣ **Result Building** (`app/dsl/schema.py`)

**MetricResult** structure:
```json
{
  "summary": 2.45,           // Main metric value
  "previous": 2.06,          // Previous period value
  "delta_pct": 0.189,        // Percentage change (18.9%)
  "timeseries": [            // Daily values (ISO YYYY-MM-DD)
    {"date": "2025-09-24", "value": 2.30},
    {"date": "2025-09-25", "value": 2.45}
  ],
  "breakdown": [             // Top entities
    {"label": "Summer Sale", "value": 3.20},
    {"label": "Winter Campaign", "value": 2.80}
  ]
}
```

### 1️⃣2️⃣ **Value Formatting** (`app/answer/formatters.py`)

**Single source of truth for display formatting** (prevents "$0" bugs):

- **Currency**: `format_metric_value("cpc", 0.4794)` → `"$0.48"`
- **Ratios**: `format_metric_value("roas", 2.456)` → `"2.46×"`
- **Percentages**: `format_metric_value("ctr", 0.042)` → `"4.2%"`
- **Counts**: `format_metric_value("clicks", 1234)` → `"1,234"`
- **Deltas**: `format_delta_pct(0.19)` → `"+19.0%"`

Used by both AnswerBuilder (GPT prompts) and QAService (fallback templates).

### 1️⃣3️⃣ **Answer Generation (Hybrid)** (`app/answer/answer_builder.py`)

**Hybrid approach** (deterministic facts + LLM rephrasing):

**Process:**
1. **Extract facts** deterministically from results
   - Summary value, delta %, top performer
   - No hallucinations possible (validated DB results)

2. **Format values** using shared formatters
   - Currency: CPC = 0.4794 → "$0.48" (prevents "$0" bug)
   - Ratios: ROAS = 2.456 → "2.46×"
   - Percentages: CTR = 0.042 → "4.2%"
   - Counts: clicks = 1234 → "1,234"
   - GPT receives **both raw and formatted** values
   - System prompt: "Always prefer formatted values"

3. **LLM rephrase** with GPT-4o-mini
   - Temperature: 0.3 (natural but controlled)
   - Strict instructions: "Do NOT invent numbers or formatting"
   - Max tokens: 150 (concise, 2-3 sentences)

4. **Fallback** to template if LLM fails
   - Always returns an answer
   - Uses same formatters for consistency
   - Robotic but safe

**Examples:**
- **LLM version**: `"Your CPC is $0.48, up 15.5% from the previous period."`
- **Template fallback**: `"Your CPC for the selected period is $0.48. That's a +15.5% change vs the previous period."`

**Safety:**
- ✅ LLM cannot invent numbers
- ✅ LLM cannot invent formatting
- ✅ Deterministic extraction ensures accuracy
- ✅ Fallback ensures reliability

### 1️⃣4️⃣ **Context Storage** (`app/context/context_manager.py`)
- Saves conversation history for future follow-ups
- Stores: Question + DSL + execution result
- Scope: User + workspace (tenant isolation)
- Retention: Last 5 entries (FIFO eviction)
- Thread-safe for concurrent requests

### 1️⃣5️⃣ **Telemetry** (`app/telemetry/logging.py`)
- Logs every run to `qa_query_logs` table
- Captures: question, DSL, success/failure, latency, errors
- Purpose: Observability, debugging, offline evaluation

### 1️⃣6️⃣ **Response**
```json
{
  "answer": "Your CPC is $0.48, up 15.5% from the previous period.",
  "executed_dsl": {
    "query_type": "metrics",
    "metric": "cpc",
    "time_range": {"last_n_days": 7},
    "compare_to_previous": true,
    "filters": {}
  },
  "data": {
    "summary": 0.4794,
    "previous": 0.4125,
    "delta_pct": 0.162,
    "timeseries": [...],
    "breakdown": [...]
  },
  "context_used": [...]  // Previous queries (for debugging)
}
```

---

## DSL Specification

### Query Types (v1.2)

DSL supports three types of queries:

1. **metrics** (default): Aggregate metrics data
   - Requires: `metric`, `time_range`
   - Example: "What's my ROAS this week?"
   
2. **providers**: List distinct ad platforms
   - Requires: (none, all fields optional)
   - Example: "Which platforms am I advertising on?"
   
3. **entities**: List entities with filters
   - Requires: (none, but filters recommended)
   - Example: "List my active campaigns"

### JSON Schema

```json
{
  "query_type": "metrics" | "providers" | "entities",  // default: "metrics"
  "metric": "spend" | "revenue" | "clicks" | ... | "cpc" | "cpm" | "ctr" | "cvr",
  "time_range": {
    "last_n_days": number,  // 1-365, OR
    "start": "YYYY-MM-DD",
    "end": "YYYY-MM-DD"
  },
  "compare_to_previous": boolean,  // default: false
  "group_by": "none" | "campaign" | "adset" | "ad",  // default: "none"
  "breakdown": "campaign" | "adset" | "ad" | null,  // default: null
  "top_n": number,  // default: 5, range: 1-50
  "filters": {
    "provider": "google" | "meta" | "tiktok" | "other" | null,
    "level": "account" | "campaign" | "adset" | "ad" | null,
    "status": "active" | "paused" | null,
    "entity_ids": [string] | null
  }
}
```

### Validation Rules

1. **Query Type**: Must be "metrics", "providers", or "entities"
2. **Metric**: Required for metrics queries; must be valid metric name
3. **Time Range**: Either `last_n_days` (1-365) OR both `start` and `end`
4. **Dates**: End date must be >= start date
5. **Breakdown**: Must match `group_by` (or group_by must be "none")
6. **Top N**: Between 1 and 50
7. **Filters**: Optional but must use valid enum values

### Query Examples

#### Example 1: Simple Aggregate (Derived Metric)
**Question**: "What was my CPC last week?"

```json
{
  "query_type": "metrics",
  "metric": "cpc",
  "time_range": {"last_n_days": 7},
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "filters": {}
}
```

#### Example 2: Comparison with New Metric
**Question**: "How did my CTR change vs last month?"

```json
{
  "query_type": "metrics",
  "metric": "ctr",
  "time_range": {"last_n_days": 30},
  "compare_to_previous": true,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "filters": {}
}
```

#### Example 3: Breakdown by Campaign
**Question**: "Compare CPM by campaign for the last 7 days"

```json
{
  "query_type": "metrics",
  "metric": "cpm",
  "time_range": {"last_n_days": 7},
  "compare_to_previous": false,
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 10,
  "filters": {}
}
```

#### Example 4: Filtered Query
**Question**: "What's my cost per lead for active campaigns?"

```json
{
  "query_type": "metrics",
  "metric": "cpl",
  "time_range": {"last_n_days": 30},
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "filters": {"status": "active"}
}
```

#### Example 5: Providers Query
**Question**: "Which platforms am I advertising on?"

```json
{
  "query_type": "providers"
}
```

**Response**:
```json
{
  "providers": ["google", "meta", "tiktok"]
}
```

#### Example 6: Entities Query
**Question**: "List my active campaigns"

```json
{
  "query_type": "entities",
  "filters": {"level": "campaign", "status": "active"},
  "top_n": 10
}
```

**Response**:
```json
{
  "entities": [
    {"name": "Holiday Sale - Purchases", "status": "active", "level": "campaign"},
    {"name": "App Install Campaign", "status": "active", "level": "campaign"}
  ]
}
```

---

## Metrics System (Derived Metrics v1)

### Architecture

**Single source of truth for metric formulas:**

```
app/metrics/formulas.py       # Pure functions with ÷0 guards
         ↓
app/metrics/registry.py       # Maps metrics → dependencies → functions
         ↓
    ┌────┴────┐
    ↓         ↓
executor   compute_service   # Both use SAME formulas
```

### Supported Metrics (24 Total)

#### Base Measures (10) - Stored in MetricFact:
- `spend`: Ad spend amount ($)
- `revenue`: Revenue generated ($)
- `clicks`: Number of clicks
- `impressions`: Number of ad impressions
- `conversions`: Number of conversions
- `leads`: Lead form submissions (Meta Lead Ads, Google Lead Forms)
- `installs`: App installations (App Install campaigns)
- `purchases`: Purchase events (ecommerce tracking)
- `visitors`: Landing page visitors (analytics integration)
- `profit`: Net profit (revenue - costs)

#### Derived Metrics (12) - Computed on-demand:

**Cost/Efficiency (6):**
- `cpc`: Cost per Click = spend / clicks
- `cpm`: Cost per Mille = (spend / impressions) × 1000
- `cpa`: Cost per Acquisition = spend / conversions
- `cpl`: Cost per Lead = spend / leads
- `cpi`: Cost per Install = spend / installs
- `cpp`: Cost per Purchase = spend / purchases

**Value (4):**
- `roas`: Return on Ad Spend = revenue / spend
- `poas`: Profit on Ad Spend = profit / spend
- `arpv`: Avg Revenue per Visitor = revenue / visitors
- `aov`: Avg Order Value = revenue / conversions

**Engagement (2):**
- `ctr`: Click-Through Rate = clicks / impressions
- `cvr`: Conversion Rate = conversions / clicks

### Metric Formulas

All formulas include **divide-by-zero guards** (return `None` instead of crash):

```python
def safe_div(numerator, denominator):
    return (numerator / denominator) if (denominator > 0) else None

# Examples:
cpc(spend, clicks) = safe_div(spend, clicks)
roas(revenue, spend) = safe_div(revenue, spend)
ctr(clicks, impressions) = safe_div(clicks, impressions)
```

**Location**: `backend/app/metrics/formulas.py`

### Storage Philosophy

**MetricFact** (source of truth):
- Stores ONLY base measures (raw facts)
- Never stores computed values
- Avoids formula drift over time

**Pnl** (materialized snapshots):
- Stores base + derived metrics
- Fast dashboard queries (no real-time computation)
- "Locked" historical reports
- Can recompute if formulas change

### Campaign Goals

**GoalEnum** (determines relevant metrics):
- `awareness`: Focus on CPM, impressions, reach
- `traffic`: Focus on CPC, CTR, clicks
- `leads`: Focus on CPL, lead volume
- `app_installs`: Focus on CPI, install volume
- `purchases`: Focus on CPP, AOV, purchase volume
- `conversions`: Focus on CPA, CVR, ROAS
- `other`: No specific objective

Used by seed data to generate appropriate base measures.

---

## Answer Formatting

### Single Source of Truth: `app/answer/formatters.py`

**Purpose**: Eliminate formatting bugs (e.g., CPC showing "$0" instead of "$0.48")

### Format Categories

**Currency** ($X,XXX.XX):
- **Metrics**: spend, revenue, profit, cpa, cpl, cpi, cpp, cpc, cpm, aov, arpv
- **Format**: $1,234.56 (2 decimals, thousands separators)
- **Example**: 0.4794 → `"$0.48"`

**Ratios** (X.XX×):
- **Metrics**: roas, poas
- **Format**: 2.45× (2 decimals, × symbol)
- **Example**: 2.456 → `"2.46×"`

**Percentages** (X.X%):
- **Metrics**: ctr, cvr
- **Format**: 4.2% (1 decimal, input is decimal fraction)
- **Example**: 0.042 → `"4.2%"`

**Counts** (X,XXX):
- **Metrics**: clicks, impressions, conversions, leads, installs, purchases, visitors
- **Format**: 12,345 (whole numbers, thousands separators)
- **Example**: 1234 → `"1,234"`

### Integration

**AnswerBuilder (GPT prompts)**:
- Provides both raw and formatted values to GPT
- System prompt: "Always prefer formatted values"
- Prevents GPT from inventing formatting

**QAService (fallback templates)**:
- Uses same formatters
- Consistent with AnswerBuilder
- Formats delta percentages with sign (+/-)

### Edge Cases

✅ None values → `"N/A"`  
✅ Zero values → `"$0.00"`, `"0.00×"`, `"0.0%"`, `"0"`  
✅ Very small values → Rounded appropriately  
✅ Very large values → Thousands separators  
✅ Unknown metrics → 2-decimal fallback  

---

## Security Guarantees

### 🔒 **Workspace Isolation**
All queries scoped at SQL level:
```python
.join(Entity, Entity.id == MetricFact.entity_id)
.filter(Entity.workspace_id == workspace_id)
```
**No cross-workspace data leaks possible.**

### 🔒 **No SQL Injection**
- LLM outputs **JSON** (not SQL)
- JSON validated by **Pydantic**
- Execution uses **SQLAlchemy ORM** (no raw SQL)

### 🔒 **Safe Math**
- All formulas have divide-by-zero guards
- Returns `None` instead of crashing
- Location: `app/metrics/formulas.py`

### 🔒 **Authentication**
- Requires valid JWT token (HTTP-only cookie)
- User context passed to telemetry
- Workspace access verified

### 🔒 **No Exposed Keys**
- All API keys in `.env`
- Settings loaded via `app/deps.get_settings()`
- No hardcoded secrets

---

## Performance Metrics

| Stage | Latency | Notes |
|-------|---------|-------|
| Context Retrieval | <1ms | In-memory lookup |
| Canonicalization | <1ms | String replacements |
| **LLM Translation** | **500-1000ms** | **OpenAI API (DSL)** |
| Validation | 1-5ms | Pydantic validation |
| Planning | <1ms | Pure Python logic |
| Database Query | 10-50ms | Depends on data volume |
| **Answer Generation** | **200-500ms** | **LLM rephrase (hybrid)** |
| Answer Fallback | <1ms | Template-based (if LLM fails) |
| Context Storage | <1ms | In-memory append |
| **Total** | **~700-1550ms** | **End-to-end** |

---

## Hierarchy & Rollup (Breakdowns)

For breakdown queries, the system uses **recursive CTEs** to roll up metrics from leaf entities (ads) to their ancestors (campaigns/adsets). This enables queries like "Which campaign had highest ROAS?" even when facts are stored at the ad level.

### How It Works

1. **Recursive CTE**: Traverses the `parent_id` chain from any entity to its campaign/adset ancestor
2. **Rollup**: Aggregates metrics from all descendant entities
3. **Ordering**: Results ordered by the requested metric value (not just spend)
4. **Top N**: Efficient DB-side limiting after ordering

### Example Query

"Which campaign had the highest ROAS?"

```json
{
  "metric": "roas",
  "time_range": {"last_n_days": 7},
  "breakdown": "campaign",
  "top_n": 1
}
```

Result: "Summer Sale had the highest ROAS at 3.20× during the selected period."

### Technical Details

- **Hierarchy Module**: `app/dsl/hierarchy.py`
- **No schema changes**: Uses existing `parent_id` relationships
- **PostgreSQL optimized**: Uses `DISTINCT ON` for efficiency
- **NULL handling**: `desc().nulls_last()` ensures clean ordering

### Future Optimizations

At scale, consider:
- Denormalized columns: `MetricFact.campaign_id`, `MetricFact.adset_id`
- Materialized views for ancestor mappings
- Application-level hierarchy caching

---

## File Reference

| Component | File | Purpose |
|-----------|------|---------|
| **Entry Point** | `app/routers/qa.py` | HTTP endpoint |
| **Orchestrator** | `app/services/qa_service.py` | Main pipeline coordinator |
| **Context Manager** | `app/context/context_manager.py` | Conversation history |
| **DSL Schema** | `app/dsl/schema.py` | Pydantic models (MetricQuery, MetricResult) |
| **Canonicalization** | `app/dsl/canonicalize.py` | Synonym mapping |
| **Validation** | `app/dsl/validate.py` | DSL validation |
| **Planning** | `app/dsl/planner.py` | Query planning |
| **Execution** | `app/dsl/executor.py` | SQL execution |
| **Hierarchy** | `app/dsl/hierarchy.py` | Entity ancestor resolution (CTEs) |
| **Translation** | `app/nlp/translator.py` | LLM integration (context-aware) |
| **Prompts** | `app/nlp/prompts.py` | System prompts & few-shots |
| **Answer Builder** | `app/answer/answer_builder.py` | Hybrid answer generation |
| **Formatters** | `app/answer/formatters.py` | Display formatting |
| **Metric Formulas** | `app/metrics/formulas.py` | Derived metric computations |
| **Metric Registry** | `app/metrics/registry.py` | Metric → formula mapping |
| **Compute Service** | `app/services/compute_service.py` | P&L snapshots |
| **Telemetry** | `app/telemetry/logging.py` | Structured logging |
| **Models** | `app/models.py` | Database models |

---

## Testing

### Run All Tests
```bash
cd backend
pytest app/tests/ -v
```

### Test Suites

| Suite | File | Coverage |
|-------|------|----------|
| DSL Validation | `test_dsl_validation.py` | Valid/invalid DSL payloads |
| DSL Executor | `test_dsl_executor.py` | Derived metrics, workspace scoping |
| DSL v1.2 | `test_dsl_v12.py` | Providers/entities queries |
| Translator | `test_translator.py` | LLM mocking, schema matching |
| Context Manager | `test_context_manager.py` | Multi-turn conversations (50+ tests) |
| Answer Builder | `test_answer_builder.py` | Hybrid answer generation |
| **Formatters** | `test_formatters.py` | **Display formatting (51 tests)** |
| **Hierarchy** | `test_breakdown_rollup.py` | **Entity rollup & ordering (8 tests)** |

### Test Coverage Summary
- ✅ 100+ total tests
- ✅ Unit tests for each pipeline stage
- ✅ Integration tests for end-to-end flow
- ✅ Thread safety tests for context manager
- ✅ Comprehensive formatter tests

---

## Module Structure

```
backend/app/
├── dsl/                      # Domain-Specific Language
│   ├── __init__.py
│   ├── schema.py            # Pydantic models (MetricQuery, MetricResult)
│   ├── canonicalize.py      # Synonym & time phrase mapping
│   ├── validate.py          # Validation logic
│   ├── planner.py           # DSL → execution plan
│   ├── executor.py          # Plan → SQL → results
│   ├── hierarchy.py         # Entity ancestor resolution (NEW)
│   ├── examples.md          # Few-shot examples (human-readable)
│   └── README.md            # Module guide
│
├── nlp/                      # Natural Language Processing
│   ├── __init__.py
│   ├── translator.py        # LLM → DSL translation
│   └── prompts.py           # System prompts & few-shots
│
├── metrics/                  # Derived Metrics v1 (NEW)
│   ├── __init__.py
│   ├── formulas.py          # Pure functions for derived metrics
│   └── registry.py          # Metric → formula mapping
│
├── answer/                   # Answer Generation
│   ├── __init__.py
│   ├── answer_builder.py    # Hybrid LLM-based builder
│   └── formatters.py        # Display formatting (NEW)
│
├── context/                  # Conversation Context
│   ├── __init__.py
│   └── context_manager.py   # Multi-turn conversation support
│
├── telemetry/                # Observability
│   ├── __init__.py
│   └── logging.py           # Structured QA logging
│
├── services/
│   ├── qa_service.py        # Main QA orchestrator
│   ├── metric_service.py    # Legacy (being phased out)
│   └── compute_service.py   # P&L snapshots (NEW)
│
├── routers/
│   ├── qa.py                # /qa HTTP endpoint
│   └── ...
│
├── tests/                    # Unit & Integration Tests
│   ├── test_dsl_validation.py
│   ├── test_dsl_executor.py
│   ├── test_dsl_v12.py
│   ├── test_translator.py
│   ├── test_context_manager.py
│   ├── test_answer_builder.py
│   ├── test_formatters.py   # NEW: 51 tests
│   └── test_breakdown_rollup.py  # NEW: 8 tests
│
├── models.py                 # Database models
├── schemas.py                # Request/response models
└── state.py                  # Application-level state
```

---

## Future Enhancements

### Phase 5: Validation Repair
- Re-ask LLM with error message for repair
- Rule-based fallback for basic intents
- Smart error recovery

### Phase 6: Evaluation & Testing
- Comprehensive evaluation harness
- Golden output validation
- Continuous accuracy monitoring

### Phase 7: Advanced Features
- Multi-metric queries ("compare ROAS vs CPA")
- Nested breakdowns (campaign → adset → ad)
- Cohort analysis
- Forecasting and trend detection
- Anomaly detection

### Context Enhancements
- Persistent storage (Redis/PostgreSQL)
- Smart context pruning (relevance-based)
- TTL-based expiration
- Cross-session history

### Metrics Enhancements
- Formula versioning (track changes over time)
- Custom derived metrics (user-defined formulas)
- Goal-aware metric recommendations
- Benchmark comparisons (vs industry averages)

---

## Documentation References

- **Main Architecture**: `backend/docs/QA_SYSTEM_ARCHITECTURE.md` (this file)
- **Module Guide**: `backend/app/dsl/README.md`
- **Few-Shot Examples**: `backend/app/dsl/examples.md`
- **Build Log**: `docs/ADNAVI_BUILD_LOG.md`
- **Class Diagram**: `backend/CLASS-DIAGRAM.MD`

---

## Version History

- **v1.4 (2025-10-05)**: Hierarchy-aware Breakdowns
  - Added recursive CTEs for entity ancestor resolution
  - Breakdowns now ordered by requested metric (not just spend)
  - Enhanced answer generation for "which X had highest Y" queries
  - Added 4 new few-shot examples for top_n=1 queries
  
- **v1.3 (2025-10-05)**: Derived Metrics v1 + Formatters
  - Added 12 new derived metrics (CPC, CPM, CPL, CPI, CPP, POAS, ARPV, AOV, CTR, CVR)
  - Added GoalEnum for campaign objectives
  - Added formatters module for consistent display
  - Extended Metric union to 24 metrics
  
- **v1.2 (2025-09-30)**: Multi-query types
  - Added query_type field (metrics, providers, entities)
  - Made metric/time_range optional for non-metrics queries
  
- **v1.1 (2025-09-30)**: Enhanced DSL + Context
  - Added conversation context manager
  - Added hybrid answer builder
  - Proper Pydantic models, canonicalization, validation
  
- **v1.0 (2025-09-30)**: Initial DSL
  - Basic metrics and filters
  - SQLAlchemy execution

---

## Quick Start

### 1. Run Migration
```bash
cd backend
alembic upgrade head
```

### 2. Seed Test Data
```bash
python -m app.seed_mock
```

### 3. Start Backend
```bash
python start_api.py
```

### 4. Test in Swagger UI
Visit: http://localhost:8000/docs

Try the `/qa` endpoint with:
- "What was my CPC last week?"
- "Show me CPL for the lead gen campaign"
- "What's my click-through rate?"
- "Compare ROAS by campaign"

---

## Changelog

### 2025-10-05T16:00:00Z - Hierarchy-aware Breakdowns
- Added `app/dsl/hierarchy.py` (recursive CTEs)
- Updated executor to use hierarchy and order by metric
- Updated AnswerBuilder for top_n=1 special handling
- Added 4 new few-shot examples in prompts
- Created 8 unit tests (test_breakdown_rollup.py)

### 2025-10-05T14:00:00Z - Formatters
- Added `app/answer/formatters.py` (display formatting)
- Updated AnswerBuilder to use formatters
- Updated QAService fallback to use formatters
- Fixed executor timeseries dates (ISO YYYY-MM-DD)
- Created 51 unit tests (100% passing)

### 2025-10-05 - Derived Metrics v1
- Added `app/metrics/` module (formulas, registry)
- Added `app/services/compute_service.py`
- Added GoalEnum + 23 database columns
- Extended DSL to support 24 metrics
- Updated executor to use metrics/registry
- Updated seed data with goal-aware generation

### 2025-10-02 - Context & Answer Builder
- Added conversation context manager
- Added hybrid answer builder (LLM + fallback)
- Added context visibility in API responses

### 2025-09-30 - DSL v1.2
- Added providers and entities query types
- Made metric/time_range optional
- Backward compatible with v1.1

### 2025-09-30 - DSL v1.1
- Enhanced DSL with proper Pydantic models
- Added canonicalization, validation, planning
- Comprehensive test coverage

---

_This is the single source of truth for QA system documentation._  
_For build history and project-wide changes, see: `docs/ADNAVI_BUILD_LOG.md`_

