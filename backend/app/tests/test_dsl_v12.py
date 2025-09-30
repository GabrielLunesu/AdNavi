"""
Tests for DSL v1.2 Extensions
==============================

Tests for providers and entities query types.

Related files:
- app/dsl/schema.py: QueryType enum
- app/dsl/planner.py: Returns None for non-metrics queries
- app/dsl/executor.py: Executes providers and entities queries
"""

import pytest
from datetime import date, timedelta

from app.dsl.schema import MetricQuery, QueryType, Filters
from app.dsl.planner import build_plan
from app.dsl.executor import execute_plan
from app import models


# ============================================================================
# Fixtures
# ============================================================================

@pytest.fixture
def workspace(db):
    """
    Create a test workspace.
    
    Returns:
        Workspace: Test workspace with known ID
    """
    ws = models.Workspace(name="Test Workspace v1.2")
    db.add(ws)
    db.commit()
    db.refresh(ws)
    return ws


@pytest.fixture
def connections(db, workspace):
    """
    Create test connections (ad platform integrations).
    
    Creates connections for Google, Meta, and TikTok.
    
    Returns:
        list: List of Connection objects
    """
    conns = [
        models.Connection(
            workspace_id=workspace.id,
            provider="google",
            name="Google Ads",
            external_account_id="google-123"
        ),
        models.Connection(
            workspace_id=workspace.id,
            provider="meta",
            name="Meta Ads",
            external_account_id="meta-456"
        ),
        models.Connection(
            workspace_id=workspace.id,
            provider="tiktok",
            name="TikTok Ads",
            external_account_id="tiktok-789"
        ),
    ]
    for conn in conns:
        db.add(conn)
    db.commit()
    return conns


@pytest.fixture
def entities(db, workspace):
    """
    Create test entities (campaigns, adsets, ads).
    
    Creates a hierarchy:
    - 2 campaigns (1 active, 1 paused)
    - 3 adsets (2 active, 1 paused)
    - 4 ads (3 active, 1 paused)
    
    Returns:
        dict: Dict with lists of entities by level
    """
    entities = {
        "campaigns": [
            models.Entity(
                workspace_id=workspace.id,
                name="Summer Sale",
                level="campaign",
                status="active",
                provider="google",
                external_id="camp-1"
            ),
            models.Entity(
                workspace_id=workspace.id,
                name="Winter Promo",
                level="campaign",
                status="paused",
                provider="meta",
                external_id="camp-2"
            ),
        ],
        "adsets": [
            models.Entity(
                workspace_id=workspace.id,
                name="Adset A",
                level="adset",
                status="active",
                provider="google",
                external_id="adset-1"
            ),
            models.Entity(
                workspace_id=workspace.id,
                name="Adset B",
                level="adset",
                status="active",
                provider="meta",
                external_id="adset-2"
            ),
            models.Entity(
                workspace_id=workspace.id,
                name="Adset C",
                level="adset",
                status="paused",
                provider="tiktok",
                external_id="adset-3"
            ),
        ],
        "ads": [
            models.Entity(
                workspace_id=workspace.id,
                name="Ad 1",
                level="ad",
                status="active",
                provider="google",
                external_id="ad-1"
            ),
            models.Entity(
                workspace_id=workspace.id,
                name="Ad 2",
                level="ad",
                status="active",
                provider="meta",
                external_id="ad-2"
            ),
            models.Entity(
                workspace_id=workspace.id,
                name="Ad 3",
                level="ad",
                status="active",
                provider="tiktok",
                external_id="ad-3"
            ),
            models.Entity(
                workspace_id=workspace.id,
                name="Ad 4",
                level="ad",
                status="paused",
                provider="google",
                external_id="ad-4"
            ),
        ],
    }
    
    for entity_list in entities.values():
        for entity in entity_list:
            db.add(entity)
    
    db.commit()
    return entities


# ============================================================================
# Planner Tests
# ============================================================================

def test_planner_returns_none_for_providers_query():
    """
    Test that build_plan returns None for providers queries.
    
    Providers queries don't need a plan; they're handled directly in executor.
    """
    query = MetricQuery(query_type=QueryType.PROVIDERS)
    plan = build_plan(query)
    
    assert plan is None, "Planner should return None for providers queries"


