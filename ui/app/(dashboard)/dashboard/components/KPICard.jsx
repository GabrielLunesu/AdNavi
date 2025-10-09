// KPI card with glass morphism and cyan accents

function Delta({ value }) {
  const sign = value > 0 ? '+' : '';
  const isPositive = value >= 0;
  const color = isPositive ? 'text-green-600' : 'text-red-600';
  const bgColor = isPositive ? 'bg-green-50' : 'bg-red-50';
  
  return (
    <span className={`px-2 py-1 rounded-full ${bgColor} ${color} text-xs font-medium`}>
      {sign}{Math.abs(value).toFixed(1)}%
    </span>
  );
}

function MiniSparkline({ data, isNegative }) {
  if (!data || data.length === 0) return null;
  
  const color = isNegative ? '#EF4444' : '#06B6D4';
  const opacity = isNegative ? 0.4 : 1;
  const points = data.map((val, i) => {
    const x = (i / (data.length - 1)) * 80;
    const y = 40 - ((val - Math.min(...data)) / (Math.max(...data) - Math.min(...data))) * 25;
    return `${x},${y}`;
  }).join(' ');

  return (
    <svg className="w-20 h-10" viewBox="0 0 80 40" fill="none" xmlns="http://www.w3.org/2000/svg">
      <polyline
        points={points}
        stroke={color}
        strokeWidth="2"
        fill="none"
        opacity={opacity}
      />
    </svg>
  );
}

export default function KPICard({ label, value, deltaPct = 0, sparklineData = [] }) {
  const isNegative = deltaPct < 0;
  
  return (
    <div className="glass-card rounded-3xl p-6 border border-neutral-200/60 shadow-lg card-hover relative overflow-hidden">
      <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-cyan-400 to-cyan-600"></div>
      <p className="text-xs font-medium text-neutral-500 mb-2 uppercase tracking-wide">{label}</p>
      <p className="text-3xl font-semibold text-neutral-900 mb-3">{value}</p>
      <div className="flex items-center justify-between">
        <Delta value={deltaPct} />
        <MiniSparkline data={sparklineData} isNegative={isNegative} />
      </div>
    </div>
  );
}

