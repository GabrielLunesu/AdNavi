# DSL Module - Domain-Specific Language for Metrics Queries

## Overview

This module provides a safe, validated query language for marketing analytics. It prevents LLMs from generating arbitrary SQL and ensures the backend is the single source of truth for metrics calculations.

## Architecture

```
User Question
    ↓
Canonicalization (synonym mapping)
    ↓
LLM Translation (nlp/translator.py)
    ↓
DSL Validation (validate.py)
    ↓
Query Planning (planner.py)
    ↓
Execution (executor.py)
    ↓
MetricResult
```

## Module Structure

### Core DSL (`dsl/`)

- **`schema.py`**: Pydantic models defining the DSL contract
  - `MetricQuery`: Input query structure
  - `MetricResult`: Output result structure
  - `TimeRange`: Time window specification
  - `Filters`: Optional query filters

- **`canonicalize.py`**: Pre-processing before LLM translation
  - Maps synonyms (e.g., "return on ad spend" → "roas")
  - Normalizes time phrases (e.g., "this week" → "last 7 days")
  - Reduces LLM variance

- **`validate.py`**: Post-processing after LLM translation
  - Pydantic-based validation
  - Clear error messages with DSLValidationError
  - Future: Repair pass and fallback logic

- **`planner.py`**: Converts DSL into execution plans
  - Resolves time ranges (relative → absolute dates)
  - Maps derived metrics to base measures
  - Plans comparison windows and breakdowns

- **`executor.py`**: Executes plans via SQLAlchemy
  - Workspace-scoped queries (tenant safety)
  - Divide-by-zero guards for derived metrics
  - Efficient aggregation with timeseries and breakdown

- **`examples.md`**: Few-shot examples for LLM prompts
  - 12 question → DSL pairs
  - Used in system prompts for consistency

### NLP Translation (`nlp/`)

- **`translator.py`**: LLM-based translation orchestrator
  - OpenAI GPT-4o-mini (cost-effective)
  - Temperature=0 (deterministic)
  - JSON mode (structured output)

- **`prompts.py`**: System prompts and few-shot examples
  - Embedded in code for versioning
  - JSON schema + examples for accuracy

### Telemetry (`telemetry/`)

- **`logging.py`**: Structured logging for QA runs
  - Logs every query (success/failure)
  - Tracks latency, DSL validity, errors
  - Stored in QaQueryLog table

## Usage

### Basic Usage

```python
from app.dsl.schema import MetricQuery, TimeRange
from app.dsl.planner import build_plan
from app.dsl.executor import execute_plan

# Create DSL query
query = MetricQuery(
    metric="roas",
    time_range=TimeRange(last_n_days=7),
    compare_to_previous=True
)

# Plan execution
plan = build_plan(query)

# Execute
result = execute_plan(db, workspace_id="...", plan=plan)

print(result.summary)  # 2.45
print(result.delta_pct)  # 0.19 (19% increase)
```

### Translation from Natural Language

```python
from app.nlp.translator import Translator

translator = Translator()
dsl, latency = translator.to_dsl("What's my ROAS this week?", log_latency=True)

# dsl is a validated MetricQuery
print(dsl.metric)  # "roas"
print(dsl.time_range.last_n_days)  # 7
```

### Full QA Pipeline

```python
from app.services.qa_service_refactored import QAService

service = QAService(db)
result = service.answer(
    question="Which campaigns drove the most revenue?",
    workspace_id="...",
    user_id="..."
)

print(result["answer"])  # Human-readable answer
print(result["executed_dsl"])  # MetricQuery that was executed
print(result["data"])  # MetricResult with breakdown
```

## Supported Metrics

### Base Metrics (directly stored)
- `spend`: Ad spend amount
- `revenue`: Revenue generated
- `clicks`: Number of clicks
- `impressions`: Number of impressions
- `conversions`: Number of conversions

### Derived Metrics (computed)
- `roas`: Return on Ad Spend (revenue / spend)
- `cpa`: Cost per Acquisition (spend / conversions)
- `cvr`: Conversion Rate (conversions / clicks)

## Time Ranges

### Relative (recommended)
```python
TimeRange(last_n_days=7)  # Last 7 days
TimeRange(last_n_days=30)  # Last 30 days
```

### Absolute
```python
TimeRange(
    start=date(2025, 9, 1),
    end=date(2025, 9, 30)
)
```

## Filters

```python
Filters(
    provider="google",  # google, meta, tiktok, other, mock
    level="campaign",   # account, campaign, adset, ad
    status="active",    # active, paused
    entity_ids=["uuid1", "uuid2"]  # Specific entities
)
```

## Security

1. **No SQL Injection**: LLM outputs JSON (not SQL), validated by Pydantic
2. **No Code Execution**: Backend executes validated DSL only
3. **Workspace Scoping**: All queries scoped by workspace_id at SQL level
4. **Safe Math**: Divide-by-zero guards for derived metrics

## Testing

