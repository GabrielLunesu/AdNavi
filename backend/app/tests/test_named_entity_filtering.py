"""
Unit tests for named entity filtering feature.

Tests the new entity_name filter added in Phase 5.

WHY this test file exists:
- Validates case-insensitive partial matching for entity names
- Ensures entity_name filter works with metrics and entities queries
- Tests combination of entity_name with other filters

Related files:
- app/dsl/schema.py: Filters.entity_name field
- app/dsl/executor.py: .ilike() filtering logic
- app/nlp/prompts.py: Few-shot examples for entity_name
"""

import pytest
from datetime import datetime, timedelta
from app.dsl.schema import MetricQuery, TimeRange, Filters, QueryType
from app.dsl.executor import execute_plan
from app.dsl.planner import build_plan
from app.database import SessionLocal
from app import models
from uuid import uuid4


@pytest.fixture
def db():
    """Create a test database session."""
    db = SessionLocal()
    yield db
    db.close()


@pytest.fixture
def test_workspace(db):
    """Create a test workspace with campaigns for name filtering."""
    # Clean up in correct foreign key order (reverse dependency order)
    db.query(models.Pnl).delete()  
    db.query(models.ComputeRun).delete()
    db.query(models.MetricFact).delete()
    db.query(models.Import).delete()  # NEW: Must delete before Fetch
    db.query(models.Fetch).delete()   # NEW: Must delete before Connection
    db.query(models.Entity).delete()
    db.query(models.Connection).delete()
    db.query(models.QaQueryLog).delete()  # NEW
    db.query(models.AuthCredential).delete()  # NEW
    db.query(models.User).delete()
    db.query(models.Token).delete()  # NEW
    db.query(models.Workspace).delete()
    db.commit()
    
    # Create workspace
    workspace = models.Workspace(id=uuid4(), name="Test Workspace")
    db.add(workspace)
    db.flush()
    
    # Create connection
    connection = models.Connection(
        id=uuid4(),
        workspace_id=workspace.id,
        provider=models.ProviderEnum.meta,
        external_account_id="TEST-123",
        name="Test Connection",
        status="active"
    )
    db.add(connection)
    db.flush()
    
    # Create Fetch and Import (required for MetricFacts)
    fetch = models.Fetch(
        id=uuid4(),
        connection_id=connection.id,
        kind="test",
        status="completed",
        started_at=datetime.utcnow(),
        finished_at=datetime.utcnow(),
        range_start=datetime.utcnow() - timedelta(days=7),
        range_end=datetime.utcnow()
    )
    db.add(fetch)
    db.flush()
    
    import_record = models.Import(
        id=uuid4(),
        fetch_id=fetch.id,
        as_of=datetime.utcnow(),
        created_at=datetime.utcnow(),
        note="Test import for name filtering"
    )
    db.add(import_record)
    db.flush()
    
    # Create campaigns with different names for testing
    campaigns = [
        models.Entity(
            id=uuid4(),
            workspace_id=workspace.id,
            connection_id=connection.id,
            level=models.LevelEnum.campaign,
            external_id="CAMP-001",
            name="Holiday Sale - Purchases",  # Match: "holiday", "Holiday Sale", "sale"
            status="active",
            goal=models.GoalEnum.purchases
        ),
        models.Entity(
            id=uuid4(),
            workspace_id=workspace.id,
            connection_id=connection.id,
            level=models.LevelEnum.campaign,
            external_id="CAMP-002",
            name="Summer Sale Campaign",  # Match: "summer", "Sale", "summer sale"
            status="active",
            goal=models.GoalEnum.purchases
        ),
        models.Entity(
            id=uuid4(),
            workspace_id=workspace.id,
            connection_id=connection.id,
            level=models.LevelEnum.campaign,
            external_id="CAMP-003",
            name="Lead Gen - B2B",  # Match: "lead", "Lead Gen", "b2b"
            status="active",
            goal=models.GoalEnum.leads
        ),
        models.Entity(
            id=uuid4(),
            workspace_id=workspace.id,
            connection_id=connection.id,
            level=models.LevelEnum.campaign,
            external_id="CAMP-004",
            name="Brand Awareness",  # Match: "brand", "awareness"
            status="active",
            goal=models.GoalEnum.awareness
        ),
    ]
    
    for campaign in campaigns:
        db.add(campaign)
    db.flush()
    
    # Add metric facts for testing
    today = datetime.utcnow().date()
    for campaign in campaigns:
        for day_offset in range(7):
            event_date = today - timedelta(days=day_offset)
            fact = models.MetricFact(
                id=uuid4(),
                entity_id=campaign.id,
                provider=connection.provider,
                level=models.LevelEnum.campaign,
                event_at=datetime.combine(event_date, datetime.min.time()),
                event_date=datetime.combine(event_date, datetime.min.time()),
                spend=100.0,
                revenue=500.0,
                clicks=1000,
                impressions=10000,
                conversions=50,
                currency="USD",
                natural_key=f"{campaign.id}-{event_date}",  # Required field
                ingested_at=datetime.utcnow(),
                import_id=import_record.id  # Required foreign key
            )
            db.add(fact)
    
    db.commit()
    
    return {
        "workspace_id": str(workspace.id),
        "campaigns": campaigns,
        "import_id": str(import_record.id)
    }