def test_planner_returns_none_for_entities_query():
    """
    Test that build_plan returns None for entities queries.
    
    Entities queries don't need a plan; they're handled directly in executor.
    """
    query = MetricQuery(
        query_type=QueryType.ENTITIES,
        filters=Filters(level="campaign", status="active")
    )
    plan = build_plan(query)
    
    assert plan is None, "Planner should return None for entities queries"


def test_planner_returns_plan_for_metrics_query():
    """
    Test that build_plan returns a Plan for metrics queries.
    
    Metrics queries (v1.1 behavior) still need a plan.
    """
    query = MetricQuery(
        query_type=QueryType.METRICS,
        metric="roas"
    )
    plan = build_plan(query)
    
    assert plan is not None, "Planner should return Plan for metrics queries"
    assert plan.derived == "roas"
    assert plan.base_measures == ["revenue", "spend"]


# ============================================================================
# Executor Tests - Providers
# ============================================================================

def test_providers_query_returns_list(db, workspace, connections):
    """
    Test that providers query returns a list of distinct providers.
    
    Expected: ["google", "meta", "tiktok"]
    """
    query = MetricQuery(query_type=QueryType.PROVIDERS)
    result = execute_plan(db, str(workspace.id), plan=None, query=query)
    
    assert "providers" in result, "Result should have 'providers' key"
    assert isinstance(result["providers"], list), "Providers should be a list"
    
    # Check that we got all 3 providers
    providers = sorted(result["providers"])
    assert providers == ["google", "meta", "tiktok"]


def test_providers_query_empty_workspace(db, workspace):
    """
    Test providers query on workspace with no connections.
    
    Expected: Empty list
    """
    # No connections fixture, so workspace has no providers
    query = MetricQuery(query_type=QueryType.PROVIDERS)
    result = execute_plan(db, str(workspace.id), plan=None, query=query)
    
    assert result["providers"] == [], "Should return empty list for no connections"


# ============================================================================
# Executor Tests - Entities
# ============================================================================

def test_entities_query_all_entities(db, workspace, entities):
    """
    Test entities query without filters returns all entities.
    
    Expected: Returns entities up to top_n limit
    """
    query = MetricQuery(query_type=QueryType.ENTITIES, top_n=20)
    result = execute_plan(db, str(workspace.id), plan=None, query=query)
    
    assert "entities" in result, "Result should have 'entities' key"
    assert isinstance(result["entities"], list), "Entities should be a list"
    
    # We created 2 + 3 + 4 = 9 entities total
    assert len(result["entities"]) == 9
    
    # Each entity should have name, status, level
    for entity in result["entities"]:
        assert "name" in entity
        assert "status" in entity
        assert "level" in entity


def test_entities_query_filter_by_level(db, workspace, entities):
    """
    Test entities query filtered by level.
    
    Query: "List my campaigns"
    Expected: Only campaign-level entities
    """
    query = MetricQuery(
        query_type=QueryType.ENTITIES,
        filters=Filters(level="campaign"),
        top_n=10
    )
    result = execute_plan(db, str(workspace.id), plan=None, query=query)
    
    assert len(result["entities"]) == 2, "Should return 2 campaigns"
    
    # All should be campaign level
    for entity in result["entities"]:
        assert entity["level"] == "campaign"


def test_entities_query_filter_by_status(db, workspace, entities):
    """
    Test entities query filtered by status.
    
    Query: "List my active entities"
    Expected: Only active entities (6 total: 1 campaign + 2 adsets + 3 ads)
    """
    query = MetricQuery(
        query_type=QueryType.ENTITIES,
        filters=Filters(status="active"),
        top_n=20
    )
    result = execute_plan(db, str(workspace.id), plan=None, query=query)
    
    assert len(result["entities"]) == 6, "Should return 6 active entities"
    
    # All should be active
    for entity in result["entities"]:
        assert entity["status"] == "active"


def test_entities_query_filter_by_level_and_status(db, workspace, entities):
    """
    Test entities query with multiple filters.
    
    Query: "List my active campaigns"
    Expected: Only active campaigns (1 entity: "Summer Sale")
    """
    query = MetricQuery(
        query_type=QueryType.ENTITIES,
        filters=Filters(level="campaign", status="active"),
        top_n=10
    )
    result = execute_plan(db, str(workspace.id), plan=None, query=query)
    
    assert len(result["entities"]) == 1, "Should return 1 active campaign"
    assert result["entities"][0]["name"] == "Summer Sale"
    assert result["entities"][0]["level"] == "campaign"
    assert result["entities"][0]["status"] == "active"


