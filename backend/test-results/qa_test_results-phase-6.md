# QA Test Results

**Test Run**: Wed Oct 15 16:25:39 CEST 2025
**Workspace**: Defang Labs (4449fa5d-746d-4aa0-b446-28df32deb1e6)
**System Version**: Phase 5 (v2.1.3)

---

## Test 1: What's my CPC this month?

**Answer**:
> Your CPC is $0.45 from October 01 to 15.

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

## Test 16: Which campaign generated the most leads?

**Answer**:
> The Website Traffic Push campaign generated the most leads last week with 5,021—your top performer! Interestingly, this was right on par with your overall average, showing consistent performance across the board.

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

## Test 2: How much did I spend this month?

**Answer**:
> You spent $145,570.10 from October 01 to 15.

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

## Test 17: Rank platforms by cost per conversion

**Answer**:
> Google had the lowest CPA at $4.17 last week, making it the most cost-effective platform. Overall, your CPA was $5.39, which was right on average for your workspace.

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

## Test 57: all adsets with clicks above 500

**Answer**:
> Here are the ad sets from last week that had more than 500 clicks:

1. **Weekend Audience - Summer Sale Campaign**: This ad set achieved 2,183 clicks with a spend of $784.94, resulting in a revenue of $14,235.14 from 55,885 impressions.

2. **Evening Audience - App Install Campaign**: Garnering 1,781 clicks, this ad set spent $523.15 and generated $392.02 in revenue from 41,256 impressions.

3. **Weekend Audience - Lead Gen - B2B**: With 1,765 clicks, it had a spend of $751.74 and brought in $1,773.62 in revenue from 50,470 impressions.

4. **Weekend Audience - App Install Campaign**: This ad set recorded 1,629 clicks, spending $660.00 and earning $204.28 in revenue from 41,686 impressions.

5. **Evening Audience - Lead Gen - B2B**: It achieved 1,581 clicks, with a spend of $830.75 and revenue of $588.60 from 53,508 impressions.

6. **Weekend Audience - Website Traffic Push**: This ad set had 1,571 clicks, spending $733.31 and generating $4,904.92 in revenue from 43,164 impressions.

7. **Morning Audience - App Install Campaign**: With 1,529 clicks, this ad set spent $559.06 and earned $456.77 in revenue from 48,835 impressions.

8. **Morning Audience - Website Traffic Push**: This ad set achieved 1,524 clicks, with a spend of $613.02 and revenue of $5,827.42 from 38,708 impressions.

9. **Evening Audience - Website Traffic Push**: It recorded 1,436 clicks, spending $506.29 and generating $6,339.68 in revenue from 36,894 impressions.

10. **Morning Audience - Summer Sale Campaign**: This ad set had 1,402 clicks, with a spend of $606.72 and revenue of $11,226.30 from 42,125 impressions.

In total, there are 10 ad sets that exceeded 500 clicks last week.

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

## Test 3: What's my ROAS this week?

**Answer**:
> Your ROAS is 5.71× this week.

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
> Your revenue was $58,024.67 yesterday.

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

## Test 58: which ad has the lowest cost per conversion?

**Answer**:
> The Video Ad - Evening Audience - Lead Gen - B2B had the lowest cost per conversion at $1.90 last week—your best performer! For context, your overall CPA was $5.39, so this ad really stood out.

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

## Test 18: give me a breakdown of holiday campaign performance

**Answer**:
> Here's a breakdown of the holiday campaign performance from last week:

1. **Holiday Sale - Purchases**: This campaign generated $4,901.60 in revenue. It involved a spend of $399.70, resulting in 716 clicks and 36 conversions. The campaign reached an audience with 41,856 impressions.

Overall, there was 1 item in the breakdown for this period.

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
    "entity_name": "Holiday",
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
> Your average order value was $32.79 last week.

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

## Test 59: show me campaigns with impressions over 10000

**Answer**:
> The "Website Traffic Push" campaign had 40,866 impressions last week, leading the pack among your campaigns. Overall, your campaigns averaged 5,892,857 impressions, so you're right on track with your goals.

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

## Test 6: How many clicks did I get last week?

**Answer**:
> You received 151,658 clicks last week.

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

## Test 60: worst performing adset by roas

**Answer**:
> The Weekend Audience - App Install Campaign had the lowest ROAS at 0.31× last week—your worst performer. For context, your overall ROAS was 6.09×, so this campaign really needs some attention.

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

## Test 20: give me a list of the top 5 adsets last week by revenue

**Answer**:
> Here's a list of the top 5 ad sets from last week based on revenue:

1. **Weekend Audience - Summer Sale Campaign**: This ad set generated $14,235.14 in revenue. It had a spend of $784.94, with 2,183 clicks and 105 conversions from 55,885 impressions.

2. **Morning Audience - Summer Sale Campaign**: Bringing in $11,226.30, this ad set had a spend of $606.72. It achieved 1,402 clicks and 78 conversions from 42,125 impressions.

3. **Evening Audience - Holiday Sale - Purchases**: This ad set earned $6,991.09 in revenue. It spent $414.67, received 1,045 clicks, and resulted in 58 conversions from 45,646 impressions.

4. **Evening Audience - Website Traffic Push**: With a revenue of $6,339.68, this ad set had a spend of $506.29. It garnered 1,436 clicks and 102.91 conversions from 36,894 impressions.

5. **Evening Audience - Summer Sale Campaign**: This ad set generated $6,234.97 in revenue. It spent $512.17, with 1,263 clicks and 56 conversions from 37,010 impressions.

These five ad sets were the top performers in terms of revenue last week.

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

## Test 7: How much profit did I make last week?

**Answer**:
> Your profit was $124,905.04 last week.

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

## Test 61: all ads with ctr above 3%

**Answer**:
> No data available for last week.

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

## Test 21: What was the revenue for the Holiday Sale campaign last week?

