/**
 * Financial Summary Cards
 * 
 * WHAT: Display P&L summary KPIs (read-only cards)
 * WHY: Top-level metrics at a glance
 * REFERENCES: lib/pnlAdapter.js:adaptPnLStatement
 */

import { TrendingUp, TrendingDown, CheckCircle } from "lucide-react";

export default function FinancialSummaryCards({ summary, showComparison }) {
  if (!summary) return null;

  const cards = [
    {
      data: summary.totalRevenue,
      progressColor: 'from-cyan-400 to-cyan-600',
      delay: '0ms',
    },
    {
      data: summary.totalSpend,
      progressColor: 'from-neutral-400 to-neutral-600',
      delay: '100ms',
    },
    {
      data: summary.grossProfit,
      progressColor: 'from-green-400 to-green-600',
      delay: '200ms',
    },
    {
      data: summary.netRoas,
      valueColor: 'text-cyan-600',
      delay: '300ms',
      showCheck: true,
    },
  ];
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 lg:gap-6 mb-8">
      {cards.map((card, idx) => {
        const hasDelta = showComparison && card.data.delta;
        const isPositive = hasDelta && !card.data.delta.startsWith('-');
        const TrendIcon = card.showCheck ? CheckCircle : (isPositive ? TrendingUp : TrendingDown);
        const trendColor = card.showCheck 
          ? 'bg-green-50 text-green-600 border-green-200' 
          : (isPositive ? 'bg-green-50 text-green-600 border-green-200' : 'bg-red-50 text-red-600 border-red-200');
        
        return (
          <div
            key={idx}
            className="glass-card rounded-3xl border border-black/5 shadow-xl p-6 lg:p-8 relative overflow-hidden card-hover fade-up-in min-w-0"
            style={{ animationDelay: card.delay }}
          >
            <div className="absolute -bottom-10 -right-10 w-32 h-32 bg-cyan-400 rounded-full blur-[80px] opacity-20 pulse-glow-aura" style={{ animationDelay: `${idx * 2}s` }}></div>
            <div className="relative z-10">
              <p className="text-sm font-medium text-neutral-500 mb-3">{card.data.label}</p>
              <p className={`text-2xl sm:text-3xl lg:text-4xl font-bold tracking-tight mb-3 truncate ${card.valueColor || 'text-black'}`} title={card.data.value}>
                {card.data.value}
              </p>
              {hasDelta && (
                <div className="flex items-center gap-2 mb-4">
                  <span className={`inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-semibold border ${trendColor}`}>
                    <TrendIcon className="w-3 h-3" strokeWidth={2} />
                    {card.data.delta}
                  </span>
                  <span className="text-xs text-neutral-400">vs prev period</span>
                </div>
              )}
            </div>
          </div>
        );
      })}
    </div>
  );
}

