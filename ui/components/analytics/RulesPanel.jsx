import RuleRow from "./RuleRow";
import { rules } from "../../data/analytics/rules";

export default function RulesPanel() {
  return (
    <section className="rounded-2xl p-4 border border-slate-700/40 bg-slate-900/35">
      {/* Scope selector */}
      <div className="mb-6 text-xl text-white/90 flex items-center gap-2">
        <span>Rules for</span>
        <ScopePill>campaign</ScopePill>
        <ScopePill>platform</ScopePill>
        <ScopePill>workspace</ScopePill>
      </div>

      <div className="flex items-center justify-between mb-3">
        <div className="flex items-center gap-2">
          <button className="px-3 py-1.5 text-sm rounded-full bg-slate-800/60">Rules</button>
          <button className="px-3 py-1.5 text-sm rounded-full hover:bg-slate-800/40">History</button>
        </div>
        <button className="text-slate-400 hover:text-white">?</button>
      </div>
      <div className="space-y-3">
        {rules.map((r, idx) => (
          <RuleRow key={idx} parts={r.parts} />
        ))}
        <div className="text-xs text-slate-400">Rules inherit workspace KPI thresholds from Finance unless overridden.</div>
        <div className="flex items-center gap-2 pt-1">
          <button className="px-3 py-1.5 text-sm rounded-full border border-slate-600/40 bg-slate-900/35 hover:border-cyan-400/60">Add Rule</button>
          <button className="px-3 py-1.5 text-sm rounded-full bg-gradient-to-r from-teal-500/80 to-cyan-500/80 hover:from-teal-500 hover:to-cyan-500 shadow-[0_0_20px_rgba(34,211,238,0.25)]">Save Rules</button>
          <button className="px-3 py-1.5 text-sm rounded-full border border-slate-600/40 bg-slate-900/35 hover:border-violet-400/60">Test Alerts</button>
        </div>
      </div>
    </section>
  );
}

function ScopePill({ children }) {
  return (
    <button className="px-2.5 py-1 rounded-full border border-slate-600/40 bg-slate-900/35 text-xs hover:border-cyan-400/60">
      {children}
    </button>
  );
}
