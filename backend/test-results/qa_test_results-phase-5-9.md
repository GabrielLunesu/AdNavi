# QA Test Results

**Test Run**: Tue Oct 14 17:45:08 CEST 2025
**Workspace**: Defang Labs (9c76b246-faf1-42d6-9a5a-f564f7801b4e)
**System Version**: Phase 5 (v2.1.3)

---

## Test 1: What's my CPC this month?

**Answer**:
> Your CPC is $0.45 from October 01 to 14.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpc",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-14"
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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "What's my CPC this month?",
  "timeframe_description": "this month"
}
```

---

## Test 2: How much did I spend this month?

**Answer**:
> You spent $114,830.27 from October 01 to 14.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "spend",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-14"
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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "How much did I spend this month?",
  "timeframe_description": "this month"
}
```

---

## Test 3: What's my ROAS this week?

**Answer**:
> Your ROAS is N/A this week.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "roas",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-13",
    "end": "2025-10-14"
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
    "entity_name": null,
    "metric_filters": null
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
    "entity_name": null,
    "metric_filters": null
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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "What's my conversion rate?",
  "timeframe_description": "last week"
}
```

---

## Test 6: How many clicks did I get last week?

**Answer**:
> You had 105,001 clicks last week.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "How many clicks did I get last week?",
  "timeframe_description": "last week"
}
```

---

## Test 7: How much profit did I make last week?

**Answer**:
> Your profit was $89,905.10 last week.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "How much profit did I make last week?",
  "timeframe_description": "last week"
}
```

---

## Test 8: How many leads did I generate this month?

**Answer**:
> You generated 8,404 leads from October 01 to 14.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "leads",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-14"
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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "How many leads did I generate this month?",
  "timeframe_description": "this month"
}
```

---

## Test 9: What is my cost per lead this month?

**Answer**:
> Your cost per lead is $13.66 from October 01 to 14.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpl",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-14"
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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "What is my cost per lead this month?",
  "timeframe_description": "this month"
}
```

---

## Test 10: Which campaign had the highest ROAS last week?

**Answer**:
> The Holiday Sale - Purchases had the highest ROAS at an impressive 22.40× last week—your top performer! For context, your overall ROAS was 6.29×, which is right at the average for the workspace. That's a fantastic result!

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Which campaign had the highest ROAS last week?",
  "timeframe_description": "last week"
}
```

---

## Test 11: What's my ROAS for Google campaigns only?

**Answer**:
> Your ROAS for Google campaigns only was 6.18× last week.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "What's my ROAS for Google campaigns only?",
  "timeframe_description": "last week"
}
```

---

## Test 12: Which campaign spent the most yesterday?

**Answer**:
> It looks like no campaigns spent anything yesterday, so there’s really no top spender to highlight. That’s pretty average, but it might be worth checking in on your budget allocation for the day!

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Which campaign spent the most yesterday?",
  "timeframe_description": "yesterday"
}
```

---

## Test 13: List all active campaigns

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "List all active campaigns",
  "timeframe_description": null
}
```

---

## Test 14: Which ad has the highest CTR?

**Answer**:
> The Carousel Ad - Evening Audience - App Install Campaign had the highest CTR at 4.2% last week—your top performer! For context, your overall CTR was 2.5%, which is right on average for the workspace.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Which ad has the highest CTR?",
  "timeframe_description": "last week"
}
```

---

## Test 15: Show me campaigns with ROAS above 4

**Answer**:
> Your campaigns had a solid ROAS of 6.29× last week, which matches the workspace average—pretty consistent! The standout was the Holiday Sale - Purchases, crushing it with a ROAS of 22.40×.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null,
    "metric_filters": [
      {
        "metric": "roas",
        "operator": ">",
        "value": 4
      }
    ]
  },
  "thresholds": null,
  "question": "Show me campaigns with ROAS above 4",
  "timeframe_description": "last week"
}
```

---

## Test 16: Which campaign generated the most leads?

**Answer**:
> The Blog Content Promotion campaign generated the most leads last week with 3,534—your top performer! That’s right on par with the workspace average, so it’s performing consistently well.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Which campaign generated the most leads?",
  "timeframe_description": "last week"
}
```

---

## Test 17: Rank platforms by cost per conversion

