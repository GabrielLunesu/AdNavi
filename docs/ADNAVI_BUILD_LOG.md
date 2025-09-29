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
- QA endpoint: `/qa` (natural language → metrics DSL → execution)
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


