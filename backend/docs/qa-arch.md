# QA System Architecture

## Overview

The AdNavi QA (Question-Answering) system translates natural language questions into validated database queries using a DSL (Domain-Specific Language).

## Why This Architecture?

### Safety First
- LLM only outputs JSON DSL (never raw SQL)
- Backend validates and executes (single source of truth)
- Workspace scoping prevents data leaks
- Divide-by-zero guards for derived metrics

### Deterministic & Testable
- Clear pipeline: question → DSL → plan → execution → answer
- Each stage is testable independently
- Reproducible results (temperature=0 for LLM)
- Table-driven tests with golden outputs

### Observable
- Every query logged with DSL, latency, validity
- Success/failure metrics tracked
- Error analytics for continuous improvement
- Offline evaluation harness

## System Dataflow

```
┌─────────────┐
│   User      │
│  Question   │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────────┐
│  Canonicalizer                      │
│  (synonym mapping, time phrases)    │
└──────┬──────────────────────────────┘
       │ "What's my roas last 7 days?"
       ▼
┌─────────────────────────────────────┐
│  Translator (LLM)                   │
│  - OpenAI GPT-4o-mini               │
│  - Temperature=0 (deterministic)    │
│  - JSON mode (structured output)    │
│  - Few-shot examples                │
└──────┬──────────────────────────────┘
       │ Raw JSON
       ▼
┌─────────────────────────────────────┐
│  Validator (Pydantic)               │
│  - Schema matching                  │
│  - Type checking                    │
│  - Constraint validation            │
└──────┬──────────────────────────────┘
       │ MetricQuery (validated)
       ▼
┌─────────────────────────────────────┐
│  Planner                            │
│  - Resolve time range               │
│  - Map derived metrics → base       │
│  - Build execution plan             │
└──────┬──────────────────────────────┘
       │ Plan (dates, measures, flags)
       ▼
┌─────────────────────────────────────┐
│  Executor (SQLAlchemy)              │
│  - Workspace-scoped queries         │
│  - Safe aggregation                 │
│  - Derived metric computation       │
│  - Timeseries & breakdown           │
└──────┬──────────────────────────────┘
       │ MetricResult
       ▼
┌─────────────────────────────────────┐
│  Answer Generator                   │
│  - Template-based (deterministic)   │
│  - Includes comparison delta        │
│  - Mentions top performer           │
└──────┬──────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────┐
│  Telemetry Logger                   │
│  - Log to QaQueryLog table          │
│  - Track success/failure            │
│  - Record latency                   │
│  - Store DSL for analysis           │
└─────────────────────────────────────┘
       │
       ▼
┌─────────────┐
│  Response   │
│  {answer,   │
│   dsl,      │
│   data}     │
└─────────────┘
```

## Module Structure

```
backend/app/
├── dsl/                     # Domain-Specific Language
│   ├── __init__.py
│   ├── schema.py           # Pydantic models (MetricQuery, MetricResult)
│   ├── canonicalize.py     # Synonym & time phrase mapping
│   ├── validate.py         # Validation & repair logic
│   ├── planner.py          # DSL → execution plan
│   ├── executor.py         # Plan → SQL → results
│   └── examples.md         # Few-shot examples
│
├── nlp/                     # Natural Language Processing
│   ├── __init__.py
│   ├── translator.py       # LLM → DSL translation
│   └── prompts.py          # System prompts & few-shots
│
├── telemetry/               # Observability
│   ├── __init__.py
│   ├── logging.py          # Structured QA logging
│   └── eval.py             # Offline evaluation (Phase 6)
│
├── services/
│   ├── qa_service_refactored.py  # High-level orchestrator
│   └── metric_service.py         # Legacy (being phased out)
│
├── routers/
│   └── qa_refactored.py    # HTTP endpoint
│
├── models.py                # QaQueryLog table
└── schemas.py               # Request/response models
```

## Key Components

### 1. Canonicalizer (`dsl/canonicalize.py`)
- Maps synonyms: "return on ad spend" → "roas"
- Normalizes time: "this week" → "last 7 days"
- Reduces LLM variance

