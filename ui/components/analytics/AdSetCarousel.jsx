import AdSetTile from "./AdSetTile";

export default function AdSetCarousel({ items }) {
  return (
    <section className="mb-6">
      <div className="flex items-center justify-between mb-3">
        <h3 className="text-xl font-medium">Ad sets</h3>
        <button className="text-slate-400 hover:text-white" title="Each ad set's contribution and efficiency">?</button>
      </div>
      <div className="flex gap-4 overflow-x-auto pb-2">
        {items?.map((it, idx) => (
          <AdSetTile key={it.name} item={it} popoverId={`pop-${idx}`} />
        ))}
      </div>
    </section>
  );
}
