"""
Tests for Context Manager
===========================

Tests the conversation history management for multi-turn QA interactions.

Test coverage:
- Basic add/get operations
- Maximum history enforcement (FIFO eviction)
- User+workspace scoping (tenant isolation)
- Thread safety (concurrent operations)
- Clear context operations
- Edge cases (empty history, missing keys)

Related files:
- app/context/context_manager.py: Module under test
- app/services/qa_service.py: Uses ContextManager in production
- app/nlp/translator.py: Consumes context for follow-up resolution

Design:
- Pure unit tests (no database, no HTTP)
- Fast execution (<100ms total)
- Clear test names describing behavior
- Comprehensive edge case coverage
"""

import pytest
from threading import Thread
from app.context.context_manager import ContextManager


class TestContextManagerBasics:
    """Test basic add and get operations."""
    
    def test_add_and_get_single_entry(self):
        """Should store and retrieve a single conversation entry."""
        cm = ContextManager(max_history=5)
        
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
    
    def test_add_multiple_entries_same_user(self):
        """Should store multiple entries in chronological order."""
        cm = ContextManager(max_history=5)
        
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
    
    def test_get_empty_context(self):
        """Should return empty list for users with no history."""
        cm = ContextManager()
        
        history = cm.get_context("new_user", "ws1")
        
        assert history == []
        assert isinstance(history, list)


class TestMaxHistoryEnforcement:
    """Test that history is limited to max_history entries (FIFO eviction)."""
    
    def test_respects_max_history_limit(self):
        """Should auto-evict oldest entries when max_history is reached."""
        cm = ContextManager(max_history=2)  # Only keep last 2
        
        # Add 3 entries (should evict the first one)
        cm.add_entry("user1", "ws1", "Q1", {}, {})
        cm.add_entry("user1", "ws1", "Q2", {}, {})
        cm.add_entry("user1", "ws1", "Q3", {}, {})
        
        history = cm.get_context("user1", "ws1")
        
        # Should only have last 2 (Q2, Q3)
        assert len(history) == 2
        assert history[0]["question"] == "Q2"
        assert history[1]["question"] == "Q3"
    
    def test_max_history_fifo_eviction(self):
        """Should evict in FIFO order (oldest first)."""
        cm = ContextManager(max_history=3)
        
        # Add 5 entries
        for i in range(1, 6):
            cm.add_entry("user1", "ws1", f"Q{i}", {}, {})
        
        history = cm.get_context("user1", "ws1")
        
        # Should only have last 3 (Q3, Q4, Q5)
        assert len(history) == 3
        assert history[0]["question"] == "Q3"
        assert history[1]["question"] == "Q4"
        assert history[2]["question"] == "Q5"
    
    def test_custom_max_history(self):
        """Should respect custom max_history value."""
        cm = ContextManager(max_history=10)
        
        # Add 12 entries
        for i in range(1, 13):
            cm.add_entry("user1", "ws1", f"Q{i}", {}, {})
        
        history = cm.get_context("user1", "ws1")
        
        # Should only have last 10
        assert len(history) == 10
        assert history[0]["question"] == "Q3"  # Oldest of the 10
        assert history[-1]["question"] == "Q12"  # Newest


class TestUserWorkspaceScoping:
    """Test that context is properly scoped per user+workspace (tenant isolation)."""
    
    def test_different_users_separate_contexts(self):
        """Should isolate context between different users in same workspace."""
        cm = ContextManager()
        
        cm.add_entry("user1", "ws1", "User1 Question", {}, {})
        cm.add_entry("user2", "ws1", "User2 Question", {}, {})
        
        user1_history = cm.get_context("user1", "ws1")
        user2_history = cm.get_context("user2", "ws1")
        
        assert len(user1_history) == 1
        assert len(user2_history) == 1
        assert user1_history[0]["question"] == "User1 Question"
        assert user2_history[0]["question"] == "User2 Question"
    
    def test_different_workspaces_separate_contexts(self):
        """Should isolate context between different workspaces for same user."""
        cm = ContextManager()
        
        cm.add_entry("user1", "ws1", "Workspace1 Question", {}, {})
        cm.add_entry("user1", "ws2", "Workspace2 Question", {}, {})
        
        ws1_history = cm.get_context("user1", "ws1")
        ws2_history = cm.get_context("user1", "ws2")
        
        assert len(ws1_history) == 1
        assert len(ws2_history) == 1
        assert ws1_history[0]["question"] == "Workspace1 Question"
        assert ws2_history[0]["question"] == "Workspace2 Question"
    
    def test_no_cross_tenant_leaks(self):
        """Should never leak context across user+workspace boundaries."""
        cm = ContextManager()
        
        # Add entries for multiple user+workspace combinations
        cm.add_entry("user1", "ws1", "U1W1", {}, {})
        cm.add_entry("user1", "ws2", "U1W2", {}, {})
        cm.add_entry("user2", "ws1", "U2W1", {}, {})
        cm.add_entry("user2", "ws2", "U2W2", {}, {})
        
        # Each combination should only see its own context
        assert cm.get_context("user1", "ws1")[0]["question"] == "U1W1"
        assert cm.get_context("user1", "ws2")[0]["question"] == "U1W2"
        assert cm.get_context("user2", "ws1")[0]["question"] == "U2W1"
        assert cm.get_context("user2", "ws2")[0]["question"] == "U2W2"


