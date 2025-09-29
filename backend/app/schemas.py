"""Pydantic schemas for request/response payloads."""

from datetime import datetime
from uuid import UUID
from typing import Optional, List
from pydantic import BaseModel, EmailStr, constr, Field
from .models import RoleEnum, ProviderEnum, LevelEnum, KindEnum, ComputeRunTypeEnum


class UserCreate(BaseModel):
    """Payload for user registration."""

    email: EmailStr = Field(
        description="User email address",
        example="user@company.com"
    )
    password: constr(min_length=8) = Field(
        description="Password (minimum 8 characters)",
        example="securePassword123"
    )
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "john.doe@company.com",
                "password": "securePassword123"
            }
        }
    }


class UserLogin(BaseModel):
    """Payload for user login."""

    email: EmailStr = Field(
        description="User email address",
        example="user@company.com"
    )
    password: str = Field(
        description="User password",
        example="securePassword123"
    )
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "john.doe@company.com",
                "password": "securePassword123"
            }
        }
    }


class UserOut(BaseModel):
    """Public representation of a user."""

    id: UUID = Field(
        description="Unique user identifier",
        example="123e4567-e89b-12d3-a456-426614174000"
    )
    email: EmailStr = Field(
        description="User email address",
        example="john.doe@company.com"
    )
    name: str = Field(
        description="User display name",
        example="John Doe"
    )
    role: RoleEnum = Field(
        description="User role within the workspace",
        example="Admin"
    )
    workspace_id: UUID = Field(
        description="ID of the workspace this user belongs to",
        example="456e7890-e89b-12d3-a456-426614174001"
    )

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "email": "john.doe@company.com",
                "name": "John Doe",
                "role": "Admin",
                "workspace_id": "456e7890-e89b-12d3-a456-426614174001"
            }
        }
    }


class TokenPayload(BaseModel):
    """JWT token contents."""

    sub: str = Field(
        description="Subject (user email)",
        example="user@company.com"
    )
    exp: int = Field(
        description="Token expiration timestamp",
        example=1640995200
    )


class LoginResponse(BaseModel):
    """Response from successful login."""
    
    user: UserOut = Field(
        description="Authenticated user information"
    )
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "user": {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "email": "john.doe@company.com",
                    "name": "John Doe",
                    "role": "Admin",
                    "workspace_id": "456e7890-e89b-12d3-a456-426614174001"
                }
            }
        }
    }


class ErrorResponse(BaseModel):
    """Standard error response."""
    
    detail: str = Field(
        description="Error message",
        example="Invalid credentials"
    )
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "detail": "Invalid credentials"
            }
        }
    }


class SuccessResponse(BaseModel):
    """Standard success response."""
    
    detail: str = Field(
        description="Success message",
        example="Operation completed successfully"
    )
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "detail": "logged out"
            }
        }
    }


class HealthResponse(BaseModel):
    """Health check response."""
    
    status: str = Field(
        description="Service status",
        example="ok"
    )
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "status": "ok"
            }
        }
    }


# Workspace Schemas
class WorkspaceCreate(BaseModel):
    """Schema for creating a new workspace."""
    
    name: str = Field(
        description="Workspace name",
        example="ACME Corp Marketing",
        min_length=1,
        max_length=100
    )


class WorkspaceUpdate(BaseModel):
    """Schema for updating workspace."""
    
    name: Optional[str] = Field(
        None,
        description="Updated workspace name",
        example="ACME Corp Marketing - Updated",
        min_length=1,
        max_length=100
    )


class WorkspaceOut(BaseModel):
    """Public representation of a workspace."""
    
    id: UUID = Field(description="Unique workspace identifier")
    name: str = Field(description="Workspace name")
    created_at: datetime = Field(description="Creation timestamp")
    
    model_config = {"from_attributes": True}


# Connection Schemas
class ConnectionCreate(BaseModel):
    """Schema for creating a new ad platform connection."""
    
    provider: ProviderEnum = Field(
        description="Ad platform provider",
        example="google"
    )
    external_account_id: str = Field(
        description="Account ID in the external platform",
        example="123-456-7890"
    )
    name: str = Field(
        description="Friendly name for this connection",
        example="ACME Google Ads"
    )
    status: str = Field(
        description="Connection status",
        example="active"
    )


class ConnectionUpdate(BaseModel):
    """Schema for updating connection."""
    
    name: Optional[str] = Field(None, description="Updated connection name")
    status: Optional[str] = Field(None, description="Updated connection status")


