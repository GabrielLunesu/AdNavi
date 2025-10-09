const metrics = [
  { label: 'CTR', value: '2.84%', change: '+0.3%', isPositive: true },
  { label: 'CPC', value: '$1.24', change: '+$0.08', isPositive: false },
  { label: 'CPA', value: '$18.98', change: '-$2.14', isPositive: true },
  { label: 'Conversion Rate', value: '4.12%', change: '+0.5%', isPositive: true },
];

export default function MetricBreakdown() {
  return (
    <div className="grid grid-cols-2 gap-4">
      {metrics.map((metric, idx) => {
        const changeColor = metric.isPositive ? 'bg-green-50 text-green-600' : 'bg-red-50 text-red-600';
        return (
          <div key={idx} className="glass-card rounded-3xl p-6 border border-neutral-200/60 shadow-lg card-hover">
            <p className="text-xs font-medium text-neutral-500 mb-2 uppercase tracking-wide">{metric.label}</p>
            <p className="text-2xl font-semibold text-neutral-900">{metric.value}</p>
            <span className={`inline-block mt-2 px-2 py-0.5 rounded-full text-xs font-medium ${changeColor}`}>
              {metric.change}
            </span>
          </div>
        );
      })}
    </div>
  );
}

