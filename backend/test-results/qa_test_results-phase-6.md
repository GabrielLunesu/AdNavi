# QA Test Results

**Test Run**: Wed Oct 15 15:03:06 CEST 2025
**Workspace**: Defang Labs (e4aee3b7-388e-428f-b5f5-a93e046b272f)
**System Version**: Phase 5 (v2.1.3)

---

## Test 1: What's my CPC this month?

**Answer**:
> Your CPC is $0.44 from October 01 to 15.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpc",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-15"
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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's my CPC this month?",
  "timeframe_description": "this month"
}
```

---

## Test 2: How much did I spend this month?

**Answer**:
> You spent $142,804.68 from October 01 to 15.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "spend",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-15"
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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "How much did I spend this month?",
  "timeframe_description": "this month"
}
```

---

## Test 3: What's my ROAS this week?

**Answer**:
> Your ROAS is 6.28× this week.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "roas",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-13",
    "end": "2025-10-15"
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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's my ROAS this week?",
  "timeframe_description": "this week"
}
```

---

## Test 4: How much revenue did I generate yesterday?

**Answer**:
> Your revenue was $59,282.83 yesterday.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "How much revenue did I generate yesterday?",
  "timeframe_description": "yesterday"
}
```

---

## Test 5: What's my conversion rate?

**Answer**:
> Your conversion rate was 8.3% last week.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's my conversion rate?",
  "timeframe_description": "last week"
}
```

---

## Test 6: How many clicks did I get last week?

**Answer**:
> You had 149,074 clicks last week.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "How many clicks did I get last week?",
  "timeframe_description": "last week"
}
```

---

## Test 7: How much profit did I make last week?

**Answer**:
> Your profit was $125,781.71 last week.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "How much profit did I make last week?",
  "timeframe_description": "last week"
}
```

---

## Test 8: How many leads did I generate this month?

**Answer**:
> You generated 10,836 leads from October 01 to 15.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "leads",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-15"
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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "How many leads did I generate this month?",
  "timeframe_description": "this month"
}
```

---

## Test 9: What is my cost per lead this month?

**Answer**:
> Here are your metrics from October 01 to 15:

• SPEND: $142,804.68
• LEADS: 10,836

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": [
    "spend",
    "leads"
  ],
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-15"
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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What is my cost per lead this month?",
  "timeframe_description": "this month"
}
```

---

## Test 10: Which campaign had the highest ROAS last week?

**Answer**:
> The General Conversions campaign had the highest ROAS last week at an impressive 23.33×—your top performer! For context, your overall ROAS was 6.34×, which matches the workspace average, so that’s a solid benchmark.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Which campaign had the highest ROAS last week?",
  "timeframe_description": "last week"
}
```

---

## Test 11: What's my ROAS for Google campaigns only?

**Answer**:
> Your ROAS for Google campaigns was 6.59× last week.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's my ROAS for Google campaigns only?",
  "timeframe_description": "last week"
}
```

---

## Test 12: Which campaign spent the most yesterday?

**Answer**:
> The Website Traffic Push campaign spent the most yesterday at $109.24—your top performer! For context, your overall spend was $9,876.34, which is right on par with the average.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Which campaign spent the most yesterday?",
  "timeframe_description": "yesterday"
}
```

---

## Test 13: List all active campaigns

**Answer**:
> You have a total of 10 active campaigns, including App Install Campaign, Black Friday Deals, Brand Awareness, and Summer Sale Campaign, among others.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "List all active campaigns",
  "timeframe_description": null
}
```

---

## Test 14: Which ad has the highest CTR?

**Answer**:
> The Image Ad - Weekend Audience - Lead Gen - B2B had the highest CTR at 4.4% last week—your top performer! For context, your overall CTR was 2.6%, which matches the workspace average, so that ad really stood out.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Which ad has the highest CTR?",
  "timeframe_description": "last week"
}
```

---

## Test 15: Show me campaigns with ROAS above 4

**Answer**:
> Last week, your campaigns had a solid ROAS of 6.34×, which matches the workspace average—pretty consistent! The standout was the General Conversions campaign, crushing it with a ROAS of 23.33×.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Show me campaigns with ROAS above 4",
  "timeframe_description": "last week"
}
```

---

## Test 16: Which campaign generated the most leads?

**Answer**:
> The App Install Campaign generated the most leads last week with 5,024—your top performer! That's right on par with the workspace average, so it looks like you're doing well overall.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Which campaign generated the most leads?",
  "timeframe_description": "last week"
}
```

---

