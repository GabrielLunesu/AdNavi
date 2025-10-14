"""
Query Executor
==============

Executes query plans against the database using SQLAlchemy.

Derived Metrics v1 changes:
- Uses app/metrics/registry for ALL metric computations
- Aggregates all base measures (including new ones: leads, installs, purchases, visitors, profit)
- Defers derived metric math to formulas (single source of truth)

WHY separate executor?
- Single source of truth for metric calculations → app/metrics/registry
- Workspace scoping enforced at query level
- Divide-by-zero guards for derived metrics → app/metrics/formulas
- Clear separation: planning vs execution

Related files:
- app/dsl/planner.py: Creates the Plan that we execute
- app/dsl/schema.py: MetricResult that we return
- app/models.py: Database models (MetricFact, Entity)
- app/metrics/registry.py: Maps metrics → formulas (USED HERE)
- app/metrics/formulas.py: Pure functions for derived metrics

Design:
- Workspace-scoped: ALL queries filter by workspace_id
- Safe math: Divide-by-zero guards in app/metrics/formulas
- Efficient: Single query for summary, separate for timeseries/breakdown
- Flexible: Supports all filter combinations
"""

from __future__ import annotations

from datetime import timedelta, datetime
from typing import Optional, Dict, Any, List
from uuid import UUID
import logging

from sqlalchemy.orm import Session
from sqlalchemy import func, cast, Date

from app.dsl.schema import MetricResult, MetricQuery, TimeRange
from app.dsl.planner import Plan
from app import models
from app.metrics.registry import compute_metric, get_required_bases

logger = logging.getLogger(__name__)


# =====================================================================
# Phase 3: Data Availability Helpers
# =====================================================================

def get_available_platforms(db: Session, workspace_id: str) -> List[str]:
    """
    Get list of platforms that actually have data in this workspace.
    
    WHY: Needed for graceful handling of platform filter queries
    WHEN: Before executing queries with provider filters
    WHERE: Called by QA service before execute_plan()
    
    Args:
        db: Database session
        workspace_id: Workspace UUID
        
    Returns:
        List of provider names that have metric data (lowercase strings)
        
    Example:
        >>> platforms = get_available_platforms(db, workspace_id)
        >>> platforms
        ['meta', 'tiktok', 'other']  # Google not present
        
    Related:
    - Used by: app/services/qa_service.py for pre-execution validation
    """
    E = models.Entity
    MF = models.MetricFact
    
    result = (
        db.query(MF.provider)
        .join(E, E.id == MF.entity_id)
        .filter(E.workspace_id == workspace_id)
        .distinct()
        .all()
    )
    
    return [r[0].value for r in result]


# =====================================================================
# REMOVED: _derive_metric() function
# =====================================================================
# Derived Metrics v1 change:
# - Old: _derive_metric() function defined here (duplicated logic)
# - New: Use compute_metric() from app/metrics/registry (single source of truth)
# - WHY: Ensures formulas never diverge between executor and compute_service
# - HOW: Import compute_metric at top of file, call it instead of _derive_metric
# =====================================================================


def execute_plan(
    db: Session, 
    workspace_id: str, 
    plan: Optional[Plan],
    query: MetricQuery
) -> Dict[str, Any]:
    """
    Execute a query plan and return results.
    
    DSL v1.2 changes:
    - Accepts both plan (Optional) and query (MetricQuery)
    - Handles three query types:
      1. METRICS: Execute plan (existing logic)
      2. PROVIDERS: List distinct ad platforms in workspace
      3. ENTITIES: List entities with filters
    - Returns either MetricResult (metrics) or dict (providers/entities)
    
    Args:
        db: SQLAlchemy database session
        workspace_id: Workspace UUID for scoping (tenant safety)
        plan: Execution plan from build_plan() (None for non-metrics queries)
        query: Original MetricQuery with query_type and filters
        
    Returns:
        For metrics: MetricResult with summary, comparison, timeseries, and breakdown
        For providers: {"providers": ["google", "meta", ...]}
        For entities: {"entities": [{"name": "...", "status": "...", "level": "..."}, ...]}
        
    Examples:
        >>> # Metrics query
        >>> query = MetricQuery(query_type="metrics", metric="roas", time_range=TimeRange(last_n_days=7))
        >>> plan = build_plan(query)
        >>> result = execute_plan(db, workspace_id="...", plan=plan, query=query)
        >>> print(result.summary)
        2.45
        >>> 
        >>> # Providers query
        >>> query = MetricQuery(query_type="providers")
        >>> result = execute_plan(db, workspace_id="...", plan=None, query=query)
        >>> print(result["providers"])
        ["google", "meta", "tiktok"]
        >>> 
        >>> # Entities query
        >>> query = MetricQuery(query_type="entities", filters={"level": "campaign", "status": "active"})
        >>> result = execute_plan(db, workspace_id="...", plan=None, query=query)
        >>> print(result["entities"])
        [{"name": "Summer Sale", "status": "active", "level": "campaign"}, ...]
    
    Tenant safety:
    - ALL queries filter by workspace_id at the database level
    - No cross-workspace data leaks possible
    
    Related:
    - Input: app/dsl/planner.Plan, app/dsl/schema.MetricQuery
    - Output: app/dsl/schema.MetricResult or dict
    - Called by: app/services/qa_service.py
    """
    # DSL v1.2: Route to appropriate handler based on query_type
    
    # PROVIDERS: List distinct ad platforms in this workspace
    # Returns: {"providers": ["google", "meta", ...]}
    # Example question: "Which platforms am I advertising on?"
    if query.query_type == "providers":
        rows = (
            db.query(models.Connection.provider)
            .filter(models.Connection.workspace_id == workspace_id)
            .distinct()
            .all()
        )
        return {"providers": [row.provider for row in rows]}
    
    # ENTITIES: List entities (campaigns/adsets/ads) with optional filters
    # Returns: {"entities": [{"name": "...", "status": "...", "level": "..."}, ...]}
    # Example question: "List my active campaigns"
    if query.query_type == "entities":
        E = models.Entity
        
        # Base query: all entities in workspace
        q_entities = (
            db.query(E.name, E.status, E.level)
            .filter(E.workspace_id == workspace_id)
        )
        
        # Apply filters from DSL
        if query.filters.level:
            q_entities = q_entities.filter(E.level == query.filters.level)
        if query.filters.status:
            q_entities = q_entities.filter(E.status == query.filters.status)
        if query.filters.entity_ids:
            q_entities = q_entities.filter(E.id.in_(query.filters.entity_ids))
        
        # NEW: Named entity filtering (case-insensitive partial match)
        # WHY: Enables natural queries like "show me Holiday Sale campaign"
        # HOW: Uses ILIKE for case-insensitive matching with wildcards
        # Example: "holiday" matches "Holiday Sale - Purchases"
        if query.filters.entity_name:
            pattern = f"%{query.filters.entity_name}%"
            q_entities = q_entities.filter(E.name.ilike(pattern))
        
        # Limit results by top_n
        rows = q_entities.limit(query.top_n).all()
        
        return {
            "entities": [
                {"name": row.name, "status": row.status, "level": row.level} 
                for row in rows
            ]
        }
    
    # METRICS: Execute the plan (existing v1.1 logic + multi-metric support)
    # This is the default/legacy behavior
    if query.query_type == "metrics":
        if not plan:
            raise ValueError("Plan is required for metrics queries")
        
        # Phase 7: Handle multi-metric queries
        if isinstance(query.metric, list):
            return _execute_multi_metric_plan(db, workspace_id, plan, query)
        else:
            return _execute_metrics_plan(db, workspace_id, plan)
    
    # Unknown query type
    raise ValueError(f"Unsupported query_type: {query.query_type}")


