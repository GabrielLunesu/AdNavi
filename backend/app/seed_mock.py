"""Seed script to populate the database with realistic mock data for testing.

Derived Metrics v1 changes:
- Assigns goals to campaigns (awareness, leads, purchases, app_installs, etc.)
- Generates base measures appropriate to each goal (leads, installs, purchases, visitors, profit)
- Uses compute_service for P&L snapshots (validates metrics/registry integration)

Usage:
    cd backend
    python -m app.seed_mock

This script will:
1. Wipe existing data
2. Create "Defang Labs" workspace with 2 users
3. Create a mock connection with entity hierarchy (campaigns > adsets > ads)
4. Assign goals to campaigns (varying objectives)
5. Generate 30 days of MetricFact data with goal-aware base measures
6. Use compute_service to generate P&L snapshots with ALL derived metrics
"""

from datetime import datetime, timedelta
import random
import uuid

from app.database import SessionLocal
from app import models
from app.security import get_password_hash
from app.services.compute_service import run_compute_snapshot


def generate_random_metrics(goal: str, provider: str):
    """Generate realistic ad metrics for a single day based on campaign goal.
    
    Derived Metrics v1: Generates goal-aware base measures.
    
    Args:
        goal: Campaign objective (awareness, traffic, leads, app_installs, purchases, conversions)
        provider: Ad provider (affects typical CTR/CVR ranges)
        
    Returns:
        Dict with base measures appropriate for the goal
        
    Design philosophy:
    - Start with impressions (always present)
    - Derive clicks from CTR (varies by provider)
    - Derive conversions/leads/installs/purchases from CVR (varies by goal)
    - Generate revenue based on AOV (varies by goal)
    - Generate profit as revenue * margin (varies by provider/goal)
    - Generate visitors for traffic/awareness goals
    
    Typical values (approximate industry averages):
    - CTR: 0.5-3% (display < social < search)
    - CVR: 2-10% (depends on funnel quality)
    - CPM: $5-$20 (varies by provider)
    - AOV: $50-$200 (varies by industry)
    - Margin: 20-40% (varies by business model)
    """
    
    # Base: impressions (always present)
    impressions = random.randint(1000, 10000)
    
    # Provider-specific CTR ranges
    ctr_ranges = {
        "google": (0.02, 0.05),  # 2-5% (search ads)
        "meta": (0.01, 0.03),    # 1-3% (social ads)
        "tiktok": (0.015, 0.035), # 1.5-3.5% (social video)
        "other": (0.01, 0.025),  # 1-2.5% (display)
    }
    ctr = random.uniform(*ctr_ranges.get(provider, (0.01, 0.025)))
    clicks = int(impressions * ctr)
    
    # Goal-specific conversion rates and metrics
    if goal == "awareness":
        # Focus: impressions, CPM, visitors
        conversions = random.uniform(0, 5)  # Few conversions
        revenue = conversions * random.uniform(20, 50) if conversions > 0 else 0
        leads = 0
        installs = 0
        purchases = 0
        visitors = int(clicks * random.uniform(0.8, 0.95))  # Most clickers → landing page
        
    elif goal == "traffic":
        # Focus: clicks, CPC, CTR, visitors
        conversions = random.uniform(5, 20)
        revenue = conversions * random.uniform(30, 80)
        leads = 0
        installs = 0
        purchases = 0
        visitors = int(clicks * random.uniform(0.85, 0.98))  # High visitor rate
        
    elif goal == "leads":
        # Focus: leads, CPL, lead volume
        leads = clicks * random.uniform(0.1, 0.25)  # 10-25% lead conversion rate
        conversions = leads  # Leads ARE the conversions for this goal
        revenue = conversions * random.uniform(0, 10)  # Some leads convert to revenue
        installs = 0
        purchases = 0
        visitors = int(clicks * 0.9)
        
    elif goal == "app_installs":
        # Focus: installs, CPI, install volume
        installs = int(clicks * random.uniform(0.05, 0.15))  # 5-15% install rate
        conversions = installs  # Installs ARE the conversions for this goal
        revenue = installs * random.uniform(0, 5)  # Some installs → in-app purchases
        leads = 0
        purchases = 0
        visitors = 0  # App installs don't have "visitors" concept
        
    elif goal == "purchases":
        # Focus: purchases, CPP, AOV, revenue
        purchases = int(clicks * random.uniform(0.02, 0.08))  # 2-8% purchase rate
        conversions = purchases  # Purchases ARE the conversions for this goal
        revenue = purchases * random.uniform(50, 200)  # AOV: $50-200
        leads = 0
        installs = 0
        visitors = int(clicks * 0.92)
        
    else:  # "conversions" or "other"
        # Generic conversions (could be signup, download, etc.)
        conversions = clicks * random.uniform(0.03, 0.12)  # 3-12% CVR
        revenue = conversions * random.uniform(40, 120)
        leads = 0
        installs = 0
        purchases = 0
        visitors = int(clicks * 0.88)
    
    # Spend: derived from CPM (varies by provider)
    cpm_ranges = {
        "google": (8, 20),   # Higher (search premium)
        "meta": (5, 15),     # Mid-range (social)
        "tiktok": (6, 18),   # Mid-high (social video)
        "other": (5, 12),    # Lower (display)
    }
    cpm = random.uniform(*cpm_ranges.get(provider, (5, 12)))
    spend = (impressions / 1000) * cpm
    
    # Profit: revenue * margin (varies by business model)
    margin = random.uniform(0.2, 0.4)  # 20-40% margin
    profit = revenue * margin if revenue > 0 else 0
    
    return {
        'spend': round(spend, 2),
        'impressions': impressions,
        'clicks': clicks,
        'conversions': round(conversions, 2),
        'revenue': round(revenue, 2),
        # Derived Metrics v1: New base measures
        'leads': round(leads, 2) if leads > 0 else None,
        'installs': int(installs) if installs > 0 else None,
        'purchases': int(purchases) if purchases > 0 else None,
        'visitors': int(visitors) if visitors > 0 else None,
        'profit': round(profit, 2) if profit > 0 else None,
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
        
        # Derived Metrics v1: Create campaigns with varying goals
        campaign_configs = [
            {"name": "Holiday Sale - Purchases", "goal": models.GoalEnum.purchases, "provider": models.ProviderEnum.meta},
            {"name": "App Install Campaign", "goal": models.GoalEnum.app_installs, "provider": models.ProviderEnum.google},
            {"name": "Lead Gen - B2B", "goal": models.GoalEnum.leads, "provider": models.ProviderEnum.google},
            {"name": "Brand Awareness", "goal": models.GoalEnum.awareness, "provider": models.ProviderEnum.tiktok},
        ]
        
        for i, config in enumerate(campaign_configs, start=1):
            campaign = models.Entity(
                id=uuid.uuid4(),
                level=models.LevelEnum.campaign,
                external_id=f"CAMP-{i:03d}",
                name=config["name"],
                status="active" if i <= 3 else "paused",  # Last campaign is paused
                parent_id=None,  # Campaigns have no parent
                workspace_id=workspace.id,
                connection_id=connection.id,
                goal=config["goal"]  # Derived Metrics v1: Campaign objective
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
        print("📊 Generating metric facts (goal-aware)...")
        today = datetime.utcnow().date()
        
        for ad in ads:
            # Find ad's campaign to get goal
            adset = next(a for a in adsets if a.id == ad.parent_id)
            campaign = next(c for c in campaigns if c.id == adset.parent_id)
            goal = campaign.goal.value
            provider = connection.provider.value
            
            for day_offset in range(30):
                event_date = today - timedelta(days=day_offset)
                event_datetime = datetime.combine(event_date, datetime.min.time())
                
                # Derived Metrics v1: Generate goal-aware metrics
                metrics = generate_random_metrics(goal, provider)
                
                fact = models.MetricFact(
                    id=uuid.uuid4(),
                    entity_id=ad.id,
                    provider=connection.provider,
                    level=models.LevelEnum.ad,
                    event_at=event_datetime,
                    event_date=event_datetime,
                    # Original base measures
                    spend=metrics['spend'],
                    impressions=metrics['impressions'],
                    clicks=metrics['clicks'],
                    conversions=metrics['conversions'],
                    revenue=metrics['revenue'],
                    # Derived Metrics v1: New base measures
                    leads=metrics['leads'],
                    installs=metrics['installs'],
                    purchases=metrics['purchases'],
                    visitors=metrics['visitors'],
                    profit=metrics['profit'],
                    currency="EUR",
                    natural_key=f"{ad.id}-{event_date}",
                    ingested_at=datetime.utcnow(),
                    import_id=import_record.id
                )
                db.add(fact)
        
        # Commit MetricFacts before running compute
        db.commit()
        
        # 7. Use compute_service to generate P&L snapshots
        # Derived Metrics v1: Uses metrics/registry for ALL derived metrics
        print("💰 Running compute service to generate P&L snapshots...")
        try:
            run_id = run_compute_snapshot(
                db=db,
                workspace_id=str(workspace.id),
                as_of=datetime.utcnow(),
                reason="Mock seed data snapshot",
                kind="snapshot"
            )
            print(f"✅ Compute run created: {run_id}")
        except Exception as e:
            print(f"⚠️  Compute service error: {e}")
            print("   (This is expected if you haven't run migrations yet)")
        
        # Verify P&L was created
        pnl_count = db.query(models.Pnl).count()
        print(f"✅ Generated {pnl_count} P&L snapshots with ALL derived metrics")
        
        # Print summary
        print("\n🎉 Seed complete!")
        print(f"✅ Created workspace: {workspace.name}")
        print(f"✅ Created {len([owner, viewer])} users")
        print(f"✅ Created {len([connection])} connection")
        print(f"✅ Created {len(campaigns)} campaigns with goals:")
        for c in campaigns:
            print(f"   - {c.name} (goal: {c.goal.value})")
        print(f"✅ Created {len(adsets)} adsets, {len(ads)} ads")
        print(f"✅ Generated {len(ads) * 30} metric facts (30 days × {len(ads)} ads)")
        print(f"   - Includes NEW base measures: leads, installs, purchases, visitors, profit")
        print(f"✅ P&L snapshots include ALL derived metrics:")
        print(f"   - Cost: CPC, CPM, CPA, CPL, CPI, CPP")
        print(f"   - Value: ROAS, POAS, ARPV, AOV")
        print(f"   - Engagement: CTR, CVR")
        print("\n📝 Login credentials:")
        print("   Owner: owner@defanglabs.com / password123")
        print("   Viewer: viewer@defanglabs.com / password123")
        print("\n🔗 View data at: http://localhost:8000/admin")
        print("\n🧪 Test queries (try in Swagger UI /docs):")
        print('   - "What was my CPC last week?"')
        print('   - "Show me CPL for the lead gen campaign"')
        print('   - "What\'s my average order value this month?"')
        print('   - "Compare CTR by campaign"')


if __name__ == "__main__":
    seed()
