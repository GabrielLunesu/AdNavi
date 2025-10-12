'use client'

import { useEffect, useState, useTransition } from 'react';
import { useParams } from 'next/navigation';
import DetailHeader from '../../../../../components/campaigns/DetailHeader';
import EntityTable from '../../../../../components/campaigns/EntityTable';
import { campaignsApiClient, campaignsAdapter } from '../../../../../lib';

export default function AdSetDetailPage() {
  const params = useParams();
  const adsetId = params?.adsetId;
  // TODO: Get workspace ID from auth context
  const workspaceId = "1e72698a-1f6c-4abb-9b99-48dba86508ce";
  
  const [filters, setFilters] = useState({ 
    timeframe: '7d',
    status: 'active',
    sortBy: 'roas',
    sortDir: 'desc',
    platform: null,
  });
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [isPending, startTransition] = useTransition();

  useEffect(() => {
    if (!adsetId) return;
    let isMounted = true;
    startTransition(() => {
      campaignsApiClient.fetchEntityPerformance({
        workspaceId,
        entityLevel: 'ad',
        parentId: adsetId,
        timeframe: filters.timeframe,
        status: filters.status,
        sortBy: filters.sortBy,
        sortDir: filters.sortDir,
        platform: filters.platform,
        page: 1,
        pageSize: 50,
      })
        .then((payload) => {
          if (!isMounted) return;
          setData(campaignsAdapter.adaptEntityPerformance(payload));
          setError(null);
        })
        .catch((err) => {
          if (!isMounted) return;
          console.error('Failed to load ads', err);
          setError(err);
        });
    });
    return () => {
      isMounted = false;
    };
  }, [adsetId, filters, workspaceId]);

  if (!adsetId) {
    return <div className="text-slate-400">No ad set selected.</div>;
  }

  const rows = data?.rows || [];
  const meta = data?.meta;

  return (
    <div className="max-w-[1200px] mx-auto">
      <DetailHeader
        name={meta?.title || 'Ad Set'}
        platform={rows[0]?.platform || '—'}
        status={rows[0]?.status || '—'}
        timeframe={filters.timeframe}
        subtitle={meta?.subtitle}
        loading={isPending}
      />
      <div className="mb-6" />
      <EntityTable 
        title="Ads" 
        rows={rows} 
        loading={isPending}
        error={error}
        onRowClick={null} // Ads are leaf nodes, no drill-down
      />
    </div>
  );
}