## Test 17: Rank platforms by cost per conversion

**Answer**:
> Google had the lowest CPA at $4.04 last week, making it your top performer. In comparison, your overall CPA was $5.27, which is right at the average for your workspace. So, it looks like Google is doing a bit better on cost per conversion!

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Rank platforms by cost per conversion",
  "timeframe_description": "last week"
}
```

---

## Test 18: give me a breakdown of holiday campaign performance

**Answer**:
> Your holiday campaign had 0 leads last week, which is below the workspace average of 5,024—definitely concerning. Interestingly, the top performer was the Holiday Sale - Purchases, but it also didn’t generate any leads. It seems like there’s some room for improvement here!

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
  "top_n": 10,
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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "give me a breakdown of holiday campaign performance",
  "timeframe_description": "last week"
}
```

---

## Test 19: what is my average order value?

**Answer**:
> Your average order value was $33.39 last week.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "what is my average order value?",
  "timeframe_description": "last week"
}
```

---

## Test 20: give me a list of the top 5 adsets last week by revenue

**Answer**:
> The Weekend Audience - Summer Sale Campaign brought in the highest revenue at $9,285.01 last week—your top performer! Overall, your total revenue was $412,855.54, which matches the workspace average, so it looks like you’re right on track!

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "give me a list of the top 5 adsets last week by revenue",
  "timeframe_description": "last week"
}
```

---

## Test 21: What was the revenue for the Holiday Sale campaign last week?

**Answer**:
> The revenue for the Holiday Sale campaign last week was $54,894.55, which is below the workspace average of $412,855.54—definitely something to keep an eye on. The top performer in your campaigns was the Holiday Sale - Purchases, bringing in $6,775.95.

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
    "entity_name": "Holiday Sale",
    "metric_filters": null
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What was the revenue for the Holiday Sale campaign last week?",
  "timeframe_description": "last week"
}
```

---

## Test 22: wich day had the lowest cpc on holiday sale campaign?

**Answer**:
> The day with the lowest CPC in your Holiday Sale campaign was October 13, at just $0.33—your best performer! For context, your CPC was $0.42 last week, which is slightly better than the workspace average of $0.44.

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
  "group_by": "day",
  "breakdown": "day",
  "top_n": 1,
  "sort_order": "asc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "Holiday Sale",
    "metric_filters": null
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "wich day had the lowest cpc on holiday sale campaign?",
  "timeframe_description": "last week"
}
```

---

## Test 23: roas last month for holiday sale campaign?

**Answer**:
> Your ROAS for the holiday sale campaign was 11.29× in the last 30 days, which is above average compared to the workspace average of 6.27×. That's an excellent performance!

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "roas last month for holiday sale campaign?",
  "timeframe_description": "last month"
}
```

---

## Test 24: wich had highest cpc, holiday campaign or app install campaign?

**Answer**:
> It looks like there are currently no entities to compare, as the count is 0. Let me know if you need help with anything else!

**DSL**:
```json
{
  "query_type": "comparison",
  "metric": null,
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
  "comparison_type": "entity_vs_entity",
  "comparison_entities": [
    "Holiday Sale",
    "App Install"
  ],
  "comparison_metrics": [
    "cpc"
  ],
  "question": "wich had highest cpc, holiday campaign or app install campaign?",
  "timeframe_description": "last week"
}
```

---

## Test 25: wich google campaigns are live?

**Answer**:
> It looks like there are currently no active campaigns. If you need assistance with setting up new campaigns, feel free to ask!

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "wich google campaigns are live?",
  "timeframe_description": null
}
```

---

## Test 26: what is my revenue this month?

**Answer**:
> Your revenue is $898,824.41 from October 01 to 15.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "revenue",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-15"
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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "what is my revenue this month?",
  "timeframe_description": "this month"
}
```

---

## Test 27: what was my revenue last month?

**Answer**:
> Your revenue was $1,795,647.50 in the last 30 days.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "what was my revenue last month?",
  "timeframe_description": "last month"
}
```

---

## Test 28: what is my revenue this year?

**Answer**:
> Your revenue was $1,795,647.50 in the last 365 days.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "what is my revenue this year?",
  "timeframe_description": "last year"
}
```

---

## Test 29: How does this week compare to last week?

**Answer**:
> This week, your revenue is $412,855.54, which is a decline of 3.5% from last week's $427,990.32. It's pretty much in line with the workspace average, so you're performing at an average level overall.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "How does this week compare to last week?",
  "timeframe_description": "this week"
}
```

---

## Test 30: Compare Google vs Meta performance

