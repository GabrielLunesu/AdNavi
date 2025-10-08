"""
Tests for Workspace Average Calculation

WHAT: Verify workspace_avg is calculated correctly (without query filters)
WHY: Ensure workspace comparison context is accurate
WHERE: Tests app/dsl/executor.py::_calculate_workspace_avg()

Critical test: workspace_avg should be different from summary when filters are applied
"""

import pytest
from datetime import date, timedelta
from sqlalchemy.orm import Session

from app.dsl.schema import MetricQuery, MetricResult, TimeRange, Filters
from app.dsl.planner import build_plan
from app.dsl.executor import execute_plan, _calculate_workspace_avg
from app import models


@pytest.fixture
def workspace_with_multi_provider_data(db: Session):
    """
    Create test data with multiple providers to test workspace avg.
    
    Setup:
    - 2 campaigns on Google (high ROAS)
    - 2 campaigns on Meta (low ROAS)
    - Overall workspace ROAS should be ~3.0
    - Google-only ROAS should be ~4.5
    - Meta-only ROAS should be ~1.5
    """
    workspace = models.Workspace(name="Test Workspace Avg")
    db.add(workspace)
    db.flush()
    
    # Google campaigns (high performers)
    google_campaign_1 = models.Entity(
        workspace_id=workspace.id,
        provider="google",
        level="campaign",
        name="Google Campaign 1",
        status="active"
    )
    google_campaign_2 = models.Entity(
        workspace_id=workspace.id,
        provider="google",
        level="campaign",
        name="Google Campaign 2",
        status="active"
    )
    
    # Meta campaigns (low performers)
    meta_campaign_1 = models.Entity(
        workspace_id=workspace.id,
        provider="meta",
        level="campaign",
        name="Meta Campaign 1",
        status="active"
    )
    meta_campaign_2 = models.Entity(
        workspace_id=workspace.id,
        provider="meta",
        level="campaign",
        name="Meta Campaign 2",
        status="active"
    )
    
    db.add_all([google_campaign_1, google_campaign_2, meta_campaign_1, meta_campaign_2])
    db.flush()
    
    # Add metrics data
    today = date.today()
    
    # Google: High ROAS (4.5× average)
    # Campaign 1: $1000 spend, $4500 revenue (4.5×)
    db.add(models.MetricFact(
        workspace_id=workspace.id,
        entity_id=google_campaign_1.id,
        provider="google",
        level="campaign",
        event_date=today - timedelta(days=15),
        spend=1000,
        revenue=4500,
        clicks=500,
        impressions=10000,
        conversions=50
    ))
    
    # Campaign 2: $1000 spend, $4500 revenue (4.5×)
    db.add(models.MetricFact(
        workspace_id=workspace.id,
        entity_id=google_campaign_2.id,
        provider="google",
        level="campaign",
        event_date=today - timedelta(days=15),
        spend=1000,
        revenue=4500,
        clicks=500,
        impressions=10000,
        conversions=50
    ))
    
    # Meta: Low ROAS (1.5× average)
    # Campaign 1: $1000 spend, $1500 revenue (1.5×)
    db.add(models.MetricFact(
        workspace_id=workspace.id,
        entity_id=meta_campaign_1.id,
        provider="meta",
        level="campaign",
        event_date=today - timedelta(days=15),
        spend=1000,
        revenue=1500,
        clicks=300,
        impressions=8000,
        conversions=30
    ))
    
    # Campaign 2: $1000 spend, $1500 revenue (1.5×)
    db.add(models.MetricFact(
        workspace_id=workspace.id,
        entity_id=meta_campaign_2.id,
        provider="meta",
        level="campaign",
        event_date=today - timedelta(days=15),
        spend=1000,
        revenue=1500,
        clicks=300,
        impressions=8000,
        conversions=30
    ))
    
    db.commit()
    
    return workspace


