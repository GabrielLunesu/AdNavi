import Link from "next/link";

export default function DetailHeader({ name, platform, status, timeframe = 'Last 7 days' }) {
  return (
    <div className="mb-4">
      <div className="text-xs text-slate-400 mb-1">
        <Link href="/campaigns" className="hover:underline">Campaigns</Link> <span className="mx-1">›</span> <span className="text-slate-300">{name}</span>
      </div>
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-medium tracking-tight">{name}</h2>
          <div className="text-slate-400 text-sm mt-1">{platform} • {status} • {timeframe}</div>
        </div>
        <div className="flex items-center gap-2">
          <button className="rounded-full px-3 py-1.5 text-sm border border-slate-600/40 bg-slate-900/35">Export</button>
          <button className="rounded-full px-3 py-1.5 text-sm border border-slate-600/40 bg-slate-900/35">Customize</button>
        </div>
      </div>
    </div>
  );
}