**Answer**:
> Google had the lowest CPA at $4.36 last week, making it your top performer! For context, your overall CPA was $5.40, which is right at the workspace average. So, it looks like Google is doing a bit better than the rest!

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Rank platforms by cost per conversion",
  "timeframe_description": "last week"
}
```

---

## Test 18: give me a breakdown of holiday campaign performance

**Answer**:
> Your holiday campaign brought in $46,934.31 last week, which is below the workspace average of $299,798.95—definitely something to keep an eye on. The top performer was the Holiday Sale - Purchases at $4,926.40, but overall, the performance is a bit concerning.

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
    "entity_name": "holiday",
    "metric_filters": null
  },
  "thresholds": null,
  "question": "give me a breakdown of holiday campaign performance",
  "timeframe_description": "last week"
}
```

---

## Test 19: what is my average order value?

**Answer**:
> Your average order value was $33.99 last week.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "what is my average order value?",
  "timeframe_description": "last week"
}
```

---

## Test 20: give me a list of the top 5 adsets last week by revenue

**Answer**:
> The top ad set last week was the Evening Audience - Summer Sale Campaign, bringing in $7,786.82—your best performer! Overall, your total revenue was $299,798.95, which is right on par with the average for the workspace.

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
  "group_by": "adset",
  "breakdown": "adset",
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "give me a list of the top 5 adsets last week by revenue",
  "timeframe_description": "last week"
}
```

---

## Test 21: What was the revenue for the Holiday Sale campaign last week?

**Answer**:
> The revenue for the Holiday Sale campaign was $46,934.31 last week.

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
    "entity_name": "Holiday Sale",
    "metric_filters": null
  },
  "thresholds": null,
  "question": "What was the revenue for the Holiday Sale campaign last week?",
  "timeframe_description": "last week"
}
```

---

## Test 22: wich day had the lowest cpc on holiday sale campaign?

**Answer**:
> ERROR

**DSL**:
```json
{}
```

---

## Test 23: roas last month for holiday sale campaign?

**Answer**:
> Your ROAS for the holiday sale campaign was 11.87× in the last 30 days, which is excellent! For some context, that's well above the workspace average of 6.43×, so it looks like the campaign really resonated with your audience.

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
    "entity_name": "Holiday Sale",
    "metric_filters": null
  },
  "thresholds": null,
  "question": "roas last month for holiday sale campaign?",
  "timeframe_description": "last month"
}
```

---

## Test 24: wich had highest cpc, holiday campaign or app install campaign?

**Answer**:
> ERROR

**DSL**:
```json
{}
```

---

## Test 25: wich google campaigns are live?

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
    "provider": "google",
    "level": "campaign",
    "entity_ids": null,
    "status": "active",
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "wich google campaigns are live?",
  "timeframe_description": null
}
```

---

## Test 26: what is my revenue this month?

**Answer**:
> Your revenue is $725,481.04 from October 01 to 14.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "revenue",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-14"
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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "what is my revenue this month?",
  "timeframe_description": "this month"
}
```

---

## Test 27: what was my revenue last month?

**Answer**:
> Your revenue was $1,706,755.03 in the last 30 days.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "what was my revenue last month?",
  "timeframe_description": "last month"
}
```

---

## Test 28: what is my revenue this year?

**Answer**:
> Your revenue was $1,828,605.13 in the last 365 days.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "what is my revenue this year?",
  "timeframe_description": "last year"
}
```

---

## Test 29: How does this week compare to last week?

**Answer**:
> This week, your revenue is $299,798.95, which is down 29.6% from last week's $425,682.09. It looks like you're performing at an average level compared to your overall workspace average, but it's definitely a dip from last week.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "How does this week compare to last week?",
  "timeframe_description": "this week"
}
```

---

## Test 30: Compare Google vs Meta performance

**Answer**:
> In the last 30 days, Google's ROAS was 6.43×, which is right on par with your workspace average. However, Meta's been leading the pack with a solid 9.44×—definitely something to note!

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Compare Google vs Meta performance",
  "timeframe_description": "last month"
}
```

---

## Test 31: Is my ROAS improving or declining?

**Answer**:
> Your ROAS was 6.29× last week, which is a slight decline of 0.8% from 6.34× the week before. It’s right at the average for your workspace, so it’s performing consistently but not improving.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Is my ROAS improving or declining?",
  "timeframe_description": "last week"
}
```

---

## Test 32: compare holiday campaign performance to app install campaign performance

**Answer**:
> ERROR

**DSL**:
```json
{}
```

---

## Test 33: Which campaign had the highest ROAS last week?

**Answer**:
> The Holiday Sale - Purchases had the highest ROAS last week at an impressive 22.40×—your top performer! For context, your overall ROAS was 6.29×, which matches the workspace average. That's a solid performance!

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Which campaign had the highest ROAS last week?",
  "timeframe_description": "last week"
}
```

