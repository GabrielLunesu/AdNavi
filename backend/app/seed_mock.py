"""Seed script to populate the database with realistic mock data for testing.

Usage:
    cd backend
    python -m app.seed_mock

This script will:
1. Wipe existing data
2. Create "Defang Labs" workspace with 2 users
3. Create a mock connection with entity hierarchy (campaigns > adsets > ads)
4. Generate 30 days of MetricFact data for each ad
5. Create ComputeRun and P&L snapshots with calculated metrics
"""

from datetime import datetime, timedelta
import random
import uuid

from app.database import SessionLocal
from app import models
from app.security import get_password_hash


def generate_random_metrics():
    """Generate realistic ad metrics for a single day."""
    spend = random.uniform(50, 200)
    impressions = random.randint(1000, 10000)
    clicks = random.randint(50, 500)
    conversions = random.uniform(5, 50)
    revenue = conversions * random.uniform(20, 100)
    
    return {
        'spend': round(spend, 2),
        'impressions': impressions,
        'clicks': clicks,
        'conversions': round(conversions, 2),
        'revenue': round(revenue, 2)
    }


def safe_divide(numerator, denominator):
    """Safely divide two numbers, returning None if denominator is 0."""
    if denominator == 0:
        return None
    return round(numerator / denominator, 4)


