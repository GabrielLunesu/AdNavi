"""Pydantic schemas for request/response payloads."""

from datetime import datetime
from pydantic import BaseModel, EmailStr, constr


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

    id: int
    email: EmailStr
    created_at: datetime

    model_config = {"from_attributes": True}


class TokenPayload(BaseModel):
    """JWT token contents."""

    sub: str
    exp: int



