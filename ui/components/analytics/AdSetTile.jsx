import { HelpCircle, Images } from 'lucide-react';

export default function AdSetTile({ item }) {
  return (
    <div className="min-w-[340px] rounded-xl p-4 border border-slate-700/40 bg-slate-900/35">
      <div className="flex items-start justify-between">
        <div>
          <div className="text-sm font-medium">{item.name}</div>
          <div className="text-xs text-emerald-400 flex items-center gap-1"><span className="w-2 h-2 rounded-full bg-emerald-400" /> Active</div>
        </div>
      </div>
      <div className="grid grid-cols-3 gap-3 mt-3 text-sm">
        <KV label="Revenue" value={item.revenue} />
        <KV label="Spend" value={item.spend} />
        <KV label="ROAS" value={item.roas} />
        <KV label="Conv" value={item.conversions} />
        <KV label="CPC" value={item.cpc} />
        <KV label="CTR" value={item.ctr} />
      </div>
      <div className="mt-3 h-10 rounded-md bg-gradient-to-tr from-emerald-400/10 to-cyan-400/10 border border-white/5" />
      <div className="mt-3">
        <button className="text-xs px-2.5 py-1 rounded-full border border-slate-600/40 bg-slate-900/35 hover:border-cyan-400/60">Ask AI</button>
      </div>
    </div>
  );
}

function KV({ label, value }) {
  return (
    <div>
      <div className="text-slate-400 text-xs">{label}</div>
      <div>{value}</div>
    </div>
  );
}
