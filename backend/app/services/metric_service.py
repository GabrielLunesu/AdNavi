"""Metric service
------------------
Centralizes metrics math and data access for both routers and AI.

Design goals:
- Single source of truth for metrics calculations (sum, derived ROAS/CPA/CVR)
- Workspace scoping and safe filtering
- Extensible: future providers, breakdowns, and caching
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from typing import Any, Dict, List, Optional, Tuple

from sqlalchemy.orm import Session
from sqlalchemy import func

from app import models
from app.schemas import MetricQuery


def _resolve_date_range(time_range: dict) -> Tuple[date, date]:
    """Resolve DSL time_range into inclusive [start, end] dates.

    Supports either {"last_n_days": int} or {"start": YYYY-MM-DD, "end": YYYY-MM-DD}.
    """
    if not isinstance(time_range, dict):
        raise ValueError("time_range must be an object with last_n_days or start/end")

    if "last_n_days" in time_range and time_range["last_n_days"]:
        n = int(time_range["last_n_days"]) or 7
        end = date.today()
        start = end - timedelta(days=n - 1)
        return start, end

    start_str = time_range.get("start")
    end_str = time_range.get("end")
    if not (start_str and end_str):
        raise ValueError("time_range requires last_n_days or both start and end")

    start = date.fromisoformat(start_str)
    end = date.fromisoformat(end_str)
    if start > end:
        raise ValueError("time_range.start must be <= time_range.end")
    return start, end


def _derived_metric(metric: str, totals: Dict[str, Any]) -> Optional[float]:
    """Compute a single metric value (base or derived) from aggregate totals."""
    if totals is None:
        return None
    spend = float(totals.get("spend") or 0)
    revenue = float(totals.get("revenue") or 0)
    clicks = float(totals.get("clicks") or 0)
    impressions = float(totals.get("impressions") or 0)
    conversions = float(totals.get("conversions") or 0)

    if metric == "roas":
        return (revenue / spend) if spend > 0 else None
    if metric == "cpa":
        return (spend / conversions) if conversions > 0 else None
    if metric == "cvr":
        return (conversions / clicks) if clicks > 0 else None

    # base metrics
    base = totals.get(metric)
    return float(base) if base is not None else None


@dataclass
class MetricService:
    """Service providing metrics aggregation and breakdowns."""

    db: Session

    def _base_query(self, workspace_id: str):
        MF, E = models.MetricFact, models.Entity
        return self.db.query(MF).join(E, E.id == MF.entity_id).filter(E.workspace_id == workspace_id)

    def _apply_filters(self, query, filters: dict | None):
        MF = models.MetricFact
        if not filters:
            return query
        provider = filters.get("provider")
        if provider:
            query = query.filter(MF.provider == provider)
        entity_ids = filters.get("entity_ids")
        if entity_ids:
            query = query.filter(MF.entity_id.in_(entity_ids))
        level = filters.get("level")
        if level:
            query = query.filter(MF.level == level)
        return query

    def _aggregate_totals(self, workspace_id: str, start: date, end: date, filters: dict | None) -> Dict[str, Any]:
        MF = models.MetricFact
        query = self._base_query(workspace_id)
        query = query.filter(MF.event_date.between(start, end))
        query = self._apply_filters(query, filters)
        row = (
            query.with_entities(
                func.coalesce(func.sum(MF.spend), 0).label("spend"),
                func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
                func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
                func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
                func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
            )
            .one()
        )
        return {
            "spend": float(row.spend or 0),
            "revenue": float(row.revenue or 0),
            "clicks": float(row.clicks or 0),
            "impressions": float(row.impressions or 0),
            "conversions": float(row.conversions or 0),
        }

    def _group_level_for(self, group_by: str) -> Optional[str]:
        if group_by in (None, "none"):
            return None
        return group_by

    def _breakdown(self, workspace_id: str, metric: str, start: date, end: date, group_by: str, filters: dict | None) -> List[Dict[str, Any]]:
        MF, E = models.MetricFact, models.Entity
        query = self._base_query(workspace_id)
        query = query.filter(MF.event_date.between(start, end))
        query = self._apply_filters(query, filters)

        # Map group_by to entity level; only include matching level rows for clear semantics
        level = self._group_level_for(group_by)
        if level:
            query = query.filter(MF.level == level)

        agg = query.with_entities(
            E.id.label("entity_id"),
            E.name.label("entity_name"),
            func.coalesce(func.sum(MF.spend), 0).label("spend"),
            func.coalesce(func.sum(MF.revenue), 0).label("revenue"),
            func.coalesce(func.sum(MF.clicks), 0).label("clicks"),
            func.coalesce(func.sum(MF.impressions), 0).label("impressions"),
            func.coalesce(func.sum(MF.conversions), 0).label("conversions"),
        ).group_by(E.id, E.name).order_by(func.sum(MF.spend).desc()).all()

        out: List[Dict[str, Any]] = []
        for r in agg:
            totals = {
                "spend": float(r.spend or 0),
                "revenue": float(r.revenue or 0),
                "clicks": float(r.clicks or 0),
                "impressions": float(r.impressions or 0),
                "conversions": float(r.conversions or 0),
            }
            out.append({"id": str(r.entity_id), "name": r.entity_name, "value": _derived_metric(metric, totals)})
        return out

    def execute(self, query: MetricQuery, workspace_id: str) -> Dict[str, Any]:
        """
        Execute a MetricQuery against MetricFact in a workspace.

        Returns a structured payload with:
        - summary: aggregated metric value for the period
        - delta: optional percentage change vs previous period
        - breakdown: optional list of per-entity values when group_by != none
        """
        start, end = _resolve_date_range(query.time_range)

        totals_now = self._aggregate_totals(workspace_id, start, end, query.filters)
        summary_val = _derived_metric(query.metric, totals_now)

        result: Dict[str, Any] = {"summary": summary_val}

        if query.compare_to_previous:
            length_days = (end - start).days + 1
            prev_start = start - timedelta(days=length_days)
            prev_end = start - timedelta(days=1)
            totals_prev = self._aggregate_totals(workspace_id, prev_start, prev_end, query.filters)
            prev_val = _derived_metric(query.metric, totals_prev)
            if prev_val not in (None, 0) and summary_val is not None:
                result["delta"] = (summary_val - prev_val) / prev_val * 100.0

        if query.group_by and query.group_by != "none":
            result["breakdown"] = self._breakdown(workspace_id, query.metric, start, end, query.group_by, query.filters)

        return result


