import AnalyticsControls from "../../../components/analytics/AnalyticsControls";
import AICopilotHero from "../../../components/analytics/AICopilotHero";
import KPIGrid from "../../../components/analytics/KPIGrid";
import AdSetCarousel from "../../../components/analytics/AdSetCarousel";
import ChartCard from "../../../components/analytics/ChartCard";
import OpportunityRadar from "../../../components/analytics/OpportunityRadar";
import RulesPanel from "../../../components/analytics/RulesPanel";

import { analyticsHeader } from "../../../data/analytics/header";
import { analyticsKpis } from "../../../data/analytics/kpis";
import { adSets } from "../../../data/analytics/adsets";
import { opportunities } from "../../../data/analytics/opportunities";

export default function AnalyticsPage() {
  return (
    <div>
      {/* Top controls */}
      <AnalyticsControls platform={analyticsHeader.platform} campaign={analyticsHeader.campaign} />
      {/* AI hero */}
      <AICopilotHero
        title={`What happened and why — ${analyticsHeader.campaign} (${analyticsHeader.platform})`}
        summary={analyticsHeader.summary}
      />
      {/* KPIs */}
      <KPIGrid items={analyticsKpis} />
      {/* Ad sets */}
      <AdSetCarousel items={adSets} />

      {/* Main content (no right rail) */}
      <div>
        <ChartCard />
        <OpportunityRadar items={opportunities} />
        <RulesPanel />
      </div>

      {/* Empty state card would render when no selection is present (omitted) */}
    </div>
  );
}
