# QA Test Results

**Test Run**: Mon Oct 13 13:55:33 CEST 2025
**Workspace**: Defang Labs (9c76b246-faf1-42d6-9a5a-f564f7801b4e)
**System Version**: Phase 5 (v2.1.3)

---

## Test 1: What's my CPC this month?

**Answer**:
> Your CPC is $0.45 this month.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpc",
  "time_range": {
    "last_n_days": 30,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "What's my CPC this month?",
  "timeframe_description": "this month"
}
```

---

## Test 2: How much did I spend this month?

**Answer**:
> You spent $275,259.45 this month.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "How much did I spend this month?",
  "timeframe_description": "this month"
}
```

---

## Test 3: What's my ROAS this week?

**Answer**:
> Your ROAS is 6.15× this week.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "What's my ROAS this week?",
  "timeframe_description": "this week"
}
```

---

## Test 4: How much revenue did I generate yesterday?

**Answer**:
> Your revenue was $0.00 yesterday.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "How much revenue did I generate yesterday?",
  "timeframe_description": "yesterday"
}
```

---

## Test 5: What's my conversion rate?

**Answer**:
> Your conversion rate was 8.4% last week.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "What's my conversion rate?",
  "timeframe_description": "last week"
}
```

---

## Test 6: How many clicks did I get last week?

**Answer**:
> You had 127,137 clicks last week.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "How many clicks did I get last week?",
  "timeframe_description": "last week"
}
```

---

## Test 7: How much profit did I make last week?

**Answer**:
> Your profit was $106,650.18 last week.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "How much profit did I make last week?",
  "timeframe_description": "last week"
}
```

---

## Test 8: How many leads did I generate this month?

**Answer**:
> You generated 19,964 leads this month.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "How many leads did I generate this month?",
  "timeframe_description": "this month"
}
```

---

## Test 9: What is my cost per lead this month?

**Answer**:
> Your cost per lead this month is $13.79.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "What is my cost per lead this month?",
  "timeframe_description": "this month"
}
```

---

## Test 10: Which campaign had the highest ROAS last week?

**Answer**:
> The Holiday Sale - Purchases had the highest ROAS last week at an impressive 13.36×—your top performer! For context, your overall ROAS was 6.15×, which matches the workspace average, so that’s a solid result overall.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "Which campaign had the highest ROAS last week?",
  "timeframe_description": "last week"
}
```

---

## Test 11: What's my ROAS for Google campaigns only?

**Answer**:
> Your ROAS for Google campaigns was 6.15× last week.

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
  "sort_order": "desc",
  "filters": {
    "provider": "google",
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "What's my ROAS for Google campaigns only?",
  "timeframe_description": "last week"
}
```

---

## Test 12: Which campaign spent the most yesterday?

**Answer**:
> It looks like no campaigns spent anything yesterday, so there wasn't a top spender. That's pretty average compared to what you usually see, but it might be worth checking in on your budget settings.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "Which campaign spent the most yesterday?",
  "timeframe_description": "yesterday"
}
```

---

## Test 13: List all active campaigns

**Answer**:
> You have 10 active campaigns, including the Holiday Sale - Purchases, Summer Sale Campaign, and Black Friday Deals, among others.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": "campaign",
    "entity_ids": null,
    "status": "active",
    "entity_name": null
  },
  "thresholds": null,
  "question": "List all active campaigns",
  "timeframe_description": null
}
```

---

## Test 14: Which ad has the highest CTR?

**Answer**:
> The Video Ad - Morning Audience - Lead Gen - B2B had the highest CTR at 4.2% last week—your top performer! For context, your overall CTR was 2.6%, which is right at the average for your workspace.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "Which ad has the highest CTR?",
  "timeframe_description": "last week"
}
```

---

## Test 15: Show me campaigns with ROAS above 4

**Answer**:
> You have a total of 10 campaigns, including the Holiday Sale - Purchases, Summer Sale Campaign, Black Friday Deals, and others like the App Install Campaign and Brand Awareness.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": "campaign",
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": {
    "min_spend": null,
    "min_clicks": null,
    "min_conversions": null
  },
  "question": "Show me campaigns with ROAS above 4",
  "timeframe_description": null
}
```

---

## Test 16: Which campaign generated the most leads?

**Answer**:
> The Lead Gen - B2B campaign generated the most leads last week with 2,704—your top performer! For context, your overall leads were 4,288, which is right at the workspace average.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "leads",
  "time_range": {
    "last_n_days": 7,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 1,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "Which campaign generated the most leads?",
  "timeframe_description": "last week"
}
```

