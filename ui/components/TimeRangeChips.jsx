// Static time range chips (non-functional)
export default function TimeRangeChips() {
  const chips = [
    { id: 'today', label: 'Today' },
    { id: '3d', label: 'Last 3d' },
    { id: '7d', label: 'Last 7d', active: true },
    { id: '30d', label: 'Last 30d' },
    { id: 'custom', label: 'Custom' },
  ];
  return (
    <div className="rounded-full p-1 border border-slate-800/60 bg-slate-900/40 inline-flex items-center gap-1">
      {chips.map((c) => (
        <button key={c.id} className={`px-3 py-1.5 rounded-full text-xs sm:text-sm ${c.active ? 'text-white bg-slate-800/60' : 'text-slate-300 hover:text-white hover:bg-slate-800/40'}`}>
          {c.label}
        </button>
      ))}
    </div>
  );
}
