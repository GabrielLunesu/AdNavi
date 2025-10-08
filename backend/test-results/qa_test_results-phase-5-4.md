# QA Test Results

**Test Run**: Wed Oct  8 17:51:02 CEST 2025
**Workspace**: Defang Labs (a8fef057-4b82-49d7-8049-4257fd9d272b)
**System Version**: Phase 3 (v2.1.3)

---

## Test 1: What's my CPC today?

**Answer**:
> Your CPC is $0.43 today.

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
  "sort_order": "desc",
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
> You spent $6,230.92 yesterday.

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
  "sort_order": "desc",
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
> Your ROAS is 6.14× this week.

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
> Your revenue was $40,376.71 today.

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
  "sort_order": "desc",
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
> You had 97,925 clicks last week.

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
> Your profit was $82,715.08 last week.

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
> You generated 14,443 leads this month.

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
> Your cost per lead is $13.86 this month.

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
> Last week, the Summer Sale Campaign had the highest ROAS at an impressive 13.29×—that's your top performer! Just to give you some context, the average ROAS across your workspace was 6.14×, so this campaign really crushed it.

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
> Your ROAS for Google campaigns only was 6.58× last week.

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
    "status": null
  },
  "thresholds": null,
  "question": "What's my ROAS for Google campaigns only?",
  "timeframe_description": "last week"
}
```

---

## Test 12: Which campaign spent the most yesterday?

**Answer**:
> Yesterday, your total spend was $6,230.92, which is right on par with the workspace average—pretty standard. The top performer was the Lead Gen - B2B campaign, spending $854.52, so it’s doing well within the overall budget.

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
> Last week, your highest CTR was 2.4%, which is right on par with the workspace average. However, the top performer was the "Video Ad - Evening Audience - Lead Gen - B2B" with an impressive 4.3%—that's definitely crushing it!

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
> You have a total of 10 campaigns, including the Holiday Sale - Purchases, Summer Sale Campaign, Black Friday Deals, and several others like the App Install Campaign and Brand Awareness.

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
    "status": null
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
> Last week, your campaigns generated a total of 3,373 leads, which is right on par with the workspace average. The top performer, "Lead Gen - B2B," brought in 2,191 leads, so it’s doing pretty well but there’s definitely room for improvement overall.

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
    "status": null
  },
  "thresholds": null,
  "question": "Which campaign generated the most leads?",
  "timeframe_description": "last week"
}
```

---

## Test 17: Rank platforms by cost per conversion

**Answer**:
> Last week, your cost per conversion was $5.47, which is right on par with the workspace average. Google was your top performer at $4.05, so it’s definitely worth keeping an eye on that platform for better efficiency!

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
    "status": null
  },
  "thresholds": null,
  "question": "Rank platforms by cost per conversion",
  "timeframe_description": "last week"
}
```

---

## Test 18: give me a breakdown of holiday campaign performance

**Answer**:
> ERROR

**DSL**:
```json
{}
```

---

## Test 19: what is my average order value?

**Answer**:
> Your average order value was $33.59 last week.

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
    "status": null
  },
  "thresholds": null,
  "question": "what is my average order value?",
  "timeframe_description": "last week"
}
```

---

## Test 20: How does this week compare to last week?

**Answer**:
> This week, your CPA is $5.47, which is a slight improvement from last week's $5.49—so that's good! You're right at the workspace average too, so it looks like you're performing pretty consistently.

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
  "compare_to_previous": true,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "sort_order": "desc",
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

## Test 21: Compare Google vs Meta performance

**Answer**:
> Last week, your CPA for Google was $5.47, which is right on par with the workspace average—so it's performing pretty average. In comparison, Meta's CPA is higher at $10.07, making Google the more cost-effective option right now.

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
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null
  },
  "thresholds": null,
  "question": "Compare Google vs Meta performance",
  "timeframe_description": "last week"
}
```

---

## Test 22: Is my ROAS improving or declining?

**Answer**:
> Your ROAS was 6.14× last week, which is an improvement of 2.4% from 5.99× the week before—that's a nice little bump! Plus, you're right on par with the workspace average, so you're doing pretty well overall.

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
    "status": null
  },
  "thresholds": null,
  "question": "Is my ROAS improving or declining?",
  "timeframe_description": "last week"
}
```

---

## Test 23: Which campaign had the highest ROAS last week?

**Answer**:
> Last week, the Summer Sale Campaign had the highest ROAS at an impressive 13.29×—that's your top performer! Just for context, your overall ROAS was 6.14×, which matches the workspace average, so the Summer Sale really stood out.

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
    "status": null
  },
  "thresholds": null,
  "question": "Which campaign had the highest ROAS last week?",
  "timeframe_description": "last week"
}
```

---

## Test 24: Show me top 5 campaigns by revenue

**Answer**:
> Last week, your total revenue was $278,056.46, which is right on par with the workspace average—so that's solid. The top performer was the Summer Sale Campaign, bringing in $63,049.54, making it your best campaign. Overall, it looks like you're maintaining a steady performance!

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
    "status": null
  },
  "thresholds": null,
  "question": "Show me top 5 campaigns by revenue",
  "timeframe_description": "last week"
}
```

---

## Test 25: List all active campaigns

