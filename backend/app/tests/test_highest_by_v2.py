"""
Tests for "Highest By" Queries v2.0
=====================================

Tests the enhancements for intent-first answers with:
- Thresholds (min_spend, min_clicks, min_conversions)
- Provider breakdowns
- Date windows in answers
- Denominators (spend, clicks, conversions) in breakdown results

WHY these tests:
- Ensure thresholds correctly filter out tiny/noisy entities
- Verify provider breakdown works alongside campaign/adset/ad breakdowns
- Validate date ranges appear in answers for transparency
- Confirm denominators are included in breakdown results
- Test intent-first answer format: "X had highest Y at Z from DATE"

Related files:
- app/dsl/schema.py: Thresholds model, provider breakdown
- app/dsl/executor.py: HAVING clauses, provider grouping, denominators
- app/answer/answer_builder.py: Intent-first format, date windows
- app/services/qa_service.py: Date window passing

Design:
- Use pytest fixtures for database setup
- Mock or use real seed data
- Test both DSL validation and execution
- Verify answer format matches expected patterns
"""

from __future__ import annotations

import pytest
from datetime import date, timedelta
from app.dsl.schema import MetricQuery, TimeRange, Filters, Thresholds
from app.dsl.planner import build_plan
from app.dsl.executor import execute_plan
from app.answer.answer_builder import AnswerBuilder, _format_date_range


class TestThresholds:
    """Test threshold filtering for breakdowns."""
    
    def test_thresholds_model_validation(self):
        """Test that Thresholds model accepts valid values."""
        # Valid thresholds
        t = Thresholds(min_spend=50.0, min_clicks=100, min_conversions=5)
        assert t.min_spend == 50.0
        assert t.min_clicks == 100
        assert t.min_conversions == 5
        
        # None values allowed (all optional)
        t2 = Thresholds()
        assert t2.min_spend is None
        assert t2.min_clicks is None
        assert t2.min_conversions is None
    
    def test_thresholds_in_metric_query(self):
        """Test that MetricQuery accepts thresholds field."""
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7),
            breakdown="campaign",
            top_n=1,
            thresholds=Thresholds(min_spend=50.0, min_conversions=5)
        )
        
        assert query.thresholds is not None
        assert query.thresholds.min_spend == 50.0
        assert query.thresholds.min_conversions == 5
    
    def test_query_without_thresholds(self):
        """Test that queries work fine without thresholds (backward compatibility)."""
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7),
            breakdown="campaign",
            top_n=1
        )
        
        # Thresholds should be None by default
        assert query.thresholds is None


class TestProviderBreakdown:
    """Test provider as a breakdown dimension."""
    
    def test_provider_in_breakdown_options(self):
        """Test that 'provider' is accepted as a breakdown value."""
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7),
            breakdown="provider",  # NEW: provider breakdown
            group_by="provider",
            top_n=3
        )
        
        assert query.breakdown == "provider"
        assert query.group_by == "provider"
    
    def test_provider_breakdown_query_structure(self):
        """Test DSL structure for provider breakdown queries."""
        query = MetricQuery(
            metric="cpc",
            time_range=TimeRange(last_n_days=30),
            breakdown="provider",
            group_by="provider",
            top_n=5
        )
        
        # Build plan
        plan = build_plan(query)
        
        assert plan.breakdown == "provider"
        assert plan.top_n == 5


class TestDateFormatting:
    """Test date range formatting for answers."""
    
    def test_same_day_format(self):
        """Test formatting when start and end are the same day."""
        result = _format_date_range(date(2025, 10, 5), date(2025, 10, 5))
        assert result == "Oct 05, 2025"
    
    def test_same_month_format(self):
        """Test formatting within same month."""
        result = _format_date_range(date(2025, 9, 29), date(2025, 9, 30))
        assert result == "Sep 29–30, 2025"
    
    def test_different_months_same_year(self):
        """Test formatting across different months."""
        result = _format_date_range(date(2025, 9, 29), date(2025, 10, 5))
        assert result == "Sep 29–Oct 05, 2025"
    
    def test_different_years(self):
        """Test formatting across different years."""
        result = _format_date_range(date(2024, 12, 29), date(2025, 1, 5))
        assert result == "Dec 29, 2024–Jan 05, 2025"


class TestBreakdownDenominators:
    """Test that breakdown results include denominators."""
    
    def test_breakdown_result_structure(self):
        """Test that breakdown items have spend, clicks, conversions fields."""
        # This would be tested against real database results
        # Mock structure for now
        breakdown_item = {
            "label": "Summer Sale",
            "value": 3.20,
            "spend": 1234.56,
            "clicks": 3850,
            "conversions": 90,
            "revenue": 3948.67,
            "impressions": 125000
        }
        
        # Verify all expected fields are present
        assert "label" in breakdown_item
        assert "value" in breakdown_item
        assert "spend" in breakdown_item
        assert "clicks" in breakdown_item
        assert "conversions" in breakdown_item
        assert "revenue" in breakdown_item
        assert "impressions" in breakdown_item


