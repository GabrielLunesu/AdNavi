// IconBadge renders a colored square with a status icon
import { TriangleAlert, TrendingUp, Lightbulb, Activity, Info } from 'lucide-react';

export default function IconBadge({ level = 'info' }) {
  const map = {
    alert: { bg: 'bg-rose-500/15', color: 'text-rose-400', Icon: TriangleAlert },
    info: { bg: 'bg-emerald-500/15', color: 'text-emerald-400', Icon: TrendingUp },
    warn: { bg: 'bg-cyan-500/15', color: 'text-cyan-400', Icon: Lightbulb },
    note: { bg: 'bg-violet-500/15', color: 'text-violet-400', Icon: Activity },
    default: { bg: 'bg-slate-700/20', color: 'text-slate-300', Icon: Info },
  };
  const { bg, color, Icon } = map[level] || map.default;
  return (
    <div className={`w-7 h-7 rounded-md ${bg} flex items-center justify-center`}>
      <Icon size={16} className={color} aria-hidden />
    </div>
  );
}