**Answer**:
> It looks like there are currently no entities to compare, as the count is 0. If you have specific entities in mind, please let me know!

**DSL**:
```json
{
  "query_type": "comparison",
  "metric": null,
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
  "comparison_type": "provider_vs_provider",
  "comparison_entities": null,
  "comparison_metrics": [
    "revenue"
  ],
  "question": "Compare Google vs Meta performance",
  "timeframe_description": "last month"
}
```

---

## Test 31: Is my ROAS improving or declining?

**Answer**:
> Your ROAS was 6.34× last week, which is a slight improvement from 6.32× the week before—so that's good! It’s right on par with the workspace average, too, so you’re performing consistently.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Is my ROAS improving or declining?",
  "timeframe_description": "last week"
}
```

---

## Test 32: compare holiday campaign performance to app install campaign performance

**Answer**:
> It looks like there are currently no entities to compare, as the count is 0. If you have specific entities in mind, feel free to share them!

**DSL**:
```json
{
  "query_type": "comparison",
  "metric": null,
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
  "comparison_type": "entity_vs_entity",
  "comparison_entities": [
    "Holiday",
    "App Install"
  ],
  "comparison_metrics": [
    "roas",
    "revenue",
    "spend"
  ],
  "question": "compare holiday campaign performance to app install campaign performance",
  "timeframe_description": "last week"
}
```

---

## Test 33: Which campaign had the highest ROAS last week?

**Answer**:
> The General Conversions campaign had the highest ROAS last week at an impressive 23.33×—your top performer! For context, your overall ROAS was 6.34×, which is right at the average for the workspace. That's a solid performance!

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Which campaign had the highest ROAS last week?",
  "timeframe_description": "last week"
}
```

---

## Test 34: Show me top 5 campaigns by revenue

**Answer**:
> The Summer Sale Campaign brought in $8,636.98 last week—your top performer! Overall, your total revenue was $412,855.54, which is right on par with the average for your workspace.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Show me top 5 campaigns by revenue",
  "timeframe_description": "last week"
}
```

---

## Test 35: List all active campaigns

**Answer**:
> You currently have 10 active campaigns, including the App Install Campaign, Black Friday Deals, Brand Awareness, and Summer Sale Campaign, among others.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "List all active campaigns",
  "timeframe_description": null
}
```

---

## Test 36: Which adset had the highest cpc last week?

**Answer**:
> The Evening Audience - Newsletter Signup Campaign had the highest CPC at $0.70 last week—your worst performer. For context, your overall CPC was $0.44, which matches the workspace average, so this adset really stood out for the wrong reasons.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Which adset had the highest cpc last week?",
  "timeframe_description": "last week"
}
```

---

## Test 37: Which adset had the highest cpc last week?

**Answer**:
> The Evening Audience - Newsletter Signup Campaign had the highest CPC at $0.70 last week—your worst performer. For context, your overall CPC was $0.44, which matches the workspace average, so this adset really stood out for the wrong reasons.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Which adset had the highest cpc last week?",
  "timeframe_description": "last week"
}
```

---

## Test 38: Which adset had the lowest ctr last week?

**Answer**:
> The Weekend Audience - General Conversions had the lowest CTR at 1.5% last week—definitely needs some attention. For context, your overall CTR was 2.6%, which is right at the average for your workspace.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Which adset had the lowest ctr last week?",
  "timeframe_description": "last week"
}
```

---

## Test 39: what is my total CVR last month?

**Answer**:
> Your total CVR was 8.4% in the last 30 days.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "what is my total CVR last month?",
  "timeframe_description": "last month"
}
```

---

## Test 40: what is my cvr on google last month?

**Answer**:
> Your CVR was 9.7% in the last 30 days.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "what is my cvr on google last month?",
  "timeframe_description": "last month"
}
```

---

## Test 41: What's my ROAS for active campaigns?

**Answer**:
> Your ROAS for active campaigns was 6.03× last week, which is just a bit below the workspace average of 6.34×. For context, your top performer, General Conversions, is really crushing it at 23.33×!

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
    "status": "active",
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's my ROAS for active campaigns?",
  "timeframe_description": "last week"
}
```

---

## Test 42: How much did I spend on Meta ads?

**Answer**:
> You spent $18,119.06 last week.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "How much did I spend on Meta ads?",
  "timeframe_description": "last week"
}
```

---

## Test 43: How much revenue on Google last week?

**Answer**:
> Your revenue on Google was $179,025.00 last week.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "How much revenue on Google last week?",
  "timeframe_description": "last week"
}
```

