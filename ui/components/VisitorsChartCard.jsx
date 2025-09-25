import Card from "./Card";
import LineChart from "./LineChart";
import { visitorsSeries, visitorsMeta } from "../data/visitors";

export default function VisitorsChartCard() {
  return (
    <Card>
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 mb-4">
        <h3 className="text-lg font-medium tracking-tight">Website Visitors</h3>
        <div className="flex items-center gap-6">
          <div className="flex items-center gap-2">
            <span className="text-slate-400 text-xs">Visitors this period</span>
            <span className="text-sm text-slate-200">{visitorsMeta.visitorsThisPeriod}</span>
          </div>
          <div className="flex items-center gap-2">
            <span className="text-slate-400 text-xs">Avg Session Duration</span>
            <span className="text-sm text-slate-200">{visitorsMeta.avgSessionDuration}</span>
          </div>
          <div className="flex items-center gap-2">
            <span className="text-slate-400 text-xs">Conversion Rate</span>
            <span className="text-sm text-slate-200">{visitorsMeta.conversionRate}</span>
          </div>
        </div>
      </div>
      <div className="rounded-xl border border-slate-800/60 p-3">
        <LineChart data={visitorsSeries} />
      </div>
    </Card>
  );
}
