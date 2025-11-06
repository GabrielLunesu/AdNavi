---
title: Campaign Canvas — Feature Module
status: scaffold
---

WHAT
- Read-only visual canvas to inspect Campaign → AdSet → Ad/Creative hierarchies with mini metrics, zoom/pan/drag, selection, and contextual sidebars.

WHY
- Investor-grade, futuristic UX for understanding campaign structures and future automations. Non-breaking: no backend changes or existing route changes in this stage.

REFERENCES
- docs/canvas/01-functional-spec.md
- docs/canvas/02-repo-findings.md
- React Flow docs: docs/docs-for-context/react-flow.md

NOTES
- This folder is self-contained (components, hooks, lib, mocks). No cross-imports outside `ui/features/canvas/*` except for existing APIs/adapters.
- Uses JSX (no TypeScript). Typings via JSDoc in `lib/types.js`.
- React Flow will be lazy-loaded at the page level in a later PR (PR-2). This scaffold does not import canvas files anywhere yet, so it adds zero bundle cost.

Structure
- components: presentational building blocks (shell, nodes, sidebars, toolbar, legends)
- hooks: data, layout persistence, selection
- lib: mapping, formatting, constants, typedefs
- mock: demo dataset for storybook/demo

Performance
- Target ≤ 200KB extra JS for the feature. Use route-level dynamic imports in the page (PR-2).

Accessibility
- Nodes must be focusable with clear focus outlines and ARIA labels. Sidebars and toolbar provide role attributes. Keyboard panning to rely on React Flow defaults.

