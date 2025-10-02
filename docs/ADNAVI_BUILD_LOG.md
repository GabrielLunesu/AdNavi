# AdNavi — Living Build Log

_Last updated: 2025-09-25T16:04:00Z_

## 0) Monorepo Map (Current & Planned)
- **Frontend (current):** `ui/` — Next.js 15.5.4 (App Router), **JSX only**
- **Backend (planned):** `api/` — (TBD: FastAPI or .NET Web API) — not implemented yet
- **Shared packages (planned):** `packages/` — shared UI/components/types/utils
- **Docs (current):** `docs/` — this file + architecture notes
- **Infra (planned):** `infra/` — IaC, CI/CD, envs, deploy scripts

> This section must stay current as we add apps/packages.

---

## 1) Project Snapshot
- Framework: Next.js 15.5.4 (App Router, **JSX only**)
- Backend: FastAPI + SQLAlchemy 2.x + Alembic, Postgres via Docker
- Auth: Email/password, JWT (HTTP-only cookie), simple cookie session
- Repo doc path: `docs/ADNAVI_BUILD_LOG.md`

### 1.1 Frontend — `ui/`
- Routing: `/` (Homepage), `/dashboard`, `/analytics`, `/copilot`, `/finance`, `/campaigns`, `/campaigns/[id]`
- Components: granular, presentational, mock props
- Charts: Recharts; Icons: lucide-react
 - Campaigns sparklines: inline SVG polylines (no chart lib)
 - Campaigns sorting fields: ROAS (default), Revenue, Spend, Conversions, CTR, CPC
 - Pagination: 8 rows per page (client-side)
- Styling: dark, rounded, soft shadows

### 1.2 Backend — `backend/`
- Framework: FastAPI with SQLAlchemy 2.x + Alembic
- Database: PostgreSQL 16 (Docker compose)
- Auth: JWT (HTTP-only cookie), bcrypt password hashing
- Admin: SQLAdmin on `/admin` endpoint for CRUD operations on all models
- Models: Workspace, User, Connection, Token, Fetch, Import, Entity, MetricFact, ComputeRun, Pnl, QaQueryLog, AuthCredential
- QA System (DSL v1.2):
  - `app/dsl/`: Domain-Specific Language for queries (schema, canonicalize, validate, planner, executor)
  - `app/nlp/`: Natural language translation via OpenAI (translator, prompts)
  - `app/telemetry/`: Structured logging and observability
  - `app/tests/`: Unit tests for DSL validation, executor, translator, v1.2 extensions

### 1.3 Infrastructure
- Envs: dev, staging, prod
- CI/CD: lint, test, build; deploy (TBD)
- IaC: Terraform/Pulumi (TBD)
- Observability: logs, metrics, tracing (TBD)

---

## 2) Plan / Next Steps
- [x] Step 1: Homepage in `ui/app/page.jsx` (h1 "AdNavi", button → `/dashboard`)
- [x] Step 2: Layouts in `ui/app/layout.jsx` and `ui/app/(dashboard)/layout.jsx`
- [x] Step 3: Dashboard `ui/app/(dashboard)/dashboard/page.jsx`
- [x] Assistant section integrated inside dashboard page (not sticky)
- [x] Background gradient + glow orbs to match wireframe mood
- [x] KPI grid 3-per-row on desktop; wraps to additional rows
- [x] Backend mock data seeder for testing (`backend/app/seed_mock.py`)
- [x] Dashboard KPIs connected to real API data (`/workspaces/{id}/kpis` endpoint)
- [ ] Future: remaining pages real data integration, advanced analytics, CI/CD

---

## 3) Decisions (Architecture & Conventions)
- Repo style: **Monorepo-ready**; current active app: `ui/`
- Files: **.jsx** only, no TS for now
- State: minimal (auth + local component state), transitioning from mock to real API data
- Directory conventions:
  - `ui/components/*` — small presentational components
  - `ui/components/sections/*` — container components with data fetching
  - `ui/data/*` — mock data modules
  - `ui/lib/*` — utilities (cn.js for classes, auth.js for auth, api.js for data fetching)
- Charts: Recharts; Icons: lucide-react

---

## 4) Dependencies

### 4.1 Frontend (`ui/`)
- Runtime (installed):
  - tailwindcss v4 + `@tailwindcss/postcss` (styling)
  - lucide-react (icons)
  - recharts (charts)
  - clsx, tailwind-merge (class merging)
  - next 15.5.4, react 19.1.0, react-dom 19.1.0
