// Placeholder for History panel (UI only)
export default function HistoryPanel({ items = [] }) {
  return (
    <div className="space-y-3">
      {items.map((it, idx) => (
        <div key={idx} className="rounded-xl p-3 border border-white/10 bg-slate-900/35 flex items-center justify-between">
          <div className="text-sm">{it.text}</div>
          <div className="flex items-center gap-3">
            <span className="text-xs px-2 py-1 rounded-full bg-white/5 border border-white/10 text-amber-300">{it.status}</span>
            <button className="text-xs text-cyan-400 hover:text-cyan-300">View AI Analysis</button>
          </div>
        </div>
      ))}
    </div>
  );
}
