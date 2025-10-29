# QA Test Results

**Test Run**: Wed Oct 29 15:28:54 CET 2025
**Workspace**: Defang Labs (4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199)
**System Version**: Phase 5 (v2.1.3)

---

## Test 1: What's my CPC this month?

**Answer**:
> Your CPC is $0.45 from October 01 to 29.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpc",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-29"
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
  "timeframe_description": "this month",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
Binary file (standard input) matches
```

---

## Test 2: How much did I spend this month?

**Answer**:
> You spent $268,552.71 from October 01 to 29.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "spend",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-29"
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
  "timeframe_description": "this month",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'How much did I spend this month?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'spend', 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 10, 1), 'end': datetime.date(2025, 10, 29)}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How much did I spend this month?', 'timeframe_description': 'this month', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 2114ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='spend', time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 29)), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How much did I spend this month?', timeframe_description='this month', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('268552.7100'), 'revenue': Decimal('1673577.6200'), 'clicks': 593809, 'impressions': 23402098, 'conversions': Decimal('50121.9000'), 'leads': Decimal('19608.4100'), 'installs': 11733, 'purchases': 6792, 'visitors': 426056, 'profit': Decimal('503172.8300')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 268552.71
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=268552.71, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 268552.71
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=268552.71 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=268552.71
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'You spent $268,552.71 from October 01 to 29.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 766ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3042ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'You spent $268,552.71 from October 01 to 29.'
```

---

## Test 3: What's my ROAS this week?

**Answer**:
> Your ROAS is 6.33× this week.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "roas",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-27",
    "end": "2025-10-29"
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
  "timeframe_description": "this week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'What's my ROAS this week?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 10, 27), 'end': datetime.date(2025, 10, 29)}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's my ROAS this week?", 'timeframe_description': 'this week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1728ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 27), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived='roas', need_timeseries=False, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 10, 27), end=datetime.date(2025, 10, 29)), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's my ROAS this week?", timeframe_description='this week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 27) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-27 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('19475.4100'), 'revenue': Decimal('123327.3500'), 'clicks': 42419, 'impressions': 1645128, 'conversions': Decimal('3586.7400'), 'leads': Decimal('1423.5300'), 'installs': 825, 'purchases': 499, 'visitors': 30340, 'profit': Decimal('36042.6200')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.332464887773864581028075917
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.332464887773864581028075917'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.332464887773864581028075917
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=6.332464887773865 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=6.332464887773865
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your ROAS is 6.33× this week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1054ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2943ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your ROAS is 6.33× this week.'
```

---

## Test 4: How much revenue did I generate yesterday?

**Answer**:
> Your revenue was $61,083.77 yesterday.

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
  "timeframe_description": "yesterday",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'How much revenue did I generate yesterday?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 1, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How much revenue did I generate yesterday?', 'timeframe_description': 'yesterday', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 6125ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 28), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=1, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How much revenue did I generate yesterday?', timeframe_description='yesterday', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 28) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-28 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('9466.4500'), 'revenue': Decimal('61083.7700'), 'clicks': 20493, 'impressions': 794781, 'conversions': Decimal('1714.4700'), 'leads': Decimal('613.8200'), 'installs': 446, 'purchases': 224, 'visitors': 14129, 'profit': Decimal('18180.0800')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 61083.77
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=61083.77, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 61083.77
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=61083.77 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=61083.77
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your revenue was $61,083.77 yesterday.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 867ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 7144ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your revenue was $61,083.77 yesterday.'
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
    "status": null,
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's my conversion rate?",
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'What's my conversion rate?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cvr', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's my conversion rate?", 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1864ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived='cvr', need_timeseries=False, need_previous=False, base_measures=['clicks', 'conversions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cvr', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's my conversion rate?", timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cvr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cvr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cvr: 0.08520973675409679422865606039
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cvr': MetricValue(value=Decimal('0.08520973675409679422865606039'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.08520973675409679422865606039
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.0852097367540968 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=0.0852097367540968
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your conversion rate was 8.5% last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 963ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2982ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your conversion rate was 8.5% last week.'
```

---

## Test 6: How many clicks did I get last week?

**Answer**:
> You had 125,586 clicks last week.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'How many clicks did I get last week?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'clicks', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How many clicks did I get last week?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1345ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['clicks'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='clicks', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How many clicks did I get last week?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['clicks']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for clicks
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for clicks: 125586.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'clicks': MetricValue(value=125586.0, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 125586.0
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=125586.0 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=125586.0
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'You had 125,586 clicks last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 643ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2149ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'You had 125,586 clicks last week.'
```

---

## Test 7: How much profit did I make last week?

**Answer**:
> Your profit was $111,922.76 last week.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'How much profit did I make last week?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'profit', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How much profit did I make last week?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1032ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['profit'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='profit', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How much profit did I make last week?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['profit']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for profit
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for profit: 111922.76
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'profit': MetricValue(value=111922.76, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 111922.76
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=111922.76 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=111922.76
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your profit was $111,922.76 last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1143ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2307ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your profit was $111,922.76 last week.'
```

---

## Test 8: How many leads did I generate this month?

**Answer**:
> You generated 19,608 leads from October 01 to 29.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "leads",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-29"
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
  "timeframe_description": "this month",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'How many leads did I generate this month?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'leads', 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 10, 1), 'end': datetime.date(2025, 10, 29)}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How many leads did I generate this month?', 'timeframe_description': 'this month', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1695ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['leads'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='leads', time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 29)), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How many leads did I generate this month?', timeframe_description='this month', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['leads']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('268552.7100'), 'revenue': Decimal('1673577.6200'), 'clicks': 593809, 'impressions': 23402098, 'conversions': Decimal('50121.9000'), 'leads': Decimal('19608.4100'), 'installs': 11733, 'purchases': 6792, 'visitors': 426056, 'profit': Decimal('503172.8300')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for leads
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for leads: 19608.41
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'leads': MetricValue(value=19608.41, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 19608.41
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=19608.41 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=19608.41
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'You generated 19,608 leads from October 01 to 29.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 660ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2502ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'You generated 19,608 leads from October 01 to 29.'
```

---

## Test 9: What is my cost per lead this month?

**Answer**:
> Your cost per lead is $13.70 from October 01 to 29.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpl",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-29"
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
  "timeframe_description": "this month",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'What is my cost per lead this month?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpl', 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 10, 1), 'end': datetime.date(2025, 10, 29)}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'What is my cost per lead this month?', 'timeframe_description': 'this month', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 3350ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived='cpl', need_timeseries=False, need_previous=False, base_measures=['leads', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpl', time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 29)), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='What is my cost per lead this month?', timeframe_description='this month', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpl']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('268552.7100'), 'revenue': Decimal('1673577.6200'), 'clicks': 593809, 'impressions': 23402098, 'conversions': Decimal('50121.9000'), 'leads': Decimal('19608.4100'), 'installs': 11733, 'purchases': 6792, 'visitors': 426056, 'profit': Decimal('503172.8300')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpl
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpl: 13.69579226464562909486286751
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpl': MetricValue(value=Decimal('13.69579226464562909486286751'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 13.69579226464562909486286751
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=13.695792264645629 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=13.695792264645629
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your cost per lead is $13.70 from October 01 to 29.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 973ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 4471ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your cost per lead is $13.70 from October 01 to 29.'
```

---

## Test 10: Which campaign had the highest ROAS last week?

**Answer**:
> The Summer Sale Campaign had the highest ROAS at 17.51× last week—crushing it as your top performer! For context, your overall ROAS was 6.51×, so this campaign really stood out.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Which campaign had the highest ROAS last week?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Which campaign had the highest ROAS last week?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1021ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Which campaign had the highest ROAS last week?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.507078653503120199422664633'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for roas by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=6.50707865350312 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 5.8664627604890764}, {'date': '2025-10-24', 'value': 6.161505000243192}, {'date': '2025-10-25', 'value': 7.76569736303204}, {'date': '2025-10-26', 'value': 6.6619532432258985}, {'date': '2025-10-27', 'value': 6.218785967772876}, {'date': '2025-10-28', 'value': 6.452658599580624}] breakdown=[{'label': 'Summer Sale Campaign', 'value': 17.509479263403474, 'spend': 441.49, 'clicks': 1053, 'conversions': 57.0, 'revenue': 7730.26, 'impressions': 31363}] workspace_avg=6.50707865350312
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Summer Sale Campaign had the highest ROAS at 17.51× last week—crushing it as your top performer! For context, your overall ROAS was 6.51×, so this campaign really stood out.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 3581ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 4829ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Summer Sale Campaign had the highest ROAS at 17.51× last week—crushing it as your top performer! For context, your overall ROAS was 6.51×, so this campaign really stood out.'
```

---

## Test 11: What's my ROAS for Google campaigns only?

**Answer**:
> Your ROAS for Google campaigns was 6.96× last week.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'What's my ROAS for Google campaigns only?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': 'google', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's my ROAS for Google campaigns only?", 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1144ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived='roas', need_timeseries=False, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': 'google', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider='google', level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's my ROAS for Google campaigns only?", timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=google, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('23974.8800'), 'revenue': Decimal('166884.1100'), 'clicks': 60326, 'impressions': 1739675, 'conversions': Decimal('5989.3100'), 'leads': Decimal('2773.4300'), 'installs': 1489, 'purchases': 746, 'visitors': 41425, 'profit': Decimal('50931.6600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.960790210420239851044092817'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.507078653503120199422664633
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=6.96079021042024 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=6.50707865350312
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your ROAS for Google campaigns was 6.96× last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 814ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2137ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your ROAS for Google campaigns was 6.96× last week.'
```

---

## Test 12: Which campaign spent the most yesterday?

**Answer**:
> The "Lead Gen - B2B" campaign spent the most yesterday at $175.72—your top performer! Interestingly, this spend was right on par with your overall average spend for the day.

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
  "timeframe_description": "yesterday",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Which campaign spent the most yesterday?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'spend', 'time_range': {'last_n_days': 1, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Which campaign spent the most yesterday?', 'timeframe_description': 'yesterday', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1080ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 28), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='spend', time_range=TimeRange(last_n_days=1, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Which campaign spent the most yesterday?', timeframe_description='yesterday', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 28) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-28 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('9466.4500'), 'revenue': Decimal('61083.7700'), 'clicks': 20493, 'impressions': 794781, 'conversions': Decimal('1714.4700'), 'leads': Decimal('613.8200'), 'installs': 446, 'purchases': 224, 'visitors': 14129, 'profit': Decimal('18180.0800')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 9466.45
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=9466.45, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 9466.45
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for spend by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 28) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-28 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=9466.45 previous=None delta_pct=None timeseries=[{'date': '2025-10-28', 'value': 9466.45}] breakdown=[{'label': 'Lead Gen - B2B', 'value': 175.72, 'spend': 175.72, 'clicks': 318, 'conversions': 66.86, 'revenue': 439.2, 'impressions': 9190}] workspace_avg=9466.45
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The "Lead Gen - B2B" campaign spent the most yesterday at $175.72—your top performer! Interestingly, this spend was right on par with your overall average spend for the day.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1350ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2630ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The "Lead Gen - B2B" campaign spent the most yesterday at $175.72—your top performer! Interestingly, this spend was right on par with your overall average spend for the day.'
```

---

## Test 13: List all active campaigns

**Answer**:
> Here are your 11 campaigns:
1. App Install Campaign
2. Black Friday Deals
3. Brand Awareness
4. General Conversions
5. Holiday Sale - Purchases
6. Lead Gen - B2B
7. Mobile Game Installs
8. Newsletter Signup Campaign
9. Product Launch Teaser
10. Summer Sale Campaign
11. Website Traffic Push

**DSL**:
```json
{
  "query_type": "entities",
  "metric": null,
  "time_range": null,
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 50,
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
  "timeframe_description": null,
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'List all active campaigns'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.ENTITIES: 'entities'>, 'metric': None, 'time_range': None, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': 'campaign', 'entity_ids': None, 'status': 'active', 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'List all active campaigns', 'timeframe_description': None, 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1168ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: None
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: campaign
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'entities': [{'name': 'App Install Campaign', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Black Friday Deals', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Brand Awareness', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'General Conversions', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Holiday Sale - Purchases', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Lead Gen - B2B', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Mobile Game Installs', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Newsletter Signup Campaign', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Product Launch Teaser', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Summer Sale Campaign', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Website Traffic Push', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}]}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your 11 campaigns:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1285ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your 11 campaigns:
```

---

## Test 14: Which ad has the highest CTR?

**Answer**:
> The Carousel Ad - Evening Audience - Summer Sale Campaign had the highest CTR at 4.6% last week—your top performer! For context, your overall CTR was 2.5%, so this ad's really standing out.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Which ad has the highest CTR?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'ctr', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Which ad has the highest CTR?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 995ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='ad', breakdown='ad', derived='ctr', need_timeseries=True, need_previous=False, base_measures=['clicks', 'impressions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='ctr', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Which ad has the highest CTR?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['ctr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for ctr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for ctr: 0.02535125290734174
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'ctr': MetricValue(value=0.02535125290734174, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.02535125290734174
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for ctr by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.02535125290734174 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 0.024331210344251276}, {'date': '2025-10-24', 'value': 0.025365635577885168}, {'date': '2025-10-25', 'value': 0.02567302059562307}, {'date': '2025-10-26', 'value': 0.02518955349620893}, {'date': '2025-10-27', 'value': 0.025784767865353792}, {'date': '2025-10-28', 'value': 0.0257844613799273}] breakdown=[{'label': 'Carousel Ad - Evening Audience - Summer Sale Campaign', 'value': 0.045697219579236704, 'spend': 510.73, 'clicks': 1729, 'conversions': 88.0, 'revenue': 12486.06, 'impressions': 37836}] workspace_avg=0.02535125290734174
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Carousel Ad - Evening Audience - Summer Sale Campaign had the highest CTR at 4.6% last week—your top performer! For context, your overall CTR was 2.5%, so this ad's really standing out.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1079ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2314ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Carousel Ad - Evening Audience - Summer Sale Campaign had the highest CTR at 4.6% last week—your top performer! For context, your overall CTR was 2.5%, so this ad's really standing out.'
```

---

## Test 15: Show me campaigns with ROAS above 4

**Answer**:
> Here are the campaigns from last week that achieved a Return on Ad Spend (ROAS) above 4:

1. **Summer Sale Campaign**: This campaign had an impressive ROAS of 17.51, with a spend of $441.49 generating $7,730.26 in revenue.

2. **Black Friday Deals**: With a ROAS of 14.94, this campaign spent $308.25 and brought in $4,605.55 in revenue.

3. **General Conversions**: Achieving a ROAS of 14.75, this campaign spent $246.56 and resulted in $3,635.87 in revenue.

4. **Blog Content Promotion**: This campaign had a ROAS of 10.56, with $425.36 spent and $4,492.06 in revenue.

5. **Holiday Sale - Purchases**: With a ROAS of 7.97, this campaign spent $343.06 and generated $2,734.58 in revenue.

6. **Website Traffic Push**: This campaign achieved a ROAS of 7.96, spending $480.89 and earning $3,830.11 in revenue.

In total, there were 6 campaigns that surpassed the ROAS threshold of 4 during the last week.

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
  "top_n": 50,
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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Show me campaigns with ROAS above 4'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'roas', 'operator': '>', 'value': 4}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Show me campaigns with ROAS above 4', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1665ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'roas', 'operator': '>', 'value': 4}]}, top_n=50, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=50, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'roas', 'operator': '>', 'value': 4}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Show me campaigns with ROAS above 4', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.507078653503120199422664633'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for roas by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 50, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=6.50707865350312 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 5.8664627604890764}, {'date': '2025-10-24', 'value': 6.161505000243192}, {'date': '2025-10-25', 'value': 7.76569736303204}, {'date': '2025-10-26', 'value': 6.6619532432258985}, {'date': '2025-10-27', 'value': 6.218785967772876}, {'date': '2025-10-28', 'value': 6.452658599580624}] breakdown=[{'label': 'Summer Sale Campaign', 'value': 17.509479263403474, 'spend': 441.49, 'clicks': 1053, 'conversions': 57.0, 'revenue': 7730.26, 'impressions': 31363}, {'label': 'Black Friday Deals', 'value': 14.94095701540957, 'spend': 308.25, 'clicks': 579, 'conversions': 30.0, 'revenue': 4605.55, 'impressions': 28010}, {'label': 'General Conversions', 'value': 14.746390330953925, 'spend': 246.56, 'clicks': 497, 'conversions': 46.22, 'revenue': 3635.87, 'impressions': 22583}, {'label': 'Blog Content Promotion', 'value': 10.56060748542411, 'spend': 425.36, 'clicks': 658, 'conversions': 82.4, 'revenue': 4492.06, 'impressions': 34881}, {'label': 'Holiday Sale - Purchases', 'value': 7.971142074272722, 'spend': 343.06, 'clicks': 593, 'conversions': 28.0, 'revenue': 2734.58, 'impressions': 30349}, {'label': 'Website Traffic Push', 'value': 7.964628085424941, 'spend': 480.89, 'clicks': 1254, 'conversions': 76.67, 'revenue': 3830.11, 'impressions': 35596}] workspace_avg=6.50707865350312
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are the campaigns from last week that achieved a Return on Ad Spend (ROAS) above 4:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 4109ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 5999ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are the campaigns from last week that achieved a Return on Ad Spend (ROAS) above 4:
```

---

## Test 16: Which campaign generated the most leads?

**Answer**:
> The "Lead Gen - B2B" campaign generated the most leads with 234 last week—your top performer! Overall, your lead generation was right at the average with 4,165 leads in total.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Which campaign generated the most leads?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'leads', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Which campaign generated the most leads?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1236ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['leads'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='leads', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Which campaign generated the most leads?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['leads']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for leads
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for leads: 4164.69
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'leads': MetricValue(value=4164.69, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 4164.69
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for leads by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=4164.69 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 660.36}, {'date': '2025-10-24', 'value': 742.53}, {'date': '2025-10-25', 'value': 632.93}, {'date': '2025-10-26', 'value': 705.34}, {'date': '2025-10-27', 'value': 809.71}, {'date': '2025-10-28', 'value': 613.82}] breakdown=[{'label': 'Lead Gen - B2B', 'value': 234.25, 'spend': 727.78, 'clicks': 1331, 'conversions': 234.25, 'revenue': 1272.83, 'impressions': 42491}] workspace_avg=4164.69
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The "Lead Gen - B2B" campaign generated the most leads with 234 last week—your top performer! Overall, your lead generation was right at the average with 4,165 leads in total.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1808ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3253ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The "Lead Gen - B2B" campaign generated the most leads with 234 last week—your top performer! Overall, your lead generation was right at the average with 4,165 leads in total.'
```

---

## Test 17: Rank platforms by cost per conversion

**Answer**:
> Google had the lowest CPA at $4.00 last week, leading the pack. Your overall average CPA was $5.31, so Google was more cost-efficient than the rest.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Rank platforms by cost per conversion'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpa', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'provider', 'breakdown': 'provider', 'top_n': 10, 'sort_order': 'asc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Rank platforms by cost per conversion', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1620ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='provider', breakdown='provider', derived='cpa', need_timeseries=True, need_previous=False, base_measures=['conversions', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=10, sort_order='asc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpa', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='provider', breakdown='provider', top_n=10, sort_order='asc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Rank platforms by cost per conversion', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpa']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpa
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpa: 5.314210154983342911743130411
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpa': MetricValue(value=Decimal('5.314210154983342911743130411'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 5.314210154983342911743130411
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpa by provider
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: asc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=5.314210154983343 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 5.403955094991365}, {'date': '2025-10-24', 'value': 5.03652698118533}, {'date': '2025-10-25', 'value': 4.962549765203165}, {'date': '2025-10-26', 'value': 5.654007994334908}, {'date': '2025-10-27', 'value': 5.345895624028586}, {'date': '2025-10-28', 'value': 5.52150227183911}] breakdown=[{'label': 'ProviderEnum.google', 'value': 4.0029452474492055, 'spend': 23974.88, 'clicks': 60326, 'conversions': 5989.31, 'revenue': 166884.11, 'impressions': 1739675}, {'label': 'ProviderEnum.meta', 'value': 5.316607776319097, 'spend': 15227.19, 'clicks': 29699, 'conversions': 2864.08, 'revenue': 148567.72, 'impressions': 1512185}, {'label': 'ProviderEnum.tiktok', 'value': 9.154799712245364, 'spend': 10435.19, 'clicks': 20969, 'conversions': 1139.86, 'revenue': 8492.29, 'impressions': 855895}, {'label': 'ProviderEnum.other', 'value': 10.214578330272637, 'spend': 7230.9, 'clicks': 14592, 'conversions': 707.9, 'revenue': 46101.47, 'impressions': 846083}] workspace_avg=5.314210154983343
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Google had the lowest CPA at $4.00 last week, leading the pack. Your overall average CPA was $5.31, so Google was more cost-efficient than the rest.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1163ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3015ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Google had the lowest CPA at $4.00 last week, leading the pack. Your overall average CPA was $5.31, so Google was more cost-efficient than the rest.'
```

---

## Test 18: give me a breakdown of holiday campaign performance

**Answer**:
> Here's a breakdown of our holiday campaign performance from last week:

1. **Weekend Audience - Holiday Sale - Purchases**: This segment generated $20,946.72 in revenue. With a spend of $1,429.02, it achieved 3,035 clicks and 152 conversions from 140,710 impressions.

2. **Morning Audience - Holiday Sale - Purchases**: This group brought in $18,158.96 in revenue. We spent $1,446.47, resulting in 2,474 clicks and 128 conversions, with 130,191 impressions.

3. **Evening Audience - Holiday Sale - Purchases**: This audience contributed $12,887.21 to our revenue. The spend was $879.07, leading to 2,068 clicks and 91 conversions from 101,143 impressions.

Overall, we analyzed three segments in our breakdown for the last week. Each segment performed uniquely, contributing to our holiday campaign's success.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'give me a breakdown of holiday campaign performance'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'give me a breakdown of holiday campaign performance', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1604ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Holiday', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='give me a breakdown of holiday campaign performance', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('3754.5600'), 'revenue': Decimal('51992.8900'), 'clicks': 7577, 'impressions': 372044, 'conversions': Decimal('371.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 371, 'visitors': 6935, 'profit': Decimal('15830.7500')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 370045.59
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=51992.89, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 370045.59
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for revenue by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 5, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity by name (exact first): 'Holiday'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using partial match for 'Holiday': Holiday Sale - Purchases (f2d2c4ee-b550-43ff-a17b-3b6a559a61b9)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Routing named-entity same-level breakdown to child level: campaign→adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=51992.89 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 6087.89}, {'date': '2025-10-24', 'value': 7677.52}, {'date': '2025-10-25', 'value': 13568.85}, {'date': '2025-10-26', 'value': 8844.85}, {'date': '2025-10-27', 'value': 7895.61}, {'date': '2025-10-28', 'value': 7918.17}] breakdown=[{'label': 'Weekend Audience - Holiday Sale - Purchases', 'value': 20946.72, 'spend': 1429.02, 'clicks': 3035, 'conversions': 152.0, 'revenue': 20946.72, 'impressions': 140710}, {'label': 'Morning Audience - Holiday Sale - Purchases', 'value': 18158.96, 'spend': 1446.47, 'clicks': 2474, 'conversions': 128.0, 'revenue': 18158.96, 'impressions': 130191}, {'label': 'Evening Audience - Holiday Sale - Purchases', 'value': 12887.21, 'spend': 879.07, 'clicks': 2068, 'conversions': 91.0, 'revenue': 12887.21, 'impressions': 101143}] workspace_avg=370045.59
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here's a breakdown of our holiday campaign performance from last week:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 3430ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 5569ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here's a breakdown of our holiday campaign performance from last week:
```

---

## Test 19: what is my average order value?

