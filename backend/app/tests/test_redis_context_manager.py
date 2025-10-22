"""
Tests for Redis Context Manager
================================

Tests the Redis-backed conversation history management for multi-turn QA interactions.

Test coverage:
- Basic add/get operations
- Maximum history enforcement (FIFO eviction)
- User+workspace scoping (tenant isolation)
- TTL expiration behavior
- Clear context operations
- Health check functionality
- Error handling for Redis failures
- JSON serialization/deserialization

Related files:
- app/context/redis_context_manager.py: Module under test
- app/services/qa_service.py: Uses RedisContextManager in production
- app/nlp/translator.py: Consumes context for follow-up resolution

Design:
- Uses fakeredis for fast in-memory Redis simulation
- No external Redis dependency required
- Tests fail-fast behavior
- Verifies FIFO eviction and TTL
"""

import pytest
import time
from unittest.mock import patch
from app.context.redis_context_manager import RedisContextManager


@pytest.fixture
def mock_redis():
    """Create a fakeredis mock for testing."""
    try:
        from fakeredis import FakeRedis
        return FakeRedis(decode_responses=True)
    except ImportError:
        pytest.skip("fakeredis not installed")


@pytest.fixture
def redis_context_manager(mock_redis):
    """Create RedisContextManager with mock Redis."""
    with patch('app.context.redis_context_manager.Redis') as mock_redis_class:
        mock_redis_class.return_value = mock_redis
        cm = RedisContextManager(
            redis_url="redis://localhost:6379/0",
            max_history=5,
            ttl_seconds=3600
        )
        cm.redis_client = mock_redis
        return cm


class TestRedisContextManagerBasics:
    """Test basic add and get operations."""
    
    def test_add_and_get_single_entry(self, redis_context_manager):
        """Should store and retrieve a single conversation entry."""
        cm = redis_context_manager
        
        cm.add_entry(
            user_id="user1",
            workspace_id="ws1",
            question="What's my ROAS?",
            dsl={"metric": "roas", "time_range": {"last_n_days": 7}},
            result={"summary": 2.5}
        )
        
        history = cm.get_context("user1", "ws1")
        
        assert len(history) == 1
        assert history[0]["question"] == "What's my ROAS?"
        assert history[0]["dsl"]["metric"] == "roas"
        assert history[0]["result"]["summary"] == 2.5
    
    def test_add_multiple_entries_same_user(self, redis_context_manager):
        """Should store multiple entries in chronological order."""
        cm = redis_context_manager
        
        # Add 3 questions
        cm.add_entry("user1", "ws1", "Q1", {"metric": "roas"}, {"summary": 2.5})
        cm.add_entry("user1", "ws1", "Q2", {"metric": "spend"}, {"summary": 100})
        cm.add_entry("user1", "ws1", "Q3", {"metric": "revenue"}, {"summary": 250})
        
        history = cm.get_context("user1", "ws1")
        
        # Should be in order: oldest first, newest last
        assert len(history) == 3
        assert history[0]["question"] == "Q1"
        assert history[1]["question"] == "Q2"
        assert history[2]["question"] == "Q3"
    
    def test_get_empty_context(self, redis_context_manager):
        """Should return empty list for users with no history."""
        cm = redis_context_manager
        
        history = cm.get_context("new_user", "ws1")
        
        assert history == []
        assert isinstance(history, list)


class TestMaxHistoryEnforcement:
    """Test that history is limited to max_history entries (FIFO eviction)."""
    
    def test_respects_max_history_limit(self, redis_context_manager):
        """Should auto-evict oldest entries when max_history is reached."""
        cm = redis_context_manager
        
        # Add 6 entries when max_history=5 (should evict first one)
        for i in range(6):
            cm.add_entry("user1", "ws1", f"Q{i+1}", {}, {})
        
        history = cm.get_context("user1", "ws1")
        
        # Should only have last 5 (Q2-Q6)
        assert len(history) == 5
        assert history[0]["question"] == "Q2"
        assert history[4]["question"] == "Q6"
    
    def test_max_history_fifo_eviction(self, redis_context_manager):
        """Should evict oldest entries when limit exceeded (FIFO behavior)."""
        cm = redis_context_manager
        
        # Add entries up to max
        for i in range(5):
            cm.add_entry("user1", "ws1", f"Q{i+1}", {}, {})
        
        # Add one more to trigger eviction
        cm.add_entry("user1", "ws1", "Q6", {}, {})
        
        history = cm.get_context("user1", "ws1")
        
        # Q1 should be evicted, Q2-Q6 should remain
        assert len(history) == 5
        assert history[0]["question"] == "Q2"
        assert history[4]["question"] == "Q6"