---

## Test 34: Show me top 5 campaigns by revenue

**Answer**:
> The Holiday Sale - Purchases brought in the highest revenue at $4,926.40 last week—your top performer! Overall, your total revenue was $299,798.95, which matches the average for your workspace, so you're right on track.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Show me top 5 campaigns by revenue",
  "timeframe_description": "last week"
}
```

---

## Test 35: List all active campaigns

**Answer**:
> You currently have 10 active campaigns, including the Holiday Sale - Purchases, Summer Sale Campaign, Black Friday Deals, and several others like the App Install Campaign and Brand Awareness.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "List all active campaigns",
  "timeframe_description": null
}
```

---

## Test 36: Which adset had the highest cpc last week?

**Answer**:
> The Evening Audience - Mobile Game Installs ad set had the highest CPC at $0.69 last week—definitely your worst performer. For context, your overall CPC was $0.45, which is right at the workspace average.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Which adset had the highest cpc last week?",
  "timeframe_description": "last week"
}
```

---

## Test 37: Which adset had the highest cpc last week?

**Answer**:
> The Evening Audience - Mobile Game Installs ad set had the highest CPC at $0.69 last week—definitely your worst performer. For context, your overall CPC was $0.45, which matches the workspace average, so this ad set really stood out in the wrong way.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Which adset had the highest cpc last week?",
  "timeframe_description": "last week"
}
```

---

## Test 38: Which adset had the lowest ctr last week?

**Answer**:
> The Weekend Audience - General Conversions had the lowest CTR at 1.5% last week—definitely needs some attention. For context, your overall CTR was 2.5%, which is right at the average for your workspace.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Which adset had the lowest ctr last week?",
  "timeframe_description": "last week"
}
```

---

## Test 39: what is my total CVR last month?

**Answer**:
> Your total CVR was 8.5% in the last 30 days.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "what is my total CVR last month?",
  "timeframe_description": "last month"
}
```

---

## Test 40: what is my cvr on google last month?

**Answer**:
> Your CVR on Google was 9.8% in the last 30 days.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "what is my cvr on google last month?",
  "timeframe_description": "last month"
}
```

---

## Test 41: What's my ROAS for active campaigns?

**Answer**:
> Your ROAS was 5.92× last week.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "What's my ROAS for active campaigns?",
  "timeframe_description": "last week"
}
```

---

## Test 42: How much did I spend on Meta ads?

**Answer**:
> You spent $13,306.46 last week.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "How much did I spend on Meta ads?",
  "timeframe_description": "last week"
}
```

---

## Test 43: How much revenue on Google last week?

**Answer**:
> Your revenue on Google was $126,245.09 last week.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "How much revenue on Google last week?",
  "timeframe_description": "last week"
}
```

---

## Test 44: What's my cost per install?

**Answer**:
> Your cost per install was $24.55 last week.

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
    "entity_name": null,
    "metric_filters": null
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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "How many leads did I generate today?",
  "timeframe_description": "today"
}
```

---

## Test 46: wich ad had the lowest cpc last week?

**Answer**:
> The Image Ad - Weekend Audience - Website Traffic Push had the lowest CPC at $0.29 last week—your top performer! For context, your overall CPC was $0.45, which is right on par with the workspace average.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "wich ad had the lowest cpc last week?",
  "timeframe_description": "last week"
}
```

---

## Test 47: What time on average do i get the best cpc?

**Answer**:
> ERROR

**DSL**:
```json
{}
```

---

## Test 48: how much revenue would i have last week if my cpc was 0.20?

**Answer**:
> Your revenue was $299,798.95 last week.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "how much revenue would i have last week if my cpc was 0.20?",
  "timeframe_description": "last week"
}
```

---

## Test 49: 

**Answer**:
> Your revenue was $299,798.95 last week.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "",
  "timeframe_description": "last week"
}
```

---

## Test 50: How is the Summer Sale campaign performing?

