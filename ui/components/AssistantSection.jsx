// AssistantSection renders the greeting, subtitle, and a non-functional prompt
// This is intentionally presentational: no state or external calls.
import { Mic, Send, Sparkles } from 'lucide-react';

export default function AssistantSection() {
  return (
    <section className="relative pt-10 md:pt-16 pb-6 md:pb-10">
      <div className="max-w-3xl mx-auto text-center">
        {/* Decorative assistant orb */}
        <div className="mx-auto mb-4 w-12 h-12 md:w-14 md:h-14 rounded-full bg-gradient-to-br from-violet-500/60 via-fuchsia-500/40 to-cyan-400/40 grid place-items-center text-slate-900 shadow-[0_0_40px_rgba(56,189,248,0.25)]">
          <Sparkles size={18} />
        </div>
        {/* Greeting */}
        <h1 className="text-4xl md:text-5xl font-semibold tracking-tight mb-3">
          Hi there. What can I help you achieve today?
        </h1>
        {/* Subtitle guidance */}
        <p className="text-slate-400 text-base md:text-lg mb-6">
          Ask about your results. Simulate a change. Or let me recommend what to do next.
        </p>

        {/* Prompt input row */}
        <div className="flex items-center gap-3 justify-center">
          <div className="flex items-center gap-2 rounded-full border border-slate-800/60 bg-slate-900/40 px-4 py-3 w-full max-w-2xl shadow-[0_10px_30px_rgba(0,0,0,0.35)]">
            <Mic size={16} className="text-slate-500" aria-hidden />
            <input
              className="bg-transparent outline-none text-sm md:text-base flex-1 placeholder:text-slate-500 text-slate-200"
              placeholder="Why is my Meta campaign underperforming?"
              aria-label="Assistant prompt"
            />
            <button className="rounded-full p-2 md:p-2.5 bg-cyan-500 text-slate-950" aria-label="Run">
              <Send size={16} />
            </button>
          </div>
        </div>

        {/* Quick actions under input */}
        <div className="mt-5 flex items-center justify-center gap-2 flex-wrap">
          <button className="rounded-full border border-slate-800/60 px-3 py-1.5 text-xs md:text-sm text-slate-300 hover:text-white hover:bg-slate-800/40">
            Show me what's working
          </button>
          <button className="rounded-full border border-slate-800/60 px-3 py-1.5 text-xs md:text-sm text-slate-300 hover:text-white hover:bg-slate-800/40">
            Suggest my next campaign
          </button>
          <button className="rounded-full border border-slate-800/60 px-3 py-1.5 text-xs md:text-sm text-slate-300 hover:text-white hover:bg-slate-800/40">
            Improve my budget efficiency
          </button>
        </div>
      </div>

      {/* Visual separator to set it apart */}
      <div className="mt-10 md:mt-12 mx-auto max-w-6xl h-px bg-gradient-to-r from-transparent via-white/10 to-transparent" />
    </section>
  );
}
