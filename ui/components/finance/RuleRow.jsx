export default function RuleRow({ rule, onRemove }) {
  return (
    <div className="rounded-xl p-3 border border-white/10 bg-slate-900/35 flex items-center justify-between">
      <div className="text-sm">{rule.label}</div>
      <div className="flex items-center gap-2">
        <span className="text-xs px-2 py-1 rounded-full bg-white/5 border border-white/10 text-cyan-300">In-app</span>
        <button onClick={() => onRemove?.(rule.id)} className="px-2.5 py-1.5 text-xs rounded-full bg-rose-500/15 text-rose-300 border border-rose-400/20">Remove</button>
      </div>
    </div>
  );
}
