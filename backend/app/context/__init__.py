"""
Context Management Module
==========================

Manages conversation history for multi-turn QA interactions.

WHY this module exists:
- Users often ask follow-up questions that reference previous queries
- Examples: "Which one performed best?" after "Show me campaigns"
- Need to store recent DSLs + results to resolve pronouns and references

Components:
- context_manager.py: In-memory conversation history storage

Related files:
- app/services/qa_service.py: Uses context manager to track conversations
- app/nlp/translator.py: Uses context to resolve follow-up questions

Design principles:
- Simple in-memory storage (no database persistence yet)
- User + workspace scoped (tenant isolation)
- Fixed-size history (last N queries to prevent memory bloat)
- Thread-safe for concurrent requests

Future enhancements:
- Persistent storage (Redis, PostgreSQL)
- Cross-session history
- Smart context pruning (relevance-based, not just FIFO)
"""

from app.context.context_manager import ContextManager

__all__ = ["ContextManager"]

