"use client";
import { useEffect, useState } from "react";
import { fetchWorkspaceKpis } from "../../../../lib/api";

const LABELS = {
  revenue: "Revenue",
  spend: "Spend",
  roas: "ROAS",
  conversions: "Conversions"
};

export default function AnalyticsKpiGrid({
  workspaceId,
  selectedProvider,
  rangeDays,
  customStartDate,
  customEndDate
}) {
  const [kpis, setKpis] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!workspaceId) return;

    let mounted = true;
    setLoading(true);

    const params = {
      workspaceId,
      metrics: ['revenue', 'spend', 'roas', 'conversions'],
      lastNDays: rangeDays,
      provider: selectedProvider === 'all' ? null : selectedProvider,
      compareToPrevious: false, // Commented out for now
      sparkline: false, // Don't need sparklines for KPI cards
      customStartDate: customStartDate || null,
      customEndDate: customEndDate || null
    };

    fetchWorkspaceKpis(params)
      .then((data) => {
        if (!mounted) return;
        setKpis(data);
        setError(null);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Failed to fetch KPIs:', err);
        if (mounted) {
          setError(err.message);
          setLoading(false);
        }
      });

    return () => { mounted = false; };
  }, [workspaceId, selectedProvider, rangeDays, customStartDate, customEndDate]);

  if (loading) {
    return (
      <div className="px-8 mb-8">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {[1, 2, 3, 4].map((i) => (
            <div key={i} className="glass-card rounded-3xl p-6 border border-neutral-200/60 animate-pulse">
              <div className="h-3 bg-neutral-200 rounded w-20 mb-3"></div>
              <div className="h-8 bg-neutral-200 rounded w-32 mb-2"></div>
            </div>
          ))}
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="px-8 mb-8">
        <div className="glass-card rounded-3xl p-6 border border-red-200/60">
          <p className="text-red-600 text-sm">Failed to load KPIs: {error}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="px-8 mb-8">
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        {kpis.map((kpi) => {
          // Format value based on metric type
          let displayValue = kpi.value;
          if (kpi.value !== null && kpi.value !== undefined) {
            if (kpi.key === "roas") {
              displayValue = `${kpi.value.toFixed(2)}x`;
            } else if (kpi.key === "spend" || kpi.key === "revenue") {
              displayValue = `$${kpi.value.toLocaleString(undefined, { maximumFractionDigits: 0 })}`;
            } else if (kpi.key === "conversions") {
              displayValue = kpi.value.toLocaleString(undefined, { maximumFractionDigits: 0 });
            }
          } else {
            displayValue = "—";
          }

          // Determine color based on metric and change
          let changeColor = 'text-neutral-600';
          if (kpi.delta_pct) {
            if (kpi.key === 'spend') {
              // For spend, negative is good (green), positive is bad (red)
              changeColor = kpi.delta_pct < 0 ? 'text-green-600' : 'text-red-600';
            } else {
              // For revenue, roas, conversions: positive is good
              changeColor = kpi.delta_pct > 0 ? 'text-green-600' : 'text-red-600';
            }
          }

          return (
            <div
              key={kpi.key}
              className="glass-card rounded-3xl p-6 border border-neutral-200/60 shadow-lg card-hover relative overflow-hidden"
            >
              <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-cyan-400 to-cyan-600"></div>
              
              <p className="text-xs font-medium text-neutral-500 mb-2 uppercase tracking-wide">
                {LABELS[kpi.key] || kpi.key}
              </p>
              
              <p className="text-3xl font-semibold text-neutral-900 mb-3">
                {displayValue}
              </p>
              
              {/* Change percentage (commented out for now) */}
              {/* {kpi.delta_pct !== null && kpi.delta_pct !== undefined && (
                <div className={`text-sm font-medium ${changeColor}`}>
                  {kpi.delta_pct > 0 ? '+' : ''}{(kpi.delta_pct * 100).toFixed(1)}%
                </div>
              )} */}
            </div>
          );
        })}
      </div>
    </div>
  );
}

