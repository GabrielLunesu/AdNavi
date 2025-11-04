"""Ad platform connection management endpoints."""

from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from .. import schemas
from ..database import get_db
from ..deps import get_current_user
from ..models import User, Connection, Workspace, ProviderEnum
from ..services.token_service import store_connection_token
from ..services.google_ads_client import GAdsClient
import os
from datetime import datetime


router = APIRouter(
    prefix="/connections",
    tags=["Connections"],
    responses={
        401: {"model": schemas.ErrorResponse, "description": "Unauthorized"},
        403: {"model": schemas.ErrorResponse, "description": "Forbidden"},
        404: {"model": schemas.ErrorResponse, "description": "Not Found"},
        500: {"model": schemas.ErrorResponse, "description": "Internal Server Error"},
    }
)


@router.get(
    "/",
    response_model=schemas.ConnectionListResponse,
    summary="List ad platform connections",
    description="""
    Get all ad platform connections for the current user's workspace.
    
    Connections represent links to advertising platforms like Google Ads,
    Meta Ads, TikTok Ads, etc.
    """
)
def list_connections(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    provider: Optional[str] = Query(None, description="Filter by provider"),
    status: Optional[str] = Query(None, description="Filter by status"),
    limit: int = Query(100, ge=1, le=1000, description="Number of results to return"),
    offset: int = Query(0, ge=0, description="Number of results to skip")
):
    """List connections for the current workspace."""
    query = db.query(Connection).filter(
        Connection.workspace_id == current_user.workspace_id
    )
    
    # Apply filters
    if provider:
        query = query.filter(Connection.provider == provider)
    if status:
        query = query.filter(Connection.status == status)
    
    # Get total count
    total = query.count()
    
    # Apply pagination
    connections = query.offset(offset).limit(limit).all()
    
    return schemas.ConnectionListResponse(
        connections=connections,
        total=total
    )


