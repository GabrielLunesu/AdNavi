"""Make tokens.access_token_enc nullable for Google refresh-token storage.

Revision ID: 20251104_000002
Revises: 20251104_000001
Create Date: 2025-11-04 16:10:00

WHAT:
    Allow storing only a refresh token for providers that don't need
    a persistent access token in DB (e.g., Google Ads).

WHY:
    Access tokens are short-lived; we keep refresh tokens encrypted and
    reconstruct clients from env + DB refresh on demand.

REFERENCES:
    docs/meta-ads-lib/PHASE_2_1_TOKEN_ENCRYPTION.md
    backend/app/services/token_service.py
"""

from alembic import op
import sqlalchemy as sa


revision = "20251104_000002"
down_revision = "20251104_000001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("tokens", "access_token_enc", nullable=True)


def downgrade() -> None:
    # WARNING: This may fail if NULL values exist
    op.alter_column("tokens", "access_token_enc", nullable=False)