**Answer**:
> The revenue for the Holiday Sale campaign was $62,227.59 last week.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What was the revenue for the Holiday Sale campaign last week?",
  "timeframe_description": "last week"
}
```

---

## Test 8: How many leads did I generate this month?

**Answer**:
> You generated 10,388 leads from October 01 to 15.

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
> Your cost per lead is $14.01 from October 01 to 15.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpl",
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

## Test 62: which campaign generated the most leads?

**Answer**:
> The Website Traffic Push campaign generated the most leads last week, but it was actually at 0, which matches your workspace average. It seems like there might be a data hiccup since both are showing as average, so it might be worth double-checking the numbers.

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

## Test 10: Which campaign had the highest ROAS last week?

**Answer**:
> The Black Friday Deals campaign had the highest ROAS at 20.20× last week—crushing it as your top performer! For a bit of context, your overall ROAS was 6.09×, so this campaign really stood out.

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
> Your ROAS for Google campaigns was 6.50× last week.

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

## Test 63: show me adsets with spend below 50 dollars

**Answer**:
> Last week, your ad sets with spend below $50 were performing at an average level. Overall, your total spend was $68,093.49, which matched the workspace average. So, while some ad sets were more budget-friendly, your overall spending was right on par with the usual.

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

## Test 12: Which campaign spent the most yesterday?

**Answer**:
> The Brand Awareness campaign spent the most yesterday at $159.59—your top performer! Interestingly, this was right on par with your overall average spend of $9,894.47 across campaigns.

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

## Test 64: best performing ad by revenue per click

**Answer**:
> The Image Ad - Weekend Audience - Summer Sale Campaign had the highest ARPV at $4.28 last week, which was your top performer! For context, your overall ARPV was $3.80, so this ad really stood out.

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

## Test 13: List all active campaigns

**Answer**:
> You currently have 10 active campaigns, including App Install Campaign, Black Friday Deals, and Summer Sale Campaign, among others.

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
> The Carousel Ad - Morning Audience - Summer Sale Campaign had the highest CTR at 4.4% last week—your top performer! For context, your overall CTR was 2.6%, so this ad is really standing out.

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

## Test 65: all campaigns with cpm under 10 dollars

**Answer**:
> Here are all the campaigns from last week with a CPM under $10:

1. **Holiday Sale - Purchases**: This campaign had a CPM of $9.55. With a spend of $399.70, it generated 716 clicks and 36 conversions, bringing in a revenue of $4,901.60 from 41,856 impressions.

2. **Product Launch Teaser**: Achieving a CPM of $8.76, this campaign spent $254.09. It garnered 465 clicks and 14.98 conversions, resulting in $575.26 in revenue from 29,001 impressions.

3. **Black Friday Deals**: With a CPM of $8.29, this campaign spent $357.03. It attracted 978 clicks and 60 conversions, generating a revenue of $7,213.10 from 43,075 impressions.

4. **General Conversions**: This campaign had the lowest CPM at $8.21. It spent $335.89, received 784 clicks, and achieved 69.76 conversions, resulting in $3,940.91 in revenue from 40,906 impressions.

In total, there are four campaigns that met the criteria of having a CPM under $10.

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
> The "Evening Audience - Lead Gen - B2B" adset had the highest conversion rate at 18.7% last week—crushing it as your top performer! For context, your overall conversion rate was 8.3%, so this adset really stood out.

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

## Test 15: Show me campaigns with ROAS above 4

**Answer**:
> Your campaigns had an average ROAS of 6.09× last week. The standout was the "Black Friday Deals" campaign, crushing it with a ROAS of 20.20×. Overall, your performance was steady, matching the workspace average.

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

## Test 67: show me ads with conversions above 20

**Answer**:
> The Image Ad - Weekend Audience - Lead Gen - B2B had 337 conversions last week, which was above the 20 conversions threshold you were interested in. Overall, your ads averaged 12,635 conversions last week, so this ad was performing right in line with your average.

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

## Test 16: Which campaign generated the most leads?

**Answer**:
> The "Website Traffic Push" campaign generated the most leads last week, but it actually didn't produce any leads, which is surprising. Overall, your lead generation was right at the average with 5,021 leads.

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
> Google had the lowest cost per conversion at $4.17 last week, leading the pack. Overall, your average CPA across platforms was $5.39, so Google was performing better than average.

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

## Test 68: worst performing campaign by cost per lead

**Answer**:
> The Product Launch Teaser campaign had a CPL of $13.56 last week, which was right at the average for your workspace. While it wasn't the worst performer, it also didn't stand out as the best.

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

## Test 18: give me a breakdown of holiday campaign performance

**Answer**:
> Here's a quick look at how our holiday campaign performed over the last week:

- **Holiday Sale - Purchases**: This campaign generated a revenue of $4,901.60. We spent $399.70 on it, which resulted in 716 clicks and 36 conversions. The campaign reached 41,856 impressions.

Overall, we analyzed 1 item in this breakdown. Let me know if you need more details!

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
    "entity_name": "Holiday",
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

## Test 69: all adsets with revenue above 5000

**Answer**:
> Here are all the ad sets from last week that generated revenue above $5,000:

1. **Weekend Audience - Summer Sale Campaign**: This ad set brought in $14,235.14 in revenue.
2. **Morning Audience - Summer Sale Campaign**: It generated $11,226.30 in revenue.
3. **Evening Audience - Holiday Sale - Purchases**: This ad set achieved $6,991.09 in revenue.
4. **Evening Audience - Website Traffic Push**: It earned $6,339.68 in revenue.
5. **Evening Audience - Summer Sale Campaign**: This ad set made $6,234.97 in revenue.
6. **Weekend Audience - Holiday Sale - Purchases**: It collected $6,063.21 in revenue.
7. **Morning Audience - Website Traffic Push**: This ad set generated $5,827.42 in revenue.
8. **Morning Audience - Blog Content Promotion**: It brought in $5,784.62 in revenue.
9. **Morning Audience - Holiday Sale - Purchases**: This ad set achieved $5,212.57 in revenue.

In total, there are 9 ad sets that surpassed the $5,000 revenue mark last week.

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

## Test 19: what is my average order value?

**Answer**:
> Your average order value was $32.79 last week.

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

## Test 70: which ad has the best profit margin?

**Answer**:
> The Image Ad - Weekend Audience - Summer Sale Campaign had the best profit margin with a POAS of 2.90× last week—it's really leading the pack! For context, your overall average POAS was 1.83×, so this ad is definitely standing out.

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

## Test 20: give me a list of the top 5 adsets last week by revenue

**Answer**:
> Here are the top 5 ad sets from last week based on revenue:

1. **Weekend Audience - Summer Sale Campaign**: This ad set generated $14,235.14 in revenue. It had a spend of $784.94 and achieved 105 conversions from 2,183 clicks.

2. **Morning Audience - Summer Sale Campaign**: Bringing in $11,226.30 in revenue, this ad set had a spend of $606.72 with 78 conversions from 1,402 clicks.

3. **Evening Audience - Holiday Sale - Purchases**: This ad set earned $6,991.09 in revenue. It spent $414.67 and resulted in 58 conversions from 1,045 clicks.

4. **Evening Audience - Website Traffic Push**: With a revenue of $6,339.68, this ad set had a spend of $506.29 and achieved 102.91 conversions from 1,436 clicks.

5. **Evening Audience - Summer Sale Campaign**: This ad set generated $6,234.97 in revenue, spending $512.17 and resulting in 56 conversions from 1,263 clicks.

These ad sets were the top performers in terms of revenue last week, with a total of five ad sets analyzed.

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
> The revenue for the Holiday Sale campaign was $62,227.59 last week.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What was the revenue for the Holiday Sale campaign last week?",
  "timeframe_description": "last week"
}
```

