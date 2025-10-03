# QA System Architecture - DSL v1.2 + Hybrid Answer Builder + Conversation Context (DSL v1.5)

## System Flow Diagram

```mermaid
graph TD
    Start([User asks question]) --> Router["/qa endpoint<br/>app/routers/qa.py"]
    
    Router --> Service["QA Service<br/>app/services/qa_service.py"]
    
    Service --> Context["Get Context<br/>app/context/context_manager.py<br/><br/>Retrieve last N queries<br/>for follow-up resolution"]
    
    Context --> Canon["Canonicalize<br/>app/dsl/canonicalize.py<br/><br/>Map synonyms:<br/>'return on ad spend' → 'roas'<br/>'this week' → 'last 7 days'"]
    
    Canon --> Translate["Translator<br/>app/nlp/translator.py<br/><br/>LLM: OpenAI GPT-4o-mini<br/>Temperature: 0<br/>Mode: JSON<br/>Context-aware"]
    
    Translate --> Prompt["Build Prompt<br/>app/nlp/prompts.py<br/><br/>System prompt +<br/>Conversation history +<br/>12 few-shot examples +<br/>User question"]
    
    Prompt --> LLM["OpenAI API Call<br/><br/>Returns JSON"]
    
    LLM --> Validate["Validate DSL<br/>app/dsl/validate.py<br/><br/>Pydantic validation<br/>Type checking<br/>Constraints"]
    
    Validate -->|Invalid| Error1["DSLValidationError<br/><br/>Log to telemetry<br/>Return 400"]
    Validate -->|Valid| Plan["Build Plan<br/>app/dsl/planner.py<br/><br/>Resolve dates<br/>Map derived metrics<br/>Plan breakdown"]
    
    Plan --> Execute["Execute Plan<br/>app/dsl/executor.py<br/><br/>SQLAlchemy queries<br/>Workspace-scoped<br/>÷0 guards"]
    
    Execute --> Query["Database Queries<br/><br/>1. Summary aggregation<br/>2. Previous period (if requested)<br/>3. Timeseries (daily)<br/>4. Breakdown (top N)"]
    
    Query --> Result["MetricResult<br/>app/dsl/schema.py<br/><br/>- summary: 2.45<br/>- delta_pct: 0.19<br/>- timeseries: [...]<br/>- breakdown: [...]"]
    
    Result --> AnswerBuilder["Answer Builder (Hybrid)<br/>app/answer/answer_builder.py<br/><br/>1. Extract facts (deterministic)<br/>2. LLM rephrase (GPT-4o-mini)<br/>Safety: No number invention"]
    
    AnswerBuilder -->|Success| Answer["Natural Answer<br/><br/>Conversational<br/>Fact-based<br/>LLM-rephrased"]
    AnswerBuilder -->|LLM Fails| Fallback["Template Fallback<br/>app/services/qa_service.py<br/><br/>Robotic but safe<br/>Always works"]
    
    Answer --> SaveContext["Save to Context<br/>app/context/context_manager.py<br/><br/>Store question + DSL + result<br/>for next follow-up"]
    Fallback --> SaveContext
    
    SaveContext --> Log["Log to Telemetry<br/>app/telemetry/logging.py<br/><br/>Success/failure<br/>Latency (total + answer)<br/>DSL validity<br/>Errors"]
    
    Log --> Response["HTTP Response<br/><br/>{<br/>  answer: '...',<br/>  executed_dsl: {...},<br/>  data: {...}<br/>}"]
    
    Error1 --> Log
    
    style Start fill:#e1f5fe
    style Response fill:#c8e6c9
    style Error1 fill:#ffcdd2
    style LLM fill:#fff9c4
    style Query fill:#f3e5f5
    style Service fill:#e3f2fd
```

## Pipeline Stages Explained

### 1️⃣ **Entry Point** (`app/routers/qa.py`)
- HTTP POST endpoint `/qa`
- Accepts: `{ "question": "What's my ROAS this week?" }`
- Requires: `workspace_id` query param + auth token
- Returns: `{ answer, executed_dsl, data }`

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
- **Storage**: In-memory (fast, no database overhead)
- **Examples**:
  - User asks "Show me ROAS by campaign"
  - User follows up with "Which one performed best?"
  - Context manager provides previous query+results to translator

### 4️⃣ **Canonicalization** (`app/dsl/canonicalize.py`)
- **Purpose**: Reduce LLM variance by normalizing inputs
- **Transforms**:
  - `"return on ad spend"` → `"roas"`
  - `"this week"` → `"last 7 days"`
  - `"conversion rate"` → `"cvr"`
  - `"cost per acquisition"` → `"cpa"`

### 5️⃣ **Translation** (`app/nlp/translator.py`)
- **LLM**: OpenAI GPT-4o-mini (cost-effective)
- **Settings**: Temperature=0 (deterministic), JSON mode
- **Input**: Canonicalized question + conversation context (NEW)
- **Output**: Raw JSON DSL
- **Context handling**: Includes last 1-2 queries to resolve follow-ups

