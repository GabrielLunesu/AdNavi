# AdNavi Deployment Guide

This guide covers deploying AdNavi to production using Defang for application hosting and Railway for the PostgreSQL database.

## Architecture Overview

- **Frontend**: Next.js application (ui/)
- **Backend**: FastAPI application (backend/)
- **Database**: PostgreSQL (hosted on Railway)
- **Container Orchestration**: Defang Playground

## Prerequisites

1. **Defang CLI** installed and authenticated
2. **Railway account** with PostgreSQL database provisioned
3. **Environment variables** configured

## Step 1: Set Up Railway Database

1. Go to [Railway](https://railway.app)
2. Create a new project
3. Add PostgreSQL service
4. Copy the connection string (format: `postgresql://user:password@host:port/dbname`)
5. Note: Railway provides the `DATABASE_URL` environment variable automatically

## Step 2: Configure Environment Variables

You'll need to set these environment variables in Defang:

### Required Variables

```bash
# Database (from Railway)
DATABASE_URL=postgresql://user:password@host:port/dbname

# Security - MUST CHANGE THESE IN PRODUCTION
JWT_SECRET=<generate-a-strong-random-secret>
ADMIN_SECRET_KEY=<generate-a-strong-random-secret>

# CORS - Set to your Defang frontend URL
BACKEND_CORS_ORIGINS=https://your-frontend-url.defang.dev
COOKIE_DOMAIN=your-frontend-domain.defang.dev

# API URL - Set to your Defang backend URL
NEXT_PUBLIC_API_URL=https://your-backend-url.defang.dev
```

### Optional Variables

```bash
# OpenAI (for AI-powered features)
OPENAI_API_KEY=sk-...

# JWT expiration (default: 7 days)
JWT_EXPIRES_MINUTES=10080
```

### Generating Secrets

```bash
# Generate JWT_SECRET
openssl rand -hex 32

# Generate ADMIN_SECRET_KEY
openssl rand -hex 32
```

## Step 3: Set Defang Configuration Variables

```bash
# Navigate to project root
cd /Users/gabriellunesu/Git/AdNavi

# Set configuration variables
defang config set --name DATABASE_URL --value "your-railway-database-url"
defang config set --name JWT_SECRET --value "your-jwt-secret"
defang config set --name ADMIN_SECRET_KEY --value "your-admin-secret"
defang config set --name BACKEND_CORS_ORIGINS --value "https://your-frontend-url.defang.dev"
defang config set --name COOKIE_DOMAIN --value "your-frontend-domain.defang.dev"
defang config set --name NEXT_PUBLIC_API_URL --value "https://your-backend-url.defang.dev"
defang config set --name OPENAI_API_KEY --value "your-openai-key"
```

## Step 4: Run Database Migrations

Before deploying, you need to run Alembic migrations on your Railway database:

```bash
# From your local machine with Railway database URL
cd backend
export DATABASE_URL="your-railway-database-url"
alembic upgrade head
```

## Step 5: Seed the Database (Optional)

To populate the database with mock data:

```bash
cd backend
export DATABASE_URL="your-railway-database-url"
python -m app.seed_mock
```

This creates:
- Workspace: "Defang Labs"
- Users: owner@defanglabs.com / viewer@defanglabs.com (password: password123)
- Sample campaigns with 30 days of metric data

## Step 6: Deploy to Defang Playground

```bash
# From project root
cd /Users/gabriellunesu/Git/AdNavi

# Deploy both services
defang compose up
```

This will:
1. Build Docker images for both frontend and backend
2. Deploy to Defang Playground
3. Provide URLs for both services

## Step 7: Update CORS and API URLs

After first deployment, Defang will give you the actual URLs. You need to update the configuration:

```bash
# Update with actual Defang URLs
defang config set --name BACKEND_CORS_ORIGINS --value "https://actual-frontend-url.defang.dev"
defang config set --name COOKIE_DOMAIN --value "actual-frontend-domain.defang.dev"
defang config set --name NEXT_PUBLIC_API_URL --value "https://actual-backend-url.defang.dev"

# Redeploy to apply new config
defang compose up
```

## Step 8: Verify Deployment

1. **Backend Health Check**
   ```bash
   curl https://your-backend-url.defang.dev/health
   ```

2. **Backend API Docs**
   - Visit: `https://your-backend-url.defang.dev/docs`

3. **Admin Panel**
   - Visit: `https://your-backend-url.defang.dev/admin`
   - Login: admin / secret (hardcoded for now)

4. **Frontend**
   - Visit: `https://your-frontend-url.defang.dev`

## Monitoring and Logs

```bash
# View service status
defang services

# View logs
defang logs --service backend
defang logs --service ui
```

## Troubleshooting

### Database Connection Issues

- Verify Railway database is running
- Check `DATABASE_URL` is correctly set
- Ensure Railway allows external connections (should be default)

### CORS Errors

- Verify `BACKEND_CORS_ORIGINS` matches frontend URL exactly
- Check `COOKIE_DOMAIN` is set correctly

### Migration Issues

- Ensure migrations ran successfully: `alembic current`
- Check database tables exist: Connect to Railway DB and list tables

### Build Failures

- Check Docker build logs: `defang logs`
- Verify all dependencies in requirements.txt / package.json

## Security Checklist

- [x] Change default admin credentials in `backend/app/authentication.py`
- [ ] Generate unique `JWT_SECRET` and `ADMIN_SECRET_KEY`
- [ ] Set appropriate `BACKEND_CORS_ORIGINS` (not wildcard)
- [ ] Use secure passwords for seeded users in production
- [ ] Enable Railway database backups
- [ ] Review and rotate secrets regularly

## Cost Estimation

```bash
# Estimate costs for AWS deployment
defang estimate --provider AWS --deployment-mode AFFORDABLE
```

## Useful Commands

```bash
# List all config variables
defang config list

# Remove a config variable
defang config remove --name VARIABLE_NAME

# Destroy all services
defang compose down

# SSH into a container (if needed)
defang ssh --service backend
```

## Next Steps After Deployment

1. Update default admin credentials
2. Create production user accounts
3. Set up monitoring and alerting
4. Configure Railway database backups
5. Set up custom domain (optional)
6. Enable SSL/TLS (Defang provides this automatically)

## Support

- Defang Docs: https://docs.defang.io
- Railway Docs: https://docs.railway.app

