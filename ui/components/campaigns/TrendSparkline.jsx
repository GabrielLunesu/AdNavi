export default function TrendSparkline({ data = [], color = '#60a5fa' }) {
  if (!data || data.length === 0) return null;
  const max = Math.max(...data);
  const min = Math.min(...data);
  const pts = data.map((v, i) => {
    const x = (i / (data.length - 1)) * 100;
    const y = 100 - ((v - min) / (max - min || 1)) * 100;
    return `${x},${y}`;
  }).join(' ');
  return (
    <svg viewBox="0 0 100 100" className="w-24 h-6">
      <polyline fill="none" stroke={color} strokeWidth="2" points={pts} />
    </svg>
  );
}
