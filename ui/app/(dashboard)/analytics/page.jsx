"use client";
import { useState } from "react";
import TopBar from "./components/TopBar";
import KPISummary from "./components/KPISummary";
import TrendChart from "./components/TrendChart";
import PlatformBreakdown from "./components/PlatformBreakdown";
import MetricBreakdown from "./components/MetricBreakdown";
import AIInsightPanel from "./components/AIInsightPanel";
import PerformanceSnapshots from "./components/PerformanceSnapshots";

// Mock KPI data - replace with real data from API
const kpis = [
  {
    label: 'Revenue',
    value: '$89,240',
    change: '+18.2%',
    changePercent: 18.2,
    sparklineData: [42000, 48000, 52000, 58000, 64000, 72000, 81000, 89240],
  },
  {
    label: 'Spend',
    value: '$24,580',
    change: '-5.3%',
    changePercent: -5.3,
    sparklineData: [26000, 25500, 25200, 25000, 24800, 24700, 24600, 24580],
  },
  {
    label: 'ROAS',
    value: '3.63x',
    change: '+12.4%',
    changePercent: 12.4,
    sparklineData: [3.1, 3.2, 3.3, 3.4, 3.5, 3.55, 3.6, 3.63],
  },
  {
    label: 'Conversions',
    value: '1,294',
    change: '+8.7%',
    changePercent: 8.7,
    sparklineData: [1000, 1050, 1100, 1150, 1200, 1230, 1260, 1294],
  },
];

export default function AnalyticsPage() {
  const [selectedPlatform, setSelectedPlatform] = useState('all');
  const [selectedTime, setSelectedTime] = useState('30d');

  const handlePlatformChange = (platform) => {
    setSelectedPlatform(platform);
    // TODO: Fetch data for selected platform
  };

  const handleTimeChange = (time) => {
    setSelectedTime(time);
    // TODO: Fetch data for selected time range
  };

  return (
    <div>
      {/* Sticky Top Bar with Filters */}
      <TopBar 
        onPlatformChange={handlePlatformChange}
        onTimeChange={handleTimeChange}
      />

      {/* KPI Summary Cards */}
      <KPISummary kpis={kpis} />

      {/* Trend Chart */}
      <TrendChart />

      {/* Breakdown Grid */}
      <div className="mx-8 mb-8">
        <div className="grid grid-cols-2 gap-6">
          <PlatformBreakdown />
          <MetricBreakdown />
        </div>
      </div>

      {/* AI Insight Panel */}
      <AIInsightPanel />

      {/* Performance Snapshots */}
      <PerformanceSnapshots />
    </div>
  );
}
