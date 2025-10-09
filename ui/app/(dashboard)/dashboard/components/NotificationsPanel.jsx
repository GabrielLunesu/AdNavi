import { TrendingDown, AlertCircle, Zap, ArrowRight } from "lucide-react";

const notifications = [
  {
    id: 1,
    icon: TrendingDown,
    text: "ROAS dropped below 1.5 on Campaign X (1.3x)",
    time: "12m ago",
  },
  {
    id: 2,
    icon: AlertCircle,
    text: "Daily budget 80% consumed on Google Ads",
    time: "1h ago",
  },
  {
    id: 3,
    icon: Zap,
    text: "New high-performing keyword detected in Campaign Y",
    time: "3h ago",
  },
];

export default function NotificationsPanel() {
  return (
    <div className="mb-12">
      <div className="glass-card rounded-3xl p-8 border border-neutral-200/60 shadow-lg">
        <div className="flex items-center justify-between mb-6">
          <h3 className="text-xl font-semibold text-neutral-900">Notifications</h3>
          <button className="text-sm font-medium text-cyan-600 hover:text-cyan-700 flex items-center gap-1 transition-colors">
            View all rules
            <ArrowRight className="w-4 h-4" strokeWidth={1.5} />
          </button>
        </div>
        <div className="space-y-4">
          {notifications.map((notification) => {
            const Icon = notification.icon;
            return (
              <div
                key={notification.id}
                className="flex items-start gap-4 p-4 rounded-2xl hover:bg-white/60 transition-all group cursor-pointer"
              >
                <div className="w-8 h-8 rounded-full bg-cyan-50 flex items-center justify-center flex-shrink-0">
                  <Icon className="w-4 h-4 text-cyan-600" strokeWidth={1.5} />
                </div>
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-medium text-neutral-900 group-hover:text-cyan-600 transition-colors">
                    {notification.text}
                  </p>
                  <p className="text-xs text-neutral-500 mt-1">{notification.time}</p>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

