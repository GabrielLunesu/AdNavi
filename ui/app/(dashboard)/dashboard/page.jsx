"use client";
import { useEffect, useState } from "react";
import { currentUser } from "../../../lib/auth";
import AssistantSection from "../../../components/AssistantSection";
import TimeRangeChips from "../../../components/TimeRangeChips";
import HomeKpiStrip from "../../../components/sections/HomeKpiStrip";
import NotificationsPanel from "../../../components/NotificationsPanel";
import CompanyCard from "../../../components/CompanyCard";
import VisitorsChartCard from "../../../components/VisitorsChartCard";
import UseCasesList from "../../../components/UseCasesList";
import ChatInput from "@/components/ui/ChatInput";

export default function DashboardPage() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [selectedRange, setSelectedRange] = useState('7d');
  const [rangeDays, setRangeDays] = useState(7);
  const [rangeOffset, setRangeOffset] = useState(0);
  
  useEffect(() => {
    let mounted = true;
    currentUser()
      .then((u) => {
        if (!mounted) return;
        setUser(u);
      })
      .catch((err) => {
        console.error("Failed to get user:", err);
        if (mounted) setUser(null);
      })
      .finally(() => {
        if (mounted) setLoading(false);
      });
    return () => {
      mounted = false;
    };
  }, []);

  // Handle time range changes
  const handleRangeChange = (rangeId, days, offset = 0) => {
    setSelectedRange(rangeId);
    setRangeDays(days);
    setRangeOffset(offset);
  };

  // Get display text for the selected range
  const getRangeText = () => {
    const rangeMap = {
      'today': 'Today',
      'yesterday': 'Yesterday',
      '7d': 'Last 7 days',
      '30d': 'Last 30 days'
    };
    return rangeMap[selectedRange] || 'Last 7 days';
  };

  if (loading) {
    return <div className="p-6">Checking authentication…</div>;
  }

  if (!user) {
    return (
      <div className="p-6">
        <div className="max-w-2xl mx-auto bg-slate-900/60 border border-slate-700 rounded-xl p-6">
          <h2 className="text-xl font-medium mb-2">You must be signed in.</h2>
          <a href="/" className="text-cyan-300 hover:text-cyan-200 underline">Go to sign in</a>
        </div>
      </div>
    );
  }
  
  // Define which metrics to show on the dashboard
  const dashboardMetrics = ["spend", "revenue", "conversions", "roas", "clicks", "impressions"];

  return (
    <div className="space-y-8">
      {/* Assistant section at top (not fixed) */}
      <AssistantSection workspaceId={user.workspace_id} />

      {/* Overview header with timeframe chips */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <h2 className="text-2xl md:text-3xl font-medium tracking-tight">Overview</h2>
          <span className="text-sm text-slate-400 hidden sm:inline-block">{getRangeText()}</span>
        </div>
        <TimeRangeChips 
          activeRange={selectedRange} 
          onRangeChange={handleRangeChange} 
        />
      </div>

      {/* KPI grid: 3 per row on desktop, wrap to next row if more */}
      <HomeKpiStrip 
        workspaceId={user.workspace_id} 
        metrics={dashboardMetrics}
        lastNDays={rangeDays}
        dayOffset={rangeOffset}
      />

      <NotificationsPanel />
      <CompanyCard />
      <VisitorsChartCard />
      <UseCasesList />

      {/* Copilot quick chat */}
      {/* <section className="mt-8">
        <h2 className="text-lg font-semibold mb-2">Copilot</h2>
        <div className="sticky bottom-6">
          <ChatInput workspaceId={user.workspace_id} />
        </div>
      </section> */}
    </div>
  );
}
