"""Authentication endpoints: register, login, me, logout."""

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from .. import schemas
from ..database import get_db
from ..deps import get_current_user, get_settings
from ..models import User
from ..security import create_access_token, get_password_hash, verify_password


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def register_user(payload: schemas.UserCreate, db: Session = Depends(get_db)):
    """Register a new user.

    - If email already exists, respond with 400.
    - Store a bcrypt-hashed password.
    - Do not auto-login.
    """
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    user = User(email=payload.email, password_hash=get_password_hash(payload.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login")
def login_user(payload: schemas.UserLogin, response: Response, db: Session = Depends(get_db)):
    """Authenticate a user and set an HTTP-only JWT cookie.

    Cookie:
    - name: access_token
    - value: "Bearer <jwt>"
    - httponly: True, samesite: lax, secure: False (dev), domain from env
    - max_age: 7 days
    """
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = create_access_token(subject=user.email)
    cookie_value = f"Bearer {token}"
    settings = get_settings()
    max_age = 7 * 24 * 3600

    response.set_cookie(
        key="access_token",
        value=cookie_value,
        httponly=True,
        samesite="lax",
        secure=False,
        max_age=max_age,
        domain=settings.COOKIE_DOMAIN,
        path="/",
    )

    return {"user": schemas.UserOut.model_validate(user)}


@router.get("/me", response_model=schemas.UserOut)
def get_me(user: User = Depends(get_current_user)):
    """Return the current authenticated user."""
    return user


@router.post("/logout")
def logout_user(response: Response):
    """Clear the access token cookie."""
    response.set_cookie(
        key="access_token",
        value="",
        max_age=0,
        httponly=True,
        samesite="lax",
        secure=False,
        domain=get_settings().COOKIE_DOMAIN,
        path="/",
    )
    return {"detail": "logged out"}



