# How to View Logs - Hierarchy Rollups & QA Pipeline

**Created**: 2025-10-16  
**Purpose**: Guide for viewing comprehensive logs added to QA system

## Quick Summary

We've added extensive logging throughout the QA pipeline and UnifiedMetricService:
- **QA Pipeline**: Every stage (context, translation, planning, execution, answer)
- **UnifiedMetricService**: Entity resolution, hierarchy rollups, calculations
- **Markers**: `[QA_PIPELINE]`, `[UNIFIED_METRICS]`, `[ENTITY_CATALOG]`

## Viewing Logs Locally

### During Development

Logs appear in the terminal where you start the backend:

```bash
cd backend
python start_api.py

# You'll see logs streaming live:
[INFO]     Started server process [12345]
[INFO]     Waiting for application startup.
[INFO]     Application startup complete.
[INFO]     Uvicorn running on http://127.0.0.1:8000

# When a QA query comes in:
[QA_PIPELINE] ===== Starting QA pipeline =====
[QA_PIPELINE] Question: 'what was the roas on product launch teaser campaign'
[QA_PIPELINE] Workspace ID: 3d70be2f-d8a9-443b-b28d-9e307c2f6183
[QA_PIPELINE] Step 1: Fetching conversation context
[QA_PIPELINE] Context retrieved: 0 previous queries
[ENTITY_CATALOG] Built catalog with 50 entities
[QA_PIPELINE] Step 2: Translating question to DSL
[QA_PIPELINE] Translation complete: {'metric': 'roas', 'filters': {'entity_name': 'Product Launch Teaser'}, ...}
[QA_PIPELINE] Translation latency: 542ms
[QA_PIPELINE] Step 3: Building execution plan
[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 21), end=datetime.date(2025, 10, 21), ...)
[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
[UNIFIED_METRICS] Time range: TimeRange(start=datetime.date(2025, 10, 21), end=datetime.date(2025, 10, 21))
[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Product Launch Teaser
[UNIFIED_METRICS] Resolved dates: 2025-10-21 to 2025-10-21
[UNIFIED_METRICS] Resolving entity name: 'Product Launch Teaser'
[UNIFIED_METRICS] Found entity: Product Launch Teaser (ID: 3032e686-121d-4209-aff6-eaf135cec7fc, Level: campaign)
[UNIFIED_METRICS] Using campaign hierarchy CTE
[UNIFIED_METRICS] Found 12 descendants for Product Launch Teaser
[UNIFIED_METRICS] Excluded parent entity 3032e686-121d-4209-aff6-eaf135cec7fc from descendants
[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
[UNIFIED_METRICS] Using hierarchy rollup for 'Product Launch Teaser': 12 descendants
[UNIFIED_METRICS] Current period totals: {'spend': 465.38, 'revenue': 599.84, 'clicks': 0, 'impressions': 0, 'conversions': 0, 'leads': 0, 'installs': 0, 'purchases': 0, 'visitors': 0, 'profit': 0}
[UNIFIED_METRICS] Calculated metrics: {'roas': 1.288925179423267}
[UNIFIED_METRICS] Workspace average: 1.2735562908689829
[QA_PIPELINE] Step 4: Executing plan
[QA_PIPELINE] Execution complete: MetricResult(summary=1.288925179423267, ...)
[QA_PIPELINE] Step 5: Building answer
[QA_PIPELINE] Answer generated successfully
[QA_PIPELINE] Answer: 'The ROAS for the Product Launch Teaser campaign was 1.29× on October 21, 2025.'
[QA_PIPELINE] Answer generation latency: 234ms
[QA_PIPELINE] Step 6: Saving to conversation context
[QA_PIPELINE] Step 7: Logging telemetry
[QA_PIPELINE] ===== Pipeline complete =====
[QA_PIPELINE] Total latency: 1256ms
[QA_PIPELINE] Final answer: 'The ROAS for the Product Launch Teaser campaign was 1.29× on October 21, 2025.'
```

### Redirect Logs to File

