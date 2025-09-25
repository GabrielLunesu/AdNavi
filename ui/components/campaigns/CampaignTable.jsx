import Card from "../../components/Card";
import CampaignRow from "./CampaignRow";

export default function CampaignTable({ rows = [], page = 1, pageSize = 8, onPrev, onNext }) {
  const total = rows.length;
  const startIdx = (page - 1) * pageSize;
  const pageRows = rows.slice(startIdx, startIdx + pageSize);
  return (
    <Card className="rounded-2xl">
      <div className="px-3 py-2 text-xs text-slate-400 flex items-center justify-between">
        <span>Campaign Overview</span>
      </div>
      <div className="grid grid-cols-[2fr_1fr_repeat(6,1fr)_1fr_1fr] px-3 py-2 text-xs text-slate-400 bg-white/5 border-y border-white/10">
        <div>Campaign</div>
        <div>Platform</div>
        <div className="text-right">Revenue</div>
        <div className="text-right">Spend</div>
        <div className="text-right">ROAS</div>
        <div className="text-right">Conversions</div>
        <div className="text-right">CPC</div>
        <div className="text-right">CTR</div>
        <div>Status</div>
        <div>Trend</div>
        <div className="text-right">Action</div>
      </div>
      <div className="divide-y divide-white/10">
        {pageRows.map(r => (
          <CampaignRow key={r.id} row={r} />
        ))}
      </div>
      <div className="px-3 py-2 text-xs text-slate-400 flex items-center justify-between">
        <span>Showing {Math.min(page * pageSize, total)} of {total} campaigns</span>
        <div className="flex items-center gap-2">
          <button onClick={onPrev} className="px-2 py-1 rounded-full border border-white/10 hover:border-slate-500/50">Prev</button>
          <button onClick={onNext} className="px-2 py-1 rounded-full border border-white/10 hover:border-slate-500/50">Next</button>
        </div>
      </div>
    </Card>
  );
}
