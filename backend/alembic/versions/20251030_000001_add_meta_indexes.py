"""add meta performance indexes

Revision ID: 20251030_000001
Revises: 9370d8b93e93
Create Date: 2025-10-30

WHY: Prepare database for high-volume Meta Ads data ingestion
- Meta provides hourly metrics → expect high insert volume
- Queries filter by date, entity, and provider frequently
- Need to prevent duplicate ingestion via natural_key

WHAT:
- Indexes for fast filtering (event_date, entity_id, provider)
- Composite index for common query pattern (entity_id + event_date)
- Unique constraint on natural_key to prevent duplicates

WHERE: metric_facts table (main fact table for all ad platform data)

REFERENCES:
- backend/docs/roadmap/meta-ads-roadmap.md Phase 1.1
- backend/app/models.py MetricFact model
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20251030_000001'
down_revision = '5b531bb7e3a8'  # Comes after add_manual_costs
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Add performance indexes for Meta Ads ingestion."""
    
    # Index on event_date for time-range queries
    # Usage: SELECT ... WHERE event_date BETWEEN '2025-01-01' AND '2025-01-31'
    op.create_index(
        'idx_metric_facts_event_date',
        'metric_facts',
        ['event_date'],
        unique=False
    )
    
    # Index on entity_id for entity-specific queries
    # Usage: SELECT ... WHERE entity_id = 'campaign-uuid'
    op.create_index(
        'idx_metric_facts_entity_id',
        'metric_facts',
        ['entity_id'],
        unique=False
    )
    
    # Index on provider for provider-specific queries
    # Usage: SELECT ... WHERE provider = 'meta'
    op.create_index(
        'idx_metric_facts_provider',
        'metric_facts',
        ['provider'],
        unique=False
    )
    
    # Composite index for common query pattern (entity + date range)
    # Usage: SELECT ... WHERE entity_id = 'uuid' AND event_date BETWEEN ...
    # PostgreSQL can use this for both filters efficiently
    op.create_index(
        'idx_metric_facts_entity_date',
        'metric_facts',
        ['entity_id', 'event_date'],
        unique=False
    )
    
    # Unique constraint on natural_key to prevent duplicate ingestion
    # natural_key format: f"{external_entity_id}-{event_at.isoformat()}"
    # Example: "act_123456789-2025-10-30T14:00:00+00:00"
    # This ensures we never ingest the same fact twice
    op.create_unique_constraint(
        'uq_metric_facts_natural_key',
        'metric_facts',
        ['natural_key']
    )


def downgrade() -> None:
    """Remove performance indexes."""
    
    # Drop unique constraint first
    op.drop_constraint('uq_metric_facts_natural_key', 'metric_facts', type_='unique')
    
    # Drop indexes
    op.drop_index('idx_metric_facts_entity_date', table_name='metric_facts')
    op.drop_index('idx_metric_facts_provider', table_name='metric_facts')
    op.drop_index('idx_metric_facts_entity_id', table_name='metric_facts')
    op.drop_index('idx_metric_facts_event_date', table_name='metric_facts')

