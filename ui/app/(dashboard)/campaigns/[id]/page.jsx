'use client'

import { useEffect, useState, useTransition } from 'react';
import { useParams } from 'next/navigation';
import DetailHeader from '../../../../components/campaigns/DetailHeader';
import EntityTable from '../../../../components/campaigns/EntityTable';
import RulesPanel from '../../../../components/campaigns/RulesPanel';
import { fetchEntityPerformance } from '@/lib/campaignsApiClient';
import { adaptEntityPerformance } from '@/lib/campaignsAdapter';

export default function CampaignDetailPage() {
  const params = useParams();
  const id = params?.id;
  const [filters, setFilters] = useState({ timeframe: '7d' });
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [isPending, startTransition] = useTransition();

  useEffect(() => {
    if (!id) return;
    let isMounted = true;
    startTransition(() => {
      fetchEntityPerformance({
        workspaceId: 'current',
        entityLevel: 'adset',
        parentId: id,
        timeframe: filters.timeframe,
        page: 1,
        pageSize: 50,
      })
        .then((payload) => {
          if (!isMounted) return;
          setData(adaptEntityPerformance(payload));
          setError(null);
        })
        .catch((err) => {
          if (!isMounted) return;
          console.error('Failed to load ad sets', err);
          setError(err);
        });
    });
    return () => {
      isMounted = false;
    };
  }, [id, filters]);

  if (!id) {
    return <div className="text-slate-400">No campaign selected.</div>;
  }

  if (error) {
    return <div className="text-slate-400">Failed to load campaign data.</div>;
  }

  const rows = data?.rows || [];
  const meta = data?.meta;

  return (
    <div className="max-w-[1200px] mx-auto">
      <DetailHeader
        name={meta?.title || 'Campaign'}
        platform={rows[0]?.platform || '—'}
        status={rows[0]?.status || '—'}
        timeframe={filters.timeframe}
        subtitle={meta?.subtitle}
        loading={isPending}
      />
      <div className="mb-6" />
      <EntityTable title="Ad Sets" rows={rows} loading={isPending} />
      <RulesPanel />
    </div>
  );
}
