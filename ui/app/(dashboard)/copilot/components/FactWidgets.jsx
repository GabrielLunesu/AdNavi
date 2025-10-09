const facts = [
  {
    label: 'Lowest CPC Right Now',
    value: '$0.64',
    subtitle: 'Meta LAL 2%',
  },
  {
    label: 'Top Campaign by Revenue',
    value: '$4,280',
    subtitle: 'Summer Sale 2024',
  },
  {
    label: 'Biggest Variance in Spend',
    value: '-12.4%',
    subtitle: 'TikTok Awareness',
  },
];

export default function FactWidgets() {
  return (
    <div className="grid grid-cols-3 gap-4 mb-12">
      {facts.map((fact, idx) => (
        <div key={idx} className="glass-card rounded-2xl p-5 border border-cyan-200/40 relative overflow-hidden">
          <div className="absolute top-0 left-0 right-0 h-0.5 bg-gradient-to-r from-transparent via-cyan-400 to-transparent"></div>
          <p className="text-xs font-medium text-neutral-500 mb-1 uppercase tracking-wide">{fact.label}</p>
          <p className="text-2xl font-semibold text-neutral-900">{fact.value}</p>
          <p className="text-xs text-neutral-600 mt-1">{fact.subtitle}</p>
        </div>
      ))}
    </div>
  );
}

