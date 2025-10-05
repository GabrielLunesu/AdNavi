"""
Metrics Registry
================

Maps metric names to their required base measures and computation functions.

This is the CONFIGURATION layer that connects:
- Metric name (what users ask for) → Required base fields → Computation function

Used by:
- app/dsl/executor.py: Determines which base measures to aggregate from MetricFact
- app/services/compute_service.py: Determines which base measures to aggregate for Pnl

Design:
- Single source of truth for metric dependencies
- Extensible: add new metrics by adding entries here + formulas.py
- Type-safe: explicit mappings prevent typos

Example usage:
    >>> from app.metrics.registry import METRIC_REGISTRY
    >>> 
    >>> # Get dependencies for ROAS
    >>> metric = METRIC_REGISTRY["roas"]
    >>> print(metric["requires"])
    >>> ["revenue", "spend"]
    >>> 
    >>> # Compute ROAS from aggregated totals
    >>> totals = {"revenue": 5000, "spend": 1000, ...}
    >>> result = metric["fn"](totals["revenue"], totals["spend"])
    >>> print(result)
    >>> 5.0
"""

from app.metrics import formulas


# =====================================================================
# BASE MEASURES (stored directly in MetricFact)
# =====================================================================
# These are not computed; they're aggregated directly from the database.
# Listed here for completeness and to differentiate from derived metrics.

BASE_MEASURES = {
    "spend",
    "revenue",
    "clicks",
    "impressions",
    "conversions",
    "leads",
    "installs",
    "purchases",
    "visitors",
    "profit",
}


# =====================================================================
# DERIVED METRICS REGISTRY
# =====================================================================
# Maps metric name → {required base measures, computation function}

METRIC_REGISTRY = {
    # Efficiency / Cost Metrics
    "cpc": {
        "requires": ["spend", "clicks"],
        "fn": formulas.cpc,
        "category": "cost",
        "format": "currency",  # Used by answer builder for formatting
    },
    "cpm": {
        "requires": ["spend", "impressions"],
        "fn": formulas.cpm,
        "category": "cost",
        "format": "currency",
    },
    "cpl": {
        "requires": ["spend", "leads"],
        "fn": formulas.cpl,
        "category": "cost",
        "format": "currency",
    },
    "cpi": {
        "requires": ["spend", "installs"],
        "fn": formulas.cpi,
        "category": "cost",
        "format": "currency",
    },
    "cpp": {
        "requires": ["spend", "purchases"],
        "fn": formulas.cpp,
        "category": "cost",
        "format": "currency",
    },
    "cpa": {
        "requires": ["spend", "conversions"],
        "fn": formulas.cpa,
        "category": "cost",
        "format": "currency",
    },
    
    # Revenue / Value Metrics
    "roas": {
        "requires": ["revenue", "spend"],
        "fn": formulas.roas,
        "category": "value",
        "format": "ratio",  # e.g., "2.5x"
    },
    "poas": {
        "requires": ["profit", "spend"],
        "fn": formulas.poas,
        "category": "value",
        "format": "ratio",
    },
    "arpv": {
        "requires": ["revenue", "visitors"],
        "fn": formulas.arpv,
        "category": "value",
        "format": "currency",
    },
    "aov": {
        "requires": ["revenue", "conversions"],
        "fn": formulas.aov,
        "category": "value",
        "format": "currency",
    },
    
    # Performance / Engagement Metrics
    "ctr": {
        "requires": ["clicks", "impressions"],
        "fn": formulas.ctr,
        "category": "engagement",
        "format": "percentage",  # e.g., "4.2%"
    },
    "cvr": {
        "requires": ["conversions", "clicks"],
        "fn": formulas.cvr,
        "category": "engagement",
        "format": "percentage",
    },
}


# =====================================================================
# HELPER FUNCTIONS
# =====================================================================

