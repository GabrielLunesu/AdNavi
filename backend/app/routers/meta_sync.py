"""Meta Ads synchronization endpoints.

WHAT:
    REST endpoints for syncing Meta entity hierarchy (campaigns/adsets/ads)
    and metrics (insights) from Meta Marketing API to AdNavi database.

WHY:
    - User-initiated sync via UI button (manual trigger)
    - Two-step process: entities first, then metrics
    - Clean separation enables independent retry and debugging

WHERE USED:
    - UI sync button calls these endpoints
    - Phase 3 automated scheduler will call these

DEPENDENCIES:
    - app/services/meta_ads_client.py (MetaAdsClient)
    - app/models.py (Entity, MetricFact, Connection)
    - app/schemas.py (sync request/response schemas)
    - app/routers/ingest.py (metric ingestion endpoint)

REFERENCES:
    - backend/docs/roadmap/meta-ads-roadmap.md (Phase 2.3, 2.4)
    - backend/test_meta_api.py (API patterns)
"""

import logging
import os
from datetime import datetime, timedelta, date
from typing import List, Tuple, Dict, Any, Optional
from uuid import UUID
import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import desc

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
from app.security import decrypt_secret
from app.services.meta_ads_client import (
    MetaAdsClient,
    MetaAdsClientError,
    MetaAdsAuthenticationError,
    MetaAdsPermissionError,
)

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/workspaces/{workspace_id}/connections/{connection_id}",
    tags=["Meta Sync"],
)


# Objective to Goal Mapping
# Maps Meta campaign objectives to AdNavi goal enums
OBJECTIVE_TO_GOAL = {
    "OUTCOME_AWARENESS": GoalEnum.awareness,
    "OUTCOME_TRAFFIC": GoalEnum.traffic,
    "OUTCOME_ENGAGEMENT": GoalEnum.traffic,
    "OUTCOME_LEADS": GoalEnum.leads,
    "OUTCOME_APP_PROMOTION": GoalEnum.app_installs,
    "OUTCOME_SALES": GoalEnum.purchases,
    "CONVERSIONS": GoalEnum.conversions,
    # Add more mappings as Meta adds objectives
}


def _get_access_token(connection: Connection) -> str:
    """Retrieve decrypted Meta access token for a connection.

    WHAT:
        Uses encrypted tokens from DB when available, otherwise falls back to
        the Phase 2 system token in `.env`.
    WHY:
        Supports the Phase 2.1 rollout (encrypted storage) while preserving
        backward compatibility for manual tokens.
    REFERENCES:
        - app/security.py::decrypt_secret
        - docs/living-docs/META_INTEGRATION_STATUS.md (Phase 2.1)
    """
    # Phase 7 (OAuth): Use connection.token
    if connection.token and connection.token.access_token_enc:
        try:
            access_token = decrypt_secret(
                connection.token.access_token_enc,
                context=f"meta-connection:{connection.id}",
            )
            logger.info("[META_SYNC] Using decrypted token for connection %s", connection.id)
            return access_token
        except ValueError:
            logger.exception("[META_SYNC] Stored token for connection %s could not be decrypted", connection.id)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Stored Meta token is invalid or corrupted."
            )
    
    # Phase 2: Use system user token from .env
    token = os.getenv("META_ACCESS_TOKEN")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="META_ACCESS_TOKEN not configured in environment"
        )
    
    logger.info("[META_SYNC] Using system user token from .env")
    return token


