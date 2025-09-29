// Container component: owns data fetching and mapping.
// WHY: separates IO (API) from presentation (KpiStatCard).
import { useEffect, useState } from "react";
import { fetchWorkspaceKpis } from "@/lib/api";
import KpiStatCard from "@/components/KPIStatCard";

const LABELS = {
  spend: "Spend",
  revenue: "Revenue",
  clicks: "Clicks",
  impressions: "Impressions",
  conversions: "Conversions",
  roas: "ROAS",
  cpa: "CPA",
};

const COLOR_MAP = {
  spend: '#22d3ee',
  revenue: '#34d399',
  conversions: '#f59e0b',
  roas: '#a78bfa',
  clicks: '#60a5fa',
  impressions: '#fb7185',
  cpa: '#ef4444'
};

export default function HomeKpiStrip({ workspaceId, metrics, lastNDays = 7, dayOffset = 0 }) {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [err, setErr] = useState(null);

  useEffect(() => {
    let mounted = true;
    setLoading(true);
    fetchWorkspaceKpis({ workspaceId, metrics, lastNDays, dayOffset })
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
  }, [workspaceId, JSON.stringify(metrics), lastNDays, dayOffset]);

  if (loading) return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
      {/* Skeleton loaders */}
      {[1, 2, 3].map(i => (
        <div key={i} className="rounded-xl p-4 border border-slate-800/60 bg-slate-900/40 animate-pulse">
          <div className="h-4 bg-slate-700 rounded w-20 mb-2"></div>
          <div className="h-8 bg-slate-700 rounded w-32 mb-1"></div>
          <div className="h-3 bg-slate-700 rounded w-24"></div>
        </div>
      ))}
    </div>
  );
  
  if (err) return (
    <div className="rounded-xl p-4 border border-red-800/60 bg-red-900/20">
      <div className="text-red-400 text-sm">Failed to load KPIs: {err}</div>
    </div>
  );

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
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
          <KpiStatCard
            key={k.key}
            label={LABELS[k.key] ?? k.key.toUpperCase()}
            value={displayValue}
            deltaPct={k.delta_pct ? k.delta_pct * 100 : 0}
            sparklineData={sparklineData}
            color={COLOR_MAP[k.key]}
          />
        );
      })}
    </div>
  );
}
