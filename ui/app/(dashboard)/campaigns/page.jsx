"use client";
import { useState, useEffect } from "react";
// import { useAuth } from "../../../lib/auth"; // TODO: Implement auth hook
import { campaignsApiClient, campaignsAdapter } from "../../../lib";
import TopToolbar from "./components/TopToolbar";
import CampaignTableHeader from "./components/CampaignTableHeader";
import CampaignRow from "./components/CampaignRow";
// import ActiveRulesPanel from "./components/ActiveRulesPanel"; // Not part of this task
import Card from "../../../components/Card";
import { useRouter } from "next/navigation";

export default function CampaignsPage() {
  // For now, hardcode the workspace_id from login response
  // TODO: Implement proper auth context with useAuth hook
  const workspaceId = "1e72698a-1f6c-4abb-9b99-48dba86508ce";
  const router = useRouter();

  const [campaignsData, setCampaignsData] = useState({
    meta: { title: "Campaigns", subtitle: "Loading...", level: "campaign", lastUpdatedAt: null },
    pagination: { total: 0, page: 1, pageSize: 8 },
    rows: [],
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const [filters, setFilters] = useState({
    platform: null,
    status: "active",
    timeframe: "7d",
    sortBy: "roas",
    sortDir: "desc",
    page: 1,
    pageSize: 8,
  });

  const fetchCampaigns = async () => {
    if (!workspaceId) return;
    setLoading(true);
    setError(null);
    try {
      const apiResponse = await campaignsApiClient.fetchEntityPerformance({
        workspaceId,
        entityLevel: "campaign",
        platform: filters.platform === "all" ? null : filters.platform,
        status: filters.status === "all" ? null : filters.status,
        timeframe: filters.timeframe,
        sortBy: filters.sortBy,
        sortDir: filters.sortDir,
        page: filters.page,
        pageSize: filters.pageSize,
      });
      const adaptedData = campaignsAdapter.adaptEntityPerformance(apiResponse);
      setCampaignsData(adaptedData);
    } catch (err) {
      console.error("Failed to fetch campaigns:", err);
      setError("Failed to load campaigns. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCampaigns();
  }, [workspaceId, filters]);

  const handlePlatformChange = (platform) => setFilters((prev) => ({ ...prev, platform, page: 1 }));
  const handleStatusChange = (status) => setFilters((prev) => ({ ...prev, status, page: 1 }));
  const handleSortChange = (sortBy, sortDir) => setFilters((prev) => ({ ...prev, sortBy, sortDir, page: 1 }));
  const handleTimeRangeChange = (timeframe) => setFilters((prev) => ({ ...prev, timeframe, page: 1 }));
  const handlePageChange = (newPage) => setFilters((prev) => ({ ...prev, page: newPage }));

  const handleCampaignClick = (campaignId) => {
    router.push(`/campaigns/${campaignId}`);
  };

  const { rows, meta, pagination } = campaignsData;

  return (
    <div>
      <TopToolbar
        meta={meta}
        filters={filters}
        onPlatformChange={handlePlatformChange}
        onStatusChange={handleStatusChange}
        onSortChange={handleSortChange}
        onTimeRangeChange={handleTimeRangeChange}
      />

      <div className="space-y-0">
        <CampaignTableHeader />

        <div className="space-y-2 pb-2">
          {loading && (
            <Card className="rounded-2xl p-8 text-center text-neutral-500">Loading campaigns...</Card>
          )}
          {error && (
            <Card className="rounded-2xl p-8 text-center text-red-500">
              {error}
              <button onClick={fetchCampaigns} className="ml-2 text-cyan-400 hover:underline">Retry</button>
            </Card>
          )}
          {!loading && !error && rows.length === 0 && (
            <Card className="rounded-2xl p-8 text-center text-neutral-500">
              No campaigns found for the selected filters and date range.
            </Card>
          )}
          {!loading && !error && rows.map((row) => (
            <CampaignRow key={row.id} row={row} onClick={() => handleCampaignClick(row.id)} />
          ))}
        </div>

        {/* Pagination */}
        {!loading && !error && rows.length > 0 && (
          <div className="flex items-center justify-between px-3 py-2 text-xs text-slate-400">
            <span>
              Showing {Math.min((pagination.page - 1) * pagination.pageSize + 1, pagination.total)} -{" "}
              {Math.min(pagination.page * pagination.pageSize, pagination.total)} of {pagination.total} campaigns
            </span>
            <div className="flex items-center gap-2">
              <button
                onClick={() => handlePageChange(pagination.page - 1)}
                disabled={pagination.page === 1}
                className="px-2 py-1 rounded-full border border-white/10 hover:border-slate-500/50 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                Prev
              </button>
              <button
                onClick={() => handlePageChange(pagination.page + 1)}
                disabled={pagination.page * pagination.pageSize >= pagination.total}
                className="px-2 py-1 rounded-full border border-white/10 hover:border-slate-500/50 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                Next
              </button>
            </div>
          </div>
        )}
      </div>

      {/* <ActiveRulesPanel /> Not part of this task */}
    </div>
  );
}