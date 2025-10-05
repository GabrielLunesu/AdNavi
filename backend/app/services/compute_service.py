"""
Compute Service
===============

Generates Pnl (Profit & Loss) snapshots by aggregating MetricFacts and computing derived metrics.

Derived Metrics v1:
- Uses app/metrics/registry for ALL metric computations (same as executor)
- Aggregates all base measures from MetricFact
- Computes derived metrics using formulas (single source of truth)
- Stores both base + derived in Pnl for fast dashboard queries

Related files:
- app/metrics/registry.py: Maps metrics → formulas (USED HERE)
- app/metrics/formulas.py: Pure functions for derived metrics
- app/dsl/executor.py: Also uses registry for ad-hoc queries
- app/models.py: ComputeRun, Pnl models

Design principles:
- Same formulas as executor → consistency guaranteed
- Workspace-scoped → no cross-tenant leaks
- Materializes expensive computations → fast dashboards
- Snapshots are "locked" historical data → can recompute if formulas change

Example usage:
    >>> from app.services.compute_service import run_compute_snapshot
    >>> from app.database import SessionLocal
    >>> 
    >>> with SessionLocal() as db:
    >>>     run_id = run_compute_snapshot(
    >>>         db=db,
    >>>         workspace_id="uuid-...",
    >>>         as_of=datetime.utcnow(),
    >>>         reason="Daily EOD snapshot"
    >>>     )
    >>>     print(f"Created compute run: {run_id}")
"""

from __future__ import annotations

import uuid
from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy import func

from app import models
from app.metrics.registry import compute_metric, get_required_bases, METRIC_REGISTRY


def run_compute_snapshot(
    db: Session,
    workspace_id: str,
    as_of: datetime,
    reason: str = "Snapshot",
    kind: str = "snapshot"
) -> str:
    """
    Run a compute operation to generate Pnl snapshots.
    
    Process:
    1. Create ComputeRun record (tracks this snapshot operation)
    2. For each provider/level/entity grouping in workspace:
       a. Aggregate all base measures from MetricFact
       b. Compute all derived metrics using app/metrics/registry
       c. Store base + derived in Pnl row
    3. Mark ComputeRun as complete
    
    Args:
        db: SQLAlchemy database session
        workspace_id: Workspace UUID (tenant scoping)
        as_of: Snapshot timestamp (what time is this snapshot for?)
        reason: Why this compute is running (for audit trail)
        kind: "snapshot" (real-time) or "eod" (end-of-day)
        
    Returns:
        ComputeRun UUID (str)
        
    Examples:
        >>> # Daily EOD snapshot
        >>> run_id = run_compute_snapshot(
        >>>     db, workspace_id="...", as_of=datetime.utcnow(),
        >>>     reason="Daily EOD", kind="eod"
        >>> )
        
        >>> # Real-time snapshot (dashboard refresh)
        >>> run_id = run_compute_snapshot(
        >>>     db, workspace_id="...", as_of=datetime.utcnow(),
        >>>     reason="Dashboard refresh", kind="snapshot"
        >>> )
    
    Design notes:
    - Materializes ALL derived metrics (not just what's requested)
    - Stores snapshots for fast dashboard queries (no real-time computation)
    - Can recompute snapshots if formulas change (track formula_version if needed)
    - Uses same formulas as executor → consistency guaranteed
    
    Related:
    - app/dsl/executor.py: Ad-hoc queries (same formulas)
    - app/metrics/registry.py: Formula definitions
    """
    
    # 1. Create ComputeRun record
    compute_run = models.ComputeRun(
        id=uuid.uuid4(),
        workspace_id=workspace_id,
        as_of=as_of,
        computed_at=datetime.utcnow(),
        reason=reason,
        status="running",
        type=models.ComputeRunTypeEnum(kind)
    )
    db.add(compute_run)
    db.flush()  # Get the run_id for Pnl foreign keys
    
    try:
        # 2. Generate Pnl snapshots for this workspace
        _generate_pnl_snapshots(
            db=db,
            workspace_id=workspace_id,
            run_id=str(compute_run.id),
            as_of=as_of,
            kind=kind
        )
        
        # 3. Mark as complete
        compute_run.status = "success"
        db.commit()
        
        return str(compute_run.id)
        
    except Exception as e:
        compute_run.status = "failed"
        db.commit()
        raise e


