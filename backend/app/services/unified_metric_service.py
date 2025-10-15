"""
Unified Metric Service
=====================

Single source of truth for all metric calculations across the system.
Powers QA, KPI, entity performance, finance, and metrics endpoints.

WHAT: Centralized metric aggregation service
WHY: Eliminates data mismatches between endpoints
HOW: Uses existing metrics registry with consistent filtering

Design Principles:
- Single source of truth for all metric calculations
- Consistent filtering logic across all endpoints
- Workspace-scoped security at SQL level
- Built-in divide-by-zero guards
- Standardized input/output contracts

Usage:
    >>> service = UnifiedMetricService(db)
    >>> result = service.get_summary(
    ...     workspace_id="...",
    ...     metrics=["roas", "cpc"],
    ...     time_range=TimeRange(last_n_days=7),
    ...     filters=MetricFilters()
    ... )
    >>> print(result.metrics["roas"].value)
    6.29

References:
- app/metrics/registry.py: Metric formulas and dependencies
- app/metrics/formulas.py: Pure calculation functions
- app/models.py: Database models (MetricFact, Entity)
"""

from __future__ import annotations

from datetime import date, datetime, timedelta
from typing import Optional, List, Dict, Any, Union
from dataclasses import dataclass
import logging

from sqlalchemy.orm import Session
from sqlalchemy import func, cast, Date, desc, asc

from app import models
from app.metrics.registry import compute_metric, get_required_bases, is_base_measure
from app.dsl.schema import TimeRange

logger = logging.getLogger(__name__)


@dataclass
class MetricFilters:
    """
    Standardized filter contract for all metric queries.
    
    Default behavior: Include ALL entities unless explicitly filtered.
    This matches the Finance page behavior where inactive campaigns
    still generated revenue and should be included.
    """
    provider: Optional[str] = None
    level: Optional[str] = None
    status: Optional[str] = None  # None = include all, "active" = active only
    entity_ids: Optional[List[str]] = None
    entity_name: Optional[str] = None
    metric_filters: Optional[List[Dict[str, Any]]] = None
    
    def normalize_provider(self) -> Optional[str]:
        """
        Normalize provider enum format to string.
        
        Handles both "meta" and "ProviderEnum.meta" formats.
        """
        if not self.provider:
            return None
        if self.provider.startswith("ProviderEnum."):
            return self.provider.split(".")[1]
        return self.provider


@dataclass
class MetricValue:
    """Single metric value with optional comparison."""
    value: Optional[float]
    previous: Optional[float] = None
    delta_pct: Optional[float] = None


@dataclass
class MetricSummary:
    """Summary results for multiple metrics."""
    metrics: Dict[str, MetricValue]
    workspace_avg: Optional[float] = None


@dataclass
class MetricTimePoint:
    """Single time point in a timeseries."""
    date: str
    value: Optional[float]


@dataclass
class MetricBreakdownItem:
    """Single item in a breakdown result."""
    label: str
    value: Optional[float]
    spend: Optional[float] = None
    clicks: Optional[float] = None
    conversions: Optional[float] = None
    revenue: Optional[float] = None
    impressions: Optional[float] = None


