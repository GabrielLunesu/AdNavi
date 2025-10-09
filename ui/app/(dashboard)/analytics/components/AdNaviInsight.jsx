"use client";

export default function AdNaviInsight({
  workspaceId,
  selectedProvider,
  selectedTimeframe,
  rangeDays,
  customStartDate,
  customEndDate
}) {
  return (
    <div className="px-8 mb-8">
      <div className="glass-card rounded-3xl p-8 border border-neutral-200/60 shadow-lg">
        <div className="flex items-center gap-3 mb-4">
          <div className="w-10 h-10 rounded-full bg-gradient-to-br from-cyan-400 to-cyan-600 flex items-center justify-center">
            <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
          </div>
          <h3 className="text-lg font-semibold text-neutral-900">AdNavi Insight</h3>
        </div>
        <div className="h-32 flex items-center justify-center bg-neutral-50 rounded-2xl">
          <p className="text-neutral-400">AI insights coming soon...</p>
        </div>
      </div>
    </div>
  );
}

