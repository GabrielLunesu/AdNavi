"use client";
import { useState, useEffect } from "react";
import { currentUser } from "@/lib/auth";

// New components (to be created)
import TopFilters from "./components/TopFilters";
import AnalyticsKpiGrid from "./components/AnalyticsKpiGrid";
import AnalyticsChart from "./components/AnalyticsChart";
import PlatformBreakdown from "./components/PlatformBreakdown";
import AdditionalMetrics from "./components/AdditionalMetrics";
import AdNaviInsight from "./components/AdNaviInsight";

export default function AnalyticsPage() {
  // User & workspace
  const [user, setUser] = useState(null);
  const [workspaceId, setWorkspaceId] = useState(null);
  
  // Top filter state
  const [selectedProvider, setSelectedProvider] = useState('all'); // 'all', 'meta', 'google', 'tiktok', 'other'
  const [availableProviders, setAvailableProviders] = useState([]);
  const [selectedTimeframe, setSelectedTimeframe] = useState('30d'); // '7d', '30d', 'custom'
  const [rangeDays, setRangeDays] = useState(30);
  const [customStartDate, setCustomStartDate] = useState('');
  const [customEndDate, setCustomEndDate] = useState('');
  
  // Chart state
  const [selectedMetric, setSelectedMetric] = useState('revenue'); // For chart
  const [selectedGrouping, setSelectedGrouping] = useState('provider'); // 'provider', 'campaign'
  const [selectedCampaign, setSelectedCampaign] = useState(null); // For campaign grouping
  
  // Loading state
  const [loading, setLoading] = useState(true);

  // Fetch user and workspace ID on mount
  useEffect(() => {
    let mounted = true;
    currentUser()
      .then((u) => {
        if (!mounted) return;
        setUser(u);
        setWorkspaceId(u?.workspace_id);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Failed to get user:", err);
        if (mounted) {
          setUser(null);
          setLoading(false);
        }
      });
    return () => {
      mounted = false;
    };
  }, []);

  // Handlers
  const handleProviderChange = (provider) => {
    setSelectedProvider(provider);
  };

  const handleTimeframeChange = (timeframe, days) => {
    setSelectedTimeframe(timeframe);
    setRangeDays(days);
  };

  const handleCustomDateApply = (startDate, endDate) => {
    setCustomStartDate(startDate);
    setCustomEndDate(endDate);
  };

  if (loading) {
    return (
      <div className="p-12 text-center">
        <div className="w-12 h-12 border-4 border-cyan-500 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
        <p className="text-neutral-600">Loading analytics...</p>
      </div>
    );
  }

  if (!user) {
    return (
      <div className="p-12 text-center">
        <div className="glass-card rounded-3xl border border-neutral-200/60 p-6 max-w-md mx-auto">
          <h2 className="text-xl font-medium mb-2 text-neutral-900">You must be signed in.</h2>
          <a href="/login" className="text-cyan-600 hover:text-cyan-700 underline">Go to sign in</a>
        </div>
      </div>
    );
  }

  return (
    <div>
      {/* Top Filters: Provider + Timeframe */}
      <TopFilters
        selectedProvider={selectedProvider}
        availableProviders={availableProviders}
        setAvailableProviders={setAvailableProviders}
        selectedTimeframe={selectedTimeframe}
        rangeDays={rangeDays}
        workspaceId={workspaceId}
        onProviderChange={handleProviderChange}
        onTimeframeChange={handleTimeframeChange}
        onCustomDateApply={handleCustomDateApply}
      />

      {/* KPI Summary Cards (Revenue, Spend, ROAS, Conversions) */}
      <AnalyticsKpiGrid
        workspaceId={workspaceId}
        selectedProvider={selectedProvider}
        rangeDays={rangeDays}
        customStartDate={customStartDate}
        customEndDate={customEndDate}
      />

      {/* Chart Section with Metric & Grouping Dropdowns */}
      <AnalyticsChart
        workspaceId={workspaceId}
        selectedProvider={selectedProvider}
        rangeDays={rangeDays}
        customStartDate={customStartDate}
        customEndDate={customEndDate}
        selectedMetric={selectedMetric}
        setSelectedMetric={setSelectedMetric}
        selectedGrouping={selectedGrouping}
        setSelectedGrouping={setSelectedGrouping}
        selectedCampaign={selectedCampaign}
        setSelectedCampaign={setSelectedCampaign}
      />

      {/* Platform Breakdown + Additional Metrics */}
      <div className="px-8 mb-8">
        <div className="grid grid-cols-2 gap-6">
          <PlatformBreakdown
            workspaceId={workspaceId}
            selectedProvider={selectedProvider}
            rangeDays={rangeDays}
            customStartDate={customStartDate}
            customEndDate={customEndDate}
          />
          <AdditionalMetrics
            workspaceId={workspaceId}
            selectedProvider={selectedProvider}
            rangeDays={rangeDays}
            customStartDate={customStartDate}
            customEndDate={customEndDate}
          />
        </div>
      </div>

      {/* AdNavi Insight (AI widget using /qa endpoint) */}
      <AdNaviInsight
        workspaceId={workspaceId}
        selectedProvider={selectedProvider}
        selectedTimeframe={selectedTimeframe}
        rangeDays={rangeDays}
        customStartDate={customStartDate}
        customEndDate={customEndDate}
      />
    </div>
  );
}