**Answer**:
> Your average order value was $34.58 last week.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'what is my average order value?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'aov', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'what is my average order value?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1016ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived='aov', need_timeseries=False, need_previous=False, base_measures=['purchases', 'revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='aov', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='what is my average order value?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['aov']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for aov
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for aov: 34.57998345972161870453175593
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'aov': MetricValue(value=Decimal('34.57998345972161870453175593'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 34.57998345972161870453175593
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=34.57998345972162 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=34.57998345972162
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your average order value was $34.58 last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1218ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2385ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your average order value was $34.58 last week.'
```

---

## Test 20: give me a list of the top 5 adsets last week by revenue

**Answer**:
> Here are the top 5 ad sets from last week based on revenue:

1. **Morning Audience - Summer Sale Campaign**: This ad set generated $9,777.93 in revenue. It had a spend of $462.05, with 1,353 clicks and 67 conversions from 35,487 impressions.

2. **Evening Audience - Summer Sale Campaign**: This ad set brought in $6,585.33 in revenue. It spent $434.67, garnered 1,153 clicks, and achieved 67 conversions from 37,178 impressions.

3. **Morning Audience - Holiday Sale - Purchases**: This ad set earned $4,452.07 in revenue. It had a spend of $364.16, with 595 clicks and 32 conversions from 32,664 impressions.

4. **Morning Audience - Website Traffic Push**: This ad set generated $4,077.99 in revenue. It spent $448.79, received 1,134 clicks, and achieved 90.6 conversions from 33,941 impressions.

5. **Evening Audience - Website Traffic Push**: This ad set brought in $4,063.25 in revenue. It had a spend of $427.26, with 1,010 clicks and 71.46 conversions from 34,967 impressions.

These ad sets were the top performers in terms of revenue last week, showcasing the effectiveness of targeting different audiences at various times.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'give me a list of the top 5 adsets last week by revenue'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'give me a list of the top 5 adsets last week by revenue', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 2855ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='adset', breakdown='adset', derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='give me a list of the top 5 adsets last week by revenue', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 370045.59
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=370045.59, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 370045.59
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for revenue by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 5, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=370045.59 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 55066.55}, {'date': '2025-10-24', 'value': 58272.68}, {'date': '2025-10-25', 'value': 69017.48}, {'date': '2025-10-26', 'value': 64361.53}, {'date': '2025-10-27', 'value': 62243.58}, {'date': '2025-10-28', 'value': 61083.77}] breakdown=[{'label': 'Morning Audience - Summer Sale Campaign', 'value': 9777.93, 'spend': 462.05, 'clicks': 1353, 'conversions': 67.0, 'revenue': 9777.93, 'impressions': 35487}, {'label': 'Evening Audience - Summer Sale Campaign', 'value': 6585.33, 'spend': 434.67, 'clicks': 1153, 'conversions': 67.0, 'revenue': 6585.33, 'impressions': 37178}, {'label': 'Morning Audience - Holiday Sale - Purchases', 'value': 4452.07, 'spend': 364.16, 'clicks': 595, 'conversions': 32.0, 'revenue': 4452.07, 'impressions': 32664}, {'label': 'Morning Audience - Website Traffic Push', 'value': 4077.99, 'spend': 448.79, 'clicks': 1134, 'conversions': 90.6, 'revenue': 4077.99, 'impressions': 33941}, {'label': 'Evening Audience - Website Traffic Push', 'value': 4063.25, 'spend': 427.26, 'clicks': 1010, 'conversions': 71.46, 'revenue': 4063.25, 'impressions': 34967}] workspace_avg=370045.59
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are the top 5 ad sets from last week based on revenue:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 4699ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 7792ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are the top 5 ad sets from last week based on revenue:
```

---

## Test 21: What was the revenue for the Holiday Sale campaign last week?

**Answer**:
> The revenue for the Holiday Sale campaign was $51,992.89 last week.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'What was the revenue for the Holiday Sale campaign last week?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'What was the revenue for the Holiday Sale campaign last week?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1657ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Holiday Sale', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='What was the revenue for the Holiday Sale campaign last week?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('3754.5600'), 'revenue': Decimal('51992.8900'), 'clicks': 7577, 'impressions': 372044, 'conversions': Decimal('371.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 371, 'visitors': 6935, 'profit': Decimal('15830.7500')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 370045.59
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=51992.89, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 370045.59
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=51992.89 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=370045.59
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The revenue for the Holiday Sale campaign was $51,992.89 last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1208ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3130ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The revenue for the Holiday Sale campaign was $51,992.89 last week.'
```

---

## Test 22: wich day had the lowest cpc on holiday sale campaign?

**Answer**:
> The day with the lowest CPC during your holiday sale campaign was October 28, with a CPC of $0.43—your best performer last week! For context, the average CPC for the week was $0.45.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'wich day had the lowest cpc on holiday sale campaign?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpc', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'day', 'breakdown': 'day', 'top_n': 1, 'sort_order': 'asc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'wich day had the lowest cpc on holiday sale campaign?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1307ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='day', breakdown='day', derived='cpc', need_timeseries=True, need_previous=False, base_measures=['clicks', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, top_n=1, sort_order='asc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpc', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='day', breakdown='day', top_n=1, sort_order='asc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Holiday Sale', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='wich day had the lowest cpc on holiday sale campaign?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('3754.5600'), 'revenue': Decimal('51992.8900'), 'clicks': 7577, 'impressions': 372044, 'conversions': Decimal('371.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 371, 'visitors': 6935, 'profit': Decimal('15830.7500')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4528224483620785756374118134
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.4955206546126435264616602877'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4528224483620785756374118134
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting time-based breakdown for cpc by day
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.49552065461264355 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 0.5838761238761239}, {'date': '2025-10-24', 'value': 0.5469913589945011}, {'date': '2025-10-25', 'value': 0.4448214285714286}, {'date': '2025-10-26', 'value': 0.48990188679245283}, {'date': '2025-10-27', 'value': 0.49471641791044774}, {'date': '2025-10-28', 'value': 0.4349238578680203}] breakdown=[{'label': '2025-10-28', 'value': 0.4349238578680203, 'spend': 514.08, 'clicks': 1182, 'conversions': 58.0, 'revenue': 7918.17, 'impressions': 60498}] workspace_avg=0.4528224483620786
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The day with the lowest CPC during your holiday sale campaign was October 28, with a CPC of $0.43—your best performer last week! For context, the average CPC for the week was $0.45.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1844ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3819ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The day with the lowest CPC during your holiday sale campaign was October 28, with a CPC of $0.43—your best performer last week! For context, the average CPC for the week was $0.45.'
```

---

## Test 23: roas last month for holiday sale campaign?

**Answer**:
> The ROAS for your Holiday Sale campaign was 11.65× in the last 30 days, which is excellent! That's way above your workspace average of 6.25×, so you're definitely seeing some strong returns.

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
  "timeframe_description": "last month",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'roas last month for holiday sale campaign?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 30, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'roas last month for holiday sale campaign?', 'timeframe_description': 'last month', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 3472ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 30), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived='roas', need_timeseries=False, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=30, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Holiday Sale', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='roas last month for holiday sale campaign?', timeframe_description='last month', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 30) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-30 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('18581.2700'), 'revenue': Decimal('216432.7500'), 'clicks': 36506, 'impressions': 1873941, 'conversions': Decimal('1634.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 1634, 'visitors': 33408, 'profit': Decimal('65638.4300')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.251952542126272547931877219
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('11.64789866354667899449284145'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.251952542126272547931877219
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=11.647898663546679 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=6.251952542126273
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The ROAS for your Holiday Sale campaign was 11.65× in the last 30 days, which is excellent! That's way above your workspace average of 6.25×, so you're definitely seeing some strong returns.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 2105ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 7293ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The ROAS for your Holiday Sale campaign was 11.65× in the last 30 days, which is excellent! That's way above your workspace average of 6.25×, so you're definitely seeing some strong returns.'
```

---

## Test 24: wich had highest cpc, holiday campaign or app install campaign?

**Answer**:
> Last week, the Holiday Sale campaign had a higher cost per click (CPC) compared to the App Install campaign. The CPC for the Holiday Sale was approximately $0.50, while the App Install campaign had a CPC of about $0.41. This means that the Holiday Sale campaign was more expensive per click than the App Install campaign.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'wich had highest cpc, holiday campaign or app install campaign?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.COMPARISON: 'comparison'>, 'metric': None, 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': 'entity_vs_entity', 'comparison_entities': ['Holiday Sale', 'App Install'], 'comparison_metrics': ['cpc'], 'question': 'wich had highest cpc, holiday campaign or app install campaign?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1456ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived='cpc', need_timeseries=False, need_previous=False, base_measures=['clicks', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.COMPARISON: 'comparison'>, metric=None, time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type='entity_vs_entity', comparison_entities=['Holiday Sale', 'App Install'], comparison_metrics=['cpc'], question='wich had highest cpc, holiday campaign or app install campaign?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.dsl.executor:[COMPARISON] Executing comparison plan for type: entity_vs_entity
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('3754.5600'), 'revenue': Decimal('51992.8900'), 'clicks': 7577, 'impressions': 372044, 'conversions': Decimal('371.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 371, 'visitors': 6935, 'profit': Decimal('15830.7500')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4528224483620785756374118134
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.4955206546126435264616602877'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4528224483620785756374118134
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=App Install
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('5788.0300'), 'revenue': Decimal('3337.7400'), 'clicks': 13991, 'impressions': 409439, 'conversions': Decimal('1416.0000'), 'leads': Decimal('0'), 'installs': 1416, 'purchases': 0, 'visitors': 0, 'profit': Decimal('953.3000')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4528224483620785756374118134
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.4136966621399471088556929455'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4528224483620785756374118134
INFO:app.dsl.executor:[COMPARISON] Completed execution for 2 items
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'comparison': [{'entity': 'Holiday Sale', 'cpc': Decimal('0.4955206546126435264616602877')}, {'entity': 'App Install', 'cpc': Decimal('0.4136966621399471088556929455')}], 'comparison_type': 'entity_vs_entity', 'metrics': ['cpc'], 'query_type': 'comparison'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Last week, the Holiday Sale campaign had a higher cost per click (CPC) compared to the App Install campaign. The CPC for the Holiday Sale was approximately $0.50, while the App Install campaign had a CPC of about $0.41. This means that the Holiday Sale campaign was more expensive per click than the App Install campaign.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 7648ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 9662ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Last week, the Holiday Sale campaign had a higher cost per click (CPC) compared to the App Install campaign. The CPC for the Holiday Sale was approximately $0.50, while the App Install campaign had a CPC of about $0.41. This means that the Holiday Sale campaign was more expensive per click than the App Install campaign.'
```

---

## Test 25: wich google campaigns are live?

**Answer**:
> Here are your 4 campaigns:
1. App Install Campaign
2. Lead Gen - B2B
3. Summer Sale Campaign
4. Website Traffic Push

**DSL**:
```json
{
  "query_type": "entities",
  "metric": null,
  "time_range": null,
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 50,
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
  "timeframe_description": null,
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'wich google campaigns are live?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.ENTITIES: 'entities'>, 'metric': None, 'time_range': None, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': 'google', 'level': 'campaign', 'entity_ids': None, 'status': 'active', 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'wich google campaigns are live?', 'timeframe_description': None, 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 938ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: None
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: campaign
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'entities': [{'name': 'App Install Campaign', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Lead Gen - B2B', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Summer Sale Campaign', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Website Traffic Push', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}]}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your 4 campaigns:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1128ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your 4 campaigns:
```

---

## Test 26: what is my revenue this month?

**Answer**:
> Your revenue is $1,673,577.62 from October 01 to 29.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "revenue",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-29"
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
  "timeframe_description": "this month",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'what is my revenue this month?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 10, 1), 'end': datetime.date(2025, 10, 29)}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'what is my revenue this month?', 'timeframe_description': 'this month', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1285ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 29)), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='what is my revenue this month?', timeframe_description='this month', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('268552.7100'), 'revenue': Decimal('1673577.6200'), 'clicks': 593809, 'impressions': 23402098, 'conversions': Decimal('50121.9000'), 'leads': Decimal('19608.4100'), 'installs': 11733, 'purchases': 6792, 'visitors': 426056, 'profit': Decimal('503172.8300')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 1673577.62
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=1673577.62, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 1673577.62
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=1673577.62 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=1673577.62
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your revenue is $1,673,577.62 from October 01 to 29.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 988ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2419ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your revenue is $1,673,577.62 from October 01 to 29.'
```

---

## Test 27: what was my revenue last month?

**Answer**:
> Your revenue was $1,741,103.20 in the last 30 days.

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
  "timeframe_description": "last month",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'what was my revenue last month?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 30, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'what was my revenue last month?', 'timeframe_description': 'last month', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 942ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 30), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=30, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='what was my revenue last month?', timeframe_description='last month', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 30) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-30 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('278489.5100'), 'revenue': Decimal('1741103.2000'), 'clicks': 615725, 'impressions': 24249976, 'conversions': Decimal('52012.9000'), 'leads': Decimal('20459.2400'), 'installs': 12080, 'purchases': 7047, 'visitors': 442102, 'profit': Decimal('523625.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 1741103.2
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=1741103.2, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 1741103.2
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=1741103.2 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=1741103.2
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your revenue was $1,741,103.20 in the last 30 days.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 773ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1861ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your revenue was $1,741,103.20 in the last 30 days.'
```

---

## Test 28: what is my revenue this year?

**Answer**:
> Your revenue was $1,803,597.38 in the last 365 days.

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
  "timeframe_description": "last year",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'what is my revenue this year?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 365, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'what is my revenue this year?', 'timeframe_description': 'last year', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1238ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2024, 10, 30), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=365, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='what is my revenue this year?', timeframe_description='last year', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2024, 10, 30) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2024-10-30 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('288394.8500'), 'revenue': Decimal('1803597.3800'), 'clicks': 636793, 'impressions': 25074397, 'conversions': Decimal('53834.9400'), 'leads': Decimal('21204.2800'), 'installs': 12443, 'purchases': 7325, 'visitors': 457334, 'profit': Decimal('541927.9400')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 1803597.38
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=1803597.38, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 1803597.38
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=1803597.38 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=1803597.38
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your revenue was $1,803,597.38 in the last 365 days.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 753ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2139ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your revenue was $1,803,597.38 in the last 365 days.'
```

---

## Test 29: How does this week compare to last week?

**Answer**:
> This week, the revenue is $370,045.59, which is a decrease compared to last week's revenue of $424,299.64. This represents a drop of about 12.8%. Last week performed better in terms of revenue.

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
  "comparison_type": "time_vs_time",
  "comparison_entities": null,
  "comparison_metrics": [
    "revenue"
  ],
  "question": "How does this week compare to last week?",
  "timeframe_description": "this week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'How does this week compare to last week?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.COMPARISON: 'comparison'>, 'metric': None, 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': True, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': 'time_vs_time', 'comparison_entities': None, 'comparison_metrics': ['revenue'], 'question': 'How does this week compare to last week?', 'timeframe_description': 'this week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1453ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=True, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.COMPARISON: 'comparison'>, metric=None, time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=True, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type='time_vs_time', comparison_entities=None, comparison_metrics=['revenue'], question='How does this week compare to last week?', timeframe_description='this week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.dsl.executor:[COMPARISON] Executing comparison plan for type: time_vs_time
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 370045.59
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=370045.59, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 370045.59
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 16) end=datetime.date(2025, 10, 22)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-16 to 2025-10-22
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('68465.8500'), 'revenue': Decimal('424299.6400'), 'clicks': 151675, 'impressions': 5915363, 'conversions': Decimal('12690.8000'), 'leads': Decimal('4852.1300'), 'installs': 3116, 'purchases': 1762, 'visitors': 106300, 'profit': Decimal('129644.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 424299.64
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=424299.64, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 424299.64
INFO:app.dsl.executor:[COMPARISON] time_vs_time computed for metrics=['revenue']
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'comparison': [{'period': 'current', 'revenue': 370045.59}, {'period': 'previous', 'revenue': 424299.64}], 'comparison_type': 'time_vs_time', 'metrics': ['revenue'], 'query_type': 'comparison'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'This week, the revenue is $370,045.59, which is a decrease compared to last week's revenue of $424,299.64. This represents a drop of about 12.8%. Last week performed better in terms of revenue.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1926ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3589ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'This week, the revenue is $370,045.59, which is a decrease compared to last week's revenue of $424,299.64. This represents a drop of about 12.8%. Last week performed better in terms of revenue.'
```

---

## Test 30: Compare Google vs Meta performance

**Answer**:
> In the last 30 days, when comparing the performance of Google and Meta based on Return on Advertising Spend (ROAS), Meta has outperformed Google. Meta achieved a ROAS of 9.11, indicating a higher return on each dollar spent on advertising. In contrast, Google's ROAS was 6.61. This suggests that, for this period, Meta provided a more effective return on advertising investment compared to Google.

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
  "timeframe_description": "last month",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Compare Google vs Meta performance'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.COMPARISON: 'comparison'>, 'metric': None, 'time_range': {'last_n_days': 30, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': 'provider_vs_provider', 'comparison_entities': None, 'comparison_metrics': ['roas'], 'question': 'Compare Google vs Meta performance', 'timeframe_description': 'last month', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1233ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 30), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived='roas', need_timeseries=False, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.COMPARISON: 'comparison'>, metric=None, time_range=TimeRange(last_n_days=30, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type='provider_vs_provider', comparison_entities=None, comparison_metrics=['roas'], question='Compare Google vs Meta performance', timeframe_description='last month', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.dsl.executor:[COMPARISON] Executing comparison plan for type: provider_vs_provider
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 30) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=google, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-30 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('116415.3100'), 'revenue': Decimal('769167.3200'), 'clicks': 289658, 'impressions': 8306314, 'conversions': Decimal('28515.9600'), 'leads': Decimal('13257.8200'), 'installs': 7227, 'purchases': 3397, 'visitors': 195984, 'profit': Decimal('232968.8600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.251952542126272547931877219
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.607097640336137918629431129'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.251952542126272547931877219
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 30) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=meta, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-30 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('75148.2800'), 'revenue': Decimal('684604.1600'), 'clicks': 148975, 'impressions': 7523234, 'conversions': Decimal('14082.8500'), 'leads': Decimal('7201.4200'), 'installs': 0, 'purchases': 3650, 'visitors': 135419, 'profit': Decimal('205015.9700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.251952542126272547931877219
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('9.110044301745828380902397234'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.251952542126272547931877219
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 30) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=tiktok, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-30 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('50540.5800'), 'revenue': Decimal('45120.1600'), 'clicks': 103688, 'impressions': 4208758, 'conversions': Decimal('5817.3900'), 'leads': Decimal('0'), 'installs': 4853, 'purchases': 0, 'visitors': 46816, 'profit': Decimal('13519.4100')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.251952542126272547931877219
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('0.8927511318627526633054072589'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.251952542126272547931877219
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 30) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=other, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-30 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('36385.3400'), 'revenue': Decimal('242211.5600'), 'clicks': 73404, 'impressions': 4211670, 'conversions': Decimal('3596.7000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 0, 'visitors': 63883, 'profit': Decimal('72121.0300')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.251952542126272547931877219
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.656844762203678734347404751'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.251952542126272547931877219
INFO:app.dsl.executor:[COMPARISON] Completed execution for 4 items
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'comparison': [{'provider': 'google', 'roas': Decimal('6.607097640336137918629431129')}, {'provider': 'meta', 'roas': Decimal('9.110044301745828380902397234')}, {'provider': 'tiktok', 'roas': Decimal('0.8927511318627526633054072589')}, {'provider': 'other', 'roas': Decimal('6.656844762203678734347404751')}], 'comparison_type': 'provider_vs_provider', 'metrics': ['roas'], 'query_type': 'comparison'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'In the last 30 days, when comparing the performance of Google and Meta based on Return on Advertising Spend (ROAS), Meta has outperformed Google. Meta achieved a ROAS of 9.11, indicating a higher return on each dollar spent on advertising. In contrast, Google's ROAS was 6.61. This suggests that, for this period, Meta provided a more effective return on advertising investment compared to Google.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 2842ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 4432ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'In the last 30 days, when comparing the performance of Google and Meta based on Return on Advertising Spend (ROAS), Meta has outperformed Google. Meta achieved a ROAS of 9.11, indicating a higher return on each dollar spent on advertising. In contrast, Google's ROAS was 6.61. This suggests that, for this period, Meta provided a more effective return on advertising investment compared to Google.'
```

---

## Test 31: Is my ROAS improving or declining?

**Answer**:
> Your ROAS was 6.34× in the last 14 days, which is a nice 2.5% improvement from 6.18× in the previous period. It's right on par with your workspace average, so you're holding steady.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "roas",
  "time_range": {
    "last_n_days": 14,
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
  "timeframe_description": "last 14 days",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Is my ROAS improving or declining?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 14, 'start': None, 'end': None}, 'compare_to_previous': True, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Is my ROAS improving or declining?', 'timeframe_description': 'last 14 days', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1110ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 16), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived='roas', need_timeseries=True, need_previous=True, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=14, start=None, end=None), compare_to_previous=True, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Is my ROAS improving or declining?', timeframe_description='last 14 days', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 16) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-16 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('125334.0100'), 'revenue': Decimal('794345.2300'), 'clicks': 277261, 'impressions': 10869201, 'conversions': Decimal('23391.9500'), 'leads': Decimal('9016.8200'), 'installs': 5564, 'purchases': 3290, 'visitors': 197124, 'profit': Decimal('241567.0300')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Previous period dates: 2025-10-02 to 2025-10-15
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Previous period totals: {'spend': Decimal('134250.9300'), 'revenue': Decimal('829866.7100'), 'clicks': 297473, 'impressions': 11728916, 'conversions': Decimal('25061.2300'), 'leads': Decimal('9904.4600'), 'installs': 5782, 'purchases': 3337, 'visitors': 214926, 'profit': Decimal('247028.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.337826660137978510381978523
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.337826660137978510381978523'), previous=Decimal('6.181459674059613590758738133'), delta_pct=Decimal('0.02529612653376292602313842903'))}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.337826660137978510381978523
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=6.337826660137979 previous=6.181459674059614 delta_pct=0.025296126533762925 timeseries=[{'date': '2025-10-16', 'value': 6.305414582533697}, {'date': '2025-10-17', 'value': 6.167299959457189}, {'date': '2025-10-18', 'value': 6.206117972767664}, {'date': '2025-10-19', 'value': 6.060904068093095}, {'date': '2025-10-20', 'value': 6.249336303504189}, {'date': '2025-10-21', 'value': 7.0186976872332245}, {'date': '2025-10-22', 'value': 5.406129400923143}, {'date': '2025-10-23', 'value': 5.8664627604890764}, {'date': '2025-10-24', 'value': 6.161505000243192}, {'date': '2025-10-25', 'value': 7.76569736303204}, {'date': '2025-10-26', 'value': 6.6619532432258985}, {'date': '2025-10-27', 'value': 6.218785967772876}, {'date': '2025-10-28', 'value': 6.452658599580624}] breakdown=None workspace_avg=6.337826660137979
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your ROAS was 6.34× in the last 14 days, which is a nice 2.5% improvement from 6.18× in the previous period. It's right on par with your workspace average, so you're holding steady.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1266ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2590ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your ROAS was 6.34× in the last 14 days, which is a nice 2.5% improvement from 6.18× in the previous period. It's right on par with your workspace average, so you're holding steady.'
```

---

## Test 32: compare holiday campaign performance to app install campaign performance

**Answer**:
> Over the last week, the performance of the Holiday Sale campaign significantly outshined the App Install campaign across all key metrics.

Starting with Return on Ad Spend (ROAS), the Holiday Sale campaign achieved an impressive ROAS of 13.85, indicating that for every dollar spent, it generated $13.85 in revenue. In contrast, the App Install campaign had a much lower ROAS of 0.58, meaning it only brought in $0.58 for every dollar spent. Clearly, the Holiday Sale campaign was far more efficient in converting ad spend into revenue.

In terms of revenue, the Holiday Sale campaign also led the way, generating $51,992.89. This is substantially higher than the $3,337.74 generated by the App Install campaign. This further underscores the Holiday Sale's superior performance in driving sales.

Lastly, when we look at ad spend, the Holiday Sale campaign spent $3,754.56, which is less than the $5,788.03 spent on the App Install campaign. Despite the lower spend, the Holiday Sale campaign achieved far greater revenue, highlighting its cost-effectiveness.

Overall, the Holiday Sale campaign was the clear winner in terms of efficiency and effectiveness, outperforming the App Install campaign in ROAS, revenue, and spend efficiency.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'compare holiday campaign performance to app install campaign performance'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.COMPARISON: 'comparison'>, 'metric': None, 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': 'entity_vs_entity', 'comparison_entities': ['Holiday Sale', 'App Install'], 'comparison_metrics': ['roas', 'revenue', 'spend'], 'question': 'compare holiday campaign performance to app install campaign performance', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1473ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.COMPARISON: 'comparison'>, metric=None, time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type='entity_vs_entity', comparison_entities=['Holiday Sale', 'App Install'], comparison_metrics=['roas', 'revenue', 'spend'], question='compare holiday campaign performance to app install campaign performance', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.dsl.executor:[COMPARISON] Executing comparison plan for type: entity_vs_entity
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['roas', 'revenue', 'spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('3754.5600'), 'revenue': Decimal('51992.8900'), 'clicks': 7577, 'impressions': 372044, 'conversions': Decimal('371.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 371, 'visitors': 6935, 'profit': Decimal('15830.7500')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('13.84793158186312111139521009'), previous=None, delta_pct=None), 'revenue': MetricValue(value=51992.89, previous=None, delta_pct=None), 'spend': MetricValue(value=3754.56, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['roas', 'revenue', 'spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=App Install
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('5788.0300'), 'revenue': Decimal('3337.7400'), 'clicks': 13991, 'impressions': 409439, 'conversions': Decimal('1416.0000'), 'leads': Decimal('0'), 'installs': 1416, 'purchases': 0, 'visitors': 0, 'profit': Decimal('953.3000')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('0.5766625259371496001230124930'), previous=None, delta_pct=None), 'revenue': MetricValue(value=3337.74, previous=None, delta_pct=None), 'spend': MetricValue(value=5788.03, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.507078653503120199422664633
INFO:app.dsl.executor:[COMPARISON] Completed execution for 2 items
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'comparison': [{'entity': 'Holiday Sale', 'roas': Decimal('13.84793158186312111139521009'), 'revenue': 51992.89, 'spend': 3754.56}, {'entity': 'App Install', 'roas': Decimal('0.5766625259371496001230124930'), 'revenue': 3337.74, 'spend': 5788.03}], 'comparison_type': 'entity_vs_entity', 'metrics': ['roas', 'revenue', 'spend'], 'query_type': 'comparison'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Over the last week, the performance of the Holiday Sale campaign significantly outshined the App Install campaign across all key metrics.
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 6090ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 7920ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Over the last week, the performance of the Holiday Sale campaign significantly outshined the App Install campaign across all key metrics.
```

---

## Test 33: Which campaign had the highest ROAS last week?

**Answer**:
> The Summer Sale Campaign had the highest ROAS at 17.51× last week—crushing it as your top performer! For context, your overall ROAS was 6.51×, so this campaign really stood out.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Which campaign had the highest ROAS last week?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Which campaign had the highest ROAS last week?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1136ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Which campaign had the highest ROAS last week?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.507078653503120199422664633'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for roas by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=6.50707865350312 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 5.8664627604890764}, {'date': '2025-10-24', 'value': 6.161505000243192}, {'date': '2025-10-25', 'value': 7.76569736303204}, {'date': '2025-10-26', 'value': 6.6619532432258985}, {'date': '2025-10-27', 'value': 6.218785967772876}, {'date': '2025-10-28', 'value': 6.452658599580624}] breakdown=[{'label': 'Summer Sale Campaign', 'value': 17.509479263403474, 'spend': 441.49, 'clicks': 1053, 'conversions': 57.0, 'revenue': 7730.26, 'impressions': 31363}] workspace_avg=6.50707865350312
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Summer Sale Campaign had the highest ROAS at 17.51× last week—crushing it as your top performer! For context, your overall ROAS was 6.51×, so this campaign really stood out.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1352ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2734ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Summer Sale Campaign had the highest ROAS at 17.51× last week—crushing it as your top performer! For context, your overall ROAS was 6.51×, so this campaign really stood out.'
```

---

## Test 34: Show me top 5 campaigns by revenue

**Answer**:
> Here are the top 5 campaigns by revenue from last week:

1. **Summer Sale Campaign**: This campaign led the pack with a revenue of $7,730.26.
2. **Black Friday Deals**: Coming in second, it generated $4,605.55 in revenue.
3. **Blog Content Promotion**: This campaign earned $4,492.06.
4. **Website Traffic Push**: It brought in $3,830.11.
5. **General Conversions**: Rounding out the list, this campaign achieved $3,635.87 in revenue.

These campaigns were the top performers in terms of revenue, with a total of five campaigns analyzed.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Show me top 5 campaigns by revenue'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Show me top 5 campaigns by revenue', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1195ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Show me top 5 campaigns by revenue', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 370045.59
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=370045.59, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 370045.59
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for revenue by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 5, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=370045.59 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 55066.55}, {'date': '2025-10-24', 'value': 58272.68}, {'date': '2025-10-25', 'value': 69017.48}, {'date': '2025-10-26', 'value': 64361.53}, {'date': '2025-10-27', 'value': 62243.58}, {'date': '2025-10-28', 'value': 61083.77}] breakdown=[{'label': 'Summer Sale Campaign', 'value': 7730.26, 'spend': 441.49, 'clicks': 1053, 'conversions': 57.0, 'revenue': 7730.26, 'impressions': 31363}, {'label': 'Black Friday Deals', 'value': 4605.55, 'spend': 308.25, 'clicks': 579, 'conversions': 30.0, 'revenue': 4605.55, 'impressions': 28010}, {'label': 'Blog Content Promotion', 'value': 4492.06, 'spend': 425.36, 'clicks': 658, 'conversions': 82.4, 'revenue': 4492.06, 'impressions': 34881}, {'label': 'Website Traffic Push', 'value': 3830.11, 'spend': 480.89, 'clicks': 1254, 'conversions': 76.67, 'revenue': 3830.11, 'impressions': 35596}, {'label': 'General Conversions', 'value': 3635.87, 'spend': 246.56, 'clicks': 497, 'conversions': 46.22, 'revenue': 3635.87, 'impressions': 22583}] workspace_avg=370045.59
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are the top 5 campaigns by revenue from last week:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 3301ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 4713ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are the top 5 campaigns by revenue from last week:
```

---

## Test 35: List all active campaigns

**Answer**:
> Here are your 11 campaigns:
1. App Install Campaign
2. Black Friday Deals
3. Brand Awareness
4. General Conversions
5. Holiday Sale - Purchases
6. Lead Gen - B2B
7. Mobile Game Installs
8. Newsletter Signup Campaign
9. Product Launch Teaser
10. Summer Sale Campaign
11. Website Traffic Push

**DSL**:
```json
{
  "query_type": "entities",
  "metric": null,
  "time_range": null,
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 50,
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
  "timeframe_description": null,
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'List all active campaigns'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.ENTITIES: 'entities'>, 'metric': None, 'time_range': None, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': 'campaign', 'entity_ids': None, 'status': 'active', 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'List all active campaigns', 'timeframe_description': None, 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 879ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: None
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: campaign
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'entities': [{'name': 'App Install Campaign', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Black Friday Deals', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Brand Awareness', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'General Conversions', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Holiday Sale - Purchases', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Lead Gen - B2B', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Mobile Game Installs', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Newsletter Signup Campaign', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Product Launch Teaser', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Summer Sale Campaign', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Website Traffic Push', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}]}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your 11 campaigns:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 992ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your 11 campaigns:
```

---

## Test 36: Which adset had the highest cpc last week?

**Answer**:
> The Weekend Audience - Black Friday Deals adset had the highest CPC at $0.71 last week—your worst performer. For context, your overall CPC was $0.45, so this adset's cost was significantly higher than average.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Which adset had the highest cpc last week?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpc', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Which adset had the highest cpc last week?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1114ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='adset', breakdown='adset', derived='cpc', need_timeseries=True, need_previous=False, base_measures=['clicks', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpc', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Which adset had the highest cpc last week?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4528224483620785756374118134
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.4528224483620785756374118134'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4528224483620785756374118134
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpc by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.4528224483620786 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 0.46385995255979445}, {'date': '2025-10-24', 'value': 0.44097263020469063}, {'date': '2025-10-25', 'value': 0.4323966137978009}, {'date': '2025-10-26', 'value': 0.4615891065456283}, {'date': '2025-10-27', 'value': 0.45648818753990694}, {'date': '2025-10-28', 'value': 0.4619357829502757}] breakdown=[{'label': 'Weekend Audience - Black Friday Deals', 'value': 0.7116336633663366, 'spend': 431.25, 'clicks': 606, 'conversions': 24.0, 'revenue': 3317.55, 'impressions': 40871}] workspace_avg=0.4528224483620786
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Weekend Audience - Black Friday Deals adset had the highest CPC at $0.71 last week—your worst performer. For context, your overall CPC was $0.45, so this adset's cost was significantly higher than average.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1699ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3215ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Weekend Audience - Black Friday Deals adset had the highest CPC at $0.71 last week—your worst performer. For context, your overall CPC was $0.45, so this adset's cost was significantly higher than average.'
```

---

## Test 37: Which adset had the highest cpc last week?

**Answer**:
> The Weekend Audience - Black Friday Deals adset had the highest CPC at $0.71 last week—it's your worst performer. For context, your overall CPC was $0.45, so this adset is definitely on the higher end.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Which adset had the highest cpc last week?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpc', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Which adset had the highest cpc last week?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1184ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='adset', breakdown='adset', derived='cpc', need_timeseries=True, need_previous=False, base_measures=['clicks', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpc', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Which adset had the highest cpc last week?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4528224483620785756374118134
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.4528224483620785756374118134'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4528224483620785756374118134
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpc by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.4528224483620786 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 0.46385995255979445}, {'date': '2025-10-24', 'value': 0.44097263020469063}, {'date': '2025-10-25', 'value': 0.4323966137978009}, {'date': '2025-10-26', 'value': 0.4615891065456283}, {'date': '2025-10-27', 'value': 0.45648818753990694}, {'date': '2025-10-28', 'value': 0.4619357829502757}] breakdown=[{'label': 'Weekend Audience - Black Friday Deals', 'value': 0.7116336633663366, 'spend': 431.25, 'clicks': 606, 'conversions': 24.0, 'revenue': 3317.55, 'impressions': 40871}] workspace_avg=0.4528224483620786
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Weekend Audience - Black Friday Deals adset had the highest CPC at $0.71 last week—it's your worst performer. For context, your overall CPC was $0.45, so this adset is definitely on the higher end.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 2208ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3616ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Weekend Audience - Black Friday Deals adset had the highest CPC at $0.71 last week—it's your worst performer. For context, your overall CPC was $0.45, so this adset is definitely on the higher end.'
```

---

## Test 38: Which adset had the lowest ctr last week?

**Answer**:
> The Evening Audience - General Conversions adset had the lowest CTR at 1.5% last week—definitely needs some attention. For context, your overall CTR was 2.5%, so this adset is underperforming compared to the average.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Which adset had the lowest ctr last week?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'ctr', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 1, 'sort_order': 'asc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Which adset had the lowest ctr last week?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1222ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='adset', breakdown='adset', derived='ctr', need_timeseries=True, need_previous=False, base_measures=['clicks', 'impressions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='asc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='ctr', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=1, sort_order='asc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Which adset had the lowest ctr last week?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['ctr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for ctr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for ctr: 0.02535125290734174
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'ctr': MetricValue(value=0.02535125290734174, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.02535125290734174
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for ctr by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: asc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.02535125290734174 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 0.024331210344251276}, {'date': '2025-10-24', 'value': 0.025365635577885168}, {'date': '2025-10-25', 'value': 0.02567302059562307}, {'date': '2025-10-26', 'value': 0.02518955349620893}, {'date': '2025-10-27', 'value': 0.025784767865353792}, {'date': '2025-10-28', 'value': 0.0257844613799273}] breakdown=[{'label': 'Evening Audience - General Conversions', 'value': 0.01459170013386881, 'spend': 302.25, 'clicks': 436, 'conversions': 39.07, 'revenue': 3053.46, 'impressions': 29880}] workspace_avg=0.02535125290734174
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Evening Audience - General Conversions adset had the lowest CTR at 1.5% last week—definitely needs some attention. For context, your overall CTR was 2.5%, so this adset is underperforming compared to the average.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1525ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3015ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Evening Audience - General Conversions adset had the lowest CTR at 1.5% last week—definitely needs some attention. For context, your overall CTR was 2.5%, so this adset is underperforming compared to the average.'
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
  "timeframe_description": "last month",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'what is my total CVR last month?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cvr', 'time_range': {'last_n_days': 30, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'what is my total CVR last month?', 'timeframe_description': 'last month', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1888ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 30), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived='cvr', need_timeseries=False, need_previous=False, base_measures=['clicks', 'conversions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cvr', time_range=TimeRange(last_n_days=30, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='what is my total CVR last month?', timeframe_description='last month', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cvr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 30) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-30 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('278489.5100'), 'revenue': Decimal('1741103.2000'), 'clicks': 615725, 'impressions': 24249976, 'conversions': Decimal('52012.9000'), 'leads': Decimal('20459.2400'), 'installs': 12080, 'purchases': 7047, 'visitors': 442102, 'profit': Decimal('523625.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cvr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cvr: 0.08447423768727922367940233059
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cvr': MetricValue(value=Decimal('0.08447423768727922367940233059'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.08447423768727922367940233059
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.08447423768727923 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=0.08447423768727923
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your total CVR was 8.4% in the last 30 days.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1487ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3539ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your total CVR was 8.4% in the last 30 days.'
```

---

## Test 40: what is my cvr on google last month?

**Answer**:
> Your CVR was 9.8% in the last 30 days.

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
  "timeframe_description": "last month",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'what is my cvr on google last month?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cvr', 'time_range': {'last_n_days': 30, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': 'google', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'what is my cvr on google last month?', 'timeframe_description': 'last month', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1080ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 30), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived='cvr', need_timeseries=False, need_previous=False, base_measures=['clicks', 'conversions'], filters={'provider': 'google', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cvr', time_range=TimeRange(last_n_days=30, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider='google', level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='what is my cvr on google last month?', timeframe_description='last month', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cvr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 30) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=google, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-30 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('116415.3100'), 'revenue': Decimal('769167.3200'), 'clicks': 289658, 'impressions': 8306314, 'conversions': Decimal('28515.9600'), 'leads': Decimal('13257.8200'), 'installs': 7227, 'purchases': 3397, 'visitors': 195984, 'profit': Decimal('232968.8600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cvr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cvr: 0.08447423768727922367940233059
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cvr': MetricValue(value=Decimal('0.09844699611265699549123449033'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.08447423768727922367940233059
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.09844699611265699 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=0.08447423768727923
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your CVR was 9.8% in the last 30 days.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1219ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2478ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your CVR was 9.8% in the last 30 days.'
```

---

## Test 41: how much did i spent last month?

**Answer**:
> You spent $278,489.51 in the last 30 days.

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
    "entity_name": null,
    "metric_filters": null
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "how much did i spent last month?",
  "timeframe_description": "last month",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'how much did i spent last month?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'spend', 'time_range': {'last_n_days': 30, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'how much did i spent last month?', 'timeframe_description': 'last month', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 910ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 30), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='spend', time_range=TimeRange(last_n_days=30, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='how much did i spent last month?', timeframe_description='last month', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 30) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-30 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('278489.5100'), 'revenue': Decimal('1741103.2000'), 'clicks': 615725, 'impressions': 24249976, 'conversions': Decimal('52012.9000'), 'leads': Decimal('20459.2400'), 'installs': 12080, 'purchases': 7047, 'visitors': 442102, 'profit': Decimal('523625.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 278489.51
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=278489.51, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 278489.51
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=278489.51 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=278489.51
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'You spent $278,489.51 in the last 30 days.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 789ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1846ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'You spent $278,489.51 in the last 30 days.'
```

---

## Test 42: wich campaign had the highest spend?

**Answer**:
> The "Lead Gen - B2B" campaign had the highest spend at $727.78 last week—your top performer! For context, this was right on par with your overall average spend of $56,868.16.

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
  "question": "wich campaign had the highest spend?",
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'wich campaign had the highest spend?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'spend', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'wich campaign had the highest spend?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1434ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='spend', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='wich campaign had the highest spend?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 56868.16
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=56868.16, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 56868.16
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for spend by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=56868.16 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 9386.67}, {'date': '2025-10-24', 'value': 9457.54}, {'date': '2025-10-25', 'value': 8887.48}, {'date': '2025-10-26', 'value': 9661.06}, {'date': '2025-10-27', 'value': 10008.96}, {'date': '2025-10-28', 'value': 9466.45}] breakdown=[{'label': 'Lead Gen - B2B', 'value': 727.78, 'spend': 727.78, 'clicks': 1331, 'conversions': 234.25, 'revenue': 1272.83, 'impressions': 42491}] workspace_avg=56868.16
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The "Lead Gen - B2B" campaign had the highest spend at $727.78 last week—your top performer! For context, this was right on par with your overall average spend of $56,868.16.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 3451ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 5177ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The "Lead Gen - B2B" campaign had the highest spend at $727.78 last week—your top performer! For context, this was right on par with your overall average spend of $56,868.16.'
```

---

## Test 43: wich ads in that campaign performed best?

**Answer**:
> The Image Ad - Morning Audience - Lead Gen - B2B had the highest ROAS at 2.76× last week—your best performer! However, it's worth noting that your overall ROAS was 2.52×, which is below the workspace average of 6.51×.

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
  "group_by": "ad",
  "breakdown": "ad",
  "top_n": 1,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": null,
    "entity_ids": null,
    "status": null,
    "entity_name": "Lead Gen - B2B",
    "metric_filters": null
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "wich ads in that campaign performed best?",
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'wich ads in that campaign performed best?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Lead Gen - B2B', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'wich ads in that campaign performed best?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 2092ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='ad', breakdown='ad', derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Lead Gen - B2B', 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Lead Gen - B2B', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='wich ads in that campaign performed best?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Lead Gen - B2B
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Lead Gen - B2B'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Lead Gen - B2B (ID: 8e751a39-6438-486a-a116-c899baed8949, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Lead Gen - B2B
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 8e751a39-6438-486a-a116-c899baed8949 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Lead Gen - B2B': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('5522.4600'), 'revenue': Decimal('13899.1200'), 'clicks': 13655, 'impressions': 378343, 'conversions': Decimal('2539.1800'), 'leads': Decimal('2539.1800'), 'installs': 0, 'purchases': 0, 'visitors': 12256, 'profit': Decimal('3966.5900')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('2.516834888799556719288143327'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Lead Gen - B2B'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Lead Gen - B2B (ID: 8e751a39-6438-486a-a116-c899baed8949, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Lead Gen - B2B
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 8e751a39-6438-486a-a116-c899baed8949 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Lead Gen - B2B': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for roas by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Lead Gen - B2B
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity by name (exact first): 'Lead Gen - B2B'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Lead Gen - B2B'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Lead Gen - B2B (ID: 8e751a39-6438-486a-a116-c899baed8949, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Lead Gen - B2B
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 8e751a39-6438-486a-a116-c899baed8949 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Lead Gen - B2B': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=2.516834888799557 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 1.337330356470913}, {'date': '2025-10-24', 'value': 2.300625757943245}, {'date': '2025-10-25', 'value': 3.6258245317188593}, {'date': '2025-10-26', 'value': 3.712920536404477}, {'date': '2025-10-27', 'value': 2.395116089202007}, {'date': '2025-10-28', 'value': 1.8775595661823208}] breakdown=[{'label': 'Image Ad - Morning Audience - Lead Gen - B2B', 'value': 2.7627486804709704, 'spend': 492.6, 'clicks': 1250, 'conversions': 203.54, 'revenue': 1360.93, 'impressions': 35883}] workspace_avg=6.50707865350312
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Image Ad - Morning Audience - Lead Gen - B2B had the highest ROAS at 2.76× last week—your best performer! However, it's worth noting that your overall ROAS was 2.52×, which is below the workspace average of 6.51×.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1522ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 4050ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Image Ad - Morning Audience - Lead Gen - B2B had the highest ROAS at 2.76× last week—your best performer! However, it's worth noting that your overall ROAS was 2.52×, which is below the workspace average of 6.51×.'
```

---

## Test 44: how many conversions did that campaign deliver?

**Answer**:
> The campaign delivered 2,539 conversions last week.

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
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "sort_order": "desc",
  "filters": {
    "provider": null,
    "level": "campaign",
    "entity_ids": null,
    "status": null,
    "entity_name": "Lead Gen - B2B",
    "metric_filters": null
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "how many conversions did that campaign deliver?",
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'how many conversions did that campaign deliver?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'conversions', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': 'campaign', 'entity_ids': None, 'status': None, 'entity_name': 'Lead Gen - B2B', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'how many conversions did that campaign deliver?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1508ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['conversions'], filters={'provider': None, 'level': 'campaign', 'entity_ids': None, 'status': None, 'entity_name': 'Lead Gen - B2B', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='conversions', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level='campaign', entity_ids=None, status=None, entity_name='Lead Gen - B2B', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='how many conversions did that campaign deliver?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['conversions']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=campaign, status=None, entity_name=Lead Gen - B2B
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Lead Gen - B2B'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Lead Gen - B2B (ID: 8e751a39-6438-486a-a116-c899baed8949, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Lead Gen - B2B
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 8e751a39-6438-486a-a116-c899baed8949 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Lead Gen - B2B': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('5522.4600'), 'revenue': Decimal('13899.1200'), 'clicks': 13655, 'impressions': 378343, 'conversions': Decimal('2539.1800'), 'leads': Decimal('2539.1800'), 'installs': 0, 'purchases': 0, 'visitors': 12256, 'profit': Decimal('3966.5900')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for conversions
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for conversions: 10701.15
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'conversions': MetricValue(value=2539.18, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 10701.15
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=2539.18 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=10701.15
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The campaign delivered 2,539 conversions last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 769ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2523ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The campaign delivered 2,539 conversions last week.'
```

---

## Test 45: how much revenue in the last week?

**Answer**:
> Your revenue was $370,045.59 last week.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "how much revenue in the last week?",
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'how much revenue in the last week?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'how much revenue in the last week?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 916ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='how much revenue in the last week?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 370045.59
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=370045.59, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 370045.59
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=370045.59 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=370045.59
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your revenue was $370,045.59 last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 797ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1857ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your revenue was $370,045.59 last week.'
```

---

## Test 46: wich campaign brought in the most?

**Answer**:
> The Summer Sale Campaign brought in the most revenue at $7,730.26 last week—your top performer! Overall, your total revenue was $370,045.59, which is right on par with your average.

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
  "question": "wich campaign brought in the most?",
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'wich campaign brought in the most?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'wich campaign brought in the most?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1354ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='wich campaign brought in the most?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 370045.59
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=370045.59, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 370045.59
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for revenue by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=370045.59 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 55066.55}, {'date': '2025-10-24', 'value': 58272.68}, {'date': '2025-10-25', 'value': 69017.48}, {'date': '2025-10-26', 'value': 64361.53}, {'date': '2025-10-27', 'value': 62243.58}, {'date': '2025-10-28', 'value': 61083.77}] breakdown=[{'label': 'Summer Sale Campaign', 'value': 7730.26, 'spend': 441.49, 'clicks': 1053, 'conversions': 57.0, 'revenue': 7730.26, 'impressions': 31363}] workspace_avg=370045.59
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Summer Sale Campaign brought in the most revenue at $7,730.26 last week—your top performer! Overall, your total revenue was $370,045.59, which is right on par with your average.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 2144ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3701ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Summer Sale Campaign brought in the most revenue at $7,730.26 last week—your top performer! Overall, your total revenue was $370,045.59, which is right on par with your average.'
```

---

## Test 47: how many conversions did that campaign deliver?

**Answer**:
> The campaign delivered 689 conversions last week.

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
  "question": "how many conversions did that campaign deliver?",
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'how many conversions did that campaign deliver?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'conversions', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': 'campaign', 'entity_ids': None, 'status': None, 'entity_name': 'Summer Sale', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'how many conversions did that campaign deliver?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 2084ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['conversions'], filters={'provider': None, 'level': 'campaign', 'entity_ids': None, 'status': None, 'entity_name': 'Summer Sale', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='conversions', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level='campaign', entity_ids=None, status=None, entity_name='Summer Sale', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='how many conversions did that campaign deliver?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['conversions']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=campaign, status=None, entity_name=Summer Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Summer Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Summer Sale Campaign (ID: d02a69cb-5368-488f-93ec-993c747a2299, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Summer Sale Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity d02a69cb-5368-488f-93ec-993c747a2299 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Summer Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('5066.1600'), 'revenue': Decimal('86933.5500'), 'clicks': 13501, 'impressions': 384040, 'conversions': Decimal('689.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 689, 'visitors': 12385, 'profit': Decimal('26986.1500')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for conversions
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for conversions: 10701.15
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'conversions': MetricValue(value=689.0, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 10701.15
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=689.0 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=10701.15
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The campaign delivered 689 conversions last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 927ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3324ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The campaign delivered 689 conversions last week.'
```

---

## Test 48: What's my ROAS for active campaigns?

**Answer**:
> Your ROAS for active campaigns was 6.15× last week, which is pretty solid but slightly below the workspace average of 6.51×. The Summer Sale Campaign was the top performer, crushing it with a ROAS of 17.51×.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'What's my ROAS for active campaigns?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': 'active', 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's my ROAS for active campaigns?", 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1122ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': 'active', 'entity_name': None, 'metric_filters': None}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status='active', entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's my ROAS for active campaigns?", timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=active, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('54027.8300'), 'revenue': Decimal('332458.1100'), 'clicks': 119821, 'impressions': 4661516, 'conversions': Decimal('10010.3300'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 85581, 'profit': Decimal('100899.9700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.153460355524180778683874588'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for roas by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=active, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=6.153460355524181 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 5.521933584995087}, {'date': '2025-10-24', 'value': 5.698221775874147}, {'date': '2025-10-25', 'value': 7.3697316693553345}, {'date': '2025-10-26', 'value': 6.302231907098084}, {'date': '2025-10-27', 'value': 5.995647458989944}, {'date': '2025-10-28', 'value': 6.109445323966241}] breakdown=[{'label': 'Summer Sale Campaign', 'value': 17.509479263403474, 'spend': 441.49, 'clicks': 1053, 'conversions': 57.0, 'revenue': 7730.26, 'impressions': 31363}, {'label': 'Black Friday Deals', 'value': 14.94095701540957, 'spend': 308.25, 'clicks': 579, 'conversions': 30.0, 'revenue': 4605.55, 'impressions': 28010}, {'label': 'General Conversions', 'value': 14.746390330953925, 'spend': 246.56, 'clicks': 497, 'conversions': 46.22, 'revenue': 3635.87, 'impressions': 22583}, {'label': 'Holiday Sale - Purchases', 'value': 7.971142074272722, 'spend': 343.06, 'clicks': 593, 'conversions': 28.0, 'revenue': 2734.58, 'impressions': 30349}, {'label': 'Website Traffic Push', 'value': 7.964628085424941, 'spend': 480.89, 'clicks': 1254, 'conversions': 76.67, 'revenue': 3830.11, 'impressions': 35596}, {'label': 'Newsletter Signup Campaign', 'value': 1.9973815283904939, 'spend': 351.35, 'clicks': 775, 'conversions': 145.67, 'revenue': 701.78, 'impressions': 35596}, {'label': 'Lead Gen - B2B', 'value': 1.7489213773393057, 'spend': 727.78, 'clicks': 1331, 'conversions': 234.25, 'revenue': 1272.83, 'impressions': 42491}, {'label': 'Brand Awareness', 'value': 1.617739189649302, 'spend': 293.7, 'clicks': 661, 'conversions': 11.92, 'revenue': 475.13, 'impressions': 27467}, {'label': 'Product Launch Teaser', 'value': 1.2602953842227822, 'spend': 313.49, 'clicks': 491, 'conversions': 12.2, 'revenue': 395.09, 'impressions': 37040}, {'label': 'App Install Campaign', 'value': 0.6241234715810987, 'spend': 283.79, 'clicks': 738, 'conversions': 73.0, 'revenue': 177.12, 'impressions': 26108}] workspace_avg=6.50707865350312
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your ROAS for active campaigns was 6.15× last week, which is pretty solid but slightly below the workspace average of 6.51×. The Summer Sale Campaign was the top performer, crushing it with a ROAS of 17.51×.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1811ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3159ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your ROAS for active campaigns was 6.15× last week, which is pretty solid but slightly below the workspace average of 6.51×. The Summer Sale Campaign was the top performer, crushing it with a ROAS of 17.51×.'
```

---

## Test 49: How much did I spend on Meta ads?

**Answer**:
> You spent $15,227.19 on Meta ads last week.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'How much did I spend on Meta ads?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'spend', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': 'meta', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How much did I spend on Meta ads?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 8290ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['spend'], filters={'provider': 'meta', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='spend', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider='meta', level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How much did I spend on Meta ads?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=meta, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('15227.1900'), 'revenue': Decimal('148567.7200'), 'clicks': 29699, 'impressions': 1512185, 'conversions': Decimal('2864.0800'), 'leads': Decimal('1391.2600'), 'installs': 0, 'purchases': 782, 'visitors': 26991, 'profit': Decimal('44590.8000')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 56868.16
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=15227.19, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 56868.16
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=15227.19 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=56868.16
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'You spent $15,227.19 on Meta ads last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 998ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 9495ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'You spent $15,227.19 on Meta ads last week.'
```

---

## Test 50: How much revenue on Google last week?

**Answer**:
> Your revenue on Google was $166,884.11 last week.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'How much revenue on Google last week?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': 'google', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How much revenue on Google last week?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 896ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['revenue'], filters={'provider': 'google', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider='google', level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How much revenue on Google last week?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=google, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('23974.8800'), 'revenue': Decimal('166884.1100'), 'clicks': 60326, 'impressions': 1739675, 'conversions': Decimal('5989.3100'), 'leads': Decimal('2773.4300'), 'installs': 1489, 'purchases': 746, 'visitors': 41425, 'profit': Decimal('50931.6600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 370045.59
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=166884.11, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 370045.59
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=166884.11 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=370045.59
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your revenue on Google was $166,884.11 last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 769ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1836ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your revenue on Google was $166,884.11 last week.'
```

---

## Test 51: What's my cost per install?

**Answer**:
> Your cost per install was $23.23 last week.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'What's my cost per install?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpi', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's my cost per install?", 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1057ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived='cpi', need_timeseries=False, need_previous=False, base_measures=['installs', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpi', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's my cost per install?", timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpi']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpi
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpi: 23.23045751633986928104575163
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpi': MetricValue(value=Decimal('23.23045751633986928104575163'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 23.23045751633986928104575163
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=23.230457516339868 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=23.230457516339868
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your cost per install was $23.23 last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 994ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2196ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your cost per install was $23.23 last week.'
```

---

## Test 52: How many leads did I generate today?

**Answer**:
> I couldn't find any data for leads today. You may want to try a different time period.

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
  "timeframe_description": "today",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'How many leads did I generate today?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'leads', 'time_range': {'last_n_days': 1, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How many leads did I generate today?', 'timeframe_description': 'today', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1272ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 29), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['leads'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='leads', time_range=TimeRange(last_n_days=1, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How many leads did I generate today?', timeframe_description='today', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['leads']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 29) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-29 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('0'), 'revenue': Decimal('0'), 'clicks': 0, 'impressions': 0, 'conversions': Decimal('0'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 0, 'visitors': 0, 'profit': Decimal('0')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for leads
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for leads: 0.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'leads': MetricValue(value=0.0, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.0
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.0 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=0.0
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'I couldn't find any data for leads today. You may want to try a different time period.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1433ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'I couldn't find any data for leads today. You may want to try a different time period.'
```

---

## Test 53: wich ad had the lowest cpc last week?

**Answer**:
> The Carousel Ad - Evening Audience - Summer Sale Campaign had the lowest CPC at $0.30 last week—your best performer! For context, your overall CPC was $0.45, so this ad was really leading the pack.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'wich ad had the lowest cpc last week?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpc', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 1, 'sort_order': 'asc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'wich ad had the lowest cpc last week?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 3181ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='ad', breakdown='ad', derived='cpc', need_timeseries=True, need_previous=False, base_measures=['clicks', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='asc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpc', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=1, sort_order='asc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='wich ad had the lowest cpc last week?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4528224483620785756374118134
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.4528224483620785756374118134'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4528224483620785756374118134
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpc by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: asc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.4528224483620786 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 0.46385995255979445}, {'date': '2025-10-24', 'value': 0.44097263020469063}, {'date': '2025-10-25', 'value': 0.4323966137978009}, {'date': '2025-10-26', 'value': 0.4615891065456283}, {'date': '2025-10-27', 'value': 0.45648818753990694}, {'date': '2025-10-28', 'value': 0.4619357829502757}] breakdown=[{'label': 'Carousel Ad - Evening Audience - Summer Sale Campaign', 'value': 0.2953903990746096, 'spend': 510.73, 'clicks': 1729, 'conversions': 88.0, 'revenue': 12486.06, 'impressions': 37836}] workspace_avg=0.4528224483620786
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Carousel Ad - Evening Audience - Summer Sale Campaign had the lowest CPC at $0.30 last week—your best performer! For context, your overall CPC was $0.45, so this ad was really leading the pack.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1817ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 5242ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Carousel Ad - Evening Audience - Summer Sale Campaign had the lowest CPC at $0.30 last week—your best performer! For context, your overall CPC was $0.45, so this ad was really leading the pack.'
```

---

## Test 54: how much revenue would i have last week if my cpc was 0.20?

**Answer**:
> None of your 50 campaigns had a CPC of exactly $0.20 last week, which is why no results were returned. You might want to check if your campaigns typically have a different CPC or adjust the filter to explore a broader range.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'how much revenue would i have last week if my cpc was 0.20?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'cpc', 'operator': '=', 'value': 0.2}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'how much revenue would i have last week if my cpc was 0.20?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1119ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'cpc', 'operator': '=', 'value': 0.2}]}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'cpc', 'operator': '=', 'value': 0.2}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='how much revenue would i have last week if my cpc was 0.20?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 370045.59
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=370045.59, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 370045.59
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=370045.59 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=370045.59
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'None of your 50 campaigns had a CPC of exactly $0.20 last week, which is why no results were returned. You might want to check if your campaigns typically have a different CPC or adjust the filter to explore a broader range.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 2364ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3630ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'None of your 50 campaigns had a CPC of exactly $0.20 last week, which is why no results were returned. You might want to check if your campaigns typically have a different CPC or adjust the filter to explore a broader range.'
```

---

## Test 55: best performing ad set in Holiday Sale campaign yesterday?

**Answer**:
> The "Morning Audience - Holiday Sale - Purchases" ad set had the lowest ROAS at 11.03× yesterday—your worst performer. For context, your overall ROAS was 15.40×, which is well above the workspace average of 6.45×. So, while the campaign's crushing it overall, this ad set could use some attention.

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
  "timeframe_description": "yesterday",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'best performing ad set in Holiday Sale campaign yesterday?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 1, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'best performing ad set in Holiday Sale campaign yesterday?', 'timeframe_description': 'yesterday', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1938ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 28), end=datetime.date(2025, 10, 28), group_by='adset', breakdown='adset', derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=1, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Holiday Sale', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='best performing ad set in Holiday Sale campaign yesterday?', timeframe_description='yesterday', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 28) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-28 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('514.0800'), 'revenue': Decimal('7918.1700'), 'clicks': 1182, 'impressions': 60498, 'conversions': Decimal('58.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 58, 'visitors': 1082, 'profit': Decimal('2414.8300')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.452658599580624204427214003
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('15.40260270774976657329598506'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.452658599580624204427214003
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for roas by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 28) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-28 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity by name (exact first): 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using partial match for 'Holiday Sale': Holiday Sale - Purchases (f2d2c4ee-b550-43ff-a17b-3b6a559a61b9)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=15.402602707749766 previous=None delta_pct=None timeseries=[{'date': '2025-10-28', 'value': 15.402602707749766}] breakdown=[{'label': 'Morning Audience - Holiday Sale - Purchases', 'value': 11.03332139018273, 'spend': 55.82, 'clicks': 75, 'conversions': 5.0, 'revenue': 615.88, 'impressions': 4133}] workspace_avg=6.452658599580624
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The "Morning Audience - Holiday Sale - Purchases" ad set had the lowest ROAS at 11.03× yesterday—your worst performer. For context, your overall ROAS was 15.40×, which is well above the workspace average of 6.45×. So, while the campaign's crushing it overall, this ad set could use some attention.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 3057ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 5559ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The "Morning Audience - Holiday Sale - Purchases" ad set had the lowest ROAS at 11.03× yesterday—your worst performer. For context, your overall ROAS was 15.40×, which is well above the workspace average of 6.45×. So, while the campaign's crushing it overall, this ad set could use some attention.'
```

---

## Test 56: all ad sets above roas 4 in the last 3 days

**Answer**:
> Here are the adsets in the last 3 days with ROAS above 4×:

1. Morning Audience - Summer Sale Campaign: 40.58×
2. Morning Audience - Black Friday Deals: 15.87×
3. Weekend Audience - General Conversions: 15.80×
4. Evening Audience - Blog Content Promotion: 14.26×
5. Evening Audience - General Conversions: 12.94×
6. Weekend Audience - Holiday Sale - Purchases: 12.12×
7. Morning Audience - Holiday Sale - Purchases: 11.35×
8. Morning Audience - General Conversions: 11.19×
9. Evening Audience - Holiday Sale - Purchases: 9.25×
10. Evening Audience - Website Traffic Push: 9.13×
11. Evening Audience - Summer Sale Campaign: 8.82×
12. Weekend Audience - Summer Sale Campaign: 7.27×
13. Morning Audience - Blog Content Promotion: 6.57×
14. Evening Audience - Black Friday Deals: 6.54×
15. Weekend Audience - Product Launch Teaser: 5.13×
16. Morning Audience - Lead Gen - B2B: 4.69×
17. Morning Audience - Website Traffic Push: 4.46×
18. Weekend Audience - Website Traffic Push: 4.44×

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
  "top_n": 50,
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
  "timeframe_description": "last 3 days",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'all ad sets above roas 4 in the last 3 days'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 3, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'roas', 'operator': '>', 'value': 4}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'all ad sets above roas 4 in the last 3 days', 'timeframe_description': 'last 3 days', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1416ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 27), end=datetime.date(2025, 10, 29), group_by='adset', breakdown='adset', derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'roas', 'operator': '>', 'value': 4}]}, top_n=50, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=3, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=50, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'roas', 'operator': '>', 'value': 4}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='all ad sets above roas 4 in the last 3 days', timeframe_description='last 3 days', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 27) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-27 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('19475.4100'), 'revenue': Decimal('123327.3500'), 'clicks': 42419, 'impressions': 1645128, 'conversions': Decimal('3586.7400'), 'leads': Decimal('1423.5300'), 'installs': 825, 'purchases': 499, 'visitors': 30340, 'profit': Decimal('36042.6200')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.332464887773864581028075917
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.332464887773864581028075917'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.332464887773864581028075917
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for roas by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 27) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 50, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-27 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=6.332464887773865 previous=None delta_pct=None timeseries=[{'date': '2025-10-27', 'value': 6.218785967772876}, {'date': '2025-10-28', 'value': 6.452658599580624}] breakdown=[{'label': 'Morning Audience - Summer Sale Campaign', 'value': 40.576608784473954, 'spend': 137.06, 'clicks': 559, 'conversions': 34.0, 'revenue': 5561.43, 'impressions': 13014}, {'label': 'Morning Audience - Black Friday Deals', 'value': 15.869470234844348, 'spend': 91.55, 'clicks': 163, 'conversions': 10.0, 'revenue': 1452.85, 'impressions': 10355}, {'label': 'Weekend Audience - General Conversions', 'value': 15.802504696305572, 'spend': 79.85, 'clicks': 250, 'conversions': 21.15, 'revenue': 1261.83, 'impressions': 13237}, {'label': 'Evening Audience - Blog Content Promotion', 'value': 14.261404697380307, 'spend': 88.56, 'clicks': 249, 'conversions': 19.9, 'revenue': 1262.99, 'impressions': 9141}, {'label': 'Evening Audience - General Conversions', 'value': 12.939257737254398, 'spend': 77.87, 'clicks': 112, 'conversions': 12.18, 'revenue': 1007.58, 'impressions': 8246}, {'label': 'Weekend Audience - Holiday Sale - Purchases', 'value': 12.118405488526141, 'spend': 84.54, 'clicks': 169, 'conversions': 10.0, 'revenue': 1024.49, 'impressions': 9952}, {'label': 'Morning Audience - Holiday Sale - Purchases', 'value': 11.347306071306527, 'spend': 87.79, 'clicks': 144, 'conversions': 7.0, 'revenue': 996.18, 'impressions': 6697}, {'label': 'Morning Audience - General Conversions', 'value': 11.19115717659407, 'spend': 152.44, 'clicks': 202, 'conversions': 22.9, 'revenue': 1705.98, 'impressions': 13516}, {'label': 'Evening Audience - Holiday Sale - Purchases', 'value': 9.25101988781234, 'spend': 78.44, 'clicks': 261, 'conversions': 9.0, 'revenue': 725.65, 'impressions': 10946}, {'label': 'Evening Audience - Website Traffic Push', 'value': 9.13206491326245, 'spend': 71.48, 'clicks': 306, 'conversions': 20.79, 'revenue': 652.76, 'impressions': 8189}, {'label': 'Evening Audience - Summer Sale Campaign', 'value': 8.824003362993064, 'spend': 142.73, 'clicks': 263, 'conversions': 17.0, 'revenue': 1259.45, 'impressions': 10180}, {'label': 'Weekend Audience - Summer Sale Campaign', 'value': 7.265659129818761, 'spend': 169.39, 'clicks': 310, 'conversions': 10.0, 'revenue': 1230.73, 'impressions': 10185}, {'label': 'Morning Audience - Blog Content Promotion', 'value': 6.570693906305037, 'spend': 141.95, 'clicks': 314, 'conversions': 18.08, 'revenue': 932.71, 'impressions': 15557}, {'label': 'Evening Audience - Black Friday Deals', 'value': 6.538584222794749, 'spend': 163.02, 'clicks': 286, 'conversions': 15.0, 'revenue': 1065.92, 'impressions': 12119}, {'label': 'Weekend Audience - Product Launch Teaser', 'value': 5.12718055762636, 'spend': 67.07, 'clicks': 140, 'conversions': 7.35, 'revenue': 343.88, 'impressions': 7713}, {'label': 'Morning Audience - Lead Gen - B2B', 'value': 4.694656488549619, 'spend': 250.21, 'clicks': 728, 'conversions': 169.38, 'revenue': 1174.65, 'impressions': 15505}, {'label': 'Morning Audience - Website Traffic Push', 'value': 4.463408614093545, 'spend': 243.09, 'clicks': 532, 'conversions': 29.37, 'revenue': 1085.01, 'impressions': 15885}, {'label': 'Weekend Audience - Website Traffic Push', 'value': 4.442080817464004, 'spend': 215.3, 'clicks': 559, 'conversions': 15.37, 'revenue': 956.38, 'impressions': 15677}] workspace_avg=6.332464887773865
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are the adsets in the last 3 days with ROAS above 4×:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1635ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are the adsets in the last 3 days with ROAS above 4×:
```

---

## Test 57: which campaign has the highest ctr?

**Answer**:
> The Website Traffic Push campaign had the highest CTR at 3.5% last week—your top performer! For context, your overall CTR across campaigns was 2.5%, so this one really stood out.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'which campaign has the highest ctr?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'ctr', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'which campaign has the highest ctr?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1587ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived='ctr', need_timeseries=True, need_previous=False, base_measures=['clicks', 'impressions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='ctr', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='which campaign has the highest ctr?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['ctr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for ctr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for ctr: 0.02535125290734174
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'ctr': MetricValue(value=0.02535125290734174, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.02535125290734174
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for ctr by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.02535125290734174 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 0.024331210344251276}, {'date': '2025-10-24', 'value': 0.025365635577885168}, {'date': '2025-10-25', 'value': 0.02567302059562307}, {'date': '2025-10-26', 'value': 0.02518955349620893}, {'date': '2025-10-27', 'value': 0.025784767865353792}, {'date': '2025-10-28', 'value': 0.0257844613799273}] breakdown=[{'label': 'Website Traffic Push', 'value': 0.03522867737948084, 'spend': 480.89, 'clicks': 1254, 'conversions': 76.67, 'revenue': 3830.11, 'impressions': 35596}] workspace_avg=0.02535125290734174
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Website Traffic Push campaign had the highest CTR at 3.5% last week—your top performer! For context, your overall CTR across campaigns was 2.5%, so this one really stood out.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1563ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3642ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Website Traffic Push campaign had the highest CTR at 3.5% last week—your top performer! For context, your overall CTR across campaigns was 2.5%, so this one really stood out.'
```

