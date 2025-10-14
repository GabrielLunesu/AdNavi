"""Performance metrics endpoints."""

from datetime import datetime
from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import func

from .. import schemas
from ..database import get_db
from ..deps import get_current_user
from ..models import User, MetricFact, Entity, Connection


router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"],
    responses={
        401: {"model": schemas.ErrorResponse, "description": "Unauthorized"},
        403: {"model": schemas.ErrorResponse, "description": "Forbidden"},
        404: {"model": schemas.ErrorResponse, "description": "Not Found"},
        500: {"model": schemas.ErrorResponse, "description": "Internal Server Error"},
    }
)


@router.get(
    "/",
    response_model=schemas.MetricListResponse,
    summary="List performance metrics",
    description="""
    Get performance metrics (spend, impressions, clicks, conversions, revenue)
    for entities in the current workspace.
    
    Use filters to narrow down results by:
    - Date range (start_date, end_date)
    - Entity (entity_id)
    - Provider (google, meta, tiktok, etc.)
    - Level (account, campaign, adset, ad)
    
    Metrics are the raw performance data imported from ad platforms.
    """
)
def list_metrics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    entity_id: Optional[UUID] = Query(None, description="Filter by entity ID"),
    provider: Optional[str] = Query(None, description="Filter by provider"),
    level: Optional[str] = Query(None, description="Filter by entity level"),
    start_date: Optional[datetime] = Query(None, description="Start date filter (YYYY-MM-DD)"),
    end_date: Optional[datetime] = Query(None, description="End date filter (YYYY-MM-DD)"),
    limit: int = Query(100, ge=1, le=1000, description="Number of results to return"),
    offset: int = Query(0, ge=0, description="Number of results to skip")
):
    """List metrics for the current workspace."""
    # Start with base query - join with Entity to filter by workspace
    query = db.query(MetricFact).join(Entity).filter(
        Entity.workspace_id == current_user.workspace_id
    )
    
    # Apply filters
    if entity_id:
        # Verify entity belongs to user's workspace
        entity = db.query(Entity).filter(
            Entity.id == entity_id,
            Entity.workspace_id == current_user.workspace_id
        ).first()
        if not entity:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Entity not found"
            )
        query = query.filter(MetricFact.entity_id == entity_id)
    
    if provider:
        query = query.filter(MetricFact.provider == provider)
    
    if level:
        query = query.filter(MetricFact.level == level)
    
    if start_date:
        query = query.filter(MetricFact.event_date >= start_date)
    
    if end_date:
        query = query.filter(MetricFact.event_date <= end_date)
    
    # Order by most recent first
    query = query.order_by(MetricFact.event_date.desc())
    
    # Get total count
    total = query.count()
    
    # Apply pagination
    metrics = query.offset(offset).limit(limit).all()
    
    return schemas.MetricListResponse(
        metrics=metrics,
        total=total
    )


