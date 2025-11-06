// WHAT: Constants for canvas nodes/edges and React Flow options
// WHY: Single place for sizing, spacing, z-index, and viewport options
// REFERENCES: docs/canvas/01-functional-spec.md

export const NODE_SIZES = {
  campaign: { w: 260, h: 160 },
  adset: { w: 180, h: 120 },
  ad: { w: 140, h: 120 },
};

export const Z_INDEX = {
  background: 0,
  edges: 5,
  nodes: 10,
  overlays: 20,
};

export const FLOW_OPTIONS = {
  fitView: true,
  proOptions: { hideAttribution: true },
};

export const COLORS = {
  accent: "#B9C7F5",
  accent2: "#A5B4FC",
  gridDot: "#E4E7EC",
};