def _execute_metrics_plan(
    db: Session,
    workspace_id: str,
    plan: Plan
) -> MetricResult:
    """
    Execute a metrics plan (DSL v1.1 logic).
    
    This is the original executor logic, now extracted as a separate function
    to keep the main execute_plan() function clean.
    
    Args:
        db: SQLAlchemy database session
        workspace_id: Workspace UUID for scoping
        plan: Execution plan with dates, metrics, filters
        
    Returns:
        MetricResult with summary, comparison, timeseries, and breakdown
        
    Process:
    1. Build base query (MetricFact JOIN Entity, filter by workspace)
    2. Apply date range and filters
    3. Aggregate base measures (spend, revenue, clicks, etc.)
    4. Derive metric value (roas = revenue/spend, etc.)
    5. Optionally compute previous period comparison
    6. Optionally compute daily timeseries
    7. Optionally compute breakdown by dimension
    """
    MF, E = models.MetricFact, models.Entity
    
    # --- SUMMARY AGGREGATION ---
    # Derived Metrics v1: Aggregate ALL base measures (including new ones)
    # WHY: Enables computing any derived metric from the result
    base_query = (
        db.query(
            # Original base measures
            func.coalesce(func.sum(MF.spend), 0).label("spend"),
            func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
            func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
            func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
            func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
            # Derived Metrics v1: New base measures
            func.coalesce(func.sum(MF.leads), 0).label("leads"),
            func.coalesce(func.sum(MF.installs), 0).label("installs"),
            func.coalesce(func.sum(MF.purchases), 0).label("purchases"),
            func.coalesce(func.sum(MF.visitors), 0).label("visitors"),
            func.coalesce(func.sum(MF.profit), 0).label("profit"),
        )
        .join(E, E.id == MF.entity_id)
        .filter(E.workspace_id == workspace_id)  # TENANT SCOPING
        .filter(cast(MF.event_date, Date).between(plan.start, plan.end))
    )
    
    # Apply filters
    if plan.filters.get("provider"):
        base_query = base_query.filter(MF.provider == plan.filters["provider"])
    if plan.filters.get("level"):
        # BUG FIX: Use E.level (Entity table) not MF.level (MetricFact doesn't have level field)
        # WHY: Level is stored in Entity table, not MetricFact table
        # IMPACT: Fixes QA vs UI mismatch where level filters weren't applied correctly
        base_query = base_query.filter(E.level == plan.filters["level"])
    # CORRECTED: Include ALL entities by default (active + inactive)
    # WHY: Inactive campaigns still generated revenue and should be included in financial analysis
    # IMPACT: QA now matches Finance page behavior which includes all entities
    if plan.filters.get("status"):
        base_query = base_query.filter(E.status == plan.filters["status"])
    # Note: No default status filter - include all entities unless explicitly filtered
    if plan.filters.get("entity_ids"):
        base_query = base_query.filter(MF.entity_id.in_(plan.filters["entity_ids"]))
    
    # NEW: Named entity filtering (case-insensitive partial match)
    # WHY: Enables queries like "revenue for Holiday Sale campaign"
    # HOW: Uses ILIKE for case-insensitive matching with wildcards
    if plan.filters.get("entity_name"):
        pattern = f"%{plan.filters['entity_name']}%"
        base_query = base_query.filter(E.name.ilike(pattern))
    
    # Execute summary query
    totals_now = base_query.one()._asdict()
    
    # Derive metric value using metrics/registry
    # Derived Metrics v1: Use compute_metric() from registry (single source of truth)
    metric_name = plan.derived or plan.base_measures[0]
    summary_value = compute_metric(metric_name, totals_now)
    
    # --- PREVIOUS PERIOD COMPARISON ---
    previous_value = None
    delta_pct = None
    
    if plan.need_previous:
        # Calculate previous period window (same length)
        period_length = (plan.end - plan.start).days + 1
        prev_start = plan.start - timedelta(days=period_length)
        prev_end = plan.start - timedelta(days=1)
        
        # Query previous period (aggregate all base measures)
        prev_query = (
            db.query(
                # Original base measures
                func.coalesce(func.sum(MF.spend), 0).label("spend"),
                func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
                func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
                func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
                func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
                # Derived Metrics v1: New base measures
                func.coalesce(func.sum(MF.leads), 0).label("leads"),
                func.coalesce(func.sum(MF.installs), 0).label("installs"),
                func.coalesce(func.sum(MF.purchases), 0).label("purchases"),
                func.coalesce(func.sum(MF.visitors), 0).label("visitors"),
                func.coalesce(func.sum(MF.profit), 0).label("profit"),
            )
            .join(E, E.id == MF.entity_id)
            .filter(E.workspace_id == workspace_id)
            .filter(cast(MF.event_date, Date).between(prev_start, prev_end))
        )
        
        # Apply same filters
        if plan.filters.get("provider"):
            prev_query = prev_query.filter(MF.provider == plan.filters["provider"])
        if plan.filters.get("level"):
            # BUG FIX: Use E.level (Entity table) not MF.level (MetricFact doesn't have level field)
            prev_query = prev_query.filter(E.level == plan.filters["level"])
        # CORRECTED: Include ALL entities by default (active + inactive)
        if plan.filters.get("status"):
            prev_query = prev_query.filter(E.status == plan.filters["status"])
        # Note: No default status filter - include all entities unless explicitly filtered
        if plan.filters.get("entity_name"):
            pattern = f"%{plan.filters['entity_name']}%"
            prev_query = prev_query.filter(E.name.ilike(pattern))
        if plan.filters.get("entity_ids"):
            prev_query = prev_query.filter(MF.entity_id.in_(plan.filters["entity_ids"]))
        
        totals_prev = prev_query.one()._asdict()
        previous_value = compute_metric(metric_name, totals_prev)
        
        # Calculate delta percentage
        if previous_value not in (None, 0) and summary_value is not None:
            delta_pct = (summary_value - previous_value) / previous_value
    
    # --- TIMESERIES (daily values) ---
    timeseries = None
    
    if plan.need_timeseries:
        series_query = (
            db.query(
                # Cast to Date for ISO YYYY-MM-DD format (not YYYY-MM-DD HH:MM:SS)
                cast(MF.event_date, Date).label("date"),
                # Original base measures
                func.coalesce(func.sum(MF.spend), 0).label("spend"),
                func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
                func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
                func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
                func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
                # Derived Metrics v1: New base measures
                func.coalesce(func.sum(MF.leads), 0).label("leads"),
                func.coalesce(func.sum(MF.installs), 0).label("installs"),
                func.coalesce(func.sum(MF.purchases), 0).label("purchases"),
                func.coalesce(func.sum(MF.visitors), 0).label("visitors"),
                func.coalesce(func.sum(MF.profit), 0).label("profit"),
            )
            .join(E, E.id == MF.entity_id)
            .filter(E.workspace_id == workspace_id)
            .filter(cast(MF.event_date, Date).between(plan.start, plan.end))
            .group_by(cast(MF.event_date, Date))
            .order_by(cast(MF.event_date, Date))
        )
        
        # Apply same filters
        if plan.filters.get("provider"):
            series_query = series_query.filter(MF.provider == plan.filters["provider"])
        if plan.filters.get("level"):
            # BUG FIX: Use E.level (Entity table) not MF.level (MetricFact doesn't have level field)
            series_query = series_query.filter(E.level == plan.filters["level"])
        if plan.filters.get("entity_name"):
            pattern = f"%{plan.filters['entity_name']}%"
            series_query = series_query.filter(E.name.ilike(pattern))
        # CORRECTED: Include ALL entities by default (active + inactive)
        if plan.filters.get("status"):
            series_query = series_query.filter(E.status == plan.filters["status"])
        # Note: No default status filter - include all entities unless explicitly filtered
        if plan.filters.get("entity_ids"):
            series_query = series_query.filter(MF.entity_id.in_(plan.filters["entity_ids"]))
        
        rows = series_query.all()
        timeseries = [
            {
                "date": str(row.date),
                "value": compute_metric(metric_name, row._asdict())
            }
            for row in rows
        ]
    
    # --- BREAKDOWN (top entities by dimension) ---
    breakdown = None
    
    if plan.breakdown:
        # Import hierarchy utilities for campaign/adset breakdowns
        from app.dsl.hierarchy import campaign_ancestor_cte, adset_ancestor_cte
        
        # PROVIDER BREAKDOWN: Group by provider (no hierarchy needed)
        # WHY: Provider is a flat dimension (google, meta, tiktok, etc.)
        # Example: "Which platform had the highest ROAS?"
        if plan.breakdown == "provider":
            breakdown_query = (
                db.query(
                    MF.provider.label("group_name"),
                    # Aggregate all base measures
                    func.coalesce(func.sum(MF.spend), 0).label("spend"),
                    func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
                    func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
                    func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
                    func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
                    func.coalesce(func.sum(MF.leads), 0).label("leads"),
                    func.coalesce(func.sum(MF.installs), 0).label("installs"),
                    func.coalesce(func.sum(MF.purchases), 0).label("purchases"),
                    func.coalesce(func.sum(MF.visitors), 0).label("visitors"),
                    func.coalesce(func.sum(MF.profit), 0).label("profit"),
                )
                .join(E, E.id == MF.entity_id)
                .filter(E.workspace_id == workspace_id)  # Tenant scoping
                .filter(cast(MF.event_date, Date).between(plan.start, plan.end))
                .group_by(MF.provider)
            )
        
        # Use hierarchy-aware rollup for campaign/adset/ad breakdowns
        # This allows facts stored at ad/adset level to be rolled up to campaign level
        elif plan.breakdown == "campaign":
            # Get CTE that maps leaf entities to their campaign ancestors
            leaf_to_ancestor = campaign_ancestor_cte(db)
            
            # Build query that joins facts → entities → ancestor mapping
            breakdown_query = (
                db.query(
                    leaf_to_ancestor.c.ancestor_id.label("group_id"),
                    leaf_to_ancestor.c.ancestor_name.label("group_name"),
                    # Original base measures
                    func.coalesce(func.sum(MF.spend), 0).label("spend"),
                    func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
                    func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
                    func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
                    func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
                    # Derived Metrics v1: New base measures
                    func.coalesce(func.sum(MF.leads), 0).label("leads"),
                    func.coalesce(func.sum(MF.installs), 0).label("installs"),
                    func.coalesce(func.sum(MF.purchases), 0).label("purchases"),
                    func.coalesce(func.sum(MF.visitors), 0).label("visitors"),
                    func.coalesce(func.sum(MF.profit), 0).label("profit"),
                )
                .join(E, E.id == MF.entity_id)  # Join to leaf entity
                .join(leaf_to_ancestor, leaf_to_ancestor.c.leaf_id == E.id)  # Map to campaign
                .filter(E.workspace_id == workspace_id)
                .filter(cast(MF.event_date, Date).between(plan.start, plan.end))
                .group_by("group_id", "group_name")
            )
            
        elif plan.breakdown == "adset":
            # Get CTE that maps leaf entities to their adset ancestors
            leaf_to_ancestor = adset_ancestor_cte(db)
            
            breakdown_query = (
                db.query(
                    leaf_to_ancestor.c.ancestor_id.label("group_id"),
                    leaf_to_ancestor.c.ancestor_name.label("group_name"),
                    func.coalesce(func.sum(MF.spend), 0).label("spend"),
                    func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
                    func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
                    func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
                    func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
                    func.coalesce(func.sum(MF.leads), 0).label("leads"),
                    func.coalesce(func.sum(MF.installs), 0).label("installs"),
                    func.coalesce(func.sum(MF.purchases), 0).label("purchases"),
                    func.coalesce(func.sum(MF.visitors), 0).label("visitors"),
                    func.coalesce(func.sum(MF.profit), 0).label("profit"),
                )
                .join(E, E.id == MF.entity_id)
                .join(leaf_to_ancestor, leaf_to_ancestor.c.leaf_id == E.id)
                .filter(E.workspace_id == workspace_id)
                .filter(cast(MF.event_date, Date).between(plan.start, plan.end))
                .group_by("group_id", "group_name")
            )
            
        # Phase 7: Temporal breakdowns (day, week, month)
        elif plan.breakdown in ["day", "week", "month"]:
            
            # Map breakdown to SQL date_trunc period
            if plan.breakdown == "day":
                date_trunc_period = "day"
            elif plan.breakdown == "week":
                date_trunc_period = "week"
            elif plan.breakdown == "month":
                date_trunc_period = "month"
            else:
                raise ValueError(f"Unknown temporal breakdown: {plan.breakdown}")
            
            # Build temporal breakdown query
            breakdown_query = (
                db.query(
                    func.cast(func.date_trunc(date_trunc_period, MF.event_date), Date).label("group_name"),
                    # Aggregate all base measures
                    func.coalesce(func.sum(MF.spend), 0).label("spend"),
                    func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
                    func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
                    func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
                    func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
                    func.coalesce(func.sum(MF.leads), 0).label("leads"),
                    func.coalesce(func.sum(MF.installs), 0).label("installs"),
                    func.coalesce(func.sum(MF.purchases), 0).label("purchases"),
                    func.coalesce(func.sum(MF.visitors), 0).label("visitors"),
                    func.coalesce(func.sum(MF.profit), 0).label("profit"),
                )
                .join(E, E.id == MF.entity_id)
                .filter(E.workspace_id == workspace_id)
                .filter(cast(MF.event_date, Date).between(plan.start, plan.end))
                .group_by(func.date_trunc(date_trunc_period, MF.event_date))
            )
            
        else:
            # For "ad" breakdown, no rollup needed - facts are at the right level
            breakdown_query = (
                db.query(
                    E.name.label("group_name"),
                    func.coalesce(func.sum(MF.spend), 0).label("spend"),
                    func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
                    func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
                    func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
                    func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
                    func.coalesce(func.sum(MF.leads), 0).label("leads"),
                    func.coalesce(func.sum(MF.installs), 0).label("installs"),
                    func.coalesce(func.sum(MF.purchases), 0).label("purchases"),
                    func.coalesce(func.sum(MF.visitors), 0).label("visitors"),
                    func.coalesce(func.sum(MF.profit), 0).label("profit"),
                )
                .join(E, E.id == MF.entity_id)
                .filter(E.workspace_id == workspace_id)
                .filter(E.level == "ad")
                .filter(cast(MF.event_date, Date).between(plan.start, plan.end))
                .group_by(E.name)
            )
        
        # Apply filters (provider/status/entity_ids/entity_name)
        if plan.filters.get("provider"):
            breakdown_query = breakdown_query.filter(MF.provider == plan.filters["provider"])
        # CORRECTED: Include ALL entities by default (active + inactive)
        if plan.filters.get("status"):
            breakdown_query = breakdown_query.filter(E.status == plan.filters["status"])
        # Note: No default status filter - include all entities unless explicitly filtered
        if plan.filters.get("entity_ids"):
            breakdown_query = breakdown_query.filter(MF.entity_id.in_(plan.filters["entity_ids"]))
        
        # NEW: Named entity filtering in breakdowns
        # WHY: Enables "breakdown of Holiday Sale campaign performance"
        # HOW: Filter by entity name before grouping/aggregation
        # Works for campaign/adset/ad breakdowns (uses Entity join)
        if plan.filters.get("entity_name"):
            pattern = f"%{plan.filters['entity_name']}%"
            breakdown_query = breakdown_query.filter(E.name.ilike(pattern))
        
        # Apply thresholds as HAVING constraints (only for breakdowns)
        # WHY: Filters out insignificant entities (e.g., campaigns with $1 spend showing 10× ROAS)
        # IMPORTANT: Uses coalesce(sum(...), 0) to handle NULL aggregates safely
        # Reference: app/dsl/schema.py (Thresholds model) for field definitions
        query = plan.query  # Access original query for thresholds
        if query.thresholds:
            t = query.thresholds
            # Build list of HAVING conditions
            having_conditions = []
            
            if t.min_spend is not None:
                # Sum of spend must be >= min_spend threshold
                having_conditions.append(
                    func.coalesce(func.sum(MF.spend), 0) >= t.min_spend
                )
            
            if t.min_clicks is not None:
                # Sum of clicks must be >= min_clicks threshold
                having_conditions.append(
                    func.coalesce(func.sum(MF.clicks), 0) >= t.min_clicks
                )
            
            if t.min_conversions is not None:
                # Sum of conversions must be >= min_conversions threshold
                having_conditions.append(
                    func.coalesce(func.sum(MF.conversions), 0) >= t.min_conversions
                )
            
            # Apply all HAVING conditions (ANDed together)
            # WHY: Entity must meet ALL thresholds to be included
            for condition in having_conditions:
                breakdown_query = breakdown_query.having(condition)
        
        # ORDER BY the requested metric value (not just spend)
        # Build SQL expression for the derived metric to enable efficient DB-side ordering
        # NOTE: We must use the aggregate functions directly in ORDER BY, not column aliases
        # PostgreSQL requires this when using GROUP BY
        
        # Build ordering expression based on the requested metric
        # Uses direct aggregate expressions to avoid PostgreSQL grouping errors
        if metric_name == "roas":
            order_expr = func.coalesce(func.sum(MF.revenue), 0) / func.nullif(func.coalesce(func.sum(MF.spend), 0), 0)
        elif metric_name == "cpa":
            order_expr = func.coalesce(func.sum(MF.spend), 0) / func.nullif(func.coalesce(func.sum(MF.conversions), 0), 0)
        elif metric_name == "cvr":
            order_expr = func.coalesce(func.sum(MF.conversions), 0) / func.nullif(func.coalesce(func.sum(MF.clicks), 0), 0)
        elif metric_name == "ctr":
            order_expr = func.coalesce(func.sum(MF.clicks), 0) / func.nullif(func.coalesce(func.sum(MF.impressions), 0), 0)
        elif metric_name == "cpm":
            order_expr = (func.coalesce(func.sum(MF.spend), 0) / func.nullif(func.coalesce(func.sum(MF.impressions), 0), 0)) * 1000
        elif metric_name == "cpc":
            order_expr = func.coalesce(func.sum(MF.spend), 0) / func.nullif(func.coalesce(func.sum(MF.clicks), 0), 0)
        elif metric_name == "cpl":
            order_expr = func.coalesce(func.sum(MF.spend), 0) / func.nullif(func.coalesce(func.sum(MF.leads), 0), 0)
        elif metric_name == "cpi":
            order_expr = func.coalesce(func.sum(MF.spend), 0) / func.nullif(func.coalesce(func.sum(MF.installs), 0), 0)
        elif metric_name == "cpp":
            order_expr = func.coalesce(func.sum(MF.spend), 0) / func.nullif(func.coalesce(func.sum(MF.purchases), 0), 0)
        elif metric_name == "poas":
            order_expr = func.coalesce(func.sum(MF.profit), 0) / func.nullif(func.coalesce(func.sum(MF.spend), 0), 0)
        elif metric_name == "arpv":
            order_expr = func.coalesce(func.sum(MF.revenue), 0) / func.nullif(func.coalesce(func.sum(MF.visitors), 0), 0)
        elif metric_name == "aov":
            order_expr = func.coalesce(func.sum(MF.revenue), 0) / func.nullif(func.coalesce(func.sum(MF.conversions), 0), 0)
        elif metric_name == "spend":
            order_expr = func.coalesce(func.sum(MF.spend), 0)
        elif metric_name == "revenue":
            order_expr = func.coalesce(func.sum(MF.revenue), 0)
        elif metric_name == "clicks":
            order_expr = func.coalesce(func.sum(MF.clicks), 0)
        elif metric_name == "impressions":
            order_expr = func.coalesce(func.sum(MF.impressions), 0)
        elif metric_name == "conversions":
            order_expr = func.coalesce(func.sum(MF.conversions), 0)
        elif metric_name == "leads":
            order_expr = func.coalesce(func.sum(MF.leads), 0)
        elif metric_name == "installs":
            order_expr = func.coalesce(func.sum(MF.installs), 0)
        elif metric_name == "purchases":
            order_expr = func.coalesce(func.sum(MF.purchases), 0)
        elif metric_name == "visitors":
            order_expr = func.coalesce(func.sum(MF.visitors), 0)
        elif metric_name == "profit":
            order_expr = func.coalesce(func.sum(MF.profit), 0)
        else:
            # Fallback to spend if metric unknown
            order_expr = func.coalesce(func.sum(MF.spend), 0)
        
        # Apply ordering and limit
        # NEW: Dynamic ordering based on plan.sort_order
        # - desc(): Highest first (default) - for "which had the highest X"
        # - asc(): Lowest first - for "which had the lowest X"
        # nulls_last() ensures NULL values (from divide-by-zero) appear last regardless of sort order
        if plan.sort_order == "asc":
            rows = breakdown_query.order_by(order_expr.asc().nulls_last()).limit(plan.top_n).all()
        else:  # Default to desc
            rows = breakdown_query.order_by(order_expr.desc().nulls_last()).limit(plan.top_n).all()
        
        # Build breakdown list using Python-side formula registry for final 'value'
        # This ensures consistent calculation with the rest of the system
        # NEW: Include denominators (spend, clicks, conversions) for answer context
        # WHY: Enables AnswerBuilder to show supporting data (e.g., "Summer Sale had ROAS 3.2× with $1,234 spend")
        breakdown = []
        for row in rows:
            totals = row._asdict()
            # Use the same compute_metric function for consistency
            # Reference: app/metrics/registry.py (single source of truth for formulas)
            value = compute_metric(metric_name, totals)
            
            # Build breakdown item with value + denominators
            # Include all key measures that might be useful for answer generation
            item = {
                "label": str(row.group_name),
                "value": value,
                # Denominators: useful for explaining results in answers
                # Example: "Summer Sale had highest ROAS at 3.20× (Spend $1,234, Revenue $3,948)"
                "spend": totals.get("spend"),
                "clicks": totals.get("clicks"),
                "conversions": totals.get("conversions"),
                # Additional measures (optional, but helpful)
                "revenue": totals.get("revenue"),
                "impressions": totals.get("impressions"),
            }
            breakdown.append(item)
    
    # --- METRIC VALUE FILTERING (NEW - Phase 7) ---
    # Apply post-aggregation filtering based on metric values
    # WHY: Enables queries like "Show me campaigns with ROAS above 4"
    # HOW: Filter breakdown results after metric calculation
    if plan.filters.get("metric_filters") and breakdown:
        filtered_breakdown = []
        for item in breakdown:
            # Check if item meets all metric filter conditions
            meets_all_filters = True
            
            for filter_condition in plan.filters["metric_filters"]:
                filter_metric = filter_condition.get("metric")
                filter_operator = filter_condition.get("operator")
                filter_value = filter_condition.get("value")
                
                if not all([filter_metric, filter_operator, filter_value is not None]):
                    logger.warning(f"Invalid metric filter condition: {filter_condition}")
                    continue
                
                # Get the metric value for this item
                item_totals = {
                    "spend": item.get("spend", 0),
                    "revenue": item.get("revenue", 0),
                    "clicks": item.get("clicks", 0),
                    "impressions": item.get("impressions", 0),
                    "conversions": item.get("conversions", 0),
                    "leads": item.get("leads", 0),
                    "installs": item.get("installs", 0),
                    "purchases": item.get("purchases", 0),
                    "visitors": item.get("visitors", 0),
                    "profit": item.get("profit", 0),
                }
                
                try:
                    item_metric_value = compute_metric(filter_metric, item_totals)
                    
                    # Apply filter condition
                    if filter_operator == ">":
                        meets_condition = item_metric_value > filter_value
                    elif filter_operator == ">=":
                        meets_condition = item_metric_value >= filter_value
                    elif filter_operator == "<":
                        meets_condition = item_metric_value < filter_value
                    elif filter_operator == "<=":
                        meets_condition = item_metric_value <= filter_value
                    elif filter_operator == "=":
                        meets_condition = item_metric_value == filter_value
                    elif filter_operator == "!=":
                        meets_condition = item_metric_value != filter_value
                    else:
                        logger.warning(f"Unknown filter operator: {filter_operator}")
                        meets_condition = True
                    
                    if not meets_condition:
                        meets_all_filters = False
                        break
                        
                except Exception as e:
                    logger.error(f"Failed to evaluate metric filter {filter_condition}: {e}")
                    meets_all_filters = False
                    break
            
            if meets_all_filters:
                filtered_breakdown.append(item)
        
        breakdown = filtered_breakdown
        logger.info(f"[METRIC_FILTER] Applied {len(plan.filters['metric_filters'])} filters, {len(breakdown)} items remain")
    
    # --- WORKSPACE AVERAGE CALCULATION (NEW in v2.0.1) ---
    # Calculate workspace-wide average for comparison context
    # WHY: Enables "above/below your workspace average" insights in answers
    # Example: "Your Campaign X ROAS (2.45×) is above workspace average (2.30×)"
    # Create TimeRange from plan dates for workspace avg calculation
    time_range = TimeRange(start=plan.start, end=plan.end)
    workspace_avg = _calculate_workspace_avg(
        db=db,
        workspace_id=workspace_id,
        metric=metric_name,
        time_range=time_range
    )
    
    if workspace_avg is not None:
        logger.info(
            f"Calculated workspace average for {metric_name}: {workspace_avg} (query value: {summary_value})"
        )
    
    # --- BUILD RESULT ---
    return MetricResult(
        summary=summary_value,
        previous=previous_value,
        delta_pct=delta_pct,
        timeseries=timeseries,
        breakdown=breakdown,
        workspace_avg=workspace_avg  # NEW in v2.0.1
    )