---

## Test 44: What's my cost per install?

**Answer**:
> Your cost per install was $22.58 in the last 30 days.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpi",
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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's my cost per install?",
  "timeframe_description": "last month"
}
```

---

## Test 45: How many leads did I generate today?

**Answer**:
> You generated 674 leads today.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "How many leads did I generate today?",
  "timeframe_description": "today"
}
```

---

## Test 46: wich ad had the lowest cpc last week?

**Answer**:
> The Carousel Ad - Weekend Audience - Website Traffic Push had the lowest CPC at $0.29 last week—your top performer! For context, your overall CPC was $0.44, which is right on par with the workspace average.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "wich ad had the lowest cpc last week?",
  "timeframe_description": "last week"
}
```

---

## Test 47: how much revenue would i have last week if my cpc was 0.20?

**Answer**:
> Your revenue was $412,855.54 last week.

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
    "metric_filters": [
      {
        "metric": "cpc",
        "operator": "<",
        "value": 0.2
      }
    ]
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "how much revenue would i have last week if my cpc was 0.20?",
  "timeframe_description": "last week"
}
```

---

## Test 48: best performing ad set in Holiday Sale campaign yesterday?

**Answer**:
> The Evening Audience - Holiday Sale - Purchases was your best performing ad set yesterday, bringing in $1,398.51. That's quite a bit below your overall revenue average of $59,282.83, which is a bit concerning.

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
  "group_by": "adset",
  "breakdown": "adset",
  "top_n": 1,
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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "best performing ad set in Holiday Sale campaign yesterday?",
  "timeframe_description": "yesterday"
}
```

---

## Test 49: all ad sets above roas 4 in the last 3 days

**Answer**:
> In the last 3 days, your overall ROAS was 6.28×, which matches your workspace average—pretty solid! The top performer was the Evening Audience - Blog Content Promotion, crushing it at 20.58×.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "roas",
  "time_range": {
    "last_n_days": 3,
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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "all ad sets above roas 4 in the last 3 days",
  "timeframe_description": "last 3 days"
}
```

---

## Test 50: which campaign has the highest ctr?

**Answer**:
> The Lead Gen - B2B campaign had the highest CTR at 3.9% last week—your top performer! For context, your overall CTR was 2.6%, which is right at the average for your workspace.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "which campaign has the highest ctr?",
  "timeframe_description": "last week"
}
```

---

## Test 51: show me adsets with cpc below 1 dollar

**Answer**:
> Your CPC was $0.44 last week, which is right on par with the workspace average—so you're doing pretty well! The top performer, the Evening Audience - Newsletter Signup Campaign, had a CPC of $0.70, but you've got a solid grip on costs overall.

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
        "metric": "cpc",
        "operator": "<",
        "value": 1.0
      }
    ]
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "show me adsets with cpc below 1 dollar",
  "timeframe_description": "last week"
}
```

---

## Test 52: worst performing ad in App Install campaign?

**Answer**:
> The worst performing ad in your App Install campaign was the Image Ad - Weekend Audience, with a CPC of $0.42 last week—just a bit above the workspace average of $0.44. For context, your top performer had a much better CPC at $0.31, so there's definitely room for improvement!

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
    "entity_name": "app install",
    "metric_filters": null
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "worst performing ad in App Install campaign?",
  "timeframe_description": "last week"
}
```

---

## Test 53: all campaigns with conversion rate above 5%

**Answer**:
> Last week, your conversion rate was 8.3%, which matches the workspace average—pretty solid performance! It looks like you're in a good spot with that rate, especially since it's above the 5% mark you were interested in.

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
        "metric": "cvr",
        "operator": ">",
        "value": 5
      }
    ]
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "all campaigns with conversion rate above 5%",
  "timeframe_description": "last week"
}
```

---

## Test 54: which adset spent the most money?

**Answer**:
> The Weekend Audience - Summer Sale Campaign spent the most money last week at $741.64—your top performer! For context, your overall spend was $65,100.68, which is right on par with the average for the week.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "which adset spent the most money?",
  "timeframe_description": "last week"
}
```

---

## Test 55: show me ads with revenue above 1000

**Answer**:
> The Carousel Ad - Weekend Audience - Summer Sale Campaign brought in $10,173.84 last week, which is your top performer. Overall, your revenue was $412,855.54, matching the average for your workspace—so it looks like you're right on track!

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
  "group_by": "ad",
  "breakdown": "ad",
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
        "metric": "revenue",
        "operator": ">",
        "value": 1000
      }
    ]
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "show me ads with revenue above 1000",
  "timeframe_description": "last week"
}
```

