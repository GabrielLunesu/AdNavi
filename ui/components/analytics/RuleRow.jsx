export default function RuleRow({ parts }) {
  return (
    <div className="rounded-xl p-3 border border-white/10 bg-slate-900/35">
      <div className="flex flex-wrap items-center gap-2 text-sm">
        {parts.map((p, i) => (
          <span key={i} className="px-2 py-1 rounded-full bg-white/5 border border-white/10">{p}</span>
        ))}
      </div>
    </div>
  );
}
