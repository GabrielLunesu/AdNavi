import PlatformBadge from "./PlatformBadge";
import TrendSparkline from "./TrendSparkline";
import Link from "next/link";

export default function CampaignRow({ row }) {
  const display = row.display || {};
  return (
    <div className="grid grid-cols-[2fr_1fr_repeat(6,1fr)_1fr_1fr] items-center px-3 py-3 text-sm">
      <div className="flex flex-col">
        <span className="text-slate-200">{row.name}</span>
        <span className="text-xs text-slate-400">{display.subtitle}</span>
      </div>
      <div className="flex items-center gap-2"><PlatformBadge platform={row.platform} /><span className="text-slate-400 text-xs">{row.platform || "—"}</span></div>
      <CellText value={display.revenue} align="right" />
      <CellText value={display.spend} align="right" />
      <CellText value={display.roas} align="right" />
      <CellText value={display.conversions} align="right" />
      <CellText value={display.cpc} align="right" />
      <CellText value={display.ctr} align="right" />
      <div>
        <span className={`text-xs px-2 py-1 rounded-full ${row.status==='active'?'bg-emerald-500/10 text-emerald-300 border border-emerald-400/20':'bg-amber-500/10 text-amber-300 border border-amber-400/20'}`}>{row.status}</span>
      </div>
      <div><TrendSparkline data={row.trend.map(point => point.value ?? 0)} /></div>
      <div className="text-right">
        <Link href={`/campaigns/${row.id}`} className="px-2.5 py-1.5 text-xs rounded-full border border-slate-600/40 bg-slate-900/35 hover:border-cyan-400/60">View</Link>
      </div>
    </div>
  );
}

function CellText({ value, align = 'left' }) {
  return <div className={`tabular-nums ${align === 'right' ? 'text-right' : ''}`}>{value ?? '—'}</div>;
}
