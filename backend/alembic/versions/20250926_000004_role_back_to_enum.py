"""convert users.role back to enum

Revision ID: 20250926_000004
Revises: 20250926_000003
Create Date: 2025-09-26 00:55:00
"""

from alembic import op


revision = '20250926_000004'
down_revision = '20250926_000003'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Normalize any lowercase values to proper labels
    op.execute("UPDATE users SET role = 'Admin' WHERE role ILIKE 'admin'")
    op.execute("UPDATE users SET role = 'Owner' WHERE role ILIKE 'owner'")
    op.execute("UPDATE users SET role = 'Viewer' WHERE role ILIKE 'viewer'")

    # Recreate enum type if missing
    op.execute("DO $$ BEGIN IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'roleenum') THEN CREATE TYPE roleenum AS ENUM ('Owner','Admin','Viewer'); END IF; END$$;")

    # Cast column to enum
    op.execute("ALTER TABLE users ALTER COLUMN role TYPE roleenum USING role::roleenum")


def downgrade() -> None:
    # Cast back to text
    op.execute("ALTER TABLE users ALTER COLUMN role TYPE VARCHAR USING role::text")
    # Leave roleenum in place (no drop) to avoid breaking other migrations


