// WHAT: Thin client for campaign/ad set performance API.
// WHY: Keeps fetch logic centralized so pages/components stay dumb.
// REFERENCES:
//   - backend/app/routers/entity_performance.py (routes, query params)
//   - app/schemas.py::EntityPerformanceResponse (DTO contract)

import { getApiBase } from './config';

const BASE = getApiBase();

const cache = new Map();

const buildKey = (level, parentId, params) => {
  return JSON.stringify({ level, parentId, params });
};

const fetchJson = async (url, init) => {
  const res = await fetch(url, {
    credentials: 'include',
    headers: { 'Content-Type': 'application/json' },
    ...init,
  });
  if (!res.ok) {
    const msg = await res.text();
    throw new Error(`Campaigns API failed: ${res.status} ${msg}`);
  }
  return res.json();
};

export async function fetchEntityPerformance({
  workspaceId,
  entityLevel,
  parentId = null,
  dateStart = null,
  dateEnd = null,
  timeframe = '7d',
  platform = null,
  status = 'active',
  sortBy = 'roas',
  sortDir = 'desc',
  page = 1,
  pageSize = 25,
}) {
  // Build params based on whether we're fetching children or list
  const params = new URLSearchParams({
    timeframe,
    sort_by: sortBy,
    sort_dir: sortDir,
    page: String(page),
    page_size: String(pageSize),
  });
  
  // Only add entity_level for list endpoint (not children)
  if (!parentId) {
    params.set('entity_level', entityLevel);
  }
  
  if (dateStart && dateEnd) {
    params.set('date_start', dateStart);
    params.set('date_end', dateEnd);
  }
  if (platform) params.set('platform', platform);
  if (status) params.set('status', status);

  const key = buildKey(entityLevel, parentId, params.toString());
  if (cache.has(key)) {
    return cache.get(key);
  }

  const url = parentId
    ? `${BASE}/entity-performance/${parentId}/children?${params.toString()}`
    : `${BASE}/entity-performance/list?${params.toString()}`;

  const data = await fetchJson(url);
  cache.set(key, data);
  return data;
}

export function invalidateEntityPerformanceCache() {
  cache.clear();
}