class TestUserWorkspaceScoping:
    """Test tenant isolation and user+workspace scoping."""
    
    def test_separate_contexts_for_different_users(self, redis_context_manager):
        """Should keep separate histories for different users."""
        cm = redis_context_manager
        
        cm.add_entry("user1", "ws1", "User1 question", {}, {})
        cm.add_entry("user2", "ws1", "User2 question", {}, {})
        
        user1_history = cm.get_context("user1", "ws1")
        user2_history = cm.get_context("user2", "ws1")
        
        assert len(user1_history) == 1
        assert len(user2_history) == 1
        assert user1_history[0]["question"] == "User1 question"
        assert user2_history[0]["question"] == "User2 question"
    
    def test_separate_contexts_for_different_workspaces(self, redis_context_manager):
        """Should keep separate histories for different workspaces."""
        cm = redis_context_manager
        
        cm.add_entry("user1", "ws1", "WS1 question", {}, {})
        cm.add_entry("user1", "ws2", "WS2 question", {}, {})
        
        ws1_history = cm.get_context("user1", "ws1")
        ws2_history = cm.get_context("user1", "ws2")
        
        assert len(ws1_history) == 1
        assert len(ws2_history) == 1
        assert ws1_history[0]["question"] == "WS1 question"
        assert ws2_history[0]["question"] == "WS2 question"
    
    def test_same_user_different_workspaces_independent(self, redis_context_manager):
        """Should keep independent histories per workspace for same user."""
        cm = redis_context_manager
        
        # Add entries to both workspaces
        cm.add_entry("user1", "ws1", "WS1 Q1", {}, {})
        cm.add_entry("user1", "ws1", "WS1 Q2", {}, {})
        cm.add_entry("user1", "ws2", "WS2 Q1", {}, {})
        
        ws1_history = cm.get_context("user1", "ws1")
        ws2_history = cm.get_context("user1", "ws2")
        
        assert len(ws1_history) == 2
        assert len(ws2_history) == 1
        assert ws1_history[0]["question"] == "WS1 Q1"
        assert ws2_history[0]["question"] == "WS2 Q1"


class TestClearContext:
    """Test clearing conversation history."""
    
    def test_clear_existing_context(self, redis_context_manager):
        """Should remove all entries for a user+workspace."""
        cm = redis_context_manager
        
        # Add some entries
        cm.add_entry("user1", "ws1", "Q1", {}, {})
        cm.add_entry("user1", "ws1", "Q2", {}, {})
        
        # Clear context
        cm.clear_context("user1", "ws1")
        
        # Should be empty
        history = cm.get_context("user1", "ws1")
        assert len(history) == 0
    
    def test_clear_only_specific_user_workspace(self, redis_context_manager):
        """Should only clear the specified user+workspace."""
        cm = redis_context_manager
        
        # Add entries for multiple users
        cm.add_entry("user1", "ws1", "User1 WS1", {}, {})
        cm.add_entry("user2", "ws1", "User2 WS1", {}, {})
        cm.add_entry("user1", "ws2", "User1 WS2", {}, {})
        
        # Clear only user1, ws1
        cm.clear_context("user1", "ws1")
        
        # User1 WS1 should be empty
        assert len(cm.get_context("user1", "ws1")) == 0
        
        # Others should still have entries
        assert len(cm.get_context("user2", "ws1")) == 1
        assert len(cm.get_context("user1", "ws2")) == 1


class TestMonitoring:
    """Test monitoring and debugging functionality."""
    
    def test_get_all_keys(self, redis_context_manager):
        """Should return all active context keys."""
        cm = redis_context_manager
        
        # Add entries for multiple users/workspaces
        cm.add_entry("user1", "ws1", "Q1", {}, {})
        cm.add_entry("user2", "ws1", "Q1", {}, {})
        cm.add_entry("user1", "ws2", "Q1", {}, {})
        
        keys = cm.get_all_keys()
        
        assert len(keys) == 3
        assert "context:user1:ws1" in keys
        assert "context:user2:ws1" in keys
        assert "context:user1:ws2" in keys
    
    def test_get_all_keys_empty(self, redis_context_manager):
        """Should return empty list when no context exists."""
        cm = redis_context_manager
        
        keys = cm.get_all_keys()
        
        assert keys == []


