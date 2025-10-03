"""
Context Manager
===============

Stores conversation history per user+workspace for multi-turn QA interactions.

WHY this exists:
- Users often ask follow-ups like "Which one performed best?" or "And yesterday?"
- To resolve these, we need recent DSLs + results in memory
- Keeps last N queries (default 5) to prevent memory bloat
- Context is scoped per user+workspace to prevent cross-tenant leaks

WHAT it does:
- Stores recent questions, DSLs, and execution results
- Provides history for the translator to resolve pronouns and references
- Automatically evicts old entries (FIFO with max_history limit)

WHERE it's used:
- app/services/qa_service.py: Adds entries after each successful QA run
- app/nlp/translator.py: Retrieves context to help resolve follow-up questions

Design principles:
- Simple in-memory storage (fast, no DB overhead)
- User+workspace scoping (tenant safety)
- Fixed-size deque (prevents unbounded memory growth)
- Thread-safe operations (safe for concurrent FastAPI requests)

Examples:
    >>> cm = ContextManager(max_history=5)
    >>> # After user asks "What's my ROAS this week?"
    >>> cm.add_entry(
    ...     user_id="user123",
    ...     workspace_id="ws456",
    ...     question="What's my ROAS this week?",
    ...     dsl={"metric": "roas", "time_range": {"last_n_days": 7}},
    ...     result={"summary": 2.45, "delta_pct": 0.19}
    ... )
    >>> # Later, retrieve context for follow-up "Which one performed best?"
    >>> history = cm.get_context("user123", "ws456")
    >>> print(history[-1]["question"])  # "What's my ROAS this week?"

Future enhancements:
- Persistent storage (Redis for session continuity across restarts)
- TTL-based expiration (auto-cleanup old conversations)
- Smart pruning (keep relevant context, not just recent)
- Cross-session history (requires database persistence)
"""

from collections import deque
from typing import Dict, Any, List
from threading import Lock


