import AssistantSection from "../../../components/AssistantSection";
import TimeRangeChips from "../../../components/TimeRangeChips";
import KPIStatCard from "../../../components/KPIStatCard";
import NotificationsPanel from "../../../components/NotificationsPanel";
import CompanyCard from "../../../components/CompanyCard";
import VisitorsChartCard from "../../../components/VisitorsChartCard";
import UseCasesList from "../../../components/UseCasesList";
import { kpis } from "../../../data/kpis";

export default function DashboardPage() {
  const colorMap = {
    spend: '#22d3ee',
    revenue: '#34d399',
    conversions: '#f59e0b',
    roas: '#a78bfa',
    clicks: '#60a5fa',
    leads: '#fb7185',
  };

  return (
    <div className="space-y-8">
      {/* Assistant section at top (not fixed) */}
      <AssistantSection />

      {/* Overview header with timeframe chips */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <h2 className="text-2xl md:text-3xl font-medium tracking-tight">Overview</h2>
          <span className="text-sm text-slate-400 hidden sm:inline-block">Last 7 days</span>
        </div>
        <TimeRangeChips />
      </div>

      {/* KPI grid: 3 per row on desktop, wrap to next row if more */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {kpis.map((k) => (
          <KPIStatCard
            key={k.id}
            label={k.label}
            value={k.value}
            deltaPct={k.deltaPct}
            sparklineData={k.sparkline}
            color={colorMap[k.id]}
          />
        ))}
      </div>

      <NotificationsPanel />
      <CompanyCard />
      <VisitorsChartCard />
      <UseCasesList />
    </div>
  );
}
