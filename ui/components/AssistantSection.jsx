// AssistantSection renders the greeting, subtitle, and a non-functional prompt
// This is intentionally presentational: no state or external calls.
import { Mic, Send, Sparkles } from 'lucide-react';

export default function AssistantSection() {
  return (
    <section className="relative mb-8">
      {/* Greeting */}
      <h1 className="text-3xl md:text-4xl font-semibold tracking-tight mb-2">
        Hi there. What can I help you achieve today?
      </h1>
      {/* Subtitle guidance */}
      <p className="text-slate-400 text-sm md:text-base mb-6">
        Ask about your results. Simulate a change. Or let me recommend what to do next.
      </p>

      {/* Prompt input row */}
      <div className="flex items-center gap-3">
        {/* Decorative assistant orb */}
        <div className="w-10 h-10 rounded-full bg-gradient-to-br from-violet-500/60 via-fuchsia-500/40 to-cyan-400/40 grid place-items-center text-slate-900">
          <Sparkles size={16} />
        </div>
        <div className="flex-1 flex items-center gap-2 rounded-full border border-slate-800/60 bg-slate-900/40 px-4 py-2">
          <Mic size={16} className="text-slate-500" aria-hidden />
          <input
            className="bg-transparent outline-none text-sm flex-1 placeholder:text-slate-500"
            placeholder="Why is my Meta campaign underperforming?"
            aria-label="Assistant prompt"
          />
          <button className="rounded-full p-2 bg-cyan-500 text-slate-950" aria-label="Run">
            <Send size={14} />
          </button>
        </div>
      </div>

      {/* Quick actions under input */}
      <div className="mt-4 flex items-center gap-2 flex-wrap">
        <button className="rounded-full border border-slate-800/60 px-3 py-1.5 text-xs text-slate-300 hover:text-white hover:bg-slate-800/40">
          Show me what's working
        </button>
        <button className="rounded-full border border-slate-800/60 px-3 py-1.5 text-xs text-slate-300 hover:text-white hover:bg-slate-800/40">
          Suggest my next campaign
        </button>
        <button className="rounded-full border border-slate-800/60 px-3 py-1.5 text-xs text-slate-300 hover:text-white hover:bg-slate-800/40">
          Improve my budget efficiency
        </button>
      </div>
    </section>
  );
}