class ContextManager:
    """
    Manages conversation history for multi-turn QA interactions.
    
    This class stores recent questions, DSLs, and execution results
    per user+workspace to enable follow-up question resolution.
    
    Thread safety:
    - Uses a lock to protect dictionary operations
    - Safe for concurrent FastAPI requests
    
    Memory management:
    - Uses deque with maxlen for automatic eviction
    - Each user+workspace limited to max_history entries
    - Old entries automatically removed (FIFO)
    
    Scoping:
    - Key format: "{user_id}:{workspace_id}"
    - Prevents cross-tenant context leaks
    - Each user sees only their own history per workspace
    
    Attributes:
        histories: Dict mapping "{user_id}:{workspace_id}" to deque of entries
        max_history: Maximum number of queries to store per user+workspace
        _lock: Thread lock for safe concurrent access
    
    Related:
    - Used by: app/services/qa_service.py (adds entries after QA runs)
    - Used by: app/nlp/translator.py (retrieves context for follow-ups)
    """
    
    def __init__(self, max_history: int = 5):
        """
        Initialize the context manager.
        
        Args:
            max_history: Maximum number of queries to store per user+workspace.
                        Default is 5 (balance between context richness and memory).
                        
        WHY max_history=5:
        - Enough context for most follow-up scenarios
        - Prevents unbounded memory growth
        - Fits comfortably in LLM context window
        
        Design:
        - histories: Dict of deques for O(1) append and automatic eviction
        - _lock: Ensures thread-safe operations for concurrent requests
        
        Examples:
            >>> # Default: store last 5 queries per user
            >>> cm = ContextManager()
            >>> 
            >>> # Custom: store only last 2 queries (minimal memory)
            >>> cm_minimal = ContextManager(max_history=2)
        """
        # Store conversation history per user+workspace
        # Key: "{user_id}:{workspace_id}"
        # Value: deque of {"question": str, "dsl": dict, "result": dict}
        self.histories: Dict[str, deque] = {}
        
        self.max_history = max_history
        
        # Thread lock for safe concurrent access
        # WHY needed: Multiple FastAPI requests may modify histories simultaneously
        self._lock = Lock()
    
    def add_entry(
        self,
        user_id: str,
        workspace_id: str,
        question: str,
        dsl: dict,
        result: dict
    ) -> None:
        """
        Add a new QA entry to the conversation history.
        
        Args:
            user_id: User UUID (or "anon" for unauthenticated sessions)
            workspace_id: Workspace UUID for scoping
            question: Original user question text
            dsl: Executed DSL (as dict, from MetricQuery.model_dump())
            result: Execution result (as dict, from MetricResult.model_dump() or executor dict)
            
        Process:
        1. Build scoped key "{user_id}:{workspace_id}"
        2. Initialize deque if first entry for this user+workspace
        3. Append entry to deque (auto-evicts oldest if at max_history)
        
        Thread safety:
        - Uses lock to prevent concurrent modification errors
        - Safe to call from multiple FastAPI request handlers
        
        Storage format:
        Each entry is a dict with:
        - question: str (original user question)
        - dsl: dict (executed MetricQuery as dict)
        - result: dict (execution result as dict)
        
        Examples:
            >>> cm = ContextManager()
            >>> cm.add_entry(
            ...     user_id="user123",
            ...     workspace_id="ws456",
            ...     question="What's my ROAS this week?",
            ...     dsl={"metric": "roas", "time_range": {"last_n_days": 7}},
            ...     result={"summary": 2.45}
            ... )
            >>> # Later add follow-up
            >>> cm.add_entry(
            ...     user_id="user123",
            ...     workspace_id="ws456",
            ...     question="And yesterday?",
            ...     dsl={"metric": "roas", "time_range": {"last_n_days": 1}},
            ...     result={"summary": 2.30}
            ... )
        
        Related:
        - Called by: app/services/qa_service.py after successful QA execution
        - Used with: get_context() to retrieve history for follow-ups
        """
        key = f"{user_id}:{workspace_id}"
        
        with self._lock:
            # Initialize deque if first entry for this user+workspace
            # WHY maxlen: Automatically evicts oldest entry when full (FIFO)
            if key not in self.histories:
                self.histories[key] = deque(maxlen=self.max_history)
            
            # Append new entry (auto-evicts oldest if at max_history)
            self.histories[key].append({
                "question": question,
                "dsl": dsl,
                "result": result
            })
    
    def get_context(self, user_id: str, workspace_id: str) -> List[Dict[str, Any]]:
        """
        Retrieve conversation history for a user+workspace.
        
        Args:
            user_id: User UUID (or "anon" for unauthenticated sessions)
            workspace_id: Workspace UUID for scoping
            
        Returns:
            List of conversation entries (oldest first, newest last)
            Each entry is a dict: {"question": str, "dsl": dict, "result": dict}
            Returns empty list if no history exists for this user+workspace
            
        Thread safety:
        - Uses lock to prevent reading during concurrent writes
        - Returns a copy of the deque as a list (safe to modify)
        
        WHY return list (not deque):
        - Easier to work with (indexing, slicing)
        - Safe to modify without affecting stored history
        - Translator can easily get last N entries
        
        Examples:
            >>> cm = ContextManager()
            >>> # ... add some entries ...
            >>> history = cm.get_context("user123", "ws456")
            >>> if history:
            ...     last_question = history[-1]["question"]
            ...     last_dsl = history[-1]["dsl"]
            ...     print(f"Last question: {last_question}")
            >>> # Empty history returns []
            >>> empty = cm.get_context("new_user", "ws456")
            >>> print(empty)  # []
        
        Related:
        - Called by: app/services/qa_service.py before translation
        - Passed to: app/nlp/translator.py for context-aware translation
        - Used with: add_entry() to store history
        """
        key = f"{user_id}:{workspace_id}"
        
        with self._lock:
            # Return copy as list (safe to modify, won't affect stored history)
            # WHY list(): deque is internal; return standard Python list
            return list(self.histories.get(key, []))
    
    def clear_context(self, user_id: str, workspace_id: str) -> None:
        """
        Clear conversation history for a specific user+workspace.
        
        Args:
            user_id: User UUID (or "anon" for unauthenticated sessions)
            workspace_id: Workspace UUID for scoping
            
        Use cases:
        - User explicitly requests to start a new conversation
        - Session reset or logout
        - Testing (clean slate between test cases)
        
        Thread safety:
        - Uses lock to prevent clearing during concurrent operations
        
        Examples:
            >>> cm = ContextManager()
            >>> # ... add some entries ...
            >>> cm.clear_context("user123", "ws456")
            >>> history = cm.get_context("user123", "ws456")
            >>> print(len(history))  # 0
        
        Related:
        - Could be called by: Future /qa/reset endpoint
        - Used in: Tests for clean state
        """
        key = f"{user_id}:{workspace_id}"
        
        with self._lock:
            if key in self.histories:
                del self.histories[key]
    
    def get_all_keys(self) -> List[str]:
        """
        Get all active user+workspace keys (for debugging/monitoring).
        
        Returns:
            List of keys in format "{user_id}:{workspace_id}"
            
        Use cases:
        - Monitoring: How many active conversations?
        - Debugging: Which users have context?
        - Cleanup: Identify stale sessions
        
        Thread safety:
        - Uses lock to get consistent snapshot
        
        Examples:
            >>> cm = ContextManager()
            >>> # ... add entries for multiple users ...
            >>> keys = cm.get_all_keys()
            >>> print(f"Active conversations: {len(keys)}")
            >>> print(keys)  # ["user1:ws1", "user2:ws1", "user1:ws2"]
        
        Related:
        - Useful for: Monitoring, debugging, cleanup
        """
        with self._lock:
            return list(self.histories.keys())

