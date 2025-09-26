"""change users.role enum to string

Revision ID: 20250926_000003
Revises: 20250926_000002
Create Date: 2025-09-26 00:45:00
"""

from alembic import op
import sqlalchemy as sa


revision = '20250926_000003'
down_revision = '20250926_000002'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Alter column type from enum to string (using USING cast)
    op.execute("ALTER TABLE users ALTER COLUMN role TYPE VARCHAR USING role::text")
    # Drop the enum type if no longer used
    op.execute("DROP TYPE IF EXISTS roleenum")


def downgrade() -> None:
    # Recreate enum and cast back if needed
    op.execute("CREATE TYPE roleenum AS ENUM ('Owner', 'Admin', 'Viewer')")
    op.execute("ALTER TABLE users ALTER COLUMN role TYPE roleenum USING role::roleenum")


