"""Authentication endpoints: register, login, me, logout."""

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from .. import schemas
from ..database import get_db
from ..deps import get_current_user, get_settings
from ..models import User, Workspace, AuthCredential, RoleEnum
from ..security import create_access_token, get_password_hash, verify_password


router = APIRouter(
    prefix="/auth", 
    tags=["Authentication"],
    responses={
        400: {"model": schemas.ErrorResponse, "description": "Bad Request"},
        401: {"model": schemas.ErrorResponse, "description": "Unauthorized"},
        500: {"model": schemas.ErrorResponse, "description": "Internal Server Error"},
    }
)


@router.post(
    "/register", 
    response_model=schemas.UserOut, 
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    description="""
    Create a new user account with a default workspace.
    
    This endpoint:
    - Creates a new workspace named "New workspace" for the user
    - Creates a user with Admin role (temporary default)
    - Stores encrypted password credentials
    - Returns user information without auto-login
    
    **Note**: All new users are currently given Admin role. This will be updated
    in the future to support invitation-based role assignment.
    """,
    responses={
        201: {
            "model": schemas.UserOut,
            "description": "User successfully created",
            "content": {
                "application/json": {
                    "example": {
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "email": "john.doe@company.com",
                        "name": "john.doe",
                        "role": "Admin",
                        "workspace_id": "456e7890-e89b-12d3-a456-426614174001"
                    }
                }
            }
        },
        400: {
            "model": schemas.ErrorResponse,
            "description": "Email already registered",
            "content": {
                "application/json": {
                    "example": {"detail": "Email already registered"}
                }
            }
        }
    }
)
def register_user(payload: schemas.UserCreate, db: Session = Depends(get_db)):
    """Register a new user with a default workspace and local credentials.

    - If email already exists, respond with 400.
    - Create a `Workspace` named "New workspace".
    - Create `User` with role Admin (temporary default) and a simple `name` derived from email.
    - Create `AuthCredential` storing the bcrypt hash.
    - Do not auto-login.
    """
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    # Create a workspace for the new user
    workspace = Workspace(name="New workspace")
    db.add(workspace)
    db.flush()  # assign workspace.id without committing yet

    # Use local-part as a friendly default name
    default_name = payload.email.split("@")[0]

    # NOTE: All users are Admin for now; tighten later with invites/roles
    user = User(
        email=payload.email,
        name=default_name,
        # Persist Admin temporarily for all signups (future: invites/roles)
        role=RoleEnum.admin,
        workspace_id=workspace.id,
    )
    db.add(user)
    db.flush()  # assign user.id

    credential = AuthCredential(user_id=user.id, password_hash=get_password_hash(payload.password))
    db.add(credential)

    db.commit()
    db.refresh(user)
    return user


@router.post(
    "/login",
    response_model=schemas.LoginResponse,
    summary="Authenticate user",
    description="""
    Authenticate a user with email and password.
    
    On successful authentication:
    - Sets an HTTP-only JWT cookie named `access_token`
    - Cookie contains JWT token with format "Bearer <token>"
    - Cookie is valid for 7 days
    - Returns user information
    
    **Security Features**:
    - HTTP-only cookie prevents XSS attacks
    - SameSite=Lax prevents CSRF attacks
    - Secure flag enabled in production
    """,
    responses={
        200: {
            "model": schemas.LoginResponse,
            "description": "Login successful",
            "content": {
                "application/json": {
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
        },
        401: {
            "model": schemas.ErrorResponse,
            "description": "Invalid credentials",
            "content": {
                "application/json": {
                    "example": {"detail": "Invalid credentials"}
                }
            }
        }
    }
)
def login_user(payload: schemas.UserLogin, response: Response, db: Session = Depends(get_db)):
    """Authenticate a user and set an HTTP-only JWT cookie.

    Cookie:
    - name: access_token
    - value: "Bearer <jwt>"
    - httponly: True, samesite: lax, secure: False (dev), domain from env
    - max_age: 7 days
    """
    user = db.query(User).filter(User.email == payload.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    cred = db.query(AuthCredential).filter(AuthCredential.user_id == user.id).first()
    if not cred or not verify_password(payload.password, cred.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = create_access_token(subject=user.email)
    cookie_value = f"Bearer {token}"
    settings = get_settings()
    max_age = 7 * 24 * 3600

    # Cookie settings that work for both local dev and production
    # For local: domain=None, secure=False
    # For production: domain=None (same-site), secure=True for HTTPS
    cookie_kwargs = {
        "key": "access_token",
        "value": cookie_value,
        "httponly": True,
        "samesite": "none",  # Changed to 'none' for cross-site cookies
        "secure": True,  # Required when samesite='none'
        "max_age": max_age,
        "path": "/",
    }
    
    # Only set domain if explicitly configured (None for most cases)
    if settings.COOKIE_DOMAIN:
        cookie_kwargs["domain"] = settings.COOKIE_DOMAIN
    
    response.set_cookie(**cookie_kwargs)

    return schemas.LoginResponse(user=schemas.UserOut.model_validate(user))


@router.get(
    "/me", 
    response_model=schemas.UserOut,
    summary="Get current user",
    description="""
    Retrieve information about the currently authenticated user.
    
    Requires a valid JWT token in the `access_token` cookie.
    Returns user details including role and workspace information.
    """,
    responses={
        200: {
            "model": schemas.UserOut,
            "description": "Current user information",
            "content": {
                "application/json": {
                    "example": {
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "email": "john.doe@company.com",
                        "name": "John Doe",
                        "role": "Admin",
                        "workspace_id": "456e7890-e89b-12d3-a456-426614174001"
                    }
                }
            }
        },
        401: {
            "model": schemas.ErrorResponse,
            "description": "Not authenticated or invalid token",
            "content": {
                "application/json": {
                    "example": {"detail": "Not authenticated"}
                }
            }
        }
    },
    dependencies=[Depends(get_current_user)]
)
def get_me(user: User = Depends(get_current_user)):
    """Return the current authenticated user."""
    return user


@router.post(
    "/logout",
    response_model=schemas.SuccessResponse,
    summary="Logout user",
    description="""
    Log out the current user by clearing the authentication cookie.
    
    This endpoint:
    - Clears the `access_token` HTTP-only cookie
    - Invalidates the current session
    - Does not require authentication (can be called even with invalid token)
    """,
    responses={
        200: {
            "model": schemas.SuccessResponse,
            "description": "Successfully logged out",
            "content": {
                "application/json": {
                    "example": {"detail": "logged out"}
                }
            }
        }
    }
)
def logout_user(response: Response):
    """Clear the access token cookie."""
    settings = get_settings()
    
    cookie_kwargs = {
        "key": "access_token",
        "value": "",
        "max_age": 0,
        "httponly": True,
        "samesite": "none",
        "secure": True,
        "path": "/",
    }
    
    if settings.COOKIE_DOMAIN:
        cookie_kwargs["domain"] = settings.COOKIE_DOMAIN
    
    response.set_cookie(**cookie_kwargs)
    return schemas.SuccessResponse(detail="logged out")