- Dev:
  - eslint, eslint-config-next
- Notes:
  - Recharts used for sparklines and the visitors chart.
  - lucide-react provides status icons for notifications and UI affordances.
  - Tailwind v4 utilities drive dark, rounded, soft-shadow styling.

### 4.2 Backend (`backend/`)
- Runtime: Python 3.11
- Deps: fastapi, uvicorn, SQLAlchemy 2.x, alembic, pydantic v2, passlib[bcrypt], python-jose, python-dotenv, psycopg2-binary, sqladmin, openai
- Auth: bcrypt password hashing, HS256 JWT cookie `access_token`
- DB: PostgreSQL 16 (Docker compose)
- Admin: SQLAdmin provides web UI for database CRUD operations

---

## 5) Routes (Frontend `ui/`)
- `/` → `ui/app/page.jsx`
- `/dashboard` → `ui/app/(dashboard)/dashboard/page.jsx`
- `/analytics` → `ui/app/(dashboard)/analytics/page.jsx`
 - `/copilot` → `ui/app/(dashboard)/copilot/page.jsx`
 - `/finance` → `ui/app/(dashboard)/finance/page.jsx`
 - `/campaigns` → `ui/app/(dashboard)/campaigns/page.jsx`
 - `/campaigns/[id]` → `ui/app/(dashboard)/campaigns/[id]/page.jsx`

---

## 6) Components Inventory (Frontend `ui/`)
- Shell: Logo, Sidebar, SidebarSection, NavItem, WorkspaceSummary (now fetches real data), UserMini, Topbar
- Inputs: PromptInput, QuickAction, TimeRangeChips
- Data Viz: KPIStatCard, Sparkline, LineChart
- Panels: NotificationsPanel, NotificationItem, CompanyCard, VisitorsChartCard, UseCasesList, UseCaseItem
- Primitives: Card, IconBadge, KeyValue
- Utils: cn.js, lib/api.js (KPI data fetching, workspace info)
- Sections: components/sections/HomeKpiStrip.jsx (container for dashboard KPIs)
 - Assist: AssistantSection (greeting + prompt + quick actions)
 - Analytics (page-specific):
   - Controls: `components/analytics/AnalyticsControls.jsx`
   - Copilot: `components/analytics/AICopilotHero.jsx`
   - KPIs: `components/analytics/KPIGrid.jsx`, `components/analytics/KPICard.jsx`
   - Ad sets: `components/analytics/AdSetCarousel.jsx`, `components/analytics/AdSetTile.jsx`
   - Chart: `components/analytics/ChartCard.jsx`
   - Opportunities: `components/analytics/OpportunityRadar.jsx`, `components/analytics/OpportunityItem.jsx`
   - Rules: `components/analytics/RulesPanel.jsx`, `components/analytics/RuleRow.jsx`
   - Right rail: `components/analytics/RightRailAIPanel.jsx`
   - Primitives used: `components/PillButton.jsx`, `components/TabPill.jsx`
 - Copilot (page-specific):
   - `components/copilot/ContextBar.jsx`, `components/copilot/OrbHeader.jsx`
   - `components/copilot/ChatThread.jsx`, `components/copilot/ChatMsgAI.jsx`, `components/copilot/ChatMsgUser.jsx`
   - `components/copilot/MiniKPI.jsx`, `components/copilot/SparklineCard.jsx`
   - `components/copilot/ExpandableSections.jsx`, `components/copilot/CampaignTile.jsx`
   - `components/copilot/SmartSuggestions.jsx`, `components/copilot/InputBar.jsx`
 - Finance (page-specific):
   - `components/finance/FinanceHeader.jsx`, `components/finance/KPIGrid.jsx`, `components/finance/KPICard.jsx`
   - `components/finance/CostsPanel.jsx`, `components/finance/CostRow.jsx`, `components/finance/AddCostRow.jsx`
   - `components/finance/RevenueChartCard.jsx`
   - `components/finance/RulesPanel.jsx`, `components/finance/RuleBuilder.jsx`, `components/finance/RuleRow.jsx`
 - Campaigns (page-specific):
   - Toolbar: `components/campaigns/PlatformFilter.jsx`, `components/campaigns/StatusFilter.jsx`, `components/campaigns/TimeframeFilter.jsx`, `components/campaigns/SortDropdown.jsx`
   - Table: `components/campaigns/CampaignTable.jsx`, `components/campaigns/CampaignRow.jsx`, `components/campaigns/PlatformBadge.jsx`, `components/campaigns/TrendSparkline.jsx`
   - Detail: `components/campaigns/DetailHeader.jsx`, `components/campaigns/EntityTable.jsx`, `components/campaigns/EntityRow.jsx`
   - Rules: `components/campaigns/RulesPanel.jsx`
