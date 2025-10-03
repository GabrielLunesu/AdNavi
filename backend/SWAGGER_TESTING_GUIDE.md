# Swagger UI Testing Guide: Context-Aware QA Endpoint

## Overview

The `/qa` endpoint now includes **context visibility** in responses, making it easy to test and debug follow-up questions directly in Swagger UI.

---

## What You'll See

Every QA response now includes a `context_used` field showing what conversation history was available:

```json
{
  "answer": "Your REVENUE for the selected period is $58,300.90.",
  "executed_dsl": {
    "metric": "revenue",
    "time_range": {"last_n_days": 7}
  },
  "data": {
    "summary": 58300.9
  },
  "context_used": [
    {
      "question": "how much revenue this week?",
      "query_type": "metrics",
      "metric": "revenue",
      "time_period": "last_7_days"
    }
  ]
}
```

---

## Testing Follow-Up Questions in Swagger UI

### Step 1: Open Swagger UI
Navigate to: `http://localhost:8000/docs`

### Step 2: Authenticate
1. Click **Authorize** button (top right)
2. Login with test credentials:
   - Email: `owner@defanglabs.com`
   - Password: `password123`

### Step 3: Test Conversation Flow

#### **Request 1: Initial Question**

**Endpoint:** `POST /qa`

**Parameters:**
- `workspace_id`: `cfdf6838-3a29-40b3-8e1a-bc3c4e1b585f` (from seed data)

**Body:**
```json
{
  "question": "how much revenue this week?"
}
```

**Expected Response:**
```json
{
  "answer": "Your REVENUE for the selected period is $58,300.90.",
  "executed_dsl": {
    "metric": "revenue",
    ...
  },
  "context_used": []  // ← Empty! This is the first question
}
```

✅ **Verify:** `context_used` is an empty array (no prior context)

---

#### **Request 2: Follow-Up Question**

**Endpoint:** `POST /qa` (same endpoint, immediately after Request 1)

**Parameters:**
- `workspace_id`: `cfdf6838-3a29-40b3-8e1a-bc3c4e1b585f` (same)

**Body:**
```json
{
  "question": "and the week before?"
}
```

**Expected Response:**
```json
{
  "answer": "Your REVENUE for the selected period is $145,890.26.",
  "executed_dsl": {
    "metric": "revenue",  // ← Should inherit "revenue" from context!
    ...
  },
  "context_used": [  // ← Now has context!
    {
      "question": "how much revenue this week?",
      "metric": "revenue",
      "time_period": "last_7_days"
    }
  ]
}
```

✅ **Verify:** 
- `executed_dsl.metric` is **"revenue"** (inherited correctly!)
- `context_used` shows the previous question with **metric: "revenue"**

---

## Debug Checklist

Use `context_used` to verify:

| What to Check | Where to Look | Expected |
|---------------|---------------|----------|
| **Context available?** | `context_used` array | Non-empty for follow-ups |
| **Metric inherited?** | `executed_dsl.metric` matches `context_used[0].metric` | Same value |
| **Time period changed?** | Compare `time_period` in context vs current query | Different if user asked "yesterday", "week before", etc. |
| **Query type correct?** | `executed_dsl.query_type` | "metrics", "providers", or "entities" |

---

## Common Test Scenarios

### Scenario 1: Metric Inheritance

```
Q1: "how many conversions this week?"
→ context_used: []
→ executed_dsl.metric: "conversions" ✅

Q2: "and yesterday?"
→ context_used: [{metric: "conversions"}]
→ executed_dsl.metric: "conversions" ✅ (inherited!)
```

### Scenario 2: Metric Switching (Bug Detection)

```
Q1: "how much revenue this week?"
→ context_used: []
→ executed_dsl.metric: "revenue" ✅

Q2: "and the week before?"
→ context_used: [{metric: "revenue"}]
→ executed_dsl.metric: "conversions" ❌ BUG! Should be "revenue"
```

If you see this ↑ **metric switching incorrectly**, it's a bug in context inheritance!

### Scenario 3: Entity References

```
Q1: "which campaigns are live?"
→ context_used: []
→ query_type: "entities" ✅

Q2: "which one performed best?"
→ context_used: [{question: "which campaigns are live?", query_type: "entities"}]
→ Should generate a query to find top performer ✅
```

---

## What Context Shows

The `context_used` field includes:

| Field | Description | Example |
|-------|-------------|---------|
| `question` | Previous question text | "how much revenue this week?" |
| `query_type` | Type of query | "metrics", "providers", "entities" |
| `metric` | Metric used (if metrics query) | "revenue", "conversions", "roas" |
| `time_period` | Time range shorthand | "last_7_days", "last_30_days" |

**Note:** Full result data is **not** included to keep responses concise.

---

## Troubleshooting

### Problem: `context_used` is always empty

**Possible causes:**
1. Testing with different `workspace_id` values (context is workspace-scoped)
2. Backend was restarted (in-memory context is lost)
3. Testing as different user (context is user-scoped)

**Solution:** Use the same `workspace_id` and stay logged in as same user for entire test session.

### Problem: Metric not inheriting correctly

**Debug steps:**
1. Check `context_used` - is previous metric visible?
2. Check `executed_dsl.metric` - does it match context?
3. If mismatch → check system prompt and translator logic

---

## Benefits of Context Visibility

✅ **Transparency**: See exactly what the LLM received  
✅ **Debugging**: Understand why follow-ups work or fail  
✅ **Validation**: Verify metric inheritance is correct  
✅ **Testing**: Easy to test in Swagger UI  
✅ **Confidence**: Know the context system is working  

---

## Advanced: Multi-Turn Conversations

Context stores up to **5 previous queries** (configurable in `app/state.py`):

```
Q1: "revenue this week?"     → context: []
Q2: "and yesterday?"          → context: [Q1]
Q3: "and last month?"         → context: [Q1, Q2]
Q4: "which campaigns?"        → context: [Q1, Q2, Q3]
Q5: "and for Google?"         → context: [Q1, Q2, Q3, Q4]
Q6: "yesterday?"              → context: [Q2, Q3, Q4, Q5]  (Q1 evicted, FIFO)
```

Each response shows **all** available context at the time of that request.

---

## Production Considerations

### Should we keep `context_used` in production?

**Pros:**
- Helps debug customer issues
- Increases trust (transparency)
- Useful for logs/analytics

**Cons:**
- Slightly larger response payload
- Exposes internal query structure

**Recommendation:** 
- ✅ **Keep it!** The benefits outweigh the costs
- Optional: Add `?debug=false` query param to hide it for production clients

---

## Summary

The `context_used` field makes the conversation context system:
- **Visible**: See what context was available
- **Testable**: Verify in Swagger UI
- **Debuggable**: Understand follow-up behavior
- **Transparent**: No black box magic

**Go test it now in Swagger UI!** → `http://localhost:8000/docs`

