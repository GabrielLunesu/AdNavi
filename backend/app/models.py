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


# Core models ----------------------------------------------------

class Workspace(Base):
    __tablename__ = "workspaces"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    users = relationship("User", back_populates="workspace")
    connections = relationship("Connection", back_populates="workspace")
    entities = relationship("Entity", back_populates="workspace")
    compute_runs = relationship("ComputeRun", back_populates="workspace")
    queries = relationship("QaQueryLog", back_populates="workspace")


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    role = Column(Enum(RoleEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)

    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.id"), nullable=False)
    workspace = relationship("Workspace", back_populates="users")

    # 1:1 credential for local password-based auth
    credential = relationship("AuthCredential", back_populates="user", uselist=False)

    queries = relationship("QaQueryLog", back_populates="user")


class Connection(Base):
    __tablename__ = "connections"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    provider = Column(Enum(ProviderEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    external_account_id = Column(String, nullable=False)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    connected_at = Column(DateTime, default=datetime.utcnow)

    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.id"), nullable=False)
    workspace = relationship("Workspace", back_populates="connections")

    token_id = Column(UUID(as_uuid=True), ForeignKey("tokens.id"))
    token = relationship("Token", back_populates="connections")

    entities = relationship("Entity", back_populates="connection")
    fetches = relationship("Fetch", back_populates="connection")


class Token(Base):
    __tablename__ = "tokens"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    provider = Column(Enum(ProviderEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    access_token_enc = Column(String, nullable=False)
    refresh_token_enc = Column(String, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    scope = Column(String, nullable=True)

    connections = relationship("Connection", back_populates="token")


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


class Import(Base):
    __tablename__ = "imports"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    as_of = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    note = Column(String, nullable=True)

    fetch_id = Column(UUID(as_uuid=True), ForeignKey("fetches.id"), nullable=False)
    fetch = relationship("Fetch", back_populates="imports")

    facts = relationship("MetricFact", back_populates="import_")


class Entity(Base):
    __tablename__ = "entities"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    level = Column(Enum(LevelEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    external_id = Column(String, nullable=False)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    parent_id = Column(UUID(as_uuid=True), ForeignKey("entities.id"), nullable=True)

    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.id"), nullable=False)
    workspace = relationship("Workspace", back_populates="entities")

    connection_id = Column(UUID(as_uuid=True), ForeignKey("connections.id"), nullable=True)
    connection = relationship("Connection", back_populates="entities")

    children = relationship("Entity", backref="parent", remote_side=[id])
    facts = relationship("MetricFact", back_populates="entity")
    pnls = relationship("Pnl", back_populates="entity")


class MetricFact(Base):
    __tablename__ = "metric_facts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    entity_id = Column(UUID(as_uuid=True), ForeignKey("entities.id"), nullable=True)
    provider = Column(Enum(ProviderEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    level = Column(Enum(LevelEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    event_at = Column(DateTime, nullable=False)
    event_date = Column(DateTime, nullable=False)
    spend = Column(Numeric(18, 4), nullable=False)
    impressions = Column(Integer, nullable=False)
    clicks = Column(Integer, nullable=False)
    conversions = Column(Numeric(18, 4), nullable=True)
    revenue = Column(Numeric(18, 4), nullable=True)
    currency = Column(String, nullable=False)
    natural_key = Column(String, nullable=False)
    ingested_at = Column(DateTime, default=datetime.utcnow)

    import_id = Column(UUID(as_uuid=True), ForeignKey("imports.id"), nullable=False)
    import_ = relationship("Import", back_populates="facts")

    entity = relationship("Entity", back_populates="facts")


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


class Pnl(Base):
    __tablename__ = "pnls"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    entity_id = Column(UUID(as_uuid=True), ForeignKey("entities.id"), nullable=True)
    run_id = Column(UUID(as_uuid=True), ForeignKey("compute_runs.id"), nullable=False)
    provider = Column(Enum(ProviderEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    level = Column(Enum(LevelEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    kind = Column(Enum(KindEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    as_of = Column(DateTime, nullable=True)
    event_date = Column(DateTime, nullable=True)
    spend = Column(Numeric(18, 4), nullable=False)
    revenue = Column(Numeric(18, 4), nullable=True)
    conversions = Column(Numeric(18, 4), nullable=True)
    clicks = Column(Integer, nullable=False)
    impressions = Column(Integer, nullable=False)
    cpa = Column(Numeric(18, 4), nullable=True)
    roas = Column(Numeric(18, 4), nullable=True)
    computed_at = Column(DateTime, default=datetime.utcnow)

    entity = relationship("Entity", back_populates="pnls")
    compute_run = relationship("ComputeRun", back_populates="pnls")


class QaQueryLog(Base):
    __tablename__ = "qa_query_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    question_text = Column(String, nullable=False)
    dsl_json = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    duration_ms = Column(Integer, nullable=True)

    workspace = relationship("Workspace", back_populates="queries")
    user = relationship("User", back_populates="queries")


# Local auth credential (password hash stored separately) ----------

class AuthCredential(Base):
    __tablename__ = "auth_credentials"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="credential")