---

## Test 58: show me adsets with cpc below 1 dollar

**Answer**:
> Here are the adsets last week with CPC below $1.00:

1. Weekend Audience - Black Friday Deals: $0.71
2. Morning Audience - General Conversions: $0.70
3. Evening Audience - General Conversions: $0.69
4. Evening Audience - Newsletter Signup Campaign: $0.62
5. Morning Audience - Holiday Sale - Purchases: $0.61
6. Evening Audience - Black Friday Deals: $0.58
7. Evening Audience - Product Launch Teaser: $0.56
8. Morning Audience - Black Friday Deals: $0.55
9. Weekend Audience - Brand Awareness: $0.54
10. Morning Audience - Brand Awareness: $0.54
11. Weekend Audience - Product Launch Teaser: $0.51
12. Morning Audience - App Install Campaign: $0.51
13. Morning Audience - Product Launch Teaser: $0.50
14. Weekend Audience - Newsletter Signup Campaign: $0.50
15. Weekend Audience - App Install Campaign: $0.49
16. Morning Audience - Newsletter Signup Campaign: $0.49
17. Evening Audience - Holiday Sale - Purchases: $0.47
18. Weekend Audience - Summer Sale Campaign: $0.47
19. Morning Audience - Blog Content Promotion: $0.45
20. Evening Audience - App Install Campaign: $0.44
21. Weekend Audience - Website Traffic Push: $0.43
22. Weekend Audience - Holiday Sale - Purchases: $0.43
23. Morning Audience - Mobile Game Installs: $0.42
24. Evening Audience - Website Traffic Push: $0.42
25. Evening Audience - Lead Gen - B2B: $0.41
26. Weekend Audience - Mobile Game Installs: $0.41
27. Evening Audience - Brand Awareness: $0.40
28. Morning Audience - Website Traffic Push: $0.40
29. Evening Audience - Blog Content Promotion: $0.39
30. Evening Audience - Summer Sale Campaign: $0.38
31. Weekend Audience - Lead Gen - B2B: $0.36
32. Morning Audience - Lead Gen - B2B: $0.36
33. Weekend Audience - General Conversions: $0.36
34. Morning Audience - Summer Sale Campaign: $0.34
35. Evening Audience - Mobile Game Installs: $0.33

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
  "top_n": 50,
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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'show me adsets with cpc below 1 dollar'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpc', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'cpc', 'operator': '<', 'value': 1}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'show me adsets with cpc below 1 dollar', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1241ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='adset', breakdown='adset', derived='cpc', need_timeseries=True, need_previous=False, base_measures=['clicks', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'cpc', 'operator': '<', 'value': 1}]}, top_n=50, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpc', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=50, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'cpc', 'operator': '<', 'value': 1}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='show me adsets with cpc below 1 dollar', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4528224483620785756374118134
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.4528224483620785756374118134'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4528224483620785756374118134
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpc by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 50, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.4528224483620786 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 0.46385995255979445}, {'date': '2025-10-24', 'value': 0.44097263020469063}, {'date': '2025-10-25', 'value': 0.4323966137978009}, {'date': '2025-10-26', 'value': 0.4615891065456283}, {'date': '2025-10-27', 'value': 0.45648818753990694}, {'date': '2025-10-28', 'value': 0.4619357829502757}] breakdown=[{'label': 'Weekend Audience - Black Friday Deals', 'value': 0.7116336633663366, 'spend': 431.25, 'clicks': 606, 'conversions': 24.0, 'revenue': 3317.55, 'impressions': 40871}, {'label': 'Morning Audience - General Conversions', 'value': 0.7016548463356974, 'spend': 296.8, 'clicks': 423, 'conversions': 42.2, 'revenue': 3201.24, 'impressions': 28404}, {'label': 'Evening Audience - General Conversions', 'value': 0.6932339449541285, 'spend': 302.25, 'clicks': 436, 'conversions': 39.07, 'revenue': 3053.46, 'impressions': 29880}, {'label': 'Evening Audience - Newsletter Signup Campaign', 'value': 0.6164392678868552, 'spend': 370.48, 'clicks': 601, 'conversions': 104.45, 'revenue': 559.62, 'impressions': 38324}, {'label': 'Morning Audience - Holiday Sale - Purchases', 'value': 0.6120336134453781, 'spend': 364.16, 'clicks': 595, 'conversions': 32.0, 'revenue': 4452.07, 'impressions': 32664}, {'label': 'Evening Audience - Black Friday Deals', 'value': 0.576330014224751, 'spend': 405.16, 'clicks': 703, 'conversions': 39.0, 'revenue': 3281.19, 'impressions': 33922}, {'label': 'Evening Audience - Product Launch Teaser', 'value': 0.5563169164882227, 'spend': 259.8, 'clicks': 467, 'conversions': 16.27, 'revenue': 584.17, 'impressions': 28737}, {'label': 'Morning Audience - Black Friday Deals', 'value': 0.5456899810964083, 'spend': 288.67, 'clicks': 529, 'conversions': 23.0, 'revenue': 3379.71, 'impressions': 29856}, {'label': 'Weekend Audience - Brand Awareness', 'value': 0.5430569430569431, 'spend': 543.6, 'clicks': 1001, 'conversions': 11.54, 'revenue': 382.48, 'impressions': 40474}, {'label': 'Morning Audience - Brand Awareness', 'value': 0.5383152173913044, 'spend': 495.25, 'clicks': 920, 'conversions': 14.99, 'revenue': 591.74, 'impressions': 38937}, {'label': 'Weekend Audience - Product Launch Teaser', 'value': 0.5122390572390573, 'spend': 304.27, 'clicks': 594, 'conversions': 19.06, 'revenue': 693.97, 'impressions': 34288}, {'label': 'Morning Audience - App Install Campaign', 'value': 0.509908350305499, 'spend': 500.73, 'clicks': 982, 'conversions': 101.0, 'revenue': 276.83, 'impressions': 31968}, {'label': 'Morning Audience - Product Launch Teaser', 'value': 0.4975, 'spend': 334.32, 'clicks': 672, 'conversions': 16.54, 'revenue': 539.54, 'impressions': 39196}, {'label': 'Weekend Audience - Newsletter Signup Campaign', 'value': 0.49575712143928036, 'spend': 330.67, 'clicks': 667, 'conversions': 118.89, 'revenue': 629.32, 'impressions': 29368}, {'label': 'Weekend Audience - App Install Campaign', 'value': 0.48897903372835005, 'spend': 536.41, 'clicks': 1097, 'conversions': 93.0, 'revenue': 195.43, 'impressions': 34584}, {'label': 'Morning Audience - Newsletter Signup Campaign', 'value': 0.48716521739130436, 'spend': 280.12, 'clicks': 575, 'conversions': 96.57, 'revenue': 486.33, 'impressions': 30508}, {'label': 'Evening Audience - Holiday Sale - Purchases', 'value': 0.4741682242990654, 'spend': 253.68, 'clicks': 535, 'conversions': 25.0, 'revenue': 3022.92, 'impressions': 29313}, {'label': 'Weekend Audience - Summer Sale Campaign', 'value': 0.4706003159557662, 'spend': 297.89, 'clicks': 633, 'conversions': 25.0, 'revenue': 3863.23, 'impressions': 19665}, {'label': 'Morning Audience - Blog Content Promotion', 'value': 0.4506241134751773, 'spend': 317.69, 'clicks': 705, 'conversions': 71.31, 'revenue': 4015.31, 'impressions': 37208}, {'label': 'Evening Audience - App Install Campaign', 'value': 0.44413019079685745, 'spend': 395.72, 'clicks': 891, 'conversions': 91.0, 'revenue': 318.76, 'impressions': 26529}, {'label': 'Weekend Audience - Website Traffic Push', 'value': 0.4339921875, 'spend': 555.51, 'clicks': 1280, 'conversions': 62.88, 'revenue': 3610.43, 'impressions': 38084}, {'label': 'Weekend Audience - Holiday Sale - Purchases', 'value': 0.4263229571984436, 'spend': 219.13, 'clicks': 514, 'conversions': 27.0, 'revenue': 2944.01, 'impressions': 25157}, {'label': 'Morning Audience - Mobile Game Installs', 'value': 0.4234737678855326, 'spend': 532.73, 'clicks': 1258, 'conversions': 116.0, 'revenue': 362.06, 'impressions': 44326}, {'label': 'Evening Audience - Website Traffic Push', 'value': 0.423029702970297, 'spend': 427.26, 'clicks': 1010, 'conversions': 71.46, 'revenue': 4063.25, 'impressions': 34967}, {'label': 'Evening Audience - Lead Gen - B2B', 'value': 0.4095691202872531, 'spend': 456.26, 'clicks': 1114, 'conversions': 228.66, 'revenue': 1404.63, 'impressions': 34235}, {'label': 'Weekend Audience - Mobile Game Installs', 'value': 0.4053125, 'spend': 376.13, 'clicks': 928, 'conversions': 76.0, 'revenue': 137.79, 'impressions': 33277}, {'label': 'Evening Audience - Brand Awareness', 'value': 0.4048391089108911, 'spend': 327.11, 'clicks': 808, 'conversions': 13.28, 'revenue': 424.92, 'impressions': 31668}, {'label': 'Morning Audience - Website Traffic Push', 'value': 0.3957583774250441, 'spend': 448.79, 'clicks': 1134, 'conversions': 90.6, 'revenue': 4077.99, 'impressions': 33941}, {'label': 'Evening Audience - Blog Content Promotion', 'value': 0.3908074534161491, 'spend': 251.68, 'clicks': 644, 'conversions': 67.24, 'revenue': 3643.6, 'impressions': 32480}, {'label': 'Evening Audience - Summer Sale Campaign', 'value': 0.376990459670425, 'spend': 434.67, 'clicks': 1153, 'conversions': 67.0, 'revenue': 6585.33, 'impressions': 37178}, {'label': 'Weekend Audience - Lead Gen - B2B', 'value': 0.36489468405215647, 'spend': 363.8, 'clicks': 997, 'conversions': 195.86, 'revenue': 952.37, 'impressions': 25979}, {'label': 'Morning Audience - Lead Gen - B2B', 'value': 0.36032777115613823, 'spend': 604.63, 'clicks': 1678, 'conversions': 360.73, 'revenue': 2502.48, 'impressions': 38899}, {'label': 'Weekend Audience - General Conversions', 'value': 0.3578321678321678, 'spend': 204.68, 'clicks': 572, 'conversions': 44.74, 'revenue': 3343.95, 'impressions': 32024}, {'label': 'Morning Audience - Summer Sale Campaign', 'value': 0.34150036954915003, 'spend': 462.05, 'clicks': 1353, 'conversions': 67.0, 'revenue': 9777.93, 'impressions': 35487}, {'label': 'Evening Audience - Mobile Game Installs', 'value': 0.3261408450704225, 'spend': 231.56, 'clicks': 710, 'conversions': 67.0, 'revenue': 155.47, 'impressions': 23397}] workspace_avg=0.4528224483620786
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are the adsets last week with CPC below $1.00:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1460ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are the adsets last week with CPC below $1.00:
```

---

## Test 59: worst performing ad in App Install campaign?

**Answer**:
> The Image Ad - Morning Audience in your App Install campaign had the lowest ROAS at 0.39× last week—definitely struggling. For some context, your overall campaign average was 6.51×, so this ad needs some attention.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'worst performing ad in App Install campaign?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 1, 'sort_order': 'asc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'App Install Campaign', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'worst performing ad in App Install campaign?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1164ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='ad', breakdown='ad', derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'App Install Campaign', 'metric_filters': None}, top_n=1, sort_order='asc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=1, sort_order='asc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='App Install Campaign', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='worst performing ad in App Install campaign?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install Campaign'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install Campaign': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('5788.0300'), 'revenue': Decimal('3337.7400'), 'clicks': 13991, 'impressions': 409439, 'conversions': Decimal('1416.0000'), 'leads': Decimal('0'), 'installs': 1416, 'purchases': 0, 'visitors': 0, 'profit': Decimal('953.3000')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('0.5766625259371496001230124930'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install Campaign'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install Campaign': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for roas by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: asc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity by name (exact first): 'App Install Campaign'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install Campaign'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install Campaign': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.5766625259371496 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 0.5285763656392423}, {'date': '2025-10-24', 'value': 0.7004389951459127}, {'date': '2025-10-25', 'value': 0.5166284466584009}, {'date': '2025-10-26', 'value': 0.469401159946894}, {'date': '2025-10-27', 'value': 0.5984178369505745}, {'date': '2025-10-28', 'value': 0.5984936049981491}] breakdown=[{'label': 'Image Ad - Morning Audience - App Install Campaign', 'value': 0.3859938940236711, 'spend': 478.22, 'clicks': 1057, 'conversions': 136.0, 'revenue': 184.59, 'impressions': 34390}] workspace_avg=6.50707865350312
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Image Ad - Morning Audience in your App Install campaign had the lowest ROAS at 0.39× last week—definitely struggling. For some context, your overall campaign average was 6.51×, so this ad needs some attention.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 2618ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 4260ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Image Ad - Morning Audience in your App Install campaign had the lowest ROAS at 0.39× last week—definitely struggling. For some context, your overall campaign average was 6.51×, so this ad needs some attention.'
```

---

## Test 60: all campaigns with conversion rate above 5%

