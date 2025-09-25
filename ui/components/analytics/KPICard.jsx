import { TrendingUp, TrendingDown, HelpCircle, ArrowUpRight, ArrowDownRight } from 'lucide-react';

export default function KPICard({ label, value, delta, trend, target, progress }) {
  const up = trend === 'up';
  const color = up ? 'text-emerald-400' : 'text-rose-400';
  const Icon = up ? (delta?.includes('pp') ? ArrowUpRight : TrendingUp) : (delta?.includes('pp') ? ArrowDownRight : TrendingDown);
  return (
    <div className="rounded-xl p-4 border border-white/10 bg-slate-900/35">
      <div className="flex items-start justify-between">
        <div>
          <div className="text-slate-400 text-sm">{label}</div>
          <div className="text-2xl font-medium tracking-tight">{value}</div>
        </div>
        <div className="flex items-center gap-2">
          <span className={`${color} text-sm flex items-center gap-1`}>
            <Icon size={16} /> {delta}
          </span>
          <button className="text-slate-400 hover:text-white" title="What this means">
            <HelpCircle size={16} />
          </button>
        </div>
      </div>
     
    </div>
  );
}
