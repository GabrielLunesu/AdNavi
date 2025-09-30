"""
DSL Executor Tests
==================

Test query execution with seed data.

Tests:
- Base metrics (spend, revenue, clicks, etc.)
- Derived metrics (roas, cpa, cvr) with divide-by-zero guards
- Timeseries computation
- Breakdown by dimension
- Workspace scoping

Setup:
- Requires test database with seed data
- Uses SQLAlchemy fixtures for isolation
"""

import pytest
from datetime import date, timedelta
from app.dsl.planner import build_plan
from app.dsl.executor import execute_plan, _derive_metric
from app.dsl.schema import MetricQuery, TimeRange, Filters


class TestDerivedMetrics:
    """Test derived metric calculations."""
    
    def test_roas_calculation(self):
        """Test ROAS = revenue / spend."""
        totals = {"spend": 1000, "revenue": 2500}
        roas = _derive_metric("roas", totals)
        assert roas == 2.5
    
    def test_roas_divide_by_zero(self):
        """Test ROAS with zero spend."""
        totals = {"spend": 0, "revenue": 1000}
        roas = _derive_metric("roas", totals)
        assert roas is None
    
    def test_cpa_calculation(self):
        """Test CPA = spend / conversions."""
        totals = {"spend": 1000, "conversions": 50}
        cpa = _derive_metric("cpa", totals)
        assert cpa == 20.0
    
    def test_cpa_divide_by_zero(self):
        """Test CPA with zero conversions."""
        totals = {"spend": 1000, "conversions": 0}
        cpa = _derive_metric("cpa", totals)
        assert cpa is None
    
    def test_cvr_calculation(self):
        """Test CVR = conversions / clicks."""
        totals = {"clicks": 200, "conversions": 50}
        cvr = _derive_metric("cvr", totals)
        assert cvr == 0.25
    
    def test_base_metric(self):
        """Test base metric passthrough."""
        totals = {"spend": 1000}
        spend = _derive_metric("spend", totals)
        assert spend == 1000.0


class TestPlanner:
    """Test query planning logic."""
    
    def test_plan_relative_time_range(self):
        """Test planning with relative time range."""
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7)
        )
        plan = build_plan(query)
        
        assert plan.derived == "roas"
        assert "spend" in plan.base_measures
        assert "revenue" in plan.base_measures
        assert plan.end == date.today()
        assert plan.start == date.today() - timedelta(days=6)
    
    def test_plan_absolute_time_range(self):
        """Test planning with absolute dates."""
        query = MetricQuery(
            metric="spend",
            time_range=TimeRange(
                start=date(2025, 9, 1),
                end=date(2025, 9, 30)
            )
        )
        plan = build_plan(query)
        
        assert plan.start == date(2025, 9, 1)
        assert plan.end == date(2025, 9, 30)
        assert plan.derived is None
        assert plan.base_measures == ["spend"]
    
    def test_plan_comparison(self):
        """Test planning with comparison enabled."""
        query = MetricQuery(
            metric="conversions",
            time_range=TimeRange(last_n_days=30),
            compare_to_previous=True
        )
        plan = build_plan(query)
        
        assert plan.need_previous is True
    
    def test_plan_breakdown(self):
        """Test planning with breakdown."""
        query = MetricQuery(
            metric="revenue",
            time_range=TimeRange(last_n_days=7),
            group_by="campaign",
            breakdown="campaign",
            top_n=10
        )
        plan = build_plan(query)
        
        assert plan.breakdown == "campaign"
        assert plan.top_n == 10


# Integration tests with database
# These require a test database and seed data

@pytest.mark.integration
class TestExecutorIntegration:
    """
    Integration tests for executor.
    
    Setup:
    - Create test database
    - Seed with known data
    - Run queries and verify results
    
    Note: These tests are skipped unless --integration flag is passed.
    """
    
    @pytest.fixture
    def db_session(self):
        """Create test database session."""
        # TODO: Implement test DB setup
        # from app.database import get_test_db
        # db = next(get_test_db())
        # yield db
        # db.close()
        pass
    
    @pytest.fixture
    def workspace_id(self):
        """Return test workspace ID."""
        # TODO: Return test workspace UUID
        return "test-workspace-id"
    
    def test_execute_simple_query(self, db_session, workspace_id):
        """Test executing a simple aggregate query."""
        # TODO: Implement after test DB setup
        pass
    
    def test_workspace_scoping(self, db_session):
        """Test that queries are properly workspace-scoped."""
        # TODO: Create data in two workspaces
        # TODO: Query one workspace, verify no cross-workspace leaks
        pass


# Run tests:
# pytest backend/app/tests/test_dsl_executor.py -v
# pytest backend/app/tests/test_dsl_executor.py -v --integration  # Include integration tests