@router.get(
    "/summary",
    summary="Get metrics summary",
    description="""
    Get aggregated metrics summary for the specified filters.
    
    Returns totals for:
    - Total spend
    - Total impressions 
    - Total clicks
    - Total conversions
    - Total revenue
    - Calculated CTR (click-through rate)
    - Calculated CPA (cost per acquisition)
    - Calculated ROAS (return on ad spend)
    """
)
def get_metrics_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    entity_id: Optional[UUID] = Query(None, description="Filter by entity ID"),
    provider: Optional[str] = Query(None, description="Filter by provider"),
    level: Optional[str] = Query(None, description="Filter by entity level"),
    start_date: Optional[datetime] = Query(None, description="Start date filter"),
    end_date: Optional[datetime] = Query(None, description="End date filter")
):
    """Get aggregated metrics summary using UnifiedMetricService."""
    # Import UnifiedMetricService
    from app.services.unified_metric_service import UnifiedMetricService, MetricFilters
    from app.dsl.schema import TimeRange as DSLTimeRange
    
    # Initialize service
    service = UnifiedMetricService(db)
    
    # Convert filters to service inputs
    time_range = None
    if start_date or end_date:
        time_range = DSLTimeRange(
            start=start_date.date() if start_date else None,
            end=end_date.date() if end_date else None
        )
    
    filters = MetricFilters(
        provider=provider,
        level=level,
        status=None,  # Include all entities by default
        entity_ids=[str(entity_id)] if entity_id else None,
        entity_name=None,
        metric_filters=None
    )
    
    # Get summary for all base metrics
    metrics = ["spend", "impressions", "clicks", "conversions", "revenue"]
    summary_result = service.get_summary(
        workspace_id=str(current_user.workspace_id),
        metrics=metrics,
        time_range=time_range,
        filters=filters,
        compare_to_previous=False
    )
    
    # Convert to expected format
    result = type('Result', (), {
        'total_spend': summary_result.metrics['spend'].value or 0,
        'total_impressions': summary_result.metrics['impressions'].value or 0,
        'total_clicks': summary_result.metrics['clicks'].value or 0,
        'total_conversions': summary_result.metrics['conversions'].value or 0,
        'total_revenue': summary_result.metrics['revenue'].value or 0,
        'record_count': None  # Not available from UnifiedMetricService
    })()
    
    # Calculate derived metrics
    total_spend = float(result.total_spend or 0)
    total_impressions = int(result.total_impressions or 0)
    total_clicks = int(result.total_clicks or 0)
    total_conversions = float(result.total_conversions or 0)
    total_revenue = float(result.total_revenue or 0)
    record_count = int(result.record_count or 0)
    
    # Calculate rates
    ctr = (total_clicks / total_impressions * 100) if total_impressions > 0 else 0
    cpa = (total_spend / total_conversions) if total_conversions > 0 else 0
    roas = (total_revenue / total_spend) if total_spend > 0 else 0
    
    return {
        "total_spend": total_spend,
        "total_impressions": total_impressions,
        "total_clicks": total_clicks,
        "total_conversions": total_conversions,
        "total_revenue": total_revenue,
        "ctr_percent": round(ctr, 2),
        "cpa": round(cpa, 2),
        "roas": round(roas, 2),
        "record_count": record_count
    }


@router.get(
    "/{metric_id}",
    response_model=schemas.MetricFactOut,
    summary="Get metric details",
    description="""
    Get detailed information about a specific metric record.
    """
)
def get_metric(
    metric_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get metric by ID."""
    # Join with Entity to ensure metric belongs to user's workspace
    metric = db.query(MetricFact).join(Entity).filter(
        MetricFact.id == metric_id,
        Entity.workspace_id == current_user.workspace_id
    ).first()
    
    if not metric:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Metric not found"
        )
    
    return metric


@router.get(
    "/entity/{entity_id}/daily",
    summary="Get daily metrics for entity",
    description="""
    Get daily performance metrics for a specific entity over a date range.
    
    Returns metrics aggregated by day, useful for creating time series charts.
    """
)
def get_entity_daily_metrics(
    entity_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    start_date: Optional[datetime] = Query(None, description="Start date"),
    end_date: Optional[datetime] = Query(None, description="End date"),
    limit: int = Query(100, ge=1, le=365, description="Maximum number of days")
):
    """Get daily metrics for an entity."""
    # Verify entity belongs to user's workspace
    entity = db.query(Entity).filter(
        Entity.id == entity_id,
        Entity.workspace_id == current_user.workspace_id
    ).first()
    
    if not entity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Entity not found"
        )
    
    # Build query
    query = db.query(MetricFact).filter(MetricFact.entity_id == entity_id)
    
    if start_date:
        query = query.filter(MetricFact.event_date >= start_date)
    
    if end_date:
        query = query.filter(MetricFact.event_date <= end_date)
    
    # Group by date and aggregate
    daily_metrics = query.with_entities(
        MetricFact.event_date,
        func.sum(MetricFact.spend).label('spend'),
        func.sum(MetricFact.impressions).label('impressions'),
        func.sum(MetricFact.clicks).label('clicks'),
        func.sum(MetricFact.conversions).label('conversions'),
        func.sum(MetricFact.revenue).label('revenue')
    ).group_by(MetricFact.event_date).order_by(MetricFact.event_date.desc()).limit(limit).all()
    
    return [
        {
            "date": metric.event_date.isoformat(),
            "spend": float(metric.spend or 0),
            "impressions": int(metric.impressions or 0),
            "clicks": int(metric.clicks or 0),
            "conversions": float(metric.conversions or 0),
            "revenue": float(metric.revenue or 0)
        }
        for metric in daily_metrics
    ]