---

## Test 17: Rank platforms by cost per conversion

**Answer**:
> Google had the lowest cost per conversion at $4.37 last week, making it your top performer. In comparison, your overall CPA was $5.43, which is right at the workspace average. So, it looks like Google is doing a bit better than the rest!

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpa",
  "time_range": {
    "last_n_days": 7,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "provider",
  "breakdown": "provider",
  "top_n": 10,
  "sort_order": "asc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "Rank platforms by cost per conversion",
  "timeframe_description": "last week"
}
```

---

## Test 18: give me a breakdown of holiday campaign performance

**Answer**:
> Your revenue from the holiday campaign was $52,634.16 last week.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "holiday"
  },
  "thresholds": null,
  "question": "give me a breakdown of holiday campaign performance",
  "timeframe_description": "last week"
}
```

---

## Test 19: what is my average order value?

**Answer**:
> Your average order value was $33.38 last week.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "what is my average order value?",
  "timeframe_description": "last week"
}
```

---

## Test 20: give me a list of the top 5 adsets last week by revenue

**Answer**:
> You have a total of 5 entities, which include Holiday Sale - Purchases, Summer Sale Campaign, Black Friday Deals, App Install Campaign, and Mobile Game Installs.

**DSL**:
```json
{
  "query_type": "entities",
  "metric": "revenue",
  "time_range": {
    "last_n_days": 7,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "adset",
  "breakdown": "adset",
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "give me a list of the top 5 adsets last week by revenue",
  "timeframe_description": "last week"
}
```

---

## Test 21: What was the revenue for the Holiday Sale campaign last week?

**Answer**:
> The revenue for the Holiday Sale campaign was $52,634.16 last week.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "Holiday Sale"
  },
  "thresholds": null,
  "question": "What was the revenue for the Holiday Sale campaign last week?",
  "timeframe_description": "last week"
}
```

---

## Test 22: wich day had the lowest cpc on holiday sale campaign?

**Answer**:
> The lowest CPC for your Holiday Sale campaign last week was $0.50, which is a bit above the workspace average of $0.45. So, while it's not your best performance, it's still pretty close to the average.

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
  "top_n": 1,
  "sort_order": "asc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "Holiday Sale"
  },
  "thresholds": null,
  "question": "wich day had the lowest cpc on holiday sale campaign?",
  "timeframe_description": "last week"
}
```

---

## Test 23: roas last month for holiday sale campaign?

**Answer**:
> Your ROAS for the Holiday Sale campaign last month was an impressive 11.80×, which is well above the workspace average of 6.40×. That's a solid performance!

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "Holiday Sale"
  },
  "thresholds": null,
  "question": "roas last month for holiday sale campaign?",
  "timeframe_description": "last month"
}
```

---

## Test 24: wich had highest cpc, holiday campaign or app install campaign?

**Answer**:
> No cost per click data available for last week.

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
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 1,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "holiday campaign, app install campaign"
  },
  "thresholds": null,
  "question": "wich had highest cpc, holiday campaign or app install campaign?",
  "timeframe_description": "last week"
}
```

---

## Test 25: wich google campaigns are live?

**Answer**:
> You have a total of 10 active campaigns, including the Holiday Sale - Purchases, Summer Sale Campaign, and Black Friday Deals, among others.

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
  "sort_order": "desc",
  "filters": {
    "provider": "google",
    "level": "campaign",
    "entity_ids": null,
    "status": "active",
    "entity_name": null
  },
  "thresholds": null,
  "question": "wich google campaigns are live?",
  "timeframe_description": null
}
```

---

## Test 26: what is my revenue this month?

**Answer**:
> Your revenue this month is $1,762,399.43.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "what is my revenue this month?",
  "timeframe_description": "this month"
}
```

---

## Test 27: what was my revenue last month?

**Answer**:
> Your revenue was $1,762,399.43 last month.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "what was my revenue last month?",
  "timeframe_description": "last month"
}
```

---

## Test 28: what is my revenue this year?

**Answer**:
> Your revenue was $1,828,605.13 last year.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "revenue",
  "time_range": {
    "last_n_days": 365,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "what is my revenue this year?",
  "timeframe_description": "last year"
}
```

---

## Test 29: How does this week compare to last week?

**Answer**:
> This week, your revenue is $355,398.23, which is down 16.9% from last week's $427,922.71. It's pretty much in line with the workspace average, so you're performing at an average level overall.

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
  "compare_to_previous": true,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "How does this week compare to last week?",
  "timeframe_description": "this week"
}
```