def _calculate_workspace_avg(
    db: Session,
    workspace_id: str,
    metric: str,
    time_range: TimeRange
) -> Optional[float]:
    """
    WHAT: Calculate workspace-wide average for a metric over time range
    WHY: Provides comparison baseline for "above/below average" context
    WHERE: Called by _execute_metrics_plan() during metrics query execution
    
    CRITICAL: This function must NOT apply any filters from the original query.
    It should calculate the metric across ALL entities in the workspace.
    
    ARGS:
        db: Database session
        workspace_id: Workspace UUID (tenant isolation)
        metric: Metric name (e.g., "roas", "cpc")
        time_range: Time range for calculation (same as query)
    
    RETURNS:
        float: Workspace average for the metric, or None if cannot compute
    
    EXAMPLE:
        Query: "What's ROAS for Google campaigns?" (filter: provider=google)
        Main query summary: 4.2× (Google only)
        workspace_avg: 3.8× (ALL platforms)
        Result: Different values ✅
    
    REFERENCES:
        - Uses: app/metrics/registry.py::compute_metric()
        - Uses: app/metrics/registry.py::get_required_bases()
        - Docs: QA_SYSTEM_ARCHITECTURE.md (Workspace Comparison)
    """
    MF, E = models.MetricFact, models.Entity
    
    try:
        # Get required base measures for this metric
        dependencies = get_required_bases(metric)
        if not dependencies:
            logger.warning(f"[WORKSPACE_AVG] Unknown metric: {metric}")
            return None
        
        logger.info(f"[WORKSPACE_AVG] Calculating for metric: {metric}")
        logger.info(f"[WORKSPACE_AVG] Dependencies: {dependencies}")
        logger.info(f"[WORKSPACE_AVG] Time range: start={time_range.start}, end={time_range.end}, last_n_days={time_range.last_n_days}")
        
        # Base query: ALL entities in workspace (NO FILTERS except workspace_id and time)
        # CRITICAL: Do NOT apply provider, level, status, or entity_ids filters
        query = (
            db.query(
                *[func.coalesce(func.sum(getattr(MF, dep)), 0).label(dep) 
                  for dep in dependencies]
            )
            .join(E, E.id == MF.entity_id)
            .filter(E.workspace_id == workspace_id)  # ✅ Only workspace filter
        )
        
        logger.info(f"[WORKSPACE_AVG] Query filters: workspace_id={workspace_id}")
        
        # Apply time range filter (but NO other filters)
        if time_range.start and time_range.end:
            query = query.filter(
                cast(MF.event_date, Date).between(
                    time_range.start, time_range.end
                )
            )
            logger.info(f"[WORKSPACE_AVG] Time filter: {time_range.start} to {time_range.end}")
        elif time_range.last_n_days:
            cutoff = datetime.now() - timedelta(days=time_range.last_n_days)
            query = query.filter(
                cast(MF.event_date, Date) >= cutoff.date()
            )
            logger.info(f"[WORKSPACE_AVG] Time filter: last {time_range.last_n_days} days")
        
        # Execute
        row = query.first()
        if not row:
            logger.warning(f"[WORKSPACE_AVG] No data found for workspace {workspace_id}")
            return None
        
        # Compute metric (with divide-by-zero protection)
        base_measures = {dep: getattr(row, dep) or 0 for dep in dependencies}
        workspace_avg = compute_metric(metric, base_measures)
        
        logger.info(f"[WORKSPACE_AVG] Base measures: {base_measures}")
        logger.info(f"[WORKSPACE_AVG] Calculated workspace avg: {workspace_avg}")
        
        return workspace_avg
    
    except Exception as e:
        logger.error(f"[WORKSPACE_AVG] Failed to calculate workspace avg for {metric}: {e}")
        return None


