"""Update tokens table for encrypted storage.

Revision ID: 20251101_000001
Revises: db163fecca9d
Create Date: 2025-11-01 09:00:00

WHAT:
    - Adds ad_account_ids JSON column for storing linked Meta accounts.
    - Allows refresh_token_enc/expires_at to be NULL (system tokens have none).

WHY:
    Phase 2.1 of the Meta integration stores encrypted tokens
    without requiring optional fields.

REFERENCES:
    docs/living-docs/META_INTEGRATION_STATUS.md
    backend/app/models.py::Token
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20251101_000001"
down_revision = "db163fecca9d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Apply Phase 2.1 token schema adjustments."""
    op.add_column(
        "tokens",
        sa.Column("ad_account_ids", sa.JSON(), nullable=True),
    )
    op.alter_column("tokens", "refresh_token_enc", nullable=True)
    op.alter_column("tokens", "expires_at", nullable=True)


def downgrade() -> None:
    """Revert Phase 2.1 token schema adjustments."""
    op.alter_column("tokens", "expires_at", nullable=False)
    op.alter_column("tokens", "refresh_token_enc", nullable=False)
    op.drop_column("tokens", "ad_account_ids")
