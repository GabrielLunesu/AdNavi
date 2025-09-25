import Card from "../../components/Card";
import { rightRail } from "../../data/analytics/panel";

export default function RightRailAIPanel() {
  return (
    <Card className="rounded-2xl sticky top-6">
      <div className="flex items-center justify-between mb-2">
        <h4 className="text-lg font-medium">AI Panel</h4>
        <button className="text-slate-400 hover:text-white">?</button>
      </div>
      <div className="text-sm text-slate-300 space-y-2">
        {rightRail.map((t, i) => (
          <p key={i}>{t}</p>
        ))}
      </div>
      <div className="mt-3 flex flex-col gap-2">
        <button className="px-3 py-1.5 text-sm rounded-full border border-slate-600/40 bg-slate-900/35 hover:border-teal-400/60">Apply to Plan</button>
        <button className="px-3 py-1.5 text-sm rounded-full border border-slate-600/40 bg-slate-900/35 hover:border-cyan-400/60">Export PDF</button>
        <button className="px-3 py-1.5 text-sm rounded-full border border-slate-600/40 bg-slate-900/35 hover:border-violet-400/60">Save Scenario</button>
      </div>
    </Card>
  );
}