def is_base_measure(metric: str) -> bool:
    """
    Check if a metric is a base measure (stored) or derived (computed).
    
    Args:
        metric: Metric name (e.g., "spend", "roas", "cpc")
        
    Returns:
        True if base measure, False if derived metric
        
    Examples:
        >>> is_base_measure("spend")
        True
        
        >>> is_base_measure("roas")
        False
    """
    return metric in BASE_MEASURES


def is_derived_metric(metric: str) -> bool:
    """
    Check if a metric is derived (computed from base measures).
    
    Args:
        metric: Metric name (e.g., "spend", "roas", "cpc")
        
    Returns:
        True if derived metric, False if base measure
        
    Examples:
        >>> is_derived_metric("roas")
        True
        
        >>> is_derived_metric("spend")
        False
    """
    return metric in METRIC_REGISTRY


def get_required_bases(metric: str) -> list[str]:
    """
    Get the list of base measures required to compute a metric.
    
    For base measures, returns the measure itself.
    For derived metrics, returns the dependencies.
    
    Args:
        metric: Metric name (e.g., "roas", "spend")
        
    Returns:
        List of required base measure names
        
    Examples:
        >>> get_required_bases("roas")
        ["revenue", "spend"]
        
        >>> get_required_bases("spend")
        ["spend"]
        
        >>> get_required_bases("invalid_metric")
        []
    """
    if is_base_measure(metric):
        return [metric]
    
    if is_derived_metric(metric):
        return METRIC_REGISTRY[metric]["requires"]
    
    return []


def compute_metric(metric: str, totals: dict) -> float | None:
    """
    Compute a metric value from aggregated base measure totals.
    
    This is the main entry point for computing ANY metric (base or derived).
    
    Args:
        metric: Metric name (e.g., "roas", "spend", "cpc")
        totals: Dict with base measure totals (e.g., {"spend": 1000, "revenue": 2500})
        
    Returns:
        Computed metric value, or None if cannot be computed
        
    Examples:
        >>> totals = {"spend": 1000, "revenue": 2500, "clicks": 500}
        >>> compute_metric("roas", totals)
        2.5
        
        >>> compute_metric("spend", totals)
        1000.0
        
        >>> compute_metric("cpc", totals)
        2.0
        
        >>> compute_metric("cpc", {"spend": 1000, "clicks": 0})
        None  # Divide by zero
    """
    # Base measure: return the value directly
    if is_base_measure(metric):
        value = totals.get(metric)
        return float(value) if value is not None else None
    
    # Derived metric: compute using the formula
    if is_derived_metric(metric):
        entry = METRIC_REGISTRY[metric]
        required = entry["requires"]
        fn = entry["fn"]
        
        # Extract required base values
        args = [totals.get(base) for base in required]
        
        # Call the formula function
        return fn(*args)
    
    # Unknown metric
    return None


def get_all_metrics() -> list[str]:
    """
    Get list of ALL supported metrics (base + derived).
    
    Returns:
        List of metric names
        
    Examples:
        >>> metrics = get_all_metrics()
        >>> "spend" in metrics
        True
        >>> "roas" in metrics
        True
    """
    return list(BASE_MEASURES) + list(METRIC_REGISTRY.keys())


def get_metric_format(metric: str) -> str:
    """
    Get the recommended format for displaying a metric.
    
    Used by answer builder to format numbers correctly.
    
    Args:
        metric: Metric name
        
    Returns:
        Format type: "currency", "ratio", "percentage", or "number"
        
    Examples:
        >>> get_metric_format("roas")
        "ratio"
        
        >>> get_metric_format("ctr")
        "percentage"
        
        >>> get_metric_format("spend")
        "currency"
    """
    # Base measures that are currency
    if metric in ["spend", "revenue", "profit"]:
        return "currency"
    
    # Base measures that are counts
    if metric in ["clicks", "impressions", "conversions", "leads", "installs", "purchases", "visitors"]:
        return "number"
    
    # Derived metrics: use the format from registry
    if metric in METRIC_REGISTRY:
        return METRIC_REGISTRY[metric].get("format", "number")
    
    return "number"