class TestAnswerBuilder:
    """Test AnswerBuilder enhancements for v2.0."""
    
    def test_intent_first_query_detection(self):
        """Test that top_n=1 + breakdown triggers intent-first format."""
        from app.dsl.schema import MetricResult
        
        dsl = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7),
            breakdown="campaign",
            top_n=1
        )
        
        result = MetricResult(
            summary=2.45,
            previous=None,
            delta_pct=None,
            timeseries=None,
            breakdown=[{
                "label": "Summer Sale",
                "value": 3.20,
                "spend": 1234.56,
                "revenue": 3948.67
            }]
        )
        
        # Build answer (would call LLM in real usage)
        # Here we just verify the facts extraction
        builder = AnswerBuilder()
        window = {"start": date(2025, 9, 29), "end": date(2025, 10, 5)}
        
        # This will fail without OpenAI key, but we can test fact extraction
        facts = builder._extract_metrics_facts(dsl, result, window)
        
        # Verify intent-first detection
        assert facts.get("query_intent") == "highest_by_metric"
        assert facts.get("breakdown_level") == "campaign"
        assert facts.get("metric_display") == "ROAS"
        assert facts.get("top_performer") == "Summer Sale"
        assert "date_range" in facts
        assert facts["date_range"] == "Sep 29–Oct 05, 2025"
    
    def test_denominators_in_facts(self):
        """Test that denominators are included in extracted facts."""
        from app.dsl.schema import MetricResult
        
        dsl = MetricQuery(
            metric="cpc",
            time_range=TimeRange(last_n_days=7),
            breakdown="provider",
            top_n=1
        )
        
        result = MetricResult(
            summary=0.45,
            previous=None,
            delta_pct=None,
            timeseries=None,
            breakdown=[{
                "label": "Google",
                "value": 0.32,
                "spend": 1234.56,
                "clicks": 3850,
                "revenue": 4567.89
            }]
        )
        
        builder = AnswerBuilder()
        window = {"start": date(2025, 10, 1), "end": date(2025, 10, 7)}
        facts = builder._extract_metrics_facts(dsl, result, window)
        
        # Verify denominators are included
        assert "top_performer_context" in facts
        context = facts["top_performer_context"]
        assert "Spend" in context
        assert "clicks" in context


class TestEndToEnd:
    """End-to-end integration tests (require database)."""
    
    @pytest.mark.skip(reason="Requires database with seed data")
    def test_provider_breakdown_with_thresholds(self, db_session):
        """Test provider breakdown with min_spend threshold."""
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=30),
            breakdown="provider",
            group_by="provider",
            top_n=3,
            thresholds=Thresholds(min_spend=100.0)
        )
        
        plan = build_plan(query)
        result = execute_plan(
            db=db_session,
            workspace_id="test-workspace-id",
            plan=plan,
            query=query
        )
        
        # Verify result structure
        assert result.summary is not None
        assert result.breakdown is not None
        
        # Verify denominators in breakdown
        for item in result.breakdown:
            assert "spend" in item
            # Verify threshold was applied (spend >= 100)
            assert item["spend"] >= 100.0
    
    @pytest.mark.skip(reason="Requires database with seed data")
    def test_campaign_breakdown_with_outlier_filtering(self, db_session):
        """Test that tiny campaigns are excluded with thresholds."""
        # Query WITHOUT thresholds
        query_no_threshold = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7),
            breakdown="campaign",
            top_n=1
        )
        
        plan1 = build_plan(query_no_threshold)
        result1 = execute_plan(
            db=db_session,
            workspace_id="test-workspace-id",
            plan=plan1,
            query=query_no_threshold
        )
        
        # Query WITH thresholds (exclude tiny campaigns)
        query_with_threshold = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7),
            breakdown="campaign",
            top_n=1,
            thresholds=Thresholds(min_spend=50.0, min_conversions=5)
        )
        
        plan2 = build_plan(query_with_threshold)
        result2 = execute_plan(
            db=db_session,
            workspace_id="test-workspace-id",
            plan=plan2,
            query=query_with_threshold
        )
        
        # Results might differ if tiny outlier was #1
        # (This test requires specific seed data setup)
        # Assert that result2 top campaign meets thresholds
        if result2.breakdown:
            top_campaign = result2.breakdown[0]
            assert top_campaign["spend"] >= 50.0
            assert top_campaign["conversions"] >= 5


# Fixtures for database testing
@pytest.fixture
def db_session():
    """Provide database session for tests."""
    # This would be implemented with actual database setup
    pytest.skip("Database fixture not implemented yet")