---

## Test 56: best performing campaign by profit margin

**Answer**:
> The App Install Campaign had the lowest profit margin at 0.14× last week—definitely needs some attention. For context, your overall profit margin was 1.93×, which is right on par with the workspace average.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "poas",
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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "best performing campaign by profit margin",
  "timeframe_description": "last week"
}
```

---

## Test 57: all adsets with clicks above 500

**Answer**:
> Last week, you had a total of 149,074 clicks, which is right on average for your workspace. The top performer was the Weekend Audience from the Summer Sale Campaign, racking up 1,890 clicks. So, it looks like your adsets are performing consistently!

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
  "group_by": "adset",
  "breakdown": "adset",
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
        "metric": "clicks",
        "operator": ">",
        "value": 500
      }
    ]
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "all adsets with clicks above 500",
  "timeframe_description": "last week"
}
```

---

## Test 58: which ad has the lowest cost per conversion?

**Answer**:
> The Video Ad - Weekend Audience - Lead Gen - B2B had the lowest cost per conversion at $1.66 last week—your best performer! For context, your overall CPA was $5.27, which is right at the average for the workspace.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "which ad has the lowest cost per conversion?",
  "timeframe_description": "last week"
}
```

---

## Test 59: show me campaigns with impressions over 10000

**Answer**:
> Your campaigns had a total of 5,786,157 impressions last week, which is right on par with the workspace average. The App Install Campaign stood out with 43,584 impressions, making it your top performer. Overall, it looks like you're maintaining a solid level of visibility!

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "impressions",
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
        "metric": "impressions",
        "operator": ">",
        "value": 10000
      }
    ]
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "show me campaigns with impressions over 10000",
  "timeframe_description": "last week"
}
```

---

## Test 60: worst performing adset by roas

**Answer**:
> The Morning Audience - App Install Campaign had the lowest ROAS at 0.38× last week—definitely needs some attention. For context, your overall ROAS was 6.34×, which is right at the average for your workspace.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "worst performing adset by roas",
  "timeframe_description": "last week"
}
```

---

## Test 61: all ads with ctr above 3%

**Answer**:
> It looks like your CTR was 2.6% last week, which is right at the average for your workspace. Unfortunately, that means there weren't any ads that hit above the 3% mark.

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
        "metric": "ctr",
        "operator": ">",
        "value": 3
      }
    ]
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "all ads with ctr above 3%",
  "timeframe_description": "last week"
}
```

---

## Test 62: which campaign generated the most leads?

**Answer**:
> The App Install Campaign generated the most leads last week with 5,024—your top performer! That's right on par with your overall average, so it looks like you're maintaining a solid pace.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "which campaign generated the most leads?",
  "timeframe_description": "last week"
}
```

---

## Test 63: show me adsets with spend below 50 dollars

**Answer**:
> It looks like your total spend last week was $65,100.68, which is right on par with your average. Since you're looking for ad sets with spend below $50, it might be a bit tricky since the overall spend is quite high. If you need help finding specific ad sets, just let me know!

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
  "group_by": "adset",
  "breakdown": "adset",
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
        "metric": "spend",
        "operator": "<",
        "value": 50
      }
    ]
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "show me adsets with spend below 50 dollars",
  "timeframe_description": "last week"
}
```

---

## Test 64: best performing ad by revenue per click

**Answer**:
> The Image Ad - Evening Audience - Website Traffic Push had the highest ARPV at $2.87 last week, but that's actually below your workspace average of $3.77. So, while it was your top performer, it's still struggling compared to the overall performance.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "arpv",
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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "best performing ad by revenue per click",
  "timeframe_description": "last week"
}
```

---

## Test 65: all campaigns with cpm under 10 dollars

**Answer**:
> The Brand Awareness campaign had a CPM of $9.93 last week, which is your only campaign under $10. For context, your overall CPM was $11.25, so that one’s performing a bit better than average!

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpm",
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
        "metric": "cpm",
        "operator": "<",
        "value": 10
      }
    ]
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "all campaigns with cpm under 10 dollars",
  "timeframe_description": "last week"
}
```

---

## Test 66: which adset has the highest conversion rate?

