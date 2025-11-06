// WHAT: Simple client-side feature flags
// WHY: Safely gate new features (like Canvas) without backend changes
// REFERENCES: docs/canvas/02-repo-findings.md

export const features = {
  // Campaign Canvas (React Flow)
  // Set to true to expose /canvas route and nav entry
  canvas: true,
};

export default features;