---

## Test 71: show me campaigns with clicks over 1000

**Answer**:
> The "Website Traffic Push" campaign had the most clicks at 1,520 last week. Overall, your clicks were right on the average at 151,658. It's consistent with what you've been seeing across your campaigns.

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

## Test 22: wich day had the lowest cpc on holiday sale campaign?

**Answer**:
> The day with the lowest CPC for your holiday sale campaign was October 9, at $0.42—your best performer last week! For context, your overall CPC was $0.47, which is slightly above the workspace average of $0.45.

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

## Test 72: best performing adset by average order value

**Answer**:
> The Evening Audience - Lead Gen - B2B ad set had the lowest AOV at $2.00 last week, making it your worst performer. For context, your overall AOV was $32.79, so this ad set really needs some attention.

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

## Test 23: roas last month for holiday sale campaign?

**Answer**:
> The Holiday Sale campaign had a ROAS of 11.84× in the last 30 days, which is excellent! That's well above your workspace average of 6.29×.

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
> In the last week, the Holiday Sale campaign had a higher cost-per-click (CPC) compared to the App Install campaign. Specifically, the Holiday Sale campaign's CPC was approximately $0.47, while the App Install campaign's CPC was about $0.38. This means that the Holiday Sale campaign was more expensive per click than the App Install campaign during this period.

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

## Test 73: all ads with spend above 200 dollars

**Answer**:
> Here are all the ads from last week that had a spend above $200:

1. **Image Ad - Weekend Audience - Summer Sale Campaign**: This ad had a spend of $800.61.
2. **Image Ad - Weekend Audience - Lead Gen - B2B**: The spend here was $737.36.
3. **Image Ad - Evening Audience - Lead Gen - B2B**: This ad spent $703.09.
4. **Carousel Ad - Weekend Audience - App Install Campaign**: The spend was $696.38.
5. **Image Ad - Morning Audience - Mobile Game Installs**: This ad had a spend of $650.60.
6. **Carousel Ad - Evening Audience - App Install Campaign**: The spend here was $644.36.
7. **Carousel Ad - Morning Audience - Brand Awareness**: This ad spent $625.21.
8. **Image Ad - Evening Audience - Summer Sale Campaign**: The spend was $616.53.
9. **Image Ad - Morning Audience - Brand Awareness**: This ad had a spend of $613.98.
10. **Video Ad - Morning Audience - Lead Gen - B2B**: The spend here was $612.88.

In total, there were 10 ads that each had a spend above $200 last week.

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

## Test 25: wich google campaigns are live?

**Answer**:
> You're currently running four active campaigns: App Install Campaign, Lead Gen - B2B, Summer Sale Campaign, and Website Traffic Push.

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

## Test 74: which campaign has the lowest cost per acquisition?

**Answer**:
> The "Lead Gen - B2B" campaign had the lowest CPA at $2.15 last week—your best performer! For context, your overall CPA was $5.39, so this campaign is really leading the pack.

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

## Test 26: what is my revenue this month?

**Answer**:
> Your revenue is $898,335.06 from October 01 to 15.

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
> Your revenue was $1,806,384.84 in the last 30 days.

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

## Test 75: show me adsets with impressions over 5000

**Answer**:
> The "Evening Audience - Lead Gen - B2B" ad set had the highest impressions at 53,508 last week. Overall, your ad sets averaged 5,892,857 impressions, which is pretty consistent across the board.

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

## Test 28: what is my revenue this year?

**Answer**:
> Your revenue was $1,806,384.84 in the last 365 days.

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

## Test 76: How is the Summer Sale campaign performing?

**Answer**:
> The Summer Sale campaign had a ROAS of 13.72× last week, which is more than double the workspace average of 6.09×—that's excellent! It's really standing out with such a strong performance.

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
    "level": "campaign",
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

## Test 29: How does this week compare to last week?

**Answer**:
> ERROR

**DSL**:
```json
{}
```

---

## Test 77: Show me all lead gen campaigns

**Answer**:
> You're currently running one campaign named "Lead Gen - B2B."

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
> The CPA for Morning Audience adsets was $5.53 last week.

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

## Test 30: Compare Google vs Meta performance

