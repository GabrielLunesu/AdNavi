# Quick Start Deployment Guide

Follow these steps to deploy AdNavi to production using Defang Playground and Railway.

## Prerequisites

- Defang CLI installed (`npm install -g defang` or download from defang.io)
- Railway account (free tier works)
- Git repository on prod branch

## 🚀 5-Minute Deployment

### Step 1: Set Up Railway Database (2 minutes)

1. Go to [railway.app](https://railway.app) and sign in
2. Click "New Project" → "Provision PostgreSQL"
3. Click on PostgreSQL service → "Connect" tab
4. Copy the `DATABASE_URL` (looks like: `postgresql://user:pass@host:port/db`)

### Step 2: Login to Defang

```bash
defang login
```

### Step 3: Set Configuration Variables (2 minutes)

```bash
cd /Users/gabriellunesu/Git/AdNavi

# Set your Railway database URL (REQUIRED)
defang config set --name DATABASE_URL --value "postgresql://user:pass@host:port/db"

# Generate and set secrets
defang config set --name JWT_SECRET --value "$(openssl rand -hex 32)"
defang config set --name ADMIN_SECRET_KEY --value "$(openssl rand -hex 32)"

# Set CORS (we'll update these after first deployment)
defang config set --name BACKEND_CORS_ORIGINS --value "http://localhost:3000"
defang config set --name COOKIE_DOMAIN --value "localhost"
defang config set --name NEXT_PUBLIC_API_URL --value "http://localhost:8000"

# Optional: Set OpenAI API key for AI features
defang config set --name OPENAI_API_KEY --value "sk-your-key-here"
```

### Step 4: Run Database Migrations (1 minute)

From your local machine:

```bash
cd backend

# Export Railway database URL
export DATABASE_URL="postgresql://user:pass@host:port/db"

# Run migrations and seed
./deploy_setup.sh
```

When asked if you want to seed the database, type `y` and press Enter.

This will create:
- Admin user: `owner@defanglabs.com` / `password123`
- Viewer user: `viewer@defanglabs.com` / `password123`
- 12 sample campaigns with 30 days of metrics

### Step 5: Deploy to Defang Playground (<1 minute to start)

```bash
cd /Users/gabriellunesu/Git/AdNavi

# Deploy both frontend and backend
defang compose up
```

Defang will:
- Build Docker images
- Deploy to Defang Playground
- Provide URLs for both services

**Note:** First deployment takes 3-5 minutes for builds.

### Step 6: Update CORS URLs

After deployment, Defang will show you the URLs:

```
✅ Service 'backend' deployed at: https://backend-abc123.defang.dev
✅ Service 'ui' deployed at: https://ui-xyz789.defang.dev
```

Update the configuration with actual URLs:

```bash
defang config set --name BACKEND_CORS_ORIGINS --value "https://ui-xyz789.defang.dev"
defang config set --name COOKIE_DOMAIN --value "ui-xyz789.defang.dev"
defang config set --name NEXT_PUBLIC_API_URL --value "https://backend-abc123.defang.dev"

# Redeploy to apply new config
defang compose up
```

### Step 7: Verify Deployment

1. **Backend Health Check**
   ```bash
   curl https://backend-abc123.defang.dev/health
   ```
   Should return: `{"status":"ok"}`

2. **API Documentation**
   - Visit: `https://backend-abc123.defang.dev/docs`

3. **Admin Panel**
   - Visit: `https://backend-abc123.defang.dev/admin`
   - Login: `admin` / `secret`

4. **Frontend**
   - Visit: `https://ui-xyz789.defang.dev`
   - Login: `owner@defanglabs.com` / `password123`

## 🎉 You're Done!

Your AdNavi instance is now live!

## Common Issues

### "DATABASE_URL is not set"
- Make sure you set it in Defang: `defang config list`
- Verify it's in the correct format: `postgresql://user:pass@host:port/db`

### CORS errors in browser
- Check `BACKEND_CORS_ORIGINS` matches frontend URL exactly
- Make sure to redeploy after updating config

### Frontend can't reach backend
- Verify `NEXT_PUBLIC_API_URL` is set correctly
- Check backend is healthy: `curl https://backend-url/health`

### Builds failing
- Check logs: `defang logs --service backend` or `defang logs --service ui`
- Verify Dockerfile syntax

## Useful Commands

```bash
# View deployed services
defang services

# View logs
defang logs --service backend
defang logs --service ui

# List all config variables
defang config list

# Stop all services (won't delete data)
defang compose down

# Redeploy after code changes
git add . && git commit -m "Update" && defang compose up

# Cost estimate
defang estimate --provider AWS
```

## Next Steps

1. ✅ Change admin password in `backend/app/authentication.py`
2. ✅ Update seeded user passwords for production
3. ✅ Set up custom domain (optional)
4. ✅ Configure Railway backups
5. ✅ Monitor usage and costs

## Need Help?

- Defang Docs: https://docs.defang.io
- Railway Docs: https://docs.railway.app
- AdNavi Docs: See `DEPLOYMENT_GUIDE.md` and `RAILWAY_SETUP.md`

