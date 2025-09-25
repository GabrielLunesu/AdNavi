# AdNavi — Living Build Log

_Last updated: 2025-09-25T15:58:00Z_

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
- Theme: Dark default
- Data: Mock only (no API/data fetching)
- Repo doc path: `docs/ADNAVI_BUILD_LOG.md`

### 1.1 Frontend — `ui/`
- Routing: `/` (Homepage), `/dashboard`, `/analytics`, `/copilot`, `/finance`, `/campaigns`, `/campaigns/[id]`
- Components: granular, presentational, mock props
- Charts: Recharts; Icons: lucide-react
 - Campaigns sparklines: inline SVG polylines (no chart lib)
 - Campaigns sorting fields: ROAS (default), Revenue, Spend, Conversions, CTR, CPC
 - Pagination: 8 rows per page (client-side)
- Styling: dark, rounded, soft shadows

### 1.2 Backend — `api/` (planned)
- Status: not implemented
- Candidates: FastAPI (Python) or .NET Web API
- Responsibilities (planned): auth, data aggregation, ads connectors, reporting

### 1.3 Infrastructure (planned)
- Envs: dev, staging, prod
- CI/CD: lint, test, build; deploy (TBD)
- IaC: Terraform/Pulumi (TBD)
- Observability: logs, metrics, tracing (TBD)

---

## 2) Plan / Next Steps
- [x] Step 1: Homepage in `ui/app/page.jsx` (h1 “AdNavi”, button → `/dashboard`)
- [x] Step 2: Layouts in `ui/app/layout.jsx` and `ui/app/(dashboard)/layout.jsx`
- [x] Step 3: Dashboard `ui/app/(dashboard)/dashboard/page.jsx`
- [x] Assistant section integrated inside dashboard page (not sticky)
- [x] Background gradient + glow orbs to match wireframe mood
- [x] KPI grid 3-per-row on desktop; wraps to additional rows
- [ ] Prep for backend: scaffold `api/` folder with README and ADRs (no code yet)
- [ ] Future: real data, auth, analytics, CI/CD

---

## 3) Decisions (Architecture & Conventions)
- Repo style: **Monorepo-ready**; current active app: `ui/`
- Files: **.jsx** only, no TS for now
- State: none (except trivial local), mock data only
- Directory conventions:
  - `ui/components/*` — small presentational components
  - `ui/data/*` — mock data modules
  - `ui/lib/cn.js` — class util
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

### 4.2 Backend (`api/`) — planned
- None yet. Record choices here when added.

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
- Shell: Logo, Sidebar, SidebarSection, NavItem, WorkspaceSummary, UserMini, Topbar
- Inputs: PromptInput, QuickAction, TimeRangeChips
- Data Viz: KPIStatCard, Sparkline, LineChart
- Panels: NotificationsPanel, NotificationItem, CompanyCard, VisitorsChartCard, UseCasesList, UseCaseItem
- Primitives: Card, IconBadge, KeyValue
- Utils: cn.js
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
  - `ui/app/(dashboard)/layout.jsx` → sidebar chrome; page renders assistant + content
- Assistant section is rendered at the top of the dashboard page (not fixed/sticky).
- KPI cards render in a 3-column grid on desktop; they wrap if more than three.
- Dashboard sections mirror wireframe; chips/CTAs non-functional.
- Charts render static arrays (Recharts used for Analytics chart and sparklines).

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


