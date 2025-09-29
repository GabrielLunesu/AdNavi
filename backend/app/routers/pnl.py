"""P&L (Profit & Loss) analytics endpoints."""

from datetime import datetime
from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import func

from .. import schemas
from ..database import get_db
from ..deps import get_current_user
from ..models import User, Pnl, Entity, ComputeRun


router = APIRouter(
    prefix="/pnl",
    tags=["P&L Analytics"],
    responses={
        401: {"model": schemas.ErrorResponse, "description": "Unauthorized"},
        403: {"model": schemas.ErrorResponse, "description": "Forbidden"},
        404: {"model": schemas.ErrorResponse, "description": "Not Found"},
        500: {"model": schemas.ErrorResponse, "description": "Internal Server Error"},
    }
)


@router.get(
    "/",
    response_model=schemas.PnlListResponse,
    summary="List P&L records",
    description="""
    Get profit and loss analytics for entities in the current workspace.
    
    P&L records are computed analytics that include:
    - Spend and revenue data
    - Calculated metrics (CPA, ROAS)
    - Performance indicators
    
    Use filters to narrow down results by:
    - Date range (start_date, end_date)
    - Entity (entity_id)
    - Provider (google, meta, tiktok, etc.)
    - Level (account, campaign, adset, ad)
    - Kind (snapshot, eod)
    """
)
def list_pnl(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    entity_id: Optional[UUID] = Query(None, description="Filter by entity ID"),
    provider: Optional[str] = Query(None, description="Filter by provider"),
    level: Optional[str] = Query(None, description="Filter by entity level"),
    kind: Optional[str] = Query(None, description="Filter by P&L kind (snapshot, eod)"),
    start_date: Optional[datetime] = Query(None, description="Start date filter"),
    end_date: Optional[datetime] = Query(None, description="End date filter"),
    limit: int = Query(100, ge=1, le=1000, description="Number of results to return"),
    offset: int = Query(0, ge=0, description="Number of results to skip")
):
    """List P&L records for the current workspace."""
    # Start with base query - join with Entity to filter by workspace
    query = db.query(Pnl).join(Entity).filter(
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
        query = query.filter(Pnl.entity_id == entity_id)
    
    if provider:
        query = query.filter(Pnl.provider == provider)
    
    if level:
        query = query.filter(Pnl.level == level)
    
    if kind:
        query = query.filter(Pnl.kind == kind)
    
    if start_date:
        query = query.filter(Pnl.event_date >= start_date)
    
    if end_date:
        query = query.filter(Pnl.event_date <= end_date)
    
    # Order by most recent first
    query = query.order_by(Pnl.event_date.desc())
    
    # Get total count
    total = query.count()
    
    # Apply pagination
    pnl_records = query.offset(offset).limit(limit).all()
    
    return schemas.PnlListResponse(
        pnl_data=pnl_records,
        total=total
    )


@router.get(
    "/summary",
    summary="Get P&L summary",
    description="""
    Get aggregated P&L summary for the specified filters.
    
    Returns totals and averages for:
    - Total spend and revenue
    - Total conversions, clicks, impressions
    - Average CPA and ROAS
    - Profit margins and performance indicators
    """
)
def get_pnl_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    entity_id: Optional[UUID] = Query(None, description="Filter by entity ID"),
    provider: Optional[str] = Query(None, description="Filter by provider"),
    level: Optional[str] = Query(None, description="Filter by entity level"),
    kind: Optional[str] = Query(None, description="Filter by P&L kind"),
    start_date: Optional[datetime] = Query(None, description="Start date filter"),
    end_date: Optional[datetime] = Query(None, description="End date filter")
):
    """Get aggregated P&L summary."""
    # Build the same query as list_pnl but aggregate
    query = db.query(Pnl).join(Entity).filter(
        Entity.workspace_id == current_user.workspace_id
    )
    
    # Apply same filters
    if entity_id:
        entity = db.query(Entity).filter(
            Entity.id == entity_id,
            Entity.workspace_id == current_user.workspace_id
        ).first()
        if not entity:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Entity not found"
            )
        query = query.filter(Pnl.entity_id == entity_id)
    
    if provider:
        query = query.filter(Pnl.provider == provider)
    
    if level:
        query = query.filter(Pnl.level == level)
    
    if kind:
        query = query.filter(Pnl.kind == kind)
    
    if start_date:
        query = query.filter(Pnl.event_date >= start_date)
    
    if end_date:
        query = query.filter(Pnl.event_date <= end_date)
    
    # Aggregate the P&L data
    result = query.with_entities(
        func.sum(Pnl.spend).label('total_spend'),
        func.sum(Pnl.revenue).label('total_revenue'),
        func.sum(Pnl.conversions).label('total_conversions'),
        func.sum(Pnl.clicks).label('total_clicks'),
        func.sum(Pnl.impressions).label('total_impressions'),
        func.avg(Pnl.cpa).label('avg_cpa'),
        func.avg(Pnl.roas).label('avg_roas'),
        func.count(Pnl.id).label('record_count')
    ).first()
    
    # Calculate derived metrics
    total_spend = float(result.total_spend or 0)
    total_revenue = float(result.total_revenue or 0)
    total_conversions = float(result.total_conversions or 0)
    total_clicks = int(result.total_clicks or 0)
    total_impressions = int(result.total_impressions or 0)
    avg_cpa = float(result.avg_cpa or 0)
    avg_roas = float(result.avg_roas or 0)
    record_count = int(result.record_count or 0)
    
    # Calculate additional metrics
    profit = total_revenue - total_spend
    profit_margin = (profit / total_revenue * 100) if total_revenue > 0 else 0
    overall_roas = (total_revenue / total_spend) if total_spend > 0 else 0
    overall_cpa = (total_spend / total_conversions) if total_conversions > 0 else 0
    
    return {
        "total_spend": total_spend,
        "total_revenue": total_revenue,
        "total_profit": profit,
        "profit_margin_percent": round(profit_margin, 2),
        "total_conversions": total_conversions,
        "total_clicks": total_clicks,
        "total_impressions": total_impressions,
        "overall_cpa": round(overall_cpa, 2),
        "overall_roas": round(overall_roas, 2),
        "average_cpa": round(avg_cpa, 2),
        "average_roas": round(avg_roas, 2),
        "record_count": record_count
    }


