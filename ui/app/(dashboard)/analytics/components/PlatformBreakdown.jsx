"use client";
import { useEffect, useState } from "react";
import { fetchQA } from "../../../../lib/api";

const PROVIDER_COLORS = {
  google: { bg: 'rgba(234, 67, 53, 0.8)', border: '#EA4335' },
  meta: { bg: 'rgba(24, 119, 242, 0.8)', border: '#1877F2' },
  tiktok: { bg: 'rgba(37, 244, 238, 0.8)', border: '#25F4EE' },
  other: { bg: 'rgba(6, 182, 212, 0.8)', border: '#06B6D4' }
};

export default function PlatformBreakdown({
  workspaceId,
  selectedProvider,
  rangeDays,
  customStartDate,
  customEndDate
}) {
  const [breakdown, setBreakdown] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!workspaceId) return;

    let mounted = true;
    setLoading(true);

    // Generate question for platform breakdown
    const timeframeText = customStartDate && customEndDate
      ? `from ${customStartDate} to ${customEndDate}`
      : `last ${rangeDays} days`;
    
    const providerText = selectedProvider === 'all'
      ? 'all platforms'
      : selectedProvider;
    
    const question = `Show me revenue by platform for ${providerText} for the ${timeframeText}`;

    fetchQA({ workspaceId, question })
      .then((data) => {
        if (!mounted) return;
        
        // Extract breakdown data from QA response
        if (data.data && data.data.breakdown) {
          setBreakdown(data.data.breakdown);
        } else {
          setBreakdown([]);
        }
        
        setError(null);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Failed to fetch platform breakdown:', err);
        if (mounted) {
          setError(err.message);
          setLoading(false);
        }
      });

    return () => { mounted = false; };
  }, [workspaceId, selectedProvider, rangeDays, customStartDate, customEndDate]);

  if (loading) {
    return (
      <div className="glass-card rounded-3xl p-8 border border-neutral-200/60 shadow-lg">
        <div className="h-3 bg-neutral-200 rounded w-32 mb-6 animate-pulse"></div>
        <div className="space-y-4">
          {[1, 2, 3].map((i) => (
            <div key={i} className="animate-pulse">
              <div className="h-4 bg-neutral-200 rounded w-20 mb-2"></div>
              <div className="h-6 bg-neutral-200 rounded"></div>
            </div>
          ))}
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="glass-card rounded-3xl p-8 border border-red-200/60 shadow-lg">
        <p className="text-red-600 text-sm">Failed to load breakdown: {error}</p>
      </div>
    );
  }

  // Calculate total and max for percentage bars
  const total = breakdown.reduce((sum, item) => sum + (item.value || 0), 0);
  const maxValue = Math.max(...breakdown.map(item => item.value || 0));

  return (
    <div className="glass-card rounded-3xl p-8 border border-neutral-200/60 shadow-lg">
      <h3 className="text-lg font-semibold text-neutral-900 mb-6">Platform Breakdown</h3>
      
      {breakdown.length === 0 ? (
        <div className="h-48 flex items-center justify-center bg-neutral-50 rounded-2xl">
          <p className="text-neutral-400">No data available</p>
        </div>
      ) : (
        <div className="space-y-4">
          {breakdown.map((item) => {
            const percentage = total > 0 ? ((item.value / total) * 100) : 0;
            const barWidth = maxValue > 0 ? ((item.value / maxValue) * 100) : 0;
            const colors = PROVIDER_COLORS[item.label] || PROVIDER_COLORS.other;

            return (
              <div key={item.label} className="space-y-2">
                <div className="flex items-center justify-between text-sm">
                  <span className="font-medium text-neutral-700 capitalize">{item.label}</span>
                  <span className="text-neutral-900 font-semibold">
                    ${(item.value || 0).toLocaleString(undefined, { maximumFractionDigits: 0 })}
                  </span>
                </div>
                
                <div className="relative h-3 bg-neutral-100 rounded-full overflow-hidden">
                  <div
                    className="absolute top-0 left-0 h-full rounded-full transition-all duration-500"
                    style={{
                      width: `${barWidth}%`,
                      backgroundColor: colors.bg,
                      borderRight: `2px solid ${colors.border}`
                    }}
                  ></div>
                </div>
                
                <div className="text-xs text-neutral-500">
                  {percentage.toFixed(1)}% of total revenue
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

