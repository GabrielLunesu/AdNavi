import { Rocket, Sliders } from 'lucide-react';

export default function OpportunityItem({ level, title }) {
  const style = level === 'High' ? 'border-emerald-500/20 hover:border-emerald-400/40' : level === 'Medium' ? 'border-amber-500/20 hover:border-amber-400/40' : 'border-white/10';
  const Icon = level === 'High' ? Rocket : Sliders;
  const badge = level;
  return (
    <div className={`rounded-xl p-4 border transition-all bg-slate-900/35 ${style}`}>
      <div className="flex items-start gap-3">
        <div className={`w-8 h-8 rounded-lg flex items-center justify-center ${level==='High'?'bg-emerald-500/15 border border-emerald-400/30':'bg-amber-500/15 border border-amber-400/30'}`}>
          <Icon size={16} className={`${level==='High'?'text-emerald-300':'text-amber-300'}`} />
        </div>
        <div className="flex-1">
          <div className="flex items-center justify-between">
            <h4 className="font-medium">{title}</h4>
            <span className={`text-xs px-2 py-1 rounded-full ${level==='High'?'bg-emerald-500/10 text-emerald-300 border border-emerald-400/20':'bg-amber-500/10 text-amber-300 border border-amber-400/20'}`}>{badge}</span>
          </div>
          <div className="mt-2 flex items-center gap-3">
            <button className="text-sm text-slate-300 hover:text-white">Explain</button>
            <button className="text-sm text-cyan-400 hover:text-cyan-300">Simulate</button>
            <button className="text-sm text-teal-400 hover:text-teal-300">Add to Plan</button>
          </div>
        </div>
      </div>
    </div>
  );
}
