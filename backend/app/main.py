"""FastAPI application entrypoint.

Configures CORS, includes routers, and exposes a healthcheck endpoint.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from sqladmin import Admin, ModelView
from starlette.middleware.sessions import SessionMiddleware
import os

from .authentication import SimpleAuth
from .database import engine
from .deps import get_settings
from .routers import auth as auth_router
from .routers import workspaces as workspaces_router
from .routers import connections as connections_router
from .routers import entities as entities_router
from .routers import metrics as metrics_router
from .routers import pnl as pnl_router
from .routers import kpis as kpis_router
from .routers import qa as qa_router
from . import schemas

# Import models so Alembic can discover metadata
from . import models  # noqa: F401


# SQLAdmin ModelView classes for each model
# WHEN MAKING CHANGES TO THESE CLASSES, MAKE SURE TO UPDATE THE __str__ METHODS IN THE MODELS.PY FILE
# This is used to display the models in the admin interface.

class WorkspaceAdmin(ModelView, model=models.Workspace):
    column_list = [models.Workspace.id, models.Workspace.name, models.Workspace.created_at]
    form_columns = ["name"]
    column_searchable_list = ["name"]
    column_sortable_list = ["name", "created_at"]
    name = "Workspace"
    name_plural = "Workspaces"
    icon = "fa-solid fa-building"


class UserAdmin(ModelView, model=models.User):
    """Admin view for User model.
    
    When creating/editing users, workspace shows as a dropdown
    listing all available workspaces.
    """
    column_list = [models.User.id, models.User.email, models.User.name, models.User.role, models.User.workspace]
    # Use "workspace" instead of "workspace_id" for proper dropdown
    form_columns = ["email", "name", "role", "workspace"]
    column_searchable_list = ["email", "name"]
    column_sortable_list = ["email", "name", "role"]
    # form_ajax_refs enables searchable dropdowns for foreign keys
    form_ajax_refs = {
        "workspace": {
            "fields": ["name"],  # Search workspaces by name
            "order_by": "name",
        }
    }
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"


class ConnectionAdmin(ModelView, model=models.Connection):
    """Admin view for Connection model.
    
    When creating a connection, you MUST select which workspace it belongs to.
    This ensures data isolation between different companies.
    """
    column_list = [models.Connection.id, models.Connection.provider, models.Connection.name, models.Connection.workspace, models.Connection.status, models.Connection.connected_at]
    # Use relationship names for proper dropdowns
    form_columns = ["provider", "external_account_id", "name", "status", "workspace", "token"]
    column_searchable_list = ["name", "external_account_id"]
    column_sortable_list = ["provider", "name", "connected_at", "status"]
    form_ajax_refs = {
        "workspace": {
            "fields": ["name"],
            "order_by": "name",
        },
        "token": {
            "fields": ["provider", "scope"],
            "order_by": "expires_at",
        }
    }
    name = "Connection"
    name_plural = "Connections"
    icon = "fa-solid fa-plug"


class TokenAdmin(ModelView, model=models.Token):
    column_list = [models.Token.id, models.Token.provider, models.Token.expires_at, models.Token.scope]
    form_columns = ["provider", "access_token_enc", "refresh_token_enc", "expires_at", "scope"]
    column_sortable_list = ["provider", "expires_at"]
    name = "Token"
    name_plural = "Tokens"
    icon = "fa-solid fa-key"


class FetchAdmin(ModelView, model=models.Fetch):
    """Admin view for Fetch operations.
    
    Each fetch belongs to a connection (required).
    """
    column_list = [models.Fetch.id, models.Fetch.kind, models.Fetch.status, models.Fetch.connection, models.Fetch.started_at, models.Fetch.finished_at]
    # Use "connection" instead of "connection_id"
    form_columns = ["kind", "status", "started_at", "finished_at", "range_start", "range_end", "connection"]
    column_searchable_list = ["kind", "status"]
    column_sortable_list = ["status", "started_at", "finished_at"]
    form_ajax_refs = {
        "connection": {
            "fields": ["name", "provider"],
            "order_by": "name",
        }
    }
    name = "Fetch"
    name_plural = "Fetches"
    icon = "fa-solid fa-download"


class ImportAdmin(ModelView, model=models.Import):
    """Admin view for Import records.
    
    Each import is linked to a fetch operation.
    """
    column_list = [models.Import.id, models.Import.as_of, models.Import.created_at, models.Import.note, models.Import.fetch]
    # Use "fetch" instead of "fetch_id"
    form_columns = ["as_of", "note", "fetch"]
    column_searchable_list = ["note"]
    column_sortable_list = ["as_of", "created_at"]
    form_ajax_refs = {
        "fetch": {
            "fields": ["kind", "status"],
            "order_by": "started_at",
        }
    }
    name = "Import"
    name_plural = "Imports"
    icon = "fa-solid fa-file-import"


class EntityAdmin(ModelView, model=models.Entity):
    """Admin view for Entity (campaigns, ad sets, ads, etc).
    
    Entities belong to:
    - A workspace (required)
    - A connection (optional - which ad platform)
    - A parent entity (optional - for hierarchy)
    """
    column_list = [models.Entity.id, models.Entity.level, models.Entity.external_id, models.Entity.name, models.Entity.status, models.Entity.workspace, models.Entity.connection]
    # Use relationship names for dropdowns
    form_columns = ["level", "external_id", "name", "status", "parent", "workspace", "connection"]
    column_searchable_list = ["external_id", "name"]
    column_sortable_list = ["level", "name", "status"]
    form_ajax_refs = {
        "workspace": {
            "fields": ["name"],
            "order_by": "name",
        },
        "connection": {
            "fields": ["name", "provider"],
            "order_by": "name",
        },
        "parent": {  # For selecting parent entity
            "fields": ["name", "level"],
            "order_by": "name",
        }
    }
    name = "Entity"
    name_plural = "Entities"
    icon = "fa-solid fa-sitemap"


class MetricFactAdmin(ModelView, model=models.MetricFact):
    """Admin view for Metric Facts (actual ad performance data)."""
    column_list = [models.MetricFact.id, models.MetricFact.entity, models.MetricFact.import_, models.MetricFact.provider, models.MetricFact.level, models.MetricFact.event_date, models.MetricFact.spend, models.MetricFact.revenue]
    # Use relationship names
    form_columns = ["entity", "provider", "level", "event_at", "event_date", "spend", "impressions", "clicks", "conversions", "revenue", "currency", "natural_key", "import_"]
    column_sortable_list = ["event_date", "spend", "clicks", "conversions"]
    form_ajax_refs = {
        "entity": {
            "fields": ["name", "level"],
            "order_by": "name",
        },
        "import_": {
            "fields": ["as_of", "note"],
            "order_by": "as_of",
        }
    }
    name = "Metric Fact"
    name_plural = "Metric Facts"
    icon = "fa-solid fa-chart-line"


class ComputeRunAdmin(ModelView, model=models.ComputeRun):
    """Admin view for Compute Runs."""
    column_list = [models.ComputeRun.id, models.ComputeRun.as_of, models.ComputeRun.reason, models.ComputeRun.status, models.ComputeRun.type, models.ComputeRun.workspace]
    # Use "workspace" relationship
    form_columns = ["as_of", "reason", "status", "type", "workspace"]
    column_searchable_list = ["reason", "status"]
    column_sortable_list = ["as_of", "computed_at", "status", "type"]
    form_ajax_refs = {
        "workspace": {
            "fields": ["name"],
            "order_by": "name",
        }
    }
    name = "Compute Run"
    name_plural = "Compute Runs"
    icon = "fa-solid fa-gears"


class PnlAdmin(ModelView, model=models.Pnl):
    """Admin view for P&L records."""
    column_list = [models.Pnl.id, models.Pnl.entity, models.Pnl.compute_run, models.Pnl.provider, models.Pnl.level, models.Pnl.kind, models.Pnl.event_date, models.Pnl.spend, models.Pnl.revenue, models.Pnl.roas]
    # Use relationships: "entity" and "compute_run" instead of IDs
    form_columns = ["entity", "compute_run", "provider", "level", "kind", "as_of", "event_date", "spend", "revenue", "conversions", "clicks", "impressions", "cpa", "roas"]
    column_sortable_list = ["event_date", "spend", "revenue", "roas"]
    form_ajax_refs = {
        "entity": {
            "fields": ["name", "level"],
            "order_by": "name",
        },
        "compute_run": {
            "fields": ["type", "as_of", "status"],
            "order_by": "as_of",
        }
    }
    name = "P&L"
    name_plural = "P&L Records"
    icon = "fa-solid fa-dollar-sign"


class QaQueryLogAdmin(ModelView, model=models.QaQueryLog):
    """Admin view for Query Log.
    
    When creating a query log:
    1. Select workspace - which workspace context
    2. Select user - who made the query
    
    Both are shown as searchable dropdowns.
    """
    column_list = [models.QaQueryLog.id, models.QaQueryLog.workspace, models.QaQueryLog.user, models.QaQueryLog.question_text, models.QaQueryLog.created_at]
    # Use "workspace" and "user" instead of "workspace_id" and "user_id" for proper dropdown rendering
    form_columns = ["workspace", "user", "question_text", "dsl_json", "duration_ms"]
    column_searchable_list = ["question_text"]
    column_sortable_list = ["created_at"]
    # Make foreign key fields required in forms
    form_args = {
        "workspace": {"validators": []},  # SQLAdmin will add required validator
        "user": {"validators": []},
    }
    form_ajax_refs = {
        "workspace": {
            "fields": ["name"],
            "order_by": "name",
        },
        "user": {
            "fields": ["name", "email"],  # Search by name or email
            "order_by": "name",
        }
    }
    name = "Query Log"
    name_plural = "Query Logs"
    icon = "fa-solid fa-magnifying-glass"


class AuthCredentialAdmin(ModelView, model=models.AuthCredential):
    """Admin view for Auth Credentials.
    
    Note: user_id is the primary key here, so we keep it as user_id.
    """
    column_list = [models.AuthCredential.user, models.AuthCredential.created_at]
    form_columns = ["user_id", "password_hash"]
    column_sortable_list = ["created_at"]
    # Special note: password_hash should be handled carefully in production
    form_args = {
        "password_hash": {"description": "Bcrypt hash of the password"}
    }
    name = "Auth Credential"
    name_plural = "Auth Credentials"
    icon = "fa-solid fa-lock"


def create_app() -> FastAPI:
    app = FastAPI(
        title="AdNavi API",
        description="""
        AdNavi is a comprehensive advertising analytics and optimization platform.
        
        This API provides endpoints for:
        - User authentication and workspace management
        - Ad platform connections (Google Ads, Meta, TikTok)
        - Campaign, ad set, and ad entity management
        - Performance metrics and analytics
        - P&L calculations and financial reporting
        - AI-powered query analytics
        
        ## Authentication
        
        The API uses JWT-based authentication with HTTP-only cookies for security.
        All authenticated endpoints require a valid JWT token obtained through the login endpoint.
        
        ## Data Model
        
        - **Workspaces**: Top-level containers for companies/organizations
        - **Users**: Individuals with access to workspaces (Owner, Admin, Viewer roles)
        - **Connections**: Links to advertising platform accounts
        - **Entities**: Hierarchical campaign structure (Account > Campaign > Ad Set > Ad)
        - **Metrics**: Performance data and analytics
        - **P&L**: Profit and loss calculations
        """,
        version="1.0.0",
        contact={
            "name": "AdNavi Support",
            "email": "support@adnavi.com",
        },
        license_info={
            "name": "Proprietary",
        },
        servers=[
            {
                "url": "http://localhost:8000",
                "description": "Development server"
            },
            {
                "url": "https://api.adnavi.com",
                "description": "Production server"
            }
        ]
    )

    settings = get_settings()
    
    # Add session middleware for admin panel authentication
    # This MUST be added before other middleware
    if settings.ADMIN_SECRET_KEY == "supersecretkey-change-this-in-production":
        print("WARNING: Using default admin secret key. Set ADMIN_SECRET_KEY environment variable for production.")
    
    app.add_middleware(
        SessionMiddleware,
        secret_key=settings.ADMIN_SECRET_KEY
    )
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include all API routers
    app.include_router(auth_router.router)
    app.include_router(workspaces_router.router)
    app.include_router(connections_router.router)
    app.include_router(entities_router.router)
    app.include_router(metrics_router.router)
    app.include_router(pnl_router.router)
    app.include_router(kpis_router.router)
    app.include_router(qa_router.router)

    @app.get(
        "/health",
        response_model=schemas.HealthResponse,
        tags=["Health"],
        summary="Health check",
        description="""
        Simple health check endpoint to verify the API is running.
        
        This endpoint:
        - Does not require authentication
        - Returns basic service status
        - Can be used for load balancer health checks
        - Indicates the API is responsive
        """
    )
    def health():
        return schemas.HealthResponse(status="ok")

    # Initialize authentication backend for admin panel
    authentication_backend = SimpleAuth(secret_key=settings.ADMIN_SECRET_KEY)
    
    # Initialize SQLAdmin with authentication
    admin = Admin(
        app, 
        engine, 
        title="AdNavi Admin",
        authentication_backend=authentication_backend
    )
    
    # Register all model views
    admin.add_view(WorkspaceAdmin)
    admin.add_view(UserAdmin)
    admin.add_view(ConnectionAdmin)
    admin.add_view(TokenAdmin)
    admin.add_view(FetchAdmin)
    admin.add_view(ImportAdmin)
    admin.add_view(EntityAdmin)
    admin.add_view(MetricFactAdmin)
    admin.add_view(ComputeRunAdmin)
    admin.add_view(PnlAdmin)
    admin.add_view(QaQueryLogAdmin)
    admin.add_view(AuthCredentialAdmin)

    # Custom OpenAPI schema with security definitions
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        
        openapi_schema = get_openapi(
            title=app.title,
            version=app.version,
            description=app.description,
            routes=app.routes,
            servers=app.servers
        )
        
        # Add security schemes
        openapi_schema["components"]["securitySchemes"] = {
            "cookieAuth": {
                "type": "apiKey",
                "in": "cookie",
                "name": "access_token",
                "description": "JWT token stored in HTTP-only cookie. Format: 'Bearer <token>'"
            }
        }
        
        # Add security requirement to protected endpoints
        public_endpoints = ["/health", "/auth/register", "/auth/login"]
        
        for path in openapi_schema["paths"]:
            for method in openapi_schema["paths"][path]:
                # Skip adding security to public endpoints
                if path in public_endpoints:
                    continue
                
                # Add security requirement for all other endpoints
                if "security" not in openapi_schema["paths"][path][method]:
                    openapi_schema["paths"][path][method]["security"] = [
                        {"cookieAuth": []}
                    ]
        
        app.openapi_schema = openapi_schema
        return app.openapi_schema
    
    app.openapi = custom_openapi
    return app


app = create_app()



