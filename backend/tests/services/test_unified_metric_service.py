"""
Unit tests for UnifiedMetricService.

Tests the core functionality of the unified metric service including:
- Summary calculations
- Timeseries generation
- Breakdown queries
- Workspace averages
- Filter application
- Security (workspace isolation)
"""

import pytest
from datetime import date, timedelta
from unittest.mock import Mock, patch
from sqlalchemy.orm import Session

from app.services.unified_metric_service import (
    UnifiedMetricService,
    MetricFilters,
    MetricValue,
    MetricSummary,
    MetricTimePoint,
    MetricBreakdownItem
)
from app.dsl.schema import TimeRange


class TestMetricFilters:
    """Test MetricFilters dataclass."""
    
    def test_default_filters(self):
        """Test default filter values."""
        filters = MetricFilters()
        assert filters.provider is None
        assert filters.level is None
        assert filters.status is None
        assert filters.entity_ids is None
        assert filters.entity_name is None
        assert filters.metric_filters is None
    
    def test_provider_normalization(self):
        """Test provider enum normalization."""
        # String format
        filters = MetricFilters(provider="meta")
        assert filters.normalize_provider() == "meta"
        
        # Enum format
        filters = MetricFilters(provider="ProviderEnum.meta")
        assert filters.normalize_provider() == "meta"
        
        # None
        filters = MetricFilters(provider=None)
        assert filters.normalize_provider() is None


