// Workspace summary block shows current workspace and quick meta
export default function WorkspaceSummary() {
  return (
    <div className="rounded-xl p-4 border border-slate-800/60 bg-slate-900/40">
      <h4 className="text-sm font-medium text-slate-300 mb-3">Current Workspace</h4>
      <div className="space-y-2 text-xs text-slate-400">
        <div className="flex items-center gap-2">
          <span className="w-2 h-2 rounded-full bg-emerald-400" aria-hidden />
          <span>Defang Labs</span>
        </div>
        <div>Active platforms: Meta, Google</div>
        <div className="flex items-center justify-between pt-2">
          <span>Last sync: 13 min ago</span>
          <button className="hover:text-white" aria-label="Refresh">
            ↻
          </button>
        </div>
      </div>
    </div>
  );
}
