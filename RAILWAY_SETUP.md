# Railway PostgreSQL Setup Guide

This guide will walk you through setting up a PostgreSQL database on Railway for AdNavi.

## Step 1: Create Railway Account

1. Go to [Railway](https://railway.app)
2. Sign up or log in with GitHub
3. Railway offers a free trial with $5 credit

## Step 2: Create New Project

1. Click "New Project"
2. Select "Provision PostgreSQL"
3. Railway will automatically provision a PostgreSQL database

## Step 3: Get Database Connection String

1. Click on your PostgreSQL service
2. Go to "Connect" tab
3. Copy the "DATABASE_URL" connection string
   - Format: `postgresql://user:password@host:port/dbname`
   - Example: `postgresql://postgres:abc123@containers-us-west-1.railway.app:5432/railway`

## Step 4: Configure Database Settings (Optional)

### Enable Public Networking (if not enabled)

1. In PostgreSQL service settings
2. Go to "Settings" → "Networking"
3. Ensure "Public Networking" is enabled (should be default)

### Backups (Recommended for Production)

1. Railway automatically backs up your database
2. You can restore from snapshots in the "Data" tab

## Step 5: Run Migrations

From your local machine with the Railway DATABASE_URL:

```bash
cd backend
export DATABASE_URL="postgresql://user:password@host:port/dbname"

# Run migrations
./deploy_setup.sh
```

Or manually:

```bash
# Run migrations only
alembic upgrade head

# Seed database (optional)
python -m app.seed_mock
```

## Step 6: Verify Database Setup

Connect to your Railway database to verify:

### Option 1: Using Railway CLI

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Connect to database
railway connect postgres
```

### Option 2: Using psql

```bash
psql "postgresql://user:password@host:port/dbname"

# List tables
\dt

# Check workspace
SELECT * FROM workspaces;

# Exit
\q
```

## Database Schema Overview

After migrations, you should have these tables:

- `workspaces` - Top-level organizations
- `users` - User accounts
- `auth_credentials` - Password hashes
- `connections` - Ad platform connections
- `tokens` - OAuth tokens
- `entities` - Campaigns, ad sets, ads hierarchy
- `fetches` - Data fetch operations
- `imports` - Import records
- `metric_facts` - Raw performance metrics
- `compute_runs` - Calculation jobs
- `pnls` - Profit & loss analytics
- `qa_query_logs` - AI query logs

## Monitoring and Maintenance

### View Database Metrics

In Railway dashboard:
- CPU usage
- Memory usage
- Disk usage
- Connection count

### Database Limits (Free Tier)

- Storage: 1 GB
- Connections: 100
- RAM: 512 MB

### Upgrade to Paid Plan

If you need more resources:
1. Go to your project settings
2. Select "Upgrade to Hobby" or "Upgrade to Pro"
3. Pricing: ~$5/month for Hobby plan

## Security Best Practices

1. **Never commit DATABASE_URL to git**
   - It's in `.gitignore` by default

2. **Rotate credentials periodically**
   - Generate new credentials in Railway settings

3. **Use environment variables**
   - Set DATABASE_URL in Defang config, not in code

4. **Enable SSL**
   - Railway enforces SSL by default

5. **Monitor access logs**
   - Check Railway logs for suspicious activity

## Troubleshooting

### Cannot connect to database

- Check if Railway service is running
- Verify DATABASE_URL format is correct
- Ensure your IP is not blocked (Railway allows all IPs by default)

### Migrations fail

- Check if DATABASE_URL is correct
- Verify Alembic is installed: `pip install alembic`
- Check migration files exist in `backend/alembic/versions/`

### Out of storage

- Check current usage in Railway dashboard
- Clean up old data or upgrade plan
- Consider archiving old metric_facts

### Too many connections

- Railway free tier: 100 concurrent connections
- Check if connection pooling is working
- Close unused connections
- Upgrade to paid plan for more connections

## Useful SQL Queries

### Check database size

```sql
SELECT pg_size_pretty(pg_database_size('railway'));
```

### Count records in all tables

```sql
SELECT 
  schemaname,
  tablename,
  pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size,
  n_tup_ins AS inserts
FROM pg_stat_user_tables
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;
```

### Check active connections

```sql
SELECT count(*) FROM pg_stat_activity;
```

## Next Steps

After setting up Railway:

1. ✅ Get DATABASE_URL
2. ✅ Run migrations
3. ✅ Seed database (optional)
4. → Set DATABASE_URL in Defang config
5. → Deploy to Defang Playground

See `DEPLOYMENT_GUIDE.md` for full deployment instructions.

