export default function SmartSuggestions({ items = [] }) {
  const list = items.slice(0, 2);
  return (
    <div className="px-3 sm:px-5 py-2">
      <div className="flex items-center gap-2 overflow-x-hidden pb-2">
        {list.map((t, i) => (
          <button key={i} className="px-3 py-1.5 rounded-full bg-slate-900/40 border border-slate-700/40 text-xs text-slate-300 hover:text-white hover:border-cyan-400/40">
            {t}
          </button>
        ))}
      </div>
    </div>
  );
}