**Answer**:
> The Summer Sale campaign brought in $4,863.18 last week, making it your top performer, but that's still concerning since it's well below the workspace average of $299,798.95. It looks like it needs some attention to boost those numbers!

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
    "entity_name": "Summer Sale",
    "metric_filters": null
  },
  "thresholds": null,
  "question": "How is the Summer Sale campaign performing?",
  "timeframe_description": "last week"
}
```

---

## Test 51: Show me all lead gen campaigns

**Answer**:
> You have one campaign named "Lead Gen - B2B."

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
    "entity_name": "lead gen",
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Show me all lead gen campaigns",
  "timeframe_description": null
}
```

---

## Test 52: What's the CPA for Morning Audience adsets?

**Answer**:
> The CPA for the Morning Audience adsets was $4.81 last week.

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
    "entity_name": "Morning Audience",
    "metric_filters": null
  },
  "thresholds": null,
  "question": "What's the CPA for Morning Audience adsets?",
  "timeframe_description": "last week"
}
```

---

## Test 53: What's the revenue for Black Friday campaign?

**Answer**:
> The revenue for the Black Friday campaign was $43,614.59 last week.

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
    "entity_name": "black friday",
    "metric_filters": null
  },
  "thresholds": null,
  "question": "What's the revenue for Black Friday campaign?",
  "timeframe_description": "last week"
}
```

---

## Test 54: Give me ROAS for App Install campaigns

**Answer**:
> Your ROAS for App Install campaigns was 0.64× last week, which is below the workspace average of 6.29×—that's concerning. The top performer in this category was the App Install Campaign at 1.11×, so there's definitely room for improvement!

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
    "entity_name": "app install",
    "metric_filters": null
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
    "entity_name": "weekend audience",
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Show me Weekend Audience adsets",
  "timeframe_description": null
}
```

---

## Test 56: What's the CTR for Evening Audience adsets?

**Answer**:
> The CTR for Evening Audience adsets was 2.4% last week.

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
    "entity_name": "evening audience",
    "metric_filters": null
  },
  "thresholds": null,
  "question": "What's the CTR for Evening Audience adsets?",
  "timeframe_description": "last week"
}
```

---

## Test 57: How much did Holiday Sale campaign spend last week?

**Answer**:
> The Holiday Sale campaign spent $3,221.99 last week.

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
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "Holiday Sale",
    "metric_filters": null
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
> Here are your metrics from 2025-09-01 to 2025-09-30:

• SPEND: $71,585.80
• REVENUE: $487,266.83
• ROAS: 6.81×

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": [
    "spend",
    "revenue",
    "roas"
  ],
  "time_range": {
    "last_n_days": null,
    "start": "2025-09-01",
    "end": "2025-09-30"
  },
  "compare_to_previous": false,
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 10,
  "sort_order": "desc",
  "filters": {
    "provider": "google",
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "What's the spend, revenue, and ROAS for all Google campaigns in September?",
  "timeframe_description": "from 2025-09-01 to 2025-09-30"
}
```

---

## Test 60: Show me clicks, conversions, and cost per conversion for Meta campaigns last 5 days

**Answer**:
> Here are your metrics in the last 5 days:

• CLICKS: 16,424
• CONVERSIONS: 1,522
• CPA: $5.46

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": [
    "clicks",
    "conversions",
    "cpa"
  ],
  "time_range": {
    "last_n_days": 5,
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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Show me clicks, conversions, and cost per conversion for Meta campaigns last 5 days",
  "timeframe_description": "last 5 days"
}
```

---

## Test 61: Give me CTR, CPC, and conversion rate for Summer Sale campaign last month

**Answer**:
> Here are your metrics in the last 30 days:

• CTR: 3.5%
• CPC: $0.40
• CVR: 4.8%

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": [
    "ctr",
    "cpc",
    "cvr"
  ],
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
    "entity_name": "Summer Sale",
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Give me CTR, CPC, and conversion rate for Summer Sale campaign last month",
  "timeframe_description": "last month"
}
```

---

## Test 62: Compare spend and revenue between Morning Audience and Evening Audience adsets this month to date

**Answer**:
> ERROR

**DSL**:
```json
{}
```

---

## Test 63: What's the ROAS, revenue, and profit for Black Friday campaign last week?

**Answer**:
> Here are your metrics last week:

• ROAS: 10.49×
• REVENUE: $43,614.59
• PROFIT: $12,707.22

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": [
    "roas",
    "revenue",
    "profit"
  ],
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
    "entity_name": "black friday",
    "metric_filters": null
  },
  "thresholds": null,
  "question": "What's the ROAS, revenue, and profit for Black Friday campaign last week?",
  "timeframe_description": "last week"
}
```

---

