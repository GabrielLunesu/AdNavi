# 🚀 AdNavi Deployment - Command Reference

Copy and paste these commands in order to deploy AdNavi.

---

## 1️⃣ Login to Defang

```bash
defang login
```

---

## 2️⃣ Get Railway Database URL

1. Go to https://railway.app
2. Create project → Provision PostgreSQL
3. Copy the `DATABASE_URL` from Connect tab
4. It looks like: `postgresql://postgres:abc123xyz@containers-us-west.railway.app:5432/railway`

---

## 3️⃣ Configure Defang Environment Variables

**Replace the values below with your actual values!**

```bash
cd /Users/gabriellunesu/Git/AdNavi

# Set Railway database URL (REQUIRED - paste your actual URL)
defang config set --name DATABASE_URL --value "postgresql://postgres:YOUR_PASSWORD@YOUR_HOST:5432/railway"

# Generate and set JWT secret (REQUIRED - run as-is)
defang config set --name JWT_SECRET --value "$(openssl rand -hex 32)"

# Generate and set admin secret (REQUIRED - run as-is)
defang config set --name ADMIN_SECRET_KEY --value "$(openssl rand -hex 32)"

# Set temporary CORS values (REQUIRED - run as-is, will update later)
defang config set --name BACKEND_CORS_ORIGINS --value "http://localhost:3000"
defang config set --name COOKIE_DOMAIN --value "localhost"
defang config set --name NEXT_PUBLIC_API_URL --value "http://localhost:8000"

# Optional: Set OpenAI API key (OPTIONAL - only if you have one)
# defang config set --name OPENAI_API_KEY --value "sk-your-key-here"
```

**Verify configuration:**
```bash
defang config list
```

---

## 4️⃣ Run Database Migrations & Seed

```bash
cd /Users/gabriellunesu/Git/AdNavi/backend

# Export your Railway database URL (paste your actual URL)
export DATABASE_URL="postgresql://postgres:YOUR_PASSWORD@YOUR_HOST:5432/railway"

# Run the setup script
./deploy_setup.sh
```

When prompted "Do you want to seed the database with mock data? (y/n)", type `y` and press Enter.

---

## 5️⃣ Deploy to Defang Playground

```bash
cd /Users/gabriellunesu/Git/AdNavi

# Deploy both services
defang compose up
```

**Wait for deployment to complete.** You'll see URLs like:
```
✅ Service 'backend' deployed at: https://backend-abc123.defang.dev
✅ Service 'ui' deployed at: https://ui-xyz789.defang.dev
```

**Copy these URLs!** You'll need them for the next step.

---

## 6️⃣ Update CORS Configuration

**Replace the URLs below with your actual Defang URLs from step 5:**

```bash
# Update backend CORS to allow frontend domain
defang config set --name BACKEND_CORS_ORIGINS --value "https://ui-xyz789.defang.dev"

# Update cookie domain (remove https:// prefix)
defang config set --name COOKIE_DOMAIN --value "ui-xyz789.defang.dev"

# Update frontend API URL
defang config set --name NEXT_PUBLIC_API_URL --value "https://backend-abc123.defang.dev"

# Redeploy to apply new configuration
defang compose up
```

---

## 7️⃣ Verify Deployment

### Test Backend Health
```bash
# Replace with your actual backend URL
curl https://backend-abc123.defang.dev/health
```

Expected response: `{"status":"ok"}`

### Open in Browser

1. **Frontend**: https://ui-xyz789.defang.dev
   - Login: `owner@defanglabs.com` / `password123`

2. **API Docs**: https://backend-abc123.defang.dev/docs

3. **Admin Panel**: https://backend-abc123.defang.dev/admin
   - Login: `admin` / `secret`

---

## 🎉 Done!

Your AdNavi instance is now live in production!

---

## 📊 View Logs (Optional)

```bash
# Backend logs
defang logs --service backend

# Frontend logs
defang logs --service ui

# Service status
defang services
```

---

## 🔄 Redeploy After Code Changes

```bash
cd /Users/gabriellunesu/Git/AdNavi

# Make your changes, then:
git add .
git commit -m "Your change description"
defang compose up
```

---

## 🛑 Stop Services

```bash
defang compose down
```

**Note:** This stops the services but doesn't delete your Railway database.

---

## 💡 Quick Troubleshooting

### "DATABASE_URL is not set" error
```bash
# Check if it's configured:
defang config list

# If not there, set it again:
defang config set --name DATABASE_URL --value "postgresql://..."
```

### CORS errors in browser console
```bash
# Make sure BACKEND_CORS_ORIGINS matches frontend URL exactly:
defang config set --name BACKEND_CORS_ORIGINS --value "https://ui-xyz789.defang.dev"
defang compose up
```

### "Token is expired" for Defang
```bash
defang login
```

### Can't connect to Railway database
- Check Railway service is running (should show "Active" in Railway dashboard)
- Verify DATABASE_URL is correct (copy it again from Railway)
- Try connecting with psql: `psql "your-database-url"`

---

## 📖 Full Documentation

- **Quick Start**: `QUICK_START_DEPLOY.md`
- **Comprehensive Guide**: `DEPLOYMENT_GUIDE.md`
- **Railway Setup**: `RAILWAY_SETUP.md`
- **Deployment Status**: `DEPLOYMENT_READY.md`

---

**Need Help?** All commands are ready to copy-paste. Just replace the placeholder URLs with your actual values! 🚀

