// WHAT: Adapter that converts backend EntityPerformanceResponse into
//       dumb view models for Campaigns UI.
// WHY: Keep formatting/string manipulation out of components.
// REFERENCES:
//   - backend app/schemas.py::EntityPerformanceResponse
//   - backend router entity_performance.py (fields, meanings)

const formatCurrency = (value) => {
  if (value == null) return '—';
  return Number(value).toLocaleString(undefined, {
    style: 'currency',
    currency: 'USD',
    maximumFractionDigits: value >= 100 ? 0 : 2,
  });
};

const formatNumber = (value) => {
  if (value == null) return '—';
  return Number(value).toLocaleString(undefined, { maximumFractionDigits: 0 });
};

const formatRatio = (value) => {
  if (value == null) return '—';
  return `${Number(value).toFixed(2)}×`;
};

const formatPercentage = (value) => {
  if (value == null) return '—';
  return `${Number(value).toFixed(2)}%`;
};

const relativeTime = (isoDate) => {
  if (!isoDate) return 'Last updated —';
  const now = new Date();
  const then = new Date(isoDate);
  const diff = Math.max(0, now.getTime() - then.getTime());
  const minutes = Math.floor(diff / 60000);
  if (minutes < 1) return 'Last updated just now';
  if (minutes < 60) return `Last updated ${minutes}m ago`;
  const hours = Math.floor(minutes / 60);
  if (hours < 24) return `Last updated ${hours}h ago`;
  const days = Math.floor(hours / 24);
  return `Last updated ${days}d ago`;
};

const alignTrend = (points, fillValue) => {
  if (!Array.isArray(points) || points.length === 0) return [];
  return points.map((point) => {
    if (point.value == null && fillValue != null) {
      return { ...point, value: fillValue };
    }
    return point;
  });
};

export const adaptEntityPerformance = (payload) => {
  if (!payload) return { rows: [], meta: null, pagination: { total: 0, page: 1, pageSize: 25 } };

  const rows = (payload.rows || []).map((row) => {
    const trendMetric = row.trend_metric;
    const fillWith = trendMetric === 'revenue' ? 0 : null;
    // Infer level from meta if not present on row
    const level = row.level || payload.meta?.level;
    return {
      id: row.id,
      name: row.name,
      platform: row.platform,
      status: row.status,
      level: level, // Used to determine if entity has children
      revenueRaw: row.revenue,
      spendRaw: row.spend,
      roasRaw: row.roas,
      conversionsRaw: row.conversions,
      cpcRaw: row.cpc,
      ctrRaw: row.ctr_pct,
      lastUpdatedAt: row.last_updated_at,
      trendMetric,
      trend: alignTrend(row.trend || [], fillWith),
      display: {
        revenue: formatCurrency(row.revenue),
        spend: formatCurrency(row.spend),
        roas: formatRatio(row.roas),
        conversions: formatNumber(row.conversions),
        cpc: formatCurrency(row.cpc),
        ctr: row.ctr_pct == null ? '—' : `${Number(row.ctr_pct).toFixed(2)}%`,
        subtitle: relativeTime(row.last_updated_at),
      },
    };
  });

  const meta = payload.meta
    ? {
        title: payload.meta.title,
        level: payload.meta.level,
        subtitle: relativeTime(payload.meta.last_updated_at),
      }
    : null;

  const pagination = payload.pagination
    ? {
        total: payload.pagination.total,
        page: payload.pagination.page,
        pageSize: payload.pagination.page_size,
      }
    : { total: rows.length, page: 1, pageSize: rows.length };

  return { rows, meta, pagination };
};


