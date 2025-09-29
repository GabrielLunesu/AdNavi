"""Workspace management endpoints."""

from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import schemas
from ..database import get_db
from ..deps import get_current_user
from ..models import User, Workspace


router = APIRouter(
    prefix="/workspaces",
    tags=["Workspaces"],
    responses={
        401: {"model": schemas.ErrorResponse, "description": "Unauthorized"},
        403: {"model": schemas.ErrorResponse, "description": "Forbidden"},
        404: {"model": schemas.ErrorResponse, "description": "Not Found"},
        500: {"model": schemas.ErrorResponse, "description": "Internal Server Error"},
    }
)


@router.get(
    "/",
    response_model=schemas.WorkspaceListResponse,
    summary="List workspaces",
    description="""
    Get a list of all workspaces accessible to the current user.
    
    Currently, users can only access their own workspace, but this will be
    extended in the future to support multi-workspace access.
    """
)
def list_workspaces(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List all workspaces accessible to the current user."""
    # For now, users only have access to their own workspace
    # TODO: Implement multi-workspace access with proper permissions
    workspace = db.query(Workspace).filter(Workspace.id == current_user.workspace_id).first()
    
    if not workspace:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workspace not found"
        )
    
    return schemas.WorkspaceListResponse(
        workspaces=[workspace],
        total=1
    )


@router.get(
    "/{workspace_id}",
    response_model=schemas.WorkspaceOut,
    summary="Get workspace details",
    description="""
    Get detailed information about a specific workspace.
    
    Users can only access workspaces they belong to.
    """
)
def get_workspace(
    workspace_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get workspace by ID."""
    # Check if user has access to this workspace
    if current_user.workspace_id != workspace_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied to this workspace"
        )
    
    workspace = db.query(Workspace).filter(Workspace.id == workspace_id).first()
    if not workspace:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workspace not found"
        )
    
    return workspace


@router.put(
    "/{workspace_id}",
    response_model=schemas.WorkspaceOut,
    summary="Update workspace",
    description="""
    Update workspace information.
    
    Only workspace owners and admins can update workspace details.
    """
)
def update_workspace(
    workspace_id: UUID,
    payload: schemas.WorkspaceUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update workspace."""
    # Check if user has access to this workspace
    if current_user.workspace_id != workspace_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied to this workspace"
        )
    
    # Check if user has admin rights
    if current_user.role.value not in ["Owner", "Admin"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only workspace owners and admins can update workspace details"
        )
    
    workspace = db.query(Workspace).filter(Workspace.id == workspace_id).first()
    if not workspace:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workspace not found"
        )
    
    # Update fields
    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(workspace, field, value)
    
    db.commit()
    db.refresh(workspace)
    return workspace


@router.get(
    "/{workspace_id}/users",
    response_model=List[schemas.UserOut],
    summary="List workspace users",
    description="""
    Get all users in a workspace.
    
    Only workspace members can view the user list.
    """
)
def list_workspace_users(
    workspace_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List all users in a workspace."""
    # Check if user has access to this workspace
    if current_user.workspace_id != workspace_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied to this workspace"
        )
    
    # Get all users in the workspace
    users = db.query(User).filter(User.workspace_id == workspace_id).all()
    return users
