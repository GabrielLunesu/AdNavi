"""
Unit Tests for Context Extractor

WHAT: Test rich context extraction logic
WHY: Ensures deterministic extraction works correctly without mocking
WHERE: Test suite (run with pytest)

COVERAGE:
- Basic context extraction
- Comparison extraction
- Workspace comparison
- Trend detection
- Outlier detection
- Performance assessment
"""

import pytest
from app.answer.context_extractor import (
    extract_rich_context,
    _extract_comparison,
    _extract_workspace_comparison,
    _extract_trend,
    _extract_outliers,
    _assess_performance,
    TrendDirection,
    PerformanceLevel
)
from app.dsl.schema import MetricResult, MetricQuery, TimeRange


class TestContextExtractor:
    """Test suite for context extraction functions."""
    
    def test_extract_rich_context_basic(self):
        """
        WHAT: Test basic context extraction with minimal data
        WHY: Ensures function works with just summary value
        """
        result = MetricResult(
            summary=2.45,
            previous=None,
            delta_pct=None,
            timeseries=[],
            breakdown=[]
        )
        
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7)
        )
        
        context = extract_rich_context(result, query)
        
        assert context.metric_name == "ROAS"
        assert context.metric_value == "2.45×"
        assert context.metric_value_raw == 2.45
        assert context.comparison is None
        assert context.workspace_comparison is None
    
    def test_extract_comparison_higher_is_better(self):
        """
        WHAT: Test comparison extraction for ROAS (higher is better)
        WHY: Verifies correct direction detection
        """
        result = MetricResult(
            summary=2.45,
            previous=2.06,
            delta_pct=0.189,
            timeseries=[],
            breakdown=[]
        )
        
        comparison = _extract_comparison("roas", result)
        
        assert comparison["previous"] == "2.06×"
        assert comparison["previous_raw"] == 2.06
        assert comparison["change"] == "+18.9%"
        assert comparison["change_raw"] == 0.189
        assert comparison["direction"] == "improved"
    
    def test_extract_comparison_lower_is_better(self):
        """
        WHAT: Test comparison extraction for CPC (lower is better)
        WHY: Verifies flipped direction logic
        """
        result = MetricResult(
            summary=0.48,
            previous=0.55,
            delta_pct=-0.127,  # Decreased by 12.7%
            timeseries=[],
            breakdown=[]
        )
        
        comparison = _extract_comparison("cpc", result)
        
        assert comparison["direction"] == "improved"  # Lower CPC = improved
    
    def test_extract_workspace_comparison_above_average(self):
        """
        WHAT: Test workspace comparison when value is above average
        WHY: Verifies correct comparison classification
        """
        comparison = _extract_workspace_comparison(
            metric="roas",
            value=2.45,
            workspace_avg=2.20
        )
        
        assert comparison["workspace_avg"] == "2.20×"
        assert comparison["comparison"] == "above average"
        assert comparison["deviation_pct"] > 0.10
    
    def test_extract_workspace_comparison_average(self):
        """
        WHAT: Test workspace comparison when value is near average
        WHY: Verifies ±10% threshold logic
        """
        comparison = _extract_workspace_comparison(
            metric="roas",
            value=2.25,
            workspace_avg=2.20
        )
        
        assert comparison["comparison"] == "average"
        assert abs(comparison["deviation_pct"]) < 0.10
    
    def test_extract_trend_increasing(self):
        """
        WHAT: Test trend detection for increasing pattern
        WHY: Verifies correct trend classification
        """
        timeseries = [
            {"date": "2025-10-01", "value": 2.1},
            {"date": "2025-10-02", "value": 2.3},
            {"date": "2025-10-03", "value": 2.5},
            {"date": "2025-10-04", "value": 2.7},
            {"date": "2025-10-05", "value": 2.8}
        ]
        
        trend = _extract_trend("roas", timeseries)
        
        assert trend["direction"] == TrendDirection.INCREASING
        assert trend["start_value"] == "2.10×"
        assert trend["end_value"] == "2.80×"
        assert trend["peak_value"] == "2.80×"
        assert trend["peak_date"] == "2025-10-05"
    
    def test_extract_trend_stable(self):
        """
        WHAT: Test trend detection for stable pattern
        WHY: Verifies <10% change threshold
        """
        timeseries = [
            {"date": "2025-10-01", "value": 2.20},
            {"date": "2025-10-02", "value": 2.22},
            {"date": "2025-10-03", "value": 2.25},
            {"date": "2025-10-04", "value": 2.23},
            {"date": "2025-10-05", "value": 2.24}
        ]
        
        trend = _extract_trend("roas", timeseries)
        
        assert trend["direction"] == TrendDirection.STABLE
    
    def test_extract_trend_volatile(self):
        """
        WHAT: Test trend detection for volatile pattern
        WHY: Verifies volatility detection (std dev / mean > 0.20)
        """
        timeseries = [
            {"date": "2025-10-01", "value": 2.0},
            {"date": "2025-10-02", "value": 4.0},
            {"date": "2025-10-03", "value": 1.5},
            {"date": "2025-10-04", "value": 3.5},
            {"date": "2025-10-05", "value": 2.2}
        ]
        
        trend = _extract_trend("roas", timeseries)
        
        assert trend["direction"] == TrendDirection.VOLATILE
        assert trend["volatility"] > 0.20
    
    def test_extract_outliers(self):
        """
        WHAT: Test outlier detection in breakdown
        WHY: Verifies z-score calculation and threshold
        """
        breakdown = [
            {"label": "Campaign A", "value": 2.0},
            {"label": "Campaign B", "value": 2.2},
            {"label": "Campaign C", "value": 2.1},
            {"label": "Campaign D", "value": 5.8},  # Outlier (high)
            {"label": "Campaign E", "value": 2.3}
        ]
        
        outliers = _extract_outliers("roas", breakdown, threshold=2.0)
        
        assert len(outliers) == 1
        assert outliers[0]["label"] == "Campaign D"
        assert outliers[0]["type"] == "high"
        assert outliers[0]["z_score"] > 2.0
    
    def test_extract_outliers_insufficient_data(self):
        """
        WHAT: Test outlier detection with <3 data points
        WHY: Verifies early return for insufficient data
        """
        breakdown = [
            {"label": "Campaign A", "value": 2.0},
            {"label": "Campaign B", "value": 2.2}
        ]
        
        outliers = _extract_outliers("roas", breakdown)
        
        assert len(outliers) == 0
    
    def test_assess_performance_excellent(self):
        """
        WHAT: Test performance assessment - EXCELLENT level
        WHY: Verifies >150% of workspace avg = EXCELLENT
        """
        performance = _assess_performance(
            metric="roas",
            value=3.5,
            workspace_avg=2.0,
            delta_pct=None
        )
        
        assert performance == PerformanceLevel.EXCELLENT
    
    def test_assess_performance_poor_from_delta(self):
        """
        WHAT: Test performance assessment - POOR from delta
        WHY: Verifies delta-based assessment when no workspace_avg
        """
        performance = _assess_performance(
            metric="roas",
            value=2.0,
            workspace_avg=None,
            delta_pct=-0.20  # Declined by 20%
        )
        
        assert performance == PerformanceLevel.POOR
    
    def test_assess_performance_lower_is_better_flip(self):
        """
        WHAT: Test performance assessment for CPC (lower is better)
        WHY: Verifies logic flip for cost metrics
        """
        # Low CPC (0.30) vs high workspace avg (0.50) = EXCELLENT
        performance = _assess_performance(
            metric="cpc",
            value=0.30,
            workspace_avg=0.50,
            delta_pct=None
        )
        
        assert performance == PerformanceLevel.EXCELLENT