```bash
# Start backend and save logs to file
cd backend
python start_api.py 2>&1 | tee qa_logs.txt

# In another terminal, tail the logs
tail -f qa_logs.txt

# Filter for specific markers
tail -f qa_logs.txt | grep "\[QA_PIPELINE\]"
tail -f qa_logs.txt | grep "\[UNIFIED_METRICS\]"
```

### Filter Logs

```bash
# Show only QA pipeline logs
grep "\[QA_PIPELINE\]" qa_logs.txt

# Show only UnifiedMetricService logs
grep "\[UNIFIED_METRICS\]" qa_logs.txt

# Show hierarchy rollup logs
grep "hierarchy\|descendants\|parent" qa_logs.txt

# Show all new logging
grep -E "\[QA_PIPELINE\]|\[UNIFIED_METRICS\]|\[ENTITY_CATALOG\]" qa_logs.txt
```

## Viewing Logs on Railway

### Get Logs from Railway

```bash
# Show live logs (follow mode)
railway logs

# Show last 100 lines
railway logs --tail 100

# Show logs for specific service
railway logs --service backend

# Filter logs
railway logs | grep "\[QA_PIPELINE\]"
railway logs | grep "\[UNIFIED_METRICS\]"
```

### Railway Web Dashboard

1. Go to https://railway.app
2. Select your project
3. Click on the backend service
4. Click "Deployments" → select latest deployment
5. View logs in the "Logs" tab

### Query Logs from Database

```bash
# Get recent QA logs
railway run psql -c "
SELECT 
  question_text,
  created_at,
  duration_ms,
  (dsl_json->>'metric') as metric,
  (dsl_json->'filters'->>'entity_name') as entity_name,
  answer_text
FROM qa_query_logs
ORDER BY created_at DESC
LIMIT 10;
"
```

## Log Markers Reference

### `[QA_PIPELINE]` - QA Service Pipeline

**When**: Every stage of the QA pipeline

**What it logs**:
- Question being processed
- Workspace ID and User ID
- Context retrieval
- Translation completion and latency
- Plan building
- Execution results
- Answer generation
- Final answer and total latency

**Example**:
```
[QA_PIPELINE] ===== Starting QA pipeline =====
[QA_PIPELINE] Question: 'what was the roas on product launch teaser campaign'
[QA_PIPELINE] Workspace ID: 3d70be2f-d8a9-443b-b28d-9e307c2f6183
[QA_PIPELINE] Step 1: Fetching conversation context
[QA_PIPELINE] Step 2: Translating question to DSL
[QA_PIPELINE] Translation complete: {...}
[QA_PIPELINE] ===== Pipeline complete =====
```

### `[UNIFIED_METRICS]` - UnifiedMetricService

**When**: All metric calculation operations

**What it logs**:
- Input metrics and filters
- Time range resolution
- Entity name resolution (if entity_name filter)
- Hierarchy CTE usage
- Descendant discovery
- Parent exclusion
- Aggregation calculations
- Final metric values

**Example**:
```
[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Product Launch Teaser
[UNIFIED_METRICS] Resolving entity name: 'Product Launch Teaser'
[UNIFIED_METRICS] Found entity: Product Launch Teaser (ID: xxx, Level: campaign)
[UNIFIED_METRICS] Using campaign hierarchy CTE
[UNIFIED_METRICS] Found 12 descendants for Product Launch Teaser
[UNIFIED_METRICS] Excluded parent entity xxx from descendants
[UNIFIED_METRICS] Current period totals: {'revenue': 599.84, 'spend': 465.38}
[UNIFIED_METRICS] Calculated metrics: {'roas': 1.288925179423267}
```

### `[ENTITY_CATALOG]` - Entity Catalog Building

**When**: Building entity catalog for LLM entity recognition

**What it logs**:
- Number of entities in catalog
- Entities being considered for recognition

**Example**:
```
[ENTITY_CATALOG] Built catalog with 50 entities
```

## Interpreting Logs

### ✅ Success Indicators

