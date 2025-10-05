"""SQLAlchemy ORM models and enums.

This module defines the domain schema using UUID primary keys and explicit
relationships. Authentication secrets are stored in a separate
`auth_credentials` table to keep the domain `users` table clean.
"""

import uuid
from datetime import datetime
import enum

from sqlalchemy import Column, String, DateTime, Enum, Integer, ForeignKey, Numeric, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base


# Single Base used by the entire application
Base = declarative_base()


# Enums ---------------------------------------------------------

class RoleEnum(str, enum.Enum):
    owner = "Owner"
    admin = "Admin"
    viewer = "Viewer"


class ProviderEnum(str, enum.Enum):
    google = "google"
    meta = "meta"
    tiktok = "tiktok"
    other = "other"


class LevelEnum(str, enum.Enum):
    account = "account"
    campaign = "campaign"
    adset = "adset"
    ad = "ad"
    creative = "creative"
    unknown = "unknown"


class KindEnum(str, enum.Enum):
    snapshot = "snapshot"
    eod = "eod"


class ComputeRunTypeEnum(str, enum.Enum):
    snapshot = "snapshot"
    eod = "eod"
    backfill = "backfill"


class GoalEnum(str, enum.Enum):
    """Campaign/entity objective type.
    
    Used to determine which derived metrics are most relevant:
    - awareness: Focus on CPM, impressions, reach
    - traffic: Focus on CPC, CTR, clicks
    - leads: Focus on CPL, lead volume
    - app_installs: Focus on CPI, install volume
    - purchases: Focus on CPP, AOV, purchase volume
    - conversions: Focus on CPA, CVR, ROAS (generic conversions)
    - other: No specific objective
    """
    awareness = "awareness"
    traffic = "traffic"
    leads = "leads"
    app_installs = "app_installs"
    purchases = "purchases"
    conversions = "conversions"
    other = "other"


# Core models ----------------------------------------------------

class Workspace(Base):
    """Workspace represents a company/organization account.
    
    A workspace is the top-level container that groups all resources
    for a specific company. All data (connections, entities, metrics)
    belongs to a workspace.
    
    Current relationship: One workspace can have many users (ONE-to-MANY)
    TODO: Should be MANY-to-MANY (users can belong to multiple workspaces)
    """
    __tablename__ = "workspaces"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships - these create reverse lookups
    users = relationship("User", back_populates="workspace")  # All users in this workspace
    connections = relationship("Connection", back_populates="workspace")  # All ad platform connections
    entities = relationship("Entity", back_populates="workspace")  # All entities (campaigns, ads, etc)
    compute_runs = relationship("ComputeRun", back_populates="workspace")  # All compute runs
    queries = relationship("QaQueryLog", back_populates="workspace")  # All queries made in workspace
    
    # This is used to display the model in the admin interface.
    def __str__(self):
        return self.name


