/**
 * Finance API Client
 * 
 * WHAT: Thin client for Finance/P&L endpoints
 * WHY: Centralized API calls with error handling, no business logic
 * REFERENCES:
 *   - lib/api.js: Similar pattern for KPI data
 *   - lib/pnlAdapter.js: Consumes these responses
 *   - app/(dashboard)/finance/page.jsx: Uses this client
 * 
 * Design:
 *   - All requests include workspace ID (from context/cookie)
 *   - Returns raw API responses (adapter handles mapping)
 *   - Throws on errors (caller handles)
 */

import { getApiBase } from './config';

const BASE = getApiBase();

/**
 * Get P&L statement for a period.
 * 
 * @param {Object} params
 * @param {string} params.workspaceId - Workspace UUID
 * @param {string} params.granularity - "month" (now) or "day" (future)
 * @param {string} params.periodStart - ISO date (YYYY-MM-DD)
 * @param {string} params.periodEnd - ISO date (YYYY-MM-DD, exclusive)
 * @param {boolean} params.compare - Include previous period comparison
 * @returns {Promise<PnLStatementResponse>}
 */
export async function getPnLStatement({ workspaceId, granularity = 'month', periodStart, periodEnd, compare = false }) {
  const params = new URLSearchParams({
    granularity,
    period_start: periodStart,
    period_end: periodEnd,
    compare: compare.toString()
  });
  
  const res = await fetch(`${BASE}/workspaces/${workspaceId}/finance/pnl?${params}`, {
    method: 'GET',
    credentials: 'include',
    headers: { 'Content-Type': 'application/json' }
  });
  
  if (!res.ok) {
    const msg = await res.text();
    throw new Error(`Failed to fetch P&L: ${res.status} ${msg}`);
  }
  
  return res.json();
}

/**
 * Create a manual cost entry.
 * 
 * @param {Object} params
 * @param {string} params.workspaceId
 * @param {Object} params.cost - ManualCostCreate payload
 * @returns {Promise<ManualCostOut>}
 */
export async function createManualCost({ workspaceId, cost }) {
  const res = await fetch(`${BASE}/workspaces/${workspaceId}/finance/costs`, {
    method: 'POST',
    credentials: 'include',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(cost)
  });
  
  if (!res.ok) {
    const msg = await res.text();
    throw new Error(`Failed to create manual cost: ${res.status} ${msg}`);
  }
  
  return res.json();
}

/**
 * List all manual costs for workspace.
 * 
 * @param {Object} params
 * @param {string} params.workspaceId
 * @returns {Promise<ManualCostOut[]>}
 */
export async function listManualCosts({ workspaceId }) {
  const res = await fetch(`${BASE}/workspaces/${workspaceId}/finance/costs`, {
    method: 'GET',
    credentials: 'include',
    headers: { 'Content-Type': 'application/json' }
  });
  
  if (!res.ok) {
    const msg = await res.text();
    throw new Error(`Failed to list manual costs: ${res.status} ${msg}`);
  }
  
  return res.json();
}

/**
 * Update a manual cost entry.
 * 
 * @param {Object} params
 * @param {string} params.workspaceId
 * @param {string} params.costId
 * @param {Object} params.updates - ManualCostUpdate payload
 * @returns {Promise<ManualCostOut>}
 */
export async function updateManualCost({ workspaceId, costId, updates }) {
  const res = await fetch(`${BASE}/workspaces/${workspaceId}/finance/costs/${costId}`, {
    method: 'PUT',
    credentials: 'include',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(updates)
  });
  
  if (!res.ok) {
    const msg = await res.text();
    throw new Error(`Failed to update manual cost: ${res.status} ${msg}`);
  }
  
  return res.json();
}

/**
 * Delete a manual cost entry.
 * 
 * @param {Object} params
 * @param {string} params.workspaceId
 * @param {string} params.costId
 * @returns {Promise<void>}
 */
export async function deleteManualCost({ workspaceId, costId }) {
  const res = await fetch(`${BASE}/workspaces/${workspaceId}/finance/costs/${costId}`, {
    method: 'DELETE',
    credentials: 'include',
    headers: { 'Content-Type': 'application/json' }
  });
  
  if (!res.ok) {
    const msg = await res.text();
    throw new Error(`Failed to delete manual cost: ${res.status} ${msg}`);
  }
  
  // DELETE returns 204 No Content
  return;
}