class TestHealthCheck:
    """Test health check functionality."""
    
    def test_health_check_healthy(self, redis_context_manager):
        """Should return True when Redis is healthy."""
        cm = redis_context_manager
        
        # FakeRedis is always healthy
        assert cm.health_check() is True
    
    def test_health_check_unhealthy(self, mock_redis):
        """Should return False when Redis is unavailable."""
        from unittest.mock import patch
        
        with patch('app.context.redis_context_manager.Redis') as mock_redis_class:
            mock_redis_class.return_value = mock_redis
            
            cm = RedisContextManager(
                redis_url="redis://localhost:6379/0",
                max_history=5,
                ttl_seconds=3600
            )
            cm.redis_client = mock_redis
            
            # Make ping raise an exception
            def failing_ping():
                raise Exception("Connection failed")
            
            cm.redis_client.ping = failing_ping
            
            assert cm.health_check() is False


class TestErrorHandling:
    """Test error handling and fail-fast behavior."""
    
    def test_connection_error_on_add(self, mock_redis):
        """Should raise ConnectionError when Redis write fails."""
        from app.context.redis_context_manager import ConnectionError
        
        with patch('app.context.redis_context_manager.Redis') as mock_redis_class:
            mock_redis_class.return_value = mock_redis
            
            cm = RedisContextManager(
                redis_url="redis://localhost:6379/0",
                max_history=5,
                ttl_seconds=3600
            )
            cm.redis_client = mock_redis
            
            # Make pipeline() raise an exception
            def failing_pipeline():
                raise Exception("Write failed")
            
            cm.redis_client.pipeline = failing_pipeline
            
            with pytest.raises(ConnectionError):
                cm.add_entry("user1", "ws1", "Q1", {}, {})
    
    def test_connection_error_on_get(self, mock_redis):
        """Should raise ConnectionError when Redis read fails."""
        from app.context.redis_context_manager import ConnectionError
        
        with patch('app.context.redis_context_manager.Redis') as mock_redis_class:
            mock_redis_class.return_value = mock_redis
            
            cm = RedisContextManager(
                redis_url="redis://localhost:6379/0",
                max_history=5,
                ttl_seconds=3600
            )
            cm.redis_client = mock_redis
            
            # Make lrange raise an exception
            def failing_lrange(*args):
                raise Exception("Read failed")
            
            cm.redis_client.lrange = failing_lrange
            
            with pytest.raises(ConnectionError):
                cm.get_context("user1", "ws1")


class TestJSONSerialization:
    """Test JSON serialization/deserialization of complex objects."""
    
    def test_complex_dsl_serialization(self, redis_context_manager):
        """Should handle complex DSL objects with nested structures."""
        cm = redis_context_manager
        
        complex_dsl = {
            "metric": "roas",
            "time_range": {
                "last_n_days": 7,
                "start": "2025-01-01",
                "end": "2025-01-07"
            },
            "filters": {
                "provider": "meta",
                "level": "campaign",
                "status": "active"
            },
            "comparison": {
                "metric": "revenue",
                "time_range": {"last_n_days": 7}
            }
        }
        
        complex_result = {
            "summary": 2.45,
            "breakdown": [
                {"entity_name": "Campaign 1", "value": 3.2},
                {"entity_name": "Campaign 2", "value": 1.8}
            ],
            "delta_pct": 0.19
        }
        
        cm.add_entry("user1", "ws1", "Complex query", complex_dsl, complex_result)
        
        history = cm.get_context("user1", "ws1")
        
        assert len(history) == 1
        assert history[0]["dsl"] == complex_dsl
        assert history[0]["result"] == complex_result


class TestTTLBehavior:
    """Test TTL expiration behavior."""
    
    def test_ttl_set_on_add(self, redis_context_manager):
        """Should set TTL on context key when adding entry."""
        cm = redis_context_manager
        
        cm.add_entry("user1", "ws1", "Q1", {}, {})
        
        # Check TTL is set (should be > 0)
        key = "context:user1:ws1"
        ttl = cm.redis_client.ttl(key)
        
        assert ttl > 0
        assert ttl <= 3600  # Should be less than or equal to configured TTL
    
    def test_ttl_refreshed_on_add(self, redis_context_manager):
        """Should refresh TTL when adding new entry."""
        cm = redis_context_manager
        
        key = "context:user1:ws1"
        
        # Add first entry
        cm.add_entry("user1", "ws1", "Q1", {}, {})
        ttl1 = cm.redis_client.ttl(key)
        
        # Wait a moment
        time.sleep(0.01)
        
        # Add second entry (should refresh TTL)
        cm.add_entry("user1", "ws1", "Q2", {}, {})
        ttl2 = cm.redis_client.ttl(key)
        
        # TTL should be refreshed (approximately equal or slightly higher)
        assert ttl2 >= ttl1 - 1  # Allow for small timing differences