class UnifiedMetricService:
    """
    Unified metric aggregation service.
    
    Single source of truth for all metric calculations across the system.
    Ensures consistent filtering, calculations, and results.
    """
    
    def __init__(self, db: Session):
        self.db = db
        self.MF = models.MetricFact
        self.E = models.Entity
    
    def get_summary(
        self,
        workspace_id: str,
        metrics: List[str],
        time_range: TimeRange,
        filters: MetricFilters,
        compare_to_previous: bool = False
    ) -> MetricSummary:
        """
        Get summary values for multiple metrics.
        
        Args:
            workspace_id: Workspace UUID for scoping
            metrics: List of metric names to calculate
            time_range: Time range for calculation
            filters: Filtering criteria
            compare_to_previous: Include previous period comparison
            
        Returns:
            MetricSummary with all requested metrics
            
        Example:
            >>> service = UnifiedMetricService(db)
            >>> result = service.get_summary(
            ...     workspace_id="...",
            ...     metrics=["roas", "cpc"],
            ...     time_range=TimeRange(last_n_days=7),
            ...     filters=MetricFilters()
            ... )
            >>> print(result.metrics["roas"].value)
            6.29
        """
        logger.info(f"[UNIFIED_METRICS] Getting summary for {len(metrics)} metrics")
        
        # Resolve time range
        start_date, end_date = self._resolve_time_range(time_range)
        
        # Get current period totals
        current_totals = self._get_base_totals(
            workspace_id, start_date, end_date, filters
        )
        
        # Get previous period totals if requested
        previous_totals = None
        if compare_to_previous:
            prev_start, prev_end = self._get_previous_period(start_date, end_date)
            previous_totals = self._get_base_totals(
                workspace_id, prev_start, prev_end, filters
            )
        
        # Calculate all requested metrics
        metric_results = {}
        for metric_name in metrics:
            current_value = compute_metric(metric_name, current_totals)
            previous_value = None
            delta_pct = None
            
            if previous_totals:
                previous_value = compute_metric(metric_name, previous_totals)
                if previous_value is not None and previous_value != 0 and current_value is not None:
                    delta_pct = (current_value - previous_value) / previous_value
            
            metric_results[metric_name] = MetricValue(
                value=current_value,
                previous=previous_value,
                delta_pct=delta_pct
            )
        
        # Calculate workspace average for primary metric
        workspace_avg = None
        if metrics:
            workspace_avg = self.get_workspace_average(
                workspace_id, metrics[0], time_range
            )
        
        return MetricSummary(
            metrics=metric_results,
            workspace_avg=workspace_avg
        )
    
    def get_timeseries(
        self,
        workspace_id: str,
        metrics: List[str],
        time_range: TimeRange,
        filters: MetricFilters
    ) -> List[MetricTimePoint]:
        """
        Get daily timeseries data for metrics.
        
        Args:
            workspace_id: Workspace UUID for scoping
            metrics: List of metric names to calculate
            time_range: Time range for calculation
            filters: Filtering criteria
            
        Returns:
            List of daily metric values
            
        Example:
            >>> service = UnifiedMetricService(db)
            >>> timeseries = service.get_timeseries(
            ...     workspace_id="...",
            ...     metrics=["roas"],
            ...     time_range=TimeRange(last_n_days=7),
            ...     filters=MetricFilters()
            ... )
            >>> print(timeseries[0].date)
            2025-10-08
        """
        logger.info(f"[UNIFIED_METRICS] Getting timeseries for {len(metrics)} metrics")
        
        # Resolve time range
        start_date, end_date = self._resolve_time_range(time_range)
        
        # Build timeseries query
        query = (
            self.db.query(
                cast(self.MF.event_date, Date).label("date"),
                func.coalesce(func.sum(self.MF.spend), 0).label("spend"),
                func.coalesce(func.sum(self.MF.revenue), 0).label("revenue"),
                func.coalesce(func.sum(self.MF.clicks), 0).label("clicks"),
                func.coalesce(func.sum(self.MF.impressions), 0).label("impressions"),
                func.coalesce(func.sum(self.MF.conversions), 0).label("conversions"),
                func.coalesce(func.sum(self.MF.leads), 0).label("leads"),
                func.coalesce(func.sum(self.MF.installs), 0).label("installs"),
                func.coalesce(func.sum(self.MF.purchases), 0).label("purchases"),
                func.coalesce(func.sum(self.MF.visitors), 0).label("visitors"),
                func.coalesce(func.sum(self.MF.profit), 0).label("profit"),
            )
            .join(self.E, self.E.id == self.MF.entity_id)
            .filter(self.E.workspace_id == workspace_id)
            .filter(cast(self.MF.event_date, Date).between(start_date, end_date))
            .group_by(cast(self.MF.event_date, Date))
            .order_by(cast(self.MF.event_date, Date))
        )
        
        # Apply filters
        query = self._apply_filters(query, filters)
        
        # Execute query
        rows = query.all()
        
        # Build timeseries results
        timeseries = []
        for row in rows:
            totals = row._asdict()
            # For now, return the primary metric (first in list)
            # TODO: Support multiple metrics in timeseries
            primary_metric = metrics[0] if metrics else "roas"
            value = compute_metric(primary_metric, totals)
            
            timeseries.append(MetricTimePoint(
                date=str(row.date),
                value=value
            ))
        
        return timeseries
    
    def get_breakdown(
        self,
        workspace_id: str,
        metric: str,
        time_range: TimeRange,
        filters: MetricFilters,
        breakdown_dimension: str,
        top_n: int = 5,
        sort_order: str = "desc"
    ) -> List[MetricBreakdownItem]:
        """
        Get breakdown results for a metric by dimension.
        
        Args:
            workspace_id: Workspace UUID for scoping
            metric: Metric name to calculate
            time_range: Time range for calculation
            filters: Filtering criteria
            breakdown_dimension: Dimension to group by (provider, campaign, adset, ad)
            top_n: Number of top results to return
            sort_order: Sort order ("asc" or "desc")
            
        Returns:
            List of breakdown items
            
        Example:
            >>> service = UnifiedMetricService(db)
            >>> breakdown = service.get_breakdown(
            ...     workspace_id="...",
            ...     metric="roas",
            ...     time_range=TimeRange(last_n_days=7),
            ...     filters=MetricFilters(),
            ...     breakdown_dimension="campaign"
            ... )
            >>> print(breakdown[0].label)
            Summer Sale Campaign
        """
        logger.info(f"[UNIFIED_METRICS] Getting breakdown for {metric} by {breakdown_dimension}")
        
        # Resolve time range
        start_date, end_date = self._resolve_time_range(time_range)
        
        # Build breakdown query based on dimension
        if breakdown_dimension == "provider":
            query = self._build_provider_breakdown_query(
                workspace_id, start_date, end_date, filters
            )
        elif breakdown_dimension in ["campaign", "adset", "ad"]:
            query = self._build_entity_breakdown_query(
                workspace_id, start_date, end_date, filters, breakdown_dimension
            )
        else:
            raise ValueError(f"Unsupported breakdown dimension: {breakdown_dimension}")
        
        # Apply ordering and limit
        if sort_order == "asc":
            query = query.order_by(asc(self._get_order_expression(metric)))
        else:
            query = query.order_by(desc(self._get_order_expression(metric)))
        
        # Execute query to get all results first
        rows = query.all()
        
        # Build breakdown results
        breakdown = []
        for row in rows:
            totals = row._asdict()
            value = compute_metric(metric, totals)
            
            # Apply metric filters if specified
            if filters.metric_filters:
                if not self._passes_metric_filters(metric, value, filters.metric_filters):
                    continue
            
            breakdown.append(MetricBreakdownItem(
                label=str(row.group_name),
                value=value,
                spend=totals.get("spend"),
                clicks=totals.get("clicks"),
                conversions=totals.get("conversions"),
                revenue=totals.get("revenue"),
                impressions=totals.get("impressions")
            ))
        
        # Apply top_n limit after filtering
        return breakdown[:top_n]
    
    def get_workspace_average(
        self,
        workspace_id: str,
        metric: str,
        time_range: TimeRange
    ) -> Optional[float]:
        """
        Get workspace-wide average for a metric.
        
        CRITICAL: This method does NOT apply any filters from the original query.
        It calculates the metric across ALL entities in the workspace to provide
        a true baseline for comparison.
        
        Args:
            workspace_id: Workspace UUID for scoping
            metric: Metric name to calculate
            time_range: Time range for calculation
            
        Returns:
            Workspace average value, or None if cannot compute
            
        Example:
            >>> service = UnifiedMetricService(db)
            >>> avg = service.get_workspace_average(
            ...     workspace_id="...",
            ...     metric="roas",
            ...     time_range=TimeRange(last_n_days=7)
            ... )
            >>> print(avg)
            6.29
        """
        logger.info(f"[UNIFIED_METRICS] Getting workspace average for {metric}")
        
        # Resolve time range
        start_date, end_date = self._resolve_time_range(time_range)
        
        # Get required base measures for this metric
        dependencies = get_required_bases(metric)
        if not dependencies:
            logger.warning(f"[UNIFIED_METRICS] Unknown metric: {metric}")
            return None
        
        # Build query for ALL entities (no filters except workspace and time)
        query = (
            self.db.query(
                *[func.coalesce(func.sum(getattr(self.MF, dep)), 0).label(dep) 
                  for dep in dependencies]
            )
            .join(self.E, self.E.id == self.MF.entity_id)
            .filter(self.E.workspace_id == workspace_id)
            .filter(cast(self.MF.event_date, Date).between(start_date, end_date))
        )
        
        # Execute query
        row = query.first()
        if not row:
            logger.warning(f"[UNIFIED_METRICS] No data found for workspace {workspace_id}")
            return None
        
        # Compute metric
        base_measures = {dep: getattr(row, dep) or 0 for dep in dependencies}
        workspace_avg = compute_metric(metric, base_measures)
        
        logger.info(f"[UNIFIED_METRICS] Workspace average for {metric}: {workspace_avg}")
        return workspace_avg
    
    def _resolve_time_range(self, time_range: TimeRange) -> tuple[date, date]:
        """Resolve TimeRange to start/end dates."""
        if time_range.start and time_range.end:
            return (time_range.start, time_range.end)
        
        n = time_range.last_n_days or 7
        end_date = date.today()
        start_date = end_date - timedelta(days=n - 1)
        return (start_date, end_date)
    
    def _get_previous_period(self, start_date: date, end_date: date) -> tuple[date, date]:
        """Calculate previous period dates."""
        period_length = (end_date - start_date).days + 1
        prev_end = start_date - timedelta(days=1)
        prev_start = prev_end - timedelta(days=period_length - 1)
        return (prev_start, prev_end)
    
    def _get_base_totals(
        self,
        workspace_id: str,
        start_date: date,
        end_date: date,
        filters: MetricFilters
    ) -> Dict[str, float]:
        """Get aggregated base measures for a time period."""
        query = (
            self.db.query(
                func.coalesce(func.sum(self.MF.spend), 0).label("spend"),
                func.coalesce(func.sum(self.MF.revenue), 0).label("revenue"),
                func.coalesce(func.sum(self.MF.clicks), 0).label("clicks"),
                func.coalesce(func.sum(self.MF.impressions), 0).label("impressions"),
                func.coalesce(func.sum(self.MF.conversions), 0).label("conversions"),
                func.coalesce(func.sum(self.MF.leads), 0).label("leads"),
                func.coalesce(func.sum(self.MF.installs), 0).label("installs"),
                func.coalesce(func.sum(self.MF.purchases), 0).label("purchases"),
                func.coalesce(func.sum(self.MF.visitors), 0).label("visitors"),
                func.coalesce(func.sum(self.MF.profit), 0).label("profit"),
            )
            .join(self.E, self.E.id == self.MF.entity_id)
            .filter(self.E.workspace_id == workspace_id)
            .filter(cast(self.MF.event_date, Date).between(start_date, end_date))
        )
        
        # Apply filters
        query = self._apply_filters(query, filters)
        
        # Execute query
        row = query.first()
        if not row:
            return {}
        
        return row._asdict()
    
    def _apply_filters(self, query, filters: MetricFilters):
        """Apply filters to a query."""
        # Provider filter
        if filters.provider:
            provider_value = filters.normalize_provider()
            query = query.filter(self.MF.provider == provider_value)
        
        # Level filter (use E.level, not MF.level)
        if filters.level:
            query = query.filter(self.E.level == filters.level)
        
        # Status filter (default: include all entities)
        if filters.status:
            query = query.filter(self.E.status == filters.status)
        
        # Entity IDs filter
        if filters.entity_ids:
            query = query.filter(self.MF.entity_id.in_(filters.entity_ids))
        
        # Entity name filter (case-insensitive partial match)
        if filters.entity_name:
            pattern = f"%{filters.entity_name}%"
            query = query.filter(self.E.name.ilike(pattern))
        
        return query
    
    def _build_provider_breakdown_query(self, workspace_id: str, start_date: date, end_date: date, filters: MetricFilters):
        """Build query for provider breakdown."""
        query = (
            self.db.query(
                self.MF.provider.label("group_name"),
                func.coalesce(func.sum(self.MF.spend), 0).label("spend"),
                func.coalesce(func.sum(self.MF.revenue), 0).label("revenue"),
                func.coalesce(func.sum(self.MF.clicks), 0).label("clicks"),
                func.coalesce(func.sum(self.MF.impressions), 0).label("impressions"),
                func.coalesce(func.sum(self.MF.conversions), 0).label("conversions"),
                func.coalesce(func.sum(self.MF.leads), 0).label("leads"),
                func.coalesce(func.sum(self.MF.installs), 0).label("installs"),
                func.coalesce(func.sum(self.MF.purchases), 0).label("purchases"),
                func.coalesce(func.sum(self.MF.visitors), 0).label("visitors"),
                func.coalesce(func.sum(self.MF.profit), 0).label("profit"),
            )
            .join(self.E, self.E.id == self.MF.entity_id)
            .filter(self.E.workspace_id == workspace_id)
            .filter(cast(self.MF.event_date, Date).between(start_date, end_date))
            .group_by(self.MF.provider)
        )
        
        return self._apply_filters(query, filters)
    
    def _build_entity_breakdown_query(self, workspace_id: str, start_date: date, end_date: date, filters: MetricFilters, level: str):
        """Build query for entity breakdown (campaign/adset/ad)."""
        # For now, implement simple ad-level breakdown
        # TODO: Add hierarchy support for campaign/adset rollups
        query = (
            self.db.query(
                self.E.name.label("group_name"),
                func.coalesce(func.sum(self.MF.spend), 0).label("spend"),
                func.coalesce(func.sum(self.MF.revenue), 0).label("revenue"),
                func.coalesce(func.sum(self.MF.clicks), 0).label("clicks"),
                func.coalesce(func.sum(self.MF.impressions), 0).label("impressions"),
                func.coalesce(func.sum(self.MF.conversions), 0).label("conversions"),
                func.coalesce(func.sum(self.MF.leads), 0).label("leads"),
                func.coalesce(func.sum(self.MF.installs), 0).label("installs"),
                func.coalesce(func.sum(self.MF.purchases), 0).label("purchases"),
                func.coalesce(func.sum(self.MF.visitors), 0).label("visitors"),
                func.coalesce(func.sum(self.MF.profit), 0).label("profit"),
            )
            .join(self.E, self.E.id == self.MF.entity_id)
            .filter(self.E.workspace_id == workspace_id)
            .filter(self.E.level == level)
            .filter(cast(self.MF.event_date, Date).between(start_date, end_date))
            .group_by(self.E.name)
        )
        
        return self._apply_filters(query, filters)
    
    def _get_order_expression(self, metric: str):
        """Get SQL expression for ordering by metric."""
        if metric == "roas":
            return func.coalesce(func.sum(self.MF.revenue), 0) / func.nullif(func.coalesce(func.sum(self.MF.spend), 0), 0)
        elif metric == "cpc":
            return func.coalesce(func.sum(self.MF.spend), 0) / func.nullif(func.coalesce(func.sum(self.MF.clicks), 0), 0)
        elif metric == "cpa":
            return func.coalesce(func.sum(self.MF.spend), 0) / func.nullif(func.coalesce(func.sum(self.MF.conversions), 0), 0)
        elif metric == "ctr":
            return func.coalesce(func.sum(self.MF.clicks), 0) / func.nullif(func.coalesce(func.sum(self.MF.impressions), 0), 0)
        elif metric == "cpm":
            return (func.coalesce(func.sum(self.MF.spend), 0) / func.nullif(func.coalesce(func.sum(self.MF.impressions), 0), 0)) * 1000
        elif metric == "spend":
            return func.coalesce(func.sum(self.MF.spend), 0)
        elif metric == "revenue":
            return func.coalesce(func.sum(self.MF.revenue), 0)
        elif metric == "clicks":
            return func.coalesce(func.sum(self.MF.clicks), 0)
        elif metric == "conversions":
            return func.coalesce(func.sum(self.MF.conversions), 0)
        else:
            # Fallback to spend
            return func.coalesce(func.sum(self.MF.spend), 0)
    
    def _passes_metric_filters(self, metric: str, value: Optional[float], metric_filters: List[Dict[str, Any]]) -> bool:
        """
        Check if a metric value passes the specified filters.
        
        Args:
            metric: The metric name being checked
            value: The calculated metric value
            metric_filters: List of filter conditions
            
        Returns:
            True if the value passes all filters, False otherwise
            
        Example:
            >>> filters = [{"metric": "roas", "operator": ">", "value": 4}]
            >>> service._passes_metric_filters("roas", 5.2, filters)
            True
        """
        if value is None:
            return False
        
        for filter_condition in metric_filters:
            filter_metric = filter_condition.get("metric")
            operator = filter_condition.get("operator")
            filter_value = filter_condition.get("value")
            
            # Only apply filters for the current metric
            if filter_metric != metric:
                continue
            
            # Apply the filter condition
            if operator == ">":
                if not (value > filter_value):
                    return False
            elif operator == ">=":
                if not (value >= filter_value):
                    return False
            elif operator == "<":
                if not (value < filter_value):
                    return False
            elif operator == "<=":
                if not (value <= filter_value):
                    return False
            elif operator == "=":
                if not (value == filter_value):
                    return False
            elif operator == "!=":
                if not (value != filter_value):
                    return False
            else:
                logger.warning(f"[UNIFIED_METRICS] Unknown operator: {operator}")
                continue
        
        return True
    
    def get_entity_list(
        self,
        workspace_id: str,
        filters: MetricFilters,
        level: Optional[str] = None,
        limit: int = 50
    ) -> List[Dict[str, Any]]:
        """
        Get list of entities matching filters.
        
        Args:
            workspace_id: Workspace UUID for scoping
            filters: Filtering criteria
            level: Entity level to filter by (campaign, adset, ad)
            limit: Maximum number of entities to return
            
        Returns:
            List of entity dictionaries with name, status, level, provider
            
        Example:
            >>> service = UnifiedMetricService(db)
            >>> entities = service.get_entity_list(
            ...     workspace_id="...",
            ...     filters=MetricFilters(status="active"),
            ...     level="campaign"
            ... )
            >>> print(entities[0]["name"])
            Summer Sale Campaign
        """
        logger.info(f"[UNIFIED_METRICS] Getting entity list for level: {level}")
        
        # Build base query with provider from MetricFact (distinct to avoid duplicates)
        query = (
            self.db.query(
                self.E.id,
                self.E.name,
                self.E.status,
                self.E.level,
                models.MetricFact.provider.label("provider")
            )
            .join(models.MetricFact, models.MetricFact.entity_id == self.E.id)
            .filter(self.E.workspace_id == workspace_id)
            .distinct()
        )
        
        # Apply level filter if specified
        if level:
            query = query.filter(self.E.level == level)
        
        # Apply other filters
        query = self._apply_entity_filters(query, filters)
        
        # Order by name and limit
        query = query.order_by(self.E.name).limit(limit)
        
        # Execute query
        rows = query.all()
        
        # Convert to dictionaries
        entities = []
        for row in rows:
            entities.append({
                "id": str(row.id),
                "name": row.name,
                "status": row.status,
                "level": row.level,
                "provider": row.provider
            })
        
        return entities
    
    def get_time_based_breakdown(
        self,
        workspace_id: str,
        metric: str,
        time_range: TimeRange,
        filters: MetricFilters,
        breakdown_dimension: str,
        top_n: int = 5,
        sort_order: str = "desc"
    ) -> List[MetricBreakdownItem]:
        """
        Get time-based breakdown results for a metric.
        
        Args:
            workspace_id: Workspace UUID for scoping
            metric: Metric name to calculate
            time_range: Time range for calculation
            filters: Filtering criteria
            breakdown_dimension: Time dimension to group by (day, week, month)
            top_n: Number of top results to return
            sort_order: Sort order ("asc" or "desc")
            
        Returns:
            List of breakdown items with time labels
            
        Example:
            >>> service = UnifiedMetricService(db)
            >>> breakdown = service.get_time_based_breakdown(
            ...     workspace_id="...",
            ...     metric="cpc",
            ...     time_range=TimeRange(last_n_days=7),
            ...     filters=MetricFilters(),
            ...     breakdown_dimension="day"
            ... )
            >>> print(breakdown[0].label)
            2025-10-15
        """
        logger.info(f"[UNIFIED_METRICS] Getting time-based breakdown for {metric} by {breakdown_dimension}")
        
        # Resolve time range
        start_date, end_date = self._resolve_time_range(time_range)
        
        # Build time-based breakdown query
        query = self._build_time_breakdown_query(
            workspace_id, start_date, end_date, filters, breakdown_dimension
        )
        
        # Apply ordering and limit
        if sort_order == "asc":
            query = query.order_by(asc(self._get_time_order_expression(metric, breakdown_dimension)))
        else:
            query = query.order_by(desc(self._get_time_order_expression(metric, breakdown_dimension)))
        
        # Execute query to get all results first
        rows = query.all()
        
        # Build breakdown results
        breakdown = []
        for row in rows:
            totals = row._asdict()
            value = compute_metric(metric, totals)
            
            # Apply metric filters if specified
            if filters.metric_filters:
                if not self._passes_metric_filters(metric, value, filters.metric_filters):
                    continue
            
            breakdown.append(MetricBreakdownItem(
                label=str(row.group_name),
                value=value,
                spend=totals.get("spend"),
                clicks=totals.get("clicks"),
                conversions=totals.get("conversions"),
                revenue=totals.get("revenue"),
                impressions=totals.get("impressions")
            ))
        
        # Apply top_n limit after filtering
        return breakdown[:top_n]
    
    def get_entity_goals(self, workspace_id: str, entity_names: List[str]) -> Dict[str, str]:
        """
        Get goals for entities by name.
        
        Args:
            workspace_id: Workspace UUID for scoping
            entity_names: List of entity names to look up
            
        Returns:
            Dict mapping entity names to their goals (or None if not found)
        """
        if not entity_names:
            return {}
        
        # Build query to find entities by name
        entities = (
            self.db.query(self.E.name, self.E.goal)
            .filter(self.E.workspace_id == workspace_id)
            .filter(self.E.name.in_(entity_names))
            .all()
        )
        
        return {entity.name: entity.goal.value if entity.goal else None for entity in entities}
    
    def _apply_entity_filters(self, query, filters: MetricFilters):
        """Apply filters to entity queries (not metric queries)."""
        # Provider filter (from MetricFact)
        if filters.provider:
            provider_value = filters.normalize_provider()
            query = query.filter(models.MetricFact.provider == provider_value)
        
        # Level filter
        if filters.level:
            query = query.filter(self.E.level == filters.level)
        
        # Status filter
        if filters.status:
            query = query.filter(self.E.status == filters.status)
        
        # Entity IDs filter
        if filters.entity_ids:
            query = query.filter(self.E.id.in_(filters.entity_ids))
        
        # Entity name filter (case-insensitive partial match)
        if filters.entity_name:
            pattern = f"%{filters.entity_name}%"
            query = query.filter(self.E.name.ilike(pattern))
        
        return query
    
    def _build_time_breakdown_query(self, workspace_id: str, start_date: date, end_date: date, filters: MetricFilters, breakdown_dimension: str):
        """Build query for time-based breakdown."""
        if breakdown_dimension == "day":
            group_expr = cast(self.MF.event_date, Date)
            label_expr = cast(self.MF.event_date, Date)
        elif breakdown_dimension == "week":
            group_expr = func.date_trunc('week', self.MF.event_date)
            label_expr = func.date_trunc('week', self.MF.event_date)
        elif breakdown_dimension == "month":
            group_expr = func.date_trunc('month', self.MF.event_date)
            label_expr = func.date_trunc('month', self.MF.event_date)
        else:
            raise ValueError(f"Unsupported time breakdown dimension: {breakdown_dimension}")
        
        query = (
            self.db.query(
                label_expr.label("group_name"),
                func.coalesce(func.sum(self.MF.spend), 0).label("spend"),
                func.coalesce(func.sum(self.MF.revenue), 0).label("revenue"),
                func.coalesce(func.sum(self.MF.clicks), 0).label("clicks"),
                func.coalesce(func.sum(self.MF.impressions), 0).label("impressions"),
                func.coalesce(func.sum(self.MF.conversions), 0).label("conversions"),
                func.coalesce(func.sum(self.MF.leads), 0).label("leads"),
                func.coalesce(func.sum(self.MF.installs), 0).label("installs"),
                func.coalesce(func.sum(self.MF.purchases), 0).label("purchases"),
                func.coalesce(func.sum(self.MF.visitors), 0).label("visitors"),
                func.coalesce(func.sum(self.MF.profit), 0).label("profit"),
            )
            .join(self.E, self.E.id == self.MF.entity_id)
            .filter(self.E.workspace_id == workspace_id)
            .filter(cast(self.MF.event_date, Date).between(start_date, end_date))
            .group_by(group_expr)
        )
        
        return self._apply_filters(query, filters)
    
    def _get_time_order_expression(self, metric: str, breakdown_dimension: str):
        """Get SQL expression for ordering by metric in time-based breakdowns."""
        # Use the same logic as _get_order_expression but for time-based queries
        if metric == "roas":
            return func.coalesce(func.sum(self.MF.revenue), 0) / func.nullif(func.coalesce(func.sum(self.MF.spend), 0), 0)
        elif metric == "cpc":
            return func.coalesce(func.sum(self.MF.spend), 0) / func.nullif(func.coalesce(func.sum(self.MF.clicks), 0), 0)
        elif metric == "cpa":
            return func.coalesce(func.sum(self.MF.spend), 0) / func.nullif(func.coalesce(func.sum(self.MF.conversions), 0), 0)
        elif metric == "ctr":
            return func.coalesce(func.sum(self.MF.clicks), 0) / func.nullif(func.coalesce(func.sum(self.MF.impressions), 0), 0)
        elif metric == "cpm":
            return (func.coalesce(func.sum(self.MF.spend), 0) / func.nullif(func.coalesce(func.sum(self.MF.impressions), 0), 0)) * 1000
        elif metric == "spend":
            return func.coalesce(func.sum(self.MF.spend), 0)
        elif metric == "revenue":
            return func.coalesce(func.sum(self.MF.revenue), 0)
        elif metric == "clicks":
            return func.coalesce(func.sum(self.MF.clicks), 0)
        elif metric == "conversions":
            return func.coalesce(func.sum(self.MF.conversions), 0)
        else:
            # Fallback to spend
            return func.coalesce(func.sum(self.MF.spend), 0)
