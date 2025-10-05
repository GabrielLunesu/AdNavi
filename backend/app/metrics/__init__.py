"""
Metrics Module
==============

Single source of truth for metric formulas used across the system.

This module provides:
- Pure mathematical functions for derived metrics (formulas.py)
- Registry mapping metric names to their dependencies and functions (registry.py)

Used by:
- app/dsl/executor.py: Ad-hoc queries from MetricFact
- app/services/compute_service.py: Snapshot/EOD computation into Pnl
- app/services/qa_service.py: Answer formatting and validation

Design principles:
- Store ONLY base measures in MetricFact
- Compute derived metrics on-demand or during compute runs
- One place to change formulas → consistency everywhere
- Divide-by-zero guards in all formulas
"""

