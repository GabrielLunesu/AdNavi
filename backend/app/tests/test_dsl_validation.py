"""
DSL Validation Tests
====================

Table-driven tests for DSL validation logic.

Tests:
- Valid DSL payloads (should pass)
- Invalid DSL payloads (should fail with specific errors)
- Edge cases (boundary values, None handling)
"""

import pytest
from app.dsl.validate import validate_dsl, DSLValidationError


class TestDSLValidation:
    """Test DSL validation with various payloads."""
    
    def test_valid_simple_query(self):
        """Test a simple valid query."""
        dsl_dict = {
            "metric": "roas",
            "time_range": {"last_n_days": 7},
            "compare_to_previous": False,
            "group_by": "none",
            "breakdown": None,
            "top_n": 5,
            "filters": {}
        }
        
        result = validate_dsl(dsl_dict)
        assert result.metric == "roas"
        assert result.time_range.last_n_days == 7
    
    def test_valid_with_filters(self):
        """Test query with filters."""
        dsl_dict = {
            "metric": "spend",
            "time_range": {"last_n_days": 30},
            "compare_to_previous": True,
            "group_by": "campaign",
            "breakdown": "campaign",
            "top_n": 10,
            "filters": {
                "provider": "google",
                "status": "active"
            }
        }
        
        result = validate_dsl(dsl_dict)
        assert result.filters.provider == "google"
        assert result.filters.status == "active"
    
    def test_valid_absolute_dates(self):
        """Test query with absolute date range."""
        dsl_dict = {
            "metric": "revenue",
            "time_range": {
                "start": "2025-09-01",
                "end": "2025-09-30"
            },
            "compare_to_previous": False,
            "group_by": "none",
            "breakdown": None,
            "top_n": 5,
            "filters": {}
        }
        
        result = validate_dsl(dsl_dict)
        assert str(result.time_range.start) == "2025-09-01"
        assert str(result.time_range.end) == "2025-09-30"
    
    def test_invalid_metric(self):
        """Test invalid metric name."""
        dsl_dict = {
            "metric": "invalid_metric",
            "time_range": {"last_n_days": 7},
        }
        
        with pytest.raises(DSLValidationError) as exc_info:
            validate_dsl(dsl_dict)
        
        assert "metric" in str(exc_info.value).lower()
    
    def test_invalid_date_range(self):
        """Test invalid date range (end before start)."""
        dsl_dict = {
            "metric": "spend",
            "time_range": {
                "start": "2025-09-30",
                "end": "2025-09-01"  # End before start
            }
        }
        
        with pytest.raises(DSLValidationError) as exc_info:
            validate_dsl(dsl_dict)
        
        assert "end" in str(exc_info.value).lower()
    
    def test_invalid_top_n(self):
        """Test invalid top_n value."""
        dsl_dict = {
            "metric": "conversions",
            "time_range": {"last_n_days": 7},
            "top_n": 100  # Exceeds max of 50
        }
        
        with pytest.raises(DSLValidationError):
            validate_dsl(dsl_dict)
    
    def test_missing_required_field(self):
        """Test missing required field."""
        dsl_dict = {
            # Missing "metric"
            "time_range": {"last_n_days": 7}
        }
        
        with pytest.raises(DSLValidationError):
            validate_dsl(dsl_dict)


# Run tests:
# pytest backend/app/tests/test_dsl_validation.py -v
