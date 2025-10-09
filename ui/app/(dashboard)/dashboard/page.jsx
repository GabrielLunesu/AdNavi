"use client";
import { useEffect, useState } from "react";
import { currentUser } from "../../../lib/auth";
import AssistantSection from "./components/AssistantSection";
import HomeKpiStrip from "./components/HomeKpiStrip";
import NotificationsPanel from "./components/NotificationsPanel";
import CompanyInfoCard from "./components/CompanyInfoCard";
import VisitorsChartCard from "./components/VisitorsChartCard";
import UseCasesList from "./components/UseCasesList";

export default function DashboardPage() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  
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

  if (loading) {
    return <div className="p-6">Checking authentication…</div>;
  }

  if (!user) {
    return (
      <div className="p-6">
        <div className="max-w-2xl mx-auto glass-card rounded-3xl border border-neutral-200/60 p-6">
          <h2 className="text-xl font-medium mb-2 text-neutral-900">You must be signed in.</h2>
          <a href="/" className="text-cyan-600 hover:text-cyan-700 underline">Go to sign in</a>
        </div>
      </div>
    );
  }
  
  // Define which metrics to show on the dashboard
  const dashboardMetrics = ["spend", "revenue", "roas", "clicks", "conversions", "impressions"];

  return (
    <div>
      {/* Hero Section with chat input */}
      <AssistantSection workspaceId={user.workspace_id} />

      {/* KPI Cards Grid with time range controls */}
      <div className="mb-12">
        <HomeKpiStrip 
          workspaceId={user.workspace_id} 
          metrics={dashboardMetrics}
        />
      </div>

      {/* Notifications Panel */}
      <NotificationsPanel />

      {/* Company Info + Visitors Section */}
      <div className="mb-12">
        <div className="grid grid-cols-2 gap-6">
          <CompanyInfoCard />
          <VisitorsChartCard />
        </div>
      </div>

      {/* Discover Use Cases */}
      <UseCasesList />
    </div>
  );
}
