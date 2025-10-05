"""add_derived_metrics_v1

Revision ID: 9370d8b93e93
Revises: 20250926_000004
Create Date: 2025-10-05 11:59:11.319723

Derived Metrics v1 Schema Changes
==================================

This migration adds support for derived metrics by:
1. Adding Goal enum to track campaign objectives
2. Adding goal column to entities
3. Adding new base measure columns to metric_facts (leads, installs, purchases, visitors, profit)
4. Adding derived metric columns to pnls (cpc, cpm, cpl, cpi, cpp, poas, arpv, aov, ctr, cvr)

WHY:
- Single source of truth for metric formulas
- Store only base measures in MetricFact (facts remain raw)
- Compute derived metrics on-demand (executor) or during snapshots (Pnl)
- Entity.goal enables context-aware metric selection (CPI for app_installs, CPL for leads, etc.)

Related:
- app/metrics/formulas.py: Pure functions for computing derived metrics
- app/metrics/registry.py: Maps metric names to dependencies and functions
- app/dsl/executor.py: Uses registry for ad-hoc queries
- app/services/compute_service.py: Uses registry for Pnl snapshots
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '9370d8b93e93'
down_revision = '20250926_000004'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """
    Apply schema changes for Derived Metrics v1.
    
    Steps:
    1. Create Goal enum type
    2. Add goal column to entities (nullable for existing data)
    3. Add new base measure columns to metric_facts (all nullable)
    4. Add derived metric columns to pnls (all nullable)
    """
    
    # 1. Create Goal enum
    goal_enum = postgresql.ENUM(
        'awareness',
        'traffic', 
        'leads',
        'app_installs',
        'purchases',
        'conversions',
        'other',
        name='goalenum'
    )
    goal_enum.create(op.get_bind())
    
    # 2. Add goal column to entities
    op.add_column('entities', 
        sa.Column('goal', sa.Enum(
            'awareness',
            'traffic',
            'leads', 
            'app_installs',
            'purchases',
            'conversions',
            'other',
            name='goalenum'
        ), nullable=True)
    )
    
    # 3. Add new base measure columns to metric_facts
    # These are the raw input data needed to compute derived metrics
    op.add_column('metric_facts', 
        sa.Column('leads', sa.Numeric(18, 4), nullable=True))
    op.add_column('metric_facts',
        sa.Column('installs', sa.Integer(), nullable=True))
    op.add_column('metric_facts',
        sa.Column('purchases', sa.Integer(), nullable=True))
    op.add_column('metric_facts',
        sa.Column('visitors', sa.Integer(), nullable=True))
    op.add_column('metric_facts',
        sa.Column('profit', sa.Numeric(18, 4), nullable=True))
    
    # 4. Add derived metric columns to pnls
    # These are materialized snapshots for fast dashboard queries
    # Note: These can be recomputed from base measures if formulas change
    
    # Cost/Efficiency metrics
    op.add_column('pnls',
        sa.Column('cpc', sa.Numeric(18, 4), nullable=True))
    op.add_column('pnls',
        sa.Column('cpm', sa.Numeric(18, 4), nullable=True))
    op.add_column('pnls',
        sa.Column('cpl', sa.Numeric(18, 4), nullable=True))
    op.add_column('pnls',
        sa.Column('cpi', sa.Numeric(18, 4), nullable=True))
    op.add_column('pnls',
        sa.Column('cpp', sa.Numeric(18, 4), nullable=True))
    
    # Value metrics
    op.add_column('pnls',
        sa.Column('poas', sa.Numeric(18, 4), nullable=True))
    op.add_column('pnls',
        sa.Column('arpv', sa.Numeric(18, 4), nullable=True))
    op.add_column('pnls',
        sa.Column('aov', sa.Numeric(18, 4), nullable=True))
    
    # Engagement metrics (stored as decimals, format as percentages in UI)
    op.add_column('pnls',
        sa.Column('ctr', sa.Numeric(18, 6), nullable=True))  # Higher precision for small percentages
    op.add_column('pnls',
        sa.Column('cvr', sa.Numeric(18, 6), nullable=True))
    
    # Add base measure columns to pnls for completeness
    # (enables recomputing derived metrics from pnl snapshots)
    op.add_column('pnls',
        sa.Column('leads', sa.Numeric(18, 4), nullable=True))
    op.add_column('pnls',
        sa.Column('installs', sa.Integer(), nullable=True))
    op.add_column('pnls',
        sa.Column('purchases', sa.Integer(), nullable=True))
    op.add_column('pnls',
        sa.Column('visitors', sa.Integer(), nullable=True))
    op.add_column('pnls',
        sa.Column('profit', sa.Numeric(18, 4), nullable=True))


def downgrade() -> None:
    """
    Revert schema changes for Derived Metrics v1.
    
    WARNING: This will drop columns and data. Only use in development.
    """
    
    # Remove pnl columns (in reverse order)
    op.drop_column('pnls', 'profit')
    op.drop_column('pnls', 'visitors')
    op.drop_column('pnls', 'purchases')
    op.drop_column('pnls', 'installs')
    op.drop_column('pnls', 'leads')
    op.drop_column('pnls', 'cvr')
    op.drop_column('pnls', 'ctr')
    op.drop_column('pnls', 'aov')
    op.drop_column('pnls', 'arpv')
    op.drop_column('pnls', 'poas')
    op.drop_column('pnls', 'cpp')
    op.drop_column('pnls', 'cpi')
    op.drop_column('pnls', 'cpl')
    op.drop_column('pnls', 'cpm')
    op.drop_column('pnls', 'cpc')
    
    # Remove metric_facts columns
    op.drop_column('metric_facts', 'profit')
    op.drop_column('metric_facts', 'visitors')
    op.drop_column('metric_facts', 'purchases')
    op.drop_column('metric_facts', 'installs')
    op.drop_column('metric_facts', 'leads')
    
    # Remove entities goal column
    op.drop_column('entities', 'goal')
    
    # Drop Goal enum
    goal_enum = postgresql.ENUM(name='goalenum')
    goal_enum.drop(op.get_bind())