```bash
# Run unit tests
pytest backend/app/tests/test_dsl_validation.py -v
pytest backend/app/tests/test_dsl_executor.py -v
pytest backend/app/tests/test_translator.py -v

# Run with integration tests
pytest backend/app/tests/ -v --integration
```

## Documentation

- **Architecture & DSL Specification**: `backend/docs/QA_SYSTEM_ARCHITECTURE.md` (single source of truth)
- **Few-Shot Examples**: `backend/app/dsl/examples.md`

## Future Enhancements

- **Phase 5**: Validation repair & rule-based fallbacks
- **Phase 6**: Comprehensive evaluation harness
- **Phase 7**: Multi-metric queries, nested breakdowns, forecasting

## Related Files

- `app/services/qa_service_refactored.py`: High-level QA orchestrator
- `app/routers/qa_refactored.py`: HTTP endpoint
- `app/models.py`: QaQueryLog table
- `app/schemas.py`: Request/response models


## Big Picture Roadmap

DSL v1.1–1.2: Basic metrics + structural queries ✅

DSL v1.3 (Phase 4): Hybrid natural answers ✅

DSL v1.4 (Phase 5–6): Context + multi-metric + comparisons ✅

DSL v1.5 (Phase 7): Insights, anomalies, recommendations → “feels like a strategist”

Phase 8: Eval harness + explainability → trust & scale

###########

DSL v1.1 – Metrics Foundation

The first version of the DSL focused entirely on metrics queries. It allowed users to ask simple performance questions like “What was my ROAS last week?” or “How much did I spend yesterday?”. The system translated natural language into a structured query, validated it, and executed safe aggregations in the database. Results included a summary, optional time comparisons, and daily timeseries. While functional, this stage was limited to numeric reporting. Users could not explore campaign structures or platforms, and answers were deterministic but robotic. Still, v1.1 provided a strong foundation: safe tenant isolation, reliable numbers, and a pipeline architecture that could be extended later without rewriting core logic.

DSL v1.2 – Structural Awareness

Version 1.2 introduced structural queries alongside metrics. Users could now ask, “Which platforms am I running ads on?” or “List my active campaigns.” The schema gained a new field, query_type, which let the system distinguish between metrics, providers, and entity queries. The executor branched accordingly, either aggregating facts, listing distinct providers, or fetching entities with filters. This change opened the door to non-numeric insights, giving marketers a sense of “inventory” and campaign scope. With DSL v1.2, the Copilot felt more versatile and useful for day-to-day tasks, not just number crunching. It was the first step toward a holistic assistant rather than a glorified calculator.

DSL v1.3 – Natural Communication

The third version focused on how answers are delivered. Until now, Copilot spoke like a machine, outputting rigid templates. In v1.3, we introduced a hybrid answer builder: deterministic numbers came from the DSL executor, but GPT-5-mini phrased them naturally. For example, instead of “Your ROAS is 2.45”, the assistant might say, “Your ROAS averaged 2.45 this week, which is slightly higher than last week’s 2.1. Campaign A is leading performance.” This balance preserved accuracy (no hallucinated numbers) while creating a conversational, human-like tone. Users began to perceive the system less as a query tool and more as a true marketing assistant.

DSL v1.4 – Multi-Metric & Comparisons

The next evolution is about expressiveness. Version 1.4 extends the schema to handle multiple metrics and cross-dimension comparisons. Marketers will be able to ask questions like “Show me spend, revenue, and ROAS for the last 30 days” or “Compare Google vs Meta CPC this week.” The executor will support multi-metric queries in a single pass and structured outputs for provider- or campaign-level comparisons. The answer builder will summarize insights and, when helpful, include inline tables or charts. This marks a shift from answering single, isolated questions to providing multi-faceted views of performance. At this stage, Copilot becomes not only conversational but also analytically powerful.

DSL v1.5 – Insights & Recommendations

In v1.5, Copilot begins to act as a strategist, not just a reporter. Beyond raw metrics, it will highlight anomalies, explain why performance changed, and suggest next actions. For example, “ROAS dropped 20% last week due to Campaign X’s rising CPC. You might reduce its budget or pause it.” This requires driver analysis in the executor (breaking down deltas into contributors) and heuristic or ML-driven recommendation logic. GPT-5-mini will package these findings into actionable insights. At this stage, the assistant moves closer to decision support, helping marketers not just see what happened, but also understand causes and plan next steps.

DSL v1.6 – Evaluation & Trust

The final planned stage focuses on trust and robustness. A golden set of 100+ benchmark questions will be created and re-run weekly to measure translation accuracy, coverage, and latency. Copilot will also provide “Explain Mode,” showing the executed DSL and raw data tables behind any answer. This transparency ensures users can trust insights, even when phrased naturally by GPT. With rigorous evaluation and explainability features, Copilot will mature into a reliable partner: conversational, analytical, prescriptive, and transparent. DSL v1.6 cements the system as a production-grade AI assistant for marketing analytics.