def _generate_pnl_snapshots(
    db: Session,
    workspace_id: str,
    run_id: str,
    as_of: datetime,
    kind: str
):
    """
    Generate Pnl snapshot rows for a workspace.
    
    This function:
    1. Queries MetricFact aggregated by provider/level/entity
    2. Computes all derived metrics using app/metrics/registry
    3. Creates Pnl rows with base + derived metrics
    
    Grouping strategy:
    - Group by: provider, level, entity_id (if entity-level snapshots)
    - Time window: Up to as_of timestamp
    - Workspace scoped: Only facts for this workspace
    
    Args:
        db: SQLAlchemy database session
        workspace_id: Workspace UUID
        run_id: ComputeRun UUID (foreign key for Pnl rows)
        as_of: Snapshot timestamp
        kind: "snapshot" or "eod"
    """
    
    MF = models.MetricFact
    E = models.Entity
    
    # Query: Aggregate all base measures by provider/level/entity
    # Derived Metrics v1: Aggregate ALL base measures (including new ones)
    aggregates = (
        db.query(
            E.id.label("entity_id"),
            MF.provider.label("provider"),
            MF.level.label("level"),
            # Original base measures
            func.coalesce(func.sum(MF.spend), 0).label("spend"),
            func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
            func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
            func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
            func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
            # Derived Metrics v1: New base measures
            func.coalesce(func.sum(MF.leads), 0).label("leads"),
            func.coalesce(func.sum(MF.installs), 0).label("installs"),
            func.coalesce(func.sum(MF.purchases), 0).label("purchases"),
            func.coalesce(func.sum(MF.visitors), 0).label("visitors"),
            func.coalesce(func.sum(MF.profit), 0).label("profit"),
        )
        .join(E, E.id == MF.entity_id)
        .filter(E.workspace_id == workspace_id)
        .filter(MF.event_at <= as_of)  # All data up to snapshot time
        .group_by(E.id, MF.provider, MF.level)
    ).all()
    
    # For each aggregation, compute derived metrics and create Pnl row
    for agg in aggregates:
        # Convert row to dict for metric computation
        totals = {
            "spend": float(agg.spend or 0),
            "revenue": float(agg.revenue or 0),
            "clicks": float(agg.clicks or 0),
            "impressions": float(agg.impressions or 0),
            "conversions": float(agg.conversions or 0),
            "leads": float(agg.leads or 0),
            "installs": float(agg.installs or 0),
            "purchases": float(agg.purchases or 0),
            "visitors": float(agg.visitors or 0),
            "profit": float(agg.profit or 0),
        }
        
        # Compute ALL derived metrics using registry
        # Derived Metrics v1: Use compute_metric() for consistency with executor
        derived_metrics = {}
        for metric_name in METRIC_REGISTRY.keys():
            value = compute_metric(metric_name, totals)
            derived_metrics[metric_name] = value
        
        # Create Pnl row with base + derived metrics
        pnl = models.Pnl(
            id=uuid.uuid4(),
            entity_id=agg.entity_id,
            run_id=run_id,
            provider=agg.provider,
            level=agg.level,
            kind=models.KindEnum(kind),
            as_of=as_of,
            event_date=None,  # Snapshot (not tied to specific date)
            computed_at=datetime.utcnow(),
            
            # Base measures
            spend=agg.spend,
            revenue=agg.revenue,
            clicks=agg.clicks,
            impressions=agg.impressions,
            conversions=agg.conversions,
            leads=agg.leads,
            installs=agg.installs,
            purchases=agg.purchases,
            visitors=agg.visitors,
            profit=agg.profit,
            
            # Derived metrics (materialized for fast dashboard queries)
            # Original derived metrics
            roas=derived_metrics.get("roas"),
            cpa=derived_metrics.get("cpa"),
            cvr=derived_metrics.get("cvr"),
            # Derived Metrics v1: New cost/efficiency metrics
            cpc=derived_metrics.get("cpc"),
            cpm=derived_metrics.get("cpm"),
            cpl=derived_metrics.get("cpl"),
            cpi=derived_metrics.get("cpi"),
            cpp=derived_metrics.get("cpp"),
            # Derived Metrics v1: New value metrics
            poas=derived_metrics.get("poas"),
            arpv=derived_metrics.get("arpv"),
            aov=derived_metrics.get("aov"),
            # Derived Metrics v1: New engagement metrics
            ctr=derived_metrics.get("ctr"),
        )
        
        db.add(pnl)
    
    db.flush()


def get_latest_snapshot(
    db: Session,
    workspace_id: str
) -> Optional[models.ComputeRun]:
    """
    Get the most recent successful compute run for a workspace.
    
    Args:
        db: SQLAlchemy database session
        workspace_id: Workspace UUID
        
    Returns:
        ComputeRun model instance, or None if no snapshots exist
        
    Examples:
        >>> latest = get_latest_snapshot(db, workspace_id="...")
        >>> if latest:
        >>>     print(f"Last snapshot: {latest.as_of}")
    """
    return (
        db.query(models.ComputeRun)
        .filter(models.ComputeRun.workspace_id == workspace_id)
        .filter(models.ComputeRun.status == "success")
        .order_by(models.ComputeRun.as_of.desc())
        .first()
    )


def recompute_derived_metrics(
    db: Session,
    run_id: str
):
    """
    Recompute derived metrics for an existing ComputeRun.
    
    Use case: Formula changed → recompute snapshots using new formulas.
    
    Process:
    1. Load all Pnl rows for this run
    2. For each row, recompute derived metrics from base measures
    3. Update Pnl row with new derived values
    
    Args:
        db: SQLAlchemy database session
        run_id: ComputeRun UUID to recompute
        
    Examples:
        >>> # Formula changed → recompute all snapshots
        >>> recompute_derived_metrics(db, run_id="...")
    
    Design notes:
    - Base measures never change (facts are immutable)
    - Only derived metrics are recomputed
    - Useful when formulas evolve (bug fixes, new logic)
    - Could track formula_version to detect when recompute is needed
    """
    
    # Load all Pnl rows for this run
    pnls = (
        db.query(models.Pnl)
        .filter(models.Pnl.run_id == run_id)
        .all()
    )
    
    # Recompute derived metrics for each Pnl
    for pnl in pnls:
        # Extract base measures from Pnl
        totals = {
            "spend": float(pnl.spend or 0),
            "revenue": float(pnl.revenue or 0),
            "clicks": float(pnl.clicks or 0),
            "impressions": float(pnl.impressions or 0),
            "conversions": float(pnl.conversions or 0),
            "leads": float(pnl.leads or 0),
            "installs": float(pnl.installs or 0),
            "purchases": float(pnl.purchases or 0),
            "visitors": float(pnl.visitors or 0),
            "profit": float(pnl.profit or 0),
        }
        
        # Recompute all derived metrics
        for metric_name in METRIC_REGISTRY.keys():
            value = compute_metric(metric_name, totals)
            setattr(pnl, metric_name, value)
        
        pnl.computed_at = datetime.utcnow()
    
    db.commit()

