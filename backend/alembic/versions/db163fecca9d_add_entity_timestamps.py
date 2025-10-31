"""add_entity_timestamps

Revision ID: db163fecca9d
Revises: 20251030_000001
Create Date: 2025-10-31 15:30:45.308092

WHAT:
    Adds created_at and updated_at timestamp columns to entities table.

WHY:
    - Track when entities are first synced from Meta
    - Track when entities are updated (status/name changes)
    - Enables debugging of sync issues
    - Consistent with other models (Workspace, Connection, etc.)

WHERE USED:
    - app/routers/meta_sync.py (sets timestamps during UPSERT)
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db163fecca9d'
down_revision = '20251030_000001'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Add created_at and updated_at columns to entities table."""
    # Add created_at column with default value
    op.add_column(
        'entities',
        sa.Column('created_at', sa.DateTime(), nullable=True)
    )
    
    # Add updated_at column with default value
    op.add_column(
        'entities',
        sa.Column('updated_at', sa.DateTime(), nullable=True)
    )
    
    # Set default values for existing rows using PostgreSQL NOW()
    # This executes at SQL execution time, not at import time
    op.execute(
        """
        UPDATE entities
        SET created_at = NOW()
        WHERE created_at IS NULL
        """
    )
    
    op.execute(
        """
        UPDATE entities
        SET updated_at = NOW()
        WHERE updated_at IS NULL
        """
    )
    
    # Make columns non-nullable after setting defaults
    op.alter_column('entities', 'created_at', nullable=False)
    op.alter_column('entities', 'updated_at', nullable=False)


def downgrade() -> None:
    """Remove created_at and updated_at columns from entities table."""
    op.drop_column('entities', 'updated_at')
    op.drop_column('entities', 'created_at')