## Test 64: Show me CPC, clicks, and spend for all active campaigns last 5 days

**Answer**:
> Here are your metrics in the last 5 days:

• CPC: $0.46
• CLICKS: 60,930
• SPEND: $27,884.89

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": [
    "cpc",
    "clicks",
    "spend"
  ],
  "time_range": {
    "last_n_days": 5,
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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Show me CPC, clicks, and spend for all active campaigns last 5 days",
  "timeframe_description": "last 5 days"
}
```

---

## Test 65: Compare CTR and conversion rate for Google vs Meta campaigns in September

**Answer**:
> Here are your metrics from 2025-09-01 to 2025-09-30:

• CTR: 2.5%
• CVR: 8.5%

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": [
    "ctr",
    "cvr"
  ],
  "time_range": {
    "last_n_days": null,
    "start": "2025-09-01",
    "end": "2025-09-30"
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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Compare CTR and conversion rate for Google vs Meta campaigns in September",
  "timeframe_description": "from 2025-09-01 to 2025-09-30"
}
```

---

## Test 66: What's the revenue, ROAS, and cost per lead for lead gen campaigns this month to date?

**Answer**:
> Here are your metrics from October 01 to 14:

• REVENUE: $2,064.52
• ROAS: 2.29×
• CPL: $2.38

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": [
    "revenue",
    "roas",
    "cpl"
  ],
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-14"
  },
  "compare_to_previous": false,
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": "campaign",
    "entity_ids": null,
    "status": null,
    "entity_name": "lead gen",
    "metric_filters": null
  },
  "thresholds": null,
  "question": "What's the revenue, ROAS, and cost per lead for lead gen campaigns this month to date?",
  "timeframe_description": "this month"
}
```

---

## Test 67: Give me spend, clicks, and CPC for Holiday Sale and Summer Sale campaigns last month

**Answer**:
> Here are your metrics in the last 30 days:

• SPEND: $0.00
• CLICKS: 0

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": [
    "spend",
    "clicks",
    "cpc"
  ],
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
    "entity_name": "Holiday Sale, Summer Sale",
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Give me spend, clicks, and CPC for Holiday Sale and Summer Sale campaigns last month",
  "timeframe_description": "last month"
}
```

---

## Test 68: Show me conversion rate, revenue, and profit for all campaigns last week

**Answer**:
> Here are your metrics last week:

• CVR: 8.4%
• REVENUE: $299,798.95
• PROFIT: $89,905.10

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": [
    "cvr",
    "revenue",
    "profit"
  ],
  "time_range": {
    "last_n_days": 7,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 10,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Show me conversion rate, revenue, and profit for all campaigns last week",
  "timeframe_description": "last week"
}
```

---

## Test 69: Compare CPA, ROAS, and revenue for App Install campaign vs Holiday Sale campaign last 5 days

**Answer**:
> ERROR

**DSL**:
```json
{}
```

---

## Test 70: What's the CTR, CPC, and conversions for Weekend Audience adsets in September?

**Answer**:
> Here are your metrics from 2025-09-01 to 2025-09-30:

• CTR: 2.5%
• CPC: $0.45
• CONVERSIONS: 2,289

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": [
    "ctr",
    "cpc",
    "conversions"
  ],
  "time_range": {
    "last_n_days": null,
    "start": "2025-09-01",
    "end": "2025-09-30"
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
    "entity_name": "weekend audience",
    "metric_filters": null
  },
  "thresholds": null,
  "question": "What's the CTR, CPC, and conversions for Weekend Audience adsets in September?",
  "timeframe_description": "from 2025-09-01 to 2025-09-30"
}
```

---

## Test 71: Give me spend, revenue, ROAS, and profit for all Meta campaigns this month to date

**Answer**:
> Here are your metrics from October 01 to 14:

• SPEND: $31,037.16
• REVENUE: $296,125.61
• ROAS: 9.54×
• PROFIT: $88,413.86

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": [
    "spend",
    "revenue",
    "roas",
    "profit"
  ],
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-14"
  },
  "compare_to_previous": false,
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 10,
  "sort_order": "desc",
  "filters": {
    "provider": "meta",
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "question": "Give me spend, revenue, ROAS, and profit for all Meta campaigns this month to date",
  "timeframe_description": "this month"
}
```

---

## Test 72: Compare clicks, CTR, and cost per click for Morning vs Evening Audience adsets last month

**Answer**:
> ERROR

**DSL**:
```json
{}
```

---

