import { TrendingUp, TrendingDown, CheckCircle } from "lucide-react";

const cards = [
  {
    label: 'Total Revenue',
    value: '€24.3K',
    trend: '+12.4%',
    trendLabel: 'vs last month',
    isPositive: true,
    progress: 82,
    progressColor: 'from-cyan-400 to-cyan-600',
    delay: '0ms',
  },
  {
    label: 'Total Spend',
    value: '€8.9K',
    trend: '−5.6%',
    trendLabel: 'vs last month',
    isPositive: false,
    progress: 45,
    progressColor: 'from-neutral-400 to-neutral-600',
    delay: '100ms',
  },
  {
    label: 'Gross Profit',
    value: '€15.4K',
    trend: '+8.2%',
    trendLabel: 'margin improved',
    isPositive: true,
    progress: 63,
    progressColor: 'from-green-400 to-green-600',
    badge: '58%',
    delay: '200ms',
  },
  {
    label: 'Net ROAS',
    value: '2.73x',
    trend: 'Above target',
    isPositive: true,
    targetInfo: 'Target: 2.5x',
    valueColor: 'text-cyan-600',
    delay: '300ms',
    showCheck: true,
  },
];

export default function FinancialSummaryCards() {
  return (
    <div className="grid grid-cols-4 gap-6 mb-8">
      {cards.map((card, idx) => {
        const TrendIcon = card.showCheck ? CheckCircle : (card.isPositive ? TrendingUp : TrendingDown);
        const trendColor = card.showCheck ? 'bg-green-50 text-green-600 border-green-200' : (card.isPositive ? 'bg-green-50 text-green-600 border-green-200' : 'bg-red-50 text-red-600 border-red-200');
        
        return (
          <div
            key={idx}
            className="glass-card rounded-3xl border border-black/5 shadow-xl p-8 relative overflow-hidden card-hover fade-up-in"
            style={{ animationDelay: card.delay }}
          >
            <div className="absolute -bottom-10 -right-10 w-32 h-32 bg-cyan-400 rounded-full blur-[80px] opacity-20 pulse-glow-aura" style={{ animationDelay: `${idx * 2}s` }}></div>
            <div className="relative z-10">
              {card.badge && (
                <div className="flex items-start justify-between mb-3">
                  <p className="text-sm font-medium text-neutral-500">{card.label}</p>
                  <span className="px-3 py-1 rounded-full bg-cyan-50 text-cyan-600 text-xs font-semibold border border-cyan-200">
                    {card.badge}
                  </span>
                </div>
              )}
              {!card.badge && (
                <p className="text-sm font-medium text-neutral-500 mb-3">{card.label}</p>
              )}
              <p className={`text-4xl font-bold tracking-tight mb-3 ${card.valueColor || 'text-black'}`}>{card.value}</p>
              <div className="flex items-center gap-2 mb-4">
                <span className={`inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-semibold border ${trendColor}`}>
                  <TrendIcon className="w-3 h-3" strokeWidth={2} />
                  {card.trend}
                </span>
                {card.trendLabel && (
                  <span className="text-xs text-neutral-400">{card.trendLabel}</span>
                )}
              </div>
              {card.progress !== undefined && (
                <div className="h-1.5 bg-neutral-100 rounded-full overflow-hidden progress-bar">
                  <div className={`h-full bg-gradient-to-r ${card.progressColor} rounded-full`} style={{ width: `${card.progress}%` }}></div>
                </div>
              )}
              {card.targetInfo && (
                <p className="text-xs text-neutral-400">{card.targetInfo}</p>
              )}
            </div>
          </div>
        );
      })}
    </div>
  );
}