class TestWorkspaceAverageCalculation:
    """Tests for workspace average calculation."""
    
    def test_workspace_avg_ignores_provider_filter(self, db, workspace_with_multi_provider_data):
        """
        CRITICAL TEST: Workspace avg should be calculated across ALL providers,
        even when the main query filters to a specific provider.
        
        Setup:
        - Google ROAS: 4.5×
        - Meta ROAS: 1.5×
        - Overall workspace ROAS: 3.0×
        
        Test:
        - Query "What's my ROAS for Google campaigns?"
        - Summary should be 4.5× (Google only)
        - workspace_avg should be 3.0× (ALL providers)
        - Values should be DIFFERENT ✅
        """
        workspace = workspace_with_multi_provider_data
        
        # Query with Google filter
        query = MetricQuery(
            query_type="metrics",
            metric="roas",
            time_range=TimeRange(last_n_days=30),
            filters=Filters(provider="google")
        )
        
        plan = build_plan(query)
        result = execute_plan(db, str(workspace.id), plan, query)
        
        # Verify summary is Google-only ROAS (4.5×)
        assert result.summary == pytest.approx(4.5, rel=0.01), \
            f"Expected Google ROAS ~4.5×, got {result.summary}"
        
        # Verify workspace_avg is ALL providers (3.0×)
        assert result.workspace_avg is not None, "workspace_avg should not be None"
        assert result.workspace_avg == pytest.approx(3.0, rel=0.01), \
            f"Expected workspace avg ~3.0×, got {result.workspace_avg}"
        
        # CRITICAL: They should be DIFFERENT
        assert result.summary != result.workspace_avg, \
            "BUG: workspace_avg should differ from summary when filters are applied!"
        
        print(f"✅ Test passed: summary={result.summary:.2f}, workspace_avg={result.workspace_avg:.2f}")
    
    def test_workspace_avg_ignores_status_filter(self, db, workspace_with_multi_provider_data):
        """
        Test that workspace avg ignores status filter.
        
        Even if we query only active campaigns, workspace_avg should include
        both active and paused campaigns.
        """
        workspace = workspace_with_multi_provider_data
        
        # Pause one Meta campaign
        meta_campaign = db.query(models.Entity).filter(
            models.Entity.workspace_id == workspace.id,
            models.Entity.provider == "meta"
        ).first()
        meta_campaign.status = "paused"
        db.commit()
        
        # Query with active filter
        query = MetricQuery(
            query_type="metrics",
            metric="roas",
            time_range=TimeRange(last_n_days=30),
            filters=Filters(status="active")
        )
        
        plan = build_plan(query)
        result = execute_plan(db, str(workspace.id), plan, query)
        
        # workspace_avg should still include the paused campaign
        assert result.workspace_avg is not None
        # Should be close to 3.0 (includes all 4 campaigns, even paused one)
        assert result.workspace_avg == pytest.approx(3.0, rel=0.1)
    
    def test_workspace_avg_with_no_filters(self, db, workspace_with_multi_provider_data):
        """
        Test that workspace avg equals summary when no filters are applied.
        
        When querying the entire workspace, summary and workspace_avg should match.
        """
        workspace = workspace_with_multi_provider_data
        
        # Query with NO filters
        query = MetricQuery(
            query_type="metrics",
            metric="roas",
            time_range=TimeRange(last_n_days=30)
        )
        
        plan = build_plan(query)
        result = execute_plan(db, str(workspace.id), plan, query)
        
        # Both should be ~3.0× (entire workspace)
        assert result.summary == pytest.approx(3.0, rel=0.01)
        assert result.workspace_avg == pytest.approx(3.0, rel=0.01)
        
        # They should be equal (or very close) in this case
        assert abs(result.summary - result.workspace_avg) < 0.01, \
            "When no filters applied, summary and workspace_avg should match"
    
    def test_workspace_avg_helper_function_directly(self, db, workspace_with_multi_provider_data):
        """
        Test _calculate_workspace_avg() function directly.
        
        Verifies the helper function works correctly in isolation.
        """
        workspace = workspace_with_multi_provider_data
        
        time_range = TimeRange(last_n_days=30)
        
        # Calculate workspace average for ROAS
        workspace_avg = _calculate_workspace_avg(
            db=db,
            workspace_id=str(workspace.id),
            metric="roas",
            time_range=time_range
        )
        
        # Should be ~3.0× (average of all 4 campaigns)
        assert workspace_avg is not None
        assert workspace_avg == pytest.approx(3.0, rel=0.01), \
            f"Expected workspace avg ~3.0×, got {workspace_avg}"


class TestWorkspaceAvgEdgeCases:
    """Test edge cases for workspace average calculation."""
    
    def test_workspace_avg_with_zero_denominator(self, db, workspace_with_multi_provider_data):
        """
        Test that workspace avg handles divide-by-zero gracefully.
        
        If a metric can't be calculated (e.g., ROAS with $0 spend),
        should return None without crashing.
        """
        workspace = workspace_with_multi_provider_data
        
        # Delete all metric facts to create zero-spend scenario
        db.query(models.MetricFact).filter(
            models.MetricFact.workspace_id == workspace.id
        ).delete()
        db.commit()
        
        time_range = TimeRange(last_n_days=30)
        
        workspace_avg = _calculate_workspace_avg(
            db=db,
            workspace_id=str(workspace.id),
            metric="roas",
            time_range=time_range
        )
        
        # Should handle gracefully (return None)
        assert workspace_avg is None, "Should return None when no data available"
    
    def test_workspace_avg_with_unknown_metric(self, db, workspace_with_multi_provider_data):
        """
        Test that workspace avg handles unknown metrics gracefully.
        """
        workspace = workspace_with_multi_provider_data
        
        time_range = TimeRange(last_n_days=30)
        
        workspace_avg = _calculate_workspace_avg(
            db=db,
            workspace_id=str(workspace.id),
            metric="invalid_metric_xyz",
            time_range=time_range
        )
        
        # Should return None for unknown metric
        assert workspace_avg is None

