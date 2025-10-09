"use client";
import { useState } from "react";
import TopBar from "./components/TopBar";
import FinancialSummaryCards from "./components/FinancialSummaryCards";
import PLTable from "./components/PLTable";
import ChartsSection from "./components/ChartsSection";
import AlertsPanel from "./components/AlertsPanel";
import AIFinancialSummary from "./components/AIFinancialSummary";

export default function FinancePage() {
  const [compareEnabled, setCompareEnabled] = useState(true);

  const handlePeriodChange = (period) => {
    console.log('Period changed to:', period);
    // TODO: Fetch data for selected period
  };

  return (
    <div>
      {/* Sticky Top Bar with Filters */}
      <TopBar
        onPeriodChange={handlePeriodChange}
        compareEnabled={compareEnabled}
        onCompareToggle={setCompareEnabled}
      />

      {/* Core Metrics Row (P&L Summary Cards) */}
      <FinancialSummaryCards />

      {/* Editable P&L Grid */}
      <PLTable />

      {/* Variance Visualization Section */}
      <ChartsSection />

      {/* Alert / Notification Panel */}
      <AlertsPanel />

      {/* Financial AI Summary (Copilot Integration) */}
      <AIFinancialSummary />
    </div>
  );
}
