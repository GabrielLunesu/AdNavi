"""
KPI router
----------
Purpose:
- Provide a single aggregated endpoint for the homepage KPI cards.
- Computes totals from MetricFact (freshest, append-only) across the workspace.
- Optionally filters by provider/level and active entities.
- Computes derived metrics (ROAS, CPA) with divide-by-zero guards.
Design choices:
- This endpoint returns exactly the data the homepage needs in one call.
- We avoid N+1 calls from the UI and centralize the metric math here.
"""

from datetime import date, timedelta
from typing import Optional, List, Union
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db
from app import models
from app.schemas import KpiRequest, KpiValue, TimeRange, SparkPoint
from app.metrics.registry import compute_metric, get_required_bases, is_base_measure

router = APIRouter(prefix="/workspaces", tags=["kpis"])

def _daterange(tr: TimeRange) -> tuple[date, date]:
    """Resolve the date range into [start, end] inclusive."""
    if tr.start and tr.end:
        return (tr.start, tr.end)
    n = tr.last_n_days or 7
    end = date.today()
    start = end - timedelta(days=n - 1)
    return (start, end)

def _derived(metric_key: str, totals: dict) -> Optional[float]:
    """
    Compute ANY metric (base or derived) using the metrics registry.
    
    This now supports all 22 metrics (10 base + 12 derived) via the centralized
    compute_metric function from app.metrics.registry.
    
    WHY: Single source of truth for metric formulas, divide-by-zero guards included.
    """
    if totals is None:
        return None
    
    # Use the metrics registry to compute the metric
    return compute_metric(metric_key, totals)

@router.post("/{workspace_id}/kpis", response_model=List[KpiValue])
def get_workspace_kpis(
    workspace_id: str,
    req: KpiRequest,
    db: Session = Depends(get_db),
    provider: Optional[str] = Query(default=None, description="Optional provider filter (google/meta/tiktok/other/mock)"),
    level: Optional[str] = Query(default=None, description="Optional entity level filter (campaign/adset/ad/...)"),
    only_active: bool = Query(default=True, description="If true, exclude non-active entities"),
):
    """
    Aggregate KPI metrics across a workspace.
    Why join Entity?
      - To scope by workspace (Entity has workspace_id)
      - To optionally filter by active status

    Why MetricFact?
      - Freshest data, append-only: ideal for real-time-ish dashboards.
      - PnL remains for EOD locks & heavy reports later.
    """
    MF, E = models.MetricFact, models.Entity
    start, end = _daterange(req.time_range)

    # Base aggregate for current period
    # Aggregate ALL base measures so derived metrics can be computed
    base = (
        db.query(
            func.coalesce(func.sum(MF.spend), 0).label("spend"),
            func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
            func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
            func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
            func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
            func.coalesce(func.sum(MF.leads), 0).label("leads"),
            func.coalesce(func.sum(MF.installs), 0).label("installs"),
            func.coalesce(func.sum(MF.purchases), 0).label("purchases"),
            func.coalesce(func.sum(MF.visitors), 0).label("visitors"),
            func.coalesce(func.sum(MF.profit), 0).label("profit"),
        )
        .join(E, E.id == MF.entity_id)
        .filter(E.workspace_id == workspace_id)
        .filter(MF.event_date.between(start, end))
    )
    if provider:
        base = base.filter(MF.provider == provider)
    if level:
        base = base.filter(MF.level == level)
    if only_active:
        base = base.filter(E.status == "active")

    totals_now = base.one()._asdict()

    # Previous period (same length) if requested
    totals_prev = None
    if req.compare_to_previous:
        length_days = (end - start).days + 1
        prev_start = start - timedelta(days=length_days)
        prev_end = start - timedelta(days=1)
        prev = (
            db.query(
                func.coalesce(func.sum(MF.spend), 0).label("spend"),
                func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
                func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
                func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
                func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
                func.coalesce(func.sum(MF.leads), 0).label("leads"),
                func.coalesce(func.sum(MF.installs), 0).label("installs"),
                func.coalesce(func.sum(MF.purchases), 0).label("purchases"),
                func.coalesce(func.sum(MF.visitors), 0).label("visitors"),
                func.coalesce(func.sum(MF.profit), 0).label("profit"),
            )
            .join(E, E.id == MF.entity_id)
            .filter(E.workspace_id == workspace_id)
            .filter(MF.event_date.between(prev_start, prev_end))
        )
        if provider:
            prev = prev.filter(MF.provider == provider)
        if level:
            prev = prev.filter(MF.level == level)
        if only_active:
            prev = prev.filter(E.status == "active")
        totals_prev = prev.one()._asdict()

    # Daily sparkline by date (optional)
    spark_by_day: dict[str, dict] = {}
    if req.sparkline:
        sparkline_query = (
            db.query(
                MF.event_date.label("d"),
                func.coalesce(func.sum(MF.spend), 0).label("spend"),
                func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
                func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
                func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
                func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
                func.coalesce(func.sum(MF.leads), 0).label("leads"),
                func.coalesce(func.sum(MF.installs), 0).label("installs"),
                func.coalesce(func.sum(MF.purchases), 0).label("purchases"),
                func.coalesce(func.sum(MF.visitors), 0).label("visitors"),
                func.coalesce(func.sum(MF.profit), 0).label("profit"),
            )
            .join(E, E.id == MF.entity_id)
            .filter(E.workspace_id == workspace_id)
            .filter(MF.event_date.between(start, end))
        )
        # Apply the same filters as the main query
        if provider:
            sparkline_query = sparkline_query.filter(MF.provider == provider)
        if level:
            sparkline_query = sparkline_query.filter(MF.level == level)
        if only_active:
            sparkline_query = sparkline_query.filter(E.status == "active")
        
        day_rows = (
            sparkline_query
            .group_by(MF.event_date)
            .order_by(MF.event_date)
            .all()
        )
        for r in day_rows:
            # Convert datetime to date string (YYYY-MM-DD format only)
            date_key = r.d.strftime('%Y-%m-%d') if hasattr(r.d, 'strftime') else str(r.d)
            spark_by_day[date_key] = {
                "spend": r.spend, "revenue": r.revenue, "clicks": r.clicks,
                "impressions": r.impressions, "conversions": r.conversions,
                "leads": r.leads, "installs": r.installs, "purchases": r.purchases,
                "visitors": r.visitors, "profit": r.profit
            }

    # Build per-metric cards
    out: List[KpiValue] = []
    for key in req.metrics:
        now_val = _derived(key, totals_now)
        prev_val = _derived(key, totals_prev) if totals_prev else None
        delta_pct = None
        if prev_val not in (None, 0) and now_val is not None:
            delta_pct = (now_val - prev_val) / prev_val

        spark = None
        if req.sparkline:
            spark = []
            cur = start
            while cur <= end:
                # Ensure date format matches the dictionary keys (YYYY-MM-DD)
                d = cur.strftime('%Y-%m-%d') if hasattr(cur, 'strftime') else str(cur)
                pieces = spark_by_day.get(d, {})
                # Always use _derived() to handle both base and derived metrics correctly
                spark_val = _derived(key, pieces)
                spark.append(SparkPoint(date=d, value=spark_val))
                cur += timedelta(days=1)

        out.append(KpiValue(key=key, value=now_val, prev=prev_val, delta_pct=delta_pct, sparkline=spark))

    return out