**Answer**:
> In the last 30 days, when comparing the performance of Google and Meta based on the Return on Ad Spend (ROAS), Meta has outperformed Google. Meta achieved a ROAS of 8.83, which is notably higher than Google's ROAS of 6.78. This indicates that for every dollar spent on advertising, Meta generated more revenue compared to Google during this period.

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
    "roas"
  ],
  "question": "Compare Google vs Meta performance",
  "timeframe_description": "last month"
}
```

---

## Test 79: What's the revenue for Black Friday campaign?

**Answer**:
> The revenue for the Black Friday campaign was $47,334.78 last week.

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
    "entity_name": "Black Friday Deals",
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

## Test 31: Is my ROAS improving or declining?

**Answer**:
> Your ROAS was 6.09× last week, which is pretty much on par with your workspace average. However, it did decline slightly by 1.5% from 6.18× the week before. So, it's holding steady overall but with a small dip.

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

## Test 80: Give me ROAS for App Install campaigns

**Answer**:
> Here's the ROAS for your App Install campaigns from last week:

- **App Install Campaign**: The ROAS was 0.27. With a spend of $260.93, this campaign generated $71.24 in revenue. It had 658 clicks, 55 conversions, and 19,652 impressions.

This breakdown includes all the data for your App Install campaigns during this period. Let me know if you need more details!

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
    "entity_name": "App Install Campaign",
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

## Test 32: compare holiday campaign performance to app install campaign performance

**Answer**:
> In comparing the performance of the Holiday Sale campaign to the App Install campaign over the past week, we can see some significant differences across key metrics.

Firstly, looking at Return on Ad Spend (ROAS), the Holiday Sale campaign significantly outperformed the App Install campaign. The Holiday Sale achieved a ROAS of 12.63, meaning it generated $12.63 for every dollar spent. In contrast, the App Install campaign had a ROAS of just 0.56, indicating it earned only $0.56 per dollar spent.

When it comes to revenue, the Holiday Sale campaign again takes the lead, generating $62,227.59. This is substantially higher than the $3,897.62 brought in by the App Install campaign.

In terms of spend, the App Install campaign spent more, with a total spend of $7,002.07, compared to the Holiday Sale campaign's $4,928.43.

Overall, the Holiday Sale campaign was more efficient and effective, delivering higher returns and revenue with less spend compared to the App Install campaign.

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
    "roas",
    "revenue",
    "spend"
  ],
  "question": "compare holiday campaign performance to app install campaign performance",
  "timeframe_description": "last week"
}
```

---

## Test 81: Show me Weekend Audience adsets

**Answer**:
> You're running 10 adsets, including Weekend Audience - App Install Campaign, Black Friday Deals, and Brand Awareness.

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
    "entity_name": "Weekend Audience",
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

## Test 33: Which campaign had the highest ROAS last week?

**Answer**:
> The "Black Friday Deals" campaign had the highest ROAS at 20.20× last week—crushing it! For context, your overall ROAS was 6.09×, so this campaign really stood out.

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

## Test 82: What's the CTR for Evening Audience adsets?

**Answer**:
> The CTR for Evening Audience adsets was 2.6% last week.

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
    "entity_name": "Evening Audience",
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

## Test 34: Show me top 5 campaigns by revenue

**Answer**:
> Here are the top 5 campaigns by revenue from last week:

1. **Black Friday Deals**: This campaign generated the highest revenue, bringing in $7,213.10.

2. **Summer Sale Campaign**: Close behind, this campaign earned $6,831.15 in revenue.

3. **Website Traffic Push**: This effort resulted in $4,998.02 in revenue.

4. **Holiday Sale - Purchases**: This campaign brought in $4,901.60.

5. **Blog Content Promotion**: Rounding out the list, this campaign generated $4,287.43.

In total, these five campaigns were the top performers in terms of revenue last week.

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

## Test 83: How much did Holiday Sale campaign spend last week?

**Answer**:
> The Holiday Sale campaign spent $4,928.43 last week.

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

## Test 35: List all active campaigns

**Answer**:
> You have 10 active campaigns, including App Install Campaign, Black Friday Deals, Brand Awareness, and Summer Sale Campaign, among others.

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

## Test 84: Compare CPC, CTR, and ROAS for Holiday Sale and App Install campaigns last week

**Answer**:
> Last week, when comparing the Holiday Sale and App Install campaigns, we can see distinct differences in their performance across key metrics.

Starting with CPC (Cost Per Click), the App Install campaign had a lower CPC at $0.38 compared to the Holiday Sale campaign, which was at $0.47. This indicates that the App Install campaign was more cost-effective in terms of attracting clicks.

In terms of CTR (Click-Through Rate), the App Install campaign also outperformed the Holiday Sale campaign. It achieved a CTR of 3.56%, whereas the Holiday Sale campaign had a lower CTR of 2.06%. This suggests that the App Install campaign was more successful in engaging users and encouraging them to click through.

However, when we look at ROAS (Return on Ad Spend), the Holiday Sale campaign significantly outshined the App Install campaign. The Holiday Sale campaign achieved a ROAS of 12.63, indicating a strong return on investment, while the App Install campaign had a much lower ROAS of 0.56.

In summary, the App Install campaign was more efficient in terms of cost per click and user engagement, but the Holiday Sale campaign delivered a far superior return on ad spend.

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

## Test 36: Which adset had the highest cpc last week?

**Answer**:
> The Weekend Audience - Black Friday Deals adset had the highest CPC at $0.64 last week—your worst performer. For context, your overall CPC was $0.45, so this adset was quite a bit higher than average.

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

## Test 85: What's the spend, revenue, and ROAS for all Google campaigns in September?

**Answer**:
> Here are your metrics from 2025-09-01 to 2025-09-30:

• SPEND: $58,565.86
• REVENUE: $412,262.76
• ROAS: 7.04×

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

• CLICKS: 26,692
• CONVERSIONS: 2,559
• CPA: $5.31

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

## Test 37: Which adset had the highest cpc last week?

**Answer**:
> The Weekend Audience - Black Friday Deals adset had the highest CPC at $0.64 last week—your worst performer. For context, your overall average CPC was $0.45, so this adset is definitely on the higher side.

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

## Test 87: Give me CTR, CPC, and conversion rate for Summer Sale campaign last month

**Answer**:
> Here are your metrics in the last 30 days:

• CTR: 3.4%
• CPC: $0.40
• CVR: 5.2%

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
    "level": "campaign",
    "entity_ids": null,
    "status": null,
    "entity_name": "Summer Sale",
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

## Test 38: Which adset had the lowest ctr last week?

**Answer**:
> The Weekend Audience - General Conversions adset had the lowest CTR at 1.6% last week—definitely struggling a bit. For context, your overall CTR was 2.6%, so this adset could use some attention.

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

## Test 88: Compare spend and revenue between Morning Audience and Evening Audience adsets this month to date