def seed():
    """Main seeding function."""
    with SessionLocal() as db:
        print("🧹 Clearing existing data...")
        
        # Clear data in reverse dependency order
        db.query(models.Pnl).delete()
        db.query(models.ComputeRun).delete()
        db.query(models.MetricFact).delete()
        db.query(models.Entity).delete()
        db.query(models.Import).delete()
        db.query(models.Fetch).delete()
        db.query(models.Connection).delete()
        db.query(models.QaQueryLog).delete()
        db.query(models.AuthCredential).delete()
        db.query(models.User).delete()
        db.query(models.Token).delete()
        db.query(models.Workspace).delete()
        db.commit()
        
        print("✅ Old data cleared")
        
        # 1. Create workspace
        print("🏢 Creating workspace...")
        workspace = models.Workspace(
            id=uuid.uuid4(),
            name="Defang Labs",
            created_at=datetime.utcnow()
        )
        db.add(workspace)
        db.flush()  # Get the ID for foreign key references
        
        # 2. Create users
        print("👥 Creating users...")
        owner_id = uuid.uuid4()
        viewer_id = uuid.uuid4()
        
        owner = models.User(
            id=owner_id,
            email="owner@defanglabs.com",
            name="Owner User",
            role=models.RoleEnum.owner,
            workspace_id=workspace.id
        )
        
        viewer = models.User(
            id=viewer_id,
            email="viewer@defanglabs.com",
            name="Viewer User", 
            role=models.RoleEnum.viewer,
            workspace_id=workspace.id
        )
        
        db.add_all([owner, viewer])
        db.flush()
        
        # Create auth credentials for both users
        owner_credential = models.AuthCredential(
            user_id=owner_id,
            password_hash=get_password_hash("password123"),
            created_at=datetime.utcnow()
        )
        
        viewer_credential = models.AuthCredential(
            user_id=viewer_id,
            password_hash=get_password_hash("password123"),
            created_at=datetime.utcnow()
        )
        
        db.add_all([owner_credential, viewer_credential])
        
        # 3. Create connection
        print("🔗 Creating connection...")
        connection = models.Connection(
            id=uuid.uuid4(),
            provider=models.ProviderEnum.other,  # Using 'other' since 'mock' doesn't exist in enum
            external_account_id="MOCK-123",
            name="Mock Ads Account",
            status="active",
            connected_at=datetime.utcnow(),
            workspace_id=workspace.id
        )
        db.add(connection)
        db.flush()
        
        # 4. Create fetch and import (required for MetricFacts)
        print("📥 Creating fetch and import records...")
        fetch = models.Fetch(
            id=uuid.uuid4(),
            kind="mock_data",
            status="completed", 
            started_at=datetime.utcnow() - timedelta(hours=1),
            finished_at=datetime.utcnow(),
            range_start=datetime.utcnow() - timedelta(days=30),
            range_end=datetime.utcnow(),
            connection_id=connection.id
        )
        db.add(fetch)
        db.flush()
        
        import_record = models.Import(
            id=uuid.uuid4(),
            as_of=datetime.utcnow(),
            created_at=datetime.utcnow(),
            note="Mock seed data import",
            fetch_id=fetch.id
        )
        db.add(import_record)
        db.flush()
        
        # 5. Create entity hierarchy
        print("🏗️ Creating entity hierarchy...")
        campaigns = []
        adsets = []
        ads = []
        
        # Create 2 campaigns
        for i in range(1, 3):
            campaign = models.Entity(
                id=uuid.uuid4(),
                level=models.LevelEnum.campaign,
                external_id=f"CAMP-{i:03d}",
                name=f"Campaign {i} - Holiday Promotion",
                status="active",
                parent_id=None,  # Campaigns have no parent
                workspace_id=workspace.id,
                connection_id=connection.id
            )
            campaigns.append(campaign)
            db.add(campaign)
        
        db.flush()  # Get campaign IDs
        
        # Create 2 adsets per campaign
        for campaign in campaigns:
            for j in range(1, 3):
                adset = models.Entity(
                    id=uuid.uuid4(),
                    level=models.LevelEnum.adset,
                    external_id=f"ADSET-{campaign.external_id}-{j:03d}",
                    name=f"AdSet {j} - {campaign.name}",
                    status="active",
                    parent_id=campaign.id,
                    workspace_id=workspace.id,
                    connection_id=connection.id
                )
                adsets.append(adset)
                db.add(adset)
        
        db.flush()  # Get adset IDs
        
        # Create 2 ads per adset
        for adset in adsets:
            for k in range(1, 3):
                ad = models.Entity(
                    id=uuid.uuid4(),
                    level=models.LevelEnum.ad,
                    external_id=f"AD-{adset.external_id}-{k:03d}",
                    name=f"Ad {k} - {adset.name}",
                    status="active", 
                    parent_id=adset.id,
                    workspace_id=workspace.id,
                    connection_id=connection.id
                )
                ads.append(ad)
                db.add(ad)
        
        db.flush()  # Get ad IDs
        
        # 6. Generate 30 days of MetricFact data for each ad
        print("📊 Generating metric facts...")
        today = datetime.utcnow().date()
        
        for ad in ads:
            for day_offset in range(30):
                event_date = today - timedelta(days=day_offset)
                event_datetime = datetime.combine(event_date, datetime.min.time())
                
                metrics = generate_random_metrics()
                
                fact = models.MetricFact(
                    id=uuid.uuid4(),
                    entity_id=ad.id,
                    provider=models.ProviderEnum.other,
                    level=models.LevelEnum.ad,
                    event_at=event_datetime,
                    event_date=event_datetime,
                    spend=metrics['spend'],
                    impressions=metrics['impressions'],
                    clicks=metrics['clicks'],
                    conversions=metrics['conversions'],
                    revenue=metrics['revenue'],
                    currency="EUR",
                    natural_key=f"{ad.id}-{event_date}",
                    ingested_at=datetime.utcnow(),
                    import_id=import_record.id
                )
                db.add(fact)
        
        # 7. Create ComputeRun and P&L snapshots
        print("💰 Creating compute run and P&L data...")
        compute_run = models.ComputeRun(
            id=uuid.uuid4(),
            as_of=datetime.utcnow(),
            computed_at=datetime.utcnow(),
            reason="mock seed",
            status="success",
            type=models.ComputeRunTypeEnum.snapshot,
            workspace_id=workspace.id
        )
        db.add(compute_run)
        db.flush()
        
        # Calculate P&L for each campaign
        for campaign in campaigns:
            # Get all facts for this campaign's ads
            campaign_facts = db.query(models.MetricFact).join(
                models.Entity, models.MetricFact.entity_id == models.Entity.id
            ).filter(
                models.Entity.parent_id.in_([adset.id for adset in adsets if adset.parent_id == campaign.id])
            ).all()
            
            if campaign_facts:
                # Aggregate metrics
                total_spend = sum(float(fact.spend) for fact in campaign_facts)
                total_revenue = sum(float(fact.revenue or 0) for fact in campaign_facts)
                total_conversions = sum(float(fact.conversions or 0) for fact in campaign_facts)
                total_clicks = sum(fact.clicks for fact in campaign_facts)
                total_impressions = sum(fact.impressions for fact in campaign_facts)
                
                # Calculate derived metrics
                cpa = safe_divide(total_spend, total_conversions)
                roas = safe_divide(total_revenue, total_spend)
                
                pnl = models.Pnl(
                    id=uuid.uuid4(),
                    entity_id=campaign.id,
                    run_id=compute_run.id,
                    provider=models.ProviderEnum.other,
                    level=models.LevelEnum.campaign,
                    kind=models.KindEnum.snapshot,
                    as_of=datetime.utcnow(),
                    event_date=None,  # Snapshot doesn't have specific event date
                    spend=total_spend,
                    revenue=total_revenue,
                    conversions=total_conversions,
                    clicks=total_clicks,
                    impressions=total_impressions,
                    cpa=cpa,
                    roas=roas,
                    computed_at=datetime.utcnow()
                )
                db.add(pnl)
        
        # Commit all changes
        db.commit()
        
        # Print summary
        print("\n🎉 Seed complete!")
        print(f"✅ Created workspace: {workspace.name}")
        print(f"✅ Created {len([owner, viewer])} users")
        print(f"✅ Created {len([connection])} connection")
        print(f"✅ Created {len(campaigns)} campaigns, {len(adsets)} adsets, {len(ads)} ads")
        print(f"✅ Generated {len(ads) * 30} metric facts (30 days × {len(ads)} ads)")
        print(f"✅ Created {len([compute_run])} compute run")
        print(f"✅ Generated {len(campaigns)} P&L snapshots")
        print("\n📝 Login credentials:")
        print("   Owner: owner@defanglabs.com / password123")
        print("   Viewer: viewer@defanglabs.com / password123")
        print("\n🔗 View data at: http://localhost:8000/admin")


if __name__ == "__main__":
    seed()
