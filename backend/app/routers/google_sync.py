"""Google Ads synchronization endpoints.

WHAT:
    REST endpoints for syncing Google entity hierarchy (campaigns/ad groups/ads)
    and daily metrics (GAQL) from Google Ads API into AdNavi DB.

WHY:
    - User-initiated sync via UI button (manual trigger)
    - Two-step process: entities first, then metrics (idempotent)
    - Mirrors Meta sync architecture for consistency

REFERENCES:
    - app/services/google_ads_client.py (GAdsClient, map_channel_to_goal)
    - app/routers/ingest.py (ingest_metrics_internal)
    - docs/living-docs/GOOGLE_INTEGRATION_STATUS.MD
"""

from __future__ import annotations

import logging
from datetime import datetime, timedelta, date
from typing import List, Tuple, Optional, Dict
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.deps import get_current_user
from app.models import User, Connection, Entity, MetricFact, LevelEnum, GoalEnum, ProviderEnum
from app.schemas import (
    EntitySyncResponse,
    EntitySyncStats,
    MetricsSyncRequest,
    MetricsSyncResponse,
    MetricsSyncStats,
    DateRange,
    MetricFactCreate,
)
from app.routers.ingest import ingest_metrics_internal
from app.services.google_ads_client import GAdsClient, map_channel_to_goal


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/workspaces/{workspace_id}/connections/{connection_id}",
    tags=["Google Sync"],
)


# --- Helpers -------------------------------------------------------------

def _normalize_customer_id(customer_id: str) -> str:
    """Normalize Google customer ID (strip hyphens)."""
    return "".join(ch for ch in str(customer_id) if ch.isdigit())


def _compute_date_chunks(start: date, end: date, chunk_days: int = 7) -> List[Tuple[date, date]]:
    """Split date range into inclusive chunks of size chunk_days."""
    chunks: List[Tuple[date, date]] = []
    cursor = start
    while cursor <= end:
        chunk_end = min(end, cursor + timedelta(days=chunk_days - 1))
        chunks.append((cursor, chunk_end))
        cursor = chunk_end + timedelta(days=1)
    return chunks


def _normalize_status(status_val: Optional[object]) -> str:
    """Map Google enum/string statuses into unified app statuses.

    Google: ENABLED/PAUSED/REMOVED → active/paused/inactive
    """
    if status_val is None:
        return "unknown"
    # Extract enum name if present
    if hasattr(status_val, "name"):
        s = str(status_val.name).upper()
    else:
        s = str(status_val).upper()
    if s == "ENABLED":
        return "active"
    if s == "PAUSED":
        return "paused"
    if s == "REMOVED":
        return "inactive"
    return s.lower()


