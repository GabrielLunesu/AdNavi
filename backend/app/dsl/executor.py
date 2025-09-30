"""
Query Executor
==============

Executes query plans against the database using SQLAlchemy.

WHY separate executor?
- Single source of truth for metric calculations
- Workspace scoping enforced at query level
- Divide-by-zero guards for derived metrics
- Clear separation: planning vs execution

Related files:
- app/dsl/planner.py: Creates the Plan that we execute
- app/dsl/schema.py: MetricResult that we return
- app/models.py: Database models (MetricFact, Entity)
- app/services/metric_service.py: Legacy service (being phased out)

Design:
- Workspace-scoped: ALL queries filter by workspace_id
- Safe math: Divide-by-zero guards for roas/cpa/cvr
- Efficient: Single query for summary, separate for timeseries/breakdown
- Flexible: Supports all filter combinations
"""

from __future__ import annotations

from datetime import timedelta
from typing import Optional, Dict, Any, List

from sqlalchemy.orm import Session
from sqlalchemy import func, cast, Date

from app.dsl.schema import MetricResult
from app.dsl.planner import Plan
from app import models


def _derive_metric(metric_name: str, totals: Dict[str, Any]) -> Optional[float]:
    """
    Compute a single metric value (base or derived) from aggregated totals.
    
    Args:
        metric_name: Metric to compute (spend, revenue, roas, cpa, cvr, etc.)
        totals: Dict with base measure totals (spend, revenue, clicks, etc.)
        
    Returns:
        Computed metric value, or None if cannot be computed
        
    Examples:
        >>> _derive_metric("roas", {"spend": 1000, "revenue": 2500})
        2.5
        
        >>> _derive_metric("cpa", {"spend": 1000, "conversions": 0})
        None  # Divide by zero guard
        
        >>> _derive_metric("spend", {"spend": 1000})
        1000.0
    
    Division by zero handling:
    - roas: Returns None if spend = 0
    - cpa: Returns None if conversions = 0
    - cvr: Returns None if clicks = 0
    
    Related:
    - Similar to: app/services/metric_service._derived_metric (legacy)
    - Used by: execute_plan() in this module
    """
    if totals is None:
        return None
    
    # Extract base measures (default to 0)
    spend = float(totals.get("spend") or 0)
    revenue = float(totals.get("revenue") or 0)
    clicks = float(totals.get("clicks") or 0)
    impressions = float(totals.get("impressions") or 0)
    conversions = float(totals.get("conversions") or 0)
    
    # Derived metrics with divide-by-zero guards
    if metric_name == "roas":
        return (revenue / spend) if spend > 0 else None
    
    if metric_name == "cpa":
        return (spend / conversions) if conversions > 0 else None
    
    if metric_name == "cvr":
        return (conversions / clicks) if clicks > 0 else None
    
    # Base metrics: return the value directly
    base_value = totals.get(metric_name)
    return float(base_value) if base_value is not None else None