---

## Test 30: Compare Google vs Meta performance

**Answer**:
> Last month, Google had a ROAS of 6.40×, which is right on par with your workspace average. In comparison, Meta really stood out with a ROAS of 9.42×, making it your top performer. So, while Google’s doing okay, Meta’s definitely leading the pack!

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "Compare Google vs Meta performance",
  "timeframe_description": "last month"
}
```

---

## Test 31: Is my ROAS improving or declining?

**Answer**:
> Your ROAS was 6.15× last week, which is a decline of about 4.7% from 6.45× the week before. So, it's not improving right now. For context, your current ROAS matches the workspace average, so you're right on par with others.

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
  "compare_to_previous": true,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "Is my ROAS improving or declining?",
  "timeframe_description": "last week"
}
```

---

## Test 32: compare holiday campaign performance to app install campaign performance

**Answer**:
> Last month, the holiday campaign brought in $0 in revenue, which is concerning since the workspace average is around $1.76 million—definitely below average. In comparison, the app install campaign also struggled, but it’s important to note that both campaigns need some attention to boost performance.

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
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "holiday, app install"
  },
  "thresholds": null,
  "question": "compare holiday campaign performance to app install campaign performance",
  "timeframe_description": "last month"
}
```

---

## Test 33: Which campaign had the highest ROAS last week?

**Answer**:
> The Holiday Sale - Purchases had the highest ROAS at 13.36× last week—your top performer! For context, your overall ROAS was 6.15×, which matches the workspace average. That's a solid result, especially with the Holiday Sale leading the pack!

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "Which campaign had the highest ROAS last week?",
  "timeframe_description": "last week"
}
```

---

## Test 34: Show me top 5 campaigns by revenue

**Answer**:
> The Summer Sale Campaign brought in the highest revenue at $85,108.72 last week—your top performer! Overall, your total revenue was $355,398.23, which is right on par with the workspace average.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "Show me top 5 campaigns by revenue",
  "timeframe_description": "last week"
}
```

---

## Test 35: List all active campaigns

**Answer**:
> You currently have 10 active campaigns, including the Holiday Sale - Purchases, Summer Sale Campaign, and Black Friday Deals, among others.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": "campaign",
    "entity_ids": null,
    "status": "active",
    "entity_name": null
  },
  "thresholds": null,
  "question": "List all active campaigns",
  "timeframe_description": null
}
```

---

## Test 36: Which adset had the highest cpc last week?

**Answer**:
> The Weekend Audience - Black Friday Deals had the highest CPC at $0.64 last week—definitely needs some attention. For context, your overall CPC was $0.45, which is right at the workspace average.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "Which adset had the highest cpc last week?",
  "timeframe_description": "last week"
}
```

---

## Test 37: Which adset had the highest cpc last week?

**Answer**:
> The Weekend Audience - Black Friday Deals had the highest CPC at $0.64 last week—definitely needs some attention. For context, your overall CPC was $0.45, which is right at the workspace average.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "Which adset had the highest cpc last week?",
  "timeframe_description": "last week"
}
```

---

## Test 38: Which adset had the lowest ctr last week?

**Answer**:
> The Morning Audience - General Conversions had the lowest CTR at 1.7% last week—definitely needs some attention. For context, your overall CTR was 2.6%, which is right at the workspace average.

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
  "sort_order": "asc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "Which adset had the lowest ctr last week?",
  "timeframe_description": "last week"
}
```

---

## Test 39: what is my total CVR last month?

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "what is my total CVR last month?",
  "timeframe_description": "last month"
}
```

---

## Test 40: what is my cvr on google last month?

**Answer**:
> Your CVR was 9.9% last month.

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
  "sort_order": "desc",
  "filters": {
    "provider": "google",
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "what is my cvr on google last month?",
  "timeframe_description": "last month"
}
```

---

## Test 41: What's my ROAS for active campaigns?

**Answer**:
> Your ROAS was 5.80× last week.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": "active",
    "entity_name": null
  },
  "thresholds": null,
  "question": "What's my ROAS for active campaigns?",
  "timeframe_description": "last week"
}
```

---

## Test 42: How much did I spend on Meta ads?

