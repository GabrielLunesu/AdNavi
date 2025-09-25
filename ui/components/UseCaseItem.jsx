export default function UseCaseItem({ title, cta }) {
  return (
    <div className="rounded-lg border border-slate-800/60 p-4 bg-slate-900/30 flex items-center justify-between">
      <p className="text-sm text-slate-200">{title}</p>
      <button className="text-xs text-cyan-400 hover:text-cyan-300">{cta}</button>
    </div>
  );
}