def execute_plan(
    db: Session, 
    workspace_id: str, 
    plan: Plan
) -> MetricResult:
    """
    Execute a query plan and return aggregated results.
    
    Args:
        db: SQLAlchemy database session
        workspace_id: Workspace UUID for scoping (tenant safety)
        plan: Execution plan from build_plan()
        
    Returns:
        MetricResult with summary, comparison, timeseries, and breakdown
        
    Examples:
        >>> from app.dsl.planner import build_plan
        >>> from app.dsl.schema import MetricQuery, TimeRange
        >>> 
        >>> query = MetricQuery(metric="roas", time_range=TimeRange(last_n_days=7))
        >>> plan = build_plan(query)
        >>> result = execute_plan(db, workspace_id="...", plan=plan)
        >>> print(result.summary)
        2.45
    
    Process:
    1. Build base query (MetricFact JOIN Entity, filter by workspace)
    2. Apply date range and filters
    3. Aggregate base measures (spend, revenue, clicks, etc.)
    4. Derive metric value (roas = revenue/spend, etc.)
    5. Optionally compute previous period comparison
    6. Optionally compute daily timeseries
    7. Optionally compute breakdown by dimension
    
    Tenant safety:
    - ALL queries filter by workspace_id at the JOIN level
    - No cross-workspace data leaks possible
    
    Related:
    - Input: app/dsl/planner.Plan
    - Output: app/dsl/schema.MetricResult
    - Called by: app/services/qa_service.py
    """
    MF, E = models.MetricFact, models.Entity
    
    # --- SUMMARY AGGREGATION ---
    # Build base query: aggregate all base measures needed for the metric
    base_query = (
        db.query(
            func.coalesce(func.sum(MF.spend), 0).label("spend"),
            func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
            func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
            func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
            func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
        )
        .join(E, E.id == MF.entity_id)
        .filter(E.workspace_id == workspace_id)  # TENANT SCOPING
        .filter(cast(MF.event_date, Date).between(plan.start, plan.end))
    )
    
    # Apply filters
    if plan.filters.get("provider"):
        base_query = base_query.filter(MF.provider == plan.filters["provider"])
    if plan.filters.get("level"):
        base_query = base_query.filter(MF.level == plan.filters["level"])
    if plan.filters.get("status"):
        base_query = base_query.filter(E.status == plan.filters["status"])
    if plan.filters.get("entity_ids"):
        base_query = base_query.filter(MF.entity_id.in_(plan.filters["entity_ids"]))
    
    # Execute summary query
    totals_now = base_query.one()._asdict()
    
    # Derive metric value
    metric_name = plan.derived or plan.base_measures[0]
    summary_value = _derive_metric(metric_name, totals_now)
    
    # --- PREVIOUS PERIOD COMPARISON ---
    previous_value = None
    delta_pct = None
    
    if plan.need_previous:
        # Calculate previous period window (same length)
        period_length = (plan.end - plan.start).days + 1
        prev_start = plan.start - timedelta(days=period_length)
        prev_end = plan.start - timedelta(days=1)
        
        # Query previous period
        prev_query = (
            db.query(
                func.coalesce(func.sum(MF.spend), 0).label("spend"),
                func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
                func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
                func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
                func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
            )
            .join(E, E.id == MF.entity_id)
            .filter(E.workspace_id == workspace_id)
            .filter(cast(MF.event_date, Date).between(prev_start, prev_end))
        )
        
        # Apply same filters
        if plan.filters.get("provider"):
            prev_query = prev_query.filter(MF.provider == plan.filters["provider"])
        if plan.filters.get("level"):
            prev_query = prev_query.filter(MF.level == plan.filters["level"])
        if plan.filters.get("status"):
            prev_query = prev_query.filter(E.status == plan.filters["status"])
        if plan.filters.get("entity_ids"):
            prev_query = prev_query.filter(MF.entity_id.in_(plan.filters["entity_ids"]))
        
        totals_prev = prev_query.one()._asdict()
        previous_value = _derive_metric(metric_name, totals_prev)
        
        # Calculate delta percentage
        if previous_value not in (None, 0) and summary_value is not None:
            delta_pct = (summary_value - previous_value) / previous_value
    
    # --- TIMESERIES (daily values) ---
    timeseries = None
    
    if plan.need_timeseries:
        series_query = (
            db.query(
                MF.event_date.label("date"),
                func.coalesce(func.sum(MF.spend), 0).label("spend"),
                func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
                func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
                func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
                func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
            )
            .join(E, E.id == MF.entity_id)
            .filter(E.workspace_id == workspace_id)
            .filter(cast(MF.event_date, Date).between(plan.start, plan.end))
            .group_by(MF.event_date)
            .order_by(MF.event_date)
        )
        
        # Apply same filters
        if plan.filters.get("provider"):
            series_query = series_query.filter(MF.provider == plan.filters["provider"])
        if plan.filters.get("level"):
            series_query = series_query.filter(MF.level == plan.filters["level"])
        if plan.filters.get("status"):
            series_query = series_query.filter(E.status == plan.filters["status"])
        if plan.filters.get("entity_ids"):
            series_query = series_query.filter(MF.entity_id.in_(plan.filters["entity_ids"]))
        
        rows = series_query.all()
        timeseries = [
            {
                "date": str(row.date),
                "value": _derive_metric(metric_name, row._asdict())
            }
            for row in rows
        ]
    
    # --- BREAKDOWN (top entities by dimension) ---
    breakdown = None
    
    if plan.breakdown:
        # Map breakdown dimension to entity level
        level_map = {"campaign": "campaign", "adset": "adset", "ad": "ad"}
        breakdown_level = level_map.get(plan.breakdown)
        
        if breakdown_level:
            breakdown_query = (
                db.query(
                    E.name.label("label"),
                    func.coalesce(func.sum(MF.spend), 0).label("spend"),
                    func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
                    func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
                    func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
                    func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
                )
                .join(E, E.id == MF.entity_id)
                .filter(E.workspace_id == workspace_id)
                .filter(E.level == breakdown_level)
                .filter(cast(MF.event_date, Date).between(plan.start, plan.end))
                .group_by(E.name)
                .order_by(func.sum(MF.spend).desc())  # Sort by spend (can enhance later)
                .limit(plan.top_n)
            )
            
            # Apply same filters (except level, which is set by breakdown)
            if plan.filters.get("provider"):
                breakdown_query = breakdown_query.filter(MF.provider == plan.filters["provider"])
            if plan.filters.get("status"):
                breakdown_query = breakdown_query.filter(E.status == plan.filters["status"])
            if plan.filters.get("entity_ids"):
                breakdown_query = breakdown_query.filter(MF.entity_id.in_(plan.filters["entity_ids"]))
            
            rows = breakdown_query.all()
            breakdown = [
                {
                    "label": row.label,
                    "value": _derive_metric(metric_name, row._asdict())
                }
                for row in rows
            ]
    
    # --- BUILD RESULT ---
    return MetricResult(
        summary=summary_value,
        previous=previous_value,
        delta_pct=delta_pct,
        timeseries=timeseries,
        breakdown=breakdown
    )