**Answer**:
> The Weekend Audience - Summer Sale Campaign had the highest conversion rate at 4.2% last week—your top performer! For context, your overall conversion rate was 8.3%, which is right on par with the workspace average.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "which adset has the highest conversion rate?",
  "timeframe_description": "last week"
}
```

---

## Test 67: show me ads with conversions above 20

**Answer**:
> The Video Ad - Weekend Audience - Lead Gen - B2B had the highest conversions at 339 last week, which is pretty solid! Overall, your total conversions were 12,364, right on par with the workspace average.

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
  "compare_to_previous": false,
  "group_by": "ad",
  "breakdown": "ad",
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
        "metric": "conversions",
        "operator": ">",
        "value": 20
      }
    ]
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "show me ads with conversions above 20",
  "timeframe_description": "last week"
}
```

---

## Test 68: worst performing campaign by cost per lead

**Answer**:
> Your worst performing campaign by cost per lead last week was $12.96, which is right at the workspace average—so it’s performing just okay. For context, your top performer in this area was the General Conversions campaign, but it didn’t have a specific CPL to compare.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpl",
  "time_range": {
    "last_n_days": 7,
    "start": null,
    "end": null
  },
  "compare_to_previous": false,
  "group_by": "campaign",
  "breakdown": "campaign",
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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "worst performing campaign by cost per lead",
  "timeframe_description": "last week"
}
```

---

## Test 69: all adsets with revenue above 5000

**Answer**:
> Last week, your total revenue was $412,855.54, which is right on par with your average. The top performer was the Weekend Audience - Summer Sale Campaign, bringing in $9,285.01. Overall, it looks like your ad sets are doing well!

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
        "metric": "revenue",
        "operator": ">",
        "value": 5000
      }
    ]
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "all adsets with revenue above 5000",
  "timeframe_description": "last week"
}
```

---

## Test 70: which ad has the best profit margin?

**Answer**:
> The Image Ad - Evening Audience - Website Traffic Push had the best profit margin at 1.69× last week—your top performer! For context, your overall profit margin was 1.93×, which matches the workspace average. So, while that ad did well, it’s right in line with your typical performance.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "poas",
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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "which ad has the best profit margin?",
  "timeframe_description": "last week"
}
```

---

## Test 71: show me campaigns with clicks over 1000

**Answer**:
> Last week, your total clicks were 149,074, which is right on par with the average for your workspace. The App Install Campaign led the pack with 1,456 clicks, showing it's performing well among your campaigns.

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
        "metric": "clicks",
        "operator": ">",
        "value": 1000
      }
    ]
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "show me campaigns with clicks over 1000",
  "timeframe_description": "last week"
}
```

---

## Test 72: best performing adset by average order value

**Answer**:
> The Weekend Audience - Summer Sale Campaign had the highest average order value at $117.53 last week—definitely your top performer! For some context, your overall average order value was $33.39, so that’s quite a jump!

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "best performing adset by average order value",
  "timeframe_description": "last week"
}
```

---

## Test 73: all ads with spend above 200 dollars

**Answer**:
> Last week, your total ad spend was $65,100.68, which is right on par with the average for your workspace. The standout was the Image Ad - Evening Audience - Website Traffic Push, racking up $755.48 in spend.

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
  "group_by": "ad",
  "breakdown": "ad",
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
        "metric": "spend",
        "operator": ">",
        "value": 200
      }
    ]
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "all ads with spend above 200 dollars",
  "timeframe_description": "last week"
}
```

---

## Test 74: which campaign has the lowest cost per acquisition?

**Answer**:
> The Lead Gen - B2B campaign had the lowest CPA at $1.74 last week—your top performer! For context, your overall CPA was $5.27, which is right at the workspace average.

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
  "group_by": "campaign",
  "breakdown": "campaign",
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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "which campaign has the lowest cost per acquisition?",
  "timeframe_description": "last week"
}
```

---

## Test 75: show me adsets with impressions over 5000

**Answer**:
> You had a total of 5,786,157 impressions last week, which is right on par with your workspace average—pretty steady! The top ad set was the Weekend Audience from the Summer Sale Campaign, pulling in 47,994 impressions.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "impressions",
  "time_range": {
    "last_n_days": 7,
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
    "entity_name": null,
    "metric_filters": [
      {
        "metric": "impressions",
        "operator": ">",
        "value": 5000
      }
    ]
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "show me adsets with impressions over 5000",
  "timeframe_description": "last week"
}
```

---

## Test 76: How is the Summer Sale campaign performing?

**Answer**:
> The Summer Sale campaign brought in $8,636.98 last week—your top performer, but that’s still concerning since it’s below the workspace average of $412,855.54. It looks like it needs some attention to boost those numbers!

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "How is the Summer Sale campaign performing?",
  "timeframe_description": "last week"
}
```

---

## Test 77: Show me all lead gen campaigns

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Show me all lead gen campaigns",
  "timeframe_description": null
}
```

