export default function ExpandableSections({ summary, drivers = [], suggestions = [] }) {
  return (
    <div className="mt-3 grid gap-2">
      <details className="rounded-lg border border-slate-700/40 bg-slate-900/30 backdrop-blur">
        <summary className="cursor-pointer px-3 py-2 text-sm text-slate-300 hover:text-white flex items-center justify-between">
          <span>Summary</span>
          <span className="text-slate-500">▼</span>
        </summary>
        <div className="px-3 pb-3 text-sm text-slate-300">{summary}</div>
      </details>
      <details className="rounded-lg border border-slate-700/40 bg-slate-900/30 backdrop-blur">
        <summary className="cursor-pointer px-3 py-2 text-sm text-slate-300 hover:text-white flex items-center justify-between">
          <span>Drivers</span>
          <span className="text-slate-500">▼</span>
        </summary>
        <div className="px-3 pb-3 text-sm text-slate-300">{drivers.map((d, i) => (<div key={i}>- {d}</div>))}</div>
      </details>
      <details className="rounded-lg border border-slate-700/40 bg-slate-900/30 backdrop-blur">
        <summary className="cursor-pointer px-3 py-2 text-sm text-slate-300 hover:text-white flex items-center justify-between">
          <span>Suggestions</span>
          <span className="text-slate-500">▼</span>
        </summary>
        <div className="px-3 pb-3 text-sm text-slate-300">{suggestions.map((s, i) => (<div key={i}>• {s}</div>))}</div>
      </details>
    </div>
  );
}
