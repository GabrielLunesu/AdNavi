# QA Test Results

**Test Run**: Wed Oct  8 16:02:55 CEST 2025
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

## Test 7: How much profit did I make last week?

**Answer**:
> Your profit was $3,536.59 last week.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "profit",
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
  "question": "How much profit did I make last week?",
  "timeframe_description": "last week"
}
```

---

## Test 8: How many leads did I generate this month?

**Answer**:
> You generated 1,964 leads this month.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "leads",
  "time_range": {
    "last_n_days": 30,
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
  "question": "How many leads did I generate this month?",
  "timeframe_description": "this month"
}
```

---

## Test 9: What is my cost per lead this month?

**Answer**:
> Your cost per lead is $10.19 this month.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpl",
  "time_range": {
    "last_n_days": 30,
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
  "question": "What is my cost per lead this month?",
  "timeframe_description": "this month"
}
```

---

## Test 10: Which campaign had the highest ROAS last week?

**Answer**:
> Last week, your top campaign was the "Holiday Sale - Purchases" with an impressive ROAS of 11.58×, which is way above the workspace average of 4.36×. That's a fantastic performance!

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

## Test 11: What's my ROAS for Google campaigns only?

**Answer**:
> You don't have any Google campaigns connected. You're currently only running ads on Other.

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
  "question": "What's my ROAS for Google campaigns only?",
  "timeframe_description": "last month"
}
```

---

## Test 12: Which campaign spent the most yesterday?

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
  "question": "Which campaign spent the most yesterday?",
  "timeframe_description": "yesterday"
}
```

---

## Test 13: List all active campaigns

**Answer**:
> You currently have three active campaigns: Holiday Sale - Purchases, App Install Campaign, and Lead Gen - B2B.

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

## Test 14: Which ad has the highest CTR?

**Answer**:
> Last week, your highest CTR was 1.7%, which is right on par with the workspace average. However, Ad 2 from AdSet 2 for Brand Awareness topped the charts at 2.1%, so there's a bit of room for improvement there.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "ctr",
  "time_range": {
    "last_n_days": 7,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "ad",
  "breakdown": "ad",
  "top_n": 1,
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "Which ad has the highest CTR?",
  "timeframe_description": "last week"
}
```

---

## Test 15: Show me campaigns with ROAS above 4

**Answer**:
> Last month, your overall ROAS was 3.88×, which is right at the workspace average. The standout campaign, though, was the Holiday Sale - Purchases, crushing it at an impressive 11.77×. So, while you didn't hit that 4× mark overall, you've definitely got a top performer to look at!

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
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 10,
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": {
    "min_spend": 0.0,
    "min_clicks": null,
    "min_conversions": 0
  },
  "question": "Show me campaigns with ROAS above 4",
  "timeframe_description": "last month"
}
```

---

## Test 16: Which campaign generated the most leads?

**Answer**:
> Last month, your top campaign for leads was "Lead Gen - B2B," generating 1,964 leads, which is right on par with the workspace average. That means you’re performing well compared to others, so nice job!

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "leads",
  "time_range": {
    "last_n_days": 30,
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
  "question": "Which campaign generated the most leads?",
  "timeframe_description": "last month"
}
```

---

## Test 17: Rank platforms by cost per conversion

**Answer**:
> Last month, your cost per conversion was $5.53, which is right on par with the workspace average—so you're doing just fine. Interestingly, that also makes you the top performer among your platforms, which is a nice spot to be in!

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpa",
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
  "question": "Rank platforms by cost per conversion",
  "timeframe_description": "last month"
}
```

---

## Test 18: give me a breakdown of holiday campaign performance

**Answer**:
> You have four campaigns running: Holiday Sale - Purchases, App Install Campaign, Lead Gen - B2B, and Brand Awareness.

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
    "status": null
  },
  "thresholds": null,
  "question": "give me a breakdown of holiday campaign performance",
  "timeframe_description": null
}
```

---

## Test 19: what is my average order value?