### 2. Translator (`nlp/translator.py`)
- Uses OpenAI GPT-4o-mini (cost-effective)
- Temperature=0 for deterministic outputs
- JSON mode for structured responses
- Few-shot examples for accuracy

### 3. Validator (`dsl/validate.py`)
- Pydantic-based validation
- Clear error messages
- Future: Repair pass (Phase 5)
- Future: Rule-based fallback (Phase 5)

### 4. Planner (`dsl/planner.py`)
- Resolves relative time → absolute dates
- Maps derived metrics → base measures
- Plans comparison windows
- Plans timeseries & breakdown

### 5. Executor (`dsl/executor.py`)
- Workspace-scoped queries (tenant safety)
- SQLAlchemy ORM (no raw SQL)
- Divide-by-zero guards
- Efficient aggregation

### 6. Telemetry (`telemetry/logging.py`)
- Logs every QA run
- Tracks success/failure rates
- Records latency
- Enables offline evaluation

## Workspace Scoping

**All queries are tenant-scoped** to prevent data leaks:

```python
# Every query starts with:
.join(Entity, Entity.id == MetricFact.entity_id)
.filter(Entity.workspace_id == workspace_id)
```

This is enforced at the SQL level, not application level.

## Security Guarantees

1. **No SQL Injection**: LLM outputs JSON (not SQL), validated by Pydantic
2. **No Code Execution**: Backend executes validated DSL (not raw text)
3. **Workspace Isolation**: All queries scoped by workspace_id
4. **Safe Math**: Divide-by-zero guards for derived metrics
5. **Auth Required**: HTTP endpoint requires valid JWT token

## Error Handling

### Translation Errors
- LLM API failure
- Invalid JSON response
- Unrecognized metric/time phrase

**Strategy**: Log error, return 400 with helpful message

### Validation Errors
- DSL doesn't match schema
- Invalid metric name
- Invalid date range

**Strategy**: Log error, return 400 with validation details

### Execution Errors
- Database query failure
- Missing data
- Divide by zero (handled gracefully)

**Strategy**: Log error, return 400 or None for missing data

## Performance

### Latency Breakdown
- Translation (LLM): ~500-1000ms
- Validation (Pydantic): ~1-5ms
- Planning: <1ms
- Execution (SQL): ~10-50ms (depends on data volume)
- **Total**: ~500-1050ms

### Optimization Strategies
- Cache common queries (Phase 7)
- Pre-compute derived metrics (Phase 7)
- Use faster LLM (gpt-4o-mini already optimized)
- Index database properly (event_date, workspace_id)

## Testing Strategy

### Unit Tests
- `test_dsl_validation.py`: Valid/invalid DSL payloads
- `test_dsl_executor.py`: Seed data → expected sums
- `test_translator.py`: Mock LLM, verify schema matching

### Integration Tests
- End-to-end: question → answer
- Workspace scoping verification
- Error handling paths

### Evaluation Harness
- CSV of (question, expected metric, expected window)
- Run offline, compute pass rate
- Identify common failure patterns

## Observability

### Metrics Tracked
- Total queries (per workspace, per day)
- Success rate (%)
- Average latency (ms)
- Common error messages

### Logs Captured
- Question text
- Translated DSL
- Validation status
- Execution time
- Error messages (if any)

### Analysis Tools
- `get_qa_stats()` in telemetry/logging.py
- QaQueryLog table for historical analysis
- Future: Grafana dashboard

## Future Enhancements

### Phase 5: Validation Repair
- Repair pass: re-ask LLM with error message
- Rule-based fallback for basic intents

### Phase 6: Tests & Eval
- Comprehensive test suite
- Offline evaluation harness
- Golden output validation

### Phase 7: Advanced Features
- Multi-metric queries
- Nested breakdowns
- Cohort analysis
- Forecasting
- Anomaly detection

## References

- DSL Spec: `docs/dsl-spec.md`
- Examples: `backend/app/dsl/examples.md`
- Build Log: `docs/ADNAVI_BUILD_LOG.md`