**Answer**:
> You spent $15,917.86 on Meta ads last week.

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
  "sort_order": "desc",
  "filters": {
    "provider": "meta",
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "How much did I spend on Meta ads?",
  "timeframe_description": "last week"
}
```

---

## Test 43: How much revenue on Google last week?

**Answer**:
> Your revenue was $154,550.10 last week.

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
  "sort_order": "desc",
  "filters": {
    "provider": "google",
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "How much revenue on Google last week?",
  "timeframe_description": "last week"
}
```

---

## Test 44: What's my cost per install?

**Answer**:
> Your cost per install was $24.74 last week.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "What's my cost per install?",
  "timeframe_description": "last week"
}
```

---

## Test 45: How many leads did I generate today?

**Answer**:
> You generated 0 leads today.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "How many leads did I generate today?",
  "timeframe_description": "today"
}
```

---

## Test 46: wich ad had the lowest cpc last week?

**Answer**:
> The Image Ad - Weekend Audience - Website Traffic Push had the lowest CPC at $0.28 last week—your best performer! For context, your overall CPC was $0.45, which matches the workspace average.

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
  "sort_order": "asc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "wich ad had the lowest cpc last week?",
  "timeframe_description": "last week"
}
```

---

## Test 47: What time on average do i get the best cpc?

**Answer**:
> Your average CPC was $0.45 last week, which is right on par with the overall workspace average—so you're doing just fine! It looks like there's been no deviation, meaning your performance is steady.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "What time on average do i get the best cpc?",
  "timeframe_description": "last week"
}
```

---

## Test 48: how much revenue would i have last week if my cpc was 0.20?

**Answer**:
> Your revenue was $355,398.23 last week.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "how much revenue would i have last week if my cpc was 0.20?",
  "timeframe_description": "last week"
}
```

---

## Test 49: 

**Answer**:
> ERROR

**DSL**:
```json
{}
```

---

## Test 50: How is the Summer Sale campaign performing?

**Answer**:
> The Summer Sale campaign brought in $6,190.20 last week, which is below the workspace average of $355,398.23—definitely concerning. It seems like it’s not hitting the mark compared to what you typically see.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": "campaign",
    "entity_ids": null,
    "status": null,
    "entity_name": "Summer Sale"
  },
  "thresholds": null,
  "question": "How is the Summer Sale campaign performing?",
  "timeframe_description": "last week"
}
```

---

## Test 51: Show me all lead gen campaigns

**Answer**:
> You're currently running one campaign, which is "Lead Gen - B2B."

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": "campaign",
    "entity_ids": null,
    "status": null,
    "entity_name": "lead gen"
  },
  "thresholds": null,
  "question": "Show me all lead gen campaigns",
  "timeframe_description": null
}
```

---

## Test 52: What's the CPA for Morning Audience adsets?

**Answer**:
> Your CPA for Morning Audience adsets was $4.83 last week.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpa",
  "time_range": {
    "last_n_days": 7,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": "adset",
    "entity_ids": null,
    "status": null,
    "entity_name": "Morning Audience"
  },
  "thresholds": null,
  "question": "What's the CPA for Morning Audience adsets?",
  "timeframe_description": "last week"
}
```

---

## Test 53: What's the revenue for Black Friday campaign?

**Answer**:
> Your revenue for the Black Friday campaign was $2,942.13 last week.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": "campaign",
    "entity_ids": null,
    "status": null,
    "entity_name": "black friday"
  },
  "thresholds": null,
  "question": "What's the revenue for Black Friday campaign?",
  "timeframe_description": "last week"
}
```

---

## Test 54: Give me ROAS for App Install campaigns

**Answer**:
> Your ROAS for App Install campaigns was 0.64× last week, which is below the workspace average of 6.15×—that's concerning. It looks like this campaign is your top performer, but it still needs some attention to get closer to that average.

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
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "app install"
  },
  "thresholds": null,
  "question": "Give me ROAS for App Install campaigns",
  "timeframe_description": "last week"
}
```

---

## Test 55: Show me Weekend Audience adsets

**Answer**:
> You have a total of 10 ad sets, including names like "Weekend Audience - Holiday Sale - Purchases," "Weekend Audience - Summer Sale Campaign," and "Weekend Audience - Black Friday Deals."

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": "adset",
    "entity_ids": null,
    "status": null,
    "entity_name": "weekend audience"
  },
  "thresholds": null,
  "question": "Show me Weekend Audience adsets",
  "timeframe_description": null
}
```

---

## Test 56: What's the CTR for Evening Audience adsets?

**Answer**:
> Your CTR was 2.5% last week.

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
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": "adset",
    "entity_ids": null,
    "status": null,
    "entity_name": "evening audience"
  },
  "thresholds": null,
  "question": "What's the CTR for Evening Audience adsets?",
  "timeframe_description": "last week"
}
```

