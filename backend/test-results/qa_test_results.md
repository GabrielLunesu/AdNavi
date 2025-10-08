# QA Test Results

**Test Run**: Wed Oct  8 15:46:52 CEST 2025
**Workspace**: Defang Labs (914019de-2190-4fcc-855a-d1e719d05cdc)
**System Version**: Phase 3 (v2.1.3)

---

## Test 1: What's my CPC today?

**Answer**:
> Your CPC is N/A today.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpc",
  "time_range": {
    "last_n_days": 1,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "What's my CPC today?",
  "timeframe_description": "today"
}
```

---

## Test 2: How much did I spend yesterday?

**Answer**:
> No data available for yesterday yet. Your ad spend last week was available - try asking about a longer timeframe.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "spend",
  "time_range": {
    "last_n_days": 1,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "How much did I spend yesterday?",
  "timeframe_description": "yesterday"
}
```

---

## Test 3: What's my ROAS this week?

**Answer**:
> Your ROAS is 4.36× this week.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "roas",
  "time_range": {
    "last_n_days": 7,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "What's my ROAS this week?",
  "timeframe_description": "this week"
}
```

---

## Test 4: How much revenue did I generate today?

**Answer**:
> No data available for today yet. Your revenue last week was available - try asking about a longer timeframe.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "revenue",
  "time_range": {
    "last_n_days": 1,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "How much revenue did I generate today?",
  "timeframe_description": "today"
}
```

---

## Test 5: What's my conversion rate?

**Answer**:
> Your conversion rate was 8.5% last week.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cvr",
  "time_range": {
    "last_n_days": 7,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "What's my conversion rate?",
  "timeframe_description": "last week"
}
```

---

