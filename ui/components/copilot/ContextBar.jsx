export default function ContextBar({ workspace, timeframe, platforms, synced }) {
  return (
    <div className="rounded-xl px-4 py-3 border border-slate-700/40 bg-slate-900/35 flex items-center justify-between">
      <div className="flex items-center gap-4">
        <div className="flex items-center gap-2">
          <span className="text-slate-400 text-xs">Workspace</span>
          <span className="text-sm text-slate-200">{workspace}</span>
        </div>
        <div className="hidden sm:block w-px h-4 bg-slate-700/40" />
        <div className="flex items-center gap-2">
          <span className="text-slate-400 text-xs">Timeframe</span>
          <span className="text-sm text-slate-200">{timeframe}</span>
        </div>
        <div className="hidden sm:block w-px h-4 bg-slate-700/40" />
        <div className="flex items-center gap-2">
          <span className="text-slate-400 text-xs">Platforms</span>
          <span className="text-sm text-slate-200">{platforms}</span>
        </div>
      </div>
      <div className="flex items-center gap-2">
        {synced ? <div className="w-2.5 h-2.5 rounded-full bg-emerald-400 shadow-[0_0_12px_2px_rgba(16,185,129,0.6)]" /> : null}
        <span className="text-xs text-slate-400">Context synced</span>
      </div>
    </div>
  );
}
