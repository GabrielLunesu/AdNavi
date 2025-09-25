'use client'

import { useParams } from 'next/navigation';
import DetailHeader from "../../../../components/campaigns/DetailHeader";
import EntityTable from "../../../../components/campaigns/EntityTable";
import RulesPanel from "../../../../components/campaigns/RulesPanel";
import { campaignDetails } from "../../../../data/campaigns/detail";

export default function CampaignDetailPage() {
  const params = useParams();
  const id = params?.id;
  const data = campaignDetails[id];
  if (!data) return <div className="text-slate-400">No data found for this campaign.</div>;

  const title = Object.entries(campaignDetails).find(([k]) => k === id)?.[0] ? Object.keys({[id]:true}) && null : null;

  return (
    <div className="max-w-[1200px] mx-auto">
      <DetailHeader name={idToName(id)} platform={data.platform} status={'Active'} timeframe={'Last 7 days'} />
      {/* Optional: KPI strip could be added here if needed */}
      <div className="mb-6" />
      <EntityTable title={data.childLabel || inferChildLabel(data.platform)} rows={data.children || []} />
      <RulesPanel />
    </div>
  );
}

function inferChildLabel(platform) {
  if (platform === 'Google Ads') return 'Ad Groups';
  return 'Ad Sets';
}

function idToName(id) {
  // Derive a friendly title from the id if name not present in this mock context
  const map = {
    'cmp-google-brand': 'Search — Brand Core',
    'cmp-meta-prospecting-lal2': 'Prospecting — Lookalike 2%',
    'cmp-meta-retarget-30d': 'Retargeting — 30d Visitors'
  };
  return map[id] || id;
}