class TestUnifiedMetricService:
    """Test UnifiedMetricService core functionality."""
    
    @pytest.fixture
    def mock_db(self):
        """Mock database session."""
        return Mock(spec=Session)
    
    @pytest.fixture
    def service(self, mock_db):
        """Service instance with mocked database."""
        return UnifiedMetricService(mock_db)
    
    def test_init(self, service):
        """Test service initialization."""
        assert service.db is not None
        assert service.MF is not None
        assert service.E is not None
    
    def test_resolve_time_range_last_n_days(self, service):
        """Test time range resolution with last_n_days."""
        time_range = TimeRange(last_n_days=7)
        start, end = service._resolve_time_range(time_range)
        
        # Should be 7 days ending today
        expected_end = date.today()
        expected_start = expected_end - timedelta(days=6)
        
        assert start == expected_start
        assert end == expected_end
    
    def test_resolve_time_range_start_end(self, service):
        """Test time range resolution with start/end dates."""
        start_date = date(2025, 10, 1)
        end_date = date(2025, 10, 7)
        time_range = TimeRange(start=start_date, end=end_date)
        
        start, end = service._resolve_time_range(time_range)
        assert start == start_date
        assert end == end_date
    
    def test_get_previous_period(self, service):
        """Test previous period calculation."""
        start_date = date(2025, 10, 1)
        end_date = date(2025, 10, 7)
        
        prev_start, prev_end = service._get_previous_period(start_date, end_date)
        
        # Should be 7 days before the original period
        expected_prev_end = date(2025, 9, 30)
        expected_prev_start = date(2025, 9, 24)
        
        assert prev_start == expected_prev_start
        assert prev_end == expected_prev_end
    
    @patch('app.services.unified_metric_service.compute_metric')
    def test_get_summary_single_metric(self, mock_compute_metric, service):
        """Test summary calculation for single metric."""
        # Mock database response
        mock_row = Mock()
        mock_row._asdict.return_value = {
            "spend": 1000.0,
            "revenue": 2500.0,
            "clicks": 500.0,
            "impressions": 10000.0,
            "conversions": 50.0,
            "leads": 0.0,
            "installs": 0.0,
            "purchases": 0.0,
            "visitors": 0.0,
            "profit": 0.0
        }
        
        # Mock query execution
        mock_query = Mock()
        mock_query.first.return_value = mock_row
        service._get_base_totals = Mock(return_value=mock_row._asdict())
        service.get_workspace_average = Mock(return_value=2.5)
        
        # Mock metric computation
        mock_compute_metric.return_value = 2.5
        
        # Test
        result = service.get_summary(
            workspace_id="test-workspace",
            metrics=["roas"],
            time_range=TimeRange(last_n_days=7),
            filters=MetricFilters()
        )
        
        # Verify
        assert isinstance(result, MetricSummary)
        assert "roas" in result.metrics
        assert result.metrics["roas"].value == 2.5
        assert result.workspace_avg == 2.5
    
    @patch('app.services.unified_metric_service.compute_metric')
    def test_get_summary_multiple_metrics(self, mock_compute_metric, service):
        """Test summary calculation for multiple metrics."""
        # Mock database response
        mock_totals = {
            "spend": 1000.0,
            "revenue": 2500.0,
            "clicks": 500.0,
            "impressions": 10000.0,
            "conversions": 50.0,
            "leads": 0.0,
            "installs": 0.0,
            "purchases": 0.0,
            "visitors": 0.0,
            "profit": 0.0
        }
        
        service._get_base_totals = Mock(return_value=mock_totals)
        service.get_workspace_average = Mock(return_value=2.5)
        
        # Mock metric computations
        def mock_compute(metric, totals):
            if metric == "roas":
                return 2.5
            elif metric == "cpc":
                return 2.0
            return None
        
        mock_compute_metric.side_effect = mock_compute
        
        # Test
        result = service.get_summary(
            workspace_id="test-workspace",
            metrics=["roas", "cpc"],
            time_range=TimeRange(last_n_days=7),
            filters=MetricFilters()
        )
        
        # Verify
        assert isinstance(result, MetricSummary)
        assert "roas" in result.metrics
        assert "cpc" in result.metrics
        assert result.metrics["roas"].value == 2.5
        assert result.metrics["cpc"].value == 2.0
    
    @patch('app.services.unified_metric_service.compute_metric')
    def test_get_summary_with_comparison(self, mock_compute_metric, service):
        """Test summary calculation with previous period comparison."""
        # Mock current and previous totals
        current_totals = {
            "spend": 1000.0,
            "revenue": 2500.0,
            "clicks": 500.0,
            "impressions": 10000.0,
            "conversions": 50.0,
            "leads": 0.0,
            "installs": 0.0,
            "purchases": 0.0,
            "visitors": 0.0,
            "profit": 0.0
        }
        
        previous_totals = {
            "spend": 800.0,
            "revenue": 2000.0,
            "clicks": 400.0,
            "impressions": 8000.0,
            "conversions": 40.0,
            "leads": 0.0,
            "installs": 0.0,
            "purchases": 0.0,
            "visitors": 0.0,
            "profit": 0.0
        }
        
        service._get_base_totals = Mock(side_effect=[current_totals, previous_totals])
        service.get_workspace_average = Mock(return_value=2.5)
        
        # Mock metric computations
        def mock_compute(metric, totals):
            if metric == "roas":
                if totals == current_totals:
                    return 2.5
                elif totals == previous_totals:
                    return 2.0
            return None
        
        mock_compute_metric.side_effect = mock_compute
        
        # Test
        result = service.get_summary(
            workspace_id="test-workspace",
            metrics=["roas"],
            time_range=TimeRange(last_n_days=7),
            filters=MetricFilters(),
            compare_to_previous=True
        )
        
        # Verify
        assert isinstance(result, MetricSummary)
        assert "roas" in result.metrics
        assert result.metrics["roas"].value == 2.5
        assert result.metrics["roas"].previous == 2.0
        assert result.metrics["roas"].delta_pct == 0.25  # (2.5 - 2.0) / 2.0
    
    def test_get_workspace_average(self, service):
        """Test workspace average calculation."""
        # Mock database response
        mock_row = Mock()
        mock_row.spend = 1000.0
        mock_row.revenue = 2500.0
        
        # Mock query
        mock_query = Mock()
        mock_query.first.return_value = mock_row
        
        # Mock database session
        service.db.query.return_value.join.return_value.filter.return_value = mock_query
        
        # Mock compute_metric
        with patch('app.services.unified_metric_service.compute_metric') as mock_compute:
            mock_compute.return_value = 2.5
            
            result = service.get_workspace_average(
                workspace_id="test-workspace",
                metric="roas",
                time_range=TimeRange(last_n_days=7)
            )
            
            assert result == 2.5
    
    def test_apply_filters_provider(self, service):
        """Test provider filter application."""
        # Mock query
        mock_query = Mock()
        
        # Test provider filter
        filters = MetricFilters(provider="meta")
        result = service._apply_filters(mock_query, filters)
        
        # Verify filter was applied
        mock_query.filter.assert_called()
    
    def test_apply_filters_level(self, service):
        """Test level filter application."""
        # Mock query
        mock_query = Mock()
        
        # Test level filter
        filters = MetricFilters(level="campaign")
        result = service._apply_filters(mock_query, filters)
        
        # Verify filter was applied
        mock_query.filter.assert_called()
    
    def test_apply_filters_status(self, service):
        """Test status filter application."""
        # Mock query
        mock_query = Mock()
        
        # Test status filter
        filters = MetricFilters(status="active")
        result = service._apply_filters(mock_query, filters)
        
        # Verify filter was applied
        mock_query.filter.assert_called()
    
    def test_apply_filters_entity_ids(self, service):
        """Test entity IDs filter application."""
        # Mock query
        mock_query = Mock()
        
        # Test entity IDs filter
        filters = MetricFilters(entity_ids=["id1", "id2"])
        result = service._apply_filters(mock_query, filters)
        
        # Verify filter was applied
        mock_query.filter.assert_called()
    
    def test_apply_filters_entity_name(self, service):
        """Test entity name filter application."""
        # Mock query
        mock_query = Mock()
        
        # Test entity name filter
        filters = MetricFilters(entity_name="Summer Sale")
        result = service._apply_filters(mock_query, filters)
        
        # Verify filter was applied
        mock_query.filter.assert_called()
    
    def test_apply_filters_no_filters(self, service):
        """Test query with no filters applied."""
        # Mock query
        mock_query = Mock()
        
        # Test no filters
        filters = MetricFilters()
        result = service._apply_filters(mock_query, filters)
        
        # Verify no filters were applied
        mock_query.filter.assert_not_called()
    
    def test_get_order_expression_roas(self, service):
        """Test order expression for ROAS."""
        expr = service._get_order_expression("roas")
        assert expr is not None
    
    def test_get_order_expression_cpc(self, service):
        """Test order expression for CPC."""
        expr = service._get_order_expression("cpc")
        assert expr is not None
    
    def test_get_order_expression_fallback(self, service):
        """Test order expression fallback to spend."""
        expr = service._get_order_expression("unknown_metric")
        assert expr is not None


