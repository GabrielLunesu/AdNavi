"""
Test suite for hierarchy-aware breakdown rollup functionality.

Tests:
1. Facts at ad level roll up to campaign level
2. Breakdown ordered by requested metric (not spend)
3. top_n=1 returns the correct top performer
4. Answer builder formats "which campaign had highest X" correctly

Related modules:
- app/dsl/hierarchy.py (CTE for ancestor resolution)
- app/dsl/executor.py (breakdown with hierarchy rollup)
- app/answer/answer_builder.py (top_n=1 special handling)
"""

import pytest
from decimal import Decimal
from datetime import date, timedelta
from sqlalchemy.orm import Session
from app import models
from app.dsl.schema import MetricQuery, MetricResult, TimeRange
from app.dsl.executor import execute_plan
from app.dsl.planner import build_plan
from app.answer.answer_builder import AnswerBuilder
from app.database import SessionLocal
import uuid


@pytest.fixture
def db():
    """Provide a test database session."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def hierarchy_test_data(db: Session):
    """
    Create test data with facts stored at ad level but with campaign hierarchy.
    
    Structure:
    - Workspace: test_workspace
    - Campaign A (ROAS: 3.0)
      - AdSet A1
        - Ad A1.1 (spend: 100, revenue: 200)
        - Ad A1.2 (spend: 100, revenue: 100)
    - Campaign B (ROAS: 2.0)
      - AdSet B1
        - Ad B1.1 (spend: 200, revenue: 400)
    
    Expected: Campaign A should have highest ROAS at 3.0
    """
    # Create workspace
    workspace = models.Workspace(
        id=str(uuid.uuid4()),
        name="Test Workspace"
    )
    db.add(workspace)
    
    # Create entities with hierarchy
    campaign_a = models.Entity(
        id=str(uuid.uuid4()),
        workspace_id=workspace.id,
        external_id="ext_campaign_a",
        name="Campaign A - High ROAS",
        level="campaign",
        status="active",
        goal=models.GoalEnum.conversions,
        parent_id=None
    )
    
    campaign_b = models.Entity(
        id=str(uuid.uuid4()),
        workspace_id=workspace.id,
        external_id="ext_campaign_b",
        name="Campaign B - Medium ROAS",
        level="campaign",
        status="active",
        goal=models.GoalEnum.conversions,
        parent_id=None
    )
    
    adset_a1 = models.Entity(
        id=str(uuid.uuid4()),
        workspace_id=workspace.id,
        external_id="ext_adset_a1",
        name="AdSet A1",
        level="adset",
        status="active",
        parent_id=campaign_a.id
    )
    
    adset_b1 = models.Entity(
        id=str(uuid.uuid4()),
        workspace_id=workspace.id,
        external_id="ext_adset_b1",
        name="AdSet B1",
        level="adset",
        status="active",
        parent_id=campaign_b.id
    )
    
    ad_a1_1 = models.Entity(
        id=str(uuid.uuid4()),
        workspace_id=workspace.id,
        external_id="ext_ad_a1_1",
        name="Ad A1.1",
        level="ad",
        status="active",
        parent_id=adset_a1.id
    )
    
    ad_a1_2 = models.Entity(
        id=str(uuid.uuid4()),
        workspace_id=workspace.id,
        external_id="ext_ad_a1_2",
        name="Ad A1.2",
        level="ad",
        status="active",
        parent_id=adset_a1.id
    )
    
    ad_b1_1 = models.Entity(
        id=str(uuid.uuid4()),
        workspace_id=workspace.id,
        external_id="ext_ad_b1_1",
        name="Ad B1.1",
        level="ad",
        status="active",
        parent_id=adset_b1.id
    )
    
    db.add_all([campaign_a, campaign_b, adset_a1, adset_b1, ad_a1_1, ad_a1_2, ad_b1_1])
    
    # Create metric facts at AD LEVEL ONLY (to test rollup)
    from datetime import datetime
    yesterday = date.today() - timedelta(days=1)
    yesterday_dt = datetime.combine(yesterday, datetime.min.time())
    
    # Campaign A ads (total: spend=200, revenue=300, ROAS=1.5)
    fact_a1_1 = models.MetricFact(
        id=str(uuid.uuid4()),
        entity_id=ad_a1_1.id,  # AD LEVEL
        provider="google",
        level="ad",
        event_at=yesterday_dt,
        event_date=yesterday,
        spend=Decimal("100"),
        revenue=Decimal("200"),  # ROAS = 2.0
        clicks=50,
        impressions=1000,
        conversions=10
    )
    
    fact_a1_2 = models.MetricFact(
        id=str(uuid.uuid4()),
        entity_id=ad_a1_2.id,  # AD LEVEL
        provider="google",
        level="ad",
        event_at=yesterday_dt,
        event_date=yesterday,
        spend=Decimal("100"),
        revenue=Decimal("100"),  # ROAS = 1.0
        clicks=40,
        impressions=800,
        conversions=5
    )
    
    # Campaign B ads (total: spend=200, revenue=400, ROAS=2.0)
    fact_b1_1 = models.MetricFact(
        id=str(uuid.uuid4()),
        entity_id=ad_b1_1.id,  # AD LEVEL
        provider="google",
        level="ad",
        event_at=yesterday_dt,
        event_date=yesterday,
        spend=Decimal("200"),
        revenue=Decimal("400"),  # ROAS = 2.0
        clicks=100,
        impressions=2000,
        conversions=20
    )
    
    db.add_all([fact_a1_1, fact_a1_2, fact_b1_1])
    db.commit()
    
    return {
        "workspace": workspace,
        "campaign_a": campaign_a,
        "campaign_b": campaign_b,
        "facts": [fact_a1_1, fact_a1_2, fact_b1_1]
    }


def test_campaign_rollup_from_ad_facts(db: Session, hierarchy_test_data):
    """
    Test that facts stored at ad level are correctly rolled up to campaign level.
    """
    workspace = hierarchy_test_data["workspace"]
    
    # Query for ROAS breakdown by campaign
    query = MetricQuery(
        metric="roas",
        time_range=TimeRange(last_n_days=7),
        compare_to_previous=False,
        group_by="campaign",
        breakdown="campaign",
        top_n=10,
        filters={}
    )
    
    # Build plan and execute
    plan = build_plan(query)
    result = execute_plan(plan, workspace.id, db)
    
    # Verify we got a breakdown
    assert result.breakdown is not None
    assert len(result.breakdown) == 2  # Two campaigns
    
    # Verify rollup worked correctly
    breakdown_by_name = {item["label"]: item["value"] for item in result.breakdown}
    
    # Campaign A: (200 + 100) / (100 + 100) = 300 / 200 = 1.5
    assert "Campaign A - High ROAS" in breakdown_by_name
    assert breakdown_by_name["Campaign A - High ROAS"] == pytest.approx(1.5, rel=0.01)
    
    # Campaign B: 400 / 200 = 2.0
    assert "Campaign B - Medium ROAS" in breakdown_by_name
    assert breakdown_by_name["Campaign B - Medium ROAS"] == pytest.approx(2.0, rel=0.01)


def test_breakdown_ordered_by_metric_not_spend(db: Session, hierarchy_test_data):
    """
    Test that breakdown is ordered by the requested metric (ROAS), not by spend.
    """
    workspace = hierarchy_test_data["workspace"]
    
    # Query for top campaign by ROAS
    query = MetricQuery(
        metric="roas",
        time_range=TimeRange(last_n_days=7),
        compare_to_previous=False,
        group_by="campaign",
        breakdown="campaign",
        top_n=10,
        filters={}
    )
    
    # Execute
    plan = build_plan(query)
    result = execute_plan(plan, workspace.id, db)
    
    # Verify ordering: Campaign B (ROAS=2.0) should be first, Campaign A (ROAS=1.5) second
    assert len(result.breakdown) == 2
    assert result.breakdown[0]["label"] == "Campaign B - Medium ROAS"
    assert result.breakdown[0]["value"] == pytest.approx(2.0, rel=0.01)
    assert result.breakdown[1]["label"] == "Campaign A - High ROAS"
    assert result.breakdown[1]["value"] == pytest.approx(1.5, rel=0.01)


def test_top_n_1_returns_single_best_performer(db: Session, hierarchy_test_data):
    """
    Test that top_n=1 returns only the single best performer.
    """
    workspace = hierarchy_test_data["workspace"]
    
    # Query for THE campaign with highest ROAS
    query = MetricQuery(
        metric="roas",
        time_range=TimeRange(last_n_days=7),
        compare_to_previous=False,
        group_by="campaign",
        breakdown="campaign",
        top_n=1,  # Only want the top one
        filters={}
    )
    
    # Execute
    plan = build_plan(query)
    result = execute_plan(plan, workspace.id, db)
    
    # Should only return Campaign B (highest ROAS at 2.0)
    assert len(result.breakdown) == 1
    assert result.breakdown[0]["label"] == "Campaign B - Medium ROAS"
    assert result.breakdown[0]["value"] == pytest.approx(2.0, rel=0.01)


def test_answer_builder_handles_top_n_1_correctly(db: Session, hierarchy_test_data):
    """
    Test that AnswerBuilder generates appropriate answer for "which campaign had highest X".
    """
    # Mock result for a top_n=1 query
    query = MetricQuery(
        metric="roas",
        time_range=TimeRange(last_n_days=7),
        compare_to_previous=False,
        group_by="campaign",
        breakdown="campaign",
        top_n=1,
        filters={}
    )
    
    result = MetricResult(
        summary=1.75,  # Overall ROAS
        previous=None,
        delta_pct=None,
        timeseries=[],
        breakdown=[
            {"label": "Summer Sale Campaign", "value": 3.2}
        ]
    )
    
    # Build answer (without actual LLM call for unit test)
    builder = AnswerBuilder()
    facts = builder._extract_metrics_facts(query, result)
    
    # Verify facts include special handling for top_n=1
    assert facts["query_intent"] == "highest_by_metric"
    assert facts["breakdown_level"] == "campaign"
    assert facts["metric_display"] == "ROAS"
    assert facts["top_performer"] == "Summer Sale Campaign"
    assert facts["top_performer_value_formatted"] == "3.20×"


def test_cpc_ordering_with_hierarchy(db: Session, hierarchy_test_data):
    """
    Test ordering by CPC (cost per click) with hierarchy rollup.
    """
    workspace = hierarchy_test_data["workspace"]
    
    # Query for campaigns by CPC (lowest is best)
    query = MetricQuery(
        metric="cpc",
        time_range=TimeRange(last_n_days=7),
        compare_to_previous=False,
        group_by="campaign",
        breakdown="campaign",
        top_n=10,
        filters={}
    )
    
    # Execute
    plan = build_plan(query)
    result = execute_plan(plan, workspace.id, db)
    
    # Calculate expected CPC values
    # Campaign A: spend=200, clicks=90, CPC=2.22
    # Campaign B: spend=200, clicks=100, CPC=2.00
    
    # Since we order DESC, higher CPC comes first
    assert len(result.breakdown) == 2
    assert result.breakdown[0]["value"] == pytest.approx(2.22, rel=0.01)  # Campaign A
    assert result.breakdown[1]["value"] == pytest.approx(2.00, rel=0.01)  # Campaign B


def test_empty_breakdown_when_no_data(db: Session):
    """
    Test that breakdown returns empty list when no data exists.
    """
    # Create empty workspace
    workspace = models.Workspace(
        id=str(uuid.uuid4()),
        name="Empty Workspace"
    )
    db.add(workspace)
    db.commit()
    
    # Query for breakdown
    query = MetricQuery(
        metric="roas",
        time_range=TimeRange(last_n_days=7),
        compare_to_previous=False,
        group_by="campaign",
        breakdown="campaign",
        top_n=10,
        filters={}
    )
    
    # Execute
    plan = build_plan(query)
    result = execute_plan(plan, workspace.id, db)
    
    # Should return empty breakdown, not error
    assert result.breakdown == []
    assert result.summary is None  # No data


def test_adset_level_breakdown(db: Session, hierarchy_test_data):
    """
    Test that adset-level breakdown also works with hierarchy.
    """
    workspace = hierarchy_test_data["workspace"]
    
    # Query for adset breakdown
    query = MetricQuery(
        metric="spend",
        time_range=TimeRange(last_n_days=7),
        compare_to_previous=False,
        group_by="adset",
        breakdown="adset",
        top_n=10,
        filters={}
    )
    
    # Execute
    plan = build_plan(query)
    result = execute_plan(plan, workspace.id, db)
    
    # Should roll up from ads to adsets
    assert len(result.breakdown) == 2  # Two adsets
    
    breakdown_by_name = {item["label"]: item["value"] for item in result.breakdown}
    
    # AdSet A1: 100 + 100 = 200
    assert "AdSet A1" in breakdown_by_name
    assert float(breakdown_by_name["AdSet A1"]) == 200.0
    
    # AdSet B1: 200
    assert "AdSet B1" in breakdown_by_name
    assert float(breakdown_by_name["AdSet B1"]) == 200.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
