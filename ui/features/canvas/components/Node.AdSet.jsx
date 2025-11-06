// WHAT: AdSet node (presentational) — compact metrics
// WHY: Visual consistency across mid-level entities
// REFERENCES: design notes in docs/canvas/01-functional-spec.md

import React from "react";
import { Handle, Position } from "@xyflow/react";

export default function NodeAdSet({ data }) {
  const { name, status, kpis = {} } = data || {};
  return (
    <div className="glass-card rounded-2xl border border-neutral-200/40 shadow-lg hover:shadow-xl transition-all cursor-default w-[180px] h-[120px] overflow-hidden">
      <Handle type="target" position={Position.Left} className="w-2 h-2 !bg-[#B9C7F5]" />
      <Handle type="source" position={Position.Right} className="w-2 h-2 !bg-[#B9C7F5]" />
      <div className="p-3 relative h-full flex flex-col">
        <div className="flex items-start justify-between mb-2 flex-shrink-0">
          <h4 className="text-xs font-medium text-[#111] truncate flex-1 pr-2" aria-label={`Ad set ${name}`}>{name || "—"}</h4>
          <div className={`w-1.5 h-1.5 rounded-full flex-shrink-0 ${status === "active" ? "bg-green-500" : status === "paused" ? "bg-amber-500" : "bg-neutral-400"}`}></div>
        </div>
        <div className="space-y-1.5 mb-2 flex-shrink-0">
          <KeyValue label="Spend" value={kpis.spend ?? "—"} />
          <KeyValue label="ROAS" value={kpis.roas ?? "—"} highlight />
        </div>
        <div className="h-8 bg-neutral-100/60 rounded-lg mt-auto flex-shrink-0" aria-hidden="true"></div>
      </div>
    </div>
  );
}

function KeyValue({ label, value, highlight = false }) {
  return (
    <div className="flex items-center justify-between">
      <span className="text-[10px] text-neutral-500">{label}</span>
      <span className={`text-xs font-medium ${highlight ? "text-[#B9C7F5]" : "text-[#111]"}`}>{value}</span>
    </div>
  );
}
