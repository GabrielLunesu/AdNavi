# QA Test Results

**Test Run**: Mon Oct 13 14:30:50 CEST 2025
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
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-13"
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
> You spent $114,830.27 this month.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "spend",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-13"
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
> You generated 8,404 leads this month.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "leads",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-13"
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
> Your cost per lead this month is $13.66.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpl",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-13"
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
> The Holiday Sale - Purchases had the highest ROAS last week at an impressive 13.36×—your top performer! For context, your overall ROAS was 6.15×, which matches the workspace average. That's a solid result, but this campaign really stood out!

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
> Your ROAS for Google campaigns only was 6.15× last week.

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
> It looks like there wasn't any spend yesterday, so no campaign spent the most—just an average day overall. If you're looking to boost your spending, it might be worth checking in on your campaigns to see where you can invest!

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
> You have a total of 10 active campaigns, including the Holiday Sale - Purchases, Summer Sale Campaign, Black Friday Deals, and others like the App Install Campaign and Brand Awareness.

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
> The Video Ad - Morning Audience - Lead Gen - B2B had the highest CTR at 4.2% last week—your top performer! For context, your overall CTR was 2.6%, which is right on par with the workspace average.

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
> The Lead Gen - B2B campaign generated the most leads last week with 2,704—your top performer! For context, your overall leads were 4,288, which is right at the average for your workspace.

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
> Google had the lowest cost per conversion at $4.37 last week, making it the top performer among your platforms. In comparison, your overall CPA was $5.43, which is right at the workspace average. So, Google’s doing a bit better than the rest!

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
  "top_n": 5,
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
> Your holiday campaign brought in $52,634.16 last week, which is below the workspace average of $355,398.23—definitely something to keep an eye on. Interestingly, the Holiday Sale - Purchases was your top performer, but overall, the performance level is concerning.

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
> You have five entities to work with: Holiday Sale - Purchases, Summer Sale Campaign, Black Friday Deals, App Install Campaign, and Mobile Game Installs.

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
> ERROR

**DSL**:
```json
{}
```

---

## Test 23: roas last month for holiday sale campaign?

**Answer**:
> Your ROAS for the Holiday Sale campaign was 11.80× last month—pretty impressive! For some context, that's well above the workspace average of 6.40×, so it really stood out.

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
> Your revenue this month is $725,481.04.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "revenue",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-13"
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
> Last month, Google had a ROAS of 6.40×, which is right on par with the workspace average. Meanwhile, Meta was your top performer, crushing it with a ROAS of 9.42×. So, while Google’s doing okay, Meta's really leading the pack!

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
> Your ROAS was 6.15× last week, which is a decline of about 4.7% from 6.45× the week before. It's sitting right at the average for your workspace, so it’s not too far off the mark. Overall, it seems like it could use a little boost!

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
> No ROAS data available for last month.

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
> The Holiday Sale - Purchases had the highest ROAS at 13.36× last week—your top performer! For context, your overall ROAS was 6.15×, which matches the workspace average. That's a solid result!

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
> The Summer Sale Campaign was your top performer last week, bringing in $85,108.72. Overall, your total revenue was $355,398.23, which matches the workspace average—so you're right on track!

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
> You have a total of 10 active campaigns, including the Holiday Sale - Purchases, Summer Sale Campaign, Black Friday Deals, and more.

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
> The Weekend Audience - Black Friday Deals had the highest CPC at $0.64 last week—your worst performer. For context, your overall CPC was $0.45, which is right at the average for your workspace.

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
> The Weekend Audience - Black Friday Deals had the highest CPC at $0.64 last week—definitely your worst performer. For context, your overall CPC was $0.45, which matches the workspace average, so this adset really stood out in the wrong way.

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
> The Morning Audience - General Conversions had the lowest CTR at 1.7% last week—definitely needs some attention. For context, your overall CTR was 2.6%, which matches the workspace average.

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
> The Image Ad - Weekend Audience - Website Traffic Push had the lowest CPC at $0.28 last week—your top performer! For context, your overall CPC was $0.45, which is right at the average for the workspace.

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
> ERROR

**DSL**:
```json
{}
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
  "question": "",
  "timeframe_description": "last week"
}
```

---

## Test 50: How is the Summer Sale campaign performing?

