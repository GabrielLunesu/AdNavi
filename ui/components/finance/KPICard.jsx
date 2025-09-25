export default function KPICard({ label, value, deltaPct = 0, trend = 'up', spark = [], color = '#22d3ee' }) {
  const up = trend === 'up' || deltaPct >= 0;
  const deltaColor = up ? 'text-emerald-400' : 'text-rose-400';
  return (
    <div className="rounded-xl p-4 border border-white/10 bg-slate-900/35">
      <div className="flex items-start justify-between">
        <div>
          <div className="text-slate-400 text-sm">{label}</div>
          <div className="text-2xl font-medium tracking-tight">{value}</div>
        </div>
        <div className={`text-sm ${deltaColor}`}>{formatDelta(deltaPct)}</div>
      </div>
      <div className="mt-3 h-10">
        <Spark data={spark} color={color} />
      </div>
    </div>
  );
}

function formatDelta(pct) {
  const sign = pct >= 0 ? '+' : '';
  return `${sign}${pct.toFixed(1)}%`;
}

function Spark({ data = [], color = '#22d3ee' }) {
  if (!Array.isArray(data) || data.length === 0) return null;
  const max = Math.max(...data);
  const min = Math.min(...data);
  const norm = data.map((v, i) => {
    const x = (i / (data.length - 1)) * 100;
    const y = 100 - ((v - min) / (max - min || 1)) * 100;
    return `${x},${y}`;
  }).join(' ');
  return (
    <svg viewBox="0 0 100 100" className="w-full h-full">
      <polyline fill="none" stroke={color} strokeWidth="2" points={norm} />
    </svg>
  );
}
