// WHAT: Selected node/edge state + helpers
// WHY: Centralize selection logic (inspector, highlights)
// REFERENCES: docs/canvas/01-functional-spec.md

import { useCallback, useState } from "react";

export default function useCanvasSelection() {
  const [selection, setSelection] = useState(null);

  const selectNode = useCallback((node) => setSelection({ type: 'node', ...node }), []);
  const selectEdge = useCallback((edge) => setSelection({ type: 'edge', ...edge }), []);
  const clearSelection = useCallback(() => setSelection(null), []);

  return { selection, selectNode, selectEdge, clearSelection };
}

