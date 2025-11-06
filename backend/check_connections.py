"""Quick script to check what connections exist in the database.

Usage:
    cd backend
    source bin/activate
    python check_connections.py
"""

from app.database import SessionLocal
from app import models

def check_connections():
    with SessionLocal() as db:
        print("=" * 70)
        print("DATABASE CONNECTIONS CHECK")
        print("=" * 70)
        
        # Get all connections
        all_connections = db.query(models.Connection).all()
        
        print(f"\n📊 Total connections in database: {len(all_connections)}\n")
        
        if len(all_connections) == 0:
            print("❌ No connections found in database!")
            print("\n💡 To create a Meta connection, you can:")
            print("   1. Use the admin panel at http://localhost:8000/admin")
            print("   2. Or create one via API/script")
            return
        
        # Group by provider
        by_provider = {}
        for conn in all_connections:
            provider = conn.provider.value
            if provider not in by_provider:
                by_provider[provider] = []
            by_provider[provider].append(conn)
        
        # Show by provider
        for provider, conns in sorted(by_provider.items()):
            print(f"\n🔗 {provider.upper()} Connections: {len(conns)}")
            for conn in conns:
                print(f"   - ID: {conn.id}")
                print(f"     Name: {conn.name}")
                print(f"     External ID: {conn.external_account_id}")
                print(f"     Status: {conn.status}")
                print(f"     Workspace ID: {conn.workspace_id}")
                print(f"     Connected: {conn.connected_at}")
                if conn.token_id:
                    token = db.query(models.Token).filter(models.Token.id == conn.token_id).first()
                    if token:
                        print(f"     Token: ✅ (scope: {token.scope})")
                    else:
                        print(f"     Token: ❌ (token_id exists but token not found)")
                else:
                    print(f"     Token: ❌ (no token)")
                print()
        
        # Check workspaces
        print("\n🏢 WORKSPACES:")
        workspaces = db.query(models.Workspace).all()
        for ws in workspaces:
            ws_conns = [c for c in all_connections if c.workspace_id == ws.id]
            print(f"   - {ws.name} (ID: {ws.id})")
            print(f"     Connections: {len(ws_conns)}")
            for conn in ws_conns:
                print(f"       • {conn.provider.value}: {conn.name} ({conn.status})")
            print()
        
        # Check Meta specifically
        meta_connections = [c for c in all_connections if c.provider.value == 'meta']
        print(f"\n📘 META CONNECTIONS: {len(meta_connections)}")
        if len(meta_connections) == 0:
            print("   ❌ No Meta connections found!")
            print("\n   💡 To create a Meta connection:")
            print("      1. Go to http://localhost:8000/admin")
            print("      2. Navigate to Connections")
            print("      3. Click 'Create'")
            print("      4. Fill in:")
            print("         - Provider: meta")
            print("         - External Account ID: your_meta_ad_account_id")
            print("         - Name: Meta Ads Account")
            print("         - Status: active")
            print("         - Workspace: select your workspace")
        else:
            for conn in meta_connections:
                print(f"   ✅ {conn.name} (ID: {conn.id})")
                print(f"      Status: {conn.status}")
                print(f"      Workspace: {conn.workspace_id}")
                print(f"      External ID: {conn.external_account_id}")
        
        print("\n" + "=" * 70)

if __name__ == "__main__":
    check_connections()