**Answer**:
> Your average order value was $24.30 last week.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "aov",
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
  "question": "what is my average order value?",
  "timeframe_description": "last week"
}
```

---

## Test 20: what is my total revenue this month?

**Answer**:
> Your total revenue this month is $77,580.62.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "revenue",
  "time_range": {
    "last_n_days": 30,
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
  "question": "what is my total revenue this month?",
  "timeframe_description": "this month"
}
```

---

## Test 21: what is my total spend this month?

**Answer**:
> Your total spend this month is $20,006.72.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "spend",
  "time_range": {
    "last_n_days": 30,
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
  "question": "what is my total spend this month?",
  "timeframe_description": "this month"
}
```

---

## Test 22: what is my total clicks this month?

**Answer**:
> Your total clicks this month are 42,351.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "clicks",
  "time_range": {
    "last_n_days": 30,
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
  "question": "what is my total clicks this month?",
  "timeframe_description": "this month"
}
```

---

## Test 23: what is my total impressions this month?

**Answer**:
> Your total impressions this month are 2,431,851.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "impressions",
  "time_range": {
    "last_n_days": 30,
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
  "question": "what is my total impressions this month?",
  "timeframe_description": "this month"
}
```

---

## Test 24: what is my total conversions this month?

**Answer**:
> Your total conversions this month is 3,618.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "conversions",
  "time_range": {
    "last_n_days": 30,
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
  "question": "what is my total conversions this month?",
  "timeframe_description": "this month"
}
```

---

## Test 25: How does this week compare to last week?

**Answer**:
> This week, you had 522 conversions, which is down 43% from 915 last week—definitely a dip. Interestingly, you're right at the workspace average, so it seems like this week’s performance is pretty typical compared to others.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "conversions",
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

## Test 26: Compare Google vs Meta performance

**Answer**:
> Last month, your ROAS for Google was 3.88×, which is right on par with the workspace average. Meta's performance isn't specified here, but it looks like Google is holding steady as a top performer in your group. That's solid!

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

## Test 27: Is my ROAS improving or declining?

**Answer**:
> Your ROAS was 3.88× last month, which is a solid improvement of 46.8% from 2.64× the month before—great job! Plus, you're right at the workspace average, so you're performing really well compared to others.

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

## Test 28: Which campaign had the highest ROAS last week?

**Answer**:
> Last week, your top campaign was the Holiday Sale - Purchases, which had an impressive ROAS of 11.58×. That’s way above the workspace average of 4.36×, so it really stood out!

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

## Test 29: Show me top 5 campaigns by revenue

**Answer**:
> Last week, your total revenue was $12,691.04, which is right on par with the workspace average—so you're doing just fine! The top performer was the "Holiday Sale - Purchases" campaign, bringing in $9,560.16, making it a solid contributor to your overall revenue.

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

## Test 30: List all active campaigns

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

## Test 31: Which adset had the highest cpc last week?

**Answer**:
> Last week, the ad set with the highest CPC was "AdSet 2 - Lead Gen - B2B" at $0.54, which is a bit above the workspace average of $0.47. So, it’s performing at a higher cost compared to the rest, but it’s not too far off from the average.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpc",
  "time_range": {
    "last_n_days": 7,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "adset",
  "breakdown": "adset",
  "top_n": 1,
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "Which adset had the highest cpc last week?",
  "timeframe_description": "last week"
}
```

---

## Test 32: Which adset had the lowest ctr last week?

**Answer**:
> Last week, the ad set with the lowest CTR was at 1.7%, which matches the workspace average, so it’s pretty average overall. Just to give you some context, your top performer, AdSet 1 for the Holiday Sale, had a CTR of 1.9%.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "ctr",
  "time_range": {
    "last_n_days": 7,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "adset",
  "breakdown": "adset",
  "top_n": 1,
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "Which adset had the lowest ctr last week?",
  "timeframe_description": "last week"
}
```

---

## Test 33: Which adset had the highest ctr last week?

