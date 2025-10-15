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

observation: there is a column wich specifies the type of campaign, i think this talked about leads because of context from last question, but this is not a lead campaign so it shouldnt give a breakdown for leads.

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

observation: this didnt give the list

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

observation: these 2 entities exist, i think the filtering is done wrong or not broad enough

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

observation: this is not correct there are google campaign live

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

observation: this is not really natural language, should say something like: i currenlty see no ads on google or meta in your account... 

also this is not correct since there are google and meta ads in this account

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

observation: this wrong , these 2 campaigns exist

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

observation: didnt give me a list

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

observation: this didnt work

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

observation: didnt give list, or all ad sets have roas above 4 then it should say something like all ad sets are above roas 4 

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

observation: didnt answer the question 

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

observation: performing and breakdowns should be: revenue, spend, roas, cpc, cvr

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

observation: should say something about the result, like you only have 1 .. or all of your ads have revenue above 1000 etc

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

observation: this is not correct, should have said highest profit margin

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

observation: in this case the users question in terms of timeframe is too vague, should ask follow up question asking for a timeframe

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

observation: arpv is not revenue per click, we should say we dont know that derived metric

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

observation: should say its Google in the answer