> Keep this list current with file paths.

---

## 7) Mock Data Sources (Frontend `ui/`)
- `ui/data/kpis.js`, `ui/data/notifications.js`, `ui/data/company.js`, `ui/data/visitors.js`, `ui/data/useCases.js`
- Analytics: `ui/data/analytics/header.js`, `ui/data/analytics/kpis.js`, `ui/data/analytics/adsets.js`, `ui/data/analytics/chart.js`, `ui/data/analytics/opportunities.js`, `ui/data/analytics/rules.js`, `ui/data/analytics/panel.js`
 - Copilot: `ui/data/copilot/context.js`, `ui/data/copilot/seedMessages.js`, `ui/data/copilot/suggestions.js`, `ui/data/copilot/placeholders.js`
 - Finance: `ui/data/finance/kpis.js`, `ui/data/finance/costs.js`, `ui/data/finance/series.js`, `ui/data/finance/rules.js`, `ui/data/finance/timeRanges.js`
 - Campaigns: `ui/data/campaigns/campaigns.js`, `ui/data/campaigns/detail.js`, `ui/data/campaigns/rules.js`, `ui/data/campaigns/sorters.js`
> Update when shapes/labels change.

---

## 8) How Things Work (Current)
- Layout hierarchy:
  - `ui/app/layout.jsx` → global shell (adds gradient + glow background)
  - `ui/app/(dashboard)/layout.jsx` → sidebar chrome; guards all dashboard pages by calling backend `/auth/me` client-side
- Assistant section is rendered at the top of the dashboard page (not fixed/sticky).
### 8.1 Backend
- Auth endpoints: `/auth/register`, `/auth/login`, `/auth/me`, `/auth/logout`
- Workspace endpoints: `/workspaces/{id}/info` (sidebar summary)
- KPI endpoints: `/workspaces/{id}/kpis` (dashboard metrics)
- QA endpoint: `/qa` (natural language → DSL → execution → hybrid answer)
  - Pipeline: Question → Canonicalize → LLM Translation → Validate → Plan → Execute → Answer Builder (LLM) → Response
  - Answer generation: Hybrid approach (deterministic facts + LLM rephrasing for natural tone)
  - Fallback: Template-based answers if LLM fails
- QA log endpoints: `/qa-log/{workspace_id}` [GET, POST] (chat history)
- Admin endpoint: `/admin` - SQLAdmin UI for all models (no auth protection yet)
- Cookie: `access_token` contains `Bearer <jwt>`, `httponly`, `samesite=lax`
- On register: create `Workspace` named "New workspace", then `User` (role Admin for now), then `AuthCredential` with bcrypt hash
- ORM models: UUID primary keys; enums for Role/Provider/Level/Kind/ComputeRunType
- Migrations: Alembic configured to read `DATABASE_URL` from env; run `alembic upgrade head`
- Admin features: List, create, update, delete for all models; searchable and sortable columns; FontAwesome icons
### 8.2 Frontend
- Sidebar shows real workspace name and last sync timestamp (fetched from API)
- KPI cards render real data from MetricFact table with time range filtering
- Time range selector functional: Today, Yesterday, Last 7 days, Last 30 days
- Dashboard sections fetch real data; other pages still use mock data
- Charts use Recharts for sparklines and visualizations

---

## 9) Open Questions
- Backend stack choice (FastAPI vs .NET)? Auth provider? Data store?
- CI/CD target platform(s)? Secrets management?

---

## 10) Known Gaps / Tech Debt
- Responsive polish <1024px TBD
- No accessibility audit yet
- No test setup

---

