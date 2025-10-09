import { Plus, AlertTriangle, DollarSign, TrendingDown, X } from "lucide-react";

const rules = [
  {
    icon: AlertTriangle,
    title: 'ROAS < 1.5 → Notify',
    subtitle: 'Alert when campaign ROAS drops below 1.5x',
    type: 'In-app',
  },
  {
    icon: DollarSign,
    title: 'Spend > $10,000 → Alert',
    subtitle: 'Daily spend exceeds budget threshold',
    type: 'Email',
  },
  {
    icon: TrendingDown,
    title: 'CTR < 1.5% → Pause Ad Set',
    subtitle: 'Auto-pause underperforming ad sets',
    type: 'Auto',
  },
];

export default function ActiveRulesPanel() {
  return (
    <div className="mt-12">
      <div className="glass-card rounded-3xl border border-neutral-200/60 p-8 relative overflow-hidden">
        <div className="absolute top-0 left-0 right-0 h-0.5 bg-gradient-to-r from-transparent via-cyan-400 to-transparent opacity-30"></div>
        
        <div className="flex items-center justify-between mb-6">
          <h3 className="text-xl font-semibold text-neutral-900">Active Rules</h3>
          <button className="px-5 py-2.5 rounded-full bg-gradient-to-r from-cyan-400 to-cyan-600 text-white text-sm font-medium shadow-lg shadow-cyan-500/30 hover:shadow-cyan-500/40 transition-all flex items-center gap-2">
            <Plus className="w-4 h-4" strokeWidth={1.5} />
            Add Rule
          </button>
        </div>
        
        <div className="space-y-3">
          {rules.map((rule, idx) => {
            const Icon = rule.icon;
            return (
              <div key={idx} className="glass-card rounded-2xl px-6 py-4 border border-neutral-200/60 hover:border-cyan-400/40 transition-all flex items-center justify-between group">
                <div className="flex items-center gap-4">
                  <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-400 to-cyan-600 flex items-center justify-center">
                    <Icon className="w-5 h-5 text-white" strokeWidth={1.5} />
                  </div>
                  <div>
                    <p className="text-sm font-semibold text-neutral-900">{rule.title}</p>
                    <p className="text-xs text-neutral-500 mt-0.5">{rule.subtitle}</p>
                  </div>
                </div>
                <div className="flex items-center gap-2">
                  <span className="px-3 py-1.5 rounded-full text-xs font-medium pill-active">{rule.type}</span>
                  <button className="w-8 h-8 rounded-full bg-white/60 border border-neutral-200/60 hover:border-red-400/40 hover:bg-red-50 transition-all flex items-center justify-center opacity-0 group-hover:opacity-100">
                    <X className="w-4 h-4 text-red-600" strokeWidth={1.5} />
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