1. **Hierarchy Rollup Happening**:
   ```
   [UNIFIED_METRICS] Using campaign hierarchy CTE
   [UNIFIED_METRICS] Found 12 descendants for Product Launch Teaser
   [UNIFIED_METRICS] Excluded parent entity xxx from descendants
   ```

2. **Fresh Data Being Used**:
   ```
   [UNIFIED_METRICS] Current period totals: {'revenue': 599.84, 'spend': 465.38}
   ```
   Revenue = $599.84 (descendants only, NOT $646.61 which includes stale campaign fact)

3. **Correct ROAS Calculation**:
   ```
   [UNIFIED_METRICS] Calculated metrics: {'roas': 1.288925179423267}
   ```
   ROAS = 1.29× (599.84 / 465.38)

### ❌ Warning Signs

1. **No Hierarchy Rollup**:
   ```
   [UNIFIED_METRICS] No workspace_id provided for entity_name filter, using simple match
   ```
   This means hierarchy rollup didn't happen - check filter application

2. **Stale Data Being Used**:
   ```
   [UNIFIED_METRICS] Current period totals: {'revenue': 646.61, ...}
   ```
   Revenue = $646.61 includes stale campaign fact - hierarchy rollup failed

3. **No Descendants Found**:
   ```
   [UNIFIED_METRICS] Found 0 descendants for Product Launch Teaser
   ```
   Check database for correct parent_id relationships

## Debugging Checklist

When debugging data mismatches:

1. ✅ Check if entity_name filter is being used
2. ✅ Verify hierarchy CTE is being invoked
3. ✅ Confirm descendants are being found
4. ✅ Verify parent entity is excluded
5. ✅ Check aggregation calculations
6. ✅ Verify final ROAS value matches expected

## Log Level Configuration

### Development (Verbose)

```python
# In backend/app/__init__.py or start_api.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Production (Selective)

```python
# Only log INFO and above
logging.basicConfig(level=logging.INFO)