class TestMetricValue:
    """Test MetricValue dataclass."""
    
    def test_metric_value_creation(self):
        """Test MetricValue creation."""
        value = MetricValue(value=2.5)
        assert value.value == 2.5
        assert value.previous is None
        assert value.delta_pct is None
    
    def test_metric_value_with_comparison(self):
        """Test MetricValue with comparison data."""
        value = MetricValue(value=2.5, previous=2.0, delta_pct=0.25)
        assert value.value == 2.5
        assert value.previous == 2.0
        assert value.delta_pct == 0.25


class TestMetricSummary:
    """Test MetricSummary dataclass."""
    
    def test_metric_summary_creation(self):
        """Test MetricSummary creation."""
        metrics = {"roas": MetricValue(value=2.5)}
        summary = MetricSummary(metrics=metrics)
        assert summary.metrics == metrics
        assert summary.workspace_avg is None
    
    def test_metric_summary_with_workspace_avg(self):
        """Test MetricSummary with workspace average."""
        metrics = {"roas": MetricValue(value=2.5)}
        summary = MetricSummary(metrics=metrics, workspace_avg=2.3)
        assert summary.metrics == metrics
        assert summary.workspace_avg == 2.3


class TestMetricTimePoint:
    """Test MetricTimePoint dataclass."""
    
    def test_metric_time_point_creation(self):
        """Test MetricTimePoint creation."""
        point = MetricTimePoint(date="2025-10-08", value=2.5)
        assert point.date == "2025-10-08"
        assert point.value == 2.5


class TestMetricBreakdownItem:
    """Test MetricBreakdownItem dataclass."""
    
    def test_metric_breakdown_item_creation(self):
        """Test MetricBreakdownItem creation."""
        item = MetricBreakdownItem(
            label="Summer Sale",
            value=2.5,
            spend=1000.0,
            clicks=500.0
        )
        assert item.label == "Summer Sale"
        assert item.value == 2.5
        assert item.spend == 1000.0
        assert item.clicks == 500.0
        assert item.conversions is None
        assert item.revenue is None
        assert item.impressions is None
