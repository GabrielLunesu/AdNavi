import { TrendingUp, CheckCircle, AlertCircle } from "lucide-react";

const alerts = [
  {
    type: 'warning',
    icon: TrendingUp,
    title: 'Meta Ads spend exceeded budget by 12%',
    subtitle: 'Testing new creatives drove higher costs',
    color: 'red',
  },
  {
    type: 'success',
    icon: CheckCircle,
    title: 'Google Ads maintained ROAS above target',
    subtitle: 'Consistent performance across search campaigns',
    color: 'green',
  },
  {
    type: 'info',
    icon: AlertCircle,
    title: 'SaaS subscriptions trending 5% higher than last month',
    subtitle: 'New analytics tool added to stack',
    color: 'amber',
  },
];

export default function AlertsPanel() {
  return (
    <div className="glass-card rounded-3xl border border-black/5 shadow-xl p-8 mb-8 fade-up-in" style={{ animationDelay: '700ms' }}>
      <div className="flex items-center justify-between mb-6">
        <h3 className="text-lg font-semibold text-black">Alerts & Variances</h3>
        <button className="text-sm font-medium text-cyan-600 hover:text-cyan-700 transition-all">View All</button>
      </div>
      
      <div className="space-y-3">
        {alerts.map((alert, idx) => {
          const Icon = alert.icon;
          const bgColor = alert.color === 'red' ? 'bg-red-50' : alert.color === 'green' ? 'bg-green-50' : 'bg-amber-50';
          const borderColor = alert.color === 'red' ? 'border-red-200' : alert.color === 'green' ? 'border-green-200' : 'border-amber-200';
          const textColor = alert.color === 'red' ? 'text-red-600' : alert.color === 'green' ? 'text-green-600' : 'text-amber-600';
          const glowClass = alert.color === 'red' ? 'alert-glow-red' : alert.color === 'green' ? 'alert-glow-green' : 'alert-glow-amber';
          const hoverBorderColor = alert.color === 'red' ? 'hover:border-red-400/40' : alert.color === 'green' ? 'hover:border-green-400/40' : 'hover:border-amber-400/40';
          
          return (
            <div key={idx} className={`glass-card rounded-2xl border border-black/5 px-6 py-4 flex items-center justify-between ${glowClass} ${hoverBorderColor} transition-all group`}>
              <div className="flex items-center gap-4">
                <div className={`w-10 h-10 rounded-xl ${bgColor} flex items-center justify-center border ${borderColor}`}>
                  <Icon className={`w-5 h-5 ${textColor}`} strokeWidth={1.5} />
                </div>
                <div>
                  <p className="text-sm font-semibold text-black">{alert.title}</p>
                  <p className="text-xs text-neutral-500 mt-0.5">{alert.subtitle}</p>
                </div>
              </div>
              <button className="text-sm font-medium text-cyan-600 hover:underline opacity-0 group-hover:opacity-100 transition-all">Details</button>
            </div>
          );
        })}
      </div>
    </div>
  );
}

