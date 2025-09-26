"""Alembic environment configuration for synchronous migrations.

Loads environment variables, builds an engine from DATABASE_URL, and exposes
Base.metadata for autogeneration.
"""

import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    # Our alembic.ini may not define logging sections; skip if missing
    try:
        fileConfig(config.config_file_name, disable_existing_loggers=False)
    except Exception:
        pass

# Ensure DATABASE_URL is available to Alembic via env var
if not os.getenv("DATABASE_URL"):
    # attempt to read from local .env
    try:
        from dotenv import load_dotenv  # type: ignore

        load_dotenv()
    except Exception:
        pass

# Ensure the app package is importable when running Alembic CLI
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # backend/
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Import application metadata
from app.database import Base  # noqa: E402
from app import models  # noqa: F401, E402  # register tables

target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = os.getenv("DATABASE_URL")
    if not url:
        raise RuntimeError("DATABASE_URL must be set for offline migrations")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    # Build a minimal configuration dict directly to avoid INI interpolation
    url = os.getenv("DATABASE_URL")
    if not url:
        raise RuntimeError("DATABASE_URL must be set for online migrations")

    connectable = engine_from_config(
        {"sqlalchemy.url": url},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()