**Answer**:
> None of your 12 campaigns currently have a conversion rate above 5% for the last week. You might want to review your strategies to improve performance.

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
  "top_n": 50,
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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'all campaigns with conversion rate above 5%'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cvr', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'cvr', 'operator': '>', 'value': 5}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'all campaigns with conversion rate above 5%', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1499ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived='cvr', need_timeseries=True, need_previous=False, base_measures=['clicks', 'conversions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'cvr', 'operator': '>', 'value': 5}]}, top_n=50, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cvr', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=50, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'cvr', 'operator': '>', 'value': 5}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='all campaigns with conversion rate above 5%', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cvr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cvr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cvr: 0.08520973675409679422865606039
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cvr': MetricValue(value=Decimal('0.08520973675409679422865606039'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.08520973675409679422865606039
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cvr by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 50, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.0852097367540968 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 0.08583712196086184}, {'date': '2025-10-24', 'value': 0.0875549027836061}, {'date': '2025-10-25', 'value': 0.08713194512017125}, {'date': '2025-10-26', 'value': 0.08163927376970856}, {'date': '2025-10-27', 'value': 0.08539040408647268}, {'date': '2025-10-28', 'value': 0.08366125018298931}] breakdown=[] workspace_avg=0.0852097367540968
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: campaign
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'None of your 12 campaigns currently have a conversion rate above 5% for the last week. You might want to review your strategies to improve performance.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1520ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3248ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'None of your 12 campaigns currently have a conversion rate above 5% for the last week. You might want to review your strategies to improve performance.'
```

---

## Test 61: which adset spent the most money?

**Answer**:
> The Morning Audience - Lead Gen - B2B adset spent the most money at $604.63 last week—your top performer! For context, this was right in line with your overall average spend of $56,868.16.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'which adset spent the most money?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'spend', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'which adset spent the most money?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1083ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='adset', breakdown='adset', derived=None, need_timeseries=True, need_previous=False, base_measures=['spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='spend', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='which adset spent the most money?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 56868.16
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=56868.16, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 56868.16
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for spend by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=56868.16 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 9386.67}, {'date': '2025-10-24', 'value': 9457.54}, {'date': '2025-10-25', 'value': 8887.48}, {'date': '2025-10-26', 'value': 9661.06}, {'date': '2025-10-27', 'value': 10008.96}, {'date': '2025-10-28', 'value': 9466.45}] breakdown=[{'label': 'Morning Audience - Lead Gen - B2B', 'value': 604.63, 'spend': 604.63, 'clicks': 1678, 'conversions': 360.73, 'revenue': 2502.48, 'impressions': 38899}] workspace_avg=56868.16
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Morning Audience - Lead Gen - B2B adset spent the most money at $604.63 last week—your top performer! For context, this was right in line with your overall average spend of $56,868.16.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1928ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3245ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Morning Audience - Lead Gen - B2B adset spent the most money at $604.63 last week—your top performer! For context, this was right in line with your overall average spend of $56,868.16.'
```

---

## Test 62: show me ads with revenue above 1000

**Answer**:
> Here are the ads last week with REVENUE above $1,000.00:

1. Carousel Ad - Evening Audience - Summer Sale Campaign: $12,486.06
2. Image Ad - Morning Audience - Summer Sale Campaign: $10,552.61
3. Video Ad - Weekend Audience - Holiday Sale - Purchases: $9,423.45
4. Video Ad - Weekend Audience - Summer Sale Campaign: $9,024.82
5. Carousel Ad - Weekend Audience - Summer Sale Campaign: $7,405.87
6. Image Ad - Evening Audience - Summer Sale Campaign: $7,299.74
7. Video Ad - Weekend Audience - Black Friday Deals: $6,200.59
8. Image Ad - Morning Audience - Holiday Sale - Purchases: $5,933.74
9. Image Ad - Weekend Audience - Holiday Sale - Purchases: $5,862.58
10. Carousel Ad - Morning Audience - Blog Content Promotion: $5,671.27
11. Image Ad - Weekend Audience - Summer Sale Campaign: $5,503.25
12. Image Ad - Morning Audience - Website Traffic Push: $5,393.26
13. Video Ad - Morning Audience - Summer Sale Campaign: $5,221.93
14. Carousel Ad - Weekend Audience - Website Traffic Push: $4,861.90
15. Carousel Ad - Morning Audience - Website Traffic Push: $4,808.89
16. Video Ad - Evening Audience - Black Friday Deals: $4,796.53
17. Video Ad - Morning Audience - Black Friday Deals: $4,663.94
18. Carousel Ad - Morning Audience - Summer Sale Campaign: $4,663.84
19. Image Ad - Evening Audience - General Conversions: $4,641.11
20. Video Ad - Morning Audience - Website Traffic Push: $4,631.65
21. Video Ad - Evening Audience - Summer Sale Campaign: $4,548.94
22. Carousel Ad - Morning Audience - Black Friday Deals: $4,534.16
23. Video Ad - Evening Audience - Holiday Sale - Purchases: $4,435.34
24. Carousel Ad - Morning Audience - Holiday Sale - Purchases: $4,348.61
25. Image Ad - Morning Audience - Blog Content Promotion: $4,305.65
26. Video Ad - Morning Audience - Blog Content Promotion: $4,296.04
27. Carousel Ad - Evening Audience - Website Traffic Push: $4,215.67
28. Carousel Ad - Evening Audience - General Conversions: $4,062.43
29. Image Ad - Evening Audience - Black Friday Deals: $4,016.65
30. Image Ad - Morning Audience - Black Friday Deals: $4,007.99
31. Video Ad - Weekend Audience - Website Traffic Push: $3,825.60
32. Image Ad - Evening Audience - Blog Content Promotion: $3,807.62
33. Image Ad - Weekend Audience - Website Traffic Push: $3,789.59
34. Video Ad - Evening Audience - Blog Content Promotion: $3,723.74
35. Carousel Ad - Evening Audience - Blog Content Promotion: $3,632.19
36. Video Ad - Evening Audience - Website Traffic Push: $3,563.88
37. Video Ad - Morning Audience - Holiday Sale - Purchases: $3,424.54
38. Video Ad - Weekend Audience - General Conversions: $3,386.31
39. Video Ad - Morning Audience - General Conversions: $2,975.43
40. Carousel Ad - Weekend Audience - Black Friday Deals: $2,921.10
41. Image Ad - Evening Audience - Website Traffic Push: $2,861.27
42. Image Ad - Evening Audience - Holiday Sale - Purchases: $2,822.87
43. Carousel Ad - Weekend Audience - Holiday Sale - Purchases: $2,716.68
44. Carousel Ad - Evening Audience - Holiday Sale - Purchases: $2,606.08
45. Carousel Ad - Weekend Audience - General Conversions: $2,604.97
46. Image Ad - Weekend Audience - General Conversions: $2,490.79
47. Carousel Ad - Morning Audience - General Conversions: $2,385.95
48. Video Ad - Evening Audience - General Conversions: $2,266.06
49. Carousel Ad - Evening Audience - Black Friday Deals: $2,118.24
50. Image Ad - Morning Audience - General Conversions: $1,689.96

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
  "top_n": 50,
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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'show me ads with revenue above 1000'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'revenue', 'operator': '>', 'value': 1000}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'show me ads with revenue above 1000', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1587ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='ad', breakdown='ad', derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'revenue', 'operator': '>', 'value': 1000}]}, top_n=50, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=50, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'revenue', 'operator': '>', 'value': 1000}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='show me ads with revenue above 1000', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 370045.59
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=370045.59, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 370045.59
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for revenue by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 50, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=370045.59 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 55066.55}, {'date': '2025-10-24', 'value': 58272.68}, {'date': '2025-10-25', 'value': 69017.48}, {'date': '2025-10-26', 'value': 64361.53}, {'date': '2025-10-27', 'value': 62243.58}, {'date': '2025-10-28', 'value': 61083.77}] breakdown=[{'label': 'Carousel Ad - Evening Audience - Summer Sale Campaign', 'value': 12486.06, 'spend': 510.73, 'clicks': 1729, 'conversions': 88.0, 'revenue': 12486.06, 'impressions': 37836}, {'label': 'Image Ad - Morning Audience - Summer Sale Campaign', 'value': 10552.61, 'spend': 483.96, 'clicks': 1240, 'conversions': 87.0, 'revenue': 10552.61, 'impressions': 33268}, {'label': 'Video Ad - Weekend Audience - Holiday Sale - Purchases', 'value': 9423.45, 'spend': 483.66, 'clicks': 1043, 'conversions': 59.0, 'revenue': 9423.45, 'impressions': 48408}, {'label': 'Video Ad - Weekend Audience - Summer Sale Campaign', 'value': 9024.82, 'spend': 454.83, 'clicks': 1142, 'conversions': 74.0, 'revenue': 9024.82, 'impressions': 36243}, {'label': 'Carousel Ad - Weekend Audience - Summer Sale Campaign', 'value': 7405.87, 'spend': 544.26, 'clicks': 1131, 'conversions': 52.0, 'revenue': 7405.87, 'impressions': 37339}, {'label': 'Image Ad - Evening Audience - Summer Sale Campaign', 'value': 7299.74, 'spend': 455.14, 'clicks': 1304, 'conversions': 62.0, 'revenue': 7299.74, 'impressions': 36529}, {'label': 'Video Ad - Weekend Audience - Black Friday Deals', 'value': 6200.59, 'spend': 320.04, 'clicks': 789, 'conversions': 48.0, 'revenue': 6200.59, 'impressions': 40002}, {'label': 'Image Ad - Morning Audience - Holiday Sale - Purchases', 'value': 5933.74, 'spend': 314.81, 'clicks': 690, 'conversions': 43.0, 'revenue': 5933.74, 'impressions': 32782}, {'label': 'Image Ad - Weekend Audience - Holiday Sale - Purchases', 'value': 5862.58, 'spend': 415.12, 'clicks': 817, 'conversions': 46.0, 'revenue': 5862.58, 'impressions': 38735}, {'label': 'Carousel Ad - Morning Audience - Blog Content Promotion', 'value': 5671.27, 'spend': 316.99, 'clicks': 527, 'conversions': 96.15, 'revenue': 5671.27, 'impressions': 27086}, {'label': 'Image Ad - Weekend Audience - Summer Sale Campaign', 'value': 5503.25, 'spend': 335.08, 'clicks': 981, 'conversions': 42.0, 'revenue': 5503.25, 'impressions': 24988}, {'label': 'Image Ad - Morning Audience - Website Traffic Push', 'value': 5393.26, 'spend': 468.0, 'clicks': 1468, 'conversions': 83.75, 'revenue': 5393.26, 'impressions': 37803}, {'label': 'Video Ad - Morning Audience - Summer Sale Campaign', 'value': 5221.93, 'spend': 314.5, 'clicks': 941, 'conversions': 57.0, 'revenue': 5221.93, 'impressions': 30622}, {'label': 'Carousel Ad - Weekend Audience - Website Traffic Push', 'value': 4861.9, 'spend': 361.69, 'clicks': 698, 'conversions': 78.22, 'revenue': 4861.9, 'impressions': 27432}, {'label': 'Carousel Ad - Morning Audience - Website Traffic Push', 'value': 4808.89, 'spend': 464.04, 'clicks': 1456, 'conversions': 82.51, 'revenue': 4808.89, 'impressions': 41749}, {'label': 'Video Ad - Evening Audience - Black Friday Deals', 'value': 4796.53, 'spend': 374.58, 'clicks': 829, 'conversions': 41.0, 'revenue': 4796.53, 'impressions': 35706}, {'label': 'Video Ad - Morning Audience - Black Friday Deals', 'value': 4663.94, 'spend': 307.22, 'clicks': 563, 'conversions': 28.0, 'revenue': 4663.94, 'impressions': 30476}, {'label': 'Carousel Ad - Morning Audience - Summer Sale Campaign', 'value': 4663.84, 'spend': 468.25, 'clicks': 1092, 'conversions': 41.0, 'revenue': 4663.84, 'impressions': 32285}, {'label': 'Image Ad - Evening Audience - General Conversions', 'value': 4641.11, 'spend': 243.19, 'clicks': 580, 'conversions': 49.37, 'revenue': 4641.11, 'impressions': 29496}, {'label': 'Video Ad - Morning Audience - Website Traffic Push', 'value': 4631.65, 'spend': 689.61, 'clicks': 1782, 'conversions': 84.83, 'revenue': 4631.65, 'impressions': 46764}, {'label': 'Video Ad - Evening Audience - Summer Sale Campaign', 'value': 4548.94, 'spend': 304.8, 'clicks': 802, 'conversions': 27.0, 'revenue': 4548.94, 'impressions': 22600}, {'label': 'Carousel Ad - Morning Audience - Black Friday Deals', 'value': 4534.16, 'spend': 303.33, 'clicks': 625, 'conversions': 32.0, 'revenue': 4534.16, 'impressions': 31721}, {'label': 'Video Ad - Evening Audience - Holiday Sale - Purchases', 'value': 4435.34, 'spend': 277.79, 'clicks': 614, 'conversions': 28.0, 'revenue': 4435.34, 'impressions': 30378}, {'label': 'Carousel Ad - Morning Audience - Holiday Sale - Purchases', 'value': 4348.61, 'spend': 361.75, 'clicks': 610, 'conversions': 29.0, 'revenue': 4348.61, 'impressions': 30337}, {'label': 'Image Ad - Morning Audience - Blog Content Promotion', 'value': 4305.65, 'spend': 374.44, 'clicks': 735, 'conversions': 79.79, 'revenue': 4305.65, 'impressions': 37195}, {'label': 'Video Ad - Morning Audience - Blog Content Promotion', 'value': 4296.04, 'spend': 356.31, 'clicks': 748, 'conversions': 68.34, 'revenue': 4296.04, 'impressions': 34754}, {'label': 'Carousel Ad - Evening Audience - Website Traffic Push', 'value': 4215.67, 'spend': 458.87, 'clicks': 1329, 'conversions': 69.91, 'revenue': 4215.67, 'impressions': 34908}, {'label': 'Carousel Ad - Evening Audience - General Conversions', 'value': 4062.43, 'spend': 324.35, 'clicks': 579, 'conversions': 51.27, 'revenue': 4062.43, 'impressions': 37074}, {'label': 'Image Ad - Evening Audience - Black Friday Deals', 'value': 4016.65, 'spend': 246.98, 'clicks': 610, 'conversions': 24.0, 'revenue': 4016.65, 'impressions': 24670}, {'label': 'Image Ad - Morning Audience - Black Friday Deals', 'value': 4007.99, 'spend': 365.19, 'clicks': 779, 'conversions': 44.0, 'revenue': 4007.99, 'impressions': 34694}, {'label': 'Video Ad - Weekend Audience - Website Traffic Push', 'value': 3825.6, 'spend': 459.64, 'clicks': 1331, 'conversions': 63.91, 'revenue': 3825.6, 'impressions': 36452}, {'label': 'Image Ad - Evening Audience - Blog Content Promotion', 'value': 3807.62, 'spend': 206.57, 'clicks': 456, 'conversions': 76.84, 'revenue': 3807.62, 'impressions': 30357}, {'label': 'Image Ad - Weekend Audience - Website Traffic Push', 'value': 3789.59, 'spend': 573.18, 'clicks': 1451, 'conversions': 81.4, 'revenue': 3789.59, 'impressions': 42313}, {'label': 'Video Ad - Evening Audience - Blog Content Promotion', 'value': 3723.74, 'spend': 319.69, 'clicks': 669, 'conversions': 68.18, 'revenue': 3723.74, 'impressions': 31487}, {'label': 'Carousel Ad - Evening Audience - Blog Content Promotion', 'value': 3632.19, 'spend': 271.6, 'clicks': 623, 'conversions': 80.57, 'revenue': 3632.19, 'impressions': 26874}, {'label': 'Video Ad - Evening Audience - Website Traffic Push', 'value': 3563.88, 'spend': 317.11, 'clicks': 994, 'conversions': 70.46, 'revenue': 3563.88, 'impressions': 28097}, {'label': 'Video Ad - Morning Audience - Holiday Sale - Purchases', 'value': 3424.54, 'spend': 405.75, 'clicks': 579, 'conversions': 24.0, 'revenue': 3424.54, 'impressions': 34408}, {'label': 'Video Ad - Weekend Audience - General Conversions', 'value': 3386.31, 'spend': 244.56, 'clicks': 626, 'conversions': 42.55, 'revenue': 3386.31, 'impressions': 32747}, {'label': 'Video Ad - Morning Audience - General Conversions', 'value': 2975.43, 'spend': 343.05, 'clicks': 646, 'conversions': 50.9, 'revenue': 2975.43, 'impressions': 34501}, {'label': 'Carousel Ad - Weekend Audience - Black Friday Deals', 'value': 2921.1, 'spend': 251.66, 'clicks': 479, 'conversions': 23.0, 'revenue': 2921.1, 'impressions': 26785}, {'label': 'Image Ad - Evening Audience - Website Traffic Push', 'value': 2861.27, 'spend': 440.58, 'clicks': 870, 'conversions': 64.28, 'revenue': 2861.27, 'impressions': 29785}, {'label': 'Image Ad - Evening Audience - Holiday Sale - Purchases', 'value': 2822.87, 'spend': 195.71, 'clicks': 454, 'conversions': 21.0, 'revenue': 2822.87, 'impressions': 23617}, {'label': 'Carousel Ad - Weekend Audience - Holiday Sale - Purchases', 'value': 2716.68, 'spend': 311.11, 'clicks': 661, 'conversions': 20.0, 'revenue': 2716.68, 'impressions': 28410}, {'label': 'Carousel Ad - Evening Audience - Holiday Sale - Purchases', 'value': 2606.08, 'spend': 151.89, 'clicks': 465, 'conversions': 17.0, 'revenue': 2606.08, 'impressions': 17835}, {'label': 'Carousel Ad - Weekend Audience - General Conversions', 'value': 2604.97, 'spend': 293.99, 'clicks': 671, 'conversions': 45.82, 'revenue': 2604.97, 'impressions': 33643}, {'label': 'Image Ad - Weekend Audience - General Conversions', 'value': 2490.79, 'spend': 239.91, 'clicks': 422, 'conversions': 27.76, 'revenue': 2490.79, 'impressions': 27457}, {'label': 'Carousel Ad - Morning Audience - General Conversions', 'value': 2385.95, 'spend': 258.35, 'clicks': 549, 'conversions': 30.29, 'revenue': 2385.95, 'impressions': 31175}, {'label': 'Video Ad - Evening Audience - General Conversions', 'value': 2266.06, 'spend': 217.72, 'clicks': 356, 'conversions': 31.05, 'revenue': 2266.06, 'impressions': 25671}, {'label': 'Carousel Ad - Evening Audience - Black Friday Deals', 'value': 2118.24, 'spend': 332.7, 'clicks': 519, 'conversions': 15.0, 'revenue': 2118.24, 'impressions': 27266}, {'label': 'Image Ad - Morning Audience - General Conversions', 'value': 1689.96, 'spend': 211.92, 'clicks': 475, 'conversions': 26.45, 'revenue': 1689.96, 'impressions': 25893}] workspace_avg=370045.59
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are the ads last week with REVENUE above $1,000.00:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1836ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are the ads last week with REVENUE above $1,000.00:
```

---

## Test 63: best performing campaign by profit margin

**Answer**:
> The Lead Gen - B2B campaign had the lowest profit margin at $400.21 last week—your worst performer. For context, your overall profit was $111,922.76, which was right on average. It looks like this campaign needs a bit of attention.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'best performing campaign by profit margin'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'profit', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'best performing campaign by profit margin', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1220ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['profit'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='profit', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='best performing campaign by profit margin', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['profit']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for profit
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for profit: 111922.76
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'profit': MetricValue(value=111922.76, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 111922.76
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for profit by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=111922.76 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 17432.2}, {'date': '2025-10-24', 'value': 17975.92}, {'date': '2025-10-25', 'value': 21491.89}, {'date': '2025-10-26', 'value': 18980.13}, {'date': '2025-10-27', 'value': 17862.54}, {'date': '2025-10-28', 'value': 18180.08}] breakdown=[{'label': 'Lead Gen - B2B', 'value': 400.21, 'spend': 727.78, 'clicks': 1331, 'conversions': 234.25, 'revenue': 1272.83, 'impressions': 42491}] workspace_avg=111922.76
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Lead Gen - B2B campaign had the lowest profit margin at $400.21 last week—your worst performer. For context, your overall profit was $111,922.76, which was right on average. It looks like this campaign needs a bit of attention.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 3863ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 5328ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Lead Gen - B2B campaign had the lowest profit margin at $400.21 last week—your worst performer. For context, your overall profit was $111,922.76, which was right on average. It looks like this campaign needs a bit of attention.'
```

---

## Test 64: all adsets with clicks above 500

**Answer**:
> Here are the adsets last week with CLICKS above 500:

1. Morning Audience - Lead Gen - B2B: 1,678
2. Morning Audience - Summer Sale Campaign: 1,353
3. Weekend Audience - Website Traffic Push: 1,280
4. Morning Audience - Mobile Game Installs: 1,258
5. Evening Audience - Summer Sale Campaign: 1,153
6. Morning Audience - Website Traffic Push: 1,134
7. Evening Audience - Lead Gen - B2B: 1,114
8. Weekend Audience - App Install Campaign: 1,097
9. Evening Audience - Website Traffic Push: 1,010
10. Weekend Audience - Brand Awareness: 1,001
11. Weekend Audience - Lead Gen - B2B: 997
12. Morning Audience - App Install Campaign: 982
13. Weekend Audience - Mobile Game Installs: 928
14. Morning Audience - Brand Awareness: 920
15. Evening Audience - App Install Campaign: 891
16. Evening Audience - Brand Awareness: 808
17. Evening Audience - Mobile Game Installs: 710
18. Morning Audience - Blog Content Promotion: 705
19. Evening Audience - Black Friday Deals: 703
20. Morning Audience - Product Launch Teaser: 672
21. Weekend Audience - Newsletter Signup Campaign: 667
22. Evening Audience - Blog Content Promotion: 644
23. Weekend Audience - Summer Sale Campaign: 633
24. Weekend Audience - Black Friday Deals: 606
25. Evening Audience - Newsletter Signup Campaign: 601
26. Morning Audience - Holiday Sale - Purchases: 595
27. Weekend Audience - Product Launch Teaser: 594
28. Morning Audience - Newsletter Signup Campaign: 575
29. Weekend Audience - General Conversions: 572
30. Evening Audience - Holiday Sale - Purchases: 535
31. Morning Audience - Black Friday Deals: 529
32. Weekend Audience - Holiday Sale - Purchases: 514

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
  "top_n": 50,
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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'all adsets with clicks above 500'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'clicks', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'clicks', 'operator': '>', 'value': 500}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'all adsets with clicks above 500', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1858ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='adset', breakdown='adset', derived=None, need_timeseries=True, need_previous=False, base_measures=['clicks'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'clicks', 'operator': '>', 'value': 500}]}, top_n=50, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='clicks', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=50, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'clicks', 'operator': '>', 'value': 500}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='all adsets with clicks above 500', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['clicks']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for clicks
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for clicks: 125586.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'clicks': MetricValue(value=125586.0, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 125586.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for clicks by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 50, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=125586.0 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 20236.0}, {'date': '2025-10-24', 'value': 21447.0}, {'date': '2025-10-25', 'value': 20554.0}, {'date': '2025-10-26', 'value': 20930.0}, {'date': '2025-10-27', 'value': 21926.0}, {'date': '2025-10-28', 'value': 20493.0}] breakdown=[{'label': 'Morning Audience - Lead Gen - B2B', 'value': 1678.0, 'spend': 604.63, 'clicks': 1678, 'conversions': 360.73, 'revenue': 2502.48, 'impressions': 38899}, {'label': 'Morning Audience - Summer Sale Campaign', 'value': 1353.0, 'spend': 462.05, 'clicks': 1353, 'conversions': 67.0, 'revenue': 9777.93, 'impressions': 35487}, {'label': 'Weekend Audience - Website Traffic Push', 'value': 1280.0, 'spend': 555.51, 'clicks': 1280, 'conversions': 62.88, 'revenue': 3610.43, 'impressions': 38084}, {'label': 'Morning Audience - Mobile Game Installs', 'value': 1258.0, 'spend': 532.73, 'clicks': 1258, 'conversions': 116.0, 'revenue': 362.06, 'impressions': 44326}, {'label': 'Evening Audience - Summer Sale Campaign', 'value': 1153.0, 'spend': 434.67, 'clicks': 1153, 'conversions': 67.0, 'revenue': 6585.33, 'impressions': 37178}, {'label': 'Morning Audience - Website Traffic Push', 'value': 1134.0, 'spend': 448.79, 'clicks': 1134, 'conversions': 90.6, 'revenue': 4077.99, 'impressions': 33941}, {'label': 'Evening Audience - Lead Gen - B2B', 'value': 1114.0, 'spend': 456.26, 'clicks': 1114, 'conversions': 228.66, 'revenue': 1404.63, 'impressions': 34235}, {'label': 'Weekend Audience - App Install Campaign', 'value': 1097.0, 'spend': 536.41, 'clicks': 1097, 'conversions': 93.0, 'revenue': 195.43, 'impressions': 34584}, {'label': 'Evening Audience - Website Traffic Push', 'value': 1010.0, 'spend': 427.26, 'clicks': 1010, 'conversions': 71.46, 'revenue': 4063.25, 'impressions': 34967}, {'label': 'Weekend Audience - Brand Awareness', 'value': 1001.0, 'spend': 543.6, 'clicks': 1001, 'conversions': 11.54, 'revenue': 382.48, 'impressions': 40474}, {'label': 'Weekend Audience - Lead Gen - B2B', 'value': 997.0, 'spend': 363.8, 'clicks': 997, 'conversions': 195.86, 'revenue': 952.37, 'impressions': 25979}, {'label': 'Morning Audience - App Install Campaign', 'value': 982.0, 'spend': 500.73, 'clicks': 982, 'conversions': 101.0, 'revenue': 276.83, 'impressions': 31968}, {'label': 'Weekend Audience - Mobile Game Installs', 'value': 928.0, 'spend': 376.13, 'clicks': 928, 'conversions': 76.0, 'revenue': 137.79, 'impressions': 33277}, {'label': 'Morning Audience - Brand Awareness', 'value': 920.0, 'spend': 495.25, 'clicks': 920, 'conversions': 14.99, 'revenue': 591.74, 'impressions': 38937}, {'label': 'Evening Audience - App Install Campaign', 'value': 891.0, 'spend': 395.72, 'clicks': 891, 'conversions': 91.0, 'revenue': 318.76, 'impressions': 26529}, {'label': 'Evening Audience - Brand Awareness', 'value': 808.0, 'spend': 327.11, 'clicks': 808, 'conversions': 13.28, 'revenue': 424.92, 'impressions': 31668}, {'label': 'Evening Audience - Mobile Game Installs', 'value': 710.0, 'spend': 231.56, 'clicks': 710, 'conversions': 67.0, 'revenue': 155.47, 'impressions': 23397}, {'label': 'Morning Audience - Blog Content Promotion', 'value': 705.0, 'spend': 317.69, 'clicks': 705, 'conversions': 71.31, 'revenue': 4015.31, 'impressions': 37208}, {'label': 'Evening Audience - Black Friday Deals', 'value': 703.0, 'spend': 405.16, 'clicks': 703, 'conversions': 39.0, 'revenue': 3281.19, 'impressions': 33922}, {'label': 'Morning Audience - Product Launch Teaser', 'value': 672.0, 'spend': 334.32, 'clicks': 672, 'conversions': 16.54, 'revenue': 539.54, 'impressions': 39196}, {'label': 'Weekend Audience - Newsletter Signup Campaign', 'value': 667.0, 'spend': 330.67, 'clicks': 667, 'conversions': 118.89, 'revenue': 629.32, 'impressions': 29368}, {'label': 'Evening Audience - Blog Content Promotion', 'value': 644.0, 'spend': 251.68, 'clicks': 644, 'conversions': 67.24, 'revenue': 3643.6, 'impressions': 32480}, {'label': 'Weekend Audience - Summer Sale Campaign', 'value': 633.0, 'spend': 297.89, 'clicks': 633, 'conversions': 25.0, 'revenue': 3863.23, 'impressions': 19665}, {'label': 'Weekend Audience - Black Friday Deals', 'value': 606.0, 'spend': 431.25, 'clicks': 606, 'conversions': 24.0, 'revenue': 3317.55, 'impressions': 40871}, {'label': 'Evening Audience - Newsletter Signup Campaign', 'value': 601.0, 'spend': 370.48, 'clicks': 601, 'conversions': 104.45, 'revenue': 559.62, 'impressions': 38324}, {'label': 'Morning Audience - Holiday Sale - Purchases', 'value': 595.0, 'spend': 364.16, 'clicks': 595, 'conversions': 32.0, 'revenue': 4452.07, 'impressions': 32664}, {'label': 'Weekend Audience - Product Launch Teaser', 'value': 594.0, 'spend': 304.27, 'clicks': 594, 'conversions': 19.06, 'revenue': 693.97, 'impressions': 34288}, {'label': 'Morning Audience - Newsletter Signup Campaign', 'value': 575.0, 'spend': 280.12, 'clicks': 575, 'conversions': 96.57, 'revenue': 486.33, 'impressions': 30508}, {'label': 'Weekend Audience - General Conversions', 'value': 572.0, 'spend': 204.68, 'clicks': 572, 'conversions': 44.74, 'revenue': 3343.95, 'impressions': 32024}, {'label': 'Evening Audience - Holiday Sale - Purchases', 'value': 535.0, 'spend': 253.68, 'clicks': 535, 'conversions': 25.0, 'revenue': 3022.92, 'impressions': 29313}, {'label': 'Morning Audience - Black Friday Deals', 'value': 529.0, 'spend': 288.67, 'clicks': 529, 'conversions': 23.0, 'revenue': 3379.71, 'impressions': 29856}, {'label': 'Weekend Audience - Holiday Sale - Purchases', 'value': 514.0, 'spend': 219.13, 'clicks': 514, 'conversions': 27.0, 'revenue': 2944.01, 'impressions': 25157}] workspace_avg=125586.0
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are the adsets last week with CLICKS above 500:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2104ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are the adsets last week with CLICKS above 500:
```

---

## Test 65: which ad has the lowest cost per conversion?

**Answer**:
> The Video Ad - Weekend Audience - Lead Gen - B2B had the lowest cost per conversion at $1.68 last week—your best performer! For context, your overall CPA was $5.31, so this ad is really crushing it.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'which ad has the lowest cost per conversion?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpa', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 1, 'sort_order': 'asc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'which ad has the lowest cost per conversion?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 2422ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='ad', breakdown='ad', derived='cpa', need_timeseries=True, need_previous=False, base_measures=['conversions', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='asc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpa', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=1, sort_order='asc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='which ad has the lowest cost per conversion?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpa']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpa
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpa: 5.314210154983342911743130411
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpa': MetricValue(value=Decimal('5.314210154983342911743130411'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 5.314210154983342911743130411
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpa by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: asc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=5.314210154983343 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 5.403955094991365}, {'date': '2025-10-24', 'value': 5.03652698118533}, {'date': '2025-10-25', 'value': 4.962549765203165}, {'date': '2025-10-26', 'value': 5.654007994334908}, {'date': '2025-10-27', 'value': 5.345895624028586}, {'date': '2025-10-28', 'value': 5.52150227183911}] breakdown=[{'label': 'Video Ad - Weekend Audience - Lead Gen - B2B', 'value': 1.6783487563168602, 'spend': 511.46, 'clicks': 1503, 'conversions': 304.74, 'revenue': 1359.4, 'impressions': 35156}] workspace_avg=5.314210154983343
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Video Ad - Weekend Audience - Lead Gen - B2B had the lowest cost per conversion at $1.68 last week—your best performer! For context, your overall CPA was $5.31, so this ad is really crushing it.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1961ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 4645ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Video Ad - Weekend Audience - Lead Gen - B2B had the lowest cost per conversion at $1.68 last week—your best performer! For context, your overall CPA was $5.31, so this ad is really crushing it.'
```

---

## Test 66: show me campaigns with impressions over 10000

**Answer**:
> Here are the campaigns last week with IMPRESSIONS above 10,000:

1. Lead Gen - B2B: 42,491
2. Website Traffic Push: 35,596
3. Summer Sale Campaign: 31,363
4. Blog Content Promotion: 34,881
5. Newsletter Signup Campaign: 35,596
6. Holiday Sale - Purchases: 30,349
7. Mobile Game Installs: 23,606
8. Product Launch Teaser: 37,040
9. Black Friday Deals: 28,010
10. Brand Awareness: 27,467
11. App Install Campaign: 26,108
12. General Conversions: 22,583

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
  "top_n": 50,
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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'show me campaigns with impressions over 10000'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'impressions', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'impressions', 'operator': '>', 'value': 10000}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'show me campaigns with impressions over 10000', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1754ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['impressions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'impressions', 'operator': '>', 'value': 10000}]}, top_n=50, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='impressions', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=50, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'impressions', 'operator': '>', 'value': 10000}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='show me campaigns with impressions over 10000', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['impressions']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for impressions
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for impressions: 4953838.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'impressions': MetricValue(value=4953838.0, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 4953838.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for impressions by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 50, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=4953838.0 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 831689.0}, {'date': '2025-10-24', 'value': 845514.0}, {'date': '2025-10-25', 'value': 800607.0}, {'date': '2025-10-26', 'value': 830900.0}, {'date': '2025-10-27', 'value': 850347.0}, {'date': '2025-10-28', 'value': 794781.0}] breakdown=[{'label': 'Lead Gen - B2B', 'value': 42491.0, 'spend': 727.78, 'clicks': 1331, 'conversions': 234.25, 'revenue': 1272.83, 'impressions': 42491}, {'label': 'Website Traffic Push', 'value': 35596.0, 'spend': 480.89, 'clicks': 1254, 'conversions': 76.67, 'revenue': 3830.11, 'impressions': 35596}, {'label': 'Summer Sale Campaign', 'value': 31363.0, 'spend': 441.49, 'clicks': 1053, 'conversions': 57.0, 'revenue': 7730.26, 'impressions': 31363}, {'label': 'Blog Content Promotion', 'value': 34881.0, 'spend': 425.36, 'clicks': 658, 'conversions': 82.4, 'revenue': 4492.06, 'impressions': 34881}, {'label': 'Newsletter Signup Campaign', 'value': 35596.0, 'spend': 351.35, 'clicks': 775, 'conversions': 145.67, 'revenue': 701.78, 'impressions': 35596}, {'label': 'Holiday Sale - Purchases', 'value': 30349.0, 'spend': 343.06, 'clicks': 593, 'conversions': 28.0, 'revenue': 2734.58, 'impressions': 30349}, {'label': 'Mobile Game Installs', 'value': 23606.0, 'spend': 318.71, 'clicks': 536, 'conversions': 52.0, 'revenue': 177.79, 'impressions': 23606}, {'label': 'Product Launch Teaser', 'value': 37040.0, 'spend': 313.49, 'clicks': 491, 'conversions': 12.2, 'revenue': 395.09, 'impressions': 37040}, {'label': 'Black Friday Deals', 'value': 28010.0, 'spend': 308.25, 'clicks': 579, 'conversions': 30.0, 'revenue': 4605.55, 'impressions': 28010}, {'label': 'Brand Awareness', 'value': 27467.0, 'spend': 293.7, 'clicks': 661, 'conversions': 11.92, 'revenue': 475.13, 'impressions': 27467}, {'label': 'App Install Campaign', 'value': 26108.0, 'spend': 283.79, 'clicks': 738, 'conversions': 73.0, 'revenue': 177.12, 'impressions': 26108}, {'label': 'General Conversions', 'value': 22583.0, 'spend': 246.56, 'clicks': 497, 'conversions': 46.22, 'revenue': 3635.87, 'impressions': 22583}] workspace_avg=4953838.0
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are the campaigns last week with IMPRESSIONS above 10,000:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1992ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are the campaigns last week with IMPRESSIONS above 10,000:
```

---

## Test 67: worst performing adset by roas

**Answer**:
> The Weekend Audience - App Install Campaign had the lowest ROAS at 0.36× last week—definitely struggling. For context, your overall ROAS was 6.51×, so this ad set could use some attention.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'worst performing adset by roas'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 1, 'sort_order': 'asc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'worst performing adset by roas', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1241ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='adset', breakdown='adset', derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='asc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=1, sort_order='asc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='worst performing adset by roas', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.507078653503120199422664633'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for roas by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: asc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=6.50707865350312 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 5.8664627604890764}, {'date': '2025-10-24', 'value': 6.161505000243192}, {'date': '2025-10-25', 'value': 7.76569736303204}, {'date': '2025-10-26', 'value': 6.6619532432258985}, {'date': '2025-10-27', 'value': 6.218785967772876}, {'date': '2025-10-28', 'value': 6.452658599580624}] breakdown=[{'label': 'Weekend Audience - App Install Campaign', 'value': 0.3643295240580899, 'spend': 536.41, 'clicks': 1097, 'conversions': 93.0, 'revenue': 195.43, 'impressions': 34584}] workspace_avg=6.50707865350312
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Weekend Audience - App Install Campaign had the lowest ROAS at 0.36× last week—definitely struggling. For context, your overall ROAS was 6.51×, so this ad set could use some attention.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 2234ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3715ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Weekend Audience - App Install Campaign had the lowest ROAS at 0.36× last week—definitely struggling. For context, your overall ROAS was 6.51×, so this ad set could use some attention.'
```

