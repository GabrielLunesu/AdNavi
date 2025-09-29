"""Entity management endpoints (campaigns, ad sets, ads, etc.)."""

from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from .. import schemas
from ..database import get_db
from ..deps import get_current_user
from ..models import User, Entity, Connection


router = APIRouter(
    prefix="/entities",
    tags=["Entities"],
    responses={
        401: {"model": schemas.ErrorResponse, "description": "Unauthorized"},
        403: {"model": schemas.ErrorResponse, "description": "Forbidden"},
        404: {"model": schemas.ErrorResponse, "description": "Not Found"},
        500: {"model": schemas.ErrorResponse, "description": "Internal Server Error"},
    }
)


@router.get(
    "/",
    response_model=schemas.EntityListResponse,
    summary="List entities",
    description="""
    Get entities (campaigns, ad sets, ads, etc.) for the current workspace.
    
    Entities represent the hierarchical structure of advertising campaigns:
    - Account (top level)
    - Campaign 
    - Ad Set
    - Ad
    - Creative (bottom level)
    
    Use filters to narrow down results by level, connection, or parent entity.
    """
)
def list_entities(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    level: Optional[str] = Query(None, description="Filter by entity level"),
    connection_id: Optional[UUID] = Query(None, description="Filter by connection"),
    parent_id: Optional[UUID] = Query(None, description="Filter by parent entity"),
    status: Optional[str] = Query(None, description="Filter by status"),
    limit: int = Query(100, ge=1, le=1000, description="Number of results to return"),
    offset: int = Query(0, ge=0, description="Number of results to skip")
):
    """List entities for the current workspace."""
    query = db.query(Entity).filter(
        Entity.workspace_id == current_user.workspace_id
    )
    
    # Apply filters
    if level:
        query = query.filter(Entity.level == level)
    if connection_id:
        # Verify connection belongs to user's workspace
        connection = db.query(Connection).filter(
            Connection.id == connection_id,
            Connection.workspace_id == current_user.workspace_id
        ).first()
        if not connection:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Connection not found"
            )
        query = query.filter(Entity.connection_id == connection_id)
    if parent_id:
        query = query.filter(Entity.parent_id == parent_id)
    if status:
        query = query.filter(Entity.status == status)
    
    # Get total count
    total = query.count()
    
    # Apply pagination
    entities = query.offset(offset).limit(limit).all()
    
    return schemas.EntityListResponse(
        entities=entities,
        total=total
    )


@router.post(
    "/",
    response_model=schemas.EntityOut,
    status_code=status.HTTP_201_CREATED,
    summary="Create new entity",
    description="""
    Create a new entity (campaign, ad set, ad, etc.).
    
    Entities are organized in a hierarchy. When creating an entity:
    - Specify the level (account, campaign, adset, ad, creative)
    - Optionally link to a connection (ad platform account)
    - Optionally specify a parent entity for hierarchy
    """
)
def create_entity(
    payload: schemas.EntityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new entity."""
    # Check if user has admin rights
    if current_user.role.value not in ["Owner", "Admin"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only workspace owners and admins can create entities"
        )
    
    # Validate connection if provided
    if payload.connection_id:
        connection = db.query(Connection).filter(
            Connection.id == payload.connection_id,
            Connection.workspace_id == current_user.workspace_id
        ).first()
        if not connection:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Connection not found"
            )
    
    # Validate parent entity if provided
    if payload.parent_id:
        parent = db.query(Entity).filter(
            Entity.id == payload.parent_id,
            Entity.workspace_id == current_user.workspace_id
        ).first()
        if not parent:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Parent entity not found"
            )
    
    # Check if entity with same external_id already exists for this connection
    if payload.connection_id:
        existing = db.query(Entity).filter(
            Entity.workspace_id == current_user.workspace_id,
            Entity.connection_id == payload.connection_id,
            Entity.external_id == payload.external_id
        ).first()
        
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Entity with external_id {payload.external_id} already exists for this connection"
            )
    
    entity = Entity(
        **payload.model_dump(),
        workspace_id=current_user.workspace_id
    )
    
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity


@router.get(
    "/{entity_id}",
    response_model=schemas.EntityOut,
    summary="Get entity details",
    description="""
    Get detailed information about a specific entity.
    """
)
def get_entity(
    entity_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get entity by ID."""
    entity = db.query(Entity).filter(
        Entity.id == entity_id,
        Entity.workspace_id == current_user.workspace_id
    ).first()
    
    if not entity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Entity not found"
        )
    
    return entity


@router.put(
    "/{entity_id}",
    response_model=schemas.EntityOut,
    summary="Update entity",
    description="""
    Update entity information such as name or status.
    
    Only workspace owners and admins can update entities.
    """
)
def update_entity(
    entity_id: UUID,
    payload: schemas.EntityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update entity."""
    # Check if user has admin rights
    if current_user.role.value not in ["Owner", "Admin"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only workspace owners and admins can update entities"
        )
    
    entity = db.query(Entity).filter(
        Entity.id == entity_id,
        Entity.workspace_id == current_user.workspace_id
    ).first()
    
    if not entity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Entity not found"
        )
    
    # Update fields
    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(entity, field, value)
    
    db.commit()
    db.refresh(entity)
    return entity


@router.get(
    "/{entity_id}/children",
    response_model=schemas.EntityListResponse,
    summary="Get child entities",
    description="""
    Get all child entities for a specific parent entity.
    
    For example, get all ad sets for a campaign, or all ads for an ad set.
    """
)
def get_entity_children(
    entity_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    limit: int = Query(100, ge=1, le=1000, description="Number of results to return"),
    offset: int = Query(0, ge=0, description="Number of results to skip")
):
    """Get child entities."""
    # Verify parent entity exists and belongs to user's workspace
    parent = db.query(Entity).filter(
        Entity.id == entity_id,
        Entity.workspace_id == current_user.workspace_id
    ).first()
    
    if not parent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Parent entity not found"
        )
    
    # Get children
    query = db.query(Entity).filter(
        Entity.parent_id == entity_id,
        Entity.workspace_id == current_user.workspace_id
    )
    
    total = query.count()
    children = query.offset(offset).limit(limit).all()
    
    return schemas.EntityListResponse(
        entities=children,
        total=total
    )


@router.delete(
    "/{entity_id}",
    response_model=schemas.SuccessResponse,
    summary="Delete entity",
    description="""
    Delete an entity and all its child entities.
    
    **Warning**: This will also delete all metrics and other data
    associated with this entity and its children. This action cannot be undone.
    
    Only workspace owners can delete entities.
    """
)
def delete_entity(
    entity_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete entity."""
    # Only owners can delete entities due to data impact
    if current_user.role.value != "Owner":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only workspace owners can delete entities"
        )
    
    entity = db.query(Entity).filter(
        Entity.id == entity_id,
        Entity.workspace_id == current_user.workspace_id
    ).first()
    
    if not entity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Entity not found"
        )
    
    db.delete(entity)
    db.commit()
    
    return schemas.SuccessResponse(detail="Entity deleted successfully")
