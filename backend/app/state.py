"""
Application State
=================

Global application state that persists across requests.

WHY this exists:
- Context manager needs to persist between HTTP requests
- Each QAService instance is created per-request and destroyed after
- Without shared state, conversation context is lost

WHAT it stores:
- context_manager: Singleton ContextManager instance for all QA requests

WHERE it's used:
- app/main.py: Initializes on startup
- app/services/qa_service.py: Uses shared instance instead of creating new one

Design:
- Simple module-level singleton pattern
- Thread-safe (ContextManager has internal locks)
- In-memory for now (could be Redis/database in future)
"""

from app.context.context_manager import ContextManager

# Singleton instance - shared across all requests
# This persists for the lifetime of the FastAPI application
context_manager = ContextManager(max_history=5)

