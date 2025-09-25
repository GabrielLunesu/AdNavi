import KPICard from "./KPICard";

export default function KPIGrid({ items }) {
  return (
    <section className="mb-6 mt-6">
      <div className="flex items-center justify-between mb-3">
        <h3 className="text-xl font-medium">Campaign KPIs</h3>
        <div className="flex items-center gap-2">
          <span className="text-xs px-2 py-1 rounded-full bg-white/5 border border-white/10 text-slate-300">ROAS</span>
          <span className="text-xs px-2 py-1 rounded-full bg-white/5 border border-white/10 text-slate-300">CPA</span>
          <span className="text-xs px-2 py-1 rounded-full bg-white/5 border border-white/10 text-slate-300">CTR</span>
        </div>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {items?.map((k) => (
          <KPICard key={k.key} {...k} />
        ))}
      </div>
    </section>
  );
}
