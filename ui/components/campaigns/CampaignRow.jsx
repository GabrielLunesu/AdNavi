import PlatformBadge from "./PlatformBadge";
import TrendSparkline from "./TrendSparkline";
import Link from "next/link";

export default function CampaignRow({ row }) {
  const k = row.kpis;
  return (
    <div className="grid grid-cols-[2fr_1fr_repeat(6,1fr)_1fr_1fr] items-center px-3 py-3 text-sm">
      <div className="flex items-center gap-3">
        <span className="text-slate-200">{row.name}</span>
      </div>
      <div className="flex items-center gap-2"><PlatformBadge platform={row.platform} /><span className="text-slate-400 text-xs">{row.platform}</span></div>
      <CellCurrency v={k.revenue} />
      <CellCurrency v={k.spend} />
      <CellPlain v={`${k.roas.toFixed(2)}×`} />
      <CellPlain v={k.conv.toLocaleString()} />
      <CellCurrency v={k.cpc} />
      <CellPlain v={`${k.ctr.toFixed(2)}%`} />
      <div>
        <span className={`text-xs px-2 py-1 rounded-full ${row.status==='Active'?'bg-emerald-500/10 text-emerald-300 border border-emerald-400/20':'bg-amber-500/10 text-amber-300 border border-amber-400/20'}`}>{row.status}</span>
      </div>
      <div><TrendSparkline data={row.trend} /></div>
      <div className="text-right">
        <Link href={`/campaigns/${row.id}`} className="px-2.5 py-1.5 text-xs rounded-full border border-slate-600/40 bg-slate-900/35 hover:border-cyan-400/60">View</Link>
      </div>
    </div>
  );
}

function CellCurrency({ v }) {
  const val = typeof v === 'number' ? v : parseFloat(v);
  return <div className="text-right tabular-nums">{fmtCurrency(val)}</div>;
}
function CellPlain({ v }) {
  return <div className="text-right tabular-nums">{v}</div>;
}
function fmtCurrency(n) {
  return n.toLocaleString(undefined, { style:'currency', currency:'USD', maximumFractionDigits: n>=100?0:2 });
}
