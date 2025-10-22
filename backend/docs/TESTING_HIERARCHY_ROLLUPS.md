# Testing Hierarchy Rollups & Logging

**Date**: 2025-10-16  
**Status**: Ready for Testing

## Overview

This guide shows how to test the new hierarchy rollup functionality and view comprehensive logs.

## Prerequisites

1. Backend running locally or on Railway
2. Database seeded with test data
3. Login credentials: `owner@defanglabs.com` / `password123`

## Testing Steps

### 1. Login and Get Auth Token

```bash
# Login
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "owner@defanglabs.com",
    "password": "password123"
  }' \
  -c cookies.txt -v

# Response will include Set-Cookie header with access_token
```

### 2. Get Workspace ID

```bash
# Get current user (includes workspace_id)
curl -X GET http://localhost:8000/auth/me \
  -b cookies.txt

# Or list workspaces
curl -X GET http://localhost:8000/workspaces \
  -b cookies.txt
```

### 3. Test QA Endpoint with Campaign Query

```bash
# Query campaign ROAS (this should trigger hierarchy rollup)
curl -X POST "http://localhost:8000/qa?workspace_id=YOUR_WORKSPACE_ID" \
  -H "Content-Type: application/json" \
  -b cookies.txt \
  -d '{
    "question": "what was the roas on product launch teaser campaign on october 21 2025"
  }' | jq .
```

**Expected Response**:
```json
{
  "answer": "The ROAS on the Product Launch Teaser campaign was 1.29× on October 21, 2025.",
  "executed_dsl": {
    "query_type": "metrics",
    "metric": "roas",
    "entity_name": "Product Launch Teaser",
    ...
  },
  "data": {
    "summary": 1.288925179423267,
    ...
  }
}
```

### 4. Test QA Endpoint with Revenue Query

```bash
curl -X POST "http://localhost:8000/qa?workspace_id=YOUR_WORKSPACE_ID" \
  -H "Content-Type: application/json" \
  -b cookies.txt \
  -d '{
    "question": "how much revenue did product launch teaser campaign make on october 21"
  }' | jq .
```

**Expected**: Revenue = $599.84 (from descendants only, not $646.61)

## Viewing Logs

### Local Development

Logs appear in the terminal where the backend is running:

```bash
# Start backend with Python logging
cd backend
python start_api.py

# You'll see logs like:
[QA_PIPELINE] ===== Starting QA pipeline =====
[QA_PIPELINE] Question: 'what was the roas on product launch teaser campaign'
[UNIFIED_METRICS] Resolving entity name: 'Product Launch Teaser'
[UNIFIED_METRICS] Found entity: Product Launch Teaser (ID: xxx, Level: campaign)
[UNIFIED_METRICS] Using campaign hierarchy CTE
[UNIFIED_METRICS] Found 12 descendants for Product Launch Teaser
[UNIFIED_METRICS] Excluded parent entity xxx from descendants
[UNIFIED_METRICS] Current period totals: {'revenue': 599.84, 'spend': 465.38}
[UNIFIED_METRICS] Calculated metrics: {'roas': 1.288925179423267}
```

### Filter Logs

```bash
# Filter QA pipeline logs
grep "[QA_PIPELINE]" logs.txt

# Filter UnifiedMetricService logs
grep "[UNIFIED_METRICS]" logs.txt

# Filter all new logging
grep -E "\[QA_PIPELINE\]|\[UNIFIED_METRICS\]|\[ENTITY_CATALOG\]" logs.txt
```

### Railway Production

```bash
# Get logs from Railway
railway logs

# Filter for QA pipeline
railway logs | grep "\[QA_PIPELINE\]"

# Filter for UnifiedMetricService
railway logs | grep "\[UNIFIED_METRICS\]"

# Show last 100 lines
railway logs --tail 100
```

### Database Logs (Telemetry)

```bash
# Query QA logs from database
railway run psql -c "
SELECT 
  question_text,
  created_at,
  duration_ms,
  (dsl_json->>'metric') as metric,
  (dsl_json->>'entity_name') as entity_name
FROM qa_query_logs
ORDER BY created_at DESC
LIMIT 10;
"
```

## What to Look For in Logs

### ✅ Success Indicators

1. **Entity Resolution**:
   ```
   [UNIFIED_METRICS] Found entity: Product Launch Teaser (ID: xxx, Level: campaign)
   ```

2. **Hierarchy CTE Usage**:
   ```
   [UNIFIED_METRICS] Using campaign hierarchy CTE
   [UNIFIED_METRICS] Found 12 descendants for Product Launch Teaser
   ```

3. **Parent Exclusion**:
   ```
   [UNIFIED_METRICS] Excluded parent entity xxx from descendants
   ```

4. **Fresh Data**:
   ```
   [UNIFIED_METRICS] Current period totals: {'revenue': 599.84, 'spend': 465.38}
   ```
   Revenue should be ~$599.84 (not $646.61 which includes stale campaign fact)

### ❌ Warning Signs

1. **No Hierarchy CTE**:
   ```
   [UNIFIED_METRICS] No workspace_id provided for entity_name filter, using simple match
   ```
   This means hierarchy rollup didn't happen

2. **Stale Data**:
   ```
   Current period totals: {'revenue': 646.61, ...}
   ```
   This includes campaign fact - hierarchy rollup not working

3. **Translation Errors**:
   ```
   [QA_PIPELINE] Translation error: ...
   ```

## Expected Results

### Before Hierarchy Rollups:
- Campaign fact: $46.77 revenue
- Children aggregate: $599.84 revenue
- **Total**: $646.61 revenue
- **ROAS**: 1.27×

### After Hierarchy Rollups:
- **Only descendants**: $599.84 revenue
- **Spend**: $465.38
- **ROAS**: 1.29×

### Key Difference:
- Old: Included stale campaign fact ($46.77)
- New: Only fresh descendant data ($599.84)

## Troubleshooting

### Issue: Logs show "simple match" instead of hierarchy CTE

**Solution**: Check that `workspace_id` is being passed to `_apply_filters()`

### Issue: ROAS still includes campaign fact

**Solution**: Check that descendant resolution is working:
```bash
# Test descendant resolution
PGPASSWORD=cOPAfFeXOYobFVnVUKXXYAVoETzYCZwX psql -h trolley.proxy.rlwy.net -p 31092 -U postgres -d railway -c "
SELECT COUNT(*) FROM entities WHERE parent_id IN (
  SELECT id FROM entities WHERE name = 'Product Launch Teaser'
);
"
```

### Issue: No logs appearing

**Solution**: Check log level configuration:
```python
# In backend/app/__init__.py or start_api.py
logging.basicConfig(level=logging.INFO)
```

## Next Steps

1. Complete remaining fixes (UI mock data removal)
2. Add entity_name filter to KPI endpoint
3. Monitor logs in production
4. Update metrics if needed