---

## Test 57: How much did Holiday Sale campaign spend last week?

**Answer**:
> The Holiday Sale campaign spent $298.38 last week.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": "campaign",
    "entity_ids": null,
    "status": null,
    "entity_name": "Holiday Sale"
  },
  "thresholds": null,
  "question": "How much did Holiday Sale campaign spend last week?",
  "timeframe_description": "last week"
}
```

---

## Test 58: Compare CPC, CTR, and ROAS for Holiday Sale and App Install campaigns last week

**Answer**:
> ERROR

**DSL**:
```json
{}
```

---

## Test 59: What's the spend, revenue, and ROAS for all Google campaigns in September?

**Answer**:
> In September, your Google campaigns had a total spend of $0.00, which is pretty average compared to previous months. Since there was no spend, revenue and ROAS are also at $0—so it looks like there’s room for improvement moving forward!

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "spend",
  "time_range": {
    "last_n_days": 7,
    "start": "2023-09-01",
    "end": "2023-09-30"
  },
  "compare_to_previous": false,
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": "google",
    "level": "campaign",
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "What's the spend, revenue, and ROAS for all Google campaigns in September?",
  "timeframe_description": "last week"
}
```

---

## Test 60: Show me clicks, conversions, and cost per conversion for Meta campaigns last 5 days

**Answer**:
> Your cost per conversion for Meta campaigns over the last 5 days was $5.25, which is a bit better than the workspace average of $5.40. Just so you know, the top performer in this period was the Black Friday Deals campaign at $11.28. Overall, you're doing pretty average!

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpa",
  "time_range": {
    "last_n_days": 5,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": "meta",
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "Show me clicks, conversions, and cost per conversion for Meta campaigns last 5 days",
  "timeframe_description": "last 5 days"
}
```

---

## Test 61: Give me CTR, CPC, and conversion rate for Summer Sale campaign last month

**Answer**:
> Your CTR for the Summer Sale campaign was 3.1% last month.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "ctr",
  "time_range": {
    "last_n_days": 30,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": "campaign",
    "entity_ids": null,
    "status": null,
    "entity_name": "Summer Sale"
  },
  "thresholds": null,
  "question": "Give me CTR, CPC, and conversion rate for Summer Sale campaign last month",
  "timeframe_description": "last month"
}
```

---

## Test 62: Compare spend and revenue between Morning Audience and Evening Audience adsets this month to date

**Answer**:
> The Morning Audience ad set hasn't spent anything this month, which is concerning since the workspace average spend is around $275,259.45—so it's definitely below average. You might want to look into why that is!

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
  "group_by": "adset",
  "breakdown": "adset",
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "morning audience, evening audience"
  },
  "thresholds": null,
  "question": "Compare spend and revenue between Morning Audience and Evening Audience adsets this month to date",
  "timeframe_description": "this month"
}
```

---

## Test 63: What's the ROAS, revenue, and profit for Black Friday campaign last week?

**Answer**:
> The Black Friday campaign had an impressive ROAS of 10.22× last week, which is well above the workspace average of 6.15×—that's excellent! It looks like those Black Friday Deals really paid off!

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
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "black friday"
  },
  "thresholds": null,
  "question": "What's the ROAS, revenue, and profit for Black Friday campaign last week?",
  "timeframe_description": "last week"
}
```

---

## Test 64: Show me CPC, clicks, and spend for all active campaigns last 5 days

**Answer**:
> Your CPC was $0.45 over the last 5 days, which is pretty much in line with the workspace average of $0.46. The Black Friday Deals campaign had the highest CPC at $0.54, but overall, your CPC performance is looking average.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpc",
  "time_range": {
    "last_n_days": 5,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": "active",
    "entity_name": null
  },
  "thresholds": null,
  "question": "Show me CPC, clicks, and spend for all active campaigns last 5 days",
  "timeframe_description": "last 5 days"
}
```

---

## Test 65: Compare CTR and conversion rate for Google vs Meta campaigns in September

**Answer**:
> In September, your Google campaigns had an average CTR, while Meta's was also around the same level—so they're pretty much neck and neck. As for conversion rates, Google performed slightly better than Meta, which is a good sign for your overall strategy.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "ctr",
  "time_range": {
    "last_n_days": 7,
    "start": "2023-09-01",
    "end": "2023-09-30"
  },
  "compare_to_previous": false,
  "group_by": "provider",
  "breakdown": "provider",
  "top_n": 10,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "Compare CTR and conversion rate for Google vs Meta campaigns in September",
  "timeframe_description": "last week"
}
```