# Suppress DEBUG logs from dependencies
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
logging.getLogger("uvicorn").setLevel(logging.INFO)
```

## Example: Complete Query Trace

Here's what a complete successful query trace looks like:

```
2025-10-16 12:41:55 INFO [QA_PIPELINE] ===== Starting QA pipeline =====
2025-10-16 12:41:55 INFO [QA_PIPELINE] Question: 'what was the roas on product launch teaser campaign on october 21 2025'
2025-10-16 12:41:55 INFO [QA_PIPELINE] Workspace ID: 3d70be2f-d8a9-443b-b28d-9e307c2f6183
2025-10-16 12:41:55 INFO [QA_PIPELINE] User ID: 783c67e3-b1ef-4afa-b2be-7a14b02a04da
2025-10-16 12:41:55 INFO [QA_PIPELINE] Step 1: Fetching conversation context
2025-10-16 12:41:55 INFO [QA_PIPELINE] Context retrieved: 0 previous queries
2025-10-16 12:41:55 INFO [ENTITY_CATALOG] Built catalog with 50 entities
2025-10-16 12:41:55 INFO [QA_PIPELINE] Step 2: Translating question to DSL
2025-10-16 12:41:56 INFO [QA_PIPELINE] Translation complete: {'query_type': 'metrics', 'metric': 'roas', 'filters': {'entity_name': 'Product Launch Teaser'}, ...}
2025-10-16 12:41:56 INFO [QA_PIPELINE] Translation latency: 542ms
2025-10-16 12:41:56 INFO [QA_PIPELINE] Step 3: Building execution plan
2025-10-16 12:41:56 INFO [QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 21), end=datetime.date(2025, 10, 21), ...)
2025-10-16 12:41:56 INFO [QA_PIPELINE] Step 4: Executing plan
2025-10-16 12:41:56 INFO [UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
2025-10-16 12:41:56 INFO [UNIFIED_METRICS] Time range: TimeRange(start=datetime.date(2025, 10, 21), end=datetime.date(2025, 10, 21))
2025-10-16 12:41:56 INFO [UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Product Launch Teaser
2025-10-16 12:41:56 INFO [UNIFIED_METRICS] Resolved dates: 2025-10-21 to 2025-10-21
2025-10-16 12:41:56 INFO [UNIFIED_METRICS] Resolving entity name: 'Product Launch Teaser'
2025-10-16 12:41:56 INFO [UNIFIED_METRICS] Found entity: Product Launch Teaser (ID: 3032e686-121d-4209-aff6-eaf135cec7fc, Level: campaign)
2025-10-16 12:41:56 INFO [UNIFIED_METRICS] Using campaign hierarchy CTE
2025-10-16 12:41:56 INFO [UNIFIED_METRICS] Found 12 descendants for Product Launch Teaser
2025-10-16 12:41:56 INFO [UNIFIED_METRICS] Excluded parent entity 3032e686-121d-4209-aff6-eaf135cec7fc from descendants
2025-10-16 12:41:56 INFO [UNIFIED_METRICS] Returning 12 descendant IDs for rollup
2025-10-16 12:41:56 INFO [UNIFIED_METRICS] Using hierarchy rollup for 'Product Launch Teaser': 12 descendants
2025-10-16 12:41:56 INFO [UNIFIED_METRICS] Current period totals: {'spend': 465.38, 'revenue': 599.84, ...}
2025-10-16 12:41:56 INFO [UNIFIED_METRICS] Calculated metrics: {'roas': 1.288925179423267}
2025-10-16 12:41:56 INFO [UNIFIED_METRICS] Workspace average: 1.2735562908689829
2025-10-16 12:41:56 INFO [QA_PIPELINE] Execution complete: MetricResult(summary=1.288925179423267, ...)
2025-10-16 12:41:56 INFO [QA_PIPELINE] Step 5: Building answer
2025-10-16 12:41:57 INFO [QA_PIPELINE] Answer generated successfully
2025-10-16 12:41:57 INFO [QA_PIPELINE] Answer: 'The ROAS for the Product Launch Teaser campaign was 1.29× on October 21, 2025.'
2025-10-16 12:41:57 INFO [QA_PIPELINE] Answer generation latency: 234ms
2025-10-16 12:41:57 INFO [QA_PIPELINE] Step 6: Saving to conversation context
2025-10-16 12:41:57 INFO [QA_PIPELINE] Step 7: Logging telemetry
2025-10-16 12:41:57 INFO [QA_PIPELINE] ===== Pipeline complete =====
2025-10-16 12:41:57 INFO [QA_PIPELINE] Total latency: 1256ms
2025-10-16 12:41:57 INFO [QA_PIPELINE] Final answer: 'The ROAS for the Product Launch Teaser campaign was 1.29× on October 21, 2025.'
```

## Testing Commands

### Test QA Endpoint

```bash
# Login first
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "owner@defanglabs.com", "password": "password123"}' \
  -c cookies.txt

# Query campaign ROAS
curl -X POST "http://localhost:8000/qa/?workspace_id=3d70be2f-d8a9-443b-b28d-9e307c2f6183" \
  -H "Content-Type: application/json" \
  -b cookies.txt \
  -d '{"question": "what was the roas on product launch teaser campaign on october 21 2025"}' \
  | jq '.answer'

# Expected: "The ROAS for the Product Launch Teaser campaign was 1.29× on October 21, 2025."
```

### Monitor Logs While Testing

```bash
# Terminal 1: Start backend with logging
cd backend
python start_api.py 2>&1 | tee qa_logs.txt

# Terminal 2: Watch logs live
tail -f qa_logs.txt | grep -E "\[QA_PIPELINE\]|\[UNIFIED_METRICS\]"

# Terminal 3: Run queries
curl -X POST "http://localhost:8000/qa/?workspace_id=..." ...
```

## Next Steps

1. ✅ View logs locally during development
2. ✅ View logs on Railway in production
3. ✅ Test QA endpoint with curl
4. ✅ Verify hierarchy rollups are working
5. ⏳ Complete remaining UI fixes
6. ⏳ Add entity_name filter to KPI endpoint

