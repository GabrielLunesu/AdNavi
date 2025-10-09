// Container component: owns data fetching and mapping.
// WHY: separates IO (API) from presentation (KpiCard).
import { useEffect, useState } from "react";
import { fetchWorkspaceKpis } from "../../../../lib/api";
import KPICard from "./KPICard";

const LABELS = {
  spend: "Spend",
  revenue: "Revenue",
  clicks: "Clicks",
  impressions: "Impressions",
  conversions: "Conversions",
  roas: "ROAS",
  cpa: "CPA",
};

export default function HomeKpiStrip({ workspaceId, metrics }) {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [err, setErr] = useState(null);
  const [selectedRange, setSelectedRange] = useState('30d');
  const [rangeDays, setRangeDays] = useState(30);
  const [rangeOffset, setRangeOffset] = useState(0);

  const timeRanges = [
    { id: 'yesterday', label: 'Yesterday', days: 1, offset: 1 },
    { id: '7d', label: '7d', days: 7, offset: 0 },
    { id: '30d', label: '30d', days: 30, offset: 0 },
    { id: 'custom', label: 'Custom', days: 30, offset: 0 },
  ];

  const handleRangeClick = (range) => {
    setSelectedRange(range.id);
    setRangeDays(range.days);
    setRangeOffset(range.offset);
  };

  useEffect(() => {
    let mounted = true;
    setLoading(true);
    fetchWorkspaceKpis({ workspaceId, metrics, lastNDays: rangeDays, dayOffset: rangeOffset })
      .then((data) => { 
        if (mounted) { 
          setItems(data); 
          setErr(null); 
        } 
      })
      .catch((e) => { 
        if (mounted) setErr(e.message); 
      })
      .finally(() => { 
        if (mounted) setLoading(false); 
      });
    return () => { mounted = false; };
  }, [workspaceId, JSON.stringify(metrics), rangeDays, rangeOffset]);

  return (
    <div>
      {/* Time Range Controls */}
      <div className="flex justify-end mb-6">
        <div className="flex items-center gap-2 glass-card px-4 py-2 rounded-full border border-neutral-200/60 shadow-sm">
          {timeRanges.map((range) => (
            <button
              key={range.id}
              onClick={() => handleRangeClick(range)}
              className={`px-3 py-1.5 text-xs font-medium transition-colors ${
                selectedRange === range.id
                  ? 'bg-cyan-500 text-white rounded-full'
                  : 'text-neutral-600 hover:text-neutral-900'
              }`}
            >
              {range.label}
            </button>
          ))}
        </div>
      </div>

      {/* KPI Cards Grid */}
      {loading ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {/* Skeleton loaders */}
          {[1, 2, 3, 4, 5, 6].map(i => (
            <div key={i} className="glass-card rounded-3xl p-6 border border-neutral-200/60 animate-pulse">
              <div className="h-3 bg-neutral-200 rounded w-20 mb-2"></div>
              <div className="h-8 bg-neutral-200 rounded w-32 mb-3"></div>
              <div className="h-6 bg-neutral-200 rounded w-16"></div>
            </div>
          ))}
        </div>
      ) : err ? (
        <div className="glass-card rounded-3xl p-6 border border-red-200/60">
          <div className="text-red-600 text-sm">Failed to load KPIs: {err}</div>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {items.map(k => {
            // Format value based on metric type
            let displayValue = k.value;
            if (k.value !== null && k.value !== undefined) {
              if (k.key === "roas") {
                displayValue = `${k.value.toFixed(2)}x`;
              } else if (k.key === "spend" || k.key === "revenue" || k.key === "cpa") {
                displayValue = `$${k.value.toLocaleString(undefined, { maximumFractionDigits: 0 })}`;
              } else if (k.key === "clicks" || k.key === "impressions" || k.key === "conversions") {
                displayValue = k.value.toLocaleString(undefined, { maximumFractionDigits: 0 });
              }
            } else {
              displayValue = "—";
            }

            // Convert sparkline data to simple array of values
            const sparklineData = k.sparkline ? k.sparkline.map(sp => sp.value || 0) : [];

            return (
              <KPICard
                key={k.key}
                label={LABELS[k.key] ?? k.key.toUpperCase()}
                value={displayValue}
                deltaPct={k.delta_pct ? k.delta_pct * 100 : 0}
                sparklineData={sparklineData}
              />
            );
          })}
        </div>
      )}
    </div>
  );
}

