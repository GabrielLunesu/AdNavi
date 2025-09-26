"""Security utilities: password hashing and JWT helpers."""

from datetime import datetime, timedelta, timezone
import os
from typing import Any, Dict

from jose import jwt, JWTError
from passlib.hash import bcrypt


ALGORITHM = "HS256"
JWT_SECRET = os.getenv("JWT_SECRET", "")
JWT_EXPIRES_MINUTES = int(os.getenv("JWT_EXPIRES_MINUTES", "10080"))

if not JWT_SECRET:
    # Attempt to load from local .env if running in dev
    try:
        from dotenv import load_dotenv  # type: ignore

        load_dotenv()
        JWT_SECRET = os.getenv("JWT_SECRET", "")
        JWT_EXPIRES_MINUTES = int(os.getenv("JWT_EXPIRES_MINUTES", "10080"))
    except Exception:
        pass

if not JWT_SECRET:
    raise RuntimeError("JWT_SECRET is not set. Ensure backend/.env is created or env var is exported.")


def get_password_hash(password: str) -> str:
    """Hash a plaintext password using bcrypt."""
    return bcrypt.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    """Verify a plaintext password against a bcrypt hash."""
    return bcrypt.verify(password, password_hash)


def create_access_token(subject: str, expires_minutes: int | None = None) -> str:
    """Create a signed JWT for the given subject (e.g., user email)."""
    if expires_minutes is None:
        expires_minutes = JWT_EXPIRES_MINUTES
    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=expires_minutes)
    to_encode: Dict[str, Any] = {"sub": subject, "iat": int(now.timestamp()), "exp": int(expire.timestamp())}
    return jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)


def decode_token(token: str) -> Dict[str, Any]:
    """Decode and validate a JWT, returning its payload.

    Raises jose.JWTError on failure.
    """
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
    except JWTError as exc:
        raise exc



