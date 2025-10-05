"""
DSL Schema (v1.2)
=================

Pydantic models defining the query DSL contract.

DSL v1.2 adds support for non-metrics queries:
- metrics: Query for metrics data (spend, revenue, ROAS, etc.)
- providers: List distinct ad platforms in the workspace
- entities: List entities (campaigns/adsets/ads) with filters

Related files:
- app/dsl/validate.py: Validation and repair logic
- app/dsl/planner.py: Converts these models into execution plans
- app/dsl/executor.py: Executes the plans
- app/nlp/translator.py: Translates natural language to these models
"""

from __future__ import annotations

from enum import Enum
from pydantic import BaseModel, Field, field_validator
from typing import Literal, Optional, List, Dict, Union
from datetime import date

# Query types: different types of questions we can answer
class QueryType(str, Enum):
    """
    Type of query to execute.
    
    - METRICS: Aggregate metrics data (spend, revenue, ROAS, etc.)
    - PROVIDERS: List distinct ad platforms (providers) in workspace
    - ENTITIES: List entities (campaigns, adsets, ads) with filters
    
    Example questions by type:
    - metrics: "What's my ROAS this week?"
    - providers: "Which platforms am I advertising on?"
    - entities: "List my active campaigns"
    """
    METRICS = "metrics"
    PROVIDERS = "providers"
    ENTITIES = "entities"

# Metric types: base metrics (directly stored) and derived metrics (computed)
# Derived Metrics v1: Extended with new base measures and derived metrics
Metric = Literal[
    # Original base measures
    "spend",        # Base: ad spend amount
    "revenue",      # Base: revenue generated
    "clicks",       # Base: number of clicks
    "impressions",  # Base: number of ad impressions
    "conversions",  # Base: number of conversions
    
    # Derived Metrics v1: New base measures
    "leads",        # Base: lead form submissions (Meta Lead Ads, etc.)
    "installs",     # Base: app installations (App Install campaigns)
    "purchases",    # Base: purchase events (ecommerce tracking)
    "visitors",     # Base: landing page visitors (analytics)
    "profit",       # Base: net profit (revenue - costs)
    
    # Original derived metrics
    "roas",         # Derived: revenue / spend (Return on Ad Spend)
    "cpa",          # Derived: spend / conversions (Cost per Acquisition)
    "cvr",          # Derived: conversions / clicks (Conversion Rate)
    
    # Derived Metrics v1: New cost/efficiency metrics
    "cpc",          # Derived: spend / clicks (Cost per Click)
    "cpm",          # Derived: (spend / impressions) * 1000 (Cost per Mille)
    "cpl",          # Derived: spend / leads (Cost per Lead)
    "cpi",          # Derived: spend / installs (Cost per Install)
    "cpp",          # Derived: spend / purchases (Cost per Purchase)
    
    # Derived Metrics v1: New value metrics
    "poas",         # Derived: profit / spend (Profit on Ad Spend)
    "arpv",         # Derived: revenue / visitors (Average Revenue per Visitor)
    "aov",          # Derived: revenue / conversions (Average Order Value)
    
    # Derived Metrics v1: New engagement metrics
    "ctr",          # Derived: clicks / impressions (Click-Through Rate)
]


class TimeRange(BaseModel):
    """
    Selectable time window for metrics queries.
    
    Supports two modes:
    1. Relative: last_n_days (e.g., last 7 days)
    2. Absolute: explicit start and end dates
    
    Examples:
        {"last_n_days": 7}
        {"start": "2025-09-01", "end": "2025-09-30"}
    
    Validation:
    - If using absolute dates, end must be >= start
    - last_n_days must be between 1 and 365
    """
    last_n_days: Optional[int] = Field(default=7, ge=1, le=365)
    start: Optional[date] = None
    end: Optional[date] = None

    @field_validator("end")
    @classmethod
    def _check_range(cls, v, info):
        """Ensure end date is not before start date."""
        if v and info.data.get("start") and v < info.data["start"]:
            raise ValueError("end date must be >= start date")
        return v


class Filters(BaseModel):
    """
    Optional query filters. All filters are ANDed together.
    
    Fields:
    - provider: Filter by ad platform (google, meta, tiktok, other, mock)
    - level: Filter by entity hierarchy level (account, campaign, adset, ad)
    - entity_ids: Filter by specific entity UUIDs
    - status: Filter by entity status (active, paused)
    
    Examples:
        {"provider": "google", "status": "active"}
        {"level": "campaign", "entity_ids": ["uuid1", "uuid2"]}
    """
    provider: Optional[str] = Field(
        default=None,
        description="Ad platform provider filter"
    )
    level: Optional[Literal["account", "campaign", "adset", "ad"]] = Field(
        default=None,
        description="Entity hierarchy level filter"
    )
    entity_ids: Optional[List[str]] = Field(
        default=None,
        description="Specific entity UUIDs to include"
    )
    status: Optional[Literal["active", "paused"]] = Field(
        default=None,
        description="Entity status filter"
    )


