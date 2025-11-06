// WHAT: React Flow viewport wrapper; registers node types and renders background grid, controls, minimap
// WHY: Encapsulates React Flow provider logic and keeps canvas page lean
// REFERENCES: docs/docs-for-context/react-flow.md

import React, { useCallback, useEffect } from "react";
import { ReactFlow, Background, useNodesState, useEdgesState, addEdge, Position } from "@xyflow/react";

import "@xyflow/react/dist/style.css";

const nodeDefaults = {
  sourcePosition: Position.Right,
  targetPosition: Position.Left,
};

/**
 * FlowViewport
 * @param {Object} props
 * @param {Array} props.initialNodes
 * @param {Array} props.initialEdges
 * @param {Object} props.nodeTypes - Custom node type map (e.g., { campaign: Component })
 * @param {Object} props.options - React Flow options (fitView, snap, etc.)
 * @param {Function} props.onNodeClick
 * @param {Function} props.onPaneClick
 * @param {Function} props.onNodeDragStop
 * @param {string} [props.className]
 */
export default function FlowViewport({
  initialNodes = [],
  initialEdges = [],
  nodeTypes = {},
  options = {},
  onNodeClick,
  onPaneClick,
  onNodeDragStop,
  className = "",
}) {
  const [nodes, setNodes, baseOnNodesChange] = useNodesState(
    (initialNodes || []).map((n) => ({ ...nodeDefaults, ...n }))
  );
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges || []);

  useEffect(() => {
    // Layout is handled by arrangeHierarchy in useCanvasData, so we just use the positions as-is
    const next = (initialNodes || []).map((n) => ({ ...nodeDefaults, ...n }));
    setNodes(next);
  }, [initialNodes, setNodes]);

  useEffect(() => {
    setEdges(initialEdges || []);
  }, [initialEdges, setEdges]);

  const onConnect = useCallback((params) => setEdges((els) => addEdge(params, els)), []);

  // Real-time collision avoidance while dragging
  const onNodesChange = useCallback(
    (changes) => {
      let movedId = null;
      changes.forEach((c) => {
        if (c.type === 'position' && c.dragging) movedId = c.id;
      });
      if (!movedId) return baseOnNodesChange(changes);

      baseOnNodesChange(changes);
      setNodes((current) => {
        const padding = 8;
        const sizeByType = { campaign: { w: 260, h: 160 }, adset: { w: 180, h: 120 }, ad: { w: 140, h: 120 } };
        const me = current.find((n) => n.id === movedId);
        if (!me) return current;
        const sz = sizeByType[me.type] || { w: 180, h: 120 };
        let { x, y } = me.position;
        const rect = () => ({ left: x, top: y, right: x + sz.w, bottom: y + sz.h });
        const intersects = (a, b) => !(a.right + padding < b.left || a.left - padding > b.right || a.bottom + padding < b.top || a.top - padding > b.bottom);
        const others = current.filter((n) => n.id !== movedId);
        let guard = 0;
        while (guard < 80) {
          const a = rect();
          const hit = others.find((o) => {
            const osz = sizeByType[o.type] || sz;
            const b = { left: o.position.x, top: o.position.y, right: o.position.x + osz.w, bottom: o.position.y + osz.h };
            return intersects(a, b);
          });
          if (!hit) break;
          // push-away vector
          if (x <= hit.position.x) x = hit.position.x - sz.w - padding; else x = hit.position.x + (sizeByType[hit.type]?.w || sz.w) + padding;
          y += 0; // minimal vertical change to keep feel stable
          guard += 1;
        }
        return current.map((n) => (n.id === movedId ? { ...n, position: { x, y } } : n));
      });
    },
    [baseOnNodesChange, setNodes]
  );

  // Basic collision-avoidance on drag stop: nudges the node until no overlapping
  const handleDragStop = useCallback((evt, node) => {
    const padding = 8;
    const sizeByType = {
      campaign: { w: 260, h: 160 },
      adset: { w: 180, h: 120 },
      ad: { w: 140, h: 120 },
    };
    const sz = sizeByType[node.type] || { w: 180, h: 120 };
    setNodes((current) => {
      const others = current.filter((n) => n.id !== node.id);
      let { x, y } = node.position;
      const rect = () => ({ left: x, top: y, right: x + sz.w, bottom: y + sz.h });
      const intersects = (a, b) => !(a.right + padding < b.left || a.left - padding > b.right || a.bottom + padding < b.top || a.top - padding > b.bottom);
      let guard = 0;
      while (guard < 200) {
        const a = rect();
        const hit = others.find((o) => {
          const osz = sizeByType[o.type] || sz;
          const b = { left: o.position.x, top: o.position.y, right: o.position.x + osz.w, bottom: o.position.y + osz.h };
          return intersects(a, b);
        });
        if (!hit) break;
        y += sz.h / 2; // nudge down
        guard += 1;
      }
      return current.map((n) => (n.id === node.id ? { ...n, position: { x, y } } : n));
    });
    onNodeDragStop && onNodeDragStop(node);
  }, [setNodes, onNodeDragStop]);

  return (
    <div className={`relative w-full h-full rounded-2xl overflow-hidden ${className}`}>
      {/* Subtle dot grid as a fallback background if theming disables Background */}
      <svg className="absolute inset-0 w-full h-full pointer-events-none" aria-hidden="true" style={{ zIndex: 0 }}>
        <defs>
          <pattern id="grid" width="12" height="12" patternUnits="userSpaceOnUse">
            <circle cx="1" cy="1" r="0.5" fill="#E4E7EC" opacity="0.3"></circle>
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#grid)"></rect>
      </svg>

      <div className="relative z-10 w-full h-full">
        <ReactFlow
          nodes={nodes}
          edges={edges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          onConnect={onConnect}
          nodeTypes={nodeTypes}
          fitView={options.fitView !== false}
          fitViewOptions={options.fitViewOptions || { padding: 0.2, maxZoom: 1 }}
          defaultViewport={options.defaultViewport}
          onNodeClick={onNodeClick}
          onPaneClick={onPaneClick}
          onNodeDragStop={handleDragStop}
          {...options}
        >
          <Background />
        </ReactFlow>
      </div>
    </div>
  );
}