---

## Test 68: all ads with ctr above 3%

**Answer**:
> None of your 50 ads currently have a click-through rate (CTR) above 3% in the last week. You might want to review your ad strategies to improve engagement.

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
  "top_n": 50,
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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'all ads with ctr above 3%'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'ctr', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'ctr', 'operator': '>', 'value': 3}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'all ads with ctr above 3%', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1568ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='ad', breakdown='ad', derived='ctr', need_timeseries=True, need_previous=False, base_measures=['clicks', 'impressions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'ctr', 'operator': '>', 'value': 3}]}, top_n=50, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='ctr', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=50, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'ctr', 'operator': '>', 'value': 3}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='all ads with ctr above 3%', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['ctr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for ctr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for ctr: 0.02535125290734174
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'ctr': MetricValue(value=0.02535125290734174, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.02535125290734174
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for ctr by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 50, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.02535125290734174 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 0.024331210344251276}, {'date': '2025-10-24', 'value': 0.025365635577885168}, {'date': '2025-10-25', 'value': 0.02567302059562307}, {'date': '2025-10-26', 'value': 0.02518955349620893}, {'date': '2025-10-27', 'value': 0.025784767865353792}, {'date': '2025-10-28', 'value': 0.0257844613799273}] breakdown=[] workspace_avg=0.02535125290734174
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: ad
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'None of your 50 ads currently have a click-through rate (CTR) above 3% in the last week. You might want to review your ad strategies to improve engagement.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 4286ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 6133ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'None of your 50 ads currently have a click-through rate (CTR) above 3% in the last week. You might want to review your ad strategies to improve engagement.'
```

---

## Test 69: which campaign generated the most leads?

**Answer**:
> The Lead Gen - B2B campaign generated the most leads last week with 234—your top performer! Overall, your lead count was right at the average with 4,165 leads.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'which campaign generated the most leads?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'leads', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'which campaign generated the most leads?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1084ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['leads'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='leads', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='which campaign generated the most leads?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['leads']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for leads
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for leads: 4164.69
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'leads': MetricValue(value=4164.69, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 4164.69
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for leads by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=4164.69 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 660.36}, {'date': '2025-10-24', 'value': 742.53}, {'date': '2025-10-25', 'value': 632.93}, {'date': '2025-10-26', 'value': 705.34}, {'date': '2025-10-27', 'value': 809.71}, {'date': '2025-10-28', 'value': 613.82}] breakdown=[{'label': 'Lead Gen - B2B', 'value': 234.25, 'spend': 727.78, 'clicks': 1331, 'conversions': 234.25, 'revenue': 1272.83, 'impressions': 42491}] workspace_avg=4164.69
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Lead Gen - B2B campaign generated the most leads last week with 234—your top performer! Overall, your lead count was right at the average with 4,165 leads.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1534ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2833ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Lead Gen - B2B campaign generated the most leads last week with 234—your top performer! Overall, your lead count was right at the average with 4,165 leads.'
```

---

## Test 70: show me adsets with spend below 50 dollars

**Answer**:
> None of your 35 adsets have a spend below $50 in the last week. It seems all your adsets are currently spending above this threshold.

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
  "top_n": 50,
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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'show me adsets with spend below 50 dollars'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'spend', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'spend', 'operator': '<', 'value': 50}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'show me adsets with spend below 50 dollars', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1532ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='adset', breakdown='adset', derived=None, need_timeseries=True, need_previous=False, base_measures=['spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'spend', 'operator': '<', 'value': 50}]}, top_n=50, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='spend', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=50, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'spend', 'operator': '<', 'value': 50}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='show me adsets with spend below 50 dollars', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 56868.16
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=56868.16, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 56868.16
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for spend by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 50, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=56868.16 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 9386.67}, {'date': '2025-10-24', 'value': 9457.54}, {'date': '2025-10-25', 'value': 8887.48}, {'date': '2025-10-26', 'value': 9661.06}, {'date': '2025-10-27', 'value': 10008.96}, {'date': '2025-10-28', 'value': 9466.45}] breakdown=[] workspace_avg=56868.16
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: adset
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'None of your 35 adsets have a spend below $50 in the last week. It seems all your adsets are currently spending above this threshold.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1402ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3146ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'None of your 35 adsets have a spend below $50 in the last week. It seems all your adsets are currently spending above this threshold.'
```

---

## Test 71: best performing ad by revenue per click

**Answer**:
> The Carousel Ad - Evening Audience - Summer Sale Campaign had the highest ROAS at 24.45× last week—crushing it as your top performer! For context, your overall ROAS was 6.51×, so this ad really stood out.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'best performing ad by revenue per click'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'best performing ad by revenue per click', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1365ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='ad', breakdown='ad', derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='best performing ad by revenue per click', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.507078653503120199422664633'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for roas by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=6.50707865350312 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 5.8664627604890764}, {'date': '2025-10-24', 'value': 6.161505000243192}, {'date': '2025-10-25', 'value': 7.76569736303204}, {'date': '2025-10-26', 'value': 6.6619532432258985}, {'date': '2025-10-27', 'value': 6.218785967772876}, {'date': '2025-10-28', 'value': 6.452658599580624}] breakdown=[{'label': 'Carousel Ad - Evening Audience - Summer Sale Campaign', 'value': 24.447477140563507, 'spend': 510.73, 'clicks': 1729, 'conversions': 88.0, 'revenue': 12486.06, 'impressions': 37836}] workspace_avg=6.50707865350312
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Carousel Ad - Evening Audience - Summer Sale Campaign had the highest ROAS at 24.45× last week—crushing it as your top performer! For context, your overall ROAS was 6.51×, so this ad really stood out.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1813ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3426ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Carousel Ad - Evening Audience - Summer Sale Campaign had the highest ROAS at 24.45× last week—crushing it as your top performer! For context, your overall ROAS was 6.51×, so this ad really stood out.'
```

---

## Test 72: all campaigns with cpm under 10 dollars

**Answer**:
> In the last week, there were two campaigns with a CPM under $10. 

1. **Newsletter Signup Campaign**: This campaign had a CPM of $9.87. It spent $351.35, garnered 775 clicks, and achieved 145.67 conversions, generating a revenue of $701.78 from 35,596 impressions.

2. **Product Launch Teaser**: With a CPM of $8.46, this campaign spent $313.49 and received 491 clicks. It resulted in 12.2 conversions and brought in $395.09 in revenue from 37,040 impressions.

In total, there were 2 campaigns meeting the criteria.

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
  "top_n": 50,
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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'all campaigns with cpm under 10 dollars'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpm', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'cpm', 'operator': '<', 'value': 10}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'all campaigns with cpm under 10 dollars', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 2433ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived='cpm', need_timeseries=True, need_previous=False, base_measures=['impressions', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'cpm', 'operator': '<', 'value': 10}]}, top_n=50, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpm', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=50, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'cpm', 'operator': '<', 'value': 10}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='all campaigns with cpm under 10 dollars', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpm']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpm
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpm: 11.47961641054875028210450160
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpm': MetricValue(value=Decimal('11.47961641054875028210450160'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 11.47961641054875028210450160
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpm by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 50, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=11.47961641054875 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 11.286274076006777}, {'date': '2025-10-24', 'value': 11.1855510375937}, {'date': '2025-10-25', 'value': 11.100927171508618}, {'date': '2025-10-26', 'value': 11.627223492598388}, {'date': '2025-10-27', 'value': 11.770441948992588}, {'date': '2025-10-28', 'value': 11.910765355487865}] breakdown=[{'label': 'Newsletter Signup Campaign', 'value': 9.870491066411956, 'spend': 351.35, 'clicks': 775, 'conversions': 145.67, 'revenue': 701.78, 'impressions': 35596}, {'label': 'Product Launch Teaser', 'value': 8.463552915766739, 'spend': 313.49, 'clicks': 491, 'conversions': 12.2, 'revenue': 395.09, 'impressions': 37040}] workspace_avg=11.47961641054875
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'In the last week, there were two campaigns with a CPM under $10. 
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 2931ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 5583ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'In the last week, there were two campaigns with a CPM under $10. 
```

---

## Test 73: which adset has the highest conversion rate?

**Answer**:
> The "Morning Audience - Lead Gen - B2B" adset had the highest conversion rate at 21.5% last week—your top performer! For context, your overall conversion rate was 8.5%, so this adset is really standing out.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'which adset has the highest conversion rate?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cvr', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'which adset has the highest conversion rate?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 2713ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='adset', breakdown='adset', derived='cvr', need_timeseries=True, need_previous=False, base_measures=['clicks', 'conversions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cvr', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='which adset has the highest conversion rate?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cvr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cvr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cvr: 0.08520973675409679422865606039
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cvr': MetricValue(value=Decimal('0.08520973675409679422865606039'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.08520973675409679422865606039
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cvr by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.0852097367540968 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 0.08583712196086184}, {'date': '2025-10-24', 'value': 0.0875549027836061}, {'date': '2025-10-25', 'value': 0.08713194512017125}, {'date': '2025-10-26', 'value': 0.08163927376970856}, {'date': '2025-10-27', 'value': 0.08539040408647268}, {'date': '2025-10-28', 'value': 0.08366125018298931}] breakdown=[{'label': 'Morning Audience - Lead Gen - B2B', 'value': 0.2149761620977354, 'spend': 604.63, 'clicks': 1678, 'conversions': 360.73, 'revenue': 2502.48, 'impressions': 38899}] workspace_avg=0.0852097367540968
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The "Morning Audience - Lead Gen - B2B" adset had the highest conversion rate at 21.5% last week—your top performer! For context, your overall conversion rate was 8.5%, so this adset is really standing out.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1799ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 4738ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The "Morning Audience - Lead Gen - B2B" adset had the highest conversion rate at 21.5% last week—your top performer! For context, your overall conversion rate was 8.5%, so this adset is really standing out.'
```

---

## Test 74: show me ads with conversions above 20

**Answer**:
> Here are the ads last week with CONVERSIONS above 20:

1. Video Ad - Weekend Audience - Lead Gen - B2B: 305
2. Image Ad - Weekend Audience - Lead Gen - B2B: 225
3. Image Ad - Morning Audience - Lead Gen - B2B: 204
4. Video Ad - Evening Audience - Lead Gen - B2B: 198
5. Video Ad - Morning Audience - Lead Gen - B2B: 186
6. Carousel Ad - Evening Audience - Lead Gen - B2B: 176
7. Carousel Ad - Weekend Audience - Lead Gen - B2B: 164
8. Image Ad - Evening Audience - Lead Gen - B2B: 159
9. Video Ad - Evening Audience - Newsletter Signup Campaign: 149
10. Image Ad - Evening Audience - App Install Campaign: 141
11. Video Ad - Morning Audience - App Install Campaign: 140
12. Carousel Ad - Morning Audience - Lead Gen - B2B: 137
13. Image Ad - Morning Audience - App Install Campaign: 136
14. Image Ad - Weekend Audience - App Install Campaign: 131
15. Carousel Ad - Morning Audience - App Install Campaign: 126
16. Carousel Ad - Weekend Audience - App Install Campaign: 124
17. Carousel Ad - Morning Audience - Newsletter Signup Campaign: 114
18. Carousel Ad - Evening Audience - App Install Campaign: 113
19. Video Ad - Evening Audience - App Install Campaign: 111
20. Image Ad - Weekend Audience - Newsletter Signup Campaign: 110
21. Carousel Ad - Weekend Audience - Newsletter Signup Campaign: 109
22. Video Ad - Weekend Audience - App Install Campaign: 109
23. Video Ad - Weekend Audience - Newsletter Signup Campaign: 104
24. Image Ad - Evening Audience - Newsletter Signup Campaign: 103
25. Carousel Ad - Evening Audience - Newsletter Signup Campaign: 101
26. Carousel Ad - Morning Audience - Blog Content Promotion: 96
27. Carousel Ad - Evening Audience - Summer Sale Campaign: 88
28. Image Ad - Morning Audience - Summer Sale Campaign: 87
29. Video Ad - Morning Audience - Mobile Game Installs: 86
30. Video Ad - Morning Audience - Website Traffic Push: 85
31. Image Ad - Morning Audience - Website Traffic Push: 84
32. Carousel Ad - Morning Audience - Website Traffic Push: 83
33. Image Ad - Weekend Audience - Website Traffic Push: 81
34. Carousel Ad - Morning Audience - Mobile Game Installs: 81
35. Carousel Ad - Evening Audience - Blog Content Promotion: 81
36. Image Ad - Morning Audience - Blog Content Promotion: 80
37. Carousel Ad - Weekend Audience - Website Traffic Push: 78
38. Carousel Ad - Evening Audience - Mobile Game Installs: 77
39. Image Ad - Evening Audience - Blog Content Promotion: 77
40. Video Ad - Weekend Audience - Mobile Game Installs: 75
41. Video Ad - Weekend Audience - Summer Sale Campaign: 74
42. Image Ad - Morning Audience - Mobile Game Installs: 74
43. Image Ad - Evening Audience - Mobile Game Installs: 72
44. Video Ad - Evening Audience - Website Traffic Push: 70
45. Carousel Ad - Evening Audience - Website Traffic Push: 70
46. Carousel Ad - Weekend Audience - Mobile Game Installs: 69
47. Image Ad - Morning Audience - Newsletter Signup Campaign: 69
48. Video Ad - Morning Audience - Blog Content Promotion: 68
49. Video Ad - Evening Audience - Blog Content Promotion: 68
50. Video Ad - Evening Audience - Mobile Game Installs: 67

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
  "top_n": 50,
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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'show me ads with conversions above 20'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'conversions', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'conversions', 'operator': '>', 'value': 20}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'show me ads with conversions above 20', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1290ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='ad', breakdown='ad', derived=None, need_timeseries=True, need_previous=False, base_measures=['conversions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'conversions', 'operator': '>', 'value': 20}]}, top_n=50, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='conversions', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=50, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'conversions', 'operator': '>', 'value': 20}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='show me ads with conversions above 20', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['conversions']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for conversions
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for conversions: 10701.15
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'conversions': MetricValue(value=10701.15, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 10701.15
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for conversions by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 50, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=10701.15 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 1737.0}, {'date': '2025-10-24', 'value': 1877.79}, {'date': '2025-10-25', 'value': 1790.91}, {'date': '2025-10-26', 'value': 1708.71}, {'date': '2025-10-27', 'value': 1872.27}, {'date': '2025-10-28', 'value': 1714.47}] breakdown=[{'label': 'Video Ad - Weekend Audience - Lead Gen - B2B', 'value': 304.74, 'spend': 511.46, 'clicks': 1503, 'conversions': 304.74, 'revenue': 1359.4, 'impressions': 35156}, {'label': 'Image Ad - Weekend Audience - Lead Gen - B2B', 'value': 225.43, 'spend': 441.45, 'clicks': 1051, 'conversions': 225.43, 'revenue': 842.95, 'impressions': 26954}, {'label': 'Image Ad - Morning Audience - Lead Gen - B2B', 'value': 203.54, 'spend': 492.6, 'clicks': 1250, 'conversions': 203.54, 'revenue': 1360.93, 'impressions': 35883}, {'label': 'Video Ad - Evening Audience - Lead Gen - B2B', 'value': 197.88, 'spend': 545.66, 'clicks': 1173, 'conversions': 197.88, 'revenue': 1276.04, 'impressions': 39594}, {'label': 'Video Ad - Morning Audience - Lead Gen - B2B', 'value': 186.41, 'spend': 469.25, 'clicks': 1100, 'conversions': 186.41, 'revenue': 1227.84, 'impressions': 30115}, {'label': 'Carousel Ad - Evening Audience - Lead Gen - B2B', 'value': 175.68, 'spend': 475.85, 'clicks': 869, 'conversions': 175.68, 'revenue': 478.6, 'impressions': 30798}, {'label': 'Carousel Ad - Weekend Audience - Lead Gen - B2B', 'value': 163.73, 'spend': 456.21, 'clicks': 1096, 'conversions': 163.73, 'revenue': 673.9, 'impressions': 29800}, {'label': 'Image Ad - Evening Audience - Lead Gen - B2B', 'value': 159.39, 'spend': 365.04, 'clicks': 974, 'conversions': 159.39, 'revenue': 981.28, 'impressions': 27232}, {'label': 'Video Ad - Evening Audience - Newsletter Signup Campaign', 'value': 149.07, 'spend': 389.17, 'clicks': 719, 'conversions': 149.07, 'revenue': 782.38, 'impressions': 33738}, {'label': 'Image Ad - Evening Audience - App Install Campaign', 'value': 141.0, 'spend': 586.66, 'clicks': 1330, 'conversions': 141.0, 'revenue': 391.92, 'impressions': 38448}, {'label': 'Video Ad - Morning Audience - App Install Campaign', 'value': 140.0, 'spend': 503.28, 'clicks': 1193, 'conversions': 140.0, 'revenue': 380.66, 'impressions': 32770}, {'label': 'Carousel Ad - Morning Audience - Lead Gen - B2B', 'value': 137.13, 'spend': 340.25, 'clicks': 850, 'conversions': 137.13, 'revenue': 838.7, 'impressions': 23698}, {'label': 'Image Ad - Morning Audience - App Install Campaign', 'value': 136.0, 'spend': 478.22, 'clicks': 1057, 'conversions': 136.0, 'revenue': 184.59, 'impressions': 34390}, {'label': 'Image Ad - Weekend Audience - App Install Campaign', 'value': 131.0, 'spend': 471.86, 'clicks': 1211, 'conversions': 131.0, 'revenue': 372.51, 'impressions': 33964}, {'label': 'Carousel Ad - Morning Audience - App Install Campaign', 'value': 126.0, 'spend': 571.36, 'clicks': 1273, 'conversions': 126.0, 'revenue': 245.69, 'impressions': 41938}, {'label': 'Carousel Ad - Weekend Audience - App Install Campaign', 'value': 124.0, 'spend': 532.46, 'clicks': 1580, 'conversions': 124.0, 'revenue': 218.05, 'impressions': 39161}, {'label': 'Carousel Ad - Morning Audience - Newsletter Signup Campaign', 'value': 113.59, 'spend': 343.68, 'clicks': 665, 'conversions': 113.59, 'revenue': 593.94, 'impressions': 36619}, {'label': 'Carousel Ad - Evening Audience - App Install Campaign', 'value': 113.0, 'spend': 355.01, 'clicks': 1106, 'conversions': 113.0, 'revenue': 258.02, 'impressions': 28872}, {'label': 'Video Ad - Evening Audience - App Install Campaign', 'value': 111.0, 'spend': 372.53, 'clicks': 1177, 'conversions': 111.0, 'revenue': 162.86, 'impressions': 30702}, {'label': 'Image Ad - Weekend Audience - Newsletter Signup Campaign', 'value': 110.14, 'spend': 423.27, 'clicks': 697, 'conversions': 110.14, 'revenue': 370.86, 'impressions': 37403}, {'label': 'Carousel Ad - Weekend Audience - Newsletter Signup Campaign', 'value': 109.21, 'spend': 286.32, 'clicks': 595, 'conversions': 109.21, 'revenue': 507.79, 'impressions': 33471}, {'label': 'Video Ad - Weekend Audience - App Install Campaign', 'value': 109.0, 'spend': 483.79, 'clicks': 1094, 'conversions': 109.0, 'revenue': 332.42, 'impressions': 36113}, {'label': 'Video Ad - Weekend Audience - Newsletter Signup Campaign', 'value': 103.64, 'spend': 385.41, 'clicks': 653, 'conversions': 103.64, 'revenue': 667.42, 'impressions': 31594}, {'label': 'Image Ad - Evening Audience - Newsletter Signup Campaign', 'value': 102.92, 'spend': 316.87, 'clicks': 553, 'conversions': 102.92, 'revenue': 669.27, 'impressions': 30931}, {'label': 'Carousel Ad - Evening Audience - Newsletter Signup Campaign', 'value': 101.2, 'spend': 207.79, 'clicks': 508, 'conversions': 101.2, 'revenue': 682.44, 'impressions': 29751}, {'label': 'Carousel Ad - Morning Audience - Blog Content Promotion', 'value': 96.15, 'spend': 316.99, 'clicks': 527, 'conversions': 96.15, 'revenue': 5671.27, 'impressions': 27086}, {'label': 'Carousel Ad - Evening Audience - Summer Sale Campaign', 'value': 88.0, 'spend': 510.73, 'clicks': 1729, 'conversions': 88.0, 'revenue': 12486.06, 'impressions': 37836}, {'label': 'Image Ad - Morning Audience - Summer Sale Campaign', 'value': 87.0, 'spend': 483.96, 'clicks': 1240, 'conversions': 87.0, 'revenue': 10552.61, 'impressions': 33268}, {'label': 'Video Ad - Morning Audience - Mobile Game Installs', 'value': 86.0, 'spend': 422.69, 'clicks': 813, 'conversions': 86.0, 'revenue': 292.99, 'impressions': 33463}, {'label': 'Video Ad - Morning Audience - Website Traffic Push', 'value': 84.83, 'spend': 689.61, 'clicks': 1782, 'conversions': 84.83, 'revenue': 4631.65, 'impressions': 46764}, {'label': 'Image Ad - Morning Audience - Website Traffic Push', 'value': 83.75, 'spend': 468.0, 'clicks': 1468, 'conversions': 83.75, 'revenue': 5393.26, 'impressions': 37803}, {'label': 'Carousel Ad - Morning Audience - Website Traffic Push', 'value': 82.51, 'spend': 464.04, 'clicks': 1456, 'conversions': 82.51, 'revenue': 4808.89, 'impressions': 41749}, {'label': 'Image Ad - Weekend Audience - Website Traffic Push', 'value': 81.4, 'spend': 573.18, 'clicks': 1451, 'conversions': 81.4, 'revenue': 3789.59, 'impressions': 42313}, {'label': 'Carousel Ad - Morning Audience - Mobile Game Installs', 'value': 81.0, 'spend': 417.72, 'clicks': 780, 'conversions': 81.0, 'revenue': 231.56, 'impressions': 32359}, {'label': 'Carousel Ad - Evening Audience - Blog Content Promotion', 'value': 80.57, 'spend': 271.6, 'clicks': 623, 'conversions': 80.57, 'revenue': 3632.19, 'impressions': 26874}, {'label': 'Image Ad - Morning Audience - Blog Content Promotion', 'value': 79.79, 'spend': 374.44, 'clicks': 735, 'conversions': 79.79, 'revenue': 4305.65, 'impressions': 37195}, {'label': 'Carousel Ad - Weekend Audience - Website Traffic Push', 'value': 78.22, 'spend': 361.69, 'clicks': 698, 'conversions': 78.22, 'revenue': 4861.9, 'impressions': 27432}, {'label': 'Carousel Ad - Evening Audience - Mobile Game Installs', 'value': 77.0, 'spend': 466.27, 'clicks': 709, 'conversions': 77.0, 'revenue': 152.56, 'impressions': 35058}, {'label': 'Image Ad - Evening Audience - Blog Content Promotion', 'value': 76.84, 'spend': 206.57, 'clicks': 456, 'conversions': 76.84, 'revenue': 3807.62, 'impressions': 30357}, {'label': 'Video Ad - Weekend Audience - Mobile Game Installs', 'value': 75.0, 'spend': 381.8, 'clicks': 611, 'conversions': 75.0, 'revenue': 267.69, 'impressions': 34003}, {'label': 'Video Ad - Weekend Audience - Summer Sale Campaign', 'value': 74.0, 'spend': 454.83, 'clicks': 1142, 'conversions': 74.0, 'revenue': 9024.82, 'impressions': 36243}, {'label': 'Image Ad - Morning Audience - Mobile Game Installs', 'value': 74.0, 'spend': 391.0, 'clicks': 815, 'conversions': 74.0, 'revenue': 247.13, 'impressions': 31341}, {'label': 'Image Ad - Evening Audience - Mobile Game Installs', 'value': 72.0, 'spend': 376.46, 'clicks': 700, 'conversions': 72.0, 'revenue': 96.3, 'impressions': 26769}, {'label': 'Video Ad - Evening Audience - Website Traffic Push', 'value': 70.46, 'spend': 317.11, 'clicks': 994, 'conversions': 70.46, 'revenue': 3563.88, 'impressions': 28097}, {'label': 'Carousel Ad - Evening Audience - Website Traffic Push', 'value': 69.91, 'spend': 458.87, 'clicks': 1329, 'conversions': 69.91, 'revenue': 4215.67, 'impressions': 34908}, {'label': 'Carousel Ad - Weekend Audience - Mobile Game Installs', 'value': 69.0, 'spend': 503.51, 'clicks': 802, 'conversions': 69.0, 'revenue': 110.94, 'impressions': 32820}, {'label': 'Image Ad - Morning Audience - Newsletter Signup Campaign', 'value': 68.93, 'spend': 201.29, 'clicks': 473, 'conversions': 68.93, 'revenue': 241.5, 'impressions': 26403}, {'label': 'Video Ad - Morning Audience - Blog Content Promotion', 'value': 68.34, 'spend': 356.31, 'clicks': 748, 'conversions': 68.34, 'revenue': 4296.04, 'impressions': 34754}, {'label': 'Video Ad - Evening Audience - Blog Content Promotion', 'value': 68.18, 'spend': 319.69, 'clicks': 669, 'conversions': 68.18, 'revenue': 3723.74, 'impressions': 31487}, {'label': 'Video Ad - Evening Audience - Mobile Game Installs', 'value': 67.0, 'spend': 271.0, 'clicks': 645, 'conversions': 67.0, 'revenue': 168.45, 'impressions': 23739}] workspace_avg=10701.15
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are the ads last week with CONVERSIONS above 20:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1526ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are the ads last week with CONVERSIONS above 20:
```

---

## Test 75: worst performing campaign by cost per lead

**Answer**:
> The "General Conversions" campaign had a cost per lead of $13.65 last week, which was right at the average for your workspace. It's not standing out as a top performer, but it's holding steady compared to everything else.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'worst performing campaign by cost per lead'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpl', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'asc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'worst performing campaign by cost per lead', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1203ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived='cpl', need_timeseries=True, need_previous=False, base_measures=['leads', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='asc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpl', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='asc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='worst performing campaign by cost per lead', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpl']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpl
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpl: 13.65483625431904895682511784
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpl': MetricValue(value=Decimal('13.65483625431904895682511784'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 13.65483625431904895682511784
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpl by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: asc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=13.654836254319049 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 14.214473923314555}, {'date': '2025-10-24', 'value': 12.736912986680673}, {'date': '2025-10-25', 'value': 14.041805570916216}, {'date': '2025-10-26', 'value': 13.697025547962685}, {'date': '2025-10-27', 'value': 12.3611663435057}, {'date': '2025-10-28', 'value': 15.422192173601381}] breakdown=[{'label': 'General Conversions', 'value': None, 'spend': 246.56, 'clicks': 497, 'conversions': 46.22, 'revenue': 3635.87, 'impressions': 22583}] workspace_avg=13.654836254319049
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The "General Conversions" campaign had a cost per lead of $13.65 last week, which was right at the average for your workspace. It's not standing out as a top performer, but it's holding steady compared to everything else.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 2787ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 4231ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The "General Conversions" campaign had a cost per lead of $13.65 last week, which was right at the average for your workspace. It's not standing out as a top performer, but it's holding steady compared to everything else.'
```

---

## Test 76: all adsets with revenue above 5000

**Answer**:
> Here are the ad sets from last week that generated revenue above $5,000:

1. **Morning Audience - Summer Sale Campaign**: This ad set brought in $9,777.93 in revenue. 

2. **Evening Audience - Summer Sale Campaign**: This ad set generated $6,585.33 in revenue.

In total, there are 2 ad sets that exceeded the $5,000 revenue mark during this period.

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
  "top_n": 50,
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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'all adsets with revenue above 5000'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'revenue', 'operator': '>', 'value': 5000}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'all adsets with revenue above 5000', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1595ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='adset', breakdown='adset', derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'revenue', 'operator': '>', 'value': 5000}]}, top_n=50, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=50, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'revenue', 'operator': '>', 'value': 5000}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='all adsets with revenue above 5000', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 370045.59
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=370045.59, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 370045.59
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for revenue by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 50, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=370045.59 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 55066.55}, {'date': '2025-10-24', 'value': 58272.68}, {'date': '2025-10-25', 'value': 69017.48}, {'date': '2025-10-26', 'value': 64361.53}, {'date': '2025-10-27', 'value': 62243.58}, {'date': '2025-10-28', 'value': 61083.77}] breakdown=[{'label': 'Morning Audience - Summer Sale Campaign', 'value': 9777.93, 'spend': 462.05, 'clicks': 1353, 'conversions': 67.0, 'revenue': 9777.93, 'impressions': 35487}, {'label': 'Evening Audience - Summer Sale Campaign', 'value': 6585.33, 'spend': 434.67, 'clicks': 1153, 'conversions': 67.0, 'revenue': 6585.33, 'impressions': 37178}] workspace_avg=370045.59
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are the ad sets from last week that generated revenue above $5,000:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 2451ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 4277ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are the ad sets from last week that generated revenue above $5,000:
```

---

## Test 77: which ad has the best profit margin?

**Answer**:
> The Video Ad - Morning Audience - Website Traffic Push had the best profit margin at $1,396.42 last week—your top performer! For context, this was right on par with your overall average profit of $111,922.76.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'which ad has the best profit margin?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'profit', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'which ad has the best profit margin?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 2512ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='ad', breakdown='ad', derived=None, need_timeseries=True, need_previous=False, base_measures=['profit'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='profit', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='which ad has the best profit margin?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['profit']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for profit
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for profit: 111922.76
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'profit': MetricValue(value=111922.76, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 111922.76
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for profit by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=111922.76 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 17432.2}, {'date': '2025-10-24', 'value': 17975.92}, {'date': '2025-10-25', 'value': 21491.89}, {'date': '2025-10-26', 'value': 18980.13}, {'date': '2025-10-27', 'value': 17862.54}, {'date': '2025-10-28', 'value': 18180.08}] breakdown=[{'label': 'Video Ad - Morning Audience - Website Traffic Push', 'value': 1396.42, 'spend': 689.61, 'clicks': 1782, 'conversions': 84.83, 'revenue': 4631.65, 'impressions': 46764}] workspace_avg=111922.76
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Video Ad - Morning Audience - Website Traffic Push had the best profit margin at $1,396.42 last week—your top performer! For context, this was right on par with your overall average profit of $111,922.76.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 3846ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 6620ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Video Ad - Morning Audience - Website Traffic Push had the best profit margin at $1,396.42 last week—your top performer! For context, this was right on par with your overall average profit of $111,922.76.'
```

---

## Test 78: show me campaigns with clicks over 1000

**Answer**:
> Here are the campaigns from last week that had over 1,000 clicks:

1. **Lead Gen - B2B**: This campaign achieved 1,331 clicks. It had a spend of $727.78 and generated revenue of $1,272.83 from 42,491 impressions.

2. **Website Traffic Push**: This campaign garnered 1,254 clicks. The spend was $480.89, and it brought in $3,830.11 in revenue from 35,596 impressions.

3. **Summer Sale Campaign**: This campaign received 1,053 clicks. It had a spend of $441.49 and resulted in $7,730.26 in revenue from 31,363 impressions.

In total, there are 3 campaigns that met the criteria of having over 1,000 clicks last week.

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
  "top_n": 50,
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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'show me campaigns with clicks over 1000'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'clicks', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'clicks', 'operator': '>', 'value': 1000}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'show me campaigns with clicks over 1000', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1996ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['clicks'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'clicks', 'operator': '>', 'value': 1000}]}, top_n=50, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='clicks', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=50, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'clicks', 'operator': '>', 'value': 1000}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='show me campaigns with clicks over 1000', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['clicks']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for clicks
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for clicks: 125586.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'clicks': MetricValue(value=125586.0, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 125586.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for clicks by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 50, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=125586.0 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 20236.0}, {'date': '2025-10-24', 'value': 21447.0}, {'date': '2025-10-25', 'value': 20554.0}, {'date': '2025-10-26', 'value': 20930.0}, {'date': '2025-10-27', 'value': 21926.0}, {'date': '2025-10-28', 'value': 20493.0}] breakdown=[{'label': 'Lead Gen - B2B', 'value': 1331.0, 'spend': 727.78, 'clicks': 1331, 'conversions': 234.25, 'revenue': 1272.83, 'impressions': 42491}, {'label': 'Website Traffic Push', 'value': 1254.0, 'spend': 480.89, 'clicks': 1254, 'conversions': 76.67, 'revenue': 3830.11, 'impressions': 35596}, {'label': 'Summer Sale Campaign', 'value': 1053.0, 'spend': 441.49, 'clicks': 1053, 'conversions': 57.0, 'revenue': 7730.26, 'impressions': 31363}] workspace_avg=125586.0
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are the campaigns from last week that had over 1,000 clicks:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 6154ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 8428ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are the campaigns from last week that had over 1,000 clicks:
```

---

## Test 79: best performing adset by average order value

**Answer**:
> The Morning Audience - Lead Gen - B2B adset had the lowest AOV at $6.94 last week—definitely struggling compared to the rest. For context, your overall AOV was $34.58, so this adset needs some attention.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'best performing adset by average order value'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'aov', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'best performing adset by average order value', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1513ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='adset', breakdown='adset', derived='aov', need_timeseries=True, need_previous=False, base_measures=['purchases', 'revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='aov', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='best performing adset by average order value', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['aov']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for aov
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for aov: 34.57998345972161870453175593
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'aov': MetricValue(value=Decimal('34.57998345972161870453175593'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 34.57998345972161870453175593
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for aov by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=34.57998345972162 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 31.70210132412205}, {'date': '2025-10-24', 'value': 31.032586178433156}, {'date': '2025-10-25', 'value': 38.53765962555349}, {'date': '2025-10-26', 'value': 37.6667368950846}, {'date': '2025-10-27', 'value': 33.244980691887385}, {'date': '2025-10-28', 'value': 35.62836911698659}] breakdown=[{'label': 'Morning Audience - Lead Gen - B2B', 'value': 6.937266099298644, 'spend': 604.63, 'clicks': 1678, 'conversions': 360.73, 'revenue': 2502.48, 'impressions': 38899}] workspace_avg=34.57998345972162
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Morning Audience - Lead Gen - B2B adset had the lowest AOV at $6.94 last week—definitely struggling compared to the rest. For context, your overall AOV was $34.58, so this adset needs some attention.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1786ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3524ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Morning Audience - Lead Gen - B2B adset had the lowest AOV at $6.94 last week—definitely struggling compared to the rest. For context, your overall AOV was $34.58, so this adset needs some attention.'
```

