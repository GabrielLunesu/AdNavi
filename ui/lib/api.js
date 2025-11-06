// API client focused on KPI consumption.
// All functions return plain JSON and throw on non-2xx.
// WHY: centralizing fetch keeps pages dumb and testable.

import { getApiBase } from './config';

const BASE = getApiBase(); 



export async function fetchWorkspaceKpis({
  workspaceId,
  metrics = ["spend","revenue","conversions","roas"],
  lastNDays = 7,
  dayOffset = 0,
  compareToPrevious = true,
  sparkline = true,
  provider = null,
  level = null,
  onlyActive = false,
  customStartDate = null,
  customEndDate = null,
  entityName = null
}) {
  const params = new URLSearchParams();
  if (provider) params.set("provider", provider);
  if (level) params.set("level", level);
  if (entityName) params.set("entity_name", entityName);
  if (onlyActive) params.set("only_active", "true");
  else params.set("only_active", "false");

  // Format dates as YYYY-MM-DD
  const formatDate = (date) => {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
  };

  // Calculate time range based on different scenarios
  let timeRange;
  if (customStartDate && customEndDate) {
    // Use custom date range
    timeRange = {
      start: customStartDate,
      end: customEndDate
    };
  } else if (dayOffset > 0) {
    // Calculate specific dates for offset (e.g., yesterday)
    const end = new Date();
    end.setDate(end.getDate() - dayOffset);
    const start = new Date(end);
    start.setDate(start.getDate() - lastNDays + 1);
    
    timeRange = {
      start: formatDate(start),
      end: formatDate(end)
    };
  } else {
    // Use last_n_days for regular cases
    timeRange = { last_n_days: lastNDays };
  }

  const res = await fetch(`${BASE}/workspaces/${workspaceId}/kpis?${params.toString()}`, {
    method: "POST",
    credentials: "include",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      metrics,
      time_range: timeRange,
      compare_to_previous: compareToPrevious,
      sparkline
    })
  });
  if (!res.ok) {
    const msg = await res.text();
    throw new Error(`KPI fetch failed: ${res.status} ${msg}`);
  }
  return res.json();
}

// Call backend QA endpoint (DSL v1.1).
// WHY: isolate fetch logic, keeps components testable and clean.
//
// Returns:
// {
//   answer: "Your ROAS for the selected period is 2.45. That's a +19.0% change vs the previous period.",
//   executed_dsl: { metric: "roas", time_range: {...}, ... },
//   data: { summary: 2.45, previous: 2.06, delta_pct: 0.189, timeseries: [...], breakdown: [...] }
// }
//
// The backend uses a DSL pipeline:
// 1. Canonicalize question (synonym mapping)
// 2. Translate to DSL via LLM (GPT-4o-mini, temp=0, JSON mode)
// 3. Validate DSL (Pydantic)
// 4. Plan execution (resolve dates, map metrics)
// 5. Execute via SQLAlchemy (workspace-scoped, safe math)
// 6. Build human-readable answer (template-based)
// 7. Log to telemetry (success/failure tracking)
export async function fetchQA({ workspaceId, question }) {
  const res = await fetch(
    `${BASE}/qa/?workspace_id=${workspaceId}`,
    {
      method: "POST",
      credentials: "include",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question })
    }
  );
  if (!res.ok) {
    const msg = await res.text();
    throw new Error(`QA failed: ${res.status} ${msg}`);
  }
  return res.json();
}

// Fetch workspace summary for sidebar.
// WHY: one tiny endpoint keeps sidebar up to date without heavy joins.
export async function fetchWorkspaceInfo(workspaceId) {
  const res = await fetch(`${BASE}/workspaces/${workspaceId}/info`, {
    method: "GET",
    credentials: "include",
    headers: { "Content-Type": "application/json" }
  });
  if (!res.ok) {
    const msg = await res.text();
    throw new Error(`Failed to load workspace info: ${res.status} ${msg}`);
  }
  return res.json();
}

export async function fetchQaLog(workspaceId) {
  const res = await fetch(`${BASE}/qa-log/${workspaceId}`, {
    method: "GET",
    credentials: "include",
    headers: { "Content-Type": "application/json" }
  });
  if (!res.ok) {
    const msg = await res.text();
    throw new Error(`Failed to fetch QA log: ${res.status} ${msg}`);
  }
  return res.json();
}

export async function createQaLog(workspaceId, { question_text, answer_text, dsl_json }) {
  const res = await fetch(`${BASE}/qa-log/${workspaceId}`, {
    method: "POST",
    credentials: "include",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question_text, answer_text, dsl_json })
  });
  if (!res.ok) {
    const msg = await res.text();
    throw new Error(`Failed to create QA log: ${res.status} ${msg}`);
  }
  return res.json();
}

// Fetch available providers (ad platforms) in workspace.
// WHY: Dynamic provider filter buttons in Analytics page.
// Returns: { providers: ["google", "meta", "tiktok", "other"] }
export async function fetchWorkspaceProviders({ workspaceId }) {
  const res = await fetch(`${BASE}/workspaces/${workspaceId}/providers`, {
    method: "GET",
    credentials: "include",
    headers: { "Content-Type": "application/json" }
  });
  if (!res.ok) {
    const msg = await res.text();
    throw new Error(`Failed to fetch providers: ${res.status} ${msg}`);
  }
  return res.json();
}