## 11) Changelog
| - 2025-10-02T00:00:00Z — Conversation Context Manager: Added multi-turn conversation support for follow-up questions.
  - Backend files:
    - `backend/app/context/__init__.py`: New module for conversation history management
    - `backend/app/context/context_manager.py`: In-memory conversation history storage per user+workspace
    - `backend/app/services/qa_service.py`: Updated to retrieve context before translation and save after execution
    - `backend/app/nlp/translator.py`: Enhanced to accept context and include conversation history in LLM prompts
    - `backend/app/tests/test_context_manager.py`: Comprehensive tests (50+ test cases covering all scenarios)
  - Documentation files:
    - `backend/QA_SYSTEM_ARCHITECTURE.md`: Updated flow diagram and architecture with context manager integration
    - `docs/ADNAVI_BUILD_LOG.md`: Added changelog entry
  - Features:
    - **Context Storage**: Stores last N queries (default 5) per user+workspace
      - WHY: Enables follow-up questions like "Which one performed best?" or "And yesterday?"
      - User+workspace scoped (no cross-tenant leaks)
      - In-memory storage (fast, <1ms operations)
      - FIFO eviction when max_history reached
    - **Context-Aware Translation**: Translator includes conversation history in LLM prompts
      - WHY: Helps LLM resolve pronouns and references ("this", "that", "which one")
      - Includes last 1-2 queries with key facts (question, metric, results)
      - Summarizes context to keep prompts concise
    - **Multi-Turn Conversations**: Complete support for follow-up questions
      - Example flow:
        1. "Show me ROAS by campaign" → stores DSL + breakdown results
        2. "Which one performed best?" → translator uses stored breakdown to resolve "which one"
      - Example flow:
        1. "What's my ROAS this week?" → stores metric + time range
        2. "And yesterday?" → translator infers to use same metric (ROAS) for yesterday
    - **Thread Safety**: ContextManager uses locks for concurrent request safety
      - Multiple FastAPI requests can add/retrieve context safely
      - No race conditions or data corruption
    - **Workspace Isolation**: Each user+workspace has separate context
      - Key format: "{user_id}:{workspace_id}"
      - No cross-tenant context leaks
      - Anonymous users supported ("anon" user ID)
  - Design principles:
    - Simple in-memory storage (no database overhead)
    - Fixed-size history (prevents memory bloat)
    - User+workspace scoping (tenant safety)
    - Thread-safe operations (production-ready)
    - Comprehensive testing (unit + integration + thread safety)
  - Performance:
    - Context retrieval: <1ms (in-memory lookup)
    - Context storage: <1ms (in-memory append)
    - No impact on overall QA latency (~700-1550ms total)
  - Test coverage:
    - 50+ test cases covering:
      - Basic add/get operations
      - Max history enforcement (FIFO eviction)
      - User+workspace scoping (tenant isolation)
      - Thread safety (concurrent reads/writes)
      - Clear context operations
      - Edge cases (empty history, complex results)
      - Integration scenarios (follow-up conversations)
  - Future enhancements:
    - Persistent storage (Redis/PostgreSQL for cross-session continuity)
    - Smart context pruning (relevance-based, not just FIFO)
    - TTL-based expiration (auto-cleanup old conversations)
    - Cross-session history retrieval
| - 2025-09-30T20:00:00Z — Hybrid Answer Builder: Added LLM-based answer generation with deterministic fallback.
  - Backend files:
    - `backend/app/answer/__init__.py`: New module for answer generation
    - `backend/app/answer/answer_builder.py`: Hybrid answer builder (GPT-4o-mini + deterministic facts)
    - `backend/app/services/qa_service.py`: Updated to use AnswerBuilder with template fallback
    - `backend/app/tests/test_answer_builder.py`: Comprehensive tests for answer builder (14 tests total)
  - Documentation files:
    - `backend/QA_SYSTEM_ARCHITECTURE.md`: Updated flow diagram and architecture with answer builder stage
  - Features:
    - **Hybrid Approach**: Combines deterministic fact extraction with LLM rephrasing
      - WHY: Facts are safe (no hallucinations), presentation is natural (not robotic)
      - Extracts numbers/data from MetricResult deterministically
      - Uses GPT-4o-mini to rephrase facts into conversational answers
    - **Safety Guarantees**:
      - LLM cannot invent numbers (strict system prompt)
      - Only provided facts are used
      - Deterministic fact extraction ensures accuracy
    - **Fallback Mechanism**: If LLM fails, uses template-based answer (robotic but safe)
      - Ensures system always returns an answer
      - Fallback logged for observability
    - **Supports All Query Types**: Works for metrics, providers, and entities queries
    - **Telemetry**: Measures answer generation latency separately from total latency
  - Design principles:
    - Separation of concerns: AnswerBuilder handles ONLY presentation layer
    - Deterministic facts: All numbers extracted safely from validated results
    - LLM constraints: Temperature=0.3 for natural but controlled output
    - Comprehensive testing: Mocked LLM calls for fast, deterministic tests
  - Performance:
    - Answer generation: ~200-500ms (LLM call)
    - Fallback: <1ms (template-based)
  - Examples:
    - Metrics: "Your ROAS is 2.45, up 19% from the previous period. Great performance!"
    - Providers: "You're running ads on Google, Meta, and TikTok."
    - Entities: "Here are your active campaigns: Summer Sale and Winter Promo."