---

## Test 80: all ads with spend above 200 dollars

**Answer**:
> Here are the ads last week with SPEND above $200.00:

1. Video Ad - Morning Audience - Website Traffic Push: $689.61
2. Image Ad - Evening Audience - App Install Campaign: $586.66
3. Image Ad - Weekend Audience - Website Traffic Push: $573.18
4. Carousel Ad - Morning Audience - App Install Campaign: $571.36
5. Video Ad - Evening Audience - Lead Gen - B2B: $545.66
6. Carousel Ad - Weekend Audience - Summer Sale Campaign: $544.26
7. Image Ad - Weekend Audience - Brand Awareness: $534.78
8. Carousel Ad - Weekend Audience - App Install Campaign: $532.46
9. Video Ad - Weekend Audience - Lead Gen - B2B: $511.46
10. Carousel Ad - Evening Audience - Summer Sale Campaign: $510.73
11. Carousel Ad - Weekend Audience - Mobile Game Installs: $503.51
12. Video Ad - Morning Audience - App Install Campaign: $503.28
13. Image Ad - Morning Audience - Lead Gen - B2B: $492.60
14. Image Ad - Morning Audience - Summer Sale Campaign: $483.96
15. Video Ad - Weekend Audience - App Install Campaign: $483.79
16. Video Ad - Weekend Audience - Holiday Sale - Purchases: $483.66
17. Image Ad - Morning Audience - App Install Campaign: $478.22
18. Carousel Ad - Evening Audience - Lead Gen - B2B: $475.85
19. Image Ad - Weekend Audience - App Install Campaign: $471.86
20. Video Ad - Morning Audience - Lead Gen - B2B: $469.25
21. Carousel Ad - Morning Audience - Summer Sale Campaign: $468.25
22. Image Ad - Morning Audience - Website Traffic Push: $468.00
23. Carousel Ad - Weekend Audience - Brand Awareness: $466.45
24. Carousel Ad - Evening Audience - Mobile Game Installs: $466.27
25. Carousel Ad - Morning Audience - Website Traffic Push: $464.04
26. Video Ad - Weekend Audience - Website Traffic Push: $459.64
27. Carousel Ad - Evening Audience - Website Traffic Push: $458.87
28. Carousel Ad - Weekend Audience - Lead Gen - B2B: $456.21
29. Image Ad - Evening Audience - Summer Sale Campaign: $455.14
30. Video Ad - Weekend Audience - Summer Sale Campaign: $454.83
31. Image Ad - Weekend Audience - Lead Gen - B2B: $441.45
32. Image Ad - Evening Audience - Website Traffic Push: $440.58
33. Image Ad - Weekend Audience - Newsletter Signup Campaign: $423.27
34. Video Ad - Morning Audience - Mobile Game Installs: $422.69
35. Video Ad - Evening Audience - Brand Awareness: $421.79
36. Carousel Ad - Morning Audience - Mobile Game Installs: $417.72
37. Image Ad - Weekend Audience - Holiday Sale - Purchases: $415.12
38. Carousel Ad - Morning Audience - Brand Awareness: $408.52
39. Video Ad - Morning Audience - Holiday Sale - Purchases: $405.75
40. Image Ad - Morning Audience - Brand Awareness: $403.35
41. Image Ad - Morning Audience - Mobile Game Installs: $391.00
42. Video Ad - Evening Audience - Newsletter Signup Campaign: $389.17
43. Carousel Ad - Evening Audience - Brand Awareness: $389.09
44. Image Ad - Evening Audience - Brand Awareness: $389.02
45. Video Ad - Weekend Audience - Newsletter Signup Campaign: $385.41
46. Video Ad - Weekend Audience - Mobile Game Installs: $381.80
47. Image Ad - Evening Audience - Mobile Game Installs: $376.46
48. Video Ad - Morning Audience - Brand Awareness: $374.96
49. Video Ad - Evening Audience - Black Friday Deals: $374.58
50. Image Ad - Morning Audience - Blog Content Promotion: $374.44

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
  "top_n": 50,
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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'all ads with spend above 200 dollars'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'spend', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'spend', 'operator': '>', 'value': 200}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'all ads with spend above 200 dollars', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1577ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='ad', breakdown='ad', derived=None, need_timeseries=True, need_previous=False, base_measures=['spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'spend', 'operator': '>', 'value': 200}]}, top_n=50, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='spend', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=50, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'spend', 'operator': '>', 'value': 200}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='all ads with spend above 200 dollars', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 56868.16
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=56868.16, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 56868.16
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for spend by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 50, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=56868.16 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 9386.67}, {'date': '2025-10-24', 'value': 9457.54}, {'date': '2025-10-25', 'value': 8887.48}, {'date': '2025-10-26', 'value': 9661.06}, {'date': '2025-10-27', 'value': 10008.96}, {'date': '2025-10-28', 'value': 9466.45}] breakdown=[{'label': 'Video Ad - Morning Audience - Website Traffic Push', 'value': 689.61, 'spend': 689.61, 'clicks': 1782, 'conversions': 84.83, 'revenue': 4631.65, 'impressions': 46764}, {'label': 'Image Ad - Evening Audience - App Install Campaign', 'value': 586.66, 'spend': 586.66, 'clicks': 1330, 'conversions': 141.0, 'revenue': 391.92, 'impressions': 38448}, {'label': 'Image Ad - Weekend Audience - Website Traffic Push', 'value': 573.18, 'spend': 573.18, 'clicks': 1451, 'conversions': 81.4, 'revenue': 3789.59, 'impressions': 42313}, {'label': 'Carousel Ad - Morning Audience - App Install Campaign', 'value': 571.36, 'spend': 571.36, 'clicks': 1273, 'conversions': 126.0, 'revenue': 245.69, 'impressions': 41938}, {'label': 'Video Ad - Evening Audience - Lead Gen - B2B', 'value': 545.66, 'spend': 545.66, 'clicks': 1173, 'conversions': 197.88, 'revenue': 1276.04, 'impressions': 39594}, {'label': 'Carousel Ad - Weekend Audience - Summer Sale Campaign', 'value': 544.26, 'spend': 544.26, 'clicks': 1131, 'conversions': 52.0, 'revenue': 7405.87, 'impressions': 37339}, {'label': 'Image Ad - Weekend Audience - Brand Awareness', 'value': 534.78, 'spend': 534.78, 'clicks': 1040, 'conversions': 14.6, 'revenue': 501.66, 'impressions': 40017}, {'label': 'Carousel Ad - Weekend Audience - App Install Campaign', 'value': 532.46, 'spend': 532.46, 'clicks': 1580, 'conversions': 124.0, 'revenue': 218.05, 'impressions': 39161}, {'label': 'Video Ad - Weekend Audience - Lead Gen - B2B', 'value': 511.46, 'spend': 511.46, 'clicks': 1503, 'conversions': 304.74, 'revenue': 1359.4, 'impressions': 35156}, {'label': 'Carousel Ad - Evening Audience - Summer Sale Campaign', 'value': 510.73, 'spend': 510.73, 'clicks': 1729, 'conversions': 88.0, 'revenue': 12486.06, 'impressions': 37836}, {'label': 'Carousel Ad - Weekend Audience - Mobile Game Installs', 'value': 503.51, 'spend': 503.51, 'clicks': 802, 'conversions': 69.0, 'revenue': 110.94, 'impressions': 32820}, {'label': 'Video Ad - Morning Audience - App Install Campaign', 'value': 503.28, 'spend': 503.28, 'clicks': 1193, 'conversions': 140.0, 'revenue': 380.66, 'impressions': 32770}, {'label': 'Image Ad - Morning Audience - Lead Gen - B2B', 'value': 492.6, 'spend': 492.6, 'clicks': 1250, 'conversions': 203.54, 'revenue': 1360.93, 'impressions': 35883}, {'label': 'Image Ad - Morning Audience - Summer Sale Campaign', 'value': 483.96, 'spend': 483.96, 'clicks': 1240, 'conversions': 87.0, 'revenue': 10552.61, 'impressions': 33268}, {'label': 'Video Ad - Weekend Audience - App Install Campaign', 'value': 483.79, 'spend': 483.79, 'clicks': 1094, 'conversions': 109.0, 'revenue': 332.42, 'impressions': 36113}, {'label': 'Video Ad - Weekend Audience - Holiday Sale - Purchases', 'value': 483.66, 'spend': 483.66, 'clicks': 1043, 'conversions': 59.0, 'revenue': 9423.45, 'impressions': 48408}, {'label': 'Image Ad - Morning Audience - App Install Campaign', 'value': 478.22, 'spend': 478.22, 'clicks': 1057, 'conversions': 136.0, 'revenue': 184.59, 'impressions': 34390}, {'label': 'Carousel Ad - Evening Audience - Lead Gen - B2B', 'value': 475.85, 'spend': 475.85, 'clicks': 869, 'conversions': 175.68, 'revenue': 478.6, 'impressions': 30798}, {'label': 'Image Ad - Weekend Audience - App Install Campaign', 'value': 471.86, 'spend': 471.86, 'clicks': 1211, 'conversions': 131.0, 'revenue': 372.51, 'impressions': 33964}, {'label': 'Video Ad - Morning Audience - Lead Gen - B2B', 'value': 469.25, 'spend': 469.25, 'clicks': 1100, 'conversions': 186.41, 'revenue': 1227.84, 'impressions': 30115}, {'label': 'Carousel Ad - Morning Audience - Summer Sale Campaign', 'value': 468.25, 'spend': 468.25, 'clicks': 1092, 'conversions': 41.0, 'revenue': 4663.84, 'impressions': 32285}, {'label': 'Image Ad - Morning Audience - Website Traffic Push', 'value': 468.0, 'spend': 468.0, 'clicks': 1468, 'conversions': 83.75, 'revenue': 5393.26, 'impressions': 37803}, {'label': 'Carousel Ad - Weekend Audience - Brand Awareness', 'value': 466.45, 'spend': 466.45, 'clicks': 947, 'conversions': 10.19, 'revenue': 269.76, 'impressions': 42121}, {'label': 'Carousel Ad - Evening Audience - Mobile Game Installs', 'value': 466.27, 'spend': 466.27, 'clicks': 709, 'conversions': 77.0, 'revenue': 152.56, 'impressions': 35058}, {'label': 'Carousel Ad - Morning Audience - Website Traffic Push', 'value': 464.04, 'spend': 464.04, 'clicks': 1456, 'conversions': 82.51, 'revenue': 4808.89, 'impressions': 41749}, {'label': 'Video Ad - Weekend Audience - Website Traffic Push', 'value': 459.64, 'spend': 459.64, 'clicks': 1331, 'conversions': 63.91, 'revenue': 3825.6, 'impressions': 36452}, {'label': 'Carousel Ad - Evening Audience - Website Traffic Push', 'value': 458.87, 'spend': 458.87, 'clicks': 1329, 'conversions': 69.91, 'revenue': 4215.67, 'impressions': 34908}, {'label': 'Carousel Ad - Weekend Audience - Lead Gen - B2B', 'value': 456.21, 'spend': 456.21, 'clicks': 1096, 'conversions': 163.73, 'revenue': 673.9, 'impressions': 29800}, {'label': 'Image Ad - Evening Audience - Summer Sale Campaign', 'value': 455.14, 'spend': 455.14, 'clicks': 1304, 'conversions': 62.0, 'revenue': 7299.74, 'impressions': 36529}, {'label': 'Video Ad - Weekend Audience - Summer Sale Campaign', 'value': 454.83, 'spend': 454.83, 'clicks': 1142, 'conversions': 74.0, 'revenue': 9024.82, 'impressions': 36243}, {'label': 'Image Ad - Weekend Audience - Lead Gen - B2B', 'value': 441.45, 'spend': 441.45, 'clicks': 1051, 'conversions': 225.43, 'revenue': 842.95, 'impressions': 26954}, {'label': 'Image Ad - Evening Audience - Website Traffic Push', 'value': 440.58, 'spend': 440.58, 'clicks': 870, 'conversions': 64.28, 'revenue': 2861.27, 'impressions': 29785}, {'label': 'Image Ad - Weekend Audience - Newsletter Signup Campaign', 'value': 423.27, 'spend': 423.27, 'clicks': 697, 'conversions': 110.14, 'revenue': 370.86, 'impressions': 37403}, {'label': 'Video Ad - Morning Audience - Mobile Game Installs', 'value': 422.69, 'spend': 422.69, 'clicks': 813, 'conversions': 86.0, 'revenue': 292.99, 'impressions': 33463}, {'label': 'Video Ad - Evening Audience - Brand Awareness', 'value': 421.79, 'spend': 421.79, 'clicks': 683, 'conversions': 20.35, 'revenue': 700.88, 'impressions': 29721}, {'label': 'Carousel Ad - Morning Audience - Mobile Game Installs', 'value': 417.72, 'spend': 417.72, 'clicks': 780, 'conversions': 81.0, 'revenue': 231.56, 'impressions': 32359}, {'label': 'Image Ad - Weekend Audience - Holiday Sale - Purchases', 'value': 415.12, 'spend': 415.12, 'clicks': 817, 'conversions': 46.0, 'revenue': 5862.58, 'impressions': 38735}, {'label': 'Carousel Ad - Morning Audience - Brand Awareness', 'value': 408.52, 'spend': 408.52, 'clicks': 1054, 'conversions': 13.11, 'revenue': 416.09, 'impressions': 38153}, {'label': 'Video Ad - Morning Audience - Holiday Sale - Purchases', 'value': 405.75, 'spend': 405.75, 'clicks': 579, 'conversions': 24.0, 'revenue': 3424.54, 'impressions': 34408}, {'label': 'Image Ad - Morning Audience - Brand Awareness', 'value': 403.35, 'spend': 403.35, 'clicks': 688, 'conversions': 14.55, 'revenue': 499.07, 'impressions': 35473}, {'label': 'Image Ad - Morning Audience - Mobile Game Installs', 'value': 391.0, 'spend': 391.0, 'clicks': 815, 'conversions': 74.0, 'revenue': 247.13, 'impressions': 31341}, {'label': 'Video Ad - Evening Audience - Newsletter Signup Campaign', 'value': 389.17, 'spend': 389.17, 'clicks': 719, 'conversions': 149.07, 'revenue': 782.38, 'impressions': 33738}, {'label': 'Carousel Ad - Evening Audience - Brand Awareness', 'value': 389.09, 'spend': 389.09, 'clicks': 761, 'conversions': 15.88, 'revenue': 503.46, 'impressions': 32945}, {'label': 'Image Ad - Evening Audience - Brand Awareness', 'value': 389.02, 'spend': 389.02, 'clicks': 684, 'conversions': 16.92, 'revenue': 537.58, 'impressions': 31109}, {'label': 'Video Ad - Weekend Audience - Newsletter Signup Campaign', 'value': 385.41, 'spend': 385.41, 'clicks': 653, 'conversions': 103.64, 'revenue': 667.42, 'impressions': 31594}, {'label': 'Video Ad - Weekend Audience - Mobile Game Installs', 'value': 381.8, 'spend': 381.8, 'clicks': 611, 'conversions': 75.0, 'revenue': 267.69, 'impressions': 34003}, {'label': 'Image Ad - Evening Audience - Mobile Game Installs', 'value': 376.46, 'spend': 376.46, 'clicks': 700, 'conversions': 72.0, 'revenue': 96.3, 'impressions': 26769}, {'label': 'Video Ad - Morning Audience - Brand Awareness', 'value': 374.96, 'spend': 374.96, 'clicks': 760, 'conversions': 15.38, 'revenue': 479.91, 'impressions': 33203}, {'label': 'Video Ad - Evening Audience - Black Friday Deals', 'value': 374.58, 'spend': 374.58, 'clicks': 829, 'conversions': 41.0, 'revenue': 4796.53, 'impressions': 35706}, {'label': 'Image Ad - Morning Audience - Blog Content Promotion', 'value': 374.44, 'spend': 374.44, 'clicks': 735, 'conversions': 79.79, 'revenue': 4305.65, 'impressions': 37195}] workspace_avg=56868.16
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are the ads last week with SPEND above $200.00:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1820ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are the ads last week with SPEND above $200.00:
```

---

## Test 81: which campaign has the lowest cost per acquisition?

**Answer**:
> The Newsletter Signup Campaign had the lowest CPA at $2.41 last week—your best performer! For context, your overall CPA was $5.31, so this campaign is really leading the pack.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'which campaign has the lowest cost per acquisition?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpa', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'asc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'which campaign has the lowest cost per acquisition?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1258ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived='cpa', need_timeseries=True, need_previous=False, base_measures=['conversions', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='asc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpa', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='asc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='which campaign has the lowest cost per acquisition?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpa']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpa
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpa: 5.314210154983342911743130411
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpa': MetricValue(value=Decimal('5.314210154983342911743130411'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 5.314210154983342911743130411
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpa by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: asc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=5.314210154983343 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 5.403955094991365}, {'date': '2025-10-24', 'value': 5.03652698118533}, {'date': '2025-10-25', 'value': 4.962549765203165}, {'date': '2025-10-26', 'value': 5.654007994334908}, {'date': '2025-10-27', 'value': 5.345895624028586}, {'date': '2025-10-28', 'value': 5.52150227183911}] breakdown=[{'label': 'Newsletter Signup Campaign', 'value': 2.411958536417931, 'spend': 351.35, 'clicks': 775, 'conversions': 145.67, 'revenue': 701.78, 'impressions': 35596}] workspace_avg=5.314210154983343
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Newsletter Signup Campaign had the lowest CPA at $2.41 last week—your best performer! For context, your overall CPA was $5.31, so this campaign is really leading the pack.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1505ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3004ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Newsletter Signup Campaign had the lowest CPA at $2.41 last week—your best performer! For context, your overall CPA was $5.31, so this campaign is really leading the pack.'
```

---

## Test 82: show me adsets with impressions over 5000

**Answer**:
> Here are the adsets last week with IMPRESSIONS above 5,000:

1. Morning Audience - Lead Gen - B2B: 38,899
2. Weekend Audience - Website Traffic Push: 38,084
3. Weekend Audience - Brand Awareness: 40,474
4. Weekend Audience - App Install Campaign: 34,584
5. Morning Audience - Mobile Game Installs: 44,326
6. Morning Audience - App Install Campaign: 31,968
7. Morning Audience - Brand Awareness: 38,937
8. Morning Audience - Summer Sale Campaign: 35,487
9. Evening Audience - Lead Gen - B2B: 34,235
10. Morning Audience - Website Traffic Push: 33,941
11. Evening Audience - Summer Sale Campaign: 37,178
12. Weekend Audience - Black Friday Deals: 40,871
13. Evening Audience - Website Traffic Push: 34,967
14. Evening Audience - Black Friday Deals: 33,922
15. Evening Audience - App Install Campaign: 26,529
16. Weekend Audience - Mobile Game Installs: 33,277
17. Evening Audience - Newsletter Signup Campaign: 38,324
18. Morning Audience - Holiday Sale - Purchases: 32,664
19. Weekend Audience - Lead Gen - B2B: 25,979
20. Morning Audience - Product Launch Teaser: 39,196
21. Weekend Audience - Newsletter Signup Campaign: 29,368
22. Evening Audience - Brand Awareness: 31,668
23. Morning Audience - Blog Content Promotion: 37,208
24. Weekend Audience - Product Launch Teaser: 34,288
25. Evening Audience - General Conversions: 29,880
26. Weekend Audience - Summer Sale Campaign: 19,665
27. Morning Audience - General Conversions: 28,404
28. Morning Audience - Black Friday Deals: 29,856
29. Morning Audience - Newsletter Signup Campaign: 30,508
30. Evening Audience - Product Launch Teaser: 28,737
31. Evening Audience - Holiday Sale - Purchases: 29,313
32. Evening Audience - Blog Content Promotion: 32,480
33. Evening Audience - Mobile Game Installs: 23,397
34. Weekend Audience - Holiday Sale - Purchases: 25,157
35. Weekend Audience - General Conversions: 32,024

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
  "top_n": 50,
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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'show me adsets with impressions over 5000'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'impressions', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'impressions', 'operator': '>', 'value': 5000}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'show me adsets with impressions over 5000', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1457ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='adset', breakdown='adset', derived=None, need_timeseries=True, need_previous=False, base_measures=['impressions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'impressions', 'operator': '>', 'value': 5000}]}, top_n=50, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='impressions', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=50, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'impressions', 'operator': '>', 'value': 5000}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='show me adsets with impressions over 5000', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['impressions']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for impressions
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for impressions: 4953838.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'impressions': MetricValue(value=4953838.0, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 4953838.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for impressions by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 50, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=4953838.0 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 831689.0}, {'date': '2025-10-24', 'value': 845514.0}, {'date': '2025-10-25', 'value': 800607.0}, {'date': '2025-10-26', 'value': 830900.0}, {'date': '2025-10-27', 'value': 850347.0}, {'date': '2025-10-28', 'value': 794781.0}] breakdown=[{'label': 'Morning Audience - Lead Gen - B2B', 'value': 38899.0, 'spend': 604.63, 'clicks': 1678, 'conversions': 360.73, 'revenue': 2502.48, 'impressions': 38899}, {'label': 'Weekend Audience - Website Traffic Push', 'value': 38084.0, 'spend': 555.51, 'clicks': 1280, 'conversions': 62.88, 'revenue': 3610.43, 'impressions': 38084}, {'label': 'Weekend Audience - Brand Awareness', 'value': 40474.0, 'spend': 543.6, 'clicks': 1001, 'conversions': 11.54, 'revenue': 382.48, 'impressions': 40474}, {'label': 'Weekend Audience - App Install Campaign', 'value': 34584.0, 'spend': 536.41, 'clicks': 1097, 'conversions': 93.0, 'revenue': 195.43, 'impressions': 34584}, {'label': 'Morning Audience - Mobile Game Installs', 'value': 44326.0, 'spend': 532.73, 'clicks': 1258, 'conversions': 116.0, 'revenue': 362.06, 'impressions': 44326}, {'label': 'Morning Audience - App Install Campaign', 'value': 31968.0, 'spend': 500.73, 'clicks': 982, 'conversions': 101.0, 'revenue': 276.83, 'impressions': 31968}, {'label': 'Morning Audience - Brand Awareness', 'value': 38937.0, 'spend': 495.25, 'clicks': 920, 'conversions': 14.99, 'revenue': 591.74, 'impressions': 38937}, {'label': 'Morning Audience - Summer Sale Campaign', 'value': 35487.0, 'spend': 462.05, 'clicks': 1353, 'conversions': 67.0, 'revenue': 9777.93, 'impressions': 35487}, {'label': 'Evening Audience - Lead Gen - B2B', 'value': 34235.0, 'spend': 456.26, 'clicks': 1114, 'conversions': 228.66, 'revenue': 1404.63, 'impressions': 34235}, {'label': 'Morning Audience - Website Traffic Push', 'value': 33941.0, 'spend': 448.79, 'clicks': 1134, 'conversions': 90.6, 'revenue': 4077.99, 'impressions': 33941}, {'label': 'Evening Audience - Summer Sale Campaign', 'value': 37178.0, 'spend': 434.67, 'clicks': 1153, 'conversions': 67.0, 'revenue': 6585.33, 'impressions': 37178}, {'label': 'Weekend Audience - Black Friday Deals', 'value': 40871.0, 'spend': 431.25, 'clicks': 606, 'conversions': 24.0, 'revenue': 3317.55, 'impressions': 40871}, {'label': 'Evening Audience - Website Traffic Push', 'value': 34967.0, 'spend': 427.26, 'clicks': 1010, 'conversions': 71.46, 'revenue': 4063.25, 'impressions': 34967}, {'label': 'Evening Audience - Black Friday Deals', 'value': 33922.0, 'spend': 405.16, 'clicks': 703, 'conversions': 39.0, 'revenue': 3281.19, 'impressions': 33922}, {'label': 'Evening Audience - App Install Campaign', 'value': 26529.0, 'spend': 395.72, 'clicks': 891, 'conversions': 91.0, 'revenue': 318.76, 'impressions': 26529}, {'label': 'Weekend Audience - Mobile Game Installs', 'value': 33277.0, 'spend': 376.13, 'clicks': 928, 'conversions': 76.0, 'revenue': 137.79, 'impressions': 33277}, {'label': 'Evening Audience - Newsletter Signup Campaign', 'value': 38324.0, 'spend': 370.48, 'clicks': 601, 'conversions': 104.45, 'revenue': 559.62, 'impressions': 38324}, {'label': 'Morning Audience - Holiday Sale - Purchases', 'value': 32664.0, 'spend': 364.16, 'clicks': 595, 'conversions': 32.0, 'revenue': 4452.07, 'impressions': 32664}, {'label': 'Weekend Audience - Lead Gen - B2B', 'value': 25979.0, 'spend': 363.8, 'clicks': 997, 'conversions': 195.86, 'revenue': 952.37, 'impressions': 25979}, {'label': 'Morning Audience - Product Launch Teaser', 'value': 39196.0, 'spend': 334.32, 'clicks': 672, 'conversions': 16.54, 'revenue': 539.54, 'impressions': 39196}, {'label': 'Weekend Audience - Newsletter Signup Campaign', 'value': 29368.0, 'spend': 330.67, 'clicks': 667, 'conversions': 118.89, 'revenue': 629.32, 'impressions': 29368}, {'label': 'Evening Audience - Brand Awareness', 'value': 31668.0, 'spend': 327.11, 'clicks': 808, 'conversions': 13.28, 'revenue': 424.92, 'impressions': 31668}, {'label': 'Morning Audience - Blog Content Promotion', 'value': 37208.0, 'spend': 317.69, 'clicks': 705, 'conversions': 71.31, 'revenue': 4015.31, 'impressions': 37208}, {'label': 'Weekend Audience - Product Launch Teaser', 'value': 34288.0, 'spend': 304.27, 'clicks': 594, 'conversions': 19.06, 'revenue': 693.97, 'impressions': 34288}, {'label': 'Evening Audience - General Conversions', 'value': 29880.0, 'spend': 302.25, 'clicks': 436, 'conversions': 39.07, 'revenue': 3053.46, 'impressions': 29880}, {'label': 'Weekend Audience - Summer Sale Campaign', 'value': 19665.0, 'spend': 297.89, 'clicks': 633, 'conversions': 25.0, 'revenue': 3863.23, 'impressions': 19665}, {'label': 'Morning Audience - General Conversions', 'value': 28404.0, 'spend': 296.8, 'clicks': 423, 'conversions': 42.2, 'revenue': 3201.24, 'impressions': 28404}, {'label': 'Morning Audience - Black Friday Deals', 'value': 29856.0, 'spend': 288.67, 'clicks': 529, 'conversions': 23.0, 'revenue': 3379.71, 'impressions': 29856}, {'label': 'Morning Audience - Newsletter Signup Campaign', 'value': 30508.0, 'spend': 280.12, 'clicks': 575, 'conversions': 96.57, 'revenue': 486.33, 'impressions': 30508}, {'label': 'Evening Audience - Product Launch Teaser', 'value': 28737.0, 'spend': 259.8, 'clicks': 467, 'conversions': 16.27, 'revenue': 584.17, 'impressions': 28737}, {'label': 'Evening Audience - Holiday Sale - Purchases', 'value': 29313.0, 'spend': 253.68, 'clicks': 535, 'conversions': 25.0, 'revenue': 3022.92, 'impressions': 29313}, {'label': 'Evening Audience - Blog Content Promotion', 'value': 32480.0, 'spend': 251.68, 'clicks': 644, 'conversions': 67.24, 'revenue': 3643.6, 'impressions': 32480}, {'label': 'Evening Audience - Mobile Game Installs', 'value': 23397.0, 'spend': 231.56, 'clicks': 710, 'conversions': 67.0, 'revenue': 155.47, 'impressions': 23397}, {'label': 'Weekend Audience - Holiday Sale - Purchases', 'value': 25157.0, 'spend': 219.13, 'clicks': 514, 'conversions': 27.0, 'revenue': 2944.01, 'impressions': 25157}, {'label': 'Weekend Audience - General Conversions', 'value': 32024.0, 'spend': 204.68, 'clicks': 572, 'conversions': 44.74, 'revenue': 3343.95, 'impressions': 32024}] workspace_avg=4953838.0
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are the adsets last week with IMPRESSIONS above 5,000:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1699ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are the adsets last week with IMPRESSIONS above 5,000:
```

---

## Test 83: How is the Summer Sale campaign performing?

**Answer**:
> The Summer Sale campaign had a ROAS of 17.16× last week, which is excellent! It's way above your workspace average of 6.51×, so it's really performing well.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'How is the Summer Sale campaign performing?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': 'campaign', 'entity_ids': None, 'status': None, 'entity_name': 'Summer Sale', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How is the Summer Sale campaign performing?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 2254ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived='roas', need_timeseries=False, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': 'campaign', 'entity_ids': None, 'status': None, 'entity_name': 'Summer Sale', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level='campaign', entity_ids=None, status=None, entity_name='Summer Sale', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How is the Summer Sale campaign performing?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=campaign, status=None, entity_name=Summer Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Summer Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Summer Sale Campaign (ID: d02a69cb-5368-488f-93ec-993c747a2299, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Summer Sale Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity d02a69cb-5368-488f-93ec-993c747a2299 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Summer Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('5066.1600'), 'revenue': Decimal('86933.5500'), 'clicks': 13501, 'impressions': 384040, 'conversions': Decimal('689.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 689, 'visitors': 12385, 'profit': Decimal('26986.1500')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('17.15965346534653465346534653'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.507078653503120199422664633
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=17.159653465346533 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=6.50707865350312
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Summer Sale campaign had a ROAS of 17.16× last week, which is excellent! It's way above your workspace average of 6.51×, so it's really performing well.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1721ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 4196ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Summer Sale campaign had a ROAS of 17.16× last week, which is excellent! It's way above your workspace average of 6.51×, so it's really performing well.'
```

---

## Test 84: Show me all lead gen campaigns

**Answer**:
> Here are your 1 campaigns:
1. Lead Gen - B2B

**DSL**:
```json
{
  "query_type": "entities",
  "metric": null,
  "time_range": null,
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 50,
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
  "timeframe_description": null,
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Show me all lead gen campaigns'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.ENTITIES: 'entities'>, 'metric': None, 'time_range': None, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': 'campaign', 'entity_ids': None, 'status': None, 'entity_name': 'lead gen', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Show me all lead gen campaigns', 'timeframe_description': None, 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 827ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: None
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: campaign
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'entities': [{'name': 'Lead Gen - B2B', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}]}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your 1 campaigns:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 992ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your 1 campaigns:
```

---

## Test 85: What's the CPA for Morning Audience adsets?

