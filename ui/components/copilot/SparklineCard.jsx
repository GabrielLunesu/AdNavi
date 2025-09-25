export default function SparklineCard({ label, value }) {
  return (
    <div className="rounded-xl bg-gradient-to-br from-violet-500/10 to-teal-500/10 border border-slate-700/40 p-3">
      <div className="flex items-center justify-between">
        <span className="text-xs text-slate-400">{label}</span>
        <span className="text-sm text-slate-200">{value}</span>
      </div>
      <div className="mt-2 h-16">
        <svg viewBox="0 0 100 40" className="w-full h-full">
          <polyline fill="none" stroke="#a78bfa" strokeWidth="2" points="0,30 10,28 20,26 30,22 40,18 50,14 60,12 70,10 80,8 90,6 100,5" />
        </svg>
      </div>
    </div>
  );
}