def test_entity_name_exact_match(db, test_workspace):
    """Test exact entity name matching."""
    query = MetricQuery(
        query_type=QueryType.ENTITIES,
        filters=Filters(
            level="campaign",
            entity_name="Holiday Sale - Purchases"  # Exact match
        ),
        top_n=10
    )
    
    # Entities queries don't need a plan
    result = execute_plan(db, test_workspace["workspace_id"], plan=None, query=query)
    
    assert "entities" in result
    assert len(result["entities"]) == 1
    assert result["entities"][0]["name"] == "Holiday Sale - Purchases"


def test_entity_name_partial_match(db, test_workspace):
    """Test partial name matching - 'Sale' should match multiple campaigns."""
    query = MetricQuery(
        query_type=QueryType.ENTITIES,
        filters=Filters(
            level="campaign",
            entity_name="Sale"  # Should match "Holiday Sale" and "Summer Sale"
        ),
        top_n=10
    )
    
    result = execute_plan(db, test_workspace["workspace_id"], plan=None, query=query)
    
    assert "entities" in result
    assert len(result["entities"]) == 2
    names = [e["name"] for e in result["entities"]]
    assert "Holiday Sale - Purchases" in names
    assert "Summer Sale Campaign" in names


def test_entity_name_case_insensitive(db, test_workspace):
    """Test case-insensitive matching."""
    query = MetricQuery(
        query_type=QueryType.ENTITIES,
        filters=Filters(
            level="campaign",
            entity_name="HOLIDAY SALE"  # Uppercase should still match
        ),
        top_n=10
    )
    
    result = execute_plan(db, test_workspace["workspace_id"], plan=None, query=query)
    
    assert "entities" in result
    assert len(result["entities"]) == 1
    assert result["entities"][0]["name"] == "Holiday Sale - Purchases"


def test_entity_name_with_metrics_query(db, test_workspace):
    """Test entity_name filter in metrics queries."""
    query = MetricQuery(
        query_type=QueryType.METRICS,
        metric="revenue",
        time_range=TimeRange(last_n_days=7),
        filters=Filters(
            level="campaign",
            entity_name="Holiday Sale"
        )
    )
    
    # Metrics queries need a plan
    plan = build_plan(query)
    result = execute_plan(db, test_workspace["workspace_id"], plan=plan, query=query)
    
    # Should aggregate revenue for only Holiday Sale campaign
    assert result.summary is not None
    # With 7 days × $500 revenue = $3,500 (but may vary based on date range)
    assert result.summary >= 3000.0  # At least 6 days
    assert result.summary <= 3500.0  # At most 7 days


def test_entity_name_with_breakdown(db, test_workspace):
    """Test entity_name filter with breakdown."""
    query = MetricQuery(
        query_type=QueryType.METRICS,
        metric="revenue",
        time_range=TimeRange(last_n_days=7),
        breakdown="campaign",
        group_by="campaign",
        filters=Filters(
            entity_name="Sale"  # Should match both "Sale" campaigns
        ),
        top_n=10
    )
    
    plan = build_plan(query)
    result = execute_plan(db, test_workspace["workspace_id"], plan=plan, query=query)
    
    assert result.breakdown is not None
    assert len(result.breakdown) == 2
    names = [item["label"] for item in result.breakdown]
    assert "Holiday Sale - Purchases" in names
    assert "Summer Sale Campaign" in names


def test_entity_name_no_match(db, test_workspace):
    """Test entity_name with no matches returns empty."""
    query = MetricQuery(
        query_type=QueryType.ENTITIES,
        filters=Filters(
            level="campaign",
            entity_name="Nonexistent Campaign"
        ),
        top_n=10
    )
    
    result = execute_plan(db, test_workspace["workspace_id"], plan=None, query=query)
    
    assert "entities" in result
    assert len(result["entities"]) == 0


def test_entity_name_combined_with_status_filter(db, test_workspace):
    """Test entity_name combined with other filters."""
    query = MetricQuery(
        query_type=QueryType.ENTITIES,
        filters=Filters(
            level="campaign",
            status="active",
            entity_name="Sale"  # Should match only active Sale campaigns
        ),
        top_n=10
    )
    
    result = execute_plan(db, test_workspace["workspace_id"], plan=None, query=query)
    
    assert "entities" in result
    assert len(result["entities"]) == 2
    # Both Sale campaigns are active
    for entity in result["entities"]:
        assert entity["status"] == "active"
        assert "Sale" in entity["name"]


def test_entity_name_lowercase_match(db, test_workspace):
    """Test lowercase pattern matches."""
    query = MetricQuery(
        query_type=QueryType.ENTITIES,
        filters=Filters(
            level="campaign",
            entity_name="holiday"  # Lowercase
        ),
        top_n=10
    )
    
    result = execute_plan(db, test_workspace["workspace_id"], plan=None, query=query)
    
    assert "entities" in result
    assert len(result["entities"]) == 1
    assert result["entities"][0]["name"] == "Holiday Sale - Purchases"


def test_entity_name_single_word_match(db, test_workspace):
    """Test single word matching."""
    query = MetricQuery(
        query_type=QueryType.ENTITIES,
        filters=Filters(
            level="campaign",
            entity_name="brand"  # Should match "Brand Awareness"
        ),
        top_n=10
    )
    
    result = execute_plan(db, test_workspace["workspace_id"], plan=None, query=query)
    
    assert "entities" in result
    assert len(result["entities"]) == 1
    assert result["entities"][0]["name"] == "Brand Awareness"