@router.get(
    "/{pnl_id}",
    response_model=schemas.PnlOut,
    summary="Get P&L record details",
    description="""
    Get detailed information about a specific P&L record.
    """
)
def get_pnl_record(
    pnl_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get P&L record by ID."""
    # Join with Entity to ensure P&L record belongs to user's workspace
    pnl_record = db.query(Pnl).join(Entity).filter(
        Pnl.id == pnl_id,
        Entity.workspace_id == current_user.workspace_id
    ).first()
    
    if not pnl_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="P&L record not found"
        )
    
    return pnl_record


@router.get(
    "/entity/{entity_id}/daily",
    summary="Get daily P&L for entity",
    description="""
    Get daily P&L analytics for a specific entity over a date range.
    
    Returns P&L data aggregated by day, useful for creating time series charts
    and performance trend analysis.
    """
)
def get_entity_daily_pnl(
    entity_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    start_date: Optional[datetime] = Query(None, description="Start date"),
    end_date: Optional[datetime] = Query(None, description="End date"),
    kind: Optional[str] = Query(None, description="Filter by P&L kind"),
    limit: int = Query(100, ge=1, le=365, description="Maximum number of days")
):
    """Get daily P&L for an entity."""
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
    query = db.query(Pnl).filter(Pnl.entity_id == entity_id)
    
    if start_date:
        query = query.filter(Pnl.event_date >= start_date)
    
    if end_date:
        query = query.filter(Pnl.event_date <= end_date)
    
    if kind:
        query = query.filter(Pnl.kind == kind)
    
    # Group by date and aggregate
    daily_pnl = query.with_entities(
        Pnl.event_date,
        func.sum(Pnl.spend).label('spend'),
        func.sum(Pnl.revenue).label('revenue'),
        func.sum(Pnl.conversions).label('conversions'),
        func.sum(Pnl.clicks).label('clicks'),
        func.sum(Pnl.impressions).label('impressions'),
        func.avg(Pnl.cpa).label('avg_cpa'),
        func.avg(Pnl.roas).label('avg_roas')
    ).group_by(Pnl.event_date).order_by(Pnl.event_date.desc()).limit(limit).all()
    
    return [
        {
            "date": record.event_date.isoformat() if record.event_date else None,
            "spend": float(record.spend or 0),
            "revenue": float(record.revenue or 0),
            "profit": float(record.revenue or 0) - float(record.spend or 0),
            "conversions": float(record.conversions or 0),
            "clicks": int(record.clicks or 0),
            "impressions": int(record.impressions or 0),
            "cpa": round(float(record.avg_cpa or 0), 2),
            "roas": round(float(record.avg_roas or 0), 2)
        }
        for record in daily_pnl
    ]


@router.get(
    "/compute-runs/",
    summary="List compute runs",
    description="""
    Get compute runs that generated P&L analytics for the workspace.
    
    Compute runs represent the batch processes that calculate P&L metrics
    from raw performance data.
    """
)
def list_compute_runs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    status: Optional[str] = Query(None, description="Filter by status"),
    type: Optional[str] = Query(None, description="Filter by compute run type"),
    limit: int = Query(50, ge=1, le=100, description="Number of results to return"),
    offset: int = Query(0, ge=0, description="Number of results to skip")
):
    """List compute runs for the current workspace."""
    query = db.query(ComputeRun).filter(
        ComputeRun.workspace_id == current_user.workspace_id
    )
    
    if status:
        query = query.filter(ComputeRun.status == status)
    
    if type:
        query = query.filter(ComputeRun.type == type)
    
    # Order by most recent first
    query = query.order_by(ComputeRun.computed_at.desc())
    
    total = query.count()
    compute_runs = query.offset(offset).limit(limit).all()
    
    return {
        "compute_runs": [
            {
                "id": str(run.id),
                "type": run.type.value,
                "status": run.status,
                "as_of": run.as_of.isoformat(),
                "computed_at": run.computed_at.isoformat(),
                "reason": run.reason
            }
            for run in compute_runs
        ],
        "total": total
    }
