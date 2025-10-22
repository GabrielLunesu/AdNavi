"""
Context Management Module
==========================

Manages conversation history for multi-turn QA interactions.

WHY this module exists:
- Users often ask follow-up questions that reference previous queries
- Examples: "Which one performed best?" after "Show me campaigns"
- Need to store recent DSLs + results to resolve pronouns and references

Components:
- redis_context_manager.py: Redis-backed conversation history storage (production)
- context_manager.py: In-memory implementation (deprecated, kept for reference)

Related files:
- app/services/qa_service.py: Uses context manager to track conversations
- app/nlp/translator.py: Uses context to resolve follow-up questions

Design principles:
- Redis-backed storage for production scalability
- User + workspace scoped (tenant isolation)
- Fixed-size history (last N queries to prevent memory bloat)
- TTL-based expiration (auto-cleanup after 1 hour)
- Thread-safe for concurrent requests
- Fail-fast if Redis unavailable

Architecture:
- Uses RedisContextManager as the primary implementation
- In-memory ContextManager kept temporarily for reference
- Single instance shared via app.state.context_manager
"""

from app.context.redis_context_manager import RedisContextManager

__all__ = ["RedisContextManager"]