**Answer**:
> Last week, the ad set with the highest CTR was "AdSet 1 - Holiday Sale - Purchases" at 1.9%, which is a bit above the workspace average of 1.7%. So, you're right on track with that performance!

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "ctr",
  "time_range": {
    "last_n_days": 7,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "adset",
  "breakdown": "adset",
  "top_n": 1,
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "Which adset had the highest ctr last week?",
  "timeframe_description": "last week"
}
```

---

## Test 34: Which adset had the lowest cpc last week?

**Answer**:
> Your lowest CPC last week was $0.47, which is right on par with the workspace average—so you're doing just fine. For context, the top performer was AdSet 2 at $0.54, but you're still holding your own!

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpc",
  "time_range": {
    "last_n_days": 7,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "adset",
  "breakdown": "adset",
  "top_n": 1,
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "Which adset had the lowest cpc last week?",
  "timeframe_description": "last week"
}
```

---

## Test 35: Which adset had the highest cpc last week?

**Answer**:
> Last week, the ad set with the highest CPC was "AdSet 2 - Lead Gen - B2B" at $0.54, which is a bit above the workspace average of $0.47. So, it looks like that one’s performing at a premium compared to the rest!

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpc",
  "time_range": {
    "last_n_days": 7,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "adset",
  "breakdown": "adset",
  "top_n": 1,
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "Which adset had the highest cpc last week?",
  "timeframe_description": "last week"
}
```

---

## Test 36: Which adset had the lowest ctr last week?

**Answer**:
> Last week, the ad set with the lowest CTR was at 1.7%, which is right on par with the workspace average. For a bit of context, your top performer, AdSet 1 for the Holiday Sale, had a CTR of 1.9%. So, you're doing about average overall!

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "ctr",
  "time_range": {
    "last_n_days": 7,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "adset",
  "breakdown": "adset",
  "top_n": 1,
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "Which adset had the lowest ctr last week?",
  "timeframe_description": "last week"
}
```

---

## Test 37: what is my total CVR last month?

**Answer**:
> Your total CVR was 8.5% last month.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cvr",
  "time_range": {
    "last_n_days": 30,
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
  "question": "what is my total CVR last month?",
  "timeframe_description": "last month"
}
```

---

## Test 38: What's my ROAS for active campaigns?

**Answer**:
> Your ROAS for active campaigns was 3.88× last month, which is right on par with the workspace average—so you're doing just fine. The top performer, the Holiday Sale - Purchases, really crushed it at 11.77×, but overall, you're holding your own!

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
  "timeframe_description": "last month"
}
```

---

## Test 39: How much did I spend on Meta ads?

**Answer**:
> You don't have any Meta campaigns connected. You're currently only running ads on Other.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "spend",
  "time_range": {
    "last_n_days": 30,
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
  "timeframe_description": "last month"
}
```

---

## Test 40: How much revenue on Google last week?

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

## Test 41: What's my cost per install?

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

## Test 42: How many leads did I generate today?

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

## Test 43: wich ad had the lowest cpc last week?

**Answer**:
> Your lowest CPC last week was $0.47, which is right on par with the workspace average. Just to give you some context, the top performer was Ad 1 from AdSet 2 at $0.70, so you’re doing pretty well overall!

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpc",
  "time_range": {
    "last_n_days": 7,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "ad",
  "breakdown": "ad",
  "top_n": 1,
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "wich ad had the lowest cpc last week?",
  "timeframe_description": "last week"
}
```

---

## Test 44: What time on average do i get the best cpc?

**Answer**:
> Last week, your CPC was $0.47, which is right on par with the workspace average—so you're doing just as well as everyone else. It looks like you’ve hit a solid spot, but there’s no standout time that’s better than average for you right now.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpc",
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
  "question": "What time on average do i get the best cpc?",
  "timeframe_description": "last week"
}
```

---

## Test 45: how much revenue would i have last week if my cpc was 0.20?

**Answer**:
> Your revenue was $12,691.04 last week.

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
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "how much revenue would i have last week if my cpc was 0.20?",
  "timeframe_description": "last week"
}
```

---

## Test 46: 

**Answer**:
> Your revenue was $12,691.04 last week.

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
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "",
  "timeframe_description": "last week"
}
```

---

