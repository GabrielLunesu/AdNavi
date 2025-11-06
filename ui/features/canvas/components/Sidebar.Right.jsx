// WHAT: Right sidebar (Inspector / Rule UI placeholder)
// WHY: Contextual panel for selected node info and future rule editor (non-functional)
// REFERENCES: docs/canvas/01-functional-spec.md

import React from "react";

export default function SidebarRight({ selection = null, onClose = () => {}, onSaveDraft = () => {} }) {
  const hasSelection = Boolean(selection);
  const title = selection?.data?.name || "Inspector";
  return (
    <div className="flex flex-col h-full bg-white">
      <div className="p-4 border-b border-neutral-200/40 flex items-center justify-between">
        <h3 className="text-base font-medium text-[#111]">{title}</h3>
        <button
          onClick={onClose}
          className="w-6 h-6 rounded-lg bg-white/40 border border-neutral-200/40 hover:border-red-400/40 transition-all flex items-center justify-center"
          aria-label="Close inspector"
        >
          <span className="text-neutral-600 text-xs">×</span>
        </button>
      </div>
      <div className="flex items-center border-b border-neutral-200/40">
        {['Overview', 'Entities', 'Rules', 'Notes'].map((t, i) => (
          <button key={t} className={`flex-1 px-4 py-3 text-sm font-medium ${i === 0 ? 'text-[#111] border-b-2 border-[#B9C7F5]' : 'text-neutral-500 hover:text-[#111]'}`}>{t}</button>
        ))}
      </div>
      <div className="flex-1 overflow-y-auto p-4">
        {!hasSelection && (
          <div className="h-full flex items-center justify-center text-sm text-neutral-500">
            Select a campaign, ad set, or ad to view details.
          </div>
        )}

        {hasSelection && (
          <div className="space-y-3">
            <InfoRow label="Status" value={selection?.data?.status} />
            <InfoRow label="Platform" value={selection?.data?.platform} />
            <InfoRow label="ROAS" value={selection?.data?.kpis?.roas} />
            <InfoRow label="Spend" value={selection?.data?.kpis?.spend} />
            <InfoRow label="CPA" value={selection?.data?.kpis?.cpa} />
            <InfoRow label="CTR" value={selection?.data?.kpis?.ctr} />
            <InfoRow label="Conversions" value={selection?.data?.kpis?.conversions} />

            {/* Rule Editor (non-functional) */}
            <div className="bg-white rounded-2xl p-3 border border-[#B9C7F5]/30">
              <h5 className="text-xs font-medium text-[#111] uppercase tracking-wide mb-2">Rule Editor (Preview)</h5>
              <div className="grid grid-cols-2 gap-2">
                <Select label="Metric" options={["ROAS","CPA","Spend","Conversions"]} />
                <Select label="Operator" options={[">","<","=","≥","≤"]} />
                <Input label="Value" type="number" defaultValue="3" />
                <Select label="Action" options={["Increase budget by 25%","Decrease budget by 25%","Pause campaign","Send notification"]} />
                <Select label="Schedule" options={["Recheck every 6 hours","Recheck every 12 hours","Recheck daily","One-time"]} className="col-span-2" />
              </div>
              <div className="pt-3">
                <button
                  onClick={() => onSaveDraft(null)}
                  disabled
                  className="w-full px-4 py-2 rounded-full bg-gradient-to-r from-[#B9C7F5] to-[#A5B4FC] text-white text-sm font-medium opacity-70 cursor-not-allowed"
                >
                  Save & Activate (soon)
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

function InfoRow({ label, value }) {
  const display = value == null || value === "" ? "—" : String(value);
  return (
    <div className="flex items-center justify-between text-sm">
      <span className="text-neutral-500">{label}</span>
      <span className="text-[#111] font-medium">{display}</span>
    </div>
  );
}

function Select({ label, options = [], className = "" }) {
  return (
    <div className={className}>
      <label className="block text-xs font-medium text-neutral-500 uppercase tracking-wide mb-1">{label}</label>
      <select className="w-full px-3 py-2 rounded-xl bg-white/60 border border-neutral-200/60 text-sm text-[#111] focus:outline-none focus:border-[#B9C7F5] transition-all">
        {options.map((opt) => <option key={opt}>{opt}</option>)}
      </select>
    </div>
  );
}

function Input({ label, type = "text", defaultValue = "" }) {
  return (
    <div>
      <label className="block text-xs font-medium text-neutral-500 uppercase tracking-wide mb-1">{label}</label>
      <input type={type} defaultValue={defaultValue} className="w-full px-3 py-2 rounded-xl bg-white/60 border border-neutral-200/60 text-sm text-[#111] focus:outline-none focus:border-[#B9C7F5] transition-all" />
    </div>
  );
}
