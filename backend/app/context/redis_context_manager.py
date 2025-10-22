"""
Redis Context Manager
====================

Stores conversation history per user+workspace in Redis for multi-turn QA interactions.

WHY this exists:
- Users often ask follow-ups like "Which one performed best?" or "And yesterday?"
- To resolve these, we need recent DSLs + results accessible across server instances
- Redis enables horizontal scaling and persistence across restarts
- TTL-based expiration prevents unbounded memory growth

WHAT it does:
- Stores recent questions, DSLs, and execution results in Redis
- Provides history for the translator to resolve pronouns and references
- Automatically expires old entries via TTL (default 1 hour)
- Enables multi-instance deployment with shared conversation state

WHERE it's used:
- app/services/qa_service.py: Adds entries after each successful QA run
- app/nlp/translator.py: Retrieves context to help resolve follow-up questions

Design principles:
- Redis-backed storage (fast, distributed, persistent)
- Connection pooling for performance
- Fail-fast approach (no fallback, clear errors)
- TTL-based cleanup (automatic expiration)
- Thread-safe operations (safe for concurrent FastAPI requests)

Examples:
    >>> from app.context.redis_context_manager import RedisContextManager
    >>> cm = RedisContextManager(
    ...     redis_url="redis://localhost:6379/0",
    ...     max_history=5,
    ...     ttl_seconds=3600
    ... )
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
- Cluster mode support for high availability
- Smarter pruning (keep relevant context, not just recent)
- Context compression for large results
- Analytics on conversation patterns
"""

import json
import logging
from typing import Dict, Any, List
from redis import Redis, ConnectionError as RedisConnectionError
from redis.connection import ConnectionPool

logger = logging.getLogger(__name__)


class ConnectionError(Exception):
    """Raised when Redis connection fails."""
    pass


