"""Clean database script to remove mock seed data.

WHAT: Removes all mock data from seed_mock.py, keeping only real workspace data
WHY: UI pages are showing mock data instead of real Meta Ads data
WHERE USED: Manual cleanup before production data sync

Usage:
    cd backend
    source bin/activate
    python -m app.clean_db

This script will:
1. Keep workspace "Defang Labs" if it exists (or create new one)
2. Keep real Meta connections (provider='meta')
3. Remove all mock connections (provider='other', external_account_id='MOCK-*')
4. Remove all entities/metrics associated with mock connections
5. Remove all manual costs (optional, can be kept)
"""

import sys
from datetime import datetime
from sqlalchemy import and_

from app.database import SessionLocal
from app import models


def clean_db(keep_manual_costs=True):
    """Clean mock data from database."""
    with SessionLocal() as db:
        print("🧹 Cleaning mock data from database...")
        
        # 1. Find mock connections
        mock_connections = db.query(models.Connection).filter(
            models.Connection.external_account_id.like('MOCK-%')
        ).all()
        
        mock_connection_ids = [c.id for c in mock_connections]
        print(f"   Found {len(mock_connections)} mock connection(s)")
        
        if not mock_connection_ids:
            print("   ✅ No mock connections found. Database is clean.")
            return
        
        # 2. Find all entities and imports FIRST (before deleting anything)
        mock_entities = db.query(models.Entity).filter(
            models.Entity.connection_id.in_(mock_connection_ids)
        ).all()
        test_entities = db.query(models.Entity).filter(
            models.Entity.external_id.like('test_%')
        ).all()
        all_entities = mock_entities + test_entities
        entity_ids = [e.id for e in all_entities]
        
        mock_fetches = db.query(models.Fetch).filter(
            models.Fetch.connection_id.in_(mock_connection_ids)
        ).all()
        fetch_ids = [f.id for f in mock_fetches]
        mock_imports = db.query(models.Import).filter(
            models.Import.fetch_id.in_(fetch_ids)
        ).all() if fetch_ids else []
        import_ids = [imp.id for imp in mock_imports]
        
        # 3. Delete P&L snapshots FIRST (they reference entities and compute runs)
        print("   💰 Deleting P&L snapshots (based on mock data)...")
        # Delete Pnl that reference mock entities OR all Pnl if we're cleaning everything
        if entity_ids:
            pnl_count = db.query(models.Pnl).filter(
                models.Pnl.entity_id.in_(entity_ids)
            ).delete(synchronize_session=False)
        else:
            pnl_count = db.query(models.Pnl).delete(synchronize_session=False)
        db.flush()  # Commit Pnl deletions before proceeding
        print(f"   ✅ Deleted {pnl_count} P&L snapshots")
        
        # 4. Delete metric facts (ALL that reference mock entities OR imports)
        print("   📊 Deleting metric facts from mock connections and test data...")
        
        # Use bulk delete for performance (much faster than loading into memory)
        # Note: We need to get entity_ids first because bulk delete doesn't work with joins
        all_entity_ids_for_facts = set(entity_ids) if entity_ids else set()
        
        # Add entity IDs from mock connections (can't use join with bulk delete)
        if mock_connection_ids:
            mock_entity_ids = [
                e.id for e in db.query(models.Entity).filter(
                    models.Entity.connection_id.in_(mock_connection_ids)
                ).all()
            ]
            all_entity_ids_for_facts.update(mock_entity_ids)
        
        total_deleted = 0
        
        # Delete facts by entity_id (combines both mock and test entities)
        if all_entity_ids_for_facts:
            fact_count = db.query(models.MetricFact).filter(
                models.MetricFact.entity_id.in_(list(all_entity_ids_for_facts))
            ).delete(synchronize_session=False)
            total_deleted += fact_count
            db.flush()
            if fact_count > 0:
                print(f"   ✅ Deleted {fact_count} metric facts by entity_id")
        
        # Delete facts that reference mock imports
        if import_ids:
            import_fact_count = db.query(models.MetricFact).filter(
                models.MetricFact.import_id.in_(import_ids)
            ).delete(synchronize_session=False)
            total_deleted += import_fact_count
            db.flush()
            if import_fact_count > 0:
                print(f"   ✅ Deleted {import_fact_count} metric facts from mock imports")
        
        print(f"   ✅ Total deleted: {total_deleted} metric facts")
        
        # 5. Delete entities
        print("   🏗️  Deleting entities from mock connections and test data...")
        entity_count = len(all_entities)
        if entity_ids:
            # Use bulk delete for better performance
            deleted_count = db.query(models.Entity).filter(
                models.Entity.id.in_(entity_ids)
            ).delete(synchronize_session=False)
            db.flush()
            print(f"   ✅ Deleted {deleted_count} entities ({len(mock_entities)} from mock, {len(test_entities)} test)")
        else:
            print(f"   ℹ️  No entities to delete")
        
        # 6. Delete imports (now safe since all referencing facts are deleted)
        print("   📥 Deleting imports...")
        import_count = len(mock_imports)
        if import_ids:
            deleted_imports = db.query(models.Import).filter(
                models.Import.id.in_(import_ids)
            ).delete(synchronize_session=False)
            db.flush()
            print(f"   ✅ Deleted {deleted_imports} imports")
        else:
            print(f"   ℹ️  No imports to delete")
        
        # 7. Delete fetches
        print("   📥 Deleting fetches...")
        fetch_count = len(mock_fetches)
        if fetch_ids:
            deleted_fetches = db.query(models.Fetch).filter(
                models.Fetch.id.in_(fetch_ids)
            ).delete(synchronize_session=False)
            db.flush()
            print(f"   ✅ Deleted {deleted_fetches} fetches")
        else:
            print(f"   ℹ️  No fetches to delete")
        
        # 8. Delete compute runs (after Pnl is deleted)
        print("   ⚙️  Deleting compute runs (based on mock data)...")
        compute_count = db.query(models.ComputeRun).count()
        if compute_count > 0:
            deleted_runs = db.query(models.ComputeRun).delete(synchronize_session=False)
            db.flush()
            print(f"   ✅ Deleted {deleted_runs} compute runs")
        else:
            print(f"   ℹ️  No compute runs to delete")
        
        # 9. Delete mock connections
        print("   🔗 Deleting mock connections...")
        if mock_connection_ids:
            deleted_connections = db.query(models.Connection).filter(
                models.Connection.id.in_(mock_connection_ids)
            ).delete(synchronize_session=False)
            db.flush()
            print(f"   ✅ Deleted {deleted_connections} mock connection(s)")
        else:
            print(f"   ℹ️  No mock connections to delete")
        
        # 10. Optionally delete manual costs
        if not keep_manual_costs:
            print("   💵 Deleting manual costs...")
            manual_cost_count = db.query(models.ManualCost).count()
            if manual_cost_count > 0:
                deleted_costs = db.query(models.ManualCost).delete(synchronize_session=False)
                db.flush()
                print(f"   ✅ Deleted {deleted_costs} manual costs")
            else:
                print(f"   ℹ️  No manual costs to delete")
        else:
            manual_cost_count = db.query(models.ManualCost).count()
            print(f"   ℹ️  Keeping {manual_cost_count} manual costs (use --delete-manual-costs to remove)")
        
        # 11. Final commit
        print("   💾 Committing all changes...")
        db.commit()
        print("   ✅ All changes committed")
        
        print("\n" + "="*70)
        print("✅ CLEANUP COMPLETE!")
        print("="*70)
        print(f"\n📊 SUMMARY:")
        print(f"   Mock connections deleted: {len(mock_connections)}")
        print(f"   Entities deleted: {entity_count}")
        print(f"   Metric facts deleted: {fact_count}")
        print(f"   Fetches deleted: {fetch_count}")
        print(f"   Imports deleted: {import_count}")
        print(f"   P&L snapshots deleted: {pnl_count}")
        print(f"   Compute runs deleted: {compute_count}")
        if not keep_manual_costs:
            print(f"   Manual costs deleted: {manual_cost_count}")
        else:
            print(f"   Manual costs kept: {manual_cost_count}")
        
        # Show remaining data
        remaining_connections = db.query(models.Connection).count()
        remaining_entities = db.query(models.Entity).count()
        remaining_facts = db.query(models.MetricFact).count()
        
        print(f"\n📈 REMAINING DATA:")
        print(f"   Connections: {remaining_connections}")
        print(f"   Entities: {remaining_entities}")
        print(f"   Metric facts: {remaining_facts}")
        
        if remaining_connections > 0:
            real_connections = db.query(models.Connection).all()
            print(f"\n🔗 REMAINING CONNECTIONS:")
            for conn in real_connections:
                print(f"   - {conn.name} ({conn.provider.value}, {conn.external_account_id})")
        
        print("="*70 + "\n")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Clean mock data from database')
    parser.add_argument(
        '--delete-manual-costs',
        action='store_true',
        help='Also delete manual costs (default: keep them)'
    )
    
    args = parser.parse_args()
    
    try:
        clean_db(keep_manual_costs=not args.delete_manual_costs)
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

