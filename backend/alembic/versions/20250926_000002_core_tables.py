"""create core tables with UUID PKs and auth_credentials

Revision ID: 20250926_000002
Revises: 20250926_000001
Create Date: 2025-09-26 00:30:00
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as pg


# revision identifiers, used by Alembic.
revision = '20250926_000002'
down_revision = '20250926_000001'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Drop legacy auth users table (integer id) if present
    op.execute("DROP TABLE IF EXISTS users CASCADE")

    # Clean up any partially-created enum types from previous failed runs
    for enum_name in [
        'roleenum', 'providerenum', 'levelenum', 'kindenum', 'computeruntypeenum'
    ]:
        op.execute(
            f"""
            DO $$
            BEGIN
                IF EXISTS (
                    SELECT 1 FROM pg_type t
                    JOIN pg_namespace n ON n.oid = t.typnamespace
                    WHERE t.typname = '{enum_name}'
                ) THEN
                    DROP TYPE {enum_name};
                END IF;
            END$$;
            """
        )

    # Enum types (create once; columns reference with create_type=False)
    role_enum_create = pg.ENUM('Owner', 'Admin', 'Viewer', name='roleenum')
    provider_enum_create = pg.ENUM('google', 'meta', 'tiktok', 'other', name='providerenum')
    level_enum_create = pg.ENUM('account', 'campaign', 'adset', 'ad', 'creative', 'unknown', name='levelenum')
    kind_enum_create = pg.ENUM('snapshot', 'eod', name='kindenum')
    run_type_enum_create = pg.ENUM('snapshot', 'eod', 'backfill', name='computeruntypeenum')

    role_enum_create.create(op.get_bind(), checkfirst=True)
    provider_enum_create.create(op.get_bind(), checkfirst=True)
    level_enum_create.create(op.get_bind(), checkfirst=True)
    kind_enum_create.create(op.get_bind(), checkfirst=True)
    run_type_enum_create.create(op.get_bind(), checkfirst=True)

    # Non-creating enum references used in table columns
    role_enum = pg.ENUM('Owner', 'Admin', 'Viewer', name='roleenum', create_type=False)
    provider_enum = pg.ENUM('google', 'meta', 'tiktok', 'other', name='providerenum', create_type=False)
    level_enum = pg.ENUM('account', 'campaign', 'adset', 'ad', 'creative', 'unknown', name='levelenum', create_type=False)
    kind_enum = pg.ENUM('snapshot', 'eod', name='kindenum', create_type=False)
    run_type_enum = pg.ENUM('snapshot', 'eod', 'backfill', name='computeruntypeenum', create_type=False)

    # Workspaces
    op.create_table(
        'workspaces',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )

    # Users
    op.create_table(
        'users',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('role', role_enum, nullable=False),
        sa.Column('workspace_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('workspaces.id'), nullable=False),
    )
    op.create_index('ix_users_email', 'users', ['email'], unique=True)

    # Tokens
    op.create_table(
        'tokens',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('provider', provider_enum, nullable=False),
        sa.Column('access_token_enc', sa.String(), nullable=False),
        sa.Column('refresh_token_enc', sa.String(), nullable=False),
        sa.Column('expires_at', sa.DateTime(), nullable=False),
        sa.Column('scope', sa.String(), nullable=True),
    )

    # Connections
    op.create_table(
        'connections',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('provider', provider_enum, nullable=False),
        sa.Column('external_account_id', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('status', sa.String(), nullable=False),
        sa.Column('connected_at', sa.DateTime(), nullable=True),
        sa.Column('workspace_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('workspaces.id'), nullable=False),
        sa.Column('token_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('tokens.id'), nullable=True),
    )

    # Fetches
    op.create_table(
        'fetches',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('kind', sa.String(), nullable=False),
        sa.Column('status', sa.String(), nullable=False),
        sa.Column('started_at', sa.DateTime(), nullable=True),
        sa.Column('finished_at', sa.DateTime(), nullable=True),
        sa.Column('range_start', sa.DateTime(), nullable=True),
        sa.Column('range_end', sa.DateTime(), nullable=True),
        sa.Column('connection_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('connections.id'), nullable=False),
    )

    # Imports
    op.create_table(
        'imports',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('as_of', sa.DateTime(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('note', sa.String(), nullable=True),
        sa.Column('fetch_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('fetches.id'), nullable=False),
    )

    # Entities
    op.create_table(
        'entities',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('level', level_enum, nullable=False),
        sa.Column('external_id', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('status', sa.String(), nullable=False),
        sa.Column('parent_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('entities.id'), nullable=True),
        sa.Column('workspace_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('workspaces.id'), nullable=False),
        sa.Column('connection_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('connections.id'), nullable=True),
    )

    # Metric facts
    op.create_table(
        'metric_facts',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('entity_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('entities.id'), nullable=True),
        sa.Column('provider', provider_enum, nullable=False),
        sa.Column('level', level_enum, nullable=False),
        sa.Column('event_at', sa.DateTime(), nullable=False),
        sa.Column('event_date', sa.DateTime(), nullable=False),
        sa.Column('spend', sa.Numeric(18, 4), nullable=False),
        sa.Column('impressions', sa.Integer(), nullable=False),
        sa.Column('clicks', sa.Integer(), nullable=False),
        sa.Column('conversions', sa.Numeric(18, 4), nullable=True),
        sa.Column('revenue', sa.Numeric(18, 4), nullable=True),
        sa.Column('currency', sa.String(), nullable=False),
        sa.Column('natural_key', sa.String(), nullable=False),
        sa.Column('ingested_at', sa.DateTime(), nullable=True),
        sa.Column('import_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('imports.id'), nullable=False),
    )

    # Compute runs
    op.create_table(
        'compute_runs',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('as_of', sa.DateTime(), nullable=False),
        sa.Column('computed_at', sa.DateTime(), nullable=True),
        sa.Column('reason', sa.String(), nullable=False),
        sa.Column('status', sa.String(), nullable=False),
        sa.Column('type', run_type_enum, nullable=False),
        sa.Column('workspace_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('workspaces.id'), nullable=False),
    )

    # Pnls
    op.create_table(
        'pnls',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('entity_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('entities.id'), nullable=True),
        sa.Column('run_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('compute_runs.id'), nullable=False),
        sa.Column('provider', provider_enum, nullable=False),
        sa.Column('level', level_enum, nullable=False),
        sa.Column('kind', kind_enum, nullable=False),
        sa.Column('as_of', sa.DateTime(), nullable=True),
        sa.Column('event_date', sa.DateTime(), nullable=True),
        sa.Column('spend', sa.Numeric(18, 4), nullable=False),
        sa.Column('revenue', sa.Numeric(18, 4), nullable=True),
        sa.Column('conversions', sa.Numeric(18, 4), nullable=True),
        sa.Column('clicks', sa.Integer(), nullable=False),
        sa.Column('impressions', sa.Integer(), nullable=False),
        sa.Column('cpa', sa.Numeric(18, 4), nullable=True),
        sa.Column('roas', sa.Numeric(18, 4), nullable=True),
        sa.Column('computed_at', sa.DateTime(), nullable=True),
    )

    # QA query log
    op.create_table(
        'qa_query_logs',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('workspace_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('workspaces.id'), nullable=False),
        sa.Column('user_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('question_text', sa.String(), nullable=False),
        sa.Column('dsl_json', sa.JSON(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('duration_ms', sa.Integer(), nullable=True),
    )

    # Local auth credentials (1:1 with users)
    op.create_table(
        'auth_credentials',
        sa.Column('user_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id'), primary_key=True),
        sa.Column('password_hash', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    # Drop in reverse dependency order
    op.drop_table('auth_credentials')
    op.drop_table('qa_query_logs')
    op.drop_table('pnls')
    op.drop_table('compute_runs')
    op.drop_table('metric_facts')
    op.drop_table('entities')
    op.drop_table('imports')
    op.drop_table('fetches')
    op.drop_table('connections')
    op.drop_table('tokens')
    op.drop_index('ix_users_email', table_name='users')
    op.drop_table('users')
    op.drop_table('workspaces')

    # Drop enum types
    sa.Enum(name='computeruntypeenum').drop(op.get_bind(), checkfirst=True)
    sa.Enum(name='kindenum').drop(op.get_bind(), checkfirst=True)
    sa.Enum(name='levelenum').drop(op.get_bind(), checkfirst=True)
    sa.Enum(name='providerenum').drop(op.get_bind(), checkfirst=True)
    sa.Enum(name='roleenum').drop(op.get_bind(), checkfirst=True)


