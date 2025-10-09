export default function CampaignTableHeader() {
  return (
    <div className="glass-card rounded-t-3xl border border-b-0 border-neutral-200/60 px-8 py-4 sticky-header">
      <div className="grid grid-cols-12 gap-4 text-xs font-semibold text-neutral-500 uppercase tracking-wide">
        <div className="col-span-3">Campaign Name</div>
        <div className="col-span-1">Platform</div>
        <div className="col-span-1 text-right">Revenue</div>
        <div className="col-span-1 text-right">Spend</div>
        <div className="col-span-1 text-right">ROAS</div>
        <div className="col-span-1 text-right">Conv.</div>
        <div className="col-span-1 text-right">CPC</div>
        <div className="col-span-1 text-right">CTR</div>
        <div className="col-span-1">Status</div>
        <div className="col-span-1">Trend</div>
      </div>
    </div>
  );
}

