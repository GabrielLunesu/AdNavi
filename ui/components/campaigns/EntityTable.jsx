import Card from "../Card";
import EntityRow from "./EntityRow";

export default function EntityTable({ title, rows = [], loading = false, error = null, onRowClick }) {
  return (
    <Card className="rounded-2xl backdrop-blur-xl bg-gradient-to-br from-white/[0.07] to-white/[0.02] border border-white/10 shadow-[0_8px_32px_rgba(0,0,0,0.12)] overflow-hidden">
      {/* Header with title and loading indicator */}
      <div className="px-6 py-4 flex items-center justify-between border-b border-white/10 bg-white/[0.03]">
        <span className="text-sm font-semibold text-slate-900 tracking-wide">{title}</span>
        {loading ? (
          <span className="text-xs text-emerald-600 font-medium animate-pulse flex items-center gap-2">
            <span className="inline-block w-1.5 h-1.5 bg-emerald-500 rounded-full animate-ping"></span>
            Loading…
          </span>
        ) : null}
      </div>
      
      {/* Column Headers */}
      <div className="flex items-stretch px-6 py-4 text-xs font-bold text-slate-700 uppercase tracking-wider bg-white/[0.02] border-b border-slate-900/20 backdrop-blur-sm">
        <div className="w-[300px] px-4 border-r border-slate-900/20 flex items-center">Name</div>
        <div className="w-[120px] px-4 border-r border-slate-900/20 flex items-center">Revenue</div>
        <div className="w-[120px] px-4 border-r border-slate-900/20 flex items-center">Spend</div>
        <div className="w-[100px] px-4 border-r border-slate-900/20 flex items-center">ROAS</div>
        <div className="w-[130px] px-4 border-r border-slate-900/20 flex items-center">Conversions</div>
        <div className="w-[100px] px-4 border-r border-slate-900/20 flex items-center">CPC</div>
        <div className="w-[100px] px-4 border-r border-slate-900/20 flex items-center">CTR</div>
        <div className="w-[120px] px-4 border-r border-slate-900/20 flex items-center">Status</div>
        <div className="w-[120px] px-4 border-r border-slate-900/20 flex items-center">Trend</div>
        <div className="flex-1 px-4 flex items-center">Action</div>
      </div>
      
      {/* Table Body */}
      <div className="relative">
        {loading && (
          <div className="p-12 text-center">
            <div className="inline-flex flex-col items-center gap-4">
              <div className="w-8 h-8 border-2 border-slate-300 border-t-cyan-500 rounded-full animate-spin"></div>
              <span className="text-sm text-slate-700 font-medium">Loading {title.toLowerCase()}...</span>
            </div>
          </div>
        )}
        {error && (
          <div className="p-12 text-center">
            <div className="inline-flex flex-col items-center gap-3">
              <div className="w-10 h-10 rounded-full bg-red-500/10 border border-red-400/30 flex items-center justify-center">
                <span className="text-red-600 text-xl">⚠</span>
              </div>
              <span className="text-sm text-red-700 font-medium">Failed to load {title.toLowerCase()}. Please try again.</span>
            </div>
          </div>
        )}
        {!loading && !error && rows.length === 0 && (
          <div className="p-12 text-center">
            <div className="inline-flex flex-col items-center gap-3">
              <div className="w-10 h-10 rounded-full bg-white/5 border border-white/10 flex items-center justify-center">
                <span className="text-slate-500 text-xl">∅</span>
              </div>
              <span className="text-sm text-slate-600 font-medium">No {title.toLowerCase()} found.</span>
            </div>
          </div>
        )}
        {!loading && !error && rows.map(r => (
          <EntityRow key={r.id} row={r} onClick={onRowClick} />
        ))}
      </div>
    </Card>
  );
}