**Answer**:
> The Summer Sale campaign brought in $6,190.20 last week, which is below the workspace average of $355,398.23—definitely concerning. It seems like it’s not quite hitting the mark compared to what you usually see.

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
> You're currently running one campaign, which is named "Lead Gen - B2B."

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
> Your CPA for the Morning Audience adsets was $4.83 last week.

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
> The revenue for the Black Friday campaign was $49,130.30 last week.

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
> Your ROAS for App Install campaigns was 0.64× last week, which is below the workspace average of 6.15×—that's concerning. It looks like this campaign is currently your top performer, but it still has a long way to go to catch up with the average.

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
> Your CTR for Evening Audience adsets was 2.5% last week.

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
    "entity_name": "Evening Audience"
  },
  "thresholds": null,
  "question": "What's the CTR for Evening Audience adsets?",
  "timeframe_description": "last week"
}
```

---

## Test 57: How much did Holiday Sale campaign spend last week?

**Answer**:
> The Holiday Sale campaign spent $3,939.79 last week.

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
> ERROR

**DSL**:
```json
{}
```

---

## Test 60: Show me clicks, conversions, and cost per conversion for Meta campaigns last 5 days

**Answer**:
> ERROR

**DSL**:
```json
{}
```

---

## Test 61: Give me CTR, CPC, and conversion rate for Summer Sale campaign last month

**Answer**:
> ERROR

**DSL**:
```json
{}
```

---

## Test 62: Compare spend and revenue between Morning Audience and Evening Audience adsets this month to date

**Answer**:
> The Morning Audience ad set hasn't spent anything this month, which is concerning since the average spend across the workspace is about $114,830.27—so it's definitely below average. It might be worth looking into why it's not performing as expected.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "spend",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-13"
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
> The Black Friday campaign had an impressive ROAS of 10.22× last week, making it your top performer! For some context, that's well above the workspace average of 6.15×—great job!

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
> Your CPC was $0.45 over the last 5 days, which is slightly better than the workspace average of $0.46. The top performer, Black Friday Deals, had a CPC of $0.54, so you're doing pretty well overall!

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
  "top_n": 10,
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
> In September, Google had a CTR of 3.5%, which is above the workspace average of 2.5%, while Meta matched that average with a CTR of 2.5%. So, Google’s definitely leading in engagement this month! Overall, both platforms performed at the average level, but Google really stood out.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "ctr",
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
    "entity_name": null
  },
  "thresholds": null,
  "question": "Compare CTR and conversion rate for Google vs Meta campaigns in September",
  "timeframe_description": "from 2025-09-01 to 2025-09-30"
}
```

---

## Test 66: What's the revenue, ROAS, and cost per lead for lead gen campaigns this month to date?

**Answer**:
> Your revenue is $2,064.52 this month.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "revenue",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-13"
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
> The Holiday Sale campaign had a spend of $0 last month, which is concerning since that's below the workspace average of about $275,259. The Summer Sale also didn’t spend anything, so both campaigns really need to ramp up their budgets to be competitive.

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
> Last week, your overall conversion rate was 8.4%, which matches the workspace average—so you're right on track! The top performer was the Lead Gen - B2B campaign, crushing it with a conversion rate of 17.5%.

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
> No cost per acquisition data available for last 5 days.

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
  "top_n": 10,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "app install, holiday sale"
  },
  "thresholds": null,
  "question": "Compare CPA, ROAS, and revenue for App Install campaign vs Holiday Sale campaign last 5 days",
  "timeframe_description": "last 5 days"
}
```

---

## Test 70: What's the CTR, CPC, and conversions for Weekend Audience adsets in September?

**Answer**:
> In September, the Weekend Audience adsets had a CTR of 2.6%, which is pretty much in line with the workspace average of 2.5%. Your top performer was the Weekend Audience - Summer Sale Campaign, hitting 3.6%—that's a solid showing!

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "ctr",
  "time_range": {
    "last_n_days": null,
    "start": "2025-09-01",
    "end": "2025-09-30"
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
    "entity_name": "weekend audience"
  },
  "thresholds": null,
  "question": "What's the CTR, CPC, and conversions for Weekend Audience adsets in September?",
  "timeframe_description": "from 2025-09-01 to 2025-09-30"
}
```

---

## Test 71: Give me spend, revenue, ROAS, and profit for all Meta campaigns this month to date

**Answer**:
> This month to date, your spend on Meta campaigns is $31,037.16, which is below the workspace average of $114,830.27—definitely something to keep an eye on. The top performer is the Black Friday Deals campaign, bringing in $9,057.84.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "spend",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-13"
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
> No click-through rate data available for last month.

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
  "group_by": "adset",
  "breakdown": "adset",
  "top_n": 10,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "morning evening audience"
  },
  "thresholds": null,
  "question": "Compare clicks, CTR, and cost per click for Morning vs Evening Audience adsets last month",
  "timeframe_description": "last month"
}
```

---