---

## Test 78: What's the CPA for Morning Audience adsets?

**Answer**:
> The CPA for the Morning Audience adsets was $4.94 last week.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's the CPA for Morning Audience adsets?",
  "timeframe_description": "last week"
}
```

---

## Test 79: What's the revenue for Black Friday campaign?

**Answer**:
> Your revenue for the Black Friday campaign was $60,038.80 last week.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's the revenue for Black Friday campaign?",
  "timeframe_description": "last week"
}
```

---

## Test 80: Give me ROAS for App Install campaigns

**Answer**:
> Your ROAS for App Install campaigns was 0.60× last week, which is below the workspace average of 6.34×—that's concerning. The top performer in this category was the App Install Campaign at 0.42×, so there’s definitely room for improvement.

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
    "entity_name": "app install",
    "metric_filters": null
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Give me ROAS for App Install campaigns",
  "timeframe_description": "last week"
}
```

---

## Test 81: Show me Weekend Audience adsets

**Answer**:
> You have a total of 10 ad sets, including campaigns like Weekend Audience - App Install Campaign, Weekend Audience - Black Friday Deals, and Weekend Audience - Summer Sale Campaign.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Show me Weekend Audience adsets",
  "timeframe_description": null
}
```

---

## Test 82: What's the CTR for Evening Audience adsets?

**Answer**:
> The CTR for Evening Audience adsets was 2.5% last week.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's the CTR for Evening Audience adsets?",
  "timeframe_description": "last week"
}
```

---

## Test 83: How much did Holiday Sale campaign spend last week?

**Answer**:
> The Holiday Sale campaign spent $4,402.51 last week.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "How much did Holiday Sale campaign spend last week?",
  "timeframe_description": "last week"
}
```

---

## Test 84: Compare CPC, CTR, and ROAS for Holiday Sale and App Install campaigns last week

**Answer**:
> It looks like there are currently no entities to compare, as the count is 0. If you have specific entities in mind, please let me know!

**DSL**:
```json
{
  "query_type": "comparison",
  "metric": null,
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
  "comparison_type": "entity_vs_entity",
  "comparison_entities": [
    "Holiday Sale",
    "App Install"
  ],
  "comparison_metrics": [
    "cpc",
    "ctr",
    "roas"
  ],
  "question": "Compare CPC, CTR, and ROAS for Holiday Sale and App Install campaigns last week",
  "timeframe_description": "last week"
}
```

---

## Test 85: What's the spend, revenue, and ROAS for all Google campaigns in September?

**Answer**:
> Here are your metrics from 2025-09-01 to 2025-09-30:

• SPEND: $59,714.10
• REVENUE: $395,657.75
• ROAS: 6.63×

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's the spend, revenue, and ROAS for all Google campaigns in September?",
  "timeframe_description": "from 2025-09-01 to 2025-09-30"
}
```

---

## Test 86: Show me clicks, conversions, and cost per conversion for Meta campaigns last 5 days

**Answer**:
> Here are your metrics in the last 5 days:

• CLICKS: 27,438
• CONVERSIONS: 2,500
• CPA: $5.21

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Show me clicks, conversions, and cost per conversion for Meta campaigns last 5 days",
  "timeframe_description": "last 5 days"
}
```

---

## Test 87: Give me CTR, CPC, and conversion rate for Summer Sale campaign last month

**Answer**:
> Here are your metrics in the last 30 days:

• CTR: 3.5%
• CPC: $0.40
• CVR: 4.7%

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
    "entity_name": "summer sale",
    "metric_filters": null
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Give me CTR, CPC, and conversion rate for Summer Sale campaign last month",
  "timeframe_description": "last month"
}
```

---

## Test 88: Compare spend and revenue between Morning Audience and Evening Audience adsets this month to date

**Answer**:
> It looks like there are currently no entities to compare, as the count is 0. Let me know if there's anything else you'd like to explore!

**DSL**:
```json
{
  "query_type": "comparison",
  "metric": null,
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-15"
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
  "comparison_type": "entity_vs_entity",
  "comparison_entities": [
    "Morning Audience",
    "Evening Audience"
  ],
  "comparison_metrics": [
    "spend",
    "revenue"
  ],
  "question": "Compare spend and revenue between Morning Audience and Evening Audience adsets this month to date",
  "timeframe_description": "this month"
}
```

---

## Test 89: What's the ROAS, revenue, and profit for Black Friday campaign last week?

**Answer**:
> Here are your metrics last week:

• ROAS: 11.87×
• REVENUE: $60,038.80
• PROFIT: $18,458.42

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's the ROAS, revenue, and profit for Black Friday campaign last week?",
  "timeframe_description": "last week"
}
```

