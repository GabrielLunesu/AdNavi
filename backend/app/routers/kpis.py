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
- We handle both enum format (ProviderEnum.meta) and string format (meta) for provider filtering.
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
    Aggregate KPI metrics across a workspace using UnifiedMetricService.
    
    REFACTORED: Now uses UnifiedMetricService for consistent calculations
    across all endpoints (QA, KPI, entity performance, finance).
    
    Why join Entity?
      - To scope by workspace (Entity has workspace_id)
      - To optionally filter by active status

    Why MetricFact?
      - Freshest data, append-only: ideal for real-time-ish dashboards.
      - PnL remains for EOD locks & heavy reports later.
    """
    # Import UnifiedMetricService
    from app.services.unified_metric_service import UnifiedMetricService, MetricFilters
    from app.dsl.schema import TimeRange as DSLTimeRange
    
    # Initialize service
    service = UnifiedMetricService(db)
    
    # Convert request to service inputs
    start, end = _daterange(req.time_range)
    time_range = DSLTimeRange(start=start, end=end)
    
    # Handle provider format conversion
    provider_value = None
    if provider:
        if provider.startswith("ProviderEnum."):
            provider_value = provider.split(".")[1]  # Extract "meta" from "ProviderEnum.meta"
        else:
            provider_value = provider
    
    # Build filters
    filters = MetricFilters(
        provider=provider_value,
        level=level,
        status="active" if only_active else None,  # Apply status filter based on only_active
        entity_ids=None,
        entity_name=None,
        metric_filters=None
    )
    
    # Get summary metrics
    summary_result = service.get_summary(
        workspace_id=workspace_id,
        metrics=req.metrics,
        time_range=time_range,
        filters=filters,
        compare_to_previous=req.compare_to_previous
    )
    
    # Get sparkline data if requested
    sparkline = []
    if req.sparkline:
        timeseries_points = service.get_timeseries(
            workspace_id=workspace_id,
            metrics=req.metrics,
            time_range=time_range,
            filters=filters
        )
        
        # Convert to expected format
        sparkline = [
            SparkPoint(
                date=point.date,
                value=point.value
            )
            for point in timeseries_points
        ]
    
    # Convert service result to expected format
    result = []
    for metric_key in req.metrics:
        metric_data = summary_result.metrics[metric_key]
        
        result.append(KpiValue(
            key=metric_key,
            value=metric_data.value,
            prev=metric_data.previous,
            delta_pct=metric_data.delta_pct,
            sparkline=sparkline if req.sparkline else None
        ))

    return result
