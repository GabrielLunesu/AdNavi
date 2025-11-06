---
title: Canvas Data Sync & Layout
status: draft
---

# Overview

Campaign Canvas now renders live campaign → ad set → ad data directly from the production database. The feature keeps platform syncs (Meta/Google/TikTok) unchanged; pressing **Sync** inside the Canvas only re-queries our own APIs so the graph always reflects the freshest ingested facts and rollups.

This note documents:

- The source tables + backend contracts used by the Canvas.
- The client-side fetch cascade that builds a complete entity tree.
- How nodes/edges are mapped and laid out to avoid overlap.
- Toolbar sync behaviour and state handling.
- Extension points for near-real-time updates down the road.

The intent is to make future backend or UI contributors productive without re-reading the repo findings doc.

## Data Sources (Backend)

- `entities` — canonical hierarchy (campaign/ad set/ad/creative) with `parent_id` links.
- `metric_facts` — raw ingest metrics keyed by entity and event date.
- `pnls` — snapshot/rollup metrics for faster reads.

The existing `entity-performance` FastAPI router aggregates across those tables and drives both the Campaigns list and the Canvas. No new backend endpoints were added.

## Fetch Flow (Frontend)

All data access happens inside `ui/features/canvas/hooks/useCanvasData.js`. The hook exposes `{ nodes, edges, loading, error, reload, lastSyncedAt }`.

1. **Campaign list** — `fetchEntityPerformance({ entityLevel: "campaign" })`.
2. **Ad set children** — one call per campaign (`/{campaignId}/children`).
3. **Ads under each ad set** — conditional (only when the **Show Ads** filter is on). One call per ad set ID (`/{adsetId}/children`).
4. Responses are adapted with `adaptEntityPerformance` so display and raw metrics stay consistent with the Campaigns page.
5. `entitiesToNodesAndEdges` converts the adapted payload into React Flow nodes/edges while preserving the full path (campaign → ad set → ad).
6. `arrangeHierarchy` deterministically positions every node into three columns with fixed gaps, preventing overlap on load or refetch.

Entity-performance results are cached per request signature via `ui/lib/campaignsApiClient.js`. The Canvas hook clears that cache before refetching to guarantee fresh numbers.

## Mapping & Layout

- **Mapping** (`ui/features/canvas/lib/mapping.js`)
  - Always emits structural edges even when lines are hidden; when the Filters panel toggles edges off, the edges remain but are flagged `hidden` so React Flow skips rendering them without losing layout references.
  - Ads default to the same custom renderer as creatives; other levels can plug in specialised components later.

- **Layout** (`ui/features/canvas/lib/layout.js`)
  - Treats each campaign as an independent group positioned horizontally.
  - Calculates the tallest child “lane” so campaigns stay vertically centred.
  - Ad sets and ads share lane indexes to keep lines straight, no matter how many ads an ad set contains.

## Toolbar Sync

`CanvasPage` wires the Toolbar’s **Sync** button to the hook’s `reload` function:

1. Clear the entity-performance cache.
2. Kick off all three fetch tiers (campaigns, ad sets, ads).
3. Disable the button + show `Syncing…` until the hook reports `loading === false`.
4. Stamp `lastSyncedAt` (local time) for the footer display.

Because the hook keeps `useMock` support, local designers can still opt into static data by flipping the flag.

## Error & Empty States

- Any fetch failure bubbles up; the hook surfaces `error` and the page displays a centered error message.
- If filters yield no matches, the search reducer returns an empty graph.
- Layout always runs, even for empty arrays, ensuring React Flow mounts with a stable viewport.

## Future Enhancements

- **Batching** — A dedicated `/canvas/tree` endpoint could replace the N+1 pattern if campaigns/ad sets scale higher.
- **SSE/WebSockets** — push notifications could call `reload()` to achieve near-live updates without UI changes.
- **Persisted layout** — current positions are deterministic from data; storing user adjustments per workspace would be an incremental addition around the layout helper.
- **Edge theming** — hidden edges already exist logically; swapping styles or animations is confined to `makeEdge` in the mapper.

Questions or follow-ups? Ping #canvas or check `docs/canvas/01-functional-spec.md` for the product brief.