class MetricQuery(BaseModel):
    """
    DSL contract for all query types (v1.2).
    
    This is the validated structure that the executor uses to run queries.
    The LLM outputs JSON matching this schema, which gets validated via Pydantic.
    
    DSL v1.2 Changes:
    - Added query_type field to support providers and entities queries
    - Made metric and time_range optional (not needed for providers/entities)
    - Kept all other fields for backward compatibility
    
    Fields:
    - query_type: Type of query (metrics, providers, entities)
    - metric: Which metric to aggregate (required for metrics queries)
    - time_range: Time window for the query (optional for providers/entities)
    - compare_to_previous: Whether to include previous period comparison
    - group_by: Grouping dimension (none = single aggregate)
    - breakdown: Driver analysis dimension (shows top movers)
    - top_n: How many items to return in breakdown or entities list
    - filters: Optional scoping filters
    
    Examples:
        # Metrics query: "What's my ROAS this week?"
        {
            "query_type": "metrics",
            "metric": "roas",
            "time_range": {"last_n_days": 7},
            "compare_to_previous": false,
            "group_by": "none",
            "breakdown": null,
            "filters": {}
        }
        
        # Providers query: "Which platforms am I running ads on?"
        {
            "query_type": "providers"
        }
        
        # Entities query: "List my active campaigns"
        {
            "query_type": "entities",
            "filters": {"level": "campaign", "status": "active"},
            "top_n": 10
        }
    
    Validation notes:
    - For metrics queries: metric field is required
    - For providers/entities queries: metric and time_range are optional
    - Filters are applied to all query types where applicable
    
    Related:
    - Consumed by: app/dsl/planner.py, app/dsl/executor.py
    - Generated by: app/nlp/translator.py
    """
    query_type: QueryType = Field(
        default=QueryType.METRICS,
        description="Type of query to execute (metrics, providers, entities)"
    )
    
    metric: Optional[Metric] = Field(
        default=None,
        description="Metric to aggregate (required for metrics queries, ignored otherwise)"
    )
    
    time_range: Optional[TimeRange] = Field(
        default=None,
        description="Time window for the query (required for metrics, optional for others)"
    )
    
    compare_to_previous: bool = Field(
        default=False,
        description="Include previous period comparison for delta calculation (metrics only)"
    )
    
    group_by: Literal["none", "campaign", "adset", "ad"] = Field(
        default="none",
        description="Grouping dimension (none = single aggregate value)"
    )
    
    breakdown: Optional[Literal["campaign", "adset", "ad"]] = Field(
        default=None,
        description="Breakdown dimension for driver analysis (top movers)"
    )
    
    top_n: int = Field(
        default=5,
        ge=1,
        le=50,
        description="Number of items to return in breakdown or entities list"
    )
    
    filters: Filters = Field(
        default_factory=Filters,
        description="Optional scoping filters (ANDed together)"
    )
    
    def model_dump_json_schema(self) -> dict:
        """Export JSON Schema for LLM structured outputs."""
        return self.model_json_schema()


class MetricResult(BaseModel):
    """
    Executor response structure.
    
    Fields:
    - summary: Main aggregated value for the metric
    - previous: Previous period value (if compare_to_previous=True)
    - delta_pct: Percentage change vs previous period
    - timeseries: Daily values over the selected period
    - breakdown: Top entities by the selected breakdown dimension
    
    Examples:
        # Simple aggregate result:
        {
            "summary": 2.5,
            "previous": 2.1,
            "delta_pct": 0.19,
            "timeseries": null,
            "breakdown": null
        }
        
        # Result with breakdown:
        {
            "summary": 1250.0,
            "previous": null,
            "delta_pct": null,
            "timeseries": [
                {"date": "2025-09-01", "value": 125.0},
                {"date": "2025-09-02", "value": 130.5}
            ],
            "breakdown": [
                {"label": "Summer Sale", "value": 450.0},
                {"label": "Winter Campaign", "value": 320.0}
            ]
        }
    
    Related:
    - Returned by: app/dsl/executor.py
    - Consumed by: app/services/qa_service.py
    """
    summary: Optional[float] = Field(
        default=None,
        description="Main aggregated metric value"
    )
    
    previous: Optional[float] = Field(
        default=None,
        description="Previous period value (for comparison)"
    )
    
    delta_pct: Optional[float] = Field(
        default=None,
        description="Percentage change vs previous period (0.19 = +19%)"
    )
    
    timeseries: Optional[List[Dict[str, Union[str, float, None]]]] = Field(
        default=None,
        description="Daily values: [{date: 'YYYY-MM-DD', value: 123.4}, ...]"
    )
    
    breakdown: Optional[List[Dict[str, Union[str, float, None]]]] = Field(
        default=None,
        description="Top entities: [{label: 'Campaign Name', value: 450.0}, ...]"
    )
