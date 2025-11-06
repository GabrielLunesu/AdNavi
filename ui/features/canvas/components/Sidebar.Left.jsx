// WHAT: Left sidebar — search, filters, toggles
// WHY: Host filtering controls that affect canvas data and visibility
// REFERENCES: docs/canvas/01-functional-spec.md

import React from "react";

export default function SidebarLeft({
  stats = { campaigns: 0, rules: 0, lastSync: null },
  filters = {},
  onChange = () => {},
}) {
  return (
    <div className="flex flex-col h-full">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-sm font-medium text-[#111] uppercase tracking-wide">Workspace</h3>
      </div>
      <div className="flex-1 space-y-6 overflow-y-auto pr-2">
        {/* Search */}
        <div>
          <label className="block text-xs font-medium text-neutral-500 uppercase tracking-wide mb-2">Search</label>
          <input
            type="text"
            placeholder="Search campaigns or rules…"
            value={filters.query || ""}
            onChange={(e) => onChange({ ...filters, query: e.target.value })}
            className="w-full px-3 py-2 rounded-xl bg-white/60 border border-neutral-200/60 text-sm text-[#111] placeholder-neutral-400 focus:outline-none focus:border-[#B9C7F5] transition-all"
          />
        </div>

        {/* Timeframe */}
        <div>
          <h4 className="text-sm font-medium text-[#111] mb-2">Timeframe</h4>
          <div className="flex flex-wrap gap-2">
            {["7d", "30d", "90d"].map((range) => {
              const active = filters.timeframe === range;
              return (
                <button
                  key={range}
                  onClick={() => onChange({ ...filters, timeframe: range })}
                  className={`px-3 py-1 text-xs rounded-full border transition-all ${active ? "bg-[#B9C7F5]/30 border-[#B9C7F5] text-[#111]" : "bg-white/40 border-neutral-200/60 text-neutral-500"}`}
                  type="button"
                >
                  {range.toUpperCase()}
                </button>
              );
            })}
          </div>
        </div>

        {/* Status */}
        <div>
          <h4 className="text-sm font-medium text-[#111] mb-2">Status</h4>
          <div className="flex gap-2">
            {["active", "paused", "all"].map((status) => {
              const active = filters.status === status;
              return (
                <button
                  key={status}
                  onClick={() => onChange({ ...filters, status })}
                  className={`px-3 py-1 text-xs rounded-full border transition-all capitalize ${active ? "bg-[#B9C7F5]/30 border-[#B9C7F5] text-[#111]" : "bg-white/40 border-neutral-200/60 text-neutral-500"}`}
                  type="button"
                >
                  {status}
                </button>
              );
            })}
          </div>
        </div>

        {/* Filters: Platforms */}
        <div>
          <h4 className="text-sm font-medium text-[#111] mb-2">Platforms</h4>
          {[
            { key: "meta", label: "Meta" },
            { key: "google", label: "Google" },
            { key: "tiktok", label: "TikTok" },
          ].map((p) => (
            <div key={p.key} className="flex items-center justify-between px-3 py-2 rounded-xl bg-white/40 border border-neutral-200/40 cursor-pointer mb-2">
              <span className="text-xs font-medium text-[#111]">{p.label}</span>
              <input
                type="checkbox"
                checked={!!filters.platforms?.[p.key]}
                onChange={(e) => onChange({
                  ...filters,
                  platforms: { ...(filters.platforms || {}), [p.key]: e.target.checked },
                })}
                className="w-4 h-4 rounded border-neutral-300"
              />
            </div>
          ))}
        </div>

        {/* Toggles */}
        <div>
          <h4 className="text-sm font-medium text-[#111] mb-2">Toggles</h4>
          {[
            { key: "showEdges", label: "Show edges" },
            { key: "showAds", label: "Show ads" },
          ].map((t) => (
            <div key={t.key} className="flex items-center justify-between px-3 py-2 rounded-xl bg-white/40 border border-neutral-200/40 cursor-pointer mb-2">
              <span className="text-xs font-medium text-[#111]">{t.label}</span>
              <input
                type="checkbox"
                checked={!!filters[t.key]}
                onChange={(e) => onChange({ ...filters, [t.key]: e.target.checked })}
                className="w-4 h-4 rounded border-neutral-300"
              />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
