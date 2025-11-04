"""Add timezone and currency_code to connections.

Revision ID: 20251104_000001
Revises: 20251101_000001
Create Date: 2025-11-04 15:00:00

WHAT:
    - Adds `timezone` and `currency_code` columns to `connections` to persist
      account-level settings for providers (Google Ads initially).

WHY:
    - Time-based windows and date segments use account timezone in Google Ads
      and should be normalized per account before aggregation.
    - Currency is set per account and needed for consistent display/rollups.

REFERENCES:
    docs/living-docs/GOOGLE_INTEGRATION_STATUS.MD (Date & timezone, Currency model)
    backend/app/models.py::Connection
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20251104_000001"
down_revision = "20251101_000001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Apply connection metadata columns for timezone/currency."""
    op.add_column(
        "connections",
        sa.Column("timezone", sa.String(), nullable=True),
    )
    op.add_column(
        "connections",
        sa.Column("currency_code", sa.String(), nullable=True),
    )


def downgrade() -> None:
    """Remove connection metadata columns."""
    op.drop_column("connections", "currency_code")
    op.drop_column("connections", "timezone")