**Answer**:
> From October 1 to 15, both the Morning Audience and Evening Audience ad sets had similar spending levels, with the Morning Audience spending slightly more at $11,907.47 compared to the Evening Audience's $11,891.30. However, when it comes to revenue, the Morning Audience outperformed the Evening Audience. The Morning Audience generated $79,539.07 in revenue, which is $7,947.57 more than the Evening Audience's $72,591.50. 

In summary, while both ad sets had nearly identical spending, the Morning Audience was more effective in generating revenue during this period.

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
    "level": "adset",
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

• ROAS: 10.68×
• REVENUE: $47,334.78
• PROFIT: $13,632.91

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
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "Black Friday Deals",
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

## Test 40: what is my cvr on google last month?

**Answer**:
> Your CVR was 9.6% in the last 30 days.

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

## Test 90: Show me CPC, clicks, and spend for all active campaigns last 5 days

**Answer**:
> Here are your metrics in the last 5 days:

• CPC: $0.45
• CLICKS: 103,195
• SPEND: $46,165.74

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

## Test 41: What's my ROAS for active campaigns?

**Answer**:
> Your ROAS was 5.81× for active campaigns last week.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's my ROAS for active campaigns?",
  "timeframe_description": "last week"
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

## Test 42: How much did I spend on Meta ads?

**Answer**:
> You spent $18,606.01 on Meta ads last week.

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

## Test 92: What's the revenue, ROAS, and cost per lead for lead gen campaigns this month to date?

**Answer**:
> Here are your metrics from October 01 to 15:

• REVENUE: $33,570.22
• ROAS: 2.16×
• CPL: $2.39

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
    "end": "2025-10-15"
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

## Test 43: How much revenue on Google last week?

**Answer**:
> The revenue on Google was $188,355.76 last week.

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
> Your cost per install was $23.61 last week.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's my cost per install?",
  "timeframe_description": "last week"
}
```

---

## Test 45: How many leads did I generate today?

**Answer**:
> You generated 703 leads today.

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

## Test 93: Give me spend, clicks, and CPC for Holiday Sale and Summer Sale campaigns last month

**Answer**:
> In the last 30 days, the Holiday Sale and Summer Sale campaigns showed some interesting differences in performance. 

Starting with spend, the Summer Sale campaign had a higher expenditure, totaling $30,441.22 compared to the Holiday Sale's $21,278.52. This indicates a more significant investment in the Summer Sale campaign.

When it comes to clicks, the Summer Sale campaign also outperformed, generating 77,665 clicks, whereas the Holiday Sale campaign garnered 43,284 clicks. This suggests that the Summer Sale campaign was more effective in driving traffic.

Looking at the cost per click (CPC), the Summer Sale campaign was more cost-efficient, with a CPC of $0.39 compared to the Holiday Sale's CPC of $0.49. This means the Summer Sale campaign was able to achieve clicks at a lower cost.

Overall, the Summer Sale campaign performed better in terms of spend efficiency and click generation, making it the more effective campaign across these metrics.

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
    "Holiday Sale",
    "Summer Sale"
  ],
  "comparison_metrics": [
    "spend",
    "clicks",
    "cpc"
  ],
  "question": "Give me spend, clicks, and CPC for Holiday Sale and Summer Sale campaigns last month",
  "timeframe_description": "last month"
}
```

---

## Test 94: Show me conversion rate, revenue, and profit for all campaigns last week

**Answer**:
> Here are your metrics last week:

• CVR: 8.3%
• REVENUE: $414,352.86
• PROFIT: $124,905.04

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Show me conversion rate, revenue, and profit for all campaigns last week",
  "timeframe_description": "last week"
}
```

---

## Test 46: wich ad had the lowest cpc last week?

**Answer**:
> The Video Ad - Weekend Audience - App Install Campaign had the lowest CPC at $0.30 last week—your best performer! For context, your overall average CPC was $0.45, so this ad really stood out.

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
> Your revenue would have been $414,352.86 last week if your CPC was $0.20.

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
        "operator": "=",
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

## Test 95: Compare CPA, ROAS, and revenue for App Install campaign vs Holiday Sale campaign last 5 days

**Answer**:
> Over the last 5 days, let's take a look at how the App Install Campaign and the Holiday Sale campaign have performed across key metrics: CPA, ROAS, and revenue.

Starting with CPA (Cost Per Acquisition), the App Install Campaign has a significantly lower CPA at approximately $4.07 compared to the Holiday Sale's $10.10. This indicates that the App Install Campaign is more cost-effective in acquiring customers.

When it comes to ROAS (Return on Advertising Spend), the Holiday Sale campaign outshines with an impressive ROAS of 12.99, whereas the App Install Campaign lags behind with a ROAS of just 0.53. This suggests that the Holiday Sale campaign is generating much more revenue for every dollar spent on advertising.

Finally, in terms of revenue, the Holiday Sale campaign again takes the lead, generating $48,152.88 compared to the App Install Campaign's $2,812.30. This substantial difference highlights the Holiday Sale campaign's effectiveness in driving sales.

In summary, while the App Install Campaign is more cost-efficient in terms of CPA, the Holiday Sale campaign excels in generating higher ROAS and overall revenue.

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
    "App Install Campaign",
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

• CTR: 2.6%
• CPC: $0.44
• CONVERSIONS: 7,260

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
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "Weekend Audience",
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

## Test 48: best performing ad set in Holiday Sale campaign yesterday?

**Answer**:
> The "Weekend Audience - Holiday Sale - Purchases" ad set had the lowest ROAS at 14.46× yesterday, which needs some attention. For context, your overall ROAS was 5.86×, so while it's still above average, there's room for improvement compared to your top performer at 18.85×.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "roas",
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

## Test 97: Give me spend, revenue, ROAS, and profit for all Meta campaigns this month to date

**Answer**:
> Here are your metrics from October 01 to 15:

• SPEND: $39,920.88
• REVENUE: $356,290.43
• ROAS: 8.92×
• PROFIT: $106,833.86

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
> In the last 30 days, when comparing the Morning Audience and Evening Audience ad sets, the Evening Audience slightly outperformed in terms of clicks, CTR, and CPC.

- **Clicks**: The Evening Audience received 209,153 clicks, which is higher than the Morning Audience's 198,401 clicks.
- **CTR (Click-Through Rate)**: The Evening Audience also had a slightly better CTR at 2.56%, compared to the Morning Audience's 2.53%.
- **CPC (Cost Per Click)**: Additionally, the Evening Audience had a more cost-effective CPC at $0.45, while the Morning Audience's CPC was $0.45.

Overall, the Evening Audience demonstrated a marginally better performance across all these key metrics.

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
    "Morning Audience",
    "Evening Audience"
  ],
  "comparison_metrics": [
    "clicks",
    "ctr",
    "cpc"
  ],
  "question": "Compare clicks, CTR, and cost per click for Morning vs Evening Audience adsets last month",
  "timeframe_description": "last month"
}
```