class TestIntegration:
    """Integration tests for full context extraction."""
    
    def test_full_context_with_all_data(self):
        """
        WHAT: Test extract_rich_context with complete data
        WHY: Verifies all context fields populated correctly
        """
        result = MetricResult(
            summary=2.45,
            previous=2.06,
            delta_pct=0.189,
            timeseries=[
                {"date": "2025-10-01", "value": 2.1},
                {"date": "2025-10-02", "value": 2.3},
                {"date": "2025-10-03", "value": 2.8},
                {"date": "2025-10-04", "value": 2.6},
                {"date": "2025-10-05", "value": 2.45}
            ],
            breakdown=[
                {"label": "Summer Sale", "value": 3.2},
                {"label": "Winter Promo", "value": 2.8},
                {"label": "Spring Launch", "value": 1.9}
            ]
        )
        
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7)
        )
        
        context = extract_rich_context(result, query, workspace_avg=2.30)
        
        # Verify all sections populated
        assert context.metric_name == "ROAS"
        assert context.metric_value == "2.45×"
        assert context.comparison is not None
        assert context.workspace_comparison is not None
        assert context.trend is not None
        assert context.top_performer is not None
        assert context.bottom_performer is not None
        assert context.performance_level is not None
        
        # Verify specific values
        assert context.comparison["direction"] == "improved"
        assert context.workspace_comparison["comparison"] == "above average"
        assert context.top_performer["label"] == "Summer Sale"
        assert context.bottom_performer["label"] == "Spring Launch"
    
    def test_context_with_workspace_avg_only(self):
        """
        WHAT: Test context extraction with workspace_avg but no previous period
        WHY: Verifies workspace comparison works independently
        """
        result = MetricResult(
            summary=2.45,
            previous=None,
            delta_pct=None,
            timeseries=[],
            breakdown=[]
        )
        
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7)
        )
        
        context = extract_rich_context(result, query, workspace_avg=2.30)
        
        assert context.comparison is None
        assert context.workspace_comparison is not None
        assert context.workspace_comparison["workspace_avg"] == "2.30×"
        assert context.workspace_comparison["comparison"] == "above average"
    
    def test_context_to_dict_filters_none(self):
        """
        WHAT: Test to_dict() filters out None values
        WHY: Ensures GPT prompt only includes available context
        """
        result = MetricResult(
            summary=2.45,
            previous=None,
            delta_pct=None,
            timeseries=[],
            breakdown=[]
        )
        
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7)
        )
        
        context = extract_rich_context(result, query)
        context_dict = context.to_dict()
        
        # Verify None values are filtered out
        assert "comparison" not in context_dict
        assert "workspace_comparison" not in context_dict
        assert "trend" not in context_dict
        
        # Verify present values are included
        assert "metric_name" in context_dict
        assert "metric_value" in context_dict
        assert "metric_value_raw" in context_dict
        assert "performance_level" in context_dict

