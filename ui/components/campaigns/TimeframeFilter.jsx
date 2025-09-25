export default function TimeframeFilter({ value='7d', onChange }) {
  const opts = ['7d','30d','Custom'];
  return (
    <div className="flex items-center gap-1 rounded-full px-1.5 py-1 border border-slate-600/40 bg-slate-900/35">
      {opts.map(o => (
        <button key={o} onClick={() => onChange?.(o)} className={`px-3 py-1.5 text-sm rounded-full ${value===o?'bg-slate-800/60':'hover:bg-slate-800/40'}`}>{o}</button>
      ))}
    </div>
  );
}