---

## Test 66: What's the revenue, ROAS, and cost per lead for lead gen campaigns this month to date?

**Answer**:
> Your revenue is $4,620.94 this month.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": "campaign",
    "entity_ids": null,
    "status": null,
    "entity_name": "lead gen"
  },
  "thresholds": null,
  "question": "What's the revenue, ROAS, and cost per lead for lead gen campaigns this month to date?",
  "timeframe_description": "this month"
}
```

---

## Test 67: Give me spend, clicks, and CPC for Holiday Sale and Summer Sale campaigns last month

**Answer**:
> The Holiday Sale campaign had a spend of $0 last month, which is concerning since it's below the workspace average of about $275,259. The Summer Sale also didn't spend anything, so both campaigns really need to ramp up their budgets to compete.

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
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "holiday sale, summer sale"
  },
  "thresholds": null,
  "question": "Give me spend, clicks, and CPC for Holiday Sale and Summer Sale campaigns last month",
  "timeframe_description": "last month"
}
```

---

## Test 68: Show me conversion rate, revenue, and profit for all campaigns last week

**Answer**:
> Last week, your overall conversion rate was 8.4%, which matches the workspace average—so you're right on track. The top performer, Lead Gen - B2B, really stood out with a conversion rate of 17.5%. That's a solid benchmark to aim for!

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
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "Show me conversion rate, revenue, and profit for all campaigns last week",
  "timeframe_description": "last week"
}
```

---

## Test 69: Compare CPA, ROAS, and revenue for App Install campaign vs Holiday Sale campaign last 5 days

**Answer**:
> The App Install campaign had a CPA of $4.21 over the last 5 days, which is below the workspace average of $5.40—pretty solid performance! In comparison, the Holiday Sale campaign's CPA was higher, making the App Install campaign your top performer in this metric.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpa",
  "time_range": {
    "last_n_days": 5,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "app install"
  },
  "thresholds": null,
  "question": "Compare CPA, ROAS, and revenue for App Install campaign vs Holiday Sale campaign last 5 days",
  "timeframe_description": "last 5 days"
}
```

---

## Test 70: What's the CTR, CPC, and conversions for Weekend Audience adsets in September?

**Answer**:
> The CTR for your Weekend Audience adsets last week was N/A, which is about average for your campaigns. For context, your overall CTR has been hovering around 2.4%, so it looks like there's room for improvement there.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "ctr",
  "time_range": {
    "last_n_days": 7,
    "start": "2023-09-01",
    "end": "2023-09-30"
  },
  "compare_to_previous": false,
  "group_by": "adset",
  "breakdown": "adset",
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": "adset",
    "entity_ids": null,
    "status": null,
    "entity_name": "weekend audience"
  },
  "thresholds": null,
  "question": "What's the CTR, CPC, and conversions for Weekend Audience adsets in September?",
  "timeframe_description": "last week"
}
```

---

## Test 71: Give me spend, revenue, ROAS, and profit for all Meta campaigns this month to date

**Answer**:
> Your spend for Meta campaigns this month is $74,391.51, which is below the workspace average of $275,259.45—definitely something to keep an eye on. The top performer is the Black Friday Deals campaign, bringing in $21,437.48.

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
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": "meta",
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "Give me spend, revenue, ROAS, and profit for all Meta campaigns this month to date",
  "timeframe_description": "this month"
}
```

---

## Test 72: Compare clicks, CTR, and cost per click for Morning vs Evening Audience adsets last month

**Answer**:
> Last month, both the Morning and Evening Audience adsets had a CPC of $0.45, which is right on par with the workspace average. However, the Evening Audience - Newsletter Signup Campaign was your top performer at $0.53. So, while both are performing average, the Evening Audience is slightly higher in cost.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpc",
  "time_range": {
    "last_n_days": 30,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "adset",
  "breakdown": "adset",
  "top_n": 10,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null
  },
  "thresholds": null,
  "question": "Compare clicks, CTR, and cost per click for Morning vs Evening Audience adsets last month",
  "timeframe_description": "last month"
}
```

---

