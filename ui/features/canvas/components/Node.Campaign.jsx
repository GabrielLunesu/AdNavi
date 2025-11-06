// WHAT: Campaign node (presentational) — title, status, 3 KPIs, sparkline placeholder
// WHY: Visual consistency across campaign-level entities
// REFERENCES: design notes in docs/canvas/01-functional-spec.md

import React from "react";
import { Handle, Position } from "@xyflow/react";

export default function NodeCampaign({ data }) {
  const { name, status, kpis = {}, platform } = data || {};
  return (
    <div className="glass-card rounded-2xl border border-neutral-200/40 shadow-lg hover:shadow-xl transition-all cursor-default w-[260px] h-[160px] overflow-hidden">
      {/* Handles for linking */}
      <Handle type="target" position={Position.Left} className="w-2 h-2 !bg-[#B9C7F5]" />
      <Handle type="source" position={Position.Right} className="w-2 h-2 !bg-[#B9C7F5]" />
      <div className="p-4 relative h-full flex flex-col">
        <div className="flex items-start justify-between mb-2">
          <h3 className="text-sm font-medium text-[#111] tracking-tight truncate flex-1 pr-2" aria-label={`Campaign ${name}`}>{name || "—"}</h3>
          <div className={`w-2 h-2 rounded-full flex-shrink-0 ${status === "active" ? "bg-green-500" : status === "paused" ? "bg-amber-500" : "bg-neutral-400"}`}></div>
        </div>
        <div className="space-y-1.5 mb-2 flex-shrink-0">
          <KeyValue label="ROAS" value={kpis.roas ?? "—"} />
          <KeyValue label="Spend" value={kpis.spend ?? "—"} />
          <KeyValue label="CPA" value={kpis.cpa ?? "—"} />
        </div>
        <div className="h-8 bg-neutral-100/60 rounded-lg mb-2 flex-shrink-0" aria-hidden="true"></div>
        <div className="flex items-center justify-between pt-2 mt-auto border-t border-neutral-200/40 text-[10px] text-neutral-500 flex-shrink-0">
          <span className="px-2 py-0.5 rounded-full bg-white/60 border border-neutral-200/60 truncate max-w-[100px]">{platform || "—"}</span>
          <span className="text-neutral-400 truncate ml-2">demo</span>
        </div>
      </div>
    </div>
  );
}

function KeyValue({ label, value }) {
  return (
    <div className="flex items-center justify-between">
      <span className="text-[10px] text-neutral-500 uppercase tracking-wide">{label}</span>
      <span className="text-sm font-medium text-[#111]">{value}</span>
    </div>
  );
}
