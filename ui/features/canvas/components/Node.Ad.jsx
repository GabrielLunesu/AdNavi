// WHAT: Ad/Creative node (presentational) — thumbnail placeholder + mini stat
// WHY: Visual consistency for leaf nodes
// REFERENCES: design notes in docs/canvas/01-functional-spec.md

import React from "react";
import { Handle, Position } from "@xyflow/react";

export default function NodeAd({ data }) {
  const { name, kpis = {} } = data || {};
  return (
    <div className="glass-card rounded-2xl border border-neutral-200/40 shadow-lg hover:shadow-xl transition-all cursor-default w-[140px] h-[120px] overflow-hidden">
      <Handle type="target" position={Position.Left} className="w-2 h-2 !bg-[#B9C7F5]" />
      <div className="p-3 relative h-full flex flex-col">
        <div className="flex items-center justify-between mb-2 flex-shrink-0">
          <span className="text-xs font-medium text-[#111] truncate" aria-label={`Ad ${name}`}>{name || "—"}</span>
        </div>
        <div className="w-full h-12 bg-gradient-to-br from-[#B9C7F5]/20 to-[#A5B4FC]/20 rounded-lg mb-2 flex items-center justify-center flex-shrink-0" aria-hidden>
          <span className="text-neutral-400 text-xs">preview</span>
        </div>
        <div className="text-xs text-neutral-500 text-center mt-auto flex-shrink-0">CTR: {kpis.ctr ?? "—"}</div>
      </div>
    </div>
  );
}