### 6️⃣ **Prompting** (`app/nlp/prompts.py`)
- **System Prompt**: Explains task, constraints, schema
- **Few-Shot Examples**: 12 question → DSL pairs
- **Format**: System prompt + examples + user question
- **Goal**: Guide LLM to output valid DSL

### 7️⃣ **Validation** (`app/dsl/validate.py`)
- **Engine**: Pydantic v2
- **Validates**:
  - Metric is valid (`roas`, `cpa`, `cvr`, etc.)
  - Time range is valid (dates, constraints)
  - Filters match schema
  - `top_n` is 1-50
- **Errors**: Raises `DSLValidationError` with helpful messages

### 8️⃣ **Planning** (`app/dsl/planner.py`)
- **Resolves**:
  - Relative dates → Absolute dates (`last_n_days: 7` → `2025-09-24 to 2025-09-30`)
  - Derived metrics → Base measures (`roas` → `["spend", "revenue"]`)
  - Comparison windows (previous period dates)
- **Output**: `Plan` object with all execution details

### 9️⃣ **Execution** (`app/dsl/executor.py`)
- **Queries**:
  1. **Summary**: Main aggregation for the metric
  2. **Previous**: Previous period (if `compare_to_previous=true`)
  3. **Timeseries**: Daily values for the period
  4. **Breakdown**: Top N entities by dimension
- **Safety**:
  - All queries workspace-scoped (tenant isolation)
  - Divide-by-zero guards for derived metrics
  - SQLAlchemy ORM (no raw SQL)

### 🔟 **Database Queries**
```sql
-- Example summary query (workspace-scoped)
SELECT 
  SUM(spend) as spend,
  SUM(revenue) as revenue
FROM metric_facts mf
JOIN entities e ON e.id = mf.entity_id
WHERE e.workspace_id = :workspace_id
  AND mf.event_date BETWEEN :start AND :end
```

### 1️⃣1️⃣ **Result Building** (`app/dsl/schema.py`)
- **MetricResult** structure:
  - `summary`: Main metric value (e.g., 2.45 for ROAS)
  - `previous`: Previous period value
  - `delta_pct`: Percentage change (0.19 = +19%)
  - `timeseries`: Daily values `[{date, value}, ...]`
  - `breakdown`: Top entities `[{label, value}, ...]`

### 1️⃣2️⃣ **Answer Generation (Hybrid)** (`app/answer/answer_builder.py`)
- **Hybrid approach** (deterministic facts + LLM rephrasing)
- **Process**:
  1. **Extract facts** deterministically from results
     - Summary value, delta %, top performer
     - No hallucinations possible (comes from validated DB results)
  2. **LLM rephrase** with GPT-4o-mini
     - Temperature: 0.3 (natural but controlled)
     - Strict instructions: "Do NOT invent numbers"
     - Max tokens: 150 (concise answers)
  3. **Fallback** to template if LLM fails
     - Always returns an answer
     - Fallback is robotic but safe
- **Examples**:
  - **LLM version**: `"Your ROAS is 2.45, up 19% from the previous period. Great performance!"`
  - **Template fallback**: `"Your ROAS for the selected period is 2.45. That's a +19.0% change vs the previous period."`
- **Safety**:
  - LLM cannot invent numbers (only rephrases provided facts)
  - Deterministic extraction ensures accuracy
  - Fallback ensures reliability

### 1️⃣3️⃣ **Context Storage** (`app/context/context_manager.py`)
- **Purpose**: Save conversation history for future follow-ups
- **Stores**: Question + DSL + execution result
- **Scope**: User + workspace (tenant isolation)
- **Retention**: Last N entries (default 5, FIFO eviction)
- **Examples**:
  - Enables "And yesterday?" after "What's my ROAS this week?"
  - Enables "Which one performed best?" after "Show me campaigns"

### 1️⃣4️⃣ **Telemetry** (`app/telemetry/logging.py`)
- **Logs every run** to `qa_query_logs` table
- **Captures**:
  - Question text
  - Executed DSL (or validation error)
  - Success/failure flag
  - Latency in milliseconds
  - Error messages (if failed)
  - User ID and workspace ID
- **Purpose**: Observability, debugging, offline evaluation

### 1️⃣5️⃣ **Response**
```json
{
  "answer": "Your ROAS for the selected period is 2.45. That's a +19.0% change vs the previous period. Top performer: Summer Sale.",
  "executed_dsl": {
    "metric": "roas",
    "time_range": {"last_n_days": 7},
    "compare_to_previous": true,
    "group_by": "campaign",
    "breakdown": "campaign",
    "top_n": 10,
    "filters": {}
  },
  "data": {
    "summary": 2.45,
    "previous": 2.06,
    "delta_pct": 0.189,
    "timeseries": [
      {"date": "2025-09-24", "value": 2.30},
      {"date": "2025-09-25", "value": 2.45}
    ],
    "breakdown": [
      {"label": "Summer Sale", "value": 3.20},
      {"label": "Winter Campaign", "value": 2.80}
    ]
  }
}
```

