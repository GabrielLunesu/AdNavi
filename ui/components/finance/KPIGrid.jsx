import KPICard from "./KPICard";

export default function KPIGrid({ kpis }) {
  const items = [kpis.spend, kpis.revenue, kpis.roas, kpis.conversions];
  const colors = ['#f43f5e', '#a78bfa', '#60a5fa', '#10b981'];
  return (
    <div className="mb-6">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {items.map((it, idx) => (
          <KPICard key={it.label} {...it} color={colors[idx]} />
        ))}
      </div>
    </div>
  );
}
