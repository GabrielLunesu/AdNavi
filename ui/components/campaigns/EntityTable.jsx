import Card from "../Card";
import EntityRow from "./EntityRow";

export default function EntityTable({ title, rows = [], loading = false, error = null }) {
  return (
    <Card className="rounded-2xl">
      <div className="px-3 py-2 text-xs text-slate-400 flex items-center justify-between">
        <span>{title}</span>
        {loading ? <span className="text-emerald-300">Loading…</span> : null}
      </div>
      <div className="grid grid-cols-[2fr_repeat(6,1fr)_1fr_1fr] px-3 py-2 text-xs text-slate-400 bg-white/5 border-y border-white/10">
        <div>Name</div>
        <div className="text-right">Revenue</div>
        <div className="text-right">Spend</div>
        <div className="text-right">ROAS</div>
        <div className="text-right">Conversions</div>
        <div className="text-right">CPC</div>
        <div className="text-right">CTR</div>
        <div>Status</div>
        <div>Trend</div>
        <div className="text-right">Action</div>
      </div>
      <div className="divide-y divide-white/10">
        {loading && (
          <div className="p-8 text-center text-slate-400">Loading {title.toLowerCase()}...</div>
        )}
        {error && (
          <div className="p-8 text-center text-red-400">Failed to load {title.toLowerCase()}. Please try again.</div>
        )}
        {!loading && !error && rows.length === 0 && (
          <div className="p-8 text-center text-slate-400">No {title.toLowerCase()} found.</div>
        )}
        {!loading && !error && rows.map(r => (
          <EntityRow key={r.id} row={r} />
        ))}
      </div>
    </Card>
  );
}
