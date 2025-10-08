# QA Test Results

**Test Run**: Wed Oct  8 15:29:48 CEST 2025
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

## Test 6: How many clicks did I get last week?

**Answer**:
> You had 6,156 clicks last week.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "clicks",
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
  "question": "How many clicks did I get last week?",
  "timeframe_description": "last week"
}
```

---

## Test 7: How does this week compare to last week?

**Answer**:
> This week, you had 6,156 clicks, which is a decline of about 43.9% compared to last week's 10,974 clicks. Interestingly, you're right at the workspace average, so it seems like it's been a pretty average week overall.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "clicks",
  "time_range": {
    "last_n_days": 7,
    "start": null,
    "end": null
  },
  "compare_to_previous": true,
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
  "question": "How does this week compare to last week?",
  "timeframe_description": "this week"
}
```

---

## Test 8: Compare Google vs Meta performance

**Answer**:
> Last month, your ROAS for Google was 3.88×, which is right on par with the workspace average. Meta's performance didn’t quite match up, as it fell behind at a lower ROAS. So, Google’s doing well, staying consistent with the top performers!

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "roas",
  "time_range": {
    "last_n_days": 30,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "provider",
  "breakdown": "provider",
  "top_n": 10,
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "Compare Google vs Meta performance",
  "timeframe_description": "last month"
}
```

---

## Test 9: Is my ROAS improving or declining?

**Answer**:
> Your ROAS was 3.88× last month, which is a solid improvement of 46.8% from 2.64× the month before—that's great to see! Plus, you're right on par with the workspace average, so you're performing well compared to others.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "roas",
  "time_range": {
    "last_n_days": 30,
    "start": null,
    "end": null
  },
  "compare_to_previous": true,
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
  "question": "Is my ROAS improving or declining?",
  "timeframe_description": "last month"
}
```

---

## Test 10: Which campaign had the highest ROAS last week?

**Answer**:
> Last week, the "Holiday Sale - Purchases" campaign had the highest ROAS at an impressive 11.58×, which is way above the workspace average of 4.36×. That’s a standout performance!

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
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 1,
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "Which campaign had the highest ROAS last week?",
  "timeframe_description": "last week"
}
```

---

## Test 11: Show me top 5 campaigns by revenue

**Answer**:
> Last week, your total revenue was $12,691.04, which is right on par with the workspace average—so that's solid! The top performer was the "Holiday Sale - Purchases" campaign, bringing in $9,560.16. Overall, you’re doing just as well as others in your workspace!

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "revenue",
  "time_range": {
    "last_n_days": 7,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 5,
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "Show me top 5 campaigns by revenue",
  "timeframe_description": "last week"
}
```

---

## Test 12: List all active campaigns

**Answer**:
> You have three active campaigns: Holiday Sale - Purchases, App Install Campaign, and Lead Gen - B2B.

**DSL**:
```json
{
  "query_type": "entities",
  "metric": null,
  "time_range": null,
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 10,
  "filters": {
    "provider": null,
    "level": "campaign",
    "entity_ids": null,
    "status": "active"
  },
  "thresholds": null,
  "question": "List all active campaigns",
  "timeframe_description": null
}
```

---

## Test 13: Why is my ROAS volatile?

**Answer**:
> Your ROAS is currently at 4.36×, which is stable and aligns perfectly with your workspace average of 4.36×. However, the volatility in your ROAS, ranging from a low of 2.09× to a peak of 5.59× over the past week, indicates fluctuating performance that may be driven by varying campaign effectiveness or external factors. Notably, the significant drop to 2.09× on October 3 suggests an anomaly that could be worth investigating further. To enhance consistency, consider analyzing the campaigns that contributed to these fluctuations.

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
  "question": "Why is my ROAS volatile?",
  "timeframe_description": "last week"
}
```

---

## Test 14: Explain my spend trend

**Answer**:
> Your spend is currently at $2,913.81, which is consistent with your workspace average of $2,913.81, indicating a stable performance level. However, the trend has been quite volatile, starting at $793.56 and peaking at $897.14 before dropping to $730.56 recently. This fluctuation, with a volatility rate of 20.4%, suggests that while your overall spend aligns with the average, there may be opportunities to optimize your budget allocation to reduce these swings.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "spend",
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
  "question": "Explain my spend trend",
  "timeframe_description": "last week"
}
```

---

## Test 15: What's my ROAS for active campaigns?

**Answer**:
> Your ROAS for active campaigns was 4.36× last week, which is right on par with the workspace average—nice consistency! Just so you know, your top performer, the Holiday Sale - Purchases, hit an impressive 11.58×.

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
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 10,
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": "active"
  },
  "thresholds": null,
  "question": "What's my ROAS for active campaigns?",
  "timeframe_description": "last week"
}
```

---

## Test 16: How much did I spend on Meta ads?

**Answer**:
> You don't have any Meta campaigns connected. You're currently only running ads on Other.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "spend",
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
    "provider": "meta",
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "How much did I spend on Meta ads?",
  "timeframe_description": "last week"
}
```

---

## Test 17: How much revenue on Google last week?

**Answer**:
> You don't have any Google campaigns connected. You're currently only running ads on Other.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "revenue",
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
    "provider": "google",
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "How much revenue on Google last week?",
  "timeframe_description": "last week"
}
```

---

## Test 18: What's my cost per install?

**Answer**:
> Your cost per install was $22.59 last week.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpi",
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
  "question": "What's my cost per install?",
  "timeframe_description": "last week"
}
```

---

## Test 19: How many leads did I generate today?

**Answer**:
> No data available for today yet. Your leads last week was available - try asking about a longer timeframe.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "leads",
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
  "question": "How many leads did I generate today?",
  "timeframe_description": "today"
}
```

---

