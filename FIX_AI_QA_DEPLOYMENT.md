# Fix AI/QA Deployment Issues

## Problem Identified
The AI/QA functionality is failing due to:
1. **Mixed Content Error**: Frontend served over HTTPS is trying to make HTTP requests
2. **Missing Environment Variables**: NEXT_PUBLIC_API_URL not properly set during build
3. **Missing OpenAI API Key**: Backend needs OPENAI_API_KEY for AI features
4. **CORS Configuration**: Backend needs to allow the production frontend domain

## Quick Fix Steps

### 1. Set Environment Variables in Defang

First, ensure these environment variables are set in your Defang deployment:

```bash
# Backend environment variables
defang config set DATABASE_URL "your-production-database-url"
defang config set JWT_SECRET "your-secure-jwt-secret-here"
defang config set JWT_EXPIRES_MINUTES "10080"
defang config set ADMIN_SECRET_KEY "your-secure-admin-key-here"
defang config set BACKEND_CORS_ORIGINS "https://t8zgrthold5r2-ui--3000.prod1a.defang.dev"
defang config set COOKIE_DOMAIN ".defang.dev"
defang config set OPENAI_API_KEY "your-openai-api-key-here"
```

### 2. Verify Backend URL

Check your backend URL by running:
```bash
defang services
```

The backend URL should be something like: `https://t8zgrthold5r2-backend--8000.prod1a.defang.dev`

### 3. Update compose.yaml if needed

If the backend URL in compose.yaml doesn't match your actual backend URL, update it:

```yaml
services:
  ui:
    build:
      args:
        NEXT_PUBLIC_API_URL: https://YOUR-ACTUAL-BACKEND-URL
    environment:
      - NEXT_PUBLIC_API_URL=https://YOUR-ACTUAL-BACKEND-URL
```

### 4. Redeploy

```bash
# Commit changes
git add -A
git commit -m "Fix AI/QA mixed content and environment issues"
git push origin prod

# Deploy
defang deploy
```

### 5. Verify Deployment

After deployment:
1. Check browser console for the correct API URL being logged
2. Test the AI/QA functionality
3. Check backend logs: `defang logs --service backend`

## Important Notes

- **NEXT_PUBLIC_API_URL** must be set during the Docker build process for Next.js to embed it correctly
- **OPENAI_API_KEY** is required for the AI/QA features to work
- **BACKEND_CORS_ORIGINS** must match your frontend URL exactly (including https://)
- **COOKIE_DOMAIN** should be set to `.defang.dev` for production to allow cookies across subdomains

## Testing

Once deployed, test the AI/QA by asking questions like:
- "What was my revenue last month?"
- "Show my conversions vs last week"
- "What's my ROAS on Google?"

If you still see errors, check:
1. Browser console for the actual API URL being used
2. Network tab to see the failed requests
3. Backend logs for any errors: `defang logs --service backend --tail`