---

## Test 90: Show me CPC, clicks, and spend for all active campaigns last 5 days

**Answer**:
> Here are your metrics in the last 5 days:

• CPC: $0.44
• CLICKS: 100,630
• SPEND: $44,176.99

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
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 10,
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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Show me CPC, clicks, and spend for all active campaigns last 5 days",
  "timeframe_description": "last 5 days"
}
```

---

## Test 91: Compare CTR and conversion rate for Google vs Meta campaigns in September

**Answer**:
> ERROR

**DSL**:
```json
{}
```

---

## Test 92: What's the revenue, ROAS, and cost per lead for lead gen campaigns this month to date?

**Answer**:
> Here are your metrics from October 01 to 15:

• REVENUE: $35,392.19
• ROAS: 2.30×
• SPEND: $15,378.69

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": [
    "revenue",
    "roas",
    "spend"
  ],
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-15"
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
    "entity_name": "lead gen",
    "metric_filters": null
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's the revenue, ROAS, and cost per lead for lead gen campaigns this month to date?",
  "timeframe_description": "this month"
}
```

---

## Test 93: Give me spend, clicks, and CPC for Holiday Sale and Summer Sale campaigns last month

**Answer**:
> Here are your metrics in the last 30 days:

• SPEND: $29,432.98
• CLICKS: 73,927
• CPC: $0.40

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
  "top_n": 10,
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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Give me spend, clicks, and CPC for Holiday Sale and Summer Sale campaigns last month",
  "timeframe_description": "last month"
}
```

---

## Test 94: Show me conversion rate, revenue, and profit for all campaigns last week

**Answer**:
> Here are your metrics last week:

• CVR: 8.3%
• REVENUE: $412,855.54
• PROFIT: $125,781.71

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Show me conversion rate, revenue, and profit for all campaigns last week",
  "timeframe_description": "last week"
}
```

---

## Test 95: Compare CPA, ROAS, and revenue for App Install campaign vs Holiday Sale campaign last 5 days

**Answer**:
> It looks like there are currently no entities to compare, as the count is 0. Let me know if you need help with anything else!

**DSL**:
```json
{
  "query_type": "comparison",
  "metric": null,
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
    "status": null,
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "comparison_type": "entity_vs_entity",
  "comparison_entities": [
    "App Install",
    "Holiday Sale"
  ],
  "comparison_metrics": [
    "cpa",
    "roas",
    "revenue"
  ],
  "question": "Compare CPA, ROAS, and revenue for App Install campaign vs Holiday Sale campaign last 5 days",
  "timeframe_description": "last 5 days"
}
```

---

## Test 96: What's the CTR, CPC, and conversions for Weekend Audience adsets in September?

**Answer**:
> Here are your metrics from 2025-09-01 to 2025-09-30:

• CTR: 2.5%
• CPC: $0.45
• CONVERSIONS: 7,357

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
  "group_by": "adset",
  "breakdown": "adset",
  "top_n": 10,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "weekend audience",
    "metric_filters": null
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's the CTR, CPC, and conversions for Weekend Audience adsets in September?",
  "timeframe_description": "from 2025-09-01 to 2025-09-30"
}
```

---

## Test 97: Give me spend, revenue, ROAS, and profit for all Meta campaigns this month to date

**Answer**:
> Here are your metrics from October 01 to 15:

• SPEND: $39,036.21
• REVENUE: $353,578.46
• ROAS: 9.06×
• PROFIT: $106,204.92

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
    "end": "2025-10-15"
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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Give me spend, revenue, ROAS, and profit for all Meta campaigns this month to date",
  "timeframe_description": "this month"
}
```

---

## Test 98: Compare clicks, CTR, and cost per click for Morning vs Evening Audience adsets last month

**Answer**:
> It looks like there are no entities to compare at this time, as the count is 0. Let me know if you need help with anything else!

**DSL**:
```json
{
  "query_type": "comparison",
  "metric": null,
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
  "comparison_type": "entity_vs_entity",
  "comparison_entities": [
    "morning audience",
    "evening audience"
  ],
  "comparison_metrics": [
    "clicks",
    "ctr",
    "spend"
  ],
  "question": "Compare clicks, CTR, and cost per click for Morning vs Evening Audience adsets last month",
  "timeframe_description": "last month"
}
```

---

