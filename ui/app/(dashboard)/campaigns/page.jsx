'use client'

import { useMemo, useState } from 'react';
import PlatformFilter from "../../../components/campaigns/PlatformFilter";
import StatusFilter from "../../../components/campaigns/StatusFilter";
import TimeframeFilter from "../../../components/campaigns/TimeframeFilter";
import SortDropdown from "../../../components/campaigns/SortDropdown";
import CampaignTable from "../../../components/campaigns/CampaignTable";
import RulesPanel from "../../../components/campaigns/RulesPanel";
import { campaigns as seed } from "../../../data/campaigns/campaigns";

export default function CampaignsPage() {
  const [platform, setPlatform] = useState('All');
  const [status, setStatus] = useState('Active');
  const [timeframe, setTimeframe] = useState('7d');
  const [sortBy, setSortBy] = useState('ROAS');
  const [page, setPage] = useState(1);

  const rows = useMemo(() => {
    let data = seed.slice();
    if (platform !== 'All') data = data.filter(r => r.platform === platform);
    if (status !== 'All') data = data.filter(r => r.status === status);
    data.sort((a, b) => {
      const ak = a.kpis, bk = b.kpis;
      if (sortBy === 'ROAS') return bk.roas - ak.roas;
      if (sortBy === 'Revenue') return bk.revenue - ak.revenue;
      if (sortBy === 'Spend') return bk.spend - ak.spend;
      if (sortBy === 'Conversions') return bk.conv - ak.conv;
      if (sortBy === 'CTR') return bk.ctr - ak.ctr;
      if (sortBy === 'CPC') return ak.cpc - bk.cpc; // lower is better
      return 0;
    });
    return data;
  }, [platform, status, sortBy]);

  return (
    <div className="max-w-[1200px] mx-auto">
      <div className="flex flex-col gap-3 lg:flex-row lg:items-center lg:justify-between mb-4">
        <div className="flex items-center gap-3 flex-wrap">
          <PlatformFilter value={platform} onChange={setPlatform} />
          <StatusFilter value={status} onChange={(v)=>{ setStatus(v); setPage(1); }} />
          <TimeframeFilter value={timeframe} onChange={setTimeframe} />
        </div>
        <SortDropdown value={sortBy} onChange={setSortBy} />
      </div>

      <CampaignTable rows={rows} page={page} pageSize={8} onPrev={()=>setPage(p=>Math.max(1,p-1))} onNext={()=>setPage(p=>p+1)} />

      <RulesPanel />
    </div>
  );
}
