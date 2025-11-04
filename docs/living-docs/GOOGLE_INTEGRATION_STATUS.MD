# Google Ads Integration - Living Status Document

Last Updated: 2025-11-04

Principles: Separation of concerns, single responsibility, modular and elegant code, comment all logic and files (WHAT/WHY/REFERENCES).

---

## Quick Status

- Current Phase: Phase 1 — Client Service (in progress)
- Overall Progress: 10% (Week 1 of 3–4)
- Env Ready: Yes (vars in `.env`)
- Token Model: DB encryption available (shared), Google OAuth TBD

| Component | Status | Notes |
|-----------|--------|-------|
| Dev token + OAuth client | ✅ Ready | Provided via env vars |
| Google Ads Python SDK | ✅ Added | `backend/requirements.txt` pinned to 23.0.0 |
| Client service | ✅ Complete (skeleton + tests) | `app/services/google_ads_client.py` |
| Entity sync endpoints | ✅ Added | Mirror Meta pattern (UPSERT) |
| Metrics sync endpoints | ✅ Added | 90-day backfill + incremental |
| Connection metadata (tz/currency) | ✅ Columns added | Alembic migration `20251104_000001` |
| UI sync button | ✅ Added | Settings page parity with Meta |
| Connect from env | ✅ Added | `POST /connections/google/from-env` + UI auto-connect |

Env keys (configured):
- `GOOGLE_DEVELOPER_TOKEN`
- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `GOOGLE_REFRESH_TOKEN`
- `GOOGLE_LOGIN_CUSTOMER_ID` (MCC)
- `GOOGLE_CUSTOMER_ID` (target account)
- `GOOGLE_ADS_ENVIRONMENT=SANDBOX`

---

## Phases & Tasks

### Phase 0 — Accounts & Credentials (Complete)
- MCC + Developer token configured (uses SANDBOX/test accounts)
- GCP project and Google Ads API enabled
- OAuth client created; refresh token present (env)

Verification (manual):
- Build `GoogleAdsClient` from env and run GAQL to list customers and basic campaign fields

### Phase 1 — Client Service (In Progress)

Goal: Provider-agnostic service encapsulating Google Ads SDK usage (auth, GAQL, pagination, retries, rate limits).

Deliverables:
- `app/services/google_ads_client.py` with:
  - Client factory from env or DB token (future OAuth)
  - GAQL search helpers (stream + paginated)
  - Entity listing: campaigns, ad groups, ads
  - Metrics query: daily performance (cost_micros → spend, clicks/impressions/conversions/value)
  - Robust retries (RESOURCE_EXHAUSTED, backoff+jitter), rate limit guard
  - Campaign type → Goal mapping covering all channel types

Tests:
- `app/tests/test_google_ads_client.py` (mocked SDK, no network)

### Phase 2 — Entity Sync (Complete)
 - Router: `google_sync.py`
 - Endpoint: `POST /workspaces/{id}/connections/{id}/sync-google-entities`
- UPSERT entities: Campaign → AdGroup → Ad (map AdGroup → `adset`)
- Persist campaign statuses: `status`, `serving_status`, `primary_status[_reasons]`
 - Stores timezone/currency on Connection during first sync
 - Tests: helper coverage for ID normalization and chunking

### Phase 3 — Metrics Sync (Complete)
 - Endpoint: `POST /workspaces/{id}/connections/{id}/sync-google-metrics`
- 90-day backfill (7-day chunks), then incremental
- Ingest via existing `ingest_metrics_internal`
 - Level: Ad (ad_group_ad); spend from cost_micros; conversions/value mapped
 - Tests: service + helpers; end-to-end to be added with fixtures

### Phase 4 — Connection Metadata (Pending)
- Store `timezone` and `currency_code` on `Connection`
- Alembic migration + model update
- Populate during first entity sync per connection

### Phase 5 — UI Integration (Complete)
- Settings page parity with Meta
- “Sync Google Ads” button with progress feedback
- Auto-connect from env on Settings load (fallbacks + error-safe)

### Phase 6 — Reliability & Quotas (Pending)
- Exponential backoff using recommended retry delays
- Monitor quotas and version deprecations

### Phase 7 — OAuth Flow (Planned)
- Backend authorize/callback
- Store tokens encrypted (reuse Token model)

---

## Design Decisions

- Two-step sync (entities → metrics) identical to Meta for idempotency and reliability
- Base measures only; derived metrics calculated by `UnifiedMetricService`
- AdGroup mapped to `LevelEnum.adset` for cross-provider consistency
- Campaign goal mapping from `advertising_channel_type` to `GoalEnum` (see below)
- Timezone/currency persisted on `Connection` for accurate windows and display

Goal mapping (initial):
- SEARCH → conversions
- DISPLAY → awareness
- VIDEO → awareness
- PERFORMANCE_MAX → purchases
- SHOPPING → purchases
- HOTEL → purchases
- LOCAL → traffic
- SMART → conversions
- DISCOVERY → traffic
- AUDIO → awareness
- APP → app_installs

Notes: mapping can be refined with sub-types and bidding strategies.

---

## Reference GAQL

Campaign statuses (delivery signals):

SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign.serving_status,
  campaign.primary_status,
  campaign.primary_status_reasons,
  campaign.advertising_channel_type
FROM campaign
ORDER BY campaign.name

Basic performance (no segments → includes zero rows):

SELECT
  campaign.id, campaign.name,
  metrics.impressions, metrics.clicks, metrics.cost_micros,
  metrics.conversions, metrics.conversions_value
FROM campaign
WHERE segments.date DURING LAST_7_DAYS

---

## Testing & Logging

- Unit tests mock SDK; no network in CI
- Log markers: use `[GOOGLE_SYNC]`, `[GOOGLE_CLIENT]` for filtering
- Follow existing comprehensive logging style used in Meta integration

Local test commands:
- `cd backend && pytest app/tests/test_google_ads_client.py app/tests/test_google_sync_helpers.py -q`
- (Migrations) `alembic upgrade head` to add `timezone`/`currency_code` on connections

---

## Next Actions (This Week)

1) Wire UI “Sync Google Ads” button (now active with endpoints)
2) Add integration tests for router with mocked GAdsClient
3) Expand goal mapping with subtypes if needed

---

## Changelog

- 2025-11-04: Converted doc into updateable plan; defined phases, tests, mappings
- 2025-11-04: Added google-ads dependency; added connection tz/currency columns; implemented client service and tests
- 2025-11-04: Added Google sync endpoints; added env-based connection creation; updated Settings UI to auto-connect + show Google Sync button; made Token.access_token_enc nullable
