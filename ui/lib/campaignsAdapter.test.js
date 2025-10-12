import { describe, it, expect } from 'vitest';
import { adaptEntityPerformance } from './campaignsAdapter';

describe('campaignsAdapter', () => {
  const payload = {
    meta: {
      title: 'Campaigns',
      level: 'campaign',
      last_updated_at: '2025-10-12T10:00:00Z',
    },
    pagination: {
      total: 2,
      page: 1,
      page_size: 2,
    },
    rows: [
      {
        id: '1',
        name: 'Alpha',
        platform: 'google',
        revenue: 1200,
        spend: 400,
        roas: 3,
        conversions: 45,
        cpc: 1.11,
        ctr_pct: 3.45,
        status: 'active',
        last_updated_at: '2025-10-12T09:30:00Z',
        trend_metric: 'roas',
        trend: [
          { date: '2025-10-10', value: 2.8 },
          { date: '2025-10-11', value: null },
        ],
      },
    ],
  };

  it('formats rows and meta correctly', () => {
    const adapted = adaptEntityPerformance(payload);
    expect(adapted.meta.title).toEqual('Campaigns');
    expect(adapted.meta.subtitle).toContain('Last updated');
    expect(adapted.rows[0].display.revenue).toEqual('$1,200.00');
    expect(adapted.rows[0].display.roas).toEqual('3.00×');
    expect(adapted.rows[0].trend[1].value).toBeNull();
  });

  it('returns defaults when payload missing', () => {
    const adapted = adaptEntityPerformance(null);
    expect(adapted.rows).toEqual([]);
    expect(adapted.pagination.page).toEqual(1);
  });
});

