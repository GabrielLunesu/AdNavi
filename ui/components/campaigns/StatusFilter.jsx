export default function StatusFilter({ value='Active', onChange }) {
  const opts = ['Active','Paused','All'];
  return (
    <div className="flex items-center gap-2">
      {opts.map(o => (
        <button key={o} onClick={() => onChange?.(o)} className={`px-3 py-1.5 text-sm rounded-full ${value===o?'bg-slate-800/60':'hover:bg-slate-800/40'}`}>{o}</button>
      ))}
    </div>
  );
}
