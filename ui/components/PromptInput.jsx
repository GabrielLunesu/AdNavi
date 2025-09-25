// Assistant prompt input (non-functional)
export default function PromptInput() {
  return (
    <div className="flex items-center gap-2 rounded-full border border-slate-800/60 bg-slate-900/40 px-3 py-2 w-full">
      <span aria-hidden>🔎</span>
      <input
        className="bg-transparent outline-none text-sm flex-1 placeholder:text-slate-500"
        placeholder="What can I help you achieve today?"
        aria-label="Assistant prompt"
      />
      <button className="rounded-full px-3 py-1 bg-cyan-500 text-slate-950 text-xs font-medium">
        Run
      </button>
    </div>
  );
}
