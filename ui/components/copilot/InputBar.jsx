import { Plus, Mic, ArrowUpRight, Sparkles } from 'lucide-react';

export default function InputBar({ placeholder = 'Ask me about your revenue today…' }) {
  return (
    <div className="sticky bottom-0 w-full px-3 sm:px-5 pb-4 pt-2 bg-gradient-to-t from-slate-900/60 to-transparent backdrop-blur">
      <div className="flex items-center gap-2">
        <div className="flex-1 rounded-full border border-slate-700/40 bg-slate-900/40 backdrop-blur px-3 py-2.5 flex items-center gap-2 ring-1 ring-white/5">
          <Sparkles size={16} className="text-cyan-300" />
          <input type="text" className="w-full bg-transparent outline-none text-sm placeholder-slate-500 text-slate-200" placeholder={placeholder} />
          <div className="flex items-center gap-1">
            <button className="p-1.5 rounded-full hover:bg-slate-800/60 border border-transparent hover:border-slate-700/50" aria-label="Attach">
              <Plus size={16} className="text-slate-300" />
            </button>
            <button className="p-1.5 rounded-full hover:bg-slate-800/60 border border-transparent hover:border-slate-700/50" aria-label="Voice">
              <Mic size={16} className="text-slate-300" />
            </button>
            <button className="p-1.5 rounded-full bg-cyan-500/20 hover:bg-cyan-500/30 ring-1 ring-cyan-400/40" aria-label="Send">
              <ArrowUpRight size={16} className="text-cyan-300" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