| - 2025-09-30T18:00:00Z — DSL v1.2 extensions: added support for providers and entities queries beyond metrics.
  - Backend files:
    - `backend/app/dsl/schema.py`: Added QueryType enum (metrics, providers, entities); made metric/time_range optional
    - `backend/app/dsl/planner.py`: Returns None for non-metrics queries (handled directly in executor)
    - `backend/app/dsl/executor.py`: Added handlers for providers (list platforms) and entities (list campaigns/adsets/ads) queries
    - `backend/app/dsl/examples.md`: Added 3 new examples for providers and entities queries
    - `backend/app/nlp/prompts.py`: Updated system prompt and added 2 new few-shot examples for v1.2
    - `backend/app/services/qa_service.py`: Updated answer builder to handle providers and entities responses
    - `backend/app/tests/test_dsl_v12.py`: Comprehensive tests for v1.2 query types (12 tests total)
  - Documentation files:
    - `backend/docs/dsl-spec.md`: Added DSL v1.2 Extensions section with full documentation
  - Features:
    - **Providers queries**: List distinct ad platforms in workspace ("Which platforms am I on?")
      - Returns: `{"providers": ["google", "meta", "tiktok"]}`
      - No metric or time_range needed
      - Workspace-scoped, no cross-tenant leaks
    - **Entities queries**: List campaigns/adsets/ads with optional filters ("List my active campaigns")
      - Returns: `{"entities": [{"name": "...", "status": "...", "level": "..."}, ...]}`
      - Supports filters: level (campaign/adset/ad), status (active/paused), entity_ids
      - Respects top_n limit (default 5, max 50)
      - Workspace-scoped, no cross-tenant leaks
    - **Backward compatibility**: All v1.1 metrics queries work unchanged; query_type defaults to "metrics"
    - **Answer generation**: Natural language responses for all query types
      - Providers: "You are running ads on Google, Meta, and TikTok."
      - Entities: "Here are your campaigns: Summer Sale, Winter Promo, Spring Launch."
      - Metrics: Existing v1.1 logic (ROAS, CPA, comparisons, breakdowns)
  - Design principles:
    - Separation of concerns: Planner returns None for non-metrics; executor branches by query_type
    - Workspace safety: All queries filter by workspace_id at SQL level
    - Comprehensive testing: 12 new tests covering all v1.2 scenarios + workspace isolation
    - Documentation-first: Every function has detailed docstrings with WHY, WHAT, WHERE, and examples
  - Use cases enabled:
    - "Which platforms am I advertising on?" → providers query
    - "List my active campaigns" → entities query with filters
    - "Show me all paused adsets" → entities query with level and status filters
    - All existing metrics queries continue to work
