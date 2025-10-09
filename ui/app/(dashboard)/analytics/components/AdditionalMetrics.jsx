"use client";
import { useEffect, useState } from "react";
import { fetchWorkspaceKpis } from "../../../../lib/api";

const LABELS = {
  ctr: "CTR",
  cpc: "CPC",
  cpa: "CPA",
  cvr: "Conversion Rate"
};

export default function AdditionalMetrics({
  workspaceId,
  selectedProvider,
  rangeDays,
  customStartDate,
  customEndDate
}) {
  const [metrics, setMetrics] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!workspaceId) return;

    let mounted = true;
    setLoading(true);

    const params = {
      workspaceId,
      metrics: ['ctr', 'cpc', 'cpa', 'cvr'],
      lastNDays: rangeDays,
      provider: selectedProvider === 'all' ? null : selectedProvider,
      compareToPrevious: false,
      sparkline: false
    };

    fetchWorkspaceKpis(params)
      .then((data) => {
        if (!mounted) return;
        setMetrics(data);
        setError(null);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Failed to fetch additional metrics:', err);
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
        <div className="grid grid-cols-2 gap-4">
          {[1, 2, 3, 4].map((i) => (
            <div key={i} className="glass-card rounded-2xl p-4 border border-neutral-200/60 animate-pulse">
              <div className="h-3 bg-neutral-200 rounded w-16 mb-2"></div>
              <div className="h-6 bg-neutral-200 rounded w-24"></div>
            </div>
          ))}
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="glass-card rounded-3xl p-8 border border-red-200/60 shadow-lg">
        <p className="text-red-600 text-sm">Failed to load metrics: {error}</p>
      </div>
    );
  }

  return (
    <div className="glass-card rounded-3xl p-8 border border-neutral-200/60 shadow-lg">
      <h3 className="text-lg font-semibold text-neutral-900 mb-6">Additional Metrics</h3>
      
      <div className="grid grid-cols-2 gap-4">
        {metrics.map((metric) => {
          // Format value based on metric type
          let displayValue = metric.value;
          if (metric.value !== null && metric.value !== undefined) {
            if (metric.key === "ctr" || metric.key === "cvr") {
              displayValue = `${(metric.value * 100).toFixed(1)}%`;
            } else if (metric.key === "cpc" || metric.key === "cpa") {
              displayValue = `$${metric.value.toFixed(2)}`;
            }
          } else {
            displayValue = "—";
          }

          return (
            <div
              key={metric.key}
              className="glass-card rounded-2xl p-4 border border-neutral-200/60 hover:border-cyan-400/60 transition-colors"
            >
              <p className="text-xs font-medium text-neutral-500 mb-1 uppercase tracking-wide">
                {LABELS[metric.key] || metric.key}
              </p>
              <p className="text-2xl font-semibold text-neutral-900">
                {displayValue}
              </p>
            </div>
          );
        })}
      </div>
    </div>
  );
}