**Answer**:
> You have 10 active campaigns, including the Holiday Sale - Purchases, Summer Sale Campaign, Black Friday Deals, and more.

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
    "status": "active"
  },
  "thresholds": null,
  "question": "List all active campaigns",
  "timeframe_description": null
}
```

---

## Test 26: Which adset had the highest cpc last week?

**Answer**:
> Last week, the ad set "Evening Audience - Black Friday Deals" had the highest CPC at $0.67, which is right at the average for your workspace of $0.46. That means it’s definitely struggling a bit compared to the rest. You might want to keep an eye on it!

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
    "status": null
  },
  "thresholds": null,
  "question": "Which adset had the highest cpc last week?",
  "timeframe_description": "last week"
}
```

---

## Test 27: Which adset had the lowest ctr last week?

**Answer**:
> Last week, the ad set with the lowest CTR was "Morning Audience - General Conversions" at 1.5%, which is right at the bottom compared to the workspace average of 2.4%. That means it’s struggling a bit, so it might need some attention to boost its performance.

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
    "status": null
  },
  "thresholds": null,
  "question": "Which adset had the lowest ctr last week?",
  "timeframe_description": "last week"
}
```

---

## Test 28: Which adset had the highest ctr last week?

**Answer**:
> Last week, the ad set "Weekend Audience - Website Traffic Push" had the highest CTR at 3.7%, which is really solid compared to the workspace average of 2.4%. That means it’s definitely your top performer in terms of engagement!

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
  "sort_order": "desc",
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

## Test 29: Which adset had the lowest cpc last week?

**Answer**:
> Last week, your CPC was $0.46, which is right on par with the workspace average. However, the Weekend Audience from the Summer Sale Campaign was your top performer at just $0.35—definitely worth noting!

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
  "sort_order": "asc",
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

## Test 30: Which adset had the highest cpc last week?

**Answer**:
> Last week, the ad set "Evening Audience - Black Friday Deals" had the highest CPC at $0.67, which is right at the top compared to the workspace average of $0.46. That means it was your worst performer in terms of cost efficiency. It's definitely something to keep an eye on!

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
    "status": null
  },
  "thresholds": null,
  "question": "Which adset had the highest cpc last week?",
  "timeframe_description": "last week"
}
```

---

## Test 31: Which adset had the lowest ctr last week?

**Answer**:
> Last week, the ad set with the lowest CTR was "Morning Audience - General Conversions" at 1.5%, which is right at the bottom compared to the workspace average of 2.4%. It looks like it’s struggling a bit, so that’s something to keep an eye on.

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
    "status": null
  },
  "thresholds": null,
  "question": "Which adset had the lowest ctr last week?",
  "timeframe_description": "last week"
}
```

---

## Test 32: what is my total CVR last month?

**Answer**:
> Your CVR was 8.3% last month.

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
    "status": null
  },
  "thresholds": null,
  "question": "what is my total CVR last month?",
  "timeframe_description": "last month"
}
```

---

## Test 33: What's my ROAS for active campaigns?

**Answer**:
> Your ROAS was 5.82× last week.

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
    "status": "active"
  },
  "thresholds": null,
  "question": "What's my ROAS for active campaigns?",
  "timeframe_description": "last week"
}
```

---

## Test 34: How much did I spend on Meta ads?

**Answer**:
> You spent $12,904.38 on Meta ads last week.

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
    "status": null
  },
  "thresholds": null,
  "question": "How much did I spend on Meta ads?",
  "timeframe_description": "last week"
}
```

---

## Test 35: How much revenue on Google last week?

**Answer**:
> Your revenue was $120,216.88 last week.

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
    "status": null
  },
  "thresholds": null,
  "question": "How much revenue on Google last week?",
  "timeframe_description": "last week"
}
```

---

## Test 36: What's my cost per install?

**Answer**:
> Your cost per install was $26.92 last week.

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
    "status": null
  },
  "thresholds": null,
  "question": "What's my cost per install?",
  "timeframe_description": "last week"
}
```

---

## Test 37: How many leads did I generate today?

**Answer**:
> You generated 509 leads today.

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
    "status": null
  },
  "thresholds": null,
  "question": "How many leads did I generate today?",
  "timeframe_description": "today"
}
```

---

## Test 38: wich ad had the lowest cpc last week?

**Answer**:
> Last week, the ad with the lowest CPC was the Carousel Ad targeting the Evening Audience at just $0.31—your best performer! That’s significantly better than the average CPC of $0.46 for the week, so it really stood out.

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
    "status": null
  },
  "thresholds": null,
  "question": "wich ad had the lowest cpc last week?",
  "timeframe_description": "last week"
}
```

---

## Test 39: What time on average do i get the best cpc?

**Answer**:
> Last week, your average CPC was $0.46, which is right on par with the workspace average. So, it looks like you're performing at an average level compared to others. Nothing to worry about, but it might be worth keeping an eye on!

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
    "status": null
  },
  "thresholds": null,
  "question": "What time on average do i get the best cpc?",
  "timeframe_description": "last week"
}
```

---

## Test 40: how much revenue would i have last week if my cpc was 0.20?

**Answer**:
> Your revenue was $278,056.46 last week.

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
    "status": null
  },
  "thresholds": null,
  "question": "how much revenue would i have last week if my cpc was 0.20?",
  "timeframe_description": "last week"
}
```

---

## Test 41: 

**Answer**:
> ERROR

**DSL**:
```json
{}
```

---