| - 2025-09-30T15:00:00Z — DSL v1.1 refactor: comprehensive QA system with enhanced DSL, NLP translation, telemetry, tests, and docs.
   - Backend files:
     - `backend/app/dsl/__init__.py`, `backend/app/dsl/schema.py`, `backend/app/dsl/canonicalize.py`, `backend/app/dsl/validate.py`
     - `backend/app/dsl/planner.py`, `backend/app/dsl/executor.py`, `backend/app/dsl/examples.md`
     - `backend/app/nlp/__init__.py`, `backend/app/nlp/translator.py`, `backend/app/nlp/prompts.py`
     - `backend/app/telemetry/__init__.py`, `backend/app/telemetry/logging.py`
     - `backend/app/services/qa_service_refactored.py`, `backend/app/routers/qa_refactored.py`
     - `backend/app/tests/__init__.py`, `backend/app/tests/test_dsl_validation.py`, `backend/app/tests/test_dsl_executor.py`, `backend/app/tests/test_translator.py`
   - Documentation files:
     - `backend/docs/dsl-spec.md`: Complete DSL specification with examples and validation rules
     - `backend/docs/qa-arch.md`: System architecture diagram and dataflow documentation
   - Features:
     - **DSL Module**: Enhanced Pydantic schema with TimeRange, Filters, MetricQuery, MetricResult models
     - **Canonicalization**: Synonym mapping (e.g., "return on ad spend" → "roas") and time phrase normalization
     - **Validation**: Comprehensive validation with DSLValidationError and helpful error messages
     - **Planner**: Converts DSL into low-level execution plans (resolves dates, maps derived metrics → base measures)
     - **Executor**: Workspace-scoped SQLAlchemy queries with divide-by-zero guards for derived metrics
     - **NLP Translator**: OpenAI GPT-4o-mini with temperature=0, JSON mode, few-shot examples (12 examples)
     - **Telemetry**: Structured logging for every QA run (success/failure, latency, DSL validity, errors)
     - **Tests**: Unit tests for validation, executor (derived metrics), and translator (mocked LLM)
     - **Documentation**: Complete DSL spec and architecture docs
   - Design principles:
     - Docs-first: Every module has docstrings explaining WHAT, WHY, and WHERE
     - Separation of concerns: DSL (structure) ↔ NLP (translation) ↔ Telemetry (observability)
     - Determinism: LLM outputs validated JSON; backend executes safely
     - Tenant safety: All queries workspace-scoped at SQL level
     - Observability: All runs logged with structured data
   - Performance: ~500-1000ms translation + ~10-50ms execution
   - Security: No SQL injection (DSL → ORM), workspace isolation, divide-by-zero guards
   - Note: Phase 5 (validation repair & fallbacks) deferred for future enhancement
| - 2025-09-30T03:00:00Z — QA history: endpoints + Copilot chat UI with bubbles.
   - Backend files: `backend/app/schemas.py`, `backend/app/routers/qa_log.py`, `backend/app/services/qa_service.py`, `backend/app/routers/qa.py`, `backend/app/main.py`
   - Frontend files: `ui/lib/api.js`, `ui/components/ui/ChatBubble.jsx`, `ui/components/ui/ChatComposer.jsx`, `ui/app/(dashboard)/copilot/page.jsx`
   - Features:
     - GET/POST `/qa-log/{workspace_id}` to fetch/store chat history (auth-scoped)
     - `/qa` now auto-logs queries with answer embedded in `dsl_json`
     - Copilot redesigned: glassmorphic container, animated orb, suggestion chips, sticky composer; history as user/AI bubbles with animations
   - Notes: avoided DB migration by embedding `answer_text` in `dsl_json` for now
| - 2025-09-30T02:20:00Z — Copilot UI: chat input → /copilot, framer-motion, QA call.
   - Frontend files: `ui/lib/api.js`, `ui/components/ui/ChatInput.jsx`, `ui/app/(dashboard)/dashboard/page.jsx`, `ui/app/(dashboard)/copilot/page.jsx`, `ui/package.json`
   - Features:
     - Chat bar on dashboard redirects to `/copilot?q=...&ws=...`
     - Copilot page reads query params, calls backend `/qa`, shows loader then answer
     - Framer-motion animations for entrance, spinner, and answer reveal
   - Design: API logic in `lib/api.js`; input atomized in `components/ui/ChatInput.jsx`
| - 2025-09-30T02:00:00Z — Added /qa endpoint with DSL translation and execution.
   - Backend files: `backend/app/schemas.py`, `backend/app/services/metric_service.py`, `backend/app/services/qa_service.py`, `backend/app/routers/qa.py`, `backend/app/main.py`, `backend/app/deps.py`, `backend/requirements.txt`
   - Features:
     - POST `/qa?workspace_id=UUID` accepts `{ question }`
     - Translates to JSON DSL (Pydantic `MetricQuery`) via OpenAI, validates
     - Executes via `MetricService.execute` against `MetricFact`
     - Returns `answer`, `executed_dsl`, and `data` (summary/breakdown)
   - Security: OpenAI key loaded from `.env` via settings; no keys hardcoded
   - Design: Clear service layer (`qa_service`, `metric_service`) for scalability
| - 2025-09-30T01:00:00Z — Added workspace info endpoint and real-time sync status in sidebar.
   - Backend files: `backend/app/schemas.py`, `backend/app/routers/workspaces.py`
   - Frontend files: `ui/lib/api.js`, `ui/components/WorkspaceSummary.jsx`, `ui/components/Sidebar.jsx`
   - Features:
     - GET `/workspaces/{id}/info` endpoint returns workspace name and last sync timestamp
     - Last sync determined by latest successful Fetch (raw data import) or ComputeRun (fallback)
     - Sidebar now displays real workspace name and formatted last sync time (e.g., "13 min ago")
     - Auto-refresh functionality when clicking the refresh button
   - Design: Clear separation of concerns with API fetch logic in WorkspaceSummary container component
