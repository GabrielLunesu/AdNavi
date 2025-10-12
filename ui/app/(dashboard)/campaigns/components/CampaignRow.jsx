"use client";
import PlatformBadge from "../../../../components/campaigns/PlatformBadge";
import TrendSparkline from "../../../../components/campaigns/TrendSparkline";
import StatusPill from "../../../../components/StatusPill"; // Global StatusPill

function CellValue({ v }) {
  return <div className="text-right tabular-nums">{v || '—'}</div>;
}

// WHAT: Displays a single row in the Campaigns or Ad Sets table.
// WHY: Presentational component, receives pre-formatted data from adapter.
// REFERENCES:
// - ui/app/(dashboard)/campaigns/page.jsx (parent)
// - ui/app/(dashboard)/campaigns/[id]/page.jsx (parent)
// - ui/lib/campaignsAdapter.js (data source)
export default function CampaignRow({ row, onClick }) {
  return (
    <div
      className="grid grid-cols-12 gap-4 items-center glass-card border border-neutral-200/60 px-8 py-4 cursor-pointer hover:border-cyan-400/40 transition-all relative overflow-hidden"
      onClick={() => onClick(row.id)}
    >
      <div className="glow-edge-hover"></div>
      <div className="col-span-3">
        <p className="text-base font-semibold text-neutral-900">{row.name}</p>
        <p className="text-sm text-neutral-500 mt-0.5">{row.display?.subtitle || '—'}</p>
      </div>
      <div className="col-span-1">
        <PlatformBadge platform={row.platform} />
      </div>
      <div className="col-span-1 text-right">
        <CellValue v={row.display?.revenue} />
      </div>
      <div className="col-span-1 text-right">
        <CellValue v={row.display?.spend} />
      </div>
      <div className="col-span-1 text-right">
        <CellValue v={row.display?.roas} />
      </div>
      <div className="col-span-1 text-right">
        <CellValue v={row.display?.conversions} />
      </div>
      <div className="col-span-1 text-right">
        <CellValue v={row.display?.cpc} />
      </div>
      <div className="col-span-1 text-right">
        <CellValue v={row.display?.ctr} />
      </div>
      <div className="col-span-1">
        <StatusPill status={row.status} />
      </div>
      <div className="col-span-1">
        <TrendSparkline data={row.trend?.map(p => p.value) || []} />
      </div>
    </div>
  );
}

