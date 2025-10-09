function MiniSparkline({ data, isNegative }) {
  if (!data || data.length === 0) return null;
  
  const color = isNegative ? '#EF4444' : '#06B6D4';
  const opacity = isNegative ? 0.5 : 1;
  const points = data.map((val, i) => {
    const x = (i / (data.length - 1)) * 60;
    const y = 24 - ((val - Math.min(...data)) / (Math.max(...data) - Math.min(...data))) * 16;
    return `${x},${y}`;
  }).join(' ');

  return (
    <svg className="sparkline-pulse" width="60" height="24" viewBox="0 0 60 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <polyline
        points={points}
        stroke={color}
        strokeWidth="2"
        fill="none"
        opacity={opacity}
      />
      <defs>
        <linearGradient id="gradient-revenue" x1="0" y1="0" x2="60" y2="0">
          <stop offset="0%" stopColor="#06B6D4" stopOpacity="0.3"/>
          <stop offset="100%" stopColor="#06B6D4" stopOpacity="1"/>
        </linearGradient>
      </defs>
    </svg>
  );
}

function KPICard({ label, value, change, changePercent, sparklineData }) {
  const isNegative = changePercent < 0;
  const changeColor = isNegative ? 'bg-red-50 text-red-600' : 'bg-green-50 text-green-600';
  
  return (
    <div className="glass-card rounded-3xl p-6 border border-neutral-200/60 shadow-lg card-hover card-animate relative overflow-hidden">
      <div className="absolute top-0 left-0 right-0 h-0.5 bg-gradient-to-r from-transparent via-cyan-400 to-transparent opacity-0 hover:opacity-100 transition-opacity"></div>
      <p className="text-xs font-medium text-neutral-500 mb-2 uppercase tracking-wide">{label}</p>
      <p className="text-3xl font-semibold text-neutral-900 mb-3">{value}</p>
      <div className="flex items-center justify-between">
        <span className={`px-2.5 py-1 rounded-full text-xs font-medium ${changeColor}`}>
          {change}
        </span>
        <MiniSparkline data={sparklineData} isNegative={isNegative} />
      </div>
      <div className="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-cyan-400 via-cyan-500 to-cyan-400 opacity-50 rounded-b-3xl"></div>
    </div>
  );
}

export default function KPISummary({ kpis }) {
  return (
    <div className="mx-8 mb-8">
      <div className="grid grid-cols-4 gap-6">
        {kpis.map((kpi, idx) => (
          <KPICard key={idx} {...kpi} />
        ))}
      </div>
    </div>
  );
}

