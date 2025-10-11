"""Unit tests for manual cost allocation logic.

WHAT: Tests pro-rating rules for one-off and range costs
WHY: Allocation logic is critical for accurate P&L; must handle edge cases
REFERENCES: app/services/cost_allocation.py
"""

import pytest
from datetime import date
from app.services.cost_allocation import calculate_allocated_amount
from app.models import ManualCost
from unittest.mock import MagicMock


def test_one_off_inside_period():
    """One-off cost inside period → full amount."""
    cost = MagicMock(spec=ManualCost)
    cost.allocation_type = "one_off"
    cost.allocation_date = date(2025, 10, 15)
    cost.amount_dollar = 299.00
    
    allocated = calculate_allocated_amount(
        cost,
        period_start=date(2025, 10, 1),
        period_end=date(2025, 11, 1)
    )
    
    assert allocated == 299.00


def test_one_off_outside_period():
    """One-off cost outside period → 0."""
    cost = MagicMock(spec=ManualCost)
    cost.allocation_type = "one_off"
    cost.allocation_date = date(2025, 9, 15)
    cost.amount_dollar = 299.00
    
    allocated = calculate_allocated_amount(
        cost,
        period_start=date(2025, 10, 1),
        period_end=date(2025, 11, 1)
    )
    
    assert allocated == 0.0


def test_range_fully_inside():
    """Range fully inside period → full amount."""
    cost = MagicMock(spec=ManualCost)
    cost.allocation_type = "range"
    cost.allocation_start = date(2025, 10, 5)
    cost.allocation_end = date(2025, 10, 15)
    cost.amount_dollar = 1000.00
    
    allocated = calculate_allocated_amount(
        cost,
        period_start=date(2025, 10, 1),
        period_end=date(2025, 11, 1)
    )
    
    assert allocated == 1000.00


def test_range_partial_overlap():
    """Range partially overlapping → pro-rated.
    
    Cost: Sept 20 - Oct 10 (20 days)
    Period: Oct 1 - Nov 1
    Overlap: Oct 1 - Oct 10 (9 days, end is exclusive)
    Expected: 9/20 of amount = 45%
    """
    cost = MagicMock(spec=ManualCost)
    cost.allocation_type = "range"
    cost.allocation_start = date(2025, 9, 20)
    cost.allocation_end = date(2025, 10, 10)
    cost.amount_dollar = 2000.00
    
    allocated = calculate_allocated_amount(
        cost,
        period_start=date(2025, 10, 1),
        period_end=date(2025, 11, 1)
    )
    
    assert allocated == 900.00  # 9 days / 20 days = 45%


def test_range_no_overlap():
    """Range outside period → 0."""
    cost = MagicMock(spec=ManualCost)
    cost.allocation_type = "range"
    cost.allocation_start = date(2025, 8, 1)
    cost.allocation_end = date(2025, 9, 1)
    cost.amount_dollar = 1000.00
    
    allocated = calculate_allocated_amount(
        cost,
        period_start=date(2025, 10, 1),
        period_end=date(2025, 11, 1)
    )
    
    assert allocated == 0.0


def test_range_spanning_multiple_months():
    """Range spanning 3 months → correct pro-rating.
    
    Cost: Oct 1 - Dec 31 (91 days)
    Period: Nov 1 - Dec 1 (30 days)
    Expected: 30/91 of amount
    """
    cost = MagicMock(spec=ManualCost)
    cost.allocation_type = "range"
    cost.allocation_start = date(2025, 10, 1)
    cost.allocation_end = date(2025, 12, 31)
    cost.amount_dollar = 9200.00
    
    allocated = calculate_allocated_amount(
        cost,
        period_start=date(2025, 11, 1),
        period_end=date(2025, 12, 1)
    )
    
    expected = 9200.00 * (30 / 91)
    assert abs(allocated - expected) < 0.01  # Float comparison


def test_leap_year_feb():
    """Leap year February (29 days) → correct allocation."""
    cost = MagicMock(spec=ManualCost)
    cost.allocation_type = "range"
    cost.allocation_start = date(2024, 2, 1)
    cost.allocation_end = date(2024, 3, 1)
    cost.amount_dollar = 2900.00
    
    allocated = calculate_allocated_amount(
        cost,
        period_start=date(2024, 2, 1),
        period_end=date(2024, 3, 1)
    )
    
    assert allocated == 2900.00  # Full 29 days

