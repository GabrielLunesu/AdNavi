"""Pydantic schemas for request/response payloads."""

from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr, constr
from .models import RoleEnum


class UserCreate(BaseModel):
    """Payload for user registration."""

    email: EmailStr
    password: constr(min_length=8)


class UserLogin(BaseModel):
    """Payload for user login."""

    email: EmailStr
    password: str


class UserOut(BaseModel):
    """Public representation of a user."""

    id: UUID
    email: EmailStr
    name: str
    role: RoleEnum
    workspace_id: UUID

    model_config = {"from_attributes": True}


class TokenPayload(BaseModel):
    """JWT token contents."""

    sub: str
    exp: int