## Security Guarantees

### 🔒 **Workspace Isolation**
All queries are scoped at the SQL level:
```python
.join(Entity, Entity.id == MetricFact.entity_id)
.filter(Entity.workspace_id == workspace_id)
```
**No cross-workspace data leaks possible.**

### 🔒 **No SQL Injection**
- LLM outputs **JSON** (not SQL)
- JSON validated by **Pydantic**
- Execution uses **SQLAlchemy ORM**

### 🔒 **Safe Math**
Derived metrics have divide-by-zero guards:
```python
if metric == "roas":
    return (revenue / spend) if spend > 0 else None
```

### 🔒 **Authentication**
- Requires valid JWT token
- User context passed to telemetry
- Workspace access verified

## Performance Metrics

| Stage | Latency | Notes |
|-------|---------|-------|
| Context Retrieval | <1ms | In-memory lookup |
| Canonicalization | <1ms | Simple string replacements |
| LLM Translation | 500-1000ms | OpenAI API call (DSL, with context) |
| Validation | 1-5ms | Pydantic validation |
| Planning | <1ms | Pure Python logic |
| Database Query | 10-50ms | Depends on data volume |
| **Answer Generation** | **200-500ms** | **LLM rephrase (hybrid)** |
| Answer Fallback | <1ms | Template-based (if LLM fails) |
| Context Storage | <1ms | In-memory append |
| **Total** | **~700-1550ms** | End-to-end (with LLM answer) |

## File Reference

| Component | File | Purpose |
|-----------|------|---------|
| **Entry Point** | `app/routers/qa.py` | HTTP endpoint |
| **Orchestrator** | `app/services/qa_service.py` | Main pipeline coordinator |
| **Context Manager** | `app/context/context_manager.py` | Conversation history (NEW) |
| **DSL Schema** | `app/dsl/schema.py` | Pydantic models |
| **Canonicalization** | `app/dsl/canonicalize.py` | Synonym mapping |
| **Validation** | `app/dsl/validate.py` | DSL validation |
| **Planning** | `app/dsl/planner.py` | Query planning |
| **Execution** | `app/dsl/executor.py` | SQL execution |
| **Translation** | `app/nlp/translator.py` | LLM integration (DSL, context-aware) |
| **Prompts** | `app/nlp/prompts.py` | System prompts (DSL) |
| **Answer Builder** | `app/answer/answer_builder.py` | Hybrid answer generation |
| **Telemetry** | `app/telemetry/logging.py` | Structured logging |
| **Examples** | `app/dsl/examples.md` | Few-shot examples |

## Testing

```bash
# Run all tests
pytest backend/app/tests/ -v

# Run specific test suites
pytest backend/app/tests/test_dsl_validation.py -v
pytest backend/app/tests/test_dsl_executor.py -v
pytest backend/app/tests/test_translator.py -v
pytest backend/app/tests/test_context_manager.py -v  # NEW: Context manager tests
```

## How to Use

### Basic Query
```bash
curl -X POST "http://localhost:8000/qa?workspace_id=<UUID>" \
  -H "Cookie: access_token=Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"question": "What's my ROAS this week?"}'
```

### With Filters
```bash
curl -X POST "http://localhost:8000/qa?workspace_id=<UUID>" \
  -H "Cookie: access_token=Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"question": "Show me revenue from active Google campaigns this month"}'
```

### Complex Query
```bash
curl -X POST "http://localhost:8000/qa?workspace_id=<UUID>" \
  -H "Cookie: access_token=Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"question": "Which campaigns had the best ROAS this quarter vs last quarter?"}'
```

## Future Enhancements

- **Phase 5**: Validation repair (re-ask LLM with errors) + rule-based fallbacks
- **Phase 6**: Comprehensive evaluation harness with golden outputs
- **Phase 7**: Multi-metric queries, nested breakdowns, forecasting, anomaly detection
- **Phase 8**: Enhanced answer personalization (user preferences, tone adaptation)
- **Phase 9**: Multi-language support for answers
- **Context Enhancements**:
  - Persistent storage (Redis/PostgreSQL for cross-session continuity)
  - Smart context pruning (relevance-based, not just FIFO)
  - Context expiration (TTL-based cleanup)
  - Cross-session history retrieval

## Documentation

- **DSL Specification**: `backend/docs/dsl-spec.md`
- **Architecture Details**: `backend/docs/qa-arch.md`
- **Module Guide**: `backend/app/dsl/README.md`
- **Build Log**: `docs/ADNAVI_BUILD_LOG.md`