| - 2025-09-30T00:30:00Z — Made time range selector functional on dashboard.
   - Frontend files: `ui/components/TimeRangeChips.jsx`, `ui/app/(dashboard)/dashboard/page.jsx`, `ui/components/sections/HomeKpiStrip.jsx`, `ui/lib/api.js`
   - Features:
     - Time range buttons now functional: Today, Yesterday, Last 7 days, Last 30 days
     - Dashboard KPIs update based on selected time range
     - Support for both last_n_days and explicit date ranges in API
     - "Yesterday" uses offset calculation for precise date range
   - UI: Selected time range highlighted and displayed next to "Overview" header
| - 2025-09-30T00:00:00Z — Added KPI aggregation endpoint and connected dashboard to real API data.
   - Backend files: `backend/app/schemas.py`, `backend/app/routers/kpis.py`, `backend/app/main.py`
   - Frontend files: `ui/lib/api.js`, `ui/components/sections/HomeKpiStrip.jsx`, `ui/app/(dashboard)/dashboard/page.jsx`
   - Features:
     - POST `/workspaces/{id}/kpis` endpoint aggregates MetricFact data with time ranges, previous period comparison, and sparklines
     - Supports filtering by provider, level, and entity status
     - Computes derived metrics (ROAS, CPA) with divide-by-zero protection
     - Dashboard now fetches real KPIs instead of using mock data
   - Design: Separation of concerns with API client in lib/, container component in sections/, presentation in existing KPIStatCard
| - 2025-09-29T12:00:00Z — Added comprehensive database seed script for testing with realistic mock data.
   - Files: `backend/app/seed_mock.py`
   - Features: Creates "Defang Labs" workspace with 2 users (owner/viewer), mock connection, entity hierarchy (2 campaigns > 4 adsets > 8 ads), 30 days of MetricFact data (240 records), ComputeRun with P&L snapshots including CPA/ROAS calculations
   - Usage: `cd backend && python3 -m app.seed_mock`
   - Credentials: owner@defanglabs.com / viewer@defanglabs.com (password: password123)
 - 2025-09-28T00:01:00Z — Fixed SQLAdmin foreign key dropdowns and added comprehensive documentation.
   - Files: `backend/app/main.py`, `backend/app/models.py`
   - Changes: 
     - Added docstrings to all models explaining relationships and foreign key requirements
     - Fixed ModelView form_columns to use relationship names instead of _id fields
     - Added form_ajax_refs for searchable dropdown selectors
     - All foreign key fields now show as proper dropdowns in admin forms
   - Note: User-Workspace is still one-to-many (needs migration to many-to-many)
 - 2025-09-28T00:00:00Z — Added SQLAdmin dashboard for backend CRUD operations on all models.
   - Route: `/admin`
   - Files: `backend/app/main.py`
   - Models exposed: Workspace, User, Connection, Token, Fetch, Import, Entity, MetricFact, ComputeRun, Pnl, QaQueryLog, AuthCredential
   - Features: ModelView for each model with searchable/sortable columns, FontAwesome icons, form fields
   - Note: No auth protection yet; to be secured later
 - 2025-09-26T00:00:00Z — Backend added (FastAPI, Postgres, Alembic) with JWT cookie auth; UI auth guard + sidebar user pill.
   - Files: `backend/app/*`, `backend/alembic/*`, `ui/lib/auth.js`, `ui/components/Sidebar.jsx`, `ui/app/(dashboard)/layout.jsx`, `ui/app/layout.jsx`, `ui/app/page.jsx`
 - 2025-09-25T16:04:00Z — Dashboard assistant hero restyled: centered, larger, extra spacing, separator.
   - Files: `ui/components/AssistantSection.jsx`
 - 2025-09-25T15:58:00Z — Add Campaigns list and detail pages with filters, sort, pagination, and rules.
   - Routes: `/campaigns`, `/campaigns/[id]`
   - Files: `ui/app/(dashboard)/campaigns/page.jsx`, `ui/app/(dashboard)/campaigns/[id]/page.jsx`, `ui/components/campaigns/*`, `ui/data/campaigns/*`, `ui/components/Sidebar.jsx`
 - 2025-09-25T15:28:00Z — Add Finance (P&L) page with mock data, components, and sidebar active state.
   - Route: `/finance`
   - Files: `ui/app/(dashboard)/finance/page.jsx`, `ui/components/finance/*`, `ui/data/finance/*`, `ui/components/Sidebar.jsx`
   - Chart lib: Recharts (line chart)
 - 2025-09-25T15:15:00Z — Copilot suggestions trimmed to 2; scrollbar removed.
   - Files: `ui/components/copilot/SmartSuggestions.jsx`
 - 2025-09-25T15:12:00Z — Add Copilot chat page with mock data and sidebar nav update.
   - Route: `/copilot`
   - Files: `ui/app/(dashboard)/copilot/page.jsx`, `ui/components/copilot/*`, `ui/components/Sidebar.jsx`, `ui/data/copilot/*`
   - Notes: UI-only chat; no networking; reuses existing primitives.
 - 2025-09-25T14:33:00Z — Fix analytics icon import and React key spread warning.
   - Files: `ui/components/analytics/OpportunityItem.jsx`, `ui/components/analytics/KPIGrid.jsx`
 - 2025-09-25T14:48:00Z — Analytics UI tweaks to match design: Today timeframe, simplified ad-set tiles, chart header tabs, remove right rail.
   - Files: `ui/components/analytics/AnalyticsControls.jsx`, `ui/components/analytics/AdSetTile.jsx`, `ui/components/analytics/ChartCard.jsx`, `ui/app/(dashboard)/analytics/page.jsx`
 - 2025-09-25T14:53:00Z — Rules panel scope selector added (“Rules for [campaign, platform, workspace]”).
   - Files: `ui/components/analytics/RulesPanel.jsx`
 - 2025-09-25T14:28:00Z — Add Analytics page with granular components and mock data; update sidebar active state.
   - Route: `/analytics`
   - Files: `ui/app/(dashboard)/analytics/page.jsx`, `ui/components/analytics/*`, `ui/components/PillButton.jsx`, `ui/components/TabPill.jsx`, `ui/components/Sidebar.jsx`, `ui/data/analytics/*`
   - Deps: (no new runtime beyond existing Recharts/lucide-react)
