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
  );
  
  if (err) return (
    <div className="glass-card rounded-3xl p-6 border border-red-200/60">
      <div className="text-red-600 text-sm">Failed to load KPIs: {err}</div>
    </div>
  );

  return (
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
  );
}