def test_entities_query_respects_top_n(db, workspace, entities):
    """
    Test that entities query respects top_n limit.
    
    Query: "Show me top 2 ads"
    Expected: Only 2 entities returned
    """
    query = MetricQuery(
        query_type=QueryType.ENTITIES,
        filters=Filters(level="ad"),
        top_n=2
    )
    result = execute_plan(db, str(workspace.id), plan=None, query=query)
    
    # We have 4 ads, but top_n=2
    assert len(result["entities"]) == 2, "Should return only top_n entities"


def test_entities_query_empty_result(db, workspace, entities):
    """
    Test entities query with filters that match nothing.
    
    Query: "List my active campaigns" (but workspace has no active campaigns at account level)
    Expected: Empty list
    """
    query = MetricQuery(
        query_type=QueryType.ENTITIES,
        filters=Filters(level="account", status="active"),
        top_n=10
    )
    result = execute_plan(db, str(workspace.id), plan=None, query=query)
    
    assert result["entities"] == [], "Should return empty list for no matches"


# ============================================================================
# Integration Tests
# ============================================================================

def test_providers_query_workspace_isolation(db):
    """
    Test that providers queries are workspace-scoped.
    
    Create two workspaces with different providers and verify isolation.
    """
    # Workspace 1: Google, Meta
    ws1 = models.Workspace(name="Workspace 1")
    db.add(ws1)
    db.commit()
    db.refresh(ws1)
    
    conn1 = models.Connection(
        workspace_id=ws1.id,
        provider="google",
        name="Google",
        external_account_id="g1"
    )
    conn2 = models.Connection(
        workspace_id=ws1.id,
        provider="meta",
        name="Meta",
        external_account_id="m1"
    )
    db.add_all([conn1, conn2])
    
    # Workspace 2: TikTok
    ws2 = models.Workspace(name="Workspace 2")
    db.add(ws2)
    db.commit()
    db.refresh(ws2)
    
    conn3 = models.Connection(
        workspace_id=ws2.id,
        provider="tiktok",
        name="TikTok",
        external_account_id="t1"
    )
    db.add(conn3)
    db.commit()
    
    # Query workspace 1
    query = MetricQuery(query_type=QueryType.PROVIDERS)
    result1 = execute_plan(db, str(ws1.id), plan=None, query=query)
    
    # Query workspace 2
    result2 = execute_plan(db, str(ws2.id), plan=None, query=query)
    
    # Verify isolation
    assert sorted(result1["providers"]) == ["google", "meta"]
    assert result2["providers"] == ["tiktok"]


def test_entities_query_workspace_isolation(db):
    """
    Test that entities queries are workspace-scoped.
    
    Create two workspaces with different entities and verify isolation.
    """
    # Workspace 1: Campaign A
    ws1 = models.Workspace(name="Workspace 1")
    db.add(ws1)
    db.commit()
    db.refresh(ws1)
    
    entity1 = models.Entity(
        workspace_id=ws1.id,
        name="Campaign A",
        level="campaign",
        status="active",
        provider="google",
        external_id="a1"
    )
    db.add(entity1)
    
    # Workspace 2: Campaign B
    ws2 = models.Workspace(name="Workspace 2")
    db.add(ws2)
    db.commit()
    db.refresh(ws2)
    
    entity2 = models.Entity(
        workspace_id=ws2.id,
        name="Campaign B",
        level="campaign",
        status="active",
        provider="meta",
        external_id="b1"
    )
    db.add(entity2)
    db.commit()
    
    # Query workspace 1
    query = MetricQuery(
        query_type=QueryType.ENTITIES,
        filters=Filters(level="campaign")
    )
    result1 = execute_plan(db, str(ws1.id), plan=None, query=query)
    
    # Query workspace 2
    result2 = execute_plan(db, str(ws2.id), plan=None, query=query)
    
    # Verify isolation
    assert len(result1["entities"]) == 1
    assert result1["entities"][0]["name"] == "Campaign A"
    
    assert len(result2["entities"]) == 1
    assert result2["entities"][0]["name"] == "Campaign B"