---

## Test 49: all ad sets above roas 4 in the last 3 days

**Answer**:
> In the last 3 days, there have been several ad sets with a ROAS (Return on Ad Spend) above 4. Here's a list of all the ad sets that performed exceptionally well:

1. **Weekend Audience - Holiday Sale - Purchases**: This ad set achieved a remarkable ROAS of 17.90, with a spend of $254.47 and generating a revenue of $4,554.37.

2. **Morning Audience - Summer Sale Campaign**: With a ROAS of 16.87, this campaign spent $283.72 and brought in $4,785.99 in revenue.

3. **Morning Audience - General Conversions**: This ad set had a ROAS of 16.75, spending $180.93 and earning $3,029.76 in revenue.

4. **Weekend Audience - Summer Sale Campaign**: Achieving a ROAS of 15.53, this campaign spent $374.98 and generated $5,825.15 in revenue.

5. **Evening Audience - Summer Sale Campaign**: This ad set recorded a ROAS of 14.24, with a spend of $201.89 and revenue of $2,874.36.

6. **Morning Audience - Website Traffic Push**: With a ROAS of 13.85, this campaign spent $179.20 and brought in $2,482.12 in revenue.

7. **Morning Audience - Black Friday Deals**: This ad set achieved a ROAS of 12.62, spending $73.20 and generating $924.01 in revenue.

8. **Evening Audience - General Conversions**: This campaign had a ROAS of 12.59, with a spend of $122.08 and revenue of $1,536.52.

9. **Weekend Audience - General Conversions**: Achieving a ROAS of 12.05, this ad set spent $127.96 and brought in $1,541.31 in revenue.

10. **Morning Audience - Blog Content Promotion**: This ad set recorded a ROAS of 10.74, with a spend of $176.59 and revenue of $1,896.36.

Overall, there are 10 ad sets that exceeded a ROAS of 4 in the last 3 days, showcasing strong performance across various audiences and campaigns.

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
> The Website Traffic Push campaign had the highest CTR at 3.7% last week—your top performer! For context, your overall CTR was 2.6%, so this campaign is really leading the pack.

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
> Last week, your ad sets had an average CPC of $0.45, which is right on target with your overall average. The Weekend Audience - Black Friday Deals ad set had a CPC of $0.64, which is a bit higher than your average but still below the $1 mark.

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
        "value": 1
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
> The worst performing ad in your App Install campaign last week was the Image Ad - Morning Audience with a CTR of 2.9%—it needs some attention. For context, your overall CTR was 3.6%, which was above the workspace average of 2.6%.

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
  "sort_order": "asc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "App Install Campaign",
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
> No data available for last week.

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
> The Evening Audience - Lead Gen - B2B adset spent the most money at $830.75 last week—your top performer! For context, this was right on par with your overall average spend of $68,093.49.

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
> The Carousel Ad - Evening Audience from the Summer Sale Campaign brought in $10,196.34 last week, which was above your $1,000 threshold. For context, this ad's revenue was part of your overall average revenue of $414,352.86 for the week.

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
> The "Website Traffic Push" campaign had the highest POAS at 2.46× last week, making it your top performer! Overall, your average POAS was 1.83×, so this campaign really stood out.

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
> Here are the ad sets from last week that had more than 500 clicks:

1. **Weekend Audience - Summer Sale Campaign**: This ad set achieved 2,183 clicks, with a spend of $784.94, generating $14,235.14 in revenue from 55,885 impressions.

2. **Evening Audience - App Install Campaign**: It garnered 1,781 clicks, spending $523.15, and brought in $392.02 in revenue with 41,256 impressions.

3. **Weekend Audience - Lead Gen - B2B**: This ad set had 1,765 clicks, with a spend of $751.74, resulting in $1,773.62 in revenue from 50,470 impressions.

4. **Weekend Audience - App Install Campaign**: It received 1,629 clicks, costing $660.00, and generated $204.28 in revenue from 41,686 impressions.

5. **Evening Audience - Lead Gen - B2B**: This ad set achieved 1,581 clicks, with a spend of $830.75, and brought in $588.60 in revenue from 53,508 impressions.

6. **Weekend Audience - Website Traffic Push**: It had 1,571 clicks, spending $733.31, and generated $4,904.92 in revenue from 43,164 impressions.

7. **Morning Audience - App Install Campaign**: This ad set received 1,529 clicks, with a spend of $559.06, resulting in $456.77 in revenue from 48,835 impressions.

8. **Morning Audience - Website Traffic Push**: It garnered 1,524 clicks, costing $613.02, and brought in $5,827.42 in revenue from 38,708 impressions.

9. **Evening Audience - Website Traffic Push**: This ad set achieved 1,436 clicks, with a spend of $506.29, and generated $6,339.68 in revenue from 36,894 impressions.

10. **Morning Audience - Summer Sale Campaign**: It received 1,402 clicks, spending $606.72, and brought in $11,226.30 in revenue from 42,125 impressions.