class RedisContextManager:
    """
    Manages conversation history in Redis for multi-turn QA interactions.
    
    This class stores recent questions, DSLs, and execution results per user+workspace
    in Redis to enable follow-up question resolution across multiple server instances.
    
    Thread safety:
    - Redis client is thread-safe by default
    - Uses connection pooling for safe concurrent access
    - Safe for concurrent FastAPI requests
    
    Memory management:
    - Uses Redis TTL for automatic expiration (default 1 hour)
    - Limits history size per user+workspace (default 5 entries)
    - Old entries auto-evicted when max_history exceeded
    
    Scoping:
    - Key format: "context:{user_id}:{workspace_id}"
    - Prevents cross-tenant context leaks
    - Each user sees only their own history per workspace
    
    Attributes:
        redis_client: Redis client instance with connection pooling
        max_history: Maximum number of queries to store per user+workspace
        ttl_seconds: Time-to-live for context entries (seconds)
        _keys_pattern: Pattern for finding all context keys
    
    Related:
    - Used by: app/services/qa_service.py (adds entries after QA runs)
    - Used by: app/nlp/translator.py (retrieves context for follow-ups)
    - Replaces: app/context/context_manager.py (in-memory implementation)
    """
    
    def __init__(self, redis_url: str, max_history: int = 5, ttl_seconds: int = 3600):
        """
        Initialize the Redis context manager.
        
        Args:
            redis_url: Redis connection URL (e.g., "redis://localhost:6379/0")
            max_history: Maximum number of queries to store per user+workspace (default: 5)
            ttl_seconds: Time-to-live for context entries in seconds (default: 3600 = 1 hour)
        
        Raises:
            ConnectionError: If Redis connection fails (fail-fast approach)
        
        WHY max_history=5:
        - Enough context for most follow-up scenarios
        - Prevents unbounded memory growth
        - Fits comfortably in LLM context window
        
        WHY ttl_seconds=3600:
        - Standard session timeout (1 hour)
        - Prevents stale context from piling up
        - Matches typical user session duration
        
        Design:
        - Uses connection pooling for performance
        - Sets decode_responses=True for automatic string handling
        - Configures socket_keepalive for stability
        
        Examples:
            >>> # Default: 5 entries, 1 hour TTL
            >>> cm = RedisContextManager("redis://localhost:6379/0")
            >>> 
            >>> # Custom: 10 entries, 30 minute TTL
            >>> cm_custom = RedisContextManager(
            ...     "redis://localhost:6379/0",
            ...     max_history=10,
            ...     ttl_seconds=1800
            ... )
        """
        self.max_history = max_history
        self.ttl_seconds = ttl_seconds
        self._keys_pattern = "context:*"
        
        # Create connection pool for performance
        try:
            self.pool = ConnectionPool.from_url(
                redis_url,
                decode_responses=True,
                socket_keepalive=True,
                max_connections=50
            )
            self.redis_client = Redis(connection_pool=self.pool)
            
            # Verify connection with ping
            self.redis_client.ping()
            logger.info(f"[REDIS_CONTEXT] Connected to Redis at {redis_url}")
        except RedisConnectionError as e:
            logger.error(f"[REDIS_CONTEXT] Failed to connect to Redis: {e}")
            raise ConnectionError(f"Redis unavailable: {e}. Ensure Redis is running and REDIS_URL is correct.")
    
    def add_entry(
        self,
        user_id: str,
        workspace_id: str,
        question: str,
        dsl: dict,
        result: dict
    ) -> None:
        """
        Add a new QA entry to the conversation history in Redis.
        
        Args:
            user_id: User UUID (or "anon" for unauthenticated sessions)
            workspace_id: Workspace UUID for scoping
            question: Original user question text
            dsl: Executed DSL (as dict, from MetricQuery.model_dump())
            result: Execution result (as dict, from MetricResult.model_dump() or executor dict)
        
        Raises:
            ConnectionError: If Redis write fails
        
        Process:
        1. Build scoped key "context:{user_id}:{workspace_id}"
        2. Serialize entry as JSON
        3. Push to front of Redis list (LPUSH)
        4. Trim list to max_history entries (LTRIM)
        5. Set TTL on key for auto-expiration
        
        Implementation:
        - Uses Redis list for FIFO behavior (LPUSH + LTRIM)
        - Stores entries as JSON strings for flexibility
        - TTL refreshed on every write (keeps active conversations alive)
        - Pipeline used for atomic multi-command execution
        
        Examples:
            >>> cm = RedisContextManager("redis://localhost:6379/0")
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
        key = f"context:{user_id}:{workspace_id}"
        entry = json.dumps({
            "question": question,
            "dsl": dsl,
            "result": result
        })
        
        try:
            # Use pipeline for atomic multi-command execution
            pipe = self.redis_client.pipeline()
            pipe.lpush(key, entry)  # Add to front
            pipe.ltrim(key, 0, self.max_history - 1)  # Keep only last N entries
            pipe.expire(key, self.ttl_seconds)  # Refresh TTL
            pipe.execute()
            
            logger.debug(f"[REDIS_CONTEXT] Added entry for {key}")
        except (RedisConnectionError, Exception) as e:
            logger.error(f"[REDIS_CONTEXT] Failed to add entry: {e}")
            raise ConnectionError(f"Redis write failed: {e}")
    
    def get_context(self, user_id: str, workspace_id: str) -> List[Dict[str, Any]]:
        """
        Retrieve conversation history for a user+workspace from Redis.
        
        Args:
            user_id: User UUID (or "anon" for unauthenticated sessions)
            workspace_id: Workspace UUID for scoping
        
        Returns:
            List of conversation entries (oldest first, newest last)
            Each entry is a dict: {"question": str, "dsl": dict, "result": dict}
            Returns empty list if no history exists for this user+workspace
        
        Raises:
            ConnectionError: If Redis read fails
        
        WHY return list (not deque):
        - Easier to work with (indexing, slicing)
        - Safe to modify without affecting stored history
        - Translator can easily get last N entries
        
        Examples:
            >>> cm = RedisContextManager("redis://localhost:6379/0")
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
        key = f"context:{user_id}:{workspace_id}"
        
        try:
            # Retrieve all entries (LRANGE returns all elements)
            entries = self.redis_client.lrange(key, 0, -1)
            
            # Deserialize JSON and reverse to get chronological order (oldest first)
            context = [json.loads(entry) for entry in reversed(entries)]
            
            logger.debug(f"[REDIS_CONTEXT] Retrieved {len(context)} entries for {key}")
            return context
        except (RedisConnectionError, Exception) as e:
            logger.error(f"[REDIS_CONTEXT] Failed to get context: {e}")
            raise ConnectionError(f"Redis read failed: {e}")
        except json.JSONDecodeError as e:
            logger.error(f"[REDIS_CONTEXT] Failed to deserialize entry: {e}")
            # Return empty context rather than failing completely
            return []
    
    def clear_context(self, user_id: str, workspace_id: str) -> None:
        """
        Clear conversation history for a specific user+workspace in Redis.
        
        Args:
            user_id: User UUID (or "anon" for unauthenticated sessions)
            workspace_id: Workspace UUID for scoping
        
        Raises:
            ConnectionError: If Redis delete fails
        
        Use cases:
        - User explicitly requests to start a new conversation
        - Session reset or logout
        - Testing (clean slate between test cases)
        
        Examples:
            >>> cm = RedisContextManager("redis://localhost:6379/0")
            >>> # ... add some entries ...
            >>> cm.clear_context("user123", "ws456")
            >>> history = cm.get_context("user123", "ws456")
            >>> print(len(history))  # 0
        
        Related:
        - Could be called by: Future /qa/reset endpoint
        - Used in: Tests for clean state
        """
        key = f"context:{user_id}:{workspace_id}"
        
        try:
            self.redis_client.delete(key)
            logger.debug(f"[REDIS_CONTEXT] Cleared context for {key}")
        except RedisConnectionError as e:
            logger.error(f"[REDIS_CONTEXT] Failed to clear context: {e}")
            raise ConnectionError(f"Redis delete failed: {e}")
    
    def get_all_keys(self) -> List[str]:
        """
        Get all active user+workspace keys (for debugging/monitoring).
        
        Returns:
            List of keys in format "context:{user_id}:{workspace_id}"
        
        Raises:
            ConnectionError: If Redis scan fails
        
        Use cases:
        - Monitoring: How many active conversations?
        - Debugging: Which users have context?
        - Cleanup: Identify stale sessions
        
        Examples:
            >>> cm = RedisContextManager("redis://localhost:6379/0")
            >>> # ... add entries for multiple users ...
            >>> keys = cm.get_all_keys()
            >>> print(f"Active conversations: {len(keys)}")
            >>> print(keys)  # ["context:user1:ws1", "context:user2:ws1", "context:user1:ws2"]
        
        Related:
        - Useful for: Monitoring, debugging, cleanup
        """
        try:
            keys = []
            # Use SCAN instead of KEYS for production-safe iteration
            for key in self.redis_client.scan_iter(match=self._keys_pattern):
                keys.append(key)
            return keys
        except RedisConnectionError as e:
            logger.error(f"[REDIS_CONTEXT] Failed to get all keys: {e}")
            raise ConnectionError(f"Redis scan failed: {e}")
    
    def health_check(self) -> bool:
        """
        Verify Redis connection is alive.
        
        Returns:
            True if Redis is reachable, False otherwise
        
        Use cases:
        - Application startup validation
        - Health check endpoints
        - Monitoring and alerting
        
        Examples:
            >>> cm = RedisContextManager("redis://localhost:6379/0")
            >>> if cm.health_check():
            ...     print("Redis is healthy")
            ... else:
            ...     print("Redis is down")
        
        Related:
        - Called by: app/main.py on startup
        - Used in: Health check endpoints
        """
        try:
            self.redis_client.ping()
            return True
        except (RedisConnectionError, Exception):
            return False

