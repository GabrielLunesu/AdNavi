---
title: Campaign Canvas — Functional Spec
status: scaffold
---

Scope
- Read-only visualization of Campaign → AdSet → Ad/Creative hierarchy.
- Interactions: pan/zoom, select nodes, drag nodes (local only), hover states.
- Sidebars: Left (search/filters), Right (Inspector + Rule UI preview).
- No backend changes. Reuse `entity-performance` endpoints.

User Flows
- Open Canvas (via route in PR-2) → viewport renders campaigns; selecting a node opens Inspector.
- Filters (left) adjust platforms/toggles (show edges/ads).
- Toolbar actions: Add Rule (opens right sidebar in Rules tab — placeholder), Sync (call existing sync endpoints), Export (future).

Data
- Fetch via `ui/lib/campaignsApiClient.js` and adapt with `ui/lib/campaignsAdapter.js`.
- Build Canvas nodes/edges on client using `ui/features/canvas/lib/mapping.js`.
- Persist layout to `localStorage` per workspace.

Accessibility
- Nodes focusable with keyboard; Inspector/toolbar/filters have clear labels.
- Contrast ≥ 4.5; focus outlines present.

Performance
- Lazy-load React Flow at page level; keep Canvas bundle additions minimal.

Non-functional Rule UI
- Display fields (metric/operator/value/action/schedule) with disabled save. Expose `onSaveDraft` prop as no-op.

Feature Flag
- Client-side `features.canvas` controls visibility (off by default).