def _execute_multi_metric_plan(
    db: Session,
    workspace_id: str,
    plan: Plan,
    query: MetricQuery
) -> Dict[str, Any]:
    """
    Execute a multi-metric query plan (Phase 7).
    
    This function handles queries that request multiple metrics at once.
    It executes the same base aggregation for all metrics and returns
    a structured result with all requested metric values.
    
    Args:
        db: SQLAlchemy database session
        workspace_id: Workspace UUID for scoping
        plan: Execution plan with dates, filters
        query: Original MetricQuery with list of metrics
        
    Returns:
        Dict with structure:
        {
            "metrics": {
                "spend": {"summary": 1000.0, "previous": 900.0, "delta_pct": 11.1},
                "revenue": {"summary": 2000.0, "previous": 1800.0, "delta_pct": 11.1},
                "roas": {"summary": 2.0, "previous": 2.0, "delta_pct": 0.0}
            },
            "timeseries": [...],  # Optional
            "breakdown": [...]    # Optional
        }
    """
    from typing import Dict, Any, List
    
    logger.info(f"[MULTI_METRIC] Executing plan for metrics: {query.metric}")
    
    # Get the base aggregation (same for all metrics)
    MF, E = models.MetricFact, models.Entity
    
    base_query = (
        db.query(
            # Original base measures
            func.coalesce(func.sum(MF.spend), 0).label("spend"),
            func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
            func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
            func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
            func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
            # Derived Metrics v1: New base measures
            func.coalesce(func.sum(MF.leads), 0).label("leads"),
            func.coalesce(func.sum(MF.installs), 0).label("installs"),
            func.coalesce(func.sum(MF.purchases), 0).label("purchases"),
            func.coalesce(func.sum(MF.visitors), 0).label("visitors"),
            func.coalesce(func.sum(MF.profit), 0).label("profit"),
        )
        .join(E, E.id == MF.entity_id)
        .filter(E.workspace_id == workspace_id)  # TENANT SCOPING
        .filter(cast(MF.event_date, Date).between(plan.start, plan.end))
    )
    
    # Apply filters (same logic as single metric)
    if plan.filters.get("provider"):
        base_query = base_query.filter(MF.provider == plan.filters["provider"])
    if plan.filters.get("level"):
        # BUG FIX: Use E.level (Entity table) not MF.level (MetricFact doesn't have level field)
        base_query = base_query.filter(E.level == plan.filters["level"])
    # CORRECTED: Include ALL entities by default (active + inactive)
    # WHY: Inactive campaigns still generated revenue and should be included in financial analysis
    # IMPACT: QA now matches Finance page behavior which includes all entities
    if plan.filters.get("status"):
        base_query = base_query.filter(E.status == plan.filters["status"])
    # Note: No default status filter - include all entities unless explicitly filtered
    if plan.filters.get("entity_ids"):
        base_query = base_query.filter(MF.entity_id.in_(plan.filters["entity_ids"]))
    
    # Named entity filtering
    if plan.filters.get("entity_name"):
        pattern = f"%{plan.filters['entity_name']}%"
        base_query = base_query.filter(E.name.ilike(pattern))
    
    # Execute base query
    totals_now = base_query.one()._asdict()
    
    # Calculate each requested metric
    metrics_result = {}
    for metric_name in query.metric:
        try:
            # Calculate current period value
            current_value = compute_metric(metric_name, totals_now)
            
            # Calculate previous period if requested
            previous_value = None
            delta_pct = None
            if plan.need_previous:
                # Calculate previous period totals
                prev_start = plan.start - timedelta(days=(plan.end - plan.start).days + 1)
                prev_end = plan.start - timedelta(days=1)
                
                prev_query = (
                    db.query(
                        func.coalesce(func.sum(MF.spend), 0).label("spend"),
                        func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
                        func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
                        func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
                        func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
                        func.coalesce(func.sum(MF.leads), 0).label("leads"),
                        func.coalesce(func.sum(MF.installs), 0).label("installs"),
                        func.coalesce(func.sum(MF.purchases), 0).label("purchases"),
                        func.coalesce(func.sum(MF.visitors), 0).label("visitors"),
                        func.coalesce(func.sum(MF.profit), 0).label("profit"),
                    )
                    .join(E, E.id == MF.entity_id)
                    .filter(E.workspace_id == workspace_id)
                    .filter(cast(MF.event_date, Date).between(prev_start, prev_end))
                )
                
                # Apply same filters to previous period
                if plan.filters.get("provider"):
                    prev_query = prev_query.filter(MF.provider == plan.filters["provider"])
                if plan.filters.get("level"):
                    # BUG FIX: Use E.level (Entity table) not MF.level (MetricFact doesn't have level field)
                    prev_query = prev_query.filter(E.level == plan.filters["level"])
                if plan.filters.get("status"):
                    prev_query = prev_query.filter(E.status == plan.filters["status"])
                if plan.filters.get("entity_ids"):
                    prev_query = prev_query.filter(MF.entity_id.in_(plan.filters["entity_ids"]))
                if plan.filters.get("entity_name"):
                    pattern = f"%{plan.filters['entity_name']}%"
                    prev_query = prev_query.filter(E.name.ilike(pattern))
                
                totals_prev = prev_query.one()._asdict()
                previous_value = compute_metric(metric_name, totals_prev)
                
                # Calculate delta percentage
                if previous_value is not None and previous_value != 0 and current_value is not None:
                    delta_pct = ((current_value - previous_value) / previous_value) * 100
            
            metrics_result[metric_name] = {
                "summary": current_value,
                "previous": previous_value,
                "delta_pct": delta_pct
            }
            
        except Exception as e:
            logger.error(f"[MULTI_METRIC] Failed to calculate {metric_name}: {e}")
            metrics_result[metric_name] = {
                "summary": None,
                "previous": None,
                "delta_pct": None
            }
    
    # Build result structure
    result = {
        "metrics": metrics_result,
        "query_type": "multi_metrics"
    }
    
    # Add timeseries if requested (simplified for multi-metric)
    if plan.need_timeseries:
        logger.info("[MULTI_METRIC] Timeseries not yet implemented for multi-metric queries")
        result["timeseries"] = []
    
    # Add breakdown if requested (simplified for multi-metric)
    if plan.breakdown:
        logger.info("[MULTI_METRIC] Breakdown not yet implemented for multi-metric queries")
        result["breakdown"] = []
    
    logger.info(f"[MULTI_METRIC] Completed execution for {len(query.metric)} metrics")
    return result