@router.post(
    "/google/from-env",
    response_model=schemas.ConnectionOut,
    status_code=status.HTTP_201_CREATED,
    summary="Create/ensure Google Ads connection from environment",
    description="""
    Creates a Google Ads connection for the current workspace using env vars:
    - GOOGLE_CUSTOMER_ID (required)
    - GOOGLE_REFRESH_TOKEN (required)
    - GOOGLE_LOGIN_CUSTOMER_ID (optional)
    - GOOGLE_DEVELOPER_TOKEN / GOOGLE_CLIENT_ID / GOOGLE_CLIENT_SECRET (required by SDK)

    Stores the refresh token encrypted. If a connection already exists, updates
    its token. Fetches timezone/currency when possible.
    """
)
def ensure_google_connection_from_env(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    customer_id = os.getenv("GOOGLE_CUSTOMER_ID")
    refresh_token = os.getenv("GOOGLE_REFRESH_TOKEN")
    developer_token = os.getenv("GOOGLE_DEVELOPER_TOKEN")
    client_id = os.getenv("GOOGLE_CLIENT_ID")
    client_secret = os.getenv("GOOGLE_CLIENT_SECRET")

    # Basic validation and clear error messaging
    missing = []
    if not customer_id:
        missing.append("GOOGLE_CUSTOMER_ID")
    if not refresh_token:
        missing.append("GOOGLE_REFRESH_TOKEN")
    for k, v in {"GOOGLE_DEVELOPER_TOKEN": developer_token, "GOOGLE_CLIENT_ID": client_id, "GOOGLE_CLIENT_SECRET": client_secret}.items():
        if not v:
            missing.append(k)
    if missing:
        raise HTTPException(status_code=400, detail=f"Missing env vars: {', '.join(sorted(set(missing)))}")

    # Normalize ID to digits only for storage; UI can format with dashes
    norm_id = "".join(ch for ch in customer_id if ch.isdigit())

    # Upsert connection
    connection = db.query(Connection).filter(
        Connection.workspace_id == current_user.workspace_id,
        Connection.provider == ProviderEnum.google,
        Connection.external_account_id == norm_id,
    ).first()

    if connection is None:
        connection = Connection(
            provider=ProviderEnum.google,
            external_account_id=norm_id,
            name=f"Google Ads - {norm_id}",
            status="active",
            connected_at=datetime.utcnow(),
            workspace_id=current_user.workspace_id,
        )
        db.add(connection)
        db.flush()

    # Store encrypted refresh token; access token remains nullable
    store_connection_token(
        db,
        connection,
        access_token=None,
        refresh_token=refresh_token,
        expires_at=None,
        scope="google-refresh-token",
        ad_account_ids=[norm_id],
    )

    # Attempt to fetch timezone/currency for nicer display (best-effort)
    try:
        meta = GAdsClient().get_customer_metadata(norm_id)
        tz = meta.get("time_zone")
        cur = meta.get("currency_code")
        if tz:
            connection.timezone = tz
        if cur:
            connection.currency_code = cur
        db.flush()
    except Exception:
        # Non-fatal; leave as None
        pass

    db.commit()
    db.refresh(connection)
    return connection


@router.post(
    "/",
    response_model=schemas.ConnectionOut,
    status_code=status.HTTP_201_CREATED,
    summary="Create new connection",
    description="""
    Create a new connection to an advertising platform.
    
    This establishes a link between your workspace and an external
    ad platform account (Google Ads, Meta, TikTok, etc.).
    """
)
def create_connection(
    payload: schemas.ConnectionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new ad platform connection."""
    # Check if user has admin rights
    if current_user.role.value not in ["Owner", "Admin"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only workspace owners and admins can create connections"
        )
    
    # Check if connection with same external_account_id already exists
    existing = db.query(Connection).filter(
        Connection.workspace_id == current_user.workspace_id,
        Connection.provider == payload.provider,
        Connection.external_account_id == payload.external_account_id
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Connection to {payload.provider} account {payload.external_account_id} already exists"
        )
    
    connection = Connection(
        **payload.model_dump(),
        workspace_id=current_user.workspace_id
    )
    
    db.add(connection)
    db.commit()
    db.refresh(connection)
    return connection


@router.get(
    "/{connection_id}",
    response_model=schemas.ConnectionOut,
    summary="Get connection details",
    description="""
    Get detailed information about a specific ad platform connection.
    """
)
def get_connection(
    connection_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get connection by ID."""
    connection = db.query(Connection).filter(
        Connection.id == connection_id,
        Connection.workspace_id == current_user.workspace_id
    ).first()
    
    if not connection:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Connection not found"
        )
    
    return connection


@router.put(
    "/{connection_id}",
    response_model=schemas.ConnectionOut,
    summary="Update connection",
    description="""
    Update connection information such as name or status.
    
    Only workspace owners and admins can update connections.
    """
)
def update_connection(
    connection_id: UUID,
    payload: schemas.ConnectionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update connection."""
    # Check if user has admin rights
    if current_user.role.value not in ["Owner", "Admin"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only workspace owners and admins can update connections"
        )
    
    connection = db.query(Connection).filter(
        Connection.id == connection_id,
        Connection.workspace_id == current_user.workspace_id
    ).first()
    
    if not connection:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Connection not found"
        )
    
    # Update fields
    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(connection, field, value)
    
    db.commit()
    db.refresh(connection)
    return connection


@router.delete(
    "/{connection_id}",
    response_model=schemas.SuccessResponse,
    summary="Delete connection",
    description="""
    Delete an ad platform connection.
    
    **Warning**: This will also delete all associated entities, metrics,
    and other data linked to this connection. This action cannot be undone.
    
    Only workspace owners can delete connections.
    """
)
def delete_connection(
    connection_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete connection."""
    # Only owners can delete connections due to data impact
    if current_user.role.value != "Owner":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only workspace owners can delete connections"
        )
    
    connection = db.query(Connection).filter(
        Connection.id == connection_id,
        Connection.workspace_id == current_user.workspace_id
    ).first()
    
    if not connection:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Connection not found"
        )
    
    db.delete(connection)
    db.commit()
    
    return schemas.SuccessResponse(detail="Connection deleted successfully")