def _upsert_entity(
    db: Session,
    connection: Connection,
    external_id: str,
    level: LevelEnum,
    name: str,
    status: str,
    parent_id: Optional[UUID] = None,
    goal: Optional[GoalEnum] = None
) -> Tuple[Entity, bool]:
    """UPSERT entity by external_id + connection_id.
    
    WHAT:
        Creates new Entity or updates existing one.
        Uses external_id + connection_id as unique key.
    
    WHY:
        Makes sync idempotent - safe to re-run without duplicates.
        Re-sync updates status/name changes from Meta.
    
    Args:
        db: Database session
        connection: Connection record
        external_id: Meta entity ID
        level: Entity level (campaign/adset/ad)
        name: Entity name
        status: Entity status (ACTIVE/PAUSED/etc.)
        parent_id: Parent entity UUID (None for campaigns)
        goal: Campaign goal/objective (None for adsets/ads)
        
    Returns:
        Tuple of (entity, was_created)
        
    Raises:
        None - always succeeds
    """
    # Check if entity already exists
    entity = db.query(Entity).filter(
        Entity.connection_id == connection.id,
        Entity.external_id == external_id
    ).first()
    
    was_created = False
    
    if entity:
        # Update existing entity
        entity.name = name
        entity.status = status
        entity.parent_id = parent_id
        entity.goal = goal
        entity.updated_at = datetime.utcnow()
        logger.debug(f"[META_SYNC] Updated entity: {external_id} ({level.value})")
    else:
        # Create new entity
        entity = Entity(
            id=uuid.uuid4(),
            workspace_id=connection.workspace_id,
            connection_id=connection.id,
            level=level,
            external_id=external_id,
            name=name,
            status=status,
            parent_id=parent_id,
            goal=goal,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.add(entity)
        was_created = True
        logger.debug(f"[META_SYNC] Created entity: {external_id} ({level.value})")
    
    db.flush()  # Get entity.id without committing
    return entity, was_created


@router.post("/sync-entities", response_model=EntitySyncResponse)
async def sync_entities(
    workspace_id: UUID,
    connection_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Sync entity hierarchy from Meta to AdNavi.
    
    WHAT:
        Fetches campaigns, adsets, and ads from Meta Marketing API.
        Creates/updates Entity records in database with hierarchy preserved.
    
    WHY:
        Establishes entity structure before fetching metrics.
        UPSERT pattern makes re-sync safe (no duplicates).
        Maps Meta IDs to AdNavi Entity UUIDs.
    
    ALGORITHM:
        1. Validate connection belongs to workspace
        2. Get Meta access token
        3. Initialize MetaAdsClient
        4. Fetch campaigns from account
        5. For each campaign:
            a. UPSERT campaign entity
            b. Fetch adsets for campaign
            c. For each adset:
                i. UPSERT adset entity (parent=campaign)
                ii. Fetch ads for adset
                iii. For each ad:
                    - UPSERT ad entity (parent=adset)
        6. Commit transaction
        7. Return stats
    
    Args:
        workspace_id: Workspace UUID
        connection_id: Connection UUID
        db: Database session
        current_user: Authenticated user
        
    Returns:
        EntitySyncResponse with stats and errors
        
    Raises:
        HTTPException: 404 if connection not found, 403 if unauthorized
    """
    start_time = datetime.utcnow()
    stats = EntitySyncStats(
        campaigns_created=0,
        campaigns_updated=0,
        adsets_created=0,
        adsets_updated=0,
        ads_created=0,
        ads_updated=0,
        duration_seconds=0.0
    )
    errors = []
    
    logger.info(
        f"[META_SYNC] Starting entity sync: "
        f"workspace={workspace_id}, connection={connection_id}"
    )
    
    try:
        # 1. Validate connection belongs to workspace
        connection = db.query(Connection).filter(
            Connection.id == connection_id,
            Connection.workspace_id == workspace_id
        ).first()
        
        if not connection:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Connection not found or does not belong to workspace"
            )
        
        if connection.provider != ProviderEnum.meta:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Connection is not a Meta connection (provider={connection.provider})"
            )
        
        # 2. Get access token
        access_token = _get_access_token(connection)
        
        # 3. Initialize Meta client
        client = MetaAdsClient(access_token=access_token)
        
        # 4. Fetch campaigns
        account_id = connection.external_account_id
        if not account_id.startswith("act_"):
            account_id = f"act_{account_id}"
        
        logger.info(f"[META_SYNC] Fetching campaigns for account: {account_id}")
        campaigns = client.get_campaigns(account_id)
        logger.info(f"[META_SYNC] Found {len(campaigns)} campaigns")
        
        # 5. Process each campaign
        for campaign_data in campaigns:
            try:
                # Extract campaign fields
                campaign_id = campaign_data['id']
                campaign_name = campaign_data.get('name', f"Campaign {campaign_id}")
                campaign_status = campaign_data.get('status', 'UNKNOWN')
                campaign_objective = campaign_data.get('objective')
                
                # Map objective to goal
                campaign_goal = OBJECTIVE_TO_GOAL.get(campaign_objective, GoalEnum.other)
                
                # a. UPSERT campaign entity
                campaign_entity, created = _upsert_entity(
                    db=db,
                    connection=connection,
                    external_id=campaign_id,
                    level=LevelEnum.campaign,
                    name=campaign_name,
                    status=campaign_status.lower(),
                    parent_id=None,
                    goal=campaign_goal
                )
                
                if created:
                    stats.campaigns_created += 1
                else:
                    stats.campaigns_updated += 1
                
                # b. Fetch adsets for this campaign
                logger.info(f"[META_SYNC] Fetching adsets for campaign: {campaign_id}")
                adsets = client.get_adsets(campaign_id)
                logger.info(f"[META_SYNC] Found {len(adsets)} adsets")
                
                # c. Process each adset
                for adset_data in adsets:
                    try:
                        adset_id = adset_data['id']
                        adset_name = adset_data.get('name', f"AdSet {adset_id}")
                        adset_status = adset_data.get('status', 'UNKNOWN')
                        
                        # i. UPSERT adset entity
                        adset_entity, created = _upsert_entity(
                            db=db,
                            connection=connection,
                            external_id=adset_id,
                            level=LevelEnum.adset,
                            name=adset_name,
                            status=adset_status.lower(),
                            parent_id=campaign_entity.id
                        )
                        
                        if created:
                            stats.adsets_created += 1
                        else:
                            stats.adsets_updated += 1
                        
                        # ii. Fetch ads for this adset
                        logger.info(f"[META_SYNC] Fetching ads for adset: {adset_id}")
                        ads = client.get_ads(adset_id)
                        logger.info(f"[META_SYNC] Found {len(ads)} ads")
                        
                        # iii. Process each ad
                        for ad_data in ads:
                            try:
                                ad_id = ad_data['id']
                                ad_name = ad_data.get('name', f"Ad {ad_id}")
                                ad_status = ad_data.get('status', 'UNKNOWN')
                                
                                # UPSERT ad entity
                                ad_entity, created = _upsert_entity(
                                    db=db,
                                    connection=connection,
                                    external_id=ad_id,
                                    level=LevelEnum.ad,
                                    name=ad_name,
                                    status=ad_status.lower(),
                                    parent_id=adset_entity.id
                                )
                                
                                if created:
                                    stats.ads_created += 1
                                else:
                                    stats.ads_updated += 1
                                    
                            except Exception as e:
                                error_msg = f"Error syncing ad {ad_data.get('id', 'unknown')}: {str(e)}"
                                logger.error(f"[META_SYNC] {error_msg}")
                                errors.append(error_msg)
                                
                    except Exception as e:
                        error_msg = f"Error syncing adset {adset_data.get('id', 'unknown')}: {str(e)}"
                        logger.error(f"[META_SYNC] {error_msg}")
                        errors.append(error_msg)
                        
            except Exception as e:
                error_msg = f"Error syncing campaign {campaign_data.get('id', 'unknown')}: {str(e)}"
                logger.error(f"[META_SYNC] {error_msg}")
                errors.append(error_msg)
        
        # 6. Commit transaction
        db.commit()
        
        # 7. Calculate duration and return
        duration = (datetime.utcnow() - start_time).total_seconds()
        stats.duration_seconds = duration
        
        logger.info(
            f"[META_SYNC] Entity sync complete: "
            f"{stats.campaigns_created + stats.campaigns_updated} campaigns, "
            f"{stats.adsets_created + stats.adsets_updated} adsets, "
            f"{stats.ads_created + stats.ads_updated} ads "
            f"({duration:.1f}s)"
        )
        
        return EntitySyncResponse(
            success=len(errors) == 0 or (stats.campaigns_created + stats.campaigns_updated) > 0,
            synced=stats,
            errors=errors
        )
        
    except MetaAdsAuthenticationError as e:
        logger.error(f"[META_SYNC] Authentication error: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
    except MetaAdsPermissionError as e:
        logger.error(f"[META_SYNC] Permission error: {e}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"[META_SYNC] Unexpected error: {e}", exc_info=True)
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Entity sync failed: {str(e)}"
        )


def _determine_date_range(
    connection: Connection,
    db: Session,
    request: MetricsSyncRequest
) -> Tuple[date, date]:
    """Determine date range for metrics sync.
    
    WHAT:
        Calculates start/end dates based on request and sync history.
        Implements 90-day policy and incremental sync logic.
    
    WHY:
        - 90-day historical backfill on first sync
        - Incremental sync on subsequent runs (only new dates)
        - Force refresh allows manual override
    
    Args:
        connection: Connection record
        db: Database session
        request: Metrics sync request with optional dates
        
    Returns:
        Tuple of (start_date, end_date)
    """
    # If explicit dates provided, use them
    if request.start_date and request.end_date:
        logger.info(
            f"[META_SYNC] Using explicit date range: "
            f"{request.start_date} to {request.end_date}"
        )
        return request.start_date, request.end_date
    
    # Default end: yesterday (today's data incomplete in Meta)
    end_date = request.end_date or (datetime.utcnow().date() - timedelta(days=1))
    
    if request.force_refresh:
        # Full 90-day refresh
        start_date = end_date - timedelta(days=90)
        logger.info(
            f"[META_SYNC] Force refresh: "
            f"90-day range {start_date} to {end_date}"
        )
    else:
        # Check last ingested date for this connection
        last_fact = db.query(MetricFact).join(Entity).filter(
            Entity.connection_id == connection.id,
            MetricFact.provider == ProviderEnum.meta
        ).order_by(desc(MetricFact.event_date)).first()
        
        if last_fact:
            # Incremental: last date + 1 day
            last_date = last_fact.event_date.date()
            start_date = last_date + timedelta(days=1)
            logger.info(
                f"[META_SYNC] Incremental sync: "
                f"last date was {last_date}, starting from {start_date}"
            )
        else:
            # First sync: 90 days from connection date
            start_date = connection.connected_at.date()
            # But cap at 90 days ago
            min_start = end_date - timedelta(days=90)
            start_date = max(start_date, min_start)
            logger.info(
                f"[META_SYNC] First sync: "
                f"90-day historical backfill {start_date} to {end_date}"
            )
    
    # Ensure start <= end
    if start_date > end_date:
        logger.warning(
            f"[META_SYNC] No new data to sync: "
            f"start {start_date} > end {end_date}"
        )
        start_date = end_date
    
    return start_date, end_date


def _chunk_date_range(start: date, end: date, chunk_days: int = 7) -> List[Tuple[date, date]]:
    """Split date range into chunks.
    
    WHAT:
        Breaks large date range into smaller windows.
        Each chunk is at most chunk_days days.
    
    WHY:
        - Prevents API timeout on large requests
        - Respects rate limits (fewer concurrent large requests)
        - Enables progress tracking per chunk
    
    Args:
        start: Start date
        end: End date
        chunk_days: Maximum days per chunk (default 7)
        
    Returns:
        List of (chunk_start, chunk_end) tuples
    """
    chunks = []
    current = start
    
    while current <= end:
        chunk_end = min(current + timedelta(days=chunk_days - 1), end)
        chunks.append((current, chunk_end))
        current = chunk_end + timedelta(days=1)
    
    logger.info(
        f"[META_SYNC] Date range chunked: "
        f"{len(chunks)} chunks of ~{chunk_days} days"
    )
    
    return chunks


def _parse_actions(insight: Dict[str, Any]) -> Dict[str, Any]:
    """Parse Meta actions array into AdNavi metrics.
    
    WHAT:
        Extracts conversions, leads, purchases, installs from Meta's nested actions structure.
        Parses action_values for revenue.
    
    WHY:
        Meta returns complex nested arrays for conversion data.
        AdNavi uses flat fields for simplicity.
    
    Meta Format:
        "actions": [
            {"action_type": "omni_purchase", "value": "12"},
            {"action_type": "lead", "value": "45"}
        ],
        "action_values": [
            {"action_type": "omni_purchase", "value": "523.50"}
        ]
    
    AdNavi Format:
        {"purchases": 12, "leads": 45, "revenue": 523.50}
    
    Args:
        insight: Insight dictionary from Meta API
        
    Returns:
        Dictionary with parsed metrics
    """
    actions = insight.get("actions", [])
    action_values = insight.get("action_values", [])
    
    result = {
        "purchases": 0,
        "leads": 0,
        "installs": 0,
        "conversions": 0,
        "revenue": 0.0
    }
    
    # Parse actions (counts)
    for action in actions:
        action_type = action.get("action_type", "")
        value = int(float(action.get("value", 0)))
        
        if action_type == "omni_purchase":
            result["purchases"] = value
        elif action_type == "lead":
            result["leads"] = value
        elif action_type == "app_install":
            result["installs"] = value
        elif action_type in ["offsite_conversion", "onsite_conversion"]:
            result["conversions"] += value
    
    # Parse action_values (revenue)
    for action_value in action_values:
        action_type = action_value.get("action_type", "")
        if action_type == "omni_purchase":
            result["revenue"] = float(action_value.get("value", 0))
    
    return result


@router.post("/sync-metrics", response_model=MetricsSyncResponse)
async def sync_metrics(
    workspace_id: UUID,
    connection_id: UUID,
    request: MetricsSyncRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Sync metrics from Meta to AdNavi.
    
    WHAT:
        Fetches insights (metrics) from Meta Marketing API for all ads.
        Ingests data into MetricFact table via ingestion API.
    
    WHY:
        - 90-day historical backfill on first sync
        - Incremental sync on subsequent runs (only new dates)
        - Ad-level metrics (database rolls up to adset/campaign)
    
    ALGORITHM:
        1. Validate connection belongs to workspace
        2. Determine date range (90-day backfill or incremental)
        3. Get all ad-level entities for this connection
        4. Chunk date range into 7-day windows
        5. For each ad entity:
            a. For each 7-day chunk:
                i. Fetch insights from Meta
                ii. Parse actions into metrics
                iii. Create MetricFactCreate objects
                iv. Ingest via Phase 1.2 endpoint
        6. Return stats
    
    Args:
        workspace_id: Workspace UUID
        connection_id: Connection UUID
        request: Metrics sync request with optional dates
        db: Database session
        current_user: Authenticated user
        
    Returns:
        MetricsSyncResponse with stats and errors
        
    Raises:
        HTTPException: 404 if connection not found, 403 if unauthorized
    """
    start_time = datetime.utcnow()
    total_ingested = 0
    total_skipped = 0
    errors = []
    
    logger.info(
        f"[META_SYNC] Starting metrics sync: "
        f"workspace={workspace_id}, connection={connection_id}"
    )
    
    try:
        # 1. Validate connection
        connection = db.query(Connection).filter(
            Connection.id == connection_id,
            Connection.workspace_id == workspace_id
        ).first()
        
        if not connection:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Connection not found or does not belong to workspace"
            )
        
        if connection.provider != ProviderEnum.meta:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Connection is not a Meta connection (provider={connection.provider})"
            )
        
        # 2. Determine date range
        start_date, end_date = _determine_date_range(connection, db, request)
        
        if start_date > end_date:
            logger.info("[META_SYNC] No new data to sync")
            return MetricsSyncResponse(
                success=True,
                synced=MetricsSyncStats(
                    facts_ingested=0,
                    facts_skipped=0,
                    date_range=DateRange(start=start_date, end=end_date),
                    ads_processed=0,
                    duration_seconds=0.0
                ),
                errors=["No new data to sync (start date > end date)"]
            )
        
        # 3. Get all ad-level entities
        ad_entities = db.query(Entity).filter(
            Entity.connection_id == connection.id,
            Entity.level == LevelEnum.ad
        ).all()
        
        if not ad_entities:
            logger.warning("[META_SYNC] No ad entities found. Run sync-entities first.")
            return MetricsSyncResponse(
                success=False,
                synced=MetricsSyncStats(
                    facts_ingested=0,
                    facts_skipped=0,
                    date_range=DateRange(start=start_date, end=end_date),
                    ads_processed=0,
                    duration_seconds=0.0
                ),
                errors=["No ad entities found. Please run entity sync first."]
            )
        
        logger.info(f"[META_SYNC] Found {len(ad_entities)} ad entities to process")
        
        # 4. Chunk date range
        chunks = _chunk_date_range(start_date, end_date, chunk_days=7)
        
        # Get access token and initialize client
        access_token = _get_access_token(connection)
        client = MetaAdsClient(access_token=access_token)
        
        # 5. Process each ad entity
        ads_processed = 0
        
        for ad_entity in ad_entities:
            try:
                logger.info(
                    f"[META_SYNC] Processing ad {ad_entity.external_id} "
                    f"({ads_processed + 1}/{len(ad_entities)})"
                )
                
                # a. Process each chunk
                for chunk_start, chunk_end in chunks:
                    try:
                        # i. Fetch insights
                        insights = client.get_insights(
                            entity_id=ad_entity.external_id,
                            start_date=chunk_start.isoformat(),
                            end_date=chunk_end.isoformat(),
                            level="ad",
                            time_increment=1  # Daily
                        )
                        
                        if not insights:
                            logger.debug(
                                f"[META_SYNC] No insights for ad {ad_entity.external_id} "
                                f"({chunk_start} to {chunk_end})"
                            )
                            continue
                        
                        # ii. Parse insights into MetricFactCreate objects
                        facts_to_ingest = []
                        
                        for insight in insights:
                            # Parse basic metrics
                            spend = float(insight.get("spend", 0))
                            impressions = int(insight.get("impressions", 0))
                            clicks = int(insight.get("clicks", 0))
                            
                            # Parse actions (conversions/leads/purchases/revenue)
                            parsed_actions = _parse_actions(insight)
                            
                            # Get date from insight
                            date_start = insight.get("date_start")
                            if not date_start:
                                logger.warning("[META_SYNC] Insight missing date_start, skipping")
                                continue
                            
                            # Create MetricFactCreate
                            fact = MetricFactCreate(
                                entity_id=ad_entity.id,
                                external_entity_id=ad_entity.external_id,
                                provider=ProviderEnum.meta,
                                level=LevelEnum.ad,
                                event_at=datetime.fromisoformat(date_start + "T12:00:00+00:00"),
                                spend=spend,
                                impressions=impressions,
                                clicks=clicks,
                                conversions=parsed_actions["conversions"],
                                revenue=parsed_actions["revenue"],
                                leads=parsed_actions["leads"],
                                installs=parsed_actions["installs"],
                                purchases=parsed_actions["purchases"],
                                currency="USD"  # Meta reports in account currency
                            )
                            
                            facts_to_ingest.append(fact)
                        
                        # iii. Ingest facts via Phase 1.2 endpoint
                        if facts_to_ingest:
                            from app.routers.ingest import ingest_metrics_internal
                            
                            result = await ingest_metrics_internal(
                                workspace_id=workspace_id,
                                facts=facts_to_ingest,
                                db=db
                            )
                            
                            total_ingested += result["ingested"]
                            total_skipped += result["skipped"]
                            
                            logger.info(
                                f"[META_SYNC] Ingested {result['ingested']} facts, "
                                f"skipped {result['skipped']} for chunk "
                                f"{chunk_start} to {chunk_end}"
                            )
                            
                    except Exception as e:
                        error_msg = (
                            f"Error fetching insights for ad {ad_entity.external_id} "
                            f"({chunk_start} to {chunk_end}): {str(e)}"
                        )
                        logger.error(f"[META_SYNC] {error_msg}")
                        errors.append(error_msg)
                
                ads_processed += 1
                
            except Exception as e:
                error_msg = f"Error processing ad {ad_entity.external_id}: {str(e)}"
                logger.error(f"[META_SYNC] {error_msg}")
                errors.append(error_msg)
        
        # 6. Calculate duration and return
        duration = (datetime.utcnow() - start_time).total_seconds()
        
        logger.info(
            f"[META_SYNC] Metrics sync complete: "
            f"{total_ingested} facts ingested, {total_skipped} skipped, "
            f"{ads_processed} ads processed ({duration:.1f}s)"
        )
        
        return MetricsSyncResponse(
            success=len(errors) == 0 or total_ingested > 0,
            synced=MetricsSyncStats(
                facts_ingested=total_ingested,
                facts_skipped=total_skipped,
                date_range=DateRange(start=start_date, end=end_date),
                ads_processed=ads_processed,
                duration_seconds=duration
            ),
            errors=errors
        )
        
    except MetaAdsAuthenticationError as e:
        logger.error(f"[META_SYNC] Authentication error: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
    except MetaAdsPermissionError as e:
        logger.error(f"[META_SYNC] Permission error: {e}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"[META_SYNC] Unexpected error: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Metrics sync failed: {str(e)}"
        )
