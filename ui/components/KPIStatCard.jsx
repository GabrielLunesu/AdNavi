// KPI card: shows label, value, delta percent, and a tiny sparkline
import Sparkline from "./Sparkline";

function Delta({ value }) {
  const sign = value > 0 ? '+' : '';
  const color = value >= 0 ? 'text-emerald-400' : 'text-rose-400';
  return (
    <div className={`flex items-center gap-1 text-xs ${color}`}>
      <span aria-hidden>{value >= 0 ? '▲' : '▼'}</span>
      <span>{sign}{Math.abs(value).toFixed(1)}%</span>
    </div>
  );
}

export default function KPIStatCard({ label, value, deltaPct = 0, sparklineData = [], color }) {
  return (
    <div className="rounded-xl p-4 border border-slate-800/60 bg-slate-900/40 relative">
      <div className="flex items-center justify-between mb-2">
        <span className="text-slate-400 text-xs">{label}</span>
        <Delta value={deltaPct} />
      </div>
      <div className="flex items-end justify-between">
        <div>
          <div className="text-2xl md:text-3xl font-medium tracking-tight">{value}</div>
          <div className="text-[11px] text-slate-500">vs prev period</div>
        </div>
        <Sparkline data={sparklineData} color={color} />
      </div>
    </div>
  );
}