// Fetch campaigns for dropdown filtering.
// WHY: Chart grouping by campaign requires campaign list.
// Returns: { campaigns: [{ id, name, status }, ...] }
export async function fetchWorkspaceCampaigns({ 
  workspaceId, 
  provider = null, 
  status = 'active' 
}) {
  const params = new URLSearchParams();
  if (provider) params.set('provider', provider);
  if (status) params.set('entity_status', status);
  
  const res = await fetch(`${BASE}/workspaces/${workspaceId}/campaigns?${params.toString()}`, {
    method: "GET",
    credentials: "include",
    headers: { "Content-Type": "application/json" }
  });
  if (!res.ok) {
    const msg = await res.text();
    throw new Error(`Failed to fetch campaigns: ${res.status} ${msg}`);
  }
  return res.json();
}

// Fetch ad platform connections for workspace.
// WHY: Settings page needs to display connected accounts.
// Returns: { connections: [{ id, provider, name, external_account_id, status, connected_at }, ...], total: number }
export async function fetchConnections({ workspaceId, provider = null, status = null }) {
  const params = new URLSearchParams();
  if (provider) params.set('provider', provider);
  if (status) params.set('status', status);
  
  const res = await fetch(`${BASE}/connections?${params.toString()}`, {
    method: "GET",
    credentials: "include",
    headers: { "Content-Type": "application/json" }
  });
  if (!res.ok) {
    const msg = await res.text();
    throw new Error(`Failed to fetch connections: ${res.status} ${msg}`);
  }
  return res.json();
}

// Ensure Google connection exists using server-side env.
// WHAT: Creates or updates a Google connection and stores encrypted refresh token.
// WHY: Temporary path before OAuth UI; enables sync button to appear.
export async function ensureGoogleConnectionFromEnv() {
  const res = await fetch(`${BASE}/connections/google/from-env`, {
    method: "POST",
    credentials: "include",
    headers: { "Content-Type": "application/json" }
  });
  if (!res.ok) {
    // Return null on failure to avoid blocking Settings load
    return null;
  }
  return res.json();
}

// Ensure Meta connection exists using server-side env.
// WHAT: Creates or updates a Meta connection and stores encrypted access token.
// WHY: Temporary path before OAuth UI; enables sync button to appear.
export async function ensureMetaConnectionFromEnv() {
  const res = await fetch(`${BASE}/connections/meta/from-env`, {
    method: "POST",
    credentials: "include",
    headers: { "Content-Type": "application/json" }
  });
  if (!res.ok) {
    // Return null on failure to avoid blocking Settings load
    return null;
  }
  return res.json();
}

// Sync Meta Ads entities (campaigns, adsets, ads).
// WHY: UI sync button triggers entity sync.
// Returns: { success: boolean, synced: { campaigns_created, campaigns_updated, adsets_created, adsets_updated, ads_created, ads_updated, duration_seconds }, errors: [] }
export async function syncMetaEntities({ workspaceId, connectionId }) {
  const res = await fetch(`${BASE}/workspaces/${workspaceId}/connections/${connectionId}/sync-entities`, {
    method: "POST",
    credentials: "include",
    headers: { "Content-Type": "application/json" }
  });
  if (!res.ok) {
    const msg = await res.text();
    throw new Error(`Failed to sync entities: ${res.status} ${msg}`);
  }
  return res.json();
}

// Sync Meta Ads metrics (insights).
// WHY: UI sync button triggers metrics sync after entities.
// Returns: { success: boolean, synced: { facts_ingested, facts_skipped, date_range, ads_processed, duration_seconds }, errors: [] }
export async function syncMetaMetrics({ workspaceId, connectionId, startDate = null, endDate = null, forceRefresh = false }) {
  const body = {};
  if (startDate) body.start_date = startDate;
  if (endDate) body.end_date = endDate;
  if (forceRefresh) body.force_refresh = forceRefresh;
  
  const res = await fetch(`${BASE}/workspaces/${workspaceId}/connections/${connectionId}/sync-metrics`, {
    method: "POST",
    credentials: "include",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  });
  if (!res.ok) {
    const msg = await res.text();
    throw new Error(`Failed to sync metrics: ${res.status} ${msg}`);
  }
  return res.json();
}

// Sync Google Ads entities (customers' campaigns, ad groups, ads).
// WHAT: Same endpoint shape as Meta, routed to Google sync on backend.
// WHY: Parity in UI; separation of concerns via shared path per connection.
// REFERENCES: backend/app/routers (google_sync planned)
export async function syncGoogleEntities({ workspaceId, connectionId }) {
  const res = await fetch(`${BASE}/workspaces/${workspaceId}/connections/${connectionId}/sync-google-entities`, {
    method: "POST",
    credentials: "include",
    headers: { "Content-Type": "application/json" }
  });
  if (!res.ok) {
    const msg = await res.text();
    throw new Error(`Failed to sync entities: ${res.status} ${msg}`);
  }
  return res.json();
}

// Sync Google Ads metrics (daily performance).
// WHAT: 90-day backfill + incremental; same path shape.
// WHY: Keep UI consistent across providers.
export async function syncGoogleMetrics({ workspaceId, connectionId, startDate = null, endDate = null, forceRefresh = false }) {
  const body = {};
  if (startDate) body.start_date = startDate;
  if (endDate) body.end_date = endDate;
  if (forceRefresh) body.force_refresh = forceRefresh;
  
  const res = await fetch(`${BASE}/workspaces/${workspaceId}/connections/${connectionId}/sync-google-metrics`, {
    method: "POST",
    credentials: "include",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  });
  if (!res.ok) {
    const msg = await res.text();
    throw new Error(`Failed to sync metrics: ${res.status} ${msg}`);
  }
  return res.json();
}
