"""add_manual_costs

Revision ID: 5b531bb7e3a8
Revises: 9370d8b93e93
Create Date: 2025-10-11 20:21:46.964010

WHAT: Adds manual_costs table for user-entered operational costs
WHY: Finance P&L needs to track non-ad costs (SaaS, agency fees, etc.)
REFERENCES: app/models.py:ManualCost
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '5b531bb7e3a8'
down_revision = '9370d8b93e93'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'manual_costs',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('label', sa.String(), nullable=False),
        sa.Column('category', sa.String(), nullable=False),
        sa.Column('notes', sa.String(), nullable=True),
        sa.Column('amount_dollar', sa.Numeric(12, 2), nullable=False),
        sa.Column('allocation_type', sa.String(), nullable=False),
        sa.Column('allocation_date', sa.DateTime(), nullable=True),
        sa.Column('allocation_start', sa.DateTime(), nullable=True),
        sa.Column('allocation_end', sa.DateTime(), nullable=True),
        sa.Column('workspace_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('created_by_user_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id']),
        sa.ForeignKeyConstraint(['created_by_user_id'], ['users.id'])
    )
    op.create_index('idx_manual_costs_workspace', 'manual_costs', ['workspace_id'])
    op.create_index('idx_manual_costs_dates', 'manual_costs', ['allocation_start', 'allocation_end'])


def downgrade() -> None:
    op.drop_index('idx_manual_costs_dates')
    op.drop_index('idx_manual_costs_workspace')
    op.drop_table('manual_costs')



