export default function MiniKPI({ label, value, delta }) {
  return (
    <div className="rounded-xl bg-gradient-to-br from-cyan-500/10 to-violet-500/10 border border-slate-700/40 p-3">
      <div className="flex items-center justify-between">
        <span className="text-xs text-slate-400">{label}</span>
        <div className="flex items-center gap-1 text-emerald-400 text-xs">
          <span>+{delta?.replace('+','')}</span>
        </div>
      </div>
      <div className="mt-1 text-2xl font-medium tracking-tight">{value}</div>
      <div className="text-[11px] text-slate-500">vs yesterday</div>
    </div>
  );
}