class ConnectionOut(BaseModel):
    """Public representation of a connection."""
    
    id: UUID = Field(description="Unique connection identifier")
    provider: ProviderEnum = Field(description="Ad platform provider")
    external_account_id: str = Field(description="External account ID")
    name: str = Field(description="Connection name")
    status: str = Field(description="Connection status")
    connected_at: datetime = Field(description="Connection timestamp")
    workspace_id: UUID = Field(description="Associated workspace ID")
    
    model_config = {"from_attributes": True}


# Entity Schemas
class EntityCreate(BaseModel):
    """Schema for creating a new entity (campaign, ad set, ad, etc.)."""
    
    level: LevelEnum = Field(
        description="Entity level in hierarchy",
        example="campaign"
    )
    external_id: str = Field(
        description="ID in the external ad platform",
        example="camp_123456"
    )
    name: str = Field(
        description="Entity name",
        example="Summer Sale Campaign"
    )
    status: str = Field(
        description="Entity status",
        example="active"
    )
    connection_id: Optional[UUID] = Field(
        None,
        description="Associated connection ID"
    )
    parent_id: Optional[UUID] = Field(
        None,
        description="Parent entity ID (for hierarchy)"
    )


class EntityUpdate(BaseModel):
    """Schema for updating entity."""
    
    name: Optional[str] = Field(None, description="Updated entity name")
    status: Optional[str] = Field(None, description="Updated entity status")


class EntityOut(BaseModel):
    """Public representation of an entity."""
    
    id: UUID = Field(description="Unique entity identifier")
    level: LevelEnum = Field(description="Entity level")
    external_id: str = Field(description="External platform ID")
    name: str = Field(description="Entity name")
    status: str = Field(description="Entity status")
    workspace_id: UUID = Field(description="Associated workspace ID")
    connection_id: Optional[UUID] = Field(description="Associated connection ID")
    parent_id: Optional[UUID] = Field(description="Parent entity ID")
    
    model_config = {"from_attributes": True}


# MetricFact Schemas
class MetricFactOut(BaseModel):
    """Public representation of performance metrics."""
    
    id: UUID = Field(description="Unique metric identifier")
    provider: ProviderEnum = Field(description="Data provider")
    level: LevelEnum = Field(description="Entity level")
    event_date: datetime = Field(description="Event date")
    spend: float = Field(description="Ad spend amount")
    impressions: int = Field(description="Number of impressions")
    clicks: int = Field(description="Number of clicks")
    conversions: Optional[float] = Field(description="Number of conversions")
    revenue: Optional[float] = Field(description="Revenue amount")
    currency: str = Field(description="Currency code")
    entity_id: Optional[UUID] = Field(description="Associated entity ID")
    
    model_config = {"from_attributes": True}


# P&L Schemas
class PnlOut(BaseModel):
    """Public representation of P&L data."""
    
    id: UUID = Field(description="Unique P&L identifier")
    provider: ProviderEnum = Field(description="Data provider")
    level: LevelEnum = Field(description="Entity level")
    kind: KindEnum = Field(description="P&L calculation type")
    event_date: Optional[datetime] = Field(description="Event date")
    spend: float = Field(description="Total spend")
    revenue: Optional[float] = Field(description="Total revenue")
    conversions: Optional[float] = Field(description="Total conversions")
    clicks: int = Field(description="Total clicks")
    impressions: int = Field(description="Total impressions")
    cpa: Optional[float] = Field(description="Cost per acquisition")
    roas: Optional[float] = Field(description="Return on ad spend")
    entity_id: Optional[UUID] = Field(description="Associated entity ID")
    
    model_config = {"from_attributes": True}


# List Response Schemas
class WorkspaceListResponse(BaseModel):
    """Response schema for workspace list."""
    
    workspaces: List[WorkspaceOut] = Field(description="List of workspaces")
    total: int = Field(description="Total number of workspaces")


class ConnectionListResponse(BaseModel):
    """Response schema for connection list."""
    
    connections: List[ConnectionOut] = Field(description="List of connections")
    total: int = Field(description="Total number of connections")


class EntityListResponse(BaseModel):
    """Response schema for entity list."""
    
    entities: List[EntityOut] = Field(description="List of entities")
    total: int = Field(description="Total number of entities")


class MetricListResponse(BaseModel):
    """Response schema for metrics list."""
    
    metrics: List[MetricFactOut] = Field(description="List of metrics")
    total: int = Field(description="Total number of metrics")


class PnlListResponse(BaseModel):
    """Response schema for P&L list."""
    
    pnl_data: List[PnlOut] = Field(description="List of P&L records")
    total: int = Field(description="Total number of P&L records")