def _upsert_entity(
    db: Session,
    connection: Connection,
    external_id: str,
    level: LevelEnum,
    name: str,
    status: str,
    parent_id: Optional[UUID] = None,
    goal: Optional[GoalEnum] = None,
) -> Tuple[Entity, bool]:
    """UPSERT entity by external_id + connection_id.

    WHAT: Creates new Entity or updates existing one.
    WHY: Idempotent synchronization across re-runs.
    """
    entity = db.query(Entity).filter(
        Entity.connection_id == connection.id,
        Entity.external_id == external_id,
    ).first()

    created = False
    if entity:
        entity.name = name
        entity.status = status
        entity.parent_id = parent_id
        entity.goal = goal
        entity.updated_at = datetime.utcnow()
    else:
        entity = Entity(
            level=level,
            external_id=external_id,
            name=name,
            status=status,
            parent_id=parent_id,
            goal=goal,
            workspace_id=connection.workspace_id,
            connection_id=connection.id,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        db.add(entity)
        created = True
    db.flush()
    return entity, created


def _update_connection_metadata(db: Session, connection: Connection, meta: Dict[str, Optional[str]]) -> None:
    """Persist timezone/currency on Connection if available."""
    tz = meta.get("time_zone")
    cur = meta.get("currency_code")
    changed = False
    if tz and tz != connection.timezone:
        connection.timezone = tz
        changed = True
    if cur and cur != connection.currency_code:
        connection.currency_code = cur
        changed = True
    if changed:
        db.flush()


# --- Endpoints -----------------------------------------------------------

@router.post("/sync-google-entities", response_model=EntitySyncResponse)
async def sync_entities(
    workspace_id: UUID,
    connection_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Sync Google Ads entity hierarchy (campaigns → ad groups → ads).

    Mirrors Meta sync endpoint; safe to re-run (UPSERT).
    """
    start_time = datetime.utcnow()
    stats = EntitySyncStats(
        campaigns_created=0,
        campaigns_updated=0,
        adsets_created=0,
        adsets_updated=0,
        ads_created=0,
        ads_updated=0,
        duration_seconds=0.0,
    )
    errors: List[str] = []

    # Validate connection
    connection = db.query(Connection).filter(
        Connection.id == connection_id,
        Connection.workspace_id == workspace_id,
    ).first()
    if not connection:
        raise HTTPException(status_code=404, detail="Connection not found or not in workspace")
    if connection.provider != ProviderEnum.google:
        raise HTTPException(status_code=400, detail=f"Connection is not a Google connection (provider={connection.provider})")

    customer_id = _normalize_customer_id(connection.external_account_id)
    client = GAdsClient()

    # Update connection metadata (timezone/currency)
    try:
        meta = client.get_customer_metadata(customer_id)
        _update_connection_metadata(db, connection, meta)
    except Exception as e:
        logger.warning("[GOOGLE_SYNC] Failed to fetch customer metadata: %s", e)

    # Campaigns
    try:
        logger.info("[GOOGLE_SYNC] Fetching campaigns for customer %s", customer_id)
        campaigns = client.list_campaigns(customer_id)
        for c in campaigns:
            goal = map_channel_to_goal(c.get("advertising_channel_type"))
            camp, created = _upsert_entity(
                db=db,
                connection=connection,
                external_id=str(c["id"]),
                level=LevelEnum.campaign,
                name=c.get("name") or f"Campaign {c['id']}",
                status=_normalize_status(c.get("status")),
                parent_id=None,
                goal=goal,
            )
            if created:
                stats.campaigns_created += 1
            else:
                stats.campaigns_updated += 1

            # Ad groups (mapped to adsets)
            try:
                ad_groups = client.list_ad_groups(customer_id, str(c["id"]))
                for ag in ad_groups:
                    adset, ag_created = _upsert_entity(
                        db=db,
                        connection=connection,
                        external_id=str(ag["id"]),
                        level=LevelEnum.adset,
                        name=ag.get("name") or f"Ad group {ag['id']}",
                        status=_normalize_status(ag.get("status")),
                        parent_id=camp.id,
                    )
                    if ag_created:
                        stats.adsets_created += 1
                    else:
                        stats.adsets_updated += 1

                    # Ads
                    try:
                        ads = client.list_ads(customer_id, str(ag["id"]))
                        for ad in ads:
                            _, ad_created = _upsert_entity(
                                db=db,
                                connection=connection,
                                external_id=str(ad["id"]),
                                level=LevelEnum.ad,
                                name=ad.get("name") or f"Ad {ad['id']}",
                                status=_normalize_status(ad.get("status")),
                                parent_id=adset.id,
                            )
                            if ad_created:
                                stats.ads_created += 1
                            else:
                                stats.ads_updated += 1
                    except Exception as e:
                        logger.exception("[GOOGLE_SYNC] Ads fetch failed for ad group %s: %s", ag.get("id"), e)
                        errors.append(f"ad_group {ag.get('id')}: {e}")
            except Exception as e:
                logger.exception("[GOOGLE_SYNC] Ad groups fetch failed for campaign %s: %s", c.get("id"), e)
                errors.append(f"campaign {c.get('id')}: {e}")
    except Exception as e:
        logger.exception("[GOOGLE_SYNC] Campaigns fetch failed: %s", e)
        errors.append(str(e))

    stats.duration_seconds = (datetime.utcnow() - start_time).total_seconds()
    db.commit()
    return EntitySyncResponse(success=len(errors) == 0, synced=stats, errors=errors)


@router.post("/sync-google-metrics", response_model=MetricsSyncResponse)
async def sync_metrics(
    workspace_id: UUID,
    connection_id: UUID,
    body: MetricsSyncRequest = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Sync Google Ads daily metrics (ad-level) into MetricFact.

    Default: 90-day backfill, 7-day chunks, incremental by last ingested date.
    """
    started = datetime.utcnow()
    errors: List[str] = []

    # Validate connection/provider
    connection = db.query(Connection).filter(
        Connection.id == connection_id,
        Connection.workspace_id == workspace_id,
    ).first()
    if not connection:
        raise HTTPException(status_code=404, detail="Connection not found or not in workspace")
    if connection.provider != ProviderEnum.google:
        raise HTTPException(status_code=400, detail=f"Connection is not a Google connection (provider={connection.provider})")

    # Determine date range
    today = date.today()
    default_end = today - timedelta(days=1)
    # Last ingested date for this connection/provider
    last_date = db.query(func.max(MetricFact.event_date)).join(Entity, Entity.id == MetricFact.entity_id).filter(
        Entity.connection_id == connection.id,
        MetricFact.provider == ProviderEnum.google,
    ).scalar()

    if body and body.start_date and body.end_date:
        start_d, end_d = body.start_date, body.end_date
    else:
        if last_date and not (body and body.force_refresh):
            start_d = (last_date.date() if isinstance(last_date, datetime) else last_date) + timedelta(days=1)
        else:
            start_d = default_end - timedelta(days=89)
        end_d = default_end

    if start_d > end_d:
        # Nothing to sync
        stats = MetricsSyncStats(
            facts_ingested=0,
            facts_skipped=0,
            date_range=DateRange(start=start_d, end=end_d),
            ads_processed=0,
            duration_seconds=(datetime.utcnow() - started).total_seconds(),
        )
        return MetricsSyncResponse(success=True, synced=stats, errors=[])

    chunks = _compute_date_chunks(start_d, end_d, 7)
    customer_id = _normalize_customer_id(connection.external_account_id)
    client = GAdsClient()

    total_ingested = 0
    total_skipped = 0
    ads_seen: set[str] = set()

    for s, e in chunks:
        try:
            rows = client.fetch_daily_metrics(customer_id, s, e, level="ad")
            facts: List[MetricFactCreate] = []
            for row in rows:
                # Identify external entity id depending on level
                raw = row.get("_raw")
                try:
                    ext_id = str(raw.ad_group_ad.ad.id)
                except Exception:
                    # Fallback: cannot parse id → skip
                    continue
                ads_seen.add(ext_id)
                ev_date = datetime.combine(date.fromisoformat(row["date"]), datetime.min.time())
                facts.append(MetricFactCreate(
                    external_entity_id=ext_id,
                    provider=ProviderEnum.google,
                    level=LevelEnum.ad,
                    event_at=ev_date,
                    spend=row.get("spend", 0.0),
                    impressions=row.get("impressions", 0),
                    clicks=row.get("clicks", 0),
                    conversions=row.get("conversions", 0.0),
                    revenue=row.get("revenue", 0.0),
                    currency=connection.currency_code or "USD",
                ))
            if facts:
                res = await ingest_metrics_internal(workspace_id=workspace_id, facts=facts, db=db)
                total_ingested += res.get("ingested", 0)
                total_skipped += res.get("skipped", 0)
        except Exception as ex:
            logger.exception("[GOOGLE_SYNC] Metrics fetch failed for %s to %s: %s", s, e, ex)
            errors.append(f"{s}..{e}: {ex}")

    stats = MetricsSyncStats(
        facts_ingested=total_ingested,
        facts_skipped=total_skipped,
        date_range=DateRange(start=start_d, end=end_d),
        ads_processed=len(ads_seen),
        duration_seconds=(datetime.utcnow() - started).total_seconds(),
    )
    return MetricsSyncResponse(success=len(errors) == 0, synced=stats, errors=errors)