**Answer**:
> The CPA for Morning Audience adsets was $11.27 last week.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'What's the CPA for Morning Audience adsets?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpa', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': 'adset', 'entity_ids': None, 'status': None, 'entity_name': 'Morning Audience', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's the CPA for Morning Audience adsets?", 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1584ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived='cpa', need_timeseries=False, need_previous=False, base_measures=['conversions', 'spend'], filters={'provider': None, 'level': 'adset', 'entity_ids': None, 'status': None, 'entity_name': 'Morning Audience', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpa', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level='adset', entity_ids=None, status=None, entity_name='Morning Audience', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's the CPA for Morning Audience adsets?", timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpa']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=adset, status=None, entity_name=Morning Audience
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Morning Audience'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Morning Audience - Holiday Sale - Purchases (ID: 2097b889-0ce5-4e1c-854d-b6099229bd5c, Level: LevelEnum.adset)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using adset hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 4 descendants for Morning Audience - Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 2097b889-0ce5-4e1c-854d-b6099229bd5c from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 3 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Morning Audience': 3 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('1082.3100'), 'revenue': Decimal('13706.8900'), 'clicks': 1879, 'impressions': 97527, 'conversions': Decimal('96.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 96, 'visitors': 1720, 'profit': Decimal('3916.8400')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpa
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpa: 5.314210154983342911743130411
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpa': MetricValue(value=Decimal('11.2740625'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 5.314210154983342911743130411
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=11.2740625 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=5.314210154983343
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The CPA for Morning Audience adsets was $11.27 last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 837ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2644ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The CPA for Morning Audience adsets was $11.27 last week.'
```

---

## Test 86: What's the revenue for Black Friday campaign?

**Answer**:
> The revenue for the Black Friday campaign was $44,458.23 last week.

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
    "entity_name": "Black Friday",
    "metric_filters": null
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's the revenue for Black Friday campaign?",
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'What's the revenue for Black Friday campaign?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Black Friday', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's the revenue for Black Friday campaign?", 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 5192ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Black Friday', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Black Friday', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's the revenue for Black Friday campaign?", timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Black Friday
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Black Friday'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Black Friday Deals (ID: a15bf796-74ca-4556-91f6-00d91bb89cea, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Black Friday Deals
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity a15bf796-74ca-4556-91f6-00d91bb89cea from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Black Friday': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('3850.5000'), 'revenue': Decimal('44458.2300'), 'clicks': 7329, 'impressions': 373438, 'conversions': Decimal('353.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 353, 'visitors': 6704, 'profit': Decimal('13309.9800')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 370045.59
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=44458.23, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 370045.59
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=44458.23 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=370045.59
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The revenue for the Black Friday campaign was $44,458.23 last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 974ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 6378ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The revenue for the Black Friday campaign was $44,458.23 last week.'
```

---

## Test 87: Give me ROAS for App Install campaigns

**Answer**:
> Here's a breakdown of the Return on Ad Spend (ROAS) for your App Install campaigns from last week:

1. **Evening Audience - App Install Campaign**: This segment achieved a ROAS of 0.66. With a spend of $1,709.92, it generated $1,131.56 in revenue from 456 conversions.

2. **Weekend Audience - App Install Campaign**: The ROAS here was 0.55. The campaign spent $2,024.52 and brought in $1,118.41 in revenue with 457 conversions.

3. **Morning Audience - App Install Campaign**: This audience had a ROAS of 0.53. It involved a spend of $2,053.59, resulting in $1,087.77 in revenue from 503 conversions.

In total, we looked at three different audience segments for your App Install campaigns.

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
    "entity_name": "App Install",
    "metric_filters": null
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Give me ROAS for App Install campaigns",
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Give me ROAS for App Install campaigns'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'App Install', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Give me ROAS for App Install campaigns', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1401ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'App Install', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='App Install', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Give me ROAS for App Install campaigns', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=App Install
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('5788.0300'), 'revenue': Decimal('3337.7400'), 'clicks': 13991, 'impressions': 409439, 'conversions': Decimal('1416.0000'), 'leads': Decimal('0'), 'installs': 1416, 'purchases': 0, 'visitors': 0, 'profit': Decimal('953.3000')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('0.5766625259371496001230124930'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for roas by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=App Install
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 5, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity by name (exact first): 'App Install'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using partial match for 'App Install': App Install Campaign (3d2aef8f-cbe3-407e-9166-689eff73bafd)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Routing named-entity same-level breakdown to child level: campaign→adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.5766625259371496 previous=None delta_pct=None timeseries=[{'date': '2025-10-23', 'value': 0.5285763656392423}, {'date': '2025-10-24', 'value': 0.7004389951459127}, {'date': '2025-10-25', 'value': 0.5166284466584009}, {'date': '2025-10-26', 'value': 0.469401159946894}, {'date': '2025-10-27', 'value': 0.5984178369505745}, {'date': '2025-10-28', 'value': 0.5984936049981491}] breakdown=[{'label': 'Evening Audience - App Install Campaign', 'value': 0.6617619537756152, 'spend': 1709.92, 'clicks': 4504, 'conversions': 456.0, 'revenue': 1131.56, 'impressions': 124551}, {'label': 'Weekend Audience - App Install Campaign', 'value': 0.5524321814553573, 'spend': 2024.52, 'clicks': 4982, 'conversions': 457.0, 'revenue': 1118.41, 'impressions': 143822}, {'label': 'Morning Audience - App Install Campaign', 'value': 0.5296919053949425, 'spend': 2053.59, 'clicks': 4505, 'conversions': 503.0, 'revenue': 1087.77, 'impressions': 141066}] workspace_avg=6.50707865350312
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here's a breakdown of the Return on Ad Spend (ROAS) for your App Install campaigns from last week:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 7596ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 9447ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here's a breakdown of the Return on Ad Spend (ROAS) for your App Install campaigns from last week:
```

---

## Test 88: Show me Weekend Audience adsets

**Answer**:
> Here are your 11 adsets:
1. Weekend Audience - App Install Campaign
2. Weekend Audience - Black Friday Deals
3. Weekend Audience - Brand Awareness
4. Weekend Audience - General Conversions
5. Weekend Audience - Holiday Sale - Purchases
6. Weekend Audience - Lead Gen - B2B
7. Weekend Audience - Mobile Game Installs
8. Weekend Audience - Newsletter Signup Campaign
9. Weekend Audience - Product Launch Teaser
10. Weekend Audience - Summer Sale Campaign
11. Weekend Audience - Website Traffic Push

**DSL**:
```json
{
  "query_type": "entities",
  "metric": null,
  "time_range": null,
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 50,
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
  "timeframe_description": null,
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Show me Weekend Audience adsets'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.ENTITIES: 'entities'>, 'metric': None, 'time_range': None, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': 'adset', 'entity_ids': None, 'status': None, 'entity_name': 'Weekend Audience', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Show me Weekend Audience adsets', 'timeframe_description': None, 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 2018ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: None
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: adset
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'entities': [{'name': 'Weekend Audience - App Install Campaign', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}, {'name': 'Weekend Audience - Black Friday Deals', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}, {'name': 'Weekend Audience - Brand Awareness', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}, {'name': 'Weekend Audience - General Conversions', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}, {'name': 'Weekend Audience - Holiday Sale - Purchases', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}, {'name': 'Weekend Audience - Lead Gen - B2B', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}, {'name': 'Weekend Audience - Mobile Game Installs', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}, {'name': 'Weekend Audience - Newsletter Signup Campaign', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}, {'name': 'Weekend Audience - Product Launch Teaser', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}, {'name': 'Weekend Audience - Summer Sale Campaign', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}, {'name': 'Weekend Audience - Website Traffic Push', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}]}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your 11 adsets:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2141ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your 11 adsets:
```

---

## Test 89: What's the CTR for Evening Audience adsets?

**Answer**:
> The CTR for Evening Audience adsets was 2.1% last week.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'What's the CTR for Evening Audience adsets?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'ctr', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': 'adset', 'entity_ids': None, 'status': None, 'entity_name': 'Evening Audience', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's the CTR for Evening Audience adsets?", 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1368ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived='ctr', need_timeseries=False, need_previous=False, base_measures=['clicks', 'impressions'], filters={'provider': None, 'level': 'adset', 'entity_ids': None, 'status': None, 'entity_name': 'Evening Audience', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='ctr', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level='adset', entity_ids=None, status=None, entity_name='Evening Audience', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's the CTR for Evening Audience adsets?", timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['ctr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=adset, status=None, entity_name=Evening Audience
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Evening Audience'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Evening Audience - Holiday Sale - Purchases (ID: a7408419-eb16-4c3b-80ec-d7cf998782c5, Level: LevelEnum.adset)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using adset hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 4 descendants for Evening Audience - Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity a7408419-eb16-4c3b-80ec-d7cf998782c5 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 3 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Evening Audience': 3 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('625.3900'), 'revenue': Decimal('9864.2900'), 'clicks': 1533, 'impressions': 71830, 'conversions': Decimal('66.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 66, 'visitors': 1401, 'profit': Decimal('2672.0900')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for ctr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for ctr: 0.02535125290734174
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'ctr': MetricValue(value=0.0213420576360852, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.02535125290734174
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.0213420576360852 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=0.02535125290734174
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The CTR for Evening Audience adsets was 2.1% last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 895ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2478ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The CTR for Evening Audience adsets was 2.1% last week.'
```

---

## Test 90: How much did Holiday Sale campaign spend last week?

**Answer**:
> The Holiday Sale campaign spent $3,754.56 last week.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'How much did Holiday Sale campaign spend last week?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'spend', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How much did Holiday Sale campaign spend last week?', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1128ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='spend', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Holiday Sale', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How much did Holiday Sale campaign spend last week?', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('3754.5600'), 'revenue': Decimal('51992.8900'), 'clicks': 7577, 'impressions': 372044, 'conversions': Decimal('371.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 371, 'visitors': 6935, 'profit': Decimal('15830.7500')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 56868.16
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=3754.56, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 56868.16
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=3754.56 previous=None delta_pct=None timeseries=None breakdown=None workspace_avg=56868.16
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Holiday Sale campaign spent $3,754.56 last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 767ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2092ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Holiday Sale campaign spent $3,754.56 last week.'
```

---

## Test 91: Compare CPC, CTR, and ROAS for Holiday Sale and App Install campaigns last week

**Answer**:
> Last week, when comparing the Holiday Sale and App Install campaigns, there were notable differences in their performance across key metrics: CPC, CTR, and ROAS.

For Cost Per Click (CPC), the App Install campaign was more cost-effective, with a CPC of $0.41 compared to the Holiday Sale's $0.50. This means the App Install campaign spent less per click.

In terms of Click-Through Rate (CTR), the App Install campaign also outperformed, achieving a CTR of 3.42%, which is significantly higher than the Holiday Sale's 2.04%. This indicates that the App Install ads were more engaging and effective at driving clicks.

However, when it comes to Return on Advertising Spend (ROAS), the Holiday Sale campaign was far superior, with a ROAS of 13.85 compared to the App Install's 0.58. This suggests that the Holiday Sale campaign generated much more revenue for each dollar spent on advertising.

Overall, while the App Install campaign had a lower CPC and higher CTR, the Holiday Sale campaign excelled in generating revenue, as reflected in its much higher ROAS.

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Compare CPC, CTR, and ROAS for Holiday Sale and App Install campaigns last week'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.COMPARISON: 'comparison'>, 'metric': None, 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': 'entity_vs_entity', 'comparison_entities': ['Holiday Sale', 'App Install'], 'comparison_metrics': ['cpc', 'ctr', 'roas'], 'question': 'Compare CPC, CTR, and ROAS for Holiday Sale and App Install campaigns last week', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1364ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['clicks', 'impressions', 'revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.COMPARISON: 'comparison'>, metric=None, time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type='entity_vs_entity', comparison_entities=['Holiday Sale', 'App Install'], comparison_metrics=['cpc', 'ctr', 'roas'], question='Compare CPC, CTR, and ROAS for Holiday Sale and App Install campaigns last week', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.dsl.executor:[COMPARISON] Executing comparison plan for type: entity_vs_entity
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['cpc', 'ctr', 'roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('3754.5600'), 'revenue': Decimal('51992.8900'), 'clicks': 7577, 'impressions': 372044, 'conversions': Decimal('371.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 371, 'visitors': 6935, 'profit': Decimal('15830.7500')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4528224483620785756374118134
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.4955206546126435264616602877'), previous=None, delta_pct=None), 'ctr': MetricValue(value=0.020365870703465183, previous=None, delta_pct=None), 'roas': MetricValue(value=Decimal('13.84793158186312111139521009'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4528224483620785756374118134
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['cpc', 'ctr', 'roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=App Install
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('5788.0300'), 'revenue': Decimal('3337.7400'), 'clicks': 13991, 'impressions': 409439, 'conversions': Decimal('1416.0000'), 'leads': Decimal('0'), 'installs': 1416, 'purchases': 0, 'visitors': 0, 'profit': Decimal('953.3000')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4528224483620785756374118134
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.4136966621399471088556929455'), previous=None, delta_pct=None), 'ctr': MetricValue(value=0.034171146373452456, previous=None, delta_pct=None), 'roas': MetricValue(value=Decimal('0.5766625259371496001230124930'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4528224483620785756374118134
INFO:app.dsl.executor:[COMPARISON] Completed execution for 2 items
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'comparison': [{'entity': 'Holiday Sale', 'cpc': Decimal('0.4955206546126435264616602877'), 'ctr': 0.020365870703465183, 'roas': Decimal('13.84793158186312111139521009')}, {'entity': 'App Install', 'cpc': Decimal('0.4136966621399471088556929455'), 'ctr': 0.034171146373452456, 'roas': Decimal('0.5766625259371496001230124930')}], 'comparison_type': 'entity_vs_entity', 'metrics': ['cpc', 'ctr', 'roas'], 'query_type': 'comparison'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Last week, when comparing the Holiday Sale and App Install campaigns, there were notable differences in their performance across key metrics: CPC, CTR, and ROAS.
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 5821ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 7495ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Last week, when comparing the Holiday Sale and App Install campaigns, there were notable differences in their performance across key metrics: CPC, CTR, and ROAS.
```

---

## Test 92: What's the spend, revenue, and ROAS for all Google campaigns in September?

**Answer**:
> Here are your metrics from 2025-09-01 to 2025-09-30:

• SPEND: $8,272.52
• REVENUE: $56,264.09
• ROAS: 6.80×

Top CAMPAIGN:
  - Summer Sale Campaign: $168.61
  - App Install Campaign: $148.91
  - Website Traffic Push: $98.83
  - Lead Gen - B2B: $94.87

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's the spend, revenue, and ROAS for all Google campaigns in September?",
  "timeframe_description": "from 2025-09-01 to 2025-09-30",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'What's the spend, revenue, and ROAS for all Google campaigns in September?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': ['spend', 'revenue', 'roas'], 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 9, 1), 'end': datetime.date(2025, 9, 30)}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': 'google', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's the spend, revenue, and ROAS for all Google campaigns in September?", 'timeframe_description': 'from 2025-09-01 to 2025-09-30', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1281ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 1), end=datetime.date(2025, 9, 30), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': 'google', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric=['spend', 'revenue', 'roas'], time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 9, 1), end=datetime.date(2025, 9, 30)), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=10, sort_order='desc', filters=Filters(provider='google', level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's the spend, revenue, and ROAS for all Google campaigns in September?", timeframe_description='from 2025-09-01 to 2025-09-30', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['spend', 'revenue', 'roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 1) end=datetime.date(2025, 9, 30)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=google, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-01 to 2025-09-30
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('8272.5200'), 'revenue': Decimal('56264.0900'), 'clicks': 19897, 'impressions': 562923, 'conversions': Decimal('1962.9600'), 'leads': Decimal('960.8700'), 'installs': 412, 'purchases': 247, 'visitors': 13870, 'profit': Decimal('17621.6500')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 19842.14
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=8272.52, previous=None, delta_pct=None), 'revenue': MetricValue(value=56264.09, previous=None, delta_pct=None), 'roas': MetricValue(value=Decimal('6.801324143066441664692258224'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 19842.14
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 3 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for spend by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 1) end=datetime.date(2025, 9, 30)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=google, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-01 to 2025-09-30
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'metrics': {'spend': {'summary': 8272.52, 'previous': None, 'delta_pct': None}, 'revenue': {'summary': 56264.09, 'previous': None, 'delta_pct': None}, 'roas': {'summary': Decimal('6.801324143066441664692258224'), 'previous': None, 'delta_pct': None}}, 'timeseries': [{'date': '2025-09-29', 'value': 4152.06}, {'date': '2025-09-30', 'value': 4120.46}], 'breakdown': [{'label': 'Summer Sale Campaign', 'value': 168.61, 'spend': Decimal('168.6100'), 'clicks': 292, 'conversions': Decimal('8.0000'), 'revenue': Decimal('1307.5200'), 'impressions': 9097}, {'label': 'App Install Campaign', 'value': 148.91, 'spend': Decimal('148.9100'), 'clicks': 485, 'conversions': Decimal('53.0000'), 'revenue': Decimal('78.6800'), 'impressions': 13052}, {'label': 'Website Traffic Push', 'value': 98.83, 'spend': Decimal('98.8300'), 'clicks': 202, 'conversions': Decimal('33.0200'), 'revenue': Decimal('1356.3000'), 'impressions': 6877}, {'label': 'Lead Gen - B2B', 'value': 94.87, 'spend': Decimal('94.8700'), 'clicks': 287, 'conversions': Decimal('42.5600'), 'revenue': Decimal('73.9600'), 'impressions': 6642}], 'query_type': 'multi_metrics'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your metrics from 2025-09-01 to 2025-09-30:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1511ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your metrics from 2025-09-01 to 2025-09-30:
```

---

## Test 93: Show me clicks, conversions, and cost per conversion for Meta campaigns last 5 days

**Answer**:
> I couldn't find any data for ['clicks', 'conversions', 'cpa'] in the last 5 days. You may want to try a different time period.

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
  "timeframe_description": "last 5 days",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Show me clicks, conversions, and cost per conversion for Meta campaigns last 5 days'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': ['clicks', 'conversions', 'cpa'], 'time_range': {'last_n_days': 5, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': 'meta', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Show me clicks, conversions, and cost per conversion for Meta campaigns last 5 days', 'timeframe_description': 'last 5 days', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1307ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 25), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['clicks', 'conversions', 'spend'], filters={'provider': 'meta', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric=['clicks', 'conversions', 'cpa'], time_range=TimeRange(last_n_days=5, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider='meta', level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Show me clicks, conversions, and cost per conversion for Meta campaigns last 5 days', timeframe_description='last 5 days', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['clicks', 'conversions', 'cpa']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 25) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=meta, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-25 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('10110.0700'), 'revenue': Decimal('105009.1200'), 'clicks': 20169, 'impressions': 995682, 'conversions': Decimal('1904.9400'), 'leads': Decimal('887.1000'), 'installs': 0, 'purchases': 555, 'visitors': 18309, 'profit': Decimal('31248.3200')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for clicks
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for clicks: 83903.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'clicks': MetricValue(value=20169.0, previous=None, delta_pct=None), 'conversions': MetricValue(value=1904.94, previous=None, delta_pct=None), 'cpa': MetricValue(value=Decimal('5.307290518336535533927577771'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 83903.0
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'metrics': {'clicks': {'summary': 20169.0, 'previous': None, 'delta_pct': None}, 'conversions': {'summary': 1904.94, 'previous': None, 'delta_pct': None}, 'cpa': {'summary': Decimal('5.307290518336535533927577771'), 'previous': None, 'delta_pct': None}}, 'timeseries': None, 'breakdown': None, 'query_type': 'multi_metrics'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'I couldn't find any data for ['clicks', 'conversions', 'cpa'] in the last 5 days. You may want to try a different time period.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1485ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'I couldn't find any data for ['clicks', 'conversions', 'cpa'] in the last 5 days. You may want to try a different time period.'
```

---

## Test 94: Give me CTR, CPC, and conversion rate for Summer Sale campaign last month

**Answer**:
> I couldn't find any data for ['ctr', 'cpc', 'cvr'] in the last 30 days. You may want to try a different time period.

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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "Give me CTR, CPC, and conversion rate for Summer Sale campaign last month",
  "timeframe_description": "last month",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Give me CTR, CPC, and conversion rate for Summer Sale campaign last month'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': ['ctr', 'cpc', 'cvr'], 'time_range': {'last_n_days': 30, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Summer Sale', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Give me CTR, CPC, and conversion rate for Summer Sale campaign last month', 'timeframe_description': 'last month', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1892ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 30), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['clicks', 'conversions', 'impressions', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Summer Sale', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric=['ctr', 'cpc', 'cvr'], time_range=TimeRange(last_n_days=30, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Summer Sale', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Give me CTR, CPC, and conversion rate for Summer Sale campaign last month', timeframe_description='last month', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['ctr', 'cpc', 'cvr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 30) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Summer Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-30 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Summer Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Summer Sale Campaign (ID: d02a69cb-5368-488f-93ec-993c747a2299, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Summer Sale Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity d02a69cb-5368-488f-93ec-993c747a2299 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Summer Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('25689.4400'), 'revenue': Decimal('399509.4600'), 'clicks': 63974, 'impressions': 1828195, 'conversions': Decimal('3196.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 3196, 'visitors': 58691, 'profit': Decimal('122480.0500')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for ctr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for ctr: 0.02539074677847104
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'ctr': MetricValue(value=0.0349929848839976, previous=None, delta_pct=None), 'cpc': MetricValue(value=Decimal('0.4015606340075655735142401601'), previous=None, delta_pct=None), 'cvr': MetricValue(value=Decimal('0.04995779535436270985087691875'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.02539074677847104
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'metrics': {'ctr': {'summary': 0.0349929848839976, 'previous': None, 'delta_pct': None}, 'cpc': {'summary': Decimal('0.4015606340075655735142401601'), 'previous': None, 'delta_pct': None}, 'cvr': {'summary': Decimal('0.04995779535436270985087691875'), 'previous': None, 'delta_pct': None}}, 'timeseries': None, 'breakdown': None, 'query_type': 'multi_metrics'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'I couldn't find any data for ['ctr', 'cpc', 'cvr'] in the last 30 days. You may want to try a different time period.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2109ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'I couldn't find any data for ['ctr', 'cpc', 'cvr'] in the last 30 days. You may want to try a different time period.'
```

---

## Test 95: Compare spend and revenue between Morning Audience and Evening Audience adsets this month to date

**Answer**:
> From October 1 to 29, let's take a look at how the Morning Audience and Evening Audience ad sets performed in terms of spend and revenue.

The Morning Audience ad set had a total spend of $4,255.33, generating a revenue of $47,319.80. On the other hand, the Evening Audience ad set spent slightly more at $4,882.90, but it also brought in higher revenue, totaling $55,810.28.

In terms of spend, the Morning Audience was more cost-effective, spending $627.57 less than the Evening Audience. However, when we look at revenue, the Evening Audience outperformed, bringing in $8,490.48 more than the Morning Audience.

Overall, while the Morning Audience was more economical in terms of spending, the Evening Audience delivered better revenue results, making it the stronger performer in terms of revenue generation.

**DSL**:
```json
{
  "query_type": "comparison",
  "metric": null,
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-29"
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
  "timeframe_description": "this month",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Compare spend and revenue between Morning Audience and Evening Audience adsets this month to date'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.COMPARISON: 'comparison'>, 'metric': None, 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 10, 1), 'end': datetime.date(2025, 10, 29)}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': 'entity_vs_entity', 'comparison_entities': ['Morning Audience', 'Evening Audience'], 'comparison_metrics': ['spend', 'revenue'], 'question': 'Compare spend and revenue between Morning Audience and Evening Audience adsets this month to date', 'timeframe_description': 'this month', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 2111ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.COMPARISON: 'comparison'>, metric=None, time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 29)), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type='entity_vs_entity', comparison_entities=['Morning Audience', 'Evening Audience'], comparison_metrics=['spend', 'revenue'], question='Compare spend and revenue between Morning Audience and Evening Audience adsets this month to date', timeframe_description='this month', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.dsl.executor:[COMPARISON] Executing comparison plan for type: entity_vs_entity
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 2 metrics: ['spend', 'revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Morning Audience
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Morning Audience'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Morning Audience - Holiday Sale - Purchases (ID: 2097b889-0ce5-4e1c-854d-b6099229bd5c, Level: LevelEnum.adset)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using adset hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 4 descendants for Morning Audience - Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 2097b889-0ce5-4e1c-854d-b6099229bd5c from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 3 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Morning Audience': 3 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('4255.3300'), 'revenue': Decimal('47319.8000'), 'clicks': 8065, 'impressions': 431457, 'conversions': Decimal('350.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 350, 'visitors': 7378, 'profit': Decimal('14200.0300')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 268552.71
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=4255.33, previous=None, delta_pct=None), 'revenue': MetricValue(value=47319.8, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 268552.71
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 2 metrics: ['spend', 'revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Evening Audience
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Evening Audience'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Evening Audience - Holiday Sale - Purchases (ID: a7408419-eb16-4c3b-80ec-d7cf998782c5, Level: LevelEnum.adset)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using adset hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 4 descendants for Evening Audience - Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity a7408419-eb16-4c3b-80ec-d7cf998782c5 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 3 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Evening Audience': 3 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('4882.9000'), 'revenue': Decimal('55810.2800'), 'clicks': 9465, 'impressions': 473002, 'conversions': Decimal('412.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 412, 'visitors': 8662, 'profit': Decimal('16698.5600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 268552.71
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=4882.9, previous=None, delta_pct=None), 'revenue': MetricValue(value=55810.28, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 268552.71
INFO:app.dsl.executor:[COMPARISON] Completed execution for 2 items
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'comparison': [{'entity': 'Morning Audience', 'spend': 4255.33, 'revenue': 47319.8}, {'entity': 'Evening Audience', 'spend': 4882.9, 'revenue': 55810.28}], 'comparison_type': 'entity_vs_entity', 'metrics': ['spend', 'revenue'], 'query_type': 'comparison'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'From October 1 to 29, let's take a look at how the Morning Audience and Evening Audience ad sets performed in terms of spend and revenue.
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 3547ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 5982ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'From October 1 to 29, let's take a look at how the Morning Audience and Evening Audience ad sets performed in terms of spend and revenue.
```

---

## Test 96: What's the ROAS, revenue, and profit for Black Friday campaign last week?

**Answer**:
> I couldn't find any data for ['roas', 'revenue', 'profit'] last week. You may want to try a different time period.

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
    "entity_name": "Black Friday",
    "metric_filters": null
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's the ROAS, revenue, and profit for Black Friday campaign last week?",
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'What's the ROAS, revenue, and profit for Black Friday campaign last week?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': ['roas', 'revenue', 'profit'], 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Black Friday', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's the ROAS, revenue, and profit for Black Friday campaign last week?", 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1399ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['profit', 'revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Black Friday', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric=['roas', 'revenue', 'profit'], time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Black Friday', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's the ROAS, revenue, and profit for Black Friday campaign last week?", timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['roas', 'revenue', 'profit']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Black Friday
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Black Friday'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Black Friday Deals (ID: a15bf796-74ca-4556-91f6-00d91bb89cea, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Black Friday Deals
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity a15bf796-74ca-4556-91f6-00d91bb89cea from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Black Friday': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('3850.5000'), 'revenue': Decimal('44458.2300'), 'clicks': 7329, 'impressions': 373438, 'conversions': Decimal('353.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 353, 'visitors': 6704, 'profit': Decimal('13309.9800')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.507078653503120199422664633
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('11.54609271523178807947019868'), previous=None, delta_pct=None), 'revenue': MetricValue(value=44458.23, previous=None, delta_pct=None), 'profit': MetricValue(value=13309.98, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.507078653503120199422664633
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'metrics': {'roas': {'summary': Decimal('11.54609271523178807947019868'), 'previous': None, 'delta_pct': None}, 'revenue': {'summary': 44458.23, 'previous': None, 'delta_pct': None}, 'profit': {'summary': 13309.98, 'previous': None, 'delta_pct': None}}, 'timeseries': None, 'breakdown': None, 'query_type': 'multi_metrics'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'I couldn't find any data for ['roas', 'revenue', 'profit'] last week. You may want to try a different time period.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1603ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'I couldn't find any data for ['roas', 'revenue', 'profit'] last week. You may want to try a different time period.'
```

---

## Test 97: Show me CPC, clicks, and spend for all active campaigns last 5 days

**Answer**:
> Here are your metrics in the last 5 days:

• CPC: $0.45
• CLICKS: 79,931
• SPEND: $36,060.60

Top CAMPAIGN:
  - Product Launch Teaser: $0.66
  - Lead Gen - B2B: $0.56
  - Mobile Game Installs: $0.55
  - General Conversions: $0.53
  - Holiday Sale - Purchases: $0.52

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
  "top_n": 50,
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
  "timeframe_description": "last 5 days",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Show me CPC, clicks, and spend for all active campaigns last 5 days'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': ['cpc', 'clicks', 'spend'], 'time_range': {'last_n_days': 5, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 50, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': 'active', 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Show me CPC, clicks, and spend for all active campaigns last 5 days', 'timeframe_description': 'last 5 days', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1275ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 25), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['clicks', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': 'active', 'entity_name': None, 'metric_filters': None}, top_n=50, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric=['cpc', 'clicks', 'spend'], time_range=TimeRange(last_n_days=5, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=50, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status='active', entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Show me CPC, clicks, and spend for all active campaigns last 5 days', timeframe_description='last 5 days', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['cpc', 'clicks', 'spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 25) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=active, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-25 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('36060.6000'), 'revenue': Decimal('231653.9000'), 'clicks': 79931, 'impressions': 3077791, 'conversions': Decimal('6623.5200'), 'leads': Decimal('2761.8000'), 'installs': 1553, 'purchases': 1058, 'visitors': 57189, 'profit': Decimal('69230.4500')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4531893972801926033634077447
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.4511466139545357871163878846'), previous=None, delta_pct=None), 'clicks': MetricValue(value=79931.0, previous=None, delta_pct=None), 'spend': MetricValue(value=36060.6, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4531893972801926033634077447
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 3 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpc by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 25) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=active, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 50, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-25 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'metrics': {'cpc': {'summary': Decimal('0.4511466139545357871163878846'), 'previous': None, 'delta_pct': None}, 'clicks': {'summary': 79931.0, 'previous': None, 'delta_pct': None}, 'spend': {'summary': 36060.6, 'previous': None, 'delta_pct': None}}, 'timeseries': [{'date': '2025-10-25', 'value': Decimal('0.4292217879080156353114371288')}, {'date': '2025-10-26', 'value': Decimal('0.4602913940613990941117262204')}, {'date': '2025-10-27', 'value': Decimal('0.4535267021736001151576219951')}, {'date': '2025-10-28', 'value': Decimal('0.4614220582961938425285589878')}], 'breakdown': [{'label': 'Product Launch Teaser', 'value': Decimal('0.6570404984423676012461059190'), 'spend': Decimal('210.9100'), 'clicks': 321, 'conversions': Decimal('9.9600'), 'revenue': Decimal('345.9100'), 'impressions': 23382}, {'label': 'Lead Gen - B2B', 'value': Decimal('0.5609725158562367864693446089'), 'spend': Decimal('530.6800'), 'clicks': 946, 'conversions': Decimal('167.7900'), 'revenue': Decimal('1029.9200'), 'impressions': 30072}, {'label': 'Mobile Game Installs', 'value': Decimal('0.5548208469055374592833876221'), 'spend': Decimal('170.3300'), 'clicks': 307, 'conversions': Decimal('27.0000'), 'revenue': Decimal('79.9900'), 'impressions': 12296}, {'label': 'General Conversions', 'value': Decimal('0.5257314148681055155875299760'), 'spend': Decimal('219.2300'), 'clicks': 417, 'conversions': Decimal('37.8200'), 'revenue': Decimal('2842.2400'), 'impressions': 19306}, {'label': 'Holiday Sale - Purchases', 'value': Decimal('0.5224698795180722891566265060'), 'spend': Decimal('173.4600'), 'clicks': 332, 'conversions': Decimal('14.0000'), 'revenue': Decimal('1397.7900'), 'impressions': 15000}, {'label': 'Black Friday Deals', 'value': Decimal('0.4948758465011286681715575621'), 'spend': Decimal('219.2300'), 'clicks': 443, 'conversions': Decimal('22.0000'), 'revenue': Decimal('3569.9300'), 'impressions': 20654}, {'label': 'Newsletter Signup Campaign', 'value': Decimal('0.4858457711442786069651741294'), 'spend': Decimal('195.3100'), 'clicks': 402, 'conversions': Decimal('64.7700'), 'revenue': Decimal('231.2600'), 'impressions': 18267}, {'label': 'Summer Sale Campaign', 'value': Decimal('0.4775171232876712328767123288'), 'spend': Decimal('278.8700'), 'clicks': 584, 'conversions': Decimal('28.0000'), 'revenue': Decimal('3853.8500'), 'impressions': 18458}, {'label': 'Brand Awareness', 'value': Decimal('0.4161845386533665835411471322'), 'spend': Decimal('166.8900'), 'clicks': 401, 'conversions': Decimal('9.3000'), 'revenue': Decimal('404.2200'), 'impressions': 16652}, {'label': 'App Install Campaign', 'value': Decimal('0.3812658227848101265822784810'), 'spend': Decimal('180.7200'), 'clicks': 474, 'conversions': Decimal('42.0000'), 'revenue': Decimal('106.3500'), 'impressions': 14624}, {'label': 'Website Traffic Push', 'value': Decimal('0.2642608695652173913043478261'), 'spend': Decimal('212.7300'), 'clicks': 805, 'conversions': Decimal('56.7500'), 'revenue': Decimal('2853.0400'), 'impressions': 20774}], 'query_type': 'multi_metrics'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your metrics in the last 5 days:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1516ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your metrics in the last 5 days:
```

---

## Test 98: Compare CTR and conversion rate for Google vs Meta campaigns in September

**Answer**:
> In September 2025, when comparing Google and Meta campaigns, we see distinct differences in performance for click-through rate (CTR) and conversion rate (CVR).

For CTR, Google outperformed Meta with a rate of 3.53%, compared to Meta's 2.09%. This indicates that Google's campaigns were more effective in getting users to click on the ads.

On the other hand, when it comes to conversion rate, Meta had a slight edge over Google. Meta's CVR was 10.45%, while Google's was 9.87%. This suggests that Meta's campaigns were slightly more successful in converting clicks into actual actions or sales.

Overall, Google led in attracting clicks, while Meta excelled in converting those clicks into conversions.

**DSL**:
```json
{
  "query_type": "comparison",
  "metric": null,
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
    "ctr",
    "cvr"
  ],
  "question": "Compare CTR and conversion rate for Google vs Meta campaigns in September",
  "timeframe_description": "from 2025-09-01 to 2025-09-30",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Compare CTR and conversion rate for Google vs Meta campaigns in September'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.COMPARISON: 'comparison'>, 'metric': None, 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 9, 1), 'end': datetime.date(2025, 9, 30)}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': 'provider_vs_provider', 'comparison_entities': None, 'comparison_metrics': ['ctr', 'cvr'], 'question': 'Compare CTR and conversion rate for Google vs Meta campaigns in September', 'timeframe_description': 'from 2025-09-01 to 2025-09-30', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1512ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 1), end=datetime.date(2025, 9, 30), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['clicks', 'conversions', 'impressions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.COMPARISON: 'comparison'>, metric=None, time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 9, 1), end=datetime.date(2025, 9, 30)), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type='provider_vs_provider', comparison_entities=None, comparison_metrics=['ctr', 'cvr'], question='Compare CTR and conversion rate for Google vs Meta campaigns in September', timeframe_description='from 2025-09-01 to 2025-09-30', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.dsl.executor:[COMPARISON] Executing comparison plan for type: provider_vs_provider
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 2 metrics: ['ctr', 'cvr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 1) end=datetime.date(2025, 9, 30)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=google, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-01 to 2025-09-30
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('8272.5200'), 'revenue': Decimal('56264.0900'), 'clicks': 19897, 'impressions': 562923, 'conversions': Decimal('1962.9600'), 'leads': Decimal('960.8700'), 'installs': 412, 'purchases': 247, 'visitors': 13870, 'profit': Decimal('17621.6500')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for ctr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for ctr: 0.025703537465489125
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'ctr': MetricValue(value=0.0353458643544499, previous=None, delta_pct=None), 'cvr': MetricValue(value=Decimal('0.09865607880585012816002412424'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.025703537465489125
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 2 metrics: ['ctr', 'cvr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 1) end=datetime.date(2025, 9, 30)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=meta, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-01 to 2025-09-30
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('5373.3000'), 'revenue': Decimal('55519.4900'), 'clicks': 10965, 'impressions': 525222, 'conversions': Decimal('1146.0900'), 'leads': Decimal('635.0000'), 'installs': 0, 'purchases': 286, 'visitors': 9958, 'profit': Decimal('15778.4900')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for ctr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for ctr: 0.025703537465489125
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'ctr': MetricValue(value=0.0208768863452026, previous=None, delta_pct=None), 'cvr': MetricValue(value=Decimal('0.1045225718194254445964432285'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.025703537465489125
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 2 metrics: ['ctr', 'cvr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 1) end=datetime.date(2025, 9, 30)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=tiktok, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-01 to 2025-09-30
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('3487.9400'), 'revenue': Decimal('3223.4300'), 'clicks': 7107, 'impressions': 284409, 'conversions': Decimal('369.9800'), 'leads': Decimal('0'), 'installs': 298, 'purchases': 0, 'visitors': 3094, 'profit': Decimal('960.3700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for ctr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for ctr: 0.025703537465489125
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'ctr': MetricValue(value=0.024988660696391465, previous=None, delta_pct=None), 'cvr': MetricValue(value=Decimal('0.05205853383987617841564654566'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.025703537465489125
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 2 metrics: ['ctr', 'cvr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 1) end=datetime.date(2025, 9, 30)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=other, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-01 to 2025-09-30
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('2708.3800'), 'revenue': Decimal('15012.7500'), 'clicks': 5015, 'impressions': 299745, 'conversions': Decimal('234.0100'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 0, 'visitors': 4356, 'profit': Decimal('4394.6000')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for ctr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for ctr: 0.025703537465489125
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'ctr': MetricValue(value=0.016730887921399856, previous=None, delta_pct=None), 'cvr': MetricValue(value=Decimal('0.04666201395812562313060817547'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.025703537465489125
INFO:app.dsl.executor:[COMPARISON] Completed execution for 4 items
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'comparison': [{'provider': 'google', 'ctr': 0.0353458643544499, 'cvr': Decimal('0.09865607880585012816002412424')}, {'provider': 'meta', 'ctr': 0.0208768863452026, 'cvr': Decimal('0.1045225718194254445964432285')}, {'provider': 'tiktok', 'ctr': 0.024988660696391465, 'cvr': Decimal('0.05205853383987617841564654566')}, {'provider': 'other', 'ctr': 0.016730887921399856, 'cvr': Decimal('0.04666201395812562313060817547')}], 'comparison_type': 'provider_vs_provider', 'metrics': ['ctr', 'cvr'], 'query_type': 'comparison'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'In September 2025, when comparing Google and Meta campaigns, we see distinct differences in performance for click-through rate (CTR) and conversion rate (CVR).
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 3183ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 5036ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'In September 2025, when comparing Google and Meta campaigns, we see distinct differences in performance for click-through rate (CTR) and conversion rate (CVR).
```

---

## Test 99: What's the revenue, ROAS, and cost per lead for lead gen campaigns this month to date?

**Answer**:
> Here are your metrics from October 01 to 29:

• REVENUE: $60,191.63
• ROAS: 2.24×
• CPL: $2.28

Top CAMPAIGN:
  - Morning Audience - Lead Gen - B2B: $21,207.11
  - Weekend Audience - Lead Gen - B2B: $20,306.07
  - Evening Audience - Lead Gen - B2B: $18,678.45

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
    "end": "2025-10-29"
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
  "timeframe_description": "this month",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'What's the revenue, ROAS, and cost per lead for lead gen campaigns this month to date?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': ['revenue', 'roas', 'cpl'], 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 10, 1), 'end': datetime.date(2025, 10, 29)}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'lead gen', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's the revenue, ROAS, and cost per lead for lead gen campaigns this month to date?", 'timeframe_description': 'this month', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1849ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['leads', 'revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'lead gen', 'metric_filters': None}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric=['revenue', 'roas', 'cpl'], time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 29)), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='lead gen', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's the revenue, ROAS, and cost per lead for lead gen campaigns this month to date?", timeframe_description='this month', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['revenue', 'roas', 'cpl']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=lead gen
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'lead gen'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Lead Gen - B2B (ID: 8e751a39-6438-486a-a116-c899baed8949, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Lead Gen - B2B
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 8e751a39-6438-486a-a116-c899baed8949 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'lead gen': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('26858.4200'), 'revenue': Decimal('60191.6300'), 'clicks': 67360, 'impressions': 1897434, 'conversions': Decimal('11765.4200'), 'leads': Decimal('11765.4200'), 'installs': 0, 'purchases': 0, 'visitors': 60462, 'profit': Decimal('17890.2800')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 1673577.62
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=60191.63, previous=None, delta_pct=None), 'roas': MetricValue(value=Decimal('2.241071142680768265594178660'), previous=None, delta_pct=None), 'cpl': MetricValue(value=Decimal('2.282827132393063741030919423'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 1673577.62
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 3 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'lead gen'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Lead Gen - B2B (ID: 8e751a39-6438-486a-a116-c899baed8949, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Lead Gen - B2B
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 8e751a39-6438-486a-a116-c899baed8949 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'lead gen': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for revenue by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=lead gen
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity by name (exact first): 'lead gen'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using partial match for 'lead gen': Lead Gen - B2B (8e751a39-6438-486a-a116-c899baed8949)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Routing named-entity same-level breakdown to child level: campaign→adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'lead gen'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Lead Gen - B2B (ID: 8e751a39-6438-486a-a116-c899baed8949, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Lead Gen - B2B
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 8e751a39-6438-486a-a116-c899baed8949 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'lead gen': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'metrics': {'revenue': {'summary': 60191.63, 'previous': None, 'delta_pct': None}, 'roas': {'summary': Decimal('2.241071142680768265594178660'), 'previous': None, 'delta_pct': None}, 'cpl': {'summary': Decimal('2.282827132393063741030919423'), 'previous': None, 'delta_pct': None}}, 'timeseries': [{'date': '2025-10-01', 'value': 1953.54}, {'date': '2025-10-02', 'value': 2360.52}, {'date': '2025-10-03', 'value': 1734.75}, {'date': '2025-10-04', 'value': 2305.82}, {'date': '2025-10-05', 'value': 2036.27}, {'date': '2025-10-06', 'value': 2520.16}, {'date': '2025-10-07', 'value': 1733.14}, {'date': '2025-10-08', 'value': 2077.45}, {'date': '2025-10-09', 'value': 2338.0}, {'date': '2025-10-10', 'value': 1548.05}, {'date': '2025-10-11', 'value': 1493.76}, {'date': '2025-10-12', 'value': 2268.82}, {'date': '2025-10-13', 'value': 1904.82}, {'date': '2025-10-14', 'value': 3326.51}, {'date': '2025-10-15', 'value': 1903.61}, {'date': '2025-10-16', 'value': 2886.5}, {'date': '2025-10-17', 'value': 2199.73}, {'date': '2025-10-18', 'value': 1806.39}, {'date': '2025-10-19', 'value': 1721.86}, {'date': '2025-10-20', 'value': 1665.69}, {'date': '2025-10-21', 'value': 1853.88}, {'date': '2025-10-22', 'value': 2653.24}, {'date': '2025-10-23', 'value': 1066.2}, {'date': '2025-10-24', 'value': 2371.37}, {'date': '2025-10-25', 'value': 2742.9}, {'date': '2025-10-26', 'value': 3314.19}, {'date': '2025-10-27', 'value': 2610.94}, {'date': '2025-10-28', 'value': 1793.52}], 'breakdown': [{'label': 'Morning Audience - Lead Gen - B2B', 'value': 21207.11, 'spend': Decimal('8946.8700'), 'clicks': 22785, 'conversions': Decimal('4007.6200'), 'revenue': Decimal('21207.1100'), 'impressions': 627044}, {'label': 'Weekend Audience - Lead Gen - B2B', 'value': 20306.07, 'spend': Decimal('8941.2400'), 'clicks': 22228, 'conversions': Decimal('3915.3700'), 'revenue': Decimal('20306.0700'), 'impressions': 622016}, {'label': 'Evening Audience - Lead Gen - B2B', 'value': 18678.45, 'spend': Decimal('8970.3100'), 'clicks': 22347, 'conversions': Decimal('3842.4300'), 'revenue': Decimal('18678.4500'), 'impressions': 648374}], 'query_type': 'multi_metrics'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your metrics from October 01 to 29:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2319ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your metrics from October 01 to 29:
```

---

## Test 100: Give me spend, clicks, and CPC for Holiday Sale and Summer Sale campaigns last month

**Answer**:
> In the last 30 days, the Holiday Sale and Summer Sale campaigns showed some interesting differences in performance. 

For spend, the Summer Sale campaign spent more, with a total of $25,689.44 compared to the Holiday Sale's $18,581.27. When it comes to clicks, the Summer Sale also led the way, generating 63,974 clicks, while the Holiday Sale campaign brought in 36,506 clicks.

Looking at the cost per click (CPC), the Summer Sale campaign was more cost-efficient, with a CPC of $0.40, compared to the Holiday Sale's CPC of $0.51. 

Overall, the Summer Sale campaign performed better in terms of both generating more clicks and maintaining a lower CPC, despite having a higher total spend.

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
  "timeframe_description": "last month",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Give me spend, clicks, and CPC for Holiday Sale and Summer Sale campaigns last month'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.COMPARISON: 'comparison'>, 'metric': None, 'time_range': {'last_n_days': 30, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': 'entity_vs_entity', 'comparison_entities': ['Holiday Sale', 'Summer Sale'], 'comparison_metrics': ['spend', 'clicks', 'cpc'], 'question': 'Give me spend, clicks, and CPC for Holiday Sale and Summer Sale campaigns last month', 'timeframe_description': 'last month', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 4310ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 30), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['clicks', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.COMPARISON: 'comparison'>, metric=None, time_range=TimeRange(last_n_days=30, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type='entity_vs_entity', comparison_entities=['Holiday Sale', 'Summer Sale'], comparison_metrics=['spend', 'clicks', 'cpc'], question='Give me spend, clicks, and CPC for Holiday Sale and Summer Sale campaigns last month', timeframe_description='last month', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.dsl.executor:[COMPARISON] Executing comparison plan for type: entity_vs_entity
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['spend', 'clicks', 'cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 30) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-30 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('18581.2700'), 'revenue': Decimal('216432.7500'), 'clicks': 36506, 'impressions': 1873941, 'conversions': Decimal('1634.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 1634, 'visitors': 33408, 'profit': Decimal('65638.4300')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 278489.51
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=18581.27, previous=None, delta_pct=None), 'clicks': MetricValue(value=36506.0, previous=None, delta_pct=None), 'cpc': MetricValue(value=Decimal('0.5089922204569111926806552348'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 278489.51
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['spend', 'clicks', 'cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 30) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Summer Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-30 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Summer Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Summer Sale Campaign (ID: d02a69cb-5368-488f-93ec-993c747a2299, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Summer Sale Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity d02a69cb-5368-488f-93ec-993c747a2299 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Summer Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('25689.4400'), 'revenue': Decimal('399509.4600'), 'clicks': 63974, 'impressions': 1828195, 'conversions': Decimal('3196.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 3196, 'visitors': 58691, 'profit': Decimal('122480.0500')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 278489.51
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=25689.44, previous=None, delta_pct=None), 'clicks': MetricValue(value=63974.0, previous=None, delta_pct=None), 'cpc': MetricValue(value=Decimal('0.4015606340075655735142401601'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 278489.51
INFO:app.dsl.executor:[COMPARISON] Completed execution for 2 items
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'comparison': [{'entity': 'Holiday Sale', 'spend': 18581.27, 'clicks': 36506.0, 'cpc': Decimal('0.5089922204569111926806552348')}, {'entity': 'Summer Sale', 'spend': 25689.44, 'clicks': 63974.0, 'cpc': Decimal('0.4015606340075655735142401601')}], 'comparison_type': 'entity_vs_entity', 'metrics': ['spend', 'clicks', 'cpc'], 'query_type': 'comparison'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'In the last 30 days, the Holiday Sale and Summer Sale campaigns showed some interesting differences in performance. 
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 6109ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 10751ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'In the last 30 days, the Holiday Sale and Summer Sale campaigns showed some interesting differences in performance. 
```

---

## Test 101: Show me conversion rate, revenue, and profit for all campaigns last week

**Answer**:
> Here are your metrics last week:

• CVR: 8.5%
• REVENUE: $370,045.59
• PROFIT: $111,922.76

Top CAMPAIGN:
  - Lead Gen - B2B: 17.6%
  - Website Traffic Push: 6.1%
  - Summer Sale Campaign: 5.4%
  - Blog Content Promotion: 12.5%
  - Newsletter Signup Campaign: 18.8%

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
  "timeframe_description": "last week",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Show me conversion rate, revenue, and profit for all campaigns last week'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': ['cvr', 'revenue', 'profit'], 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Show me conversion rate, revenue, and profit for all campaigns last week', 'timeframe_description': 'last week', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1557ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 23), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['clicks', 'conversions', 'profit', 'revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric=['cvr', 'revenue', 'profit'], time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Show me conversion rate, revenue, and profit for all campaigns last week', timeframe_description='last week', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['cvr', 'revenue', 'profit']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('56868.1600'), 'revenue': Decimal('370045.5900'), 'clicks': 125586, 'impressions': 4953838, 'conversions': Decimal('10701.1500'), 'leads': Decimal('4164.6900'), 'installs': 2448, 'purchases': 1528, 'visitors': 90824, 'profit': Decimal('111922.7600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cvr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cvr: 0.08520973675409679422865606039
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cvr': MetricValue(value=Decimal('0.08520973675409679422865606039'), previous=None, delta_pct=None), 'revenue': MetricValue(value=370045.59, previous=None, delta_pct=None), 'profit': MetricValue(value=111922.76, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.08520973675409679422865606039
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 3 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cvr by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 23) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-23 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'metrics': {'cvr': {'summary': Decimal('0.08520973675409679422865606039'), 'previous': None, 'delta_pct': None}, 'revenue': {'summary': 370045.59, 'previous': None, 'delta_pct': None}, 'profit': {'summary': 111922.76, 'previous': None, 'delta_pct': None}}, 'timeseries': [{'date': '2025-10-23', 'value': Decimal('0.08583712196086183040126507215')}, {'date': '2025-10-24', 'value': Decimal('0.08755490278360609875507063925')}, {'date': '2025-10-25', 'value': Decimal('0.08713194512017125620317213195')}, {'date': '2025-10-26', 'value': Decimal('0.08163927376970855231724796942')}, {'date': '2025-10-27', 'value': Decimal('0.08539040408647268083553771778')}, {'date': '2025-10-28', 'value': Decimal('0.08366125018298931342409603279')}], 'breakdown': [{'label': 'Lead Gen - B2B', 'value': Decimal('0.1759954921111945905334335086'), 'spend': Decimal('727.7800'), 'clicks': 1331, 'conversions': Decimal('234.2500'), 'revenue': Decimal('1272.8300'), 'impressions': 42491}, {'label': 'Website Traffic Push', 'value': Decimal('0.06114035087719298245614035088'), 'spend': Decimal('480.8900'), 'clicks': 1254, 'conversions': Decimal('76.6700'), 'revenue': Decimal('3830.1100'), 'impressions': 35596}, {'label': 'Summer Sale Campaign', 'value': Decimal('0.05413105413105413105413105413'), 'spend': Decimal('441.4900'), 'clicks': 1053, 'conversions': Decimal('57.0000'), 'revenue': Decimal('7730.2600'), 'impressions': 31363}, {'label': 'Blog Content Promotion', 'value': Decimal('0.1252279635258358662613981763'), 'spend': Decimal('425.3600'), 'clicks': 658, 'conversions': Decimal('82.4000'), 'revenue': Decimal('4492.0600'), 'impressions': 34881}, {'label': 'Newsletter Signup Campaign', 'value': Decimal('0.1879612903225806451612903226'), 'spend': Decimal('351.3500'), 'clicks': 775, 'conversions': Decimal('145.6700'), 'revenue': Decimal('701.7800'), 'impressions': 35596}, {'label': 'Holiday Sale - Purchases', 'value': Decimal('0.04721753794266441821247892074'), 'spend': Decimal('343.0600'), 'clicks': 593, 'conversions': Decimal('28.0000'), 'revenue': Decimal('2734.5800'), 'impressions': 30349}, {'label': 'Mobile Game Installs', 'value': Decimal('0.09701492537313432835820895522'), 'spend': Decimal('318.7100'), 'clicks': 536, 'conversions': Decimal('52.0000'), 'revenue': Decimal('177.7900'), 'impressions': 23606}, {'label': 'Product Launch Teaser', 'value': Decimal('0.02484725050916496945010183299'), 'spend': Decimal('313.4900'), 'clicks': 491, 'conversions': Decimal('12.2000'), 'revenue': Decimal('395.0900'), 'impressions': 37040}, {'label': 'Black Friday Deals', 'value': Decimal('0.05181347150259067357512953368'), 'spend': Decimal('308.2500'), 'clicks': 579, 'conversions': Decimal('30.0000'), 'revenue': Decimal('4605.5500'), 'impressions': 28010}, {'label': 'Brand Awareness', 'value': Decimal('0.01803328290468986384266263238'), 'spend': Decimal('293.7000'), 'clicks': 661, 'conversions': Decimal('11.9200'), 'revenue': Decimal('475.1300'), 'impressions': 27467}], 'query_type': 'multi_metrics'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your metrics last week:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1765ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your metrics last week:
```

---

## Test 102: Compare CPA, ROAS, and revenue for App Install campaign vs Holiday Sale campaign last 5 days

**Answer**:
> Over the last 5 days, we've seen some interesting differences between the App Install Campaign and the Holiday Sale campaign across key metrics.

Starting with Cost Per Acquisition (CPA), the App Install Campaign performed better with a lower CPA of $4.33 compared to the Holiday Sale's $9.37. This indicates that acquiring each customer was more cost-effective for the App Install Campaign.

However, when we look at Return on Ad Spend (ROAS), the Holiday Sale campaign significantly outperformed the App Install Campaign. The Holiday Sale achieved a ROAS of 15.45, meaning it generated $15.45 for every dollar spent, while the App Install Campaign had a ROAS of only 0.55, indicating less than a dollar return for each dollar spent.

In terms of revenue, the Holiday Sale campaign also took the lead, generating $38,227.48 compared to the App Install Campaign's $2,123.93. This substantial difference highlights the Holiday Sale's effectiveness in driving sales.

Overall, while the App Install Campaign was more cost-efficient per acquisition, the Holiday Sale campaign excelled in generating higher returns and revenue.

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
  "timeframe_description": "last 5 days",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Compare CPA, ROAS, and revenue for App Install campaign vs Holiday Sale campaign last 5 days'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.COMPARISON: 'comparison'>, 'metric': None, 'time_range': {'last_n_days': 5, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': 'entity_vs_entity', 'comparison_entities': ['App Install Campaign', 'Holiday Sale'], 'comparison_metrics': ['cpa', 'roas', 'revenue'], 'question': 'Compare CPA, ROAS, and revenue for App Install campaign vs Holiday Sale campaign last 5 days', 'timeframe_description': 'last 5 days', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 3252ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 25), end=datetime.date(2025, 10, 29), group_by='none', breakdown=None, derived=None, need_timeseries=False, need_previous=False, base_measures=['conversions', 'revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.COMPARISON: 'comparison'>, metric=None, time_range=TimeRange(last_n_days=5, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type='entity_vs_entity', comparison_entities=['App Install Campaign', 'Holiday Sale'], comparison_metrics=['cpa', 'roas', 'revenue'], question='Compare CPA, ROAS, and revenue for App Install campaign vs Holiday Sale campaign last 5 days', timeframe_description='last 5 days', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.dsl.executor:[COMPARISON] Executing comparison plan for type: entity_vs_entity
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['cpa', 'roas', 'revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 25) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-25 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install Campaign'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install Campaign': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('3827.9100'), 'revenue': Decimal('2123.9300'), 'clicks': 9048, 'impressions': 262148, 'conversions': Decimal('884.0000'), 'leads': Decimal('0'), 'installs': 884, 'purchases': 0, 'visitors': 0, 'profit': Decimal('585.9400')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpa
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpa: 5.365794286488408717592670990
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpa': MetricValue(value=Decimal('4.330214932126696832579185520'), previous=None, delta_pct=None), 'roas': MetricValue(value=Decimal('0.5548536930074113550214085493'), previous=None, delta_pct=None), 'revenue': MetricValue(value=2123.93, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 5.365794286488408717592670990
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['cpa', 'roas', 'revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 25) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-25 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('2473.7800'), 'revenue': Decimal('38227.4800'), 'clicks': 5303, 'impressions': 247677, 'conversions': Decimal('264.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 264, 'visitors': 4853, 'profit': Decimal('11470.5300')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpa
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpa: 5.365794286488408717592670990
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpa': MetricValue(value=Decimal('9.370378787878787878787878788'), previous=None, delta_pct=None), 'roas': MetricValue(value=Decimal('15.45306373242568053747705940'), previous=None, delta_pct=None), 'revenue': MetricValue(value=38227.48, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 5.365794286488408717592670990
INFO:app.dsl.executor:[COMPARISON] Completed execution for 2 items
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'comparison': [{'entity': 'App Install Campaign', 'cpa': Decimal('4.330214932126696832579185520'), 'roas': Decimal('0.5548536930074113550214085493'), 'revenue': 2123.93}, {'entity': 'Holiday Sale', 'cpa': Decimal('9.370378787878787878787878788'), 'roas': Decimal('15.45306373242568053747705940'), 'revenue': 38227.48}], 'comparison_type': 'entity_vs_entity', 'metrics': ['cpa', 'roas', 'revenue'], 'query_type': 'comparison'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Over the last 5 days, we've seen some interesting differences between the App Install Campaign and the Holiday Sale campaign across key metrics.
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 8420ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 11970ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Over the last 5 days, we've seen some interesting differences between the App Install Campaign and the Holiday Sale campaign across key metrics.
```

---

## Test 103: What's the CTR, CPC, and conversions for Weekend Audience adsets in September?

**Answer**:
> Here are your metrics from 2025-09-01 to 2025-09-30:

• CTR: 2.0%
• CPC: $0.45
• CONVERSIONS: 20

Top ADSET:
  - Carousel Ad - Weekend Audience - Holiday Sale - Purchases: 2.5%
  - Video Ad - Weekend Audience - Holiday Sale - Purchases: 1.4%
  - Image Ad - Weekend Audience - Holiday Sale - Purchases: 1.4%

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
    "entity_name": "Weekend Audience",
    "metric_filters": null
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "What's the CTR, CPC, and conversions for Weekend Audience adsets in September?",
  "timeframe_description": "from 2025-09-01 to 2025-09-30",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'What's the CTR, CPC, and conversions for Weekend Audience adsets in September?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': ['ctr', 'cpc', 'conversions'], 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 9, 1), 'end': datetime.date(2025, 9, 30)}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Weekend Audience', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's the CTR, CPC, and conversions for Weekend Audience adsets in September?", 'timeframe_description': 'from 2025-09-01 to 2025-09-30', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 2027ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 1), end=datetime.date(2025, 9, 30), group_by='adset', breakdown='adset', derived=None, need_timeseries=True, need_previous=False, base_measures=['clicks', 'conversions', 'impressions', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Weekend Audience', 'metric_filters': None}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric=['ctr', 'cpc', 'conversions'], time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 9, 1), end=datetime.date(2025, 9, 30)), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Weekend Audience', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's the CTR, CPC, and conversions for Weekend Audience adsets in September?", timeframe_description='from 2025-09-01 to 2025-09-30', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['ctr', 'cpc', 'conversions']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 1) end=datetime.date(2025, 9, 30)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Weekend Audience
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-01 to 2025-09-30
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Weekend Audience'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Weekend Audience - Holiday Sale - Purchases (ID: bf14ea12-7e05-4c11-9b51-b4d6511f16c1, Level: LevelEnum.adset)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using adset hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 4 descendants for Weekend Audience - Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity bf14ea12-7e05-4c11-9b51-b4d6511f16c1 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 3 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Weekend Audience': 3 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('257.7400'), 'revenue': Decimal('3185.6900'), 'clicks': 578, 'impressions': 28822, 'conversions': Decimal('20.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 20, 'visitors': 529, 'profit': Decimal('731.9700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for ctr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for ctr: 0.025703537465489125
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'ctr': MetricValue(value=0.020054125320935395, previous=None, delta_pct=None), 'cpc': MetricValue(value=Decimal('0.4459169550173010380622837370'), previous=None, delta_pct=None), 'conversions': MetricValue(value=20.0, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.025703537465489125
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 3 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Weekend Audience'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Weekend Audience - Holiday Sale - Purchases (ID: bf14ea12-7e05-4c11-9b51-b4d6511f16c1, Level: LevelEnum.adset)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using adset hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 4 descendants for Weekend Audience - Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity bf14ea12-7e05-4c11-9b51-b4d6511f16c1 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 3 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Weekend Audience': 3 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for ctr by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 1) end=datetime.date(2025, 9, 30)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Weekend Audience
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-01 to 2025-09-30
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity by name (exact first): 'Weekend Audience'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using partial match for 'Weekend Audience': Weekend Audience - Holiday Sale - Purchases (bf14ea12-7e05-4c11-9b51-b4d6511f16c1)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Routing named-entity same-level breakdown to child level: adset→ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Weekend Audience'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Weekend Audience - Holiday Sale - Purchases (ID: bf14ea12-7e05-4c11-9b51-b4d6511f16c1, Level: LevelEnum.adset)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using adset hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 4 descendants for Weekend Audience - Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity bf14ea12-7e05-4c11-9b51-b4d6511f16c1 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 3 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Weekend Audience': 3 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'metrics': {'ctr': {'summary': 0.020054125320935395, 'previous': None, 'delta_pct': None}, 'cpc': {'summary': Decimal('0.4459169550173010380622837370'), 'previous': None, 'delta_pct': None}, 'conversions': {'summary': 20.0, 'previous': None, 'delta_pct': None}}, 'timeseries': [{'date': '2025-09-29', 'value': 0.02149366085578447}, {'date': '2025-09-30', 'value': 0.019278009185090247}], 'breakdown': [{'label': 'Carousel Ad - Weekend Audience - Holiday Sale - Purchases', 'value': 0.024819855884707767, 'spend': Decimal('159.5800'), 'clicks': 403, 'conversions': Decimal('13.0000'), 'revenue': Decimal('2166.2200'), 'impressions': 16237}, {'label': 'Video Ad - Weekend Audience - Holiday Sale - Purchases', 'value': 0.014113836186950486, 'spend': Decimal('27.2800'), 'clicks': 61, 'conversions': Decimal('1.0000'), 'revenue': Decimal('57.4200'), 'impressions': 4322}, {'label': 'Image Ad - Weekend Audience - Holiday Sale - Purchases', 'value': 0.01379644197022873, 'spend': Decimal('70.8800'), 'clicks': 114, 'conversions': Decimal('6.0000'), 'revenue': Decimal('962.0500'), 'impressions': 8263}], 'query_type': 'multi_metrics'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your metrics from 2025-09-01 to 2025-09-30:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2471ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your metrics from 2025-09-01 to 2025-09-30:
```

---

## Test 104: Give me spend, revenue, ROAS, and profit for all Meta campaigns this month to date

**Answer**:
> Here are your metrics from October 01 to 29:

• SPEND: $72,576.55
• REVENUE: $656,144.96
• ROAS: 9.04×
• PROFIT: $196,854.19

Top CAMPAIGN:
  - Blog Content Promotion: $1,802.24
  - Newsletter Signup Campaign: $1,708.30
  - Holiday Sale - Purchases: $1,324.75
  - Black Friday Deals: $1,231.56

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
    "end": "2025-10-29"
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
  "timeframe_description": "this month",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Give me spend, revenue, ROAS, and profit for all Meta campaigns this month to date'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': ['spend', 'revenue', 'roas', 'profit'], 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 10, 1), 'end': datetime.date(2025, 10, 29)}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': 'meta', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Give me spend, revenue, ROAS, and profit for all Meta campaigns this month to date', 'timeframe_description': 'this month', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1011ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 29), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['profit', 'revenue', 'spend'], filters={'provider': 'meta', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric=['spend', 'revenue', 'roas', 'profit'], time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 29)), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=10, sort_order='desc', filters=Filters(provider='meta', level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Give me spend, revenue, ROAS, and profit for all Meta campaigns this month to date', timeframe_description='this month', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 4 metrics: ['spend', 'revenue', 'roas', 'profit']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=meta, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('72576.5500'), 'revenue': Decimal('656144.9600'), 'clicks': 143052, 'impressions': 7253988, 'conversions': Decimal('13464.8300'), 'leads': Decimal('6839.4200'), 'installs': 0, 'purchases': 3509, 'visitors': 130033, 'profit': Decimal('196854.1900')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 268552.71
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=72576.55, previous=None, delta_pct=None), 'revenue': MetricValue(value=656144.96, previous=None, delta_pct=None), 'roas': MetricValue(value=Decimal('9.040729546940437372677538406'), previous=None, delta_pct=None), 'profit': MetricValue(value=196854.19, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 268552.71
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 4 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for spend by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=meta, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-29
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'metrics': {'spend': {'summary': 72576.55, 'previous': None, 'delta_pct': None}, 'revenue': {'summary': 656144.96, 'previous': None, 'delta_pct': None}, 'roas': {'summary': Decimal('9.040729546940437372677538406'), 'previous': None, 'delta_pct': None}, 'profit': {'summary': 196854.19, 'previous': None, 'delta_pct': None}}, 'timeseries': [{'date': '2025-10-01', 'value': 2530.12}, {'date': '2025-10-02', 'value': 2393.98}, {'date': '2025-10-03', 'value': 2390.46}, {'date': '2025-10-04', 'value': 2401.8}, {'date': '2025-10-05', 'value': 2758.83}, {'date': '2025-10-06', 'value': 2273.11}, {'date': '2025-10-07', 'value': 2884.56}, {'date': '2025-10-08', 'value': 2575.61}, {'date': '2025-10-09', 'value': 2846.19}, {'date': '2025-10-10', 'value': 2664.13}, {'date': '2025-10-11', 'value': 2255.98}, {'date': '2025-10-12', 'value': 2776.25}, {'date': '2025-10-13', 'value': 3090.87}, {'date': '2025-10-14', 'value': 2495.08}, {'date': '2025-10-15', 'value': 2500.11}, {'date': '2025-10-16', 'value': 2617.36}, {'date': '2025-10-17', 'value': 2654.28}, {'date': '2025-10-18', 'value': 2480.58}, {'date': '2025-10-19', 'value': 3337.02}, {'date': '2025-10-20', 'value': 2454.67}, {'date': '2025-10-21', 'value': 2589.77}, {'date': '2025-10-22', 'value': 2378.6}, {'date': '2025-10-23', 'value': 2722.94}, {'date': '2025-10-24', 'value': 2394.18}, {'date': '2025-10-25', 'value': 2407.04}, {'date': '2025-10-26', 'value': 2531.83}, {'date': '2025-10-27', 'value': 3054.27}, {'date': '2025-10-28', 'value': 2116.93}], 'breakdown': [{'label': 'Blog Content Promotion', 'value': 1802.24, 'spend': Decimal('1802.2400'), 'clicks': 3146, 'conversions': Decimal('374.9700'), 'revenue': Decimal('20108.3900'), 'impressions': 161436}, {'label': 'Newsletter Signup Campaign', 'value': 1708.3, 'spend': Decimal('1708.3000'), 'clicks': 3323, 'conversions': Decimal('640.5600'), 'revenue': Decimal('3107.3600'), 'impressions': 171372}, {'label': 'Holiday Sale - Purchases', 'value': 1324.75, 'spend': Decimal('1324.7500'), 'clicks': 2782, 'conversions': Decimal('127.0000'), 'revenue': Decimal('16412.8400'), 'impressions': 142651}, {'label': 'Black Friday Deals', 'value': 1231.56, 'spend': Decimal('1231.5600'), 'clicks': 2362, 'conversions': Decimal('103.0000'), 'revenue': Decimal('14019.4500'), 'impressions': 121431}], 'query_type': 'multi_metrics'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your metrics from October 01 to 29:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1301ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your metrics from October 01 to 29:
```

---

## Test 105: Compare clicks, CTR, and cost per click for Morning vs Evening Audience adsets last month

**Answer**:
> In the last 30 days, the Evening Audience ad set outperformed the Morning Audience in several key metrics. The Evening Audience garnered 9,793 clicks compared to the Morning Audience's 8,321 clicks, indicating a higher engagement level. Additionally, the Evening Audience had a slightly better click-through rate (CTR) of 2.01% versus the Morning Audience's 1.87%. When it comes to cost efficiency, the Evening Audience also had a lower cost per click (CPC) at $0.51, compared to the Morning Audience's $0.52. Overall, the Evening Audience ad set demonstrated superior performance across clicks, CTR, and CPC.

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
  "timeframe_description": "last month",
  "workspace_id": "4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'Compare clicks, CTR, and cost per click for Morning vs Evening Audience adsets last month'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 5 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.COMPARISON: 'comparison'>, 'metric': None, 'time_range': {'last_n_days': 30, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': 'entity_vs_entity', 'comparison_entities': ['Morning Audience', 'Evening Audience'], 'comparison_metrics': ['clicks', 'ctr', 'cpc'], 'question': 'Compare clicks, CTR, and cost per click for Morning vs Evening Audience adsets last month', 'timeframe_description': 'last month', 'workspace_id': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1399ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 30), end=datetime.date(2025, 10, 29), group_by='adset', breakdown='adset', derived=None, need_timeseries=True, need_previous=False, base_measures=['clicks', 'impressions', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.COMPARISON: 'comparison'>, metric=None, time_range=TimeRange(last_n_days=30, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type='entity_vs_entity', comparison_entities=['Morning Audience', 'Evening Audience'], comparison_metrics=['clicks', 'ctr', 'cpc'], question='Compare clicks, CTR, and cost per click for Morning vs Evening Audience adsets last month', timeframe_description='last month', workspace_id='4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.dsl.executor:[COMPARISON] Executing comparison plan for type: entity_vs_entity
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['clicks', 'ctr', 'cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 30) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Morning Audience
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-30 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Morning Audience'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Morning Audience - Holiday Sale - Purchases (ID: 2097b889-0ce5-4e1c-854d-b6099229bd5c, Level: LevelEnum.adset)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using adset hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 4 descendants for Morning Audience - Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 2097b889-0ce5-4e1c-854d-b6099229bd5c from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 3 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Morning Audience': 3 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('4346.5300'), 'revenue': Decimal('48599.5700'), 'clicks': 8321, 'impressions': 444993, 'conversions': Decimal('358.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 358, 'visitors': 7612, 'profit': Decimal('14514.9200')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for clicks
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for clicks: 615725.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'clicks': MetricValue(value=8321.0, previous=None, delta_pct=None), 'ctr': MetricValue(value=0.018699170548750206, previous=None, delta_pct=None), 'cpc': MetricValue(value=Decimal('0.5223566878980891719745222930'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 615725.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['clicks', 'ctr', 'cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 30) end=datetime.date(2025, 10, 29)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Evening Audience
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-30 to 2025-10-29
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Evening Audience'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Evening Audience - Holiday Sale - Purchases (ID: a7408419-eb16-4c3b-80ec-d7cf998782c5, Level: LevelEnum.adset)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using adset hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 4 descendants for Evening Audience - Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity a7408419-eb16-4c3b-80ec-d7cf998782c5 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 3 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Evening Audience': 3 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('5002.2400'), 'revenue': Decimal('57978.9900'), 'clicks': 9793, 'impressions': 486688, 'conversions': Decimal('429.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 429, 'visitors': 8962, 'profit': Decimal('17373.4600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for clicks
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for clicks: 615725.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'clicks': MetricValue(value=9793.0, previous=None, delta_pct=None), 'ctr': MetricValue(value=0.020121720691695707, previous=None, delta_pct=None), 'cpc': MetricValue(value=Decimal('0.5107975084243847646277953640'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 615725.0
INFO:app.dsl.executor:[COMPARISON] Completed execution for 2 items
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'comparison': [{'entity': 'Morning Audience', 'clicks': 8321.0, 'ctr': 0.018699170548750206, 'cpc': Decimal('0.5223566878980891719745222930')}, {'entity': 'Evening Audience', 'clicks': 9793.0, 'ctr': 0.020121720691695707, 'cpc': Decimal('0.5107975084243847646277953640')}], 'comparison_type': 'entity_vs_entity', 'metrics': ['clicks', 'ctr', 'cpc'], 'query_type': 'comparison'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'In the last 30 days, the Evening Audience ad set outperformed the Morning Audience in several key metrics. The Evening Audience garnered 9,793 clicks compared to the Morning Audience's 8,321 clicks, indicating a higher engagement level. Additionally, the Evening Audience had a slightly better click-through rate (CTR) of 2.01% versus the Morning Audience's 1.87%. When it comes to cost efficiency, the Evening Audience also had a lower cost per click (CPC) at $0.51, compared to the Morning Audience's $0.52. Overall, the Evening Audience ad set demonstrated superior performance across clicks, CTR, and CPC.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 4376ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 6072ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'In the last 30 days, the Evening Audience ad set outperformed the Morning Audience in several key metrics. The Evening Audience garnered 9,793 clicks compared to the Morning Audience's 8,321 clicks, indicating a higher engagement level. Additionally, the Evening Audience had a slightly better click-through rate (CTR) of 2.01% versus the Morning Audience's 1.87%. When it comes to cost efficiency, the Evening Audience also had a lower cost per click (CPC) at $0.51, compared to the Morning Audience's $0.52. Overall, the Evening Audience ad set demonstrated superior performance across clicks, CTR, and CPC.'
```

---

