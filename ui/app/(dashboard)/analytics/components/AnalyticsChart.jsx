"use client";

export default function AnalyticsChart({
  workspaceId,
  selectedProvider,
  rangeDays,
  customStartDate,
  customEndDate,
  selectedMetric,
  setSelectedMetric,
  selectedGrouping,
  setSelectedGrouping,
  selectedCampaign,
  setSelectedCampaign
}) {
  return (
    <div className="px-8 mb-8">
      <div className="glass-card rounded-3xl p-8 border border-neutral-200/60 shadow-lg">
        <h3 className="text-lg font-semibold text-neutral-900 mb-6">Chart (Coming Soon)</h3>
        <div className="h-64 flex items-center justify-center bg-neutral-50 rounded-2xl">
          <p className="text-neutral-400">Chart implementation in progress...</p>
        </div>
      </div>
    </div>
  );
}

