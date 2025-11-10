"""Google Ads OAuth 2.0 flow endpoints.

WHAT:
    Implements OAuth authorization flow for user-initiated Google Ads connections.
    
WHY:
    Allows users to connect their own Google Ads accounts without manual token setup.
    
REFERENCES:
    - docs/living-docs/GOOGLE_INTEGRATION_STATUS.MD (Phase 7)
    - https://developers.google.com/google-ads/api/docs/oauth/overview
"""

import os
import logging
from typing import Optional
from urllib.parse import urlencode
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import httpx

from app.database import get_db
from app.deps import get_current_user
from app.models import User, Connection, ProviderEnum
from app.services.token_service import store_connection_token

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth/google", tags=["Google OAuth"])

# OAuth configuration from environment
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI", "http://localhost:8000/auth/google/callback")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")

GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_SCOPES = ["https://www.googleapis.com/auth/adwords"]


@router.get("/authorize")
async def google_authorize(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Redirect user to Google OAuth consent screen.
    
    WHAT:
        Builds authorization URL with required parameters and redirects user.
    WHY:
        Initiates OAuth flow for connecting Google Ads account.
    """
    if not GOOGLE_CLIENT_ID or not GOOGLE_CLIENT_SECRET:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Google OAuth not configured. Missing CLIENT_ID or CLIENT_SECRET."
        )
    
    # Build authorization URL
    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "response_type": "code",
        "scope": " ".join(GOOGLE_SCOPES),
        "access_type": "offline",  # Request refresh token
        "prompt": "consent",  # Force consent screen to ensure refresh token
        "state": str(current_user.workspace_id),  # Pass workspace ID for callback
    }
    
    auth_url = f"{GOOGLE_AUTH_URL}?{urlencode(params)}"
    logger.info(f"[GOOGLE_OAUTH] Redirecting user {current_user.id} to Google consent screen")
    
    return RedirectResponse(url=auth_url)


@router.get("/callback")
async def google_callback(
    code: Optional[str] = Query(None),
    error: Optional[str] = Query(None),
    state: Optional[str] = Query(None),  # workspace_id
    db: Session = Depends(get_db)
):
    """
    Handle OAuth callback from Google.
    
    WHAT:
        Exchanges authorization code for access/refresh tokens.
        Fetches customer IDs and creates connection.
    WHY:
        Completes OAuth flow and stores encrypted tokens.
    """
    # Validate configuration
    if not GOOGLE_CLIENT_ID or not GOOGLE_CLIENT_SECRET:
        logger.error("[GOOGLE_OAUTH] OAuth not configured - missing credentials")
        return RedirectResponse(
            url=f"{FRONTEND_URL}/settings?google_oauth=error&message=oauth_not_configured"
        )
    
    # Handle errors from Google
    if error:
        logger.error(f"[GOOGLE_OAUTH] OAuth error: {error}")
        return RedirectResponse(
            url=f"{FRONTEND_URL}/settings?google_oauth=error&message={error}"
        )
    
    if not code:
        logger.error("[GOOGLE_OAUTH] Missing authorization code")
        return RedirectResponse(
            url=f"{FRONTEND_URL}/settings?google_oauth=error&message=missing_code"
        )
    
    # Validate state parameter (workspace_id)
    if not state:
        logger.error("[GOOGLE_OAUTH] Missing state parameter")
        return RedirectResponse(
            url=f"{FRONTEND_URL}/settings?google_oauth=error&message=missing_state"
        )
    
    # Verify workspace exists
    from app.models import Workspace
    workspace = db.query(Workspace).filter(Workspace.id == state).first()
    if not workspace:
        logger.error(f"[GOOGLE_OAUTH] Invalid workspace ID: {state}")
        return RedirectResponse(
            url=f"{FRONTEND_URL}/settings?google_oauth=error&message=invalid_workspace"
        )
    
    # Exchange code for tokens
    try:
        async with httpx.AsyncClient() as client:
            token_response = await client.post(
                GOOGLE_TOKEN_URL,
                data={
                    "code": code,
                    "client_id": GOOGLE_CLIENT_ID,
                    "client_secret": GOOGLE_CLIENT_SECRET,
                    "redirect_uri": GOOGLE_REDIRECT_URI,
                    "grant_type": "authorization_code",
                }
            )
            token_response.raise_for_status()
            token_data = token_response.json()
    except Exception as e:
        logger.exception("[GOOGLE_OAUTH] Failed to exchange code for tokens")
        return RedirectResponse(
            url=f"{FRONTEND_URL}/settings?google_oauth=error&message=token_exchange_failed"
        )
    
    access_token = token_data.get("access_token")
    refresh_token = token_data.get("refresh_token")
    expires_in = token_data.get("expires_in")  # seconds
    
    if not access_token or not refresh_token:
        logger.error("[GOOGLE_OAUTH] Missing tokens in response")
        return RedirectResponse(
            url=f"{FRONTEND_URL}/settings?google_oauth=error&message=missing_tokens"
        )
    
    # Fetch accessible customer IDs using the new access token
    try:
        # Validate developer token is configured
        developer_token = os.getenv("GOOGLE_DEVELOPER_TOKEN")
        if not developer_token:
            logger.error("[GOOGLE_OAUTH] GOOGLE_DEVELOPER_TOKEN not configured")
            return RedirectResponse(
                url=f"{FRONTEND_URL}/settings?google_oauth=error&message=developer_token_missing"
            )
        
        # Build temporary client with OAuth tokens
        from google.ads.googleads.client import GoogleAdsClient as _SdkClient
        
        oauth_config = {
            "developer_token": developer_token,
            "client_id": GOOGLE_CLIENT_ID,
            "client_secret": GOOGLE_CLIENT_SECRET,
            "refresh_token": refresh_token,
            "use_proto_plus": True,
        }
        
        temp_client = _SdkClient.load_from_dict(oauth_config)
        customer_service = temp_client.get_service("CustomerService")
        
        # List accessible customers
        accessible_customers = customer_service.list_accessible_customers()
        customer_ids = accessible_customers.resource_names
        
        if not customer_ids:
            logger.error("[GOOGLE_OAUTH] No accessible customers found")
            return RedirectResponse(
                url=f"{FRONTEND_URL}/settings?google_oauth=error&message=no_customers"
            )
        
        # Extract first customer ID (format: "customers/1234567890")
        first_customer_id = customer_ids[0].split("/")[-1]
        logger.info(f"[GOOGLE_OAUTH] Found customer ID: {first_customer_id}")
        
        # Fetch customer details
        query = f"""
            SELECT
                customer.id,
                customer.descriptive_name,
                customer.currency_code,
                customer.time_zone
            FROM customer
            WHERE customer.id = {first_customer_id}
        """
        
        ga_service = temp_client.get_service("GoogleAdsService")
        response = ga_service.search(customer_id=first_customer_id, query=query)
        
        customer_data = None
        for row in response:
            customer_data = {
                "id": str(row.customer.id),
                "name": row.customer.descriptive_name or f"Google Ads {row.customer.id}",
                "currency": row.customer.currency_code,
                "timezone": row.customer.time_zone,
            }
            break
        
        if not customer_data:
            raise Exception("Could not fetch customer details")
        
        logger.info(f"[GOOGLE_OAUTH] Fetched customer data: {customer_data['name']} ({customer_data['id']})")
        
    except ImportError as e:
        logger.exception("[GOOGLE_OAUTH] Google Ads SDK not installed")
        return RedirectResponse(
            url=f"{FRONTEND_URL}/settings?google_oauth=error&message=sdk_not_installed"
        )
    except Exception as e:
        logger.exception(f"[GOOGLE_OAUTH] Failed to fetch customer details: {str(e)}")
        return RedirectResponse(
            url=f"{FRONTEND_URL}/settings?google_oauth=error&message=customer_fetch_failed"
        )
    
    # Create or update connection
    workspace_id = state  # Already validated above
    
    try:
        connection = db.query(Connection).filter(
            Connection.workspace_id == workspace_id,
            Connection.provider == ProviderEnum.google,
            Connection.external_account_id == customer_data["id"],
        ).first()
        
        if not connection:
            connection = Connection(
                provider=ProviderEnum.google,
                external_account_id=customer_data["id"],
                name=customer_data["name"],
                status="active",
                timezone=customer_data["timezone"],
                currency_code=customer_data["currency"],
                workspace_id=workspace_id,
                connected_at=datetime.utcnow(),
            )
            db.add(connection)
            db.flush()
            logger.info(f"[GOOGLE_OAUTH] Created new connection for customer {customer_data['id']}")
        else:
            logger.info(f"[GOOGLE_OAUTH] Updating existing connection for customer {customer_data['id']}")
            # Update connection metadata
            connection.name = customer_data["name"]
            connection.timezone = customer_data["timezone"]
            connection.currency_code = customer_data["currency"]
            connection.status = "active"
        
        # Store encrypted tokens
        expires_at = datetime.utcnow() + timedelta(seconds=expires_in) if expires_in else None
        
        store_connection_token(
            db,
            connection,
            access_token=access_token,
            refresh_token=refresh_token,
            expires_at=expires_at,
            scope=" ".join(GOOGLE_SCOPES),
            ad_account_ids=[customer_data["id"]],
        )
        
        db.commit()
        
        logger.info(f"[GOOGLE_OAUTH] Successfully connected Google Ads account {customer_data['id']} to workspace {workspace_id}")
        
        return RedirectResponse(
            url=f"{FRONTEND_URL}/settings?google_oauth=success&connection_id={connection.id}"
        )
        
    except Exception as e:
        db.rollback()
        logger.exception(f"[GOOGLE_OAUTH] Failed to create/update connection: {str(e)}")
        return RedirectResponse(
            url=f"{FRONTEND_URL}/settings?google_oauth=error&message=connection_save_failed"
        )

