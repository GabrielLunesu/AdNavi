"use client";

export default function AdditionalMetrics({
  workspaceId,
  selectedProvider,
  rangeDays,
  customStartDate,
  customEndDate
}) {
  return (
    <div className="glass-card rounded-3xl p-8 border border-neutral-200/60 shadow-lg">
      <h3 className="text-lg font-semibold text-neutral-900 mb-6">Additional Metrics</h3>
      <div className="h-48 flex items-center justify-center bg-neutral-50 rounded-2xl">
        <p className="text-neutral-400">CTR, CPC, CPA, CVR metrics coming soon...</p>
      </div>
    </div>
  );
}