In total, all 10 ad sets surpassed the 500-click mark last week.

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
> The Video Ad - Evening Audience - Lead Gen - B2B had the lowest cost per conversion at $1.90 last week—your best performer! For context, your overall CPA was $5.39, so this ad really stood out.

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
> The "Website Traffic Push" campaign had the highest impressions at 40,866 last week. Overall, your campaigns averaged 5,892,857 impressions, so this one was right in line with the average.

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
> The Weekend Audience - App Install Campaign had the lowest ROAS at 0.31× last week—definitely your worst performer. For context, your overall ROAS was 6.09×, so this campaign really needs some attention.

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
> No data available for last week.

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
> The Website Traffic Push campaign generated the most leads last week with 5,021—your top performer! Interestingly, this was right on par with your workspace average, so it's consistently performing well.

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
> Last week, your ad sets with spend below $50 were performing at an average level. Overall, your total spend was $68,093.49, which matched the workspace average. So, while those ad sets kept costs low, they didn't stand out in terms of overall performance.

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
> The Image Ad - Weekend Audience - Summer Sale Campaign had the highest ARPV at $4.28 last week, making it your top performer! For comparison, your overall ARPV was $3.80, so this ad really stood out.

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
> Here are all the campaigns from last week with a CPM under $10:

1. **Holiday Sale - Purchases**: This campaign had a CPM of $9.55. It spent $399.70, garnered 716 clicks, achieved 36 conversions, and generated $4,901.60 in revenue with 41,856 impressions.

2. **Product Launch Teaser**: With a CPM of $8.76, this campaign spent $254.09, received 465 clicks, resulted in approximately 15 conversions, and brought in $575.26 in revenue from 29,001 impressions.

3. **Black Friday Deals**: This campaign had a CPM of $8.29. It spent $357.03, attracted 978 clicks, achieved 60 conversions, and generated $7,213.10 in revenue with 43,075 impressions.

4. **General Conversions**: With a CPM of $8.21, this campaign spent $335.89, received 784 clicks, resulted in about 70 conversions, and brought in $3,940.91 in revenue from 40,906 impressions.

In total, there are 4 campaigns that met the criteria of having a CPM under $10.

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
> The Evening Audience - Lead Gen - B2B adset had the highest conversion rate at 18.7% last week—crushing it! For context, your overall conversion rate was 8.3%, so this adset really stood out.

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
> The Image Ad targeting the Weekend Audience for Lead Gen in B2B had 337 conversions last week. That's right on par with your overall average of 12,635 conversions during the same period. It seems like your ads are performing consistently across the board!

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
> The Product Launch Teaser campaign had a CPL of $13.56 last week, which was right at the average for your workspace. It's not standing out as the best or worst performer, just holding steady in the middle. For context, your overall CPL was also $13.56.

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
> Here is a list of all ad sets from last week that generated revenue above $5,000:

1. **Weekend Audience - Summer Sale Campaign**: This ad set brought in $14,235.14 in revenue.
2. **Morning Audience - Summer Sale Campaign**: It generated $11,226.30 in revenue.
3. **Evening Audience - Holiday Sale - Purchases**: This ad set achieved $6,991.09 in revenue.
4. **Evening Audience - Website Traffic Push**: It earned $6,339.68 in revenue.
5. **Evening Audience - Summer Sale Campaign**: This ad set brought in $6,234.97 in revenue.
6. **Weekend Audience - Holiday Sale - Purchases**: It generated $6,063.21 in revenue.
7. **Morning Audience - Website Traffic Push**: This ad set achieved $5,827.42 in revenue.
8. **Morning Audience - Blog Content Promotion**: It earned $5,784.62 in revenue.
9. **Morning Audience - Holiday Sale - Purchases**: This ad set brought in $5,212.57 in revenue.

In total, there are 9 ad sets that exceeded the $5,000 revenue mark last week.

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
> The Image Ad - Weekend Audience - Summer Sale Campaign had the best profit margin with a POAS of 2.90× last week—it's really leading the pack! For context, your overall POAS was 1.83×, so this ad is definitely crushing it.

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
> The "Website Traffic Push" campaign had 1,520 clicks last week, which is above the 1,000-click threshold you were looking for. Overall, your campaigns averaged 151,658 clicks last week, so this one was right in line with your average performance.

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
> The Evening Audience - Lead Gen - B2B ad set had the lowest AOV at $2.00 last week—definitely your worst performer. For context, your overall AOV was $32.79, so this one really needs some attention.

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
> Here are all the ads from last week that had a spend of over $200:

1. **Image Ad - Weekend Audience - Summer Sale Campaign**: This ad had a spend of $800.61.
2. **Image Ad - Weekend Audience - Lead Gen - B2B**: The spend for this ad was $737.36.
3. **Image Ad - Evening Audience - Lead Gen - B2B**: This ad spent $703.09.
4. **Carousel Ad - Weekend Audience - App Install Campaign**: The spend here was $696.38.
5. **Image Ad - Morning Audience - Mobile Game Installs**: This ad had a spend of $650.60.
6. **Carousel Ad - Evening Audience - App Install Campaign**: The spend for this ad was $644.36.
7. **Carousel Ad - Morning Audience - Brand Awareness**: This ad spent $625.21.
8. **Image Ad - Evening Audience - Summer Sale Campaign**: The spend here was $616.53.
9. **Image Ad - Morning Audience - Brand Awareness**: This ad had a spend of $613.98.
10. **Video Ad - Morning Audience - Lead Gen - B2B**: The spend for this ad was $612.88.

In total, there were 10 ads that each spent over $200 last week.

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
> The "Lead Gen - B2B" campaign had the lowest CPA at $2.15 last week—your best performer! For context, your overall CPA was $5.39, so this campaign is really leading the pack.

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
> The Evening Audience - Lead Gen - B2B ad set had the highest impressions at 53,508 last week. Overall, your ad sets averaged 5,892,857 impressions, which is right on target with your usual performance.

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
> The Summer Sale campaign had a ROAS of 13.72× last week, which is more than double the workspace average of 6.09×. That's an excellent performance, showing it's really crushing it compared to your other campaigns!

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
    "level": "campaign",
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
> You're currently running one campaign named "Lead Gen - B2B."

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
> The CPA for Morning Audience adsets was $5.53 last week.

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
> The revenue for the Black Friday campaign was $47,334.78 last week.

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
    "entity_name": "Black Friday Deals",
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
> Here's the ROAS for your App Install campaigns from last week:

- **App Install Campaign**: The ROAS is 0.27. With a spend of $260.93, the campaign generated $71.24 in revenue from 55 conversions. It also achieved 658 clicks and 19,652 impressions.

