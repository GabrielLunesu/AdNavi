export default function CampaignTile({ title, stats, tip }) {
  return (
    <div className="rounded-xl border border-slate-700/40 bg-gradient-to-br from-teal-500/10 to-cyan-500/10 p-3">
      <div className="flex items-center justify-between">
        <div className="text-sm font-medium tracking-tight">{title}</div>
        <span className="text-xs text-slate-400">Now</span>
      </div>
      <div className="mt-2 grid grid-cols-3 gap-2">
        <Stat label="Spend" value={stats.spend} />
        <Stat label="ROAS" value={stats.roas} />
        <Stat label="CPC" value={stats.cpc} highlight />
      </div>
      {tip ? <div className="mt-2 text-xs text-slate-400">{tip}</div> : null}
    </div>
  );
}

function Stat({ label, value, highlight }) {
  return (
    <div className="rounded-lg bg-slate-900/40 border border-slate-700/40 p-2">
      <div className="text-[11px] text-slate-400">{label}</div>
      <div className={`text-sm ${highlight ? 'text-emerald-400' : 'text-slate-200'}`}>{value}</div>
    </div>
  );
}