class User(Base):
    """User represents a person who can access the system.
    
    Users authenticate via email/password and belong to workspaces.
    Each user has a role (Owner, Admin, Viewer) within their workspace.
    
    CURRENT ISSUE: User can only belong to ONE workspace (via workspace_id)
    This should be changed to MANY-to-MANY relationship.
    """
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    role = Column(Enum(RoleEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)

    # Foreign key - links this user to ONE workspace
    # When creating a user in admin, you must select which workspace they belong to
    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.id"), nullable=False)
    workspace = relationship("Workspace", back_populates="users")

    # 1:1 credential for local password-based auth
    credential = relationship("AuthCredential", back_populates="user", uselist=False)

    # All queries made by this user
    queries = relationship("QaQueryLog", back_populates="user")
    
    # This is used to display the model in the admin interface.
    def __str__(self):
        return f"{self.name} ({self.email})"


class Connection(Base):
    """Connection represents a link to an advertising platform account.
    
    Each connection belongs to ONE workspace. When you create a connection
    in the admin panel, you MUST select which workspace it belongs to.
    
    Examples: Google Ads account, Facebook Ads account, TikTok Ads account
    """
    __tablename__ = "connections"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    provider = Column(Enum(ProviderEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    external_account_id = Column(String, nullable=False)  # The account ID in the external platform
    name = Column(String, nullable=False)  # Friendly name for this connection
    status = Column(String, nullable=False)  # active, paused, disconnected, etc.
    connected_at = Column(DateTime, default=datetime.utcnow)

    # Foreign key - EVERY connection belongs to exactly ONE workspace
    # This ensures data isolation between different companies
    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.id"), nullable=False)
    workspace = relationship("Workspace", back_populates="connections")

    # Optional link to authentication token
    token_id = Column(UUID(as_uuid=True), ForeignKey("tokens.id"))
    token = relationship("Token", back_populates="connections")

    # Reverse relationships
    entities = relationship("Entity", back_populates="connection")  # All campaigns/ads from this connection
    fetches = relationship("Fetch", back_populates="connection")  # All data fetch operations
    
    def __str__(self):
        return f"{self.name} ({self.provider.value})"


class Token(Base):
    __tablename__ = "tokens"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    provider = Column(Enum(ProviderEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    access_token_enc = Column(String, nullable=False)
    refresh_token_enc = Column(String, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    scope = Column(String, nullable=True)

    connections = relationship("Connection", back_populates="token")
    
    def __str__(self):
        return f"{self.provider.value} token (expires: {self.expires_at.strftime('%Y-%m-%d %H:%M')})"


class Fetch(Base):
    __tablename__ = "fetches"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    kind = Column(String, nullable=False)
    status = Column(String, nullable=False)
    started_at = Column(DateTime, default=datetime.utcnow)
    finished_at = Column(DateTime, nullable=True)
    range_start = Column(DateTime, nullable=True)
    range_end = Column(DateTime, nullable=True)

    connection_id = Column(UUID(as_uuid=True), ForeignKey("connections.id"), nullable=False)
    connection = relationship("Connection", back_populates="fetches")

    imports = relationship("Import", back_populates="fetch")
    
    def __str__(self):
        return f"{self.kind} ({self.status}) - {self.started_at.strftime('%Y-%m-%d %H:%M')}"


class Import(Base):
    __tablename__ = "imports"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    as_of = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    note = Column(String, nullable=True)

    fetch_id = Column(UUID(as_uuid=True), ForeignKey("fetches.id"), nullable=False)
    fetch = relationship("Fetch", back_populates="imports")

    facts = relationship("MetricFact", back_populates="import_")
    
    def __str__(self):
        return f"Import as of {self.as_of.strftime('%Y-%m-%d')}{' - ' + self.note if self.note else ''}"


class Entity(Base):
    """Entity represents a marketing entity (campaign, ad set, ad, etc.).
    
    Derived Metrics v1 addition:
    - goal: Campaign objective (awareness, traffic, leads, app_installs, purchases, conversions, other)
    
    WHY goal matters:
    - Helps determine which metrics are most relevant to the user
    - CPL makes sense for leads campaigns, CPI for app_installs, CPP for purchases
    - QA system can recommend metrics based on goal
    - Seed data generates appropriate base measures based on goal
    """
    __tablename__ = "entities"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    level = Column(Enum(LevelEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    external_id = Column(String, nullable=False)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    parent_id = Column(UUID(as_uuid=True), ForeignKey("entities.id"), nullable=True)
    
    # Derived Metrics v1: Campaign objective
    goal = Column(Enum(GoalEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=True)

    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.id"), nullable=False)
    workspace = relationship("Workspace", back_populates="entities")

    connection_id = Column(UUID(as_uuid=True), ForeignKey("connections.id"), nullable=True)
    connection = relationship("Connection", back_populates="entities")

    children = relationship("Entity", backref="parent", remote_side=[id])
    facts = relationship("MetricFact", back_populates="entity")
    pnls = relationship("Pnl", back_populates="entity")
    
    def __str__(self):
        return f"{self.name} ({self.level.value})"


class MetricFact(Base):
    """MetricFact stores RAW BASE MEASURES from ad platforms.
    
    Derived Metrics v1 philosophy:
    - Store ONLY base measures (raw facts from platforms)
    - Compute derived metrics on-demand (executor) or during snapshots (Pnl)
    - Never store computed values here → avoids formula drift over time
    
    Base measures (original):
    - spend, impressions, clicks, conversions, revenue
    
    Base measures (added in Derived Metrics v1):
    - leads: Lead form submissions (Meta Lead Ads, Google Lead Form Extensions)
    - installs: App installations (App Install campaigns)
    - purchases: Purchase events (Conversions API, pixel tracking)
    - visitors: Landing page visitors (from analytics platforms)
    - profit: Net profit (revenue - COGS/costs)
    
    WHY these additions:
    - Enables computing CPL, CPI, CPP, ARPV, POAS, AOV
    - Maintains fact table as wide "base" table (no joins needed)
    - Platform APIs provide these metrics → we store them raw
    
    Related:
    - app/metrics/registry.py: Lists all base measures
    - app/dsl/executor.py: Aggregates these for ad-hoc queries
    - app/services/compute_service.py: Aggregates these for Pnl snapshots
    """
    __tablename__ = "metric_facts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    entity_id = Column(UUID(as_uuid=True), ForeignKey("entities.id"), nullable=True)
    provider = Column(Enum(ProviderEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    level = Column(Enum(LevelEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    event_at = Column(DateTime, nullable=False)
    event_date = Column(DateTime, nullable=False)
    
    # Original base measures
    spend = Column(Numeric(18, 4), nullable=False)
    impressions = Column(Integer, nullable=False)
    clicks = Column(Integer, nullable=False)
    conversions = Column(Numeric(18, 4), nullable=True)
    revenue = Column(Numeric(18, 4), nullable=True)
    
    # Derived Metrics v1: New base measures
    leads = Column(Numeric(18, 4), nullable=True)  # Lead form submissions
    installs = Column(Integer, nullable=True)  # App installs
    purchases = Column(Integer, nullable=True)  # Purchase events
    visitors = Column(Integer, nullable=True)  # Landing page visitors
    profit = Column(Numeric(18, 4), nullable=True)  # Net profit (revenue - costs)
    
    currency = Column(String, nullable=False)
    natural_key = Column(String, nullable=False)
    ingested_at = Column(DateTime, default=datetime.utcnow)

    import_id = Column(UUID(as_uuid=True), ForeignKey("imports.id"), nullable=False)
    import_ = relationship("Import", back_populates="facts")

    entity = relationship("Entity", back_populates="facts")
    
    def __str__(self):
        return f"{self.event_date.strftime('%Y-%m-%d')} - {self.provider.value} - ${self.spend}"


class ComputeRun(Base):
    __tablename__ = "compute_runs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    as_of = Column(DateTime, nullable=False)
    computed_at = Column(DateTime, default=datetime.utcnow)
    reason = Column(String, nullable=False)
    status = Column(String, nullable=False)
    type = Column(Enum(ComputeRunTypeEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)

    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.id"), nullable=False)
    workspace = relationship("Workspace", back_populates="compute_runs")

    pnls = relationship("Pnl", back_populates="compute_run")
    
    def __str__(self):
        return f"{self.type.value} - {self.as_of.strftime('%Y-%m-%d')} ({self.status})"


class Pnl(Base):
    """Pnl (Profit & Loss) stores SNAPSHOT/EOD aggregations with BOTH base and derived metrics.
    
    Derived Metrics v1 philosophy:
    - Store base measures + derived metrics for FAST dashboard queries
    - Materialize expensive computations (no real-time calculation overhead)
    - "Locked" historical reports → snapshots don't change
    - Can recompute if formulas change (track formula_version if needed)
    
    WHY store derived in Pnl but not MetricFact?
    - Pnl: Snapshot/EOD → performance matters, data is historical
    - MetricFact: Source of truth → keep raw, avoid formula drift
    
    Original columns:
    - Base: spend, revenue, conversions, clicks, impressions
    - Derived: cpa, roas
    
    Derived Metrics v1 additions:
    - Base: leads, installs, purchases, visitors, profit
    - Derived: cpc, cpm, cpl, cpi, cpp, poas, arpv, aov, ctr, cvr
    
    Related:
    - app/services/compute_service.py: Computes these snapshots using app/metrics/registry
    - app/metrics/formulas.py: Pure functions for computing derived metrics
    """
    __tablename__ = "pnls"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    entity_id = Column(UUID(as_uuid=True), ForeignKey("entities.id"), nullable=True)
    run_id = Column(UUID(as_uuid=True), ForeignKey("compute_runs.id"), nullable=False)
    provider = Column(Enum(ProviderEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    level = Column(Enum(LevelEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    kind = Column(Enum(KindEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    as_of = Column(DateTime, nullable=True)
    event_date = Column(DateTime, nullable=True)
    
    # Original base measures
    spend = Column(Numeric(18, 4), nullable=False)
    revenue = Column(Numeric(18, 4), nullable=True)
    conversions = Column(Numeric(18, 4), nullable=True)
    clicks = Column(Integer, nullable=False)
    impressions = Column(Integer, nullable=False)
    
    # Derived Metrics v1: New base measures
    leads = Column(Numeric(18, 4), nullable=True)
    installs = Column(Integer, nullable=True)
    purchases = Column(Integer, nullable=True)
    visitors = Column(Integer, nullable=True)
    profit = Column(Numeric(18, 4), nullable=True)
    
    # Original derived metrics
    cpa = Column(Numeric(18, 4), nullable=True)
    roas = Column(Numeric(18, 4), nullable=True)
    
    # Derived Metrics v1: New derived metrics (Cost/Efficiency)
    cpc = Column(Numeric(18, 4), nullable=True)  # spend / clicks
    cpm = Column(Numeric(18, 4), nullable=True)  # (spend / impressions) * 1000
    cpl = Column(Numeric(18, 4), nullable=True)  # spend / leads
    cpi = Column(Numeric(18, 4), nullable=True)  # spend / installs
    cpp = Column(Numeric(18, 4), nullable=True)  # spend / purchases
    
    # Derived Metrics v1: New derived metrics (Revenue/Value)
    poas = Column(Numeric(18, 4), nullable=True)  # profit / spend
    arpv = Column(Numeric(18, 4), nullable=True)  # revenue / visitors
    aov = Column(Numeric(18, 4), nullable=True)  # revenue / conversions
    
    # Derived Metrics v1: New derived metrics (Performance/Engagement)
    ctr = Column(Numeric(18, 6), nullable=True)  # clicks / impressions (higher precision)
    cvr = Column(Numeric(18, 6), nullable=True)  # conversions / clicks (higher precision)
    
    computed_at = Column(DateTime, default=datetime.utcnow)

    entity = relationship("Entity", back_populates="pnls")
    compute_run = relationship("ComputeRun", back_populates="pnls")
    
    def __str__(self):
        date_str = self.event_date.strftime('%Y-%m-%d') if self.event_date else 'N/A'
        return f"{self.kind.value} P&L - {date_str} - ${self.spend}"


class QaQueryLog(Base):
    """QaQueryLog tracks all natural language queries made by users.
    
    When creating a query log in the admin panel:
    1. You MUST select a workspace_id - which workspace was this query made in?
    2. You MUST select a user_id - which user made this query?
    
    This creates an audit trail of who asked what questions and when.
    """
    __tablename__ = "qa_query_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Foreign keys - BOTH are required to track query context
    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    
    question_text = Column(String, nullable=False)  # The natural language question
    dsl_json = Column(JSON, nullable=False)  # The parsed query structure
    created_at = Column(DateTime, default=datetime.utcnow)
    duration_ms = Column(Integer, nullable=True)  # How long the query took to execute

    # Relationships for easy access to related objects
    workspace = relationship("Workspace", back_populates="queries")
    user = relationship("User", back_populates="queries")
    
    def __str__(self):
        return f"{self.question_text[:50]}... - {self.created_at.strftime('%Y-%m-%d %H:%M')}"


# Local auth credential (password hash stored separately) ----------

class AuthCredential(Base):
    __tablename__ = "auth_credentials"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="credential")
    
    def __str__(self):
        return f"Credential for {self.user.email if self.user else 'Unknown'}"