This breakdown includes all the data available for the specified timeframe. If you have any more questions or need further analysis, feel free to ask!

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
    "entity_name": "App Install Campaign",
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
> You're managing 10 ad sets, including campaigns like Weekend Audience - App Install Campaign, Black Friday Deals, and Brand Awareness.

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
    "entity_name": "Weekend Audience",
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
> The CTR for Evening Audience adsets was 2.6% last week.

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
    "entity_name": "Evening Audience",
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
> The Holiday Sale campaign spent $4,928.43 last week.

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
> Last week, we compared the performance of the Holiday Sale and App Install campaigns based on CPC, CTR, and ROAS.

Starting with Cost Per Click (CPC), the App Install campaign had a lower CPC at $0.38 compared to the Holiday Sale's $0.47. This indicates that the App Install campaign was more cost-effective in terms of clicks.

Looking at Click-Through Rate (CTR), the App Install campaign also outperformed with a CTR of 3.56%, while the Holiday Sale campaign had a CTR of 2.06%. This suggests that the App Install ads were more engaging to the audience.

However, when it comes to Return on Advertising Spend (ROAS), the Holiday Sale campaign significantly outshined the App Install campaign. The Holiday Sale achieved a ROAS of 12.63, indicating a strong return on investment, whereas the App Install campaign had a much lower ROAS of 0.56.

In summary, while the App Install campaign was more efficient in terms of CPC and CTR, the Holiday Sale campaign delivered a far superior return on investment with its higher ROAS.

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

• SPEND: $58,565.86
• REVENUE: $412,262.76
• ROAS: 7.04×

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

• CLICKS: 26,692
• CONVERSIONS: 2,559
• CPA: $5.31

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

• CTR: 3.4%
• CPC: $0.40
• CVR: 5.2%

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
    "level": "campaign",
    "entity_ids": null,
    "status": null,
    "entity_name": "Summer Sale",
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
> From October 1 to 15, the Morning Audience and Evening Audience ad sets showed some interesting differences in their performance. The Morning Audience had a slightly higher spend of $11,907.47 compared to the Evening Audience's $11,891.30. Despite this small difference in spending, the Morning Audience generated a significantly higher revenue of $79,539.07, whereas the Evening Audience brought in $72,591.50.

In terms of efficiency, the Morning Audience not only spent marginally more but also achieved better revenue outcomes. This suggests that the Morning Audience ad set was more effective in converting spend into revenue during this period.

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
    "level": "adset",
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

• ROAS: 10.68×
• REVENUE: $47,334.78
• PROFIT: $13,632.91

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
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "Black Friday Deals",
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

• CPC: $0.45
• CLICKS: 103,195
• SPEND: $46,165.74

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

• REVENUE: $33,570.22
• ROAS: 2.16×
• CPL: $2.39

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
    "end": "2025-10-15"
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
> In the last 30 days, the Summer Sale campaign outperformed the Holiday Sale campaign across all key metrics. 

Firstly, in terms of spend, the Summer Sale campaign invested $30,441.22, which is significantly higher than the $21,278.52 spent on the Holiday Sale campaign. This higher investment seems to have paid off in terms of clicks, as the Summer Sale garnered 77,665 clicks compared to the Holiday Sale's 43,284 clicks.

When we look at the cost per click (CPC), the Summer Sale campaign also had a more efficient performance, with a CPC of $0.39, while the Holiday Sale's CPC was $0.49. This indicates that the Summer Sale campaign was not only more cost-effective but also more successful in driving traffic with its budget.

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
    "Holiday Sale",
    "Summer Sale"
  ],
  "comparison_metrics": [
    "spend",
    "clicks",
    "cpc"
  ],
  "question": "Give me spend, clicks, and CPC for Holiday Sale and Summer Sale campaigns last month",
  "timeframe_description": "last month"
}
```

---

## Test 94: Show me conversion rate, revenue, and profit for all campaigns last week

**Answer**:
> Here are your metrics last week:

• CVR: 8.3%
• REVENUE: $414,352.86
• PROFIT: $124,905.04

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
> Over the last 5 days, let's take a look at how the App Install Campaign and the Holiday Sale campaign have performed across key metrics: CPA, ROAS, and revenue.

Starting with CPA (Cost Per Acquisition), the App Install Campaign has a significantly lower CPA at $4.07 compared to the Holiday Sale campaign's $10.10. This means the App Install Campaign is more cost-effective in acquiring users.

When it comes to ROAS (Return on Ad Spend), the Holiday Sale campaign shines with a remarkable ROAS of 12.99, indicating a high return for every dollar spent. In contrast, the App Install Campaign has a ROAS of just 0.53, suggesting it is not generating as much return on the advertising investment.

Looking at revenue, the Holiday Sale campaign again outperforms, generating $48,152.88, which is substantially higher than the App Install Campaign's revenue of $2,812.30.

In summary, while the App Install Campaign is more efficient in terms of CPA, the Holiday Sale campaign excels in generating higher returns and revenue.

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
    "App Install Campaign",
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

• CTR: 2.6%
• CPC: $0.44
• CONVERSIONS: 7,260

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
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "Weekend Audience",
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

• SPEND: $39,920.88
• REVENUE: $356,290.43
• ROAS: 8.92×
• PROFIT: $106,833.86

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
> In the last 30 days, when comparing the Morning Audience and Evening Audience ad sets, the Evening Audience performed slightly better across most metrics. 

The Evening Audience had more clicks, with a total of 209,153 compared to the Morning Audience's 198,401 clicks. In terms of click-through rate (CTR), the Evening Audience also had a slight edge, achieving a CTR of 2.56% compared to the Morning Audience's 2.53%. 

Additionally, the cost per click (CPC) was lower for the Evening Audience at $0.45, whereas the Morning Audience had a CPC of $0.45 as well, but slightly higher. Overall, the Evening Audience ad set showed a marginally better performance in clicks, CTR, and CPC.

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
    "Morning Audience",
    "Evening Audience"
  ],
  "comparison_metrics": [
    "clicks",
    "ctr",
    "cpc"
  ],
  "question": "Compare clicks, CTR, and cost per click for Morning vs Evening Audience adsets last month",
  "timeframe_description": "last month"
}
```

---

