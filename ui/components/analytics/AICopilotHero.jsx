import { HelpCircle, Sparkles } from 'lucide-react';
import Card from "../../components/Card";

export default function AICopilotHero({ title, summary }) {
  return (
    <Card className="rounded-2xl">
      <div className="flex items-start gap-4">
        <div className="w-12 h-12 rounded-full bg-gradient-to-br from-cyan-400/60 via-violet-400/40 to-teal-400/40 flex items-center justify-center ring-1 ring-cyan-400/30 shadow-[0_0_40px_rgba(56,189,248,0.35)]">
          <Sparkles size={18} />
        </div>
        <div className="flex-1">
          <div className="flex items-center justify-between">
            <h2 className="text-2xl lg:text-3xl font-medium tracking-tight">{title}</h2>
            <button className="text-slate-400 hover:text-white" title="AI summary explains performance shifts in plain English.">
              <HelpCircle size={20} />
            </button>
          </div>
          <div className="mt-3 text-slate-300 space-y-2">
            {summary?.map((s, i) => <p key={i}>{s}</p>)}
          </div>
          <div className="mt-4 flex flex-wrap gap-2">
            <HeroPill>Explain simply</HeroPill>

          </div>
        </div>
      </div>
    </Card>
  );
}

function HeroPill({ children }) {
  return (
    <button className="px-3 py-1.5 rounded-full text-sm border border-slate-600/40 bg-slate-900/35 hover:border-cyan-400/60">
      {children}
    </button>
  );
}