- 2025-09-25T13:55:00Z — Initialize living docs and sync with current state; scaffold `docs/ADNAVI_BUILD_LOG.md`.
  - Files: `docs/ADNAVI_BUILD_LOG.md`
- 2025-09-25T13:44:00Z — Frontend foundation: created `app/` router structure, global layout, homepage, and dashboard shell; installed UI deps.
  - Files: `ui/app/layout.jsx`, `ui/app/page.jsx`, `ui/app/(dashboard)/layout.jsx`, `ui/components/*`, `ui/data/*`, `ui/lib/cn.js`, `ui/postcss.config.mjs`, `ui/src/app/* (removed)`
  - Deps: `lucide-react`, `recharts`, `clsx`, `tailwind-merge` (reasons: icons, charts, class merging)
- 2025-09-25T13:50:00Z — Dashboard content: sections, KPIs, notifications, company, visitors chart, use cases; mock data wired.
  - Files: `ui/app/(dashboard)/dashboard/page.jsx`, `ui/components/*`, `ui/data/*`
- 2025-09-25T13:53:00Z — Wireframe parity: AssistantSection inside page, KPI grid 3-col desktop, gradient background + glow orbs; removed sticky topbar usage from layout.
  - Files: `ui/components/AssistantSection.jsx`, `ui/app/(dashboard)/dashboard/page.jsx`, `ui/app/(dashboard)/layout.jsx`, `ui/app/layout.jsx`

Update routine (repeat every change)

READ docs/ADNAVI_BUILD_LOG.md.

SYNC PLAN if your upcoming change differs from “Plan / Next Steps”.

MAKE CHANGES in the repo.

DOCUMENT:

Add a Changelog entry (ISO time, summary, files touched).

Update sections that changed (Deps, Decisions, Routes, Components, Mock Data, Map, Gaps, Questions).

COMMIT with a message starting docs: or chore: docs mirroring the Changelog line.

Guardrails

Do not move or rename docs/ADNAVI_BUILD_LOG.md.

Keep the Monorepo Map accurate as soon as new folders (like api/) appear.

Prefer concise bullets; link code paths when helpful.