class TestClearContext:
    """Test context clearing operations."""
    
    def test_clear_context_removes_history(self):
        """Should remove all history for a specific user+workspace."""
        cm = ContextManager()
        
        cm.add_entry("user1", "ws1", "Q1", {}, {})
        cm.add_entry("user1", "ws1", "Q2", {}, {})
        
        # Verify history exists
        assert len(cm.get_context("user1", "ws1")) == 2
        
        # Clear context
        cm.clear_context("user1", "ws1")
        
        # History should be empty
        assert cm.get_context("user1", "ws1") == []
    
    def test_clear_context_only_affects_target(self):
        """Should only clear the specified user+workspace, not others."""
        cm = ContextManager()
        
        cm.add_entry("user1", "ws1", "U1W1", {}, {})
        cm.add_entry("user1", "ws2", "U1W2", {}, {})
        cm.add_entry("user2", "ws1", "U2W1", {}, {})
        
        # Clear only user1+ws1
        cm.clear_context("user1", "ws1")
        
        # user1+ws1 should be empty
        assert cm.get_context("user1", "ws1") == []
        
        # Others should still have their history
        assert len(cm.get_context("user1", "ws2")) == 1
        assert len(cm.get_context("user2", "ws1")) == 1
    
    def test_clear_nonexistent_context(self):
        """Should handle clearing context that doesn't exist gracefully."""
        cm = ContextManager()
        
        # Should not raise an error
        cm.clear_context("nonexistent_user", "nonexistent_ws")
        
        # Should still return empty list
        assert cm.get_context("nonexistent_user", "nonexistent_ws") == []


class TestGetAllKeys:
    """Test monitoring/debugging helper methods."""
    
    def test_get_all_keys_empty(self):
        """Should return empty list when no conversations exist."""
        cm = ContextManager()
        
        keys = cm.get_all_keys()
        
        assert keys == []
    
    def test_get_all_keys_with_entries(self):
        """Should return all active user+workspace keys."""
        cm = ContextManager()
        
        cm.add_entry("user1", "ws1", "Q1", {}, {})
        cm.add_entry("user1", "ws2", "Q2", {}, {})
        cm.add_entry("user2", "ws1", "Q3", {}, {})
        
        keys = cm.get_all_keys()
        
        assert len(keys) == 3
        assert "user1:ws1" in keys
        assert "user1:ws2" in keys
        assert "user2:ws1" in keys
    
    def test_get_all_keys_after_clear(self):
        """Should not include cleared contexts in keys list."""
        cm = ContextManager()
        
        cm.add_entry("user1", "ws1", "Q1", {}, {})
        cm.add_entry("user2", "ws1", "Q2", {}, {})
        
        # Clear one context
        cm.clear_context("user1", "ws1")
        
        keys = cm.get_all_keys()
        
        # Only user2:ws1 should remain
        assert len(keys) == 1
        assert "user2:ws1" in keys
        assert "user1:ws1" not in keys


class TestThreadSafety:
    """Test that ContextManager is thread-safe for concurrent access."""
    
    def test_concurrent_writes(self):
        """Should handle concurrent writes from multiple threads safely."""
        cm = ContextManager()
        
        def add_entries(user_id, count):
            for i in range(count):
                cm.add_entry(user_id, "ws1", f"Q{i}", {}, {})
        
        # Create multiple threads adding entries concurrently
        threads = [
            Thread(target=add_entries, args=(f"user{i}", 10))
            for i in range(5)
        ]
        
        # Start all threads
        for t in threads:
            t.start()
        
        # Wait for all threads to complete
        for t in threads:
            t.join()
        
        # Verify all entries were added correctly
        for i in range(5):
            history = cm.get_context(f"user{i}", "ws1")
            # Should have 10 entries (within max_history default of 5, so actually 5)
            assert len(history) == 5  # Limited by default max_history
    
    def test_concurrent_read_write(self):
        """Should handle concurrent reads and writes safely."""
        cm = ContextManager()
        
        # Pre-populate some context
        cm.add_entry("user1", "ws1", "Initial", {}, {})
        
        results = []
        
        def read_context():
            for _ in range(100):
                history = cm.get_context("user1", "ws1")
                results.append(len(history))
        
        def write_context():
            for i in range(50):
                cm.add_entry("user1", "ws1", f"Q{i}", {}, {})
        
        # Create reader and writer threads
        reader = Thread(target=read_context)
        writer = Thread(target=write_context)
        
        # Start both
        reader.start()
        writer.start()
        
        # Wait for completion
        reader.join()
        writer.join()
        
        # All reads should have succeeded (no crashes)
        assert len(results) == 100
        # All results should be valid lengths (1-5, given max_history=5)
        assert all(1 <= r <= 5 for r in results)


class TestEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_anonymous_user_context(self):
        """Should handle 'anon' user ID for unauthenticated sessions."""
        cm = ContextManager()
        
        cm.add_entry("anon", "ws1", "Anonymous question", {}, {})
        
        history = cm.get_context("anon", "ws1")
        
        assert len(history) == 1
        assert history[0]["question"] == "Anonymous question"
    
    def test_empty_question(self):
        """Should handle empty question strings."""
        cm = ContextManager()
        
        cm.add_entry("user1", "ws1", "", {}, {})
        
        history = cm.get_context("user1", "ws1")
        
        assert len(history) == 1
        assert history[0]["question"] == ""
    
    def test_empty_dsl_and_result(self):
        """Should handle empty dsl and result dicts."""
        cm = ContextManager()
        
        cm.add_entry("user1", "ws1", "Question", {}, {})
        
        history = cm.get_context("user1", "ws1")
        
        assert len(history) == 1
        assert history[0]["dsl"] == {}
        assert history[0]["result"] == {}
    
    def test_complex_result_structures(self):
        """Should handle complex nested result structures."""
        cm = ContextManager()
        
        complex_result = {
            "summary": 2.5,
            "previous": 2.1,
            "delta_pct": 0.19,
            "timeseries": [
                {"date": "2025-09-01", "value": 2.3},
                {"date": "2025-09-02", "value": 2.5}
            ],
            "breakdown": [
                {"label": "Campaign A", "value": 3.2},
                {"label": "Campaign B", "value": 2.8}
            ]
        }
        
        cm.add_entry("user1", "ws1", "Question", {}, complex_result)
        
        history = cm.get_context("user1", "ws1")
        
        # Should preserve entire structure
        assert history[0]["result"] == complex_result
        assert len(history[0]["result"]["timeseries"]) == 2
        assert len(history[0]["result"]["breakdown"]) == 2


class TestIntegrationScenarios:
    """Test realistic multi-turn conversation scenarios."""
    
    def test_follow_up_question_scenario(self):
        """Simulate a real follow-up question conversation."""
        cm = ContextManager()
        
        # User asks initial question
        cm.add_entry(
            "user1", "ws1",
            "What's my ROAS this week?",
            {"metric": "roas", "time_range": {"last_n_days": 7}},
            {"summary": 2.45, "delta_pct": 0.19}
        )
        
        # User asks follow-up
        cm.add_entry(
            "user1", "ws1",
            "And yesterday?",
            {"metric": "roas", "time_range": {"last_n_days": 1}},
            {"summary": 2.30}
        )
        
        history = cm.get_context("user1", "ws1")
        
        # Should have both questions in order
        assert len(history) == 2
        assert "this week" in history[0]["question"]
        assert "yesterday" in history[1]["question"]
        
        # Latest context should reference ROAS
        assert history[0]["dsl"]["metric"] == "roas"
        assert history[1]["dsl"]["metric"] == "roas"
    
    def test_campaign_breakdown_follow_up(self):
        """Simulate asking for breakdown then asking 'which one performed best'."""
        cm = ContextManager()
        
        # Initial: Show me campaigns
        cm.add_entry(
            "user1", "ws1",
            "Show me ROAS by campaign",
            {"metric": "roas", "breakdown": "campaign", "top_n": 10},
            {
                "summary": 2.45,
                "breakdown": [
                    {"label": "Summer Sale", "value": 3.2},
                    {"label": "Winter Promo", "value": 2.8},
                    {"label": "Spring Launch", "value": 2.1}
                ]
            }
        )
        
        # Follow-up: Which one performed best?
        # (Would need translator to resolve "which one" to top from breakdown)
        cm.add_entry(
            "user1", "ws1",
            "Which one performed best?",
            {"query_type": "entities", "filters": {"level": "campaign"}, "top_n": 1},
            {"entities": [{"name": "Summer Sale", "status": "active"}]}
        )
        
        history = cm.get_context("user1", "ws1")
        
        # Context should include the breakdown for resolution
        assert len(history) == 2
        assert len(history[0]["result"]["breakdown"]) == 3
        assert history[0]["result"]["breakdown"][0]["label"] == "Summer Sale"

