---
config:
  theme: neo
  look: neo
  layout: elk
---

## Changelog

### 2025-10-11 - Finance & P&L Integration
- **Added ManualCost model**: Stores user-entered operational costs (non-ad spend)
- **Fields**: 
  - label, category, notes (string)
  - amount_dollar (decimal, 12,2) - stored in USD
  - allocation_type (string): "one_off" or "range"
  - allocation_date (datetime, nullable): For one_off costs
  - allocation_start, allocation_end (datetime, nullable): For range costs
  - workspace_id (FK to workspaces)
  - created_by_user_id (FK to users, nullable)
  - created_at, updated_at (datetime)
- **Purpose**: Combine ad spend (MetricFact) with manual costs for complete P&L view
- **WHY**: Finance page needs full cost picture, not just ad platform costs
- **Allocation rules**: 
  - one_off = single date, included if date falls within query period
  - range = pro-rated daily across date range, only overlapping days included
- **Workspace scoping**: All costs belong to one workspace (tenant isolation)
- **Migration**: `backend/alembic/versions/5b531bb7e3a8_add_manual_costs.py`

### 2025-10-05 - Derived Metrics v1
- **Added Goal enum** (7 values): awareness, traffic, leads, app_installs, purchases, conversions, other
- **Entity**: Added `goal` field (nullable) to track campaign objective
- **MetricFact**: Added 5 new base measure columns (all nullable):
  - `leads`: Lead form submissions (decimal)
  - `installs`: App installations (int)
  - `purchases`: Purchase events (int)
  - `visitors`: Landing page visitors (int)
  - `profit`: Net profit after costs (decimal)
- **Pnl**: Added 17 new columns (12 derived + 5 base, all nullable):
  - Base: leads, installs, purchases, visitors, profit
  - Derived cost metrics: cpc, cpm, cpl, cpi, cpp
  - Derived value metrics: poas, arpv, aov
  - Derived engagement metrics: ctr, cvr
- **Purpose**: Single source of truth for metric formulas (app/metrics/), used by executor and compute_service
- **Migration**: `backend/alembic/versions/9370d8b93e93_add_derived_metrics_v1.py`

---

classDiagram
direction LR
class Workspace {
  +uuid id
  +string name
  +datetime createdAt
}
class User {
  +uuid id
  +string email
  +string name
  +Role role
}
class Role {
  Owner
  Admin
  Viewer
}
class Provider {
  google
  meta
  tiktok
  other
}
class Connection {
  +uuid id
  +Provider provider
  +string externalAccountId
  +string name
  +string status
  +datetime connectedAt
}
class Token {
  +uuid id
  +Provider provider
  +string accessToken_enc
  +string refreshToken_enc
  +datetime expiresAt
  +string scope
}
class Fetch {
  +uuid id
  +string kind
  +string status
  +datetime startedAt
  +datetime finishedAt?
  +date rangeStart?
  +date rangeEnd?
}
class Import {
  +uuid id
  +datetime asOf
  +datetime createdAt
  +string note?
}
class Level {
  account
  campaign
  adset
  ad
  creative
  unknown
}
class Entity {
  +uuid id
  +Level level
  +string externalId
  +string name
  +string status
  +uuid parentId?
  +Goal goal?
}
class MetricFact {
  +uuid id
  +uuid entityId?
  +Provider provider
  +Level level
  +datetime eventAt
  +date eventDate
  +decimal spend
  +int impressions
  +int clicks
  +decimal conversions?
  +decimal revenue?
  +decimal leads?
  +int installs?
  +int purchases?
  +int visitors?
  +decimal profit?
  +string currency
  +string naturalKey
  +datetime ingestedAt
}
class ComputeRun {
  +uuid id
  +datetime asOf
  +datetime computedAt
  +string reason
  +string status
  +string type
}
class Kind {
  snapshot
  eod
}
class Goal {
  awareness
  traffic
  leads
  app_installs
  purchases
  conversions
  other
}
class Pnl {
  +uuid id
  +uuid entityId?
  +uuid runId
  +Provider provider
  +Level level
  +Kind kind
  +datetime asOf?
  +date eventDate?
  +decimal spend
  +decimal revenue?
  +decimal conversions?
  +int clicks
  +int impressions
  +decimal leads?
  +int installs?
  +int purchases?
  +int visitors?
  +decimal profit?
  +decimal cpa?
  +decimal roas?
  +decimal cpc?
  +decimal cpm?
  +decimal cpl?
  +decimal cpi?
  +decimal cpp?
  +decimal poas?
  +decimal arpv?
  +decimal aov?
  +decimal ctr?
  +decimal cvr?
  +datetime computedAt
}
class ManualCost {
  +uuid id
  +string label
  +string category
  +decimal amount_dollar
  +string allocation_type
  +datetime allocation_date?
  +datetime allocation_start?
  +datetime allocation_end?
  +uuid workspace_id
  +datetime created_at
  +datetime updated_at
  +uuid created_by_user_id?
  +string notes?
}
class QaQueryLog {
  +uuid id
  +uuid workspaceId
  +uuid userId
  +string questionText
  +json dslJson
  +datetime createdAt
  +int durationMs
}
Workspace "1" -- "0..*" User : has users
Workspace "1" -- "0..*" Connection : has connections
Workspace "1" -- "1" ComputeRun : runs compute
Workspace "1" -- "0..*" ManualCost : has manual costs
User "1" -- "1" Role : role
User "1" -- "0..*" Connection : asked by
User "1" -- "0..*" QaQueryLog : logs queries
Connection "1" -- "1" Provider : provider
Connection "1" -- "0..*" Token : uses token
Connection "1" -- "0..*" Fetch : schedules
Connection "1" -- "0..*" QaQueryLog : from connection
Fetch "1" -- "0..*" Import : produces
Import "1" -- "0..*" MetricFact : contains facts
MetricFact "1" -- "1" Provider : provider
MetricFact "1" -- "1" Level : level
MetricFact "0..*" -- "0..1" Entity : facts for entity
Entity "1" -- "1" Level : level
ComputeRun "1" -- "0..*" Pnl : writes
Pnl "0..*" -- "0..1" Entity : pnl for entity
Pnl "1" -- "1" Provider : provider
Pnl "1" -- "1" Level : level
Pnl "1" -- "1" Kind : kind
Entity "1" -- "0..1" Goal : goal
```

## Changelog

- 2025-10-05T16:00:00Z: Added hierarchy module for entity ancestor resolution (recursive CTEs)
- 2025-10-05T13:00:00Z: Added GoalEnum and new columns for Derived Metrics v1 (Entity.goal, MetricFact bases, Pnl derived)
