export default function CostRow({ row, onRemove }) {
  return (
    <div className="grid grid-cols-12 px-3 py-3 items-center">
      <div className="col-span-3 text-sm">{row.name}</div>
      <div className="col-span-2 text-sm text-slate-300">{row.amount}</div>
      <div className="col-span-3 text-sm text-slate-300">{formatRange(row.start, row.end)}</div>
      <div className="col-span-3 text-sm text-slate-400">{row.notes || ''}</div>
      <div className="col-span-1 flex items-center justify-end">
        <button onClick={() => onRemove?.(row.id)} className="px-2.5 py-1.5 text-xs rounded-full bg-rose-500/15 text-rose-300 border border-rose-400/20">Remove</button>
      </div>
    </div>
  );
}

function formatRange(start, end) {
  const f = (d) => {
    const dt = new Date(d);
    const m = dt.toLocaleString(undefined, { month:'short' });
    return `${m} ${dt.getDate()}, ${dt.getFullYear()}`;
  };
  if (start && end) return `${f(start)} – ${f(end)}`;
  if (start && !end) return f(start);
  return '—';
}
