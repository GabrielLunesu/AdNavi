"""
Application State
=================

Global application state that persists across requests.

WHY this exists:
- Context manager needs to persist between HTTP requests
- Each QAService instance is created per-request and destroyed after
- Without shared state, conversation context is lost

WHAT it stores:
- context_manager: Singleton RedisContextManager instance for all QA requests

WHERE it's used:
- app/main.py: Initializes on startup with Redis validation
- app/services/qa_service.py: Uses shared instance instead of creating new one

Design:
- Simple module-level singleton pattern
- Thread-safe (Redis client has connection pooling)
- Redis-backed for production scalability
"""

import logging
from app.context.redis_context_manager import RedisContextManager
from app.deps import get_settings

logger = logging.getLogger(__name__)

# Singleton instance - shared across all requests
# This persists for the lifetime of the FastAPI application
# Uses Redis for distributed session storage across multiple instances
try:
    settings = get_settings()
    context_manager = RedisContextManager(
        redis_url=settings.REDIS_URL,
        max_history=settings.CONTEXT_MAX_HISTORY,
        ttl_seconds=settings.CONTEXT_TTL_SECONDS
    )
    logger.info("[STATE] Redis context manager initialized successfully")
except Exception as e:
    logger.error(f"[STATE] Failed to initialize Redis context manager: {e}")
    raise

