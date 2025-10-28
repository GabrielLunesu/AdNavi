# QA Test Results

**Test Run**: Tue Oct 28 14:25:29 CET 2025
**Workspace**: Defang Labs (4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199)
**System Version**: Phase 5 (v2.1.3)

---

## Test 1: What's my CPC this month?

**Answer**:
> Your CPC is $0.45 from October 01 to 28.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpc",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-28"
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

**Logs**:
```
Binary file (standard input) matches
```

---

## Test 2: How much did I spend this month?

**Answer**:
> You spent $268,552.71 from October 01 to 28.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "spend",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-28"
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

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'How much did I spend this month?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 1 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'spend', 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 10, 1), 'end': datetime.date(2025, 10, 28)}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How much did I spend this month?', 'timeframe_description': 'this month'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 2036ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='spend', time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 28)), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How much did I spend this month?', timeframe_description='this month'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('268552.7100'), 'revenue': Decimal('1673577.6200'), 'clicks': 593809, 'impressions': 23402098, 'conversions': Decimal('50121.9000'), 'leads': Decimal('19608.4100'), 'installs': 11733, 'purchases': 6792, 'visitors': 426056, 'profit': Decimal('503172.8300')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 268552.71
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=268552.71, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 268552.71
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=268552.71 previous=None delta_pct=None timeseries=[{'date': '2025-10-01', 'value': 8967.77}, {'date': '2025-10-02', 'value': 9536.8}, {'date': '2025-10-03', 'value': 8453.33}, {'date': '2025-10-04', 'value': 9493.13}, {'date': '2025-10-05', 'value': 10412.57}, {'date': '2025-10-06', 'value': 9041.32}, {'date': '2025-10-07', 'value': 10133.74}, {'date': '2025-10-08', 'value': 9551.81}, {'date': '2025-10-09', 'value': 10079.91}, {'date': '2025-10-10', 'value': 10308.26}, {'date': '2025-10-11', 'value': 8213.11}, {'date': '2025-10-12', 'value': 9737.22}, {'date': '2025-10-13', 'value': 10139.91}, {'date': '2025-10-14', 'value': 9607.39}, {'date': '2025-10-15', 'value': 9542.43}, {'date': '2025-10-16', 'value': 9848.22}, {'date': '2025-10-17', 'value': 9940.11}, {'date': '2025-10-18', 'value': 9405.73}, {'date': '2025-10-19', 'value': 10312.94}, {'date': '2025-10-20', 'value': 9364.22}, {'date': '2025-10-21', 'value': 9654.67}, {'date': '2025-10-22', 'value': 9939.96}, {'date': '2025-10-23', 'value': 9386.67}, {'date': '2025-10-24', 'value': 9457.54}, {'date': '2025-10-25', 'value': 8887.48}, {'date': '2025-10-26', 'value': 9661.06}, {'date': '2025-10-27', 'value': 10008.96}, {'date': '2025-10-28', 'value': 9466.45}] breakdown=None workspace_avg=268552.71
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'You spent $268,552.71 from October 01 to 28.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 737ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2948ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'You spent $268,552.71 from October 01 to 28.'
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
    "end": "2025-10-28"
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

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'What's my ROAS this week?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 2 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 10, 27), 'end': datetime.date(2025, 10, 28)}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's my ROAS this week?", 'timeframe_description': 'this week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 887ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 27), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 10, 27), end=datetime.date(2025, 10, 28)), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's my ROAS this week?", timeframe_description='this week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 27) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-27 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('19475.4100'), 'revenue': Decimal('123327.3500'), 'clicks': 42419, 'impressions': 1645128, 'conversions': Decimal('3586.7400'), 'leads': Decimal('1423.5300'), 'installs': 825, 'purchases': 499, 'visitors': 30340, 'profit': Decimal('36042.6200')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.332464887773864581028075917
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.332464887773864581028075917'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.332464887773864581028075917
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=6.332464887773865 previous=None delta_pct=None timeseries=[{'date': '2025-10-27', 'value': 6.218785967772876}, {'date': '2025-10-28', 'value': 6.452658599580624}] breakdown=None workspace_avg=6.332464887773865
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your ROAS is 6.33× this week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1038ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2086ms
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
  "timeframe_description": "yesterday"
}
```

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'How much revenue did I generate yesterday?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 3 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 1, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How much revenue did I generate yesterday?', 'timeframe_description': 'yesterday'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1557ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 28), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=1, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How much revenue did I generate yesterday?', timeframe_description='yesterday'))
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
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=61083.77 previous=None delta_pct=None timeseries=[{'date': '2025-10-28', 'value': 61083.77}] breakdown=None workspace_avg=61083.77
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your revenue was $61,083.77 yesterday.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1279ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3020ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your revenue was $61,083.77 yesterday.'
```

---

## Test 5: What's my conversion rate?

**Answer**:
> Your conversion rate was 8.6% last week.

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

**Logs**:
```
INFO:app.services.qa_service:[QA_PIPELINE] ===== Starting QA pipeline =====
INFO:app.services.qa_service:[QA_PIPELINE] Question: 'What's my conversion rate?'
INFO:app.services.qa_service:[QA_PIPELINE] Workspace ID: 4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199
INFO:app.services.qa_service:[QA_PIPELINE] User ID: 9d2b37b8-8cd5-4864-830b-36a890bc6ff4
INFO:app.services.qa_service:[QA_PIPELINE] Step 1: Fetching conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Context retrieved: 4 previous queries
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: None
INFO:app.services.qa_service:[ENTITY_CATALOG] Built catalog with 50 entities
INFO:app.services.qa_service:[QA_PIPELINE] Step 2: Translating question to DSL
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cvr', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's my conversion rate?", 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 980ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived='cvr', need_timeseries=True, need_previous=False, base_measures=['clicks', 'conversions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cvr', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's my conversion rate?", timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cvr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cvr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cvr: 0.08608288224573620215978021380
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cvr': MetricValue(value=Decimal('0.08608288224573620215978021380'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.08608288224573620215978021380
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.08608288224573621 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 0.09119118606167893}, {'date': '2025-10-23', 'value': 0.08583712196086184}, {'date': '2025-10-24', 'value': 0.0875549027836061}, {'date': '2025-10-25', 'value': 0.08713194512017125}, {'date': '2025-10-26', 'value': 0.08163927376970856}, {'date': '2025-10-27', 'value': 0.08539040408647268}, {'date': '2025-10-28', 'value': 0.08366125018298931}] breakdown=None workspace_avg=0.08608288224573621
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your conversion rate was 8.6% last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 736ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1895ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your conversion rate was 8.6% last week.'
```

---

## Test 6: How many clicks did I get last week?

**Answer**:
> You had 147,052 clicks last week.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'clicks', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How many clicks did I get last week?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1739ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['clicks'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='clicks', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How many clicks did I get last week?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['clicks']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for clicks
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for clicks: 147052.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'clicks': MetricValue(value=147052.0, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 147052.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=147052.0 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 21466.0}, {'date': '2025-10-23', 'value': 20236.0}, {'date': '2025-10-24', 'value': 21447.0}, {'date': '2025-10-25', 'value': 20554.0}, {'date': '2025-10-26', 'value': 20930.0}, {'date': '2025-10-27', 'value': 21926.0}, {'date': '2025-10-28', 'value': 20493.0}] breakdown=None workspace_avg=147052.0
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'You had 147,052 clicks last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 691ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2605ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'You had 147,052 clicks last week.'
```

---

## Test 7: How much profit did I make last week?

**Answer**:
> Your profit was $128,021.27 last week.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'profit', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How much profit did I make last week?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1622ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['profit'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='profit', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How much profit did I make last week?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['profit']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for profit
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for profit: 128021.27
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'profit': MetricValue(value=128021.27, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 128021.27
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=128021.27 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 16098.51}, {'date': '2025-10-23', 'value': 17432.2}, {'date': '2025-10-24', 'value': 17975.92}, {'date': '2025-10-25', 'value': 21491.89}, {'date': '2025-10-26', 'value': 18980.13}, {'date': '2025-10-27', 'value': 17862.54}, {'date': '2025-10-28', 'value': 18180.08}] breakdown=None workspace_avg=128021.27
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your profit was $128,021.27 last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 814ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2622ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your profit was $128,021.27 last week.'
```

---

## Test 8: How many leads did I generate this month?

**Answer**:
> You generated 19,608 leads from October 01 to 28.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "leads",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-28"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'leads', 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 10, 1), 'end': datetime.date(2025, 10, 28)}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How many leads did I generate this month?', 'timeframe_description': 'this month'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1343ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['leads'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='leads', time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 28)), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How many leads did I generate this month?', timeframe_description='this month'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['leads']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('268552.7100'), 'revenue': Decimal('1673577.6200'), 'clicks': 593809, 'impressions': 23402098, 'conversions': Decimal('50121.9000'), 'leads': Decimal('19608.4100'), 'installs': 11733, 'purchases': 6792, 'visitors': 426056, 'profit': Decimal('503172.8300')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for leads
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for leads: 19608.41
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'leads': MetricValue(value=19608.41, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 19608.41
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=19608.41 previous=None delta_pct=None timeseries=[{'date': '2025-10-01', 'value': 687.13}, {'date': '2025-10-02', 'value': 578.18}, {'date': '2025-10-03', 'value': 685.96}, {'date': '2025-10-04', 'value': 658.9}, {'date': '2025-10-05', 'value': 694.67}, {'date': '2025-10-06', 'value': 605.53}, {'date': '2025-10-07', 'value': 639.14}, {'date': '2025-10-08', 'value': 788.85}, {'date': '2025-10-09', 'value': 799.28}, {'date': '2025-10-10', 'value': 818.81}, {'date': '2025-10-11', 'value': 618.62}, {'date': '2025-10-12', 'value': 706.41}, {'date': '2025-10-13', 'value': 743.31}, {'date': '2025-10-14', 'value': 878.3}, {'date': '2025-10-15', 'value': 688.5}, {'date': '2025-10-16', 'value': 729.8}, {'date': '2025-10-17', 'value': 832.99}, {'date': '2025-10-18', 'value': 608.15}, {'date': '2025-10-19', 'value': 687.26}, {'date': '2025-10-20', 'value': 525.67}, {'date': '2025-10-21', 'value': 588.48}, {'date': '2025-10-22', 'value': 879.78}, {'date': '2025-10-23', 'value': 660.36}, {'date': '2025-10-24', 'value': 742.53}, {'date': '2025-10-25', 'value': 632.93}, {'date': '2025-10-26', 'value': 705.34}, {'date': '2025-10-27', 'value': 809.71}, {'date': '2025-10-28', 'value': 613.82}] breakdown=None workspace_avg=19608.41
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'You generated 19,608 leads from October 01 to 28.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 717ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2231ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'You generated 19,608 leads from October 01 to 28.'
```

---

## Test 9: What is my cost per lead this month?

**Answer**:
> Your cost per lead is $13.70 from October 01 to 28.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "cpl",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-28"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpl', 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 10, 1), 'end': datetime.date(2025, 10, 28)}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'What is my cost per lead this month?', 'timeframe_description': 'this month'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1548ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived='cpl', need_timeseries=True, need_previous=False, base_measures=['leads', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpl', time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 28)), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='What is my cost per lead this month?', timeframe_description='this month'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpl']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('268552.7100'), 'revenue': Decimal('1673577.6200'), 'clicks': 593809, 'impressions': 23402098, 'conversions': Decimal('50121.9000'), 'leads': Decimal('19608.4100'), 'installs': 11733, 'purchases': 6792, 'visitors': 426056, 'profit': Decimal('503172.8300')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpl
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpl: 13.69579226464562909486286751
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpl': MetricValue(value=Decimal('13.69579226464562909486286751'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 13.69579226464562909486286751
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=13.695792264645629 previous=None delta_pct=None timeseries=[{'date': '2025-10-01', 'value': 13.051052930304309}, {'date': '2025-10-02', 'value': 16.49451727835622}, {'date': '2025-10-03', 'value': 12.323357047058137}, {'date': '2025-10-04', 'value': 14.407542874487783}, {'date': '2025-10-05', 'value': 14.98923229734982}, {'date': '2025-10-06', 'value': 14.931250309646096}, {'date': '2025-10-07', 'value': 15.85527427480677}, {'date': '2025-10-08', 'value': 12.108525068137162}, {'date': '2025-10-09', 'value': 12.611237613852467}, {'date': '2025-10-10', 'value': 12.589318645351181}, {'date': '2025-10-11', 'value': 13.276502537906953}, {'date': '2025-10-12', 'value': 13.784091391684715}, {'date': '2025-10-13', 'value': 13.641562739637568}, {'date': '2025-10-14', 'value': 10.938620061482409}, {'date': '2025-10-15', 'value': 13.859738562091504}, {'date': '2025-10-16', 'value': 13.49440942724034}, {'date': '2025-10-17', 'value': 11.93304841594737}, {'date': '2025-10-18', 'value': 15.466134999588917}, {'date': '2025-10-19', 'value': 15.005878415737858}, {'date': '2025-10-20', 'value': 17.813875625392356}, {'date': '2025-10-21', 'value': 16.406114056552475}, {'date': '2025-10-22', 'value': 11.298233649321421}, {'date': '2025-10-23', 'value': 14.214473923314555}, {'date': '2025-10-24', 'value': 12.736912986680673}, {'date': '2025-10-25', 'value': 14.041805570916216}, {'date': '2025-10-26', 'value': 13.697025547962685}, {'date': '2025-10-27', 'value': 12.3611663435057}, {'date': '2025-10-28', 'value': 15.422192173601381}] breakdown=None workspace_avg=13.695792264645629
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your cost per lead is $13.70 from October 01 to 28.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 811ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2539ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your cost per lead is $13.70 from October 01 to 28.'
```

---

## Test 10: Which campaign had the highest ROAS last week?

**Answer**:
> The Summer Sale Campaign had the highest ROAS at 17.24× last week—crushing it! For context, your overall ROAS was 6.34×, so this campaign really stood out.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Which campaign had the highest ROAS last week?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1074ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Which campaign had the highest ROAS last week?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.343275338387010441245764736'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for roas by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=6.34327533838701 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 5.406129400923143}, {'date': '2025-10-23', 'value': 5.8664627604890764}, {'date': '2025-10-24', 'value': 6.161505000243192}, {'date': '2025-10-25', 'value': 7.76569736303204}, {'date': '2025-10-26', 'value': 6.6619532432258985}, {'date': '2025-10-27', 'value': 6.218785967772876}, {'date': '2025-10-28', 'value': 6.452658599580624}] breakdown=[{'label': 'Summer Sale Campaign', 'value': 17.238995169897283, 'spend': 474.11, 'clicks': 1122, 'conversions': 61.0, 'revenue': 8173.18, 'impressions': 33284}] workspace_avg=6.34327533838701
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Summer Sale Campaign had the highest ROAS at 17.24× last week—crushing it! For context, your overall ROAS was 6.34×, so this campaign really stood out.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1236ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2520ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Summer Sale Campaign had the highest ROAS at 17.24× last week—crushing it! For context, your overall ROAS was 6.34×, so this campaign really stood out.'
```

---

## Test 11: What's my ROAS for Google campaigns only?

**Answer**:
> Your ROAS for Google campaigns was 6.77× last week.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': 'google', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's my ROAS for Google campaigns only?", 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 895ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': 'google', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider='google', level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's my ROAS for Google campaigns only?", timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=google, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('28160.8500'), 'revenue': Decimal('190536.2100'), 'clicks': 70200, 'impressions': 2024276, 'conversions': Decimal('7089.5500'), 'leads': Decimal('3378.2800'), 'installs': 1728, 'purchases': 850, 'visitors': 48129, 'profit': Decimal('58404.8400')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.765996409909502021423359025'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=6.765996409909502 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 5.65032716431317}, {'date': '2025-10-23', 'value': 6.200168474255028}, {'date': '2025-10-24', 'value': 6.772585360904613}, {'date': '2025-10-25', 'value': 8.136396579214379}, {'date': '2025-10-26', 'value': 7.445626515365965}, {'date': '2025-10-27', 'value': 6.979547407619593}, {'date': '2025-10-28', 'value': 6.253761212252494}] breakdown=None workspace_avg=6.34327533838701
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your ROAS for Google campaigns was 6.77× last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 968ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2170ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your ROAS for Google campaigns was 6.77× last week.'
```

---

## Test 12: Which campaign spent the most yesterday?

**Answer**:
> The "Lead Gen - B2B" campaign spent the most yesterday at $175.72—your top performer! For context, this matches your overall average spend of $9,466.45, so it's right on target.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'spend', 'time_range': {'last_n_days': 1, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Which campaign spent the most yesterday?', 'timeframe_description': 'yesterday'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1040ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 28), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='spend', time_range=TimeRange(last_n_days=1, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Which campaign spent the most yesterday?', timeframe_description='yesterday'))
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
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The "Lead Gen - B2B" campaign spent the most yesterday at $175.72—your top performer! For context, this matches your overall average spend of $9,466.45, so it's right on target.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1402ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2677ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The "Lead Gen - B2B" campaign spent the most yesterday at $175.72—your top performer! For context, this matches your overall average spend of $9,466.45, so it's right on target.'
```

---

## Test 13: List all active campaigns

**Answer**:
> Here are your 10 campaigns:
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.ENTITIES: 'entities'>, 'metric': None, 'time_range': None, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': 'campaign', 'entity_ids': None, 'status': 'active', 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'List all active campaigns', 'timeframe_description': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 983ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: None
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: campaign
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'entities': [{'name': 'App Install Campaign', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Black Friday Deals', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Brand Awareness', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'General Conversions', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Holiday Sale - Purchases', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Lead Gen - B2B', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Mobile Game Installs', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Newsletter Signup Campaign', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Product Launch Teaser', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Summer Sale Campaign', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}]}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your 10 campaigns:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1088ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your 10 campaigns:
```

---

## Test 14: Which ad has the highest CTR?

**Answer**:
> The Carousel Ad - Evening Audience - Summer Sale Campaign had the highest CTR at 4.5% last week—your top performer! For context, your overall CTR was 2.5%, so this ad really stood out.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'ctr', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Which ad has the highest CTR?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1085ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='ad', breakdown='ad', derived='ctr', need_timeseries=True, need_previous=False, base_measures=['clicks', 'impressions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='ctr', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Which ad has the highest CTR?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['ctr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for ctr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for ctr: 0.025313548925062414
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'ctr': MetricValue(value=0.025313548925062414, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.025313548925062414
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for ctr by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.025313548925062414 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 0.02509519127689}, {'date': '2025-10-23', 'value': 0.024331210344251276}, {'date': '2025-10-24', 'value': 0.025365635577885168}, {'date': '2025-10-25', 'value': 0.02567302059562307}, {'date': '2025-10-26', 'value': 0.02518955349620893}, {'date': '2025-10-27', 'value': 0.025784767865353792}, {'date': '2025-10-28', 'value': 0.0257844613799273}] breakdown=[{'label': 'Carousel Ad - Evening Audience - Summer Sale Campaign', 'value': 0.04516129032258064, 'spend': 535.33, 'clicks': 1806, 'conversions': 92.0, 'revenue': 13134.73, 'impressions': 39990}] workspace_avg=0.025313548925062414
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Carousel Ad - Evening Audience - Summer Sale Campaign had the highest CTR at 4.5% last week—your top performer! For context, your overall CTR was 2.5%, so this ad really stood out.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1065ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2392ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Carousel Ad - Evening Audience - Summer Sale Campaign had the highest CTR at 4.5% last week—your top performer! For context, your overall CTR was 2.5%, so this ad really stood out.'
```

---

## Test 15: Show me campaigns with ROAS above 4

**Answer**:
> Last week, your ROAS was 6.34×, which is right at the average for your campaigns. However, the Summer Sale Campaign was the standout, crushing it with a ROAS of 17.24×!

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'roas', 'operator': '>', 'value': 4}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Show me campaigns with ROAS above 4', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1166ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'roas', 'operator': '>', 'value': 4}]}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'roas', 'operator': '>', 'value': 4}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Show me campaigns with ROAS above 4', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.343275338387010441245764736'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for roas by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=6.34327533838701 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 5.406129400923143}, {'date': '2025-10-23', 'value': 5.8664627604890764}, {'date': '2025-10-24', 'value': 6.161505000243192}, {'date': '2025-10-25', 'value': 7.76569736303204}, {'date': '2025-10-26', 'value': 6.6619532432258985}, {'date': '2025-10-27', 'value': 6.218785967772876}, {'date': '2025-10-28', 'value': 6.452658599580624}] breakdown=[{'label': 'Summer Sale Campaign', 'value': 17.238995169897283, 'spend': 474.11, 'clicks': 1122, 'conversions': 61.0, 'revenue': 8173.18, 'impressions': 33284}, {'label': 'Black Friday Deals', 'value': 15.538023421381455, 'spend': 344.13, 'clicks': 658, 'conversions': 34.0, 'revenue': 5347.1, 'impressions': 34236}, {'label': 'General Conversions', 'value': 15.161493020280695, 'spend': 265.77, 'clicks': 554, 'conversions': 50.92, 'revenue': 4029.47, 'impressions': 25870}, {'label': 'Blog Content Promotion', 'value': 9.338649324662331, 'spend': 499.75, 'clicks': 795, 'conversions': 87.63, 'revenue': 4666.99, 'impressions': 44601}, {'label': 'Website Traffic Push', 'value': 8.78933733296973, 'spend': 513.38, 'clicks': 1339, 'conversions': 90.13, 'revenue': 4512.27, 'impressions': 37902}, {'label': 'Holiday Sale - Purchases', 'value': 7.809964230965764, 'spend': 391.4, 'clicks': 696, 'conversions': 30.0, 'revenue': 3056.82, 'impressions': 37036}] workspace_avg=6.34327533838701
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Last week, your ROAS was 6.34×, which is right at the average for your campaigns. However, the Summer Sale Campaign was the standout, crushing it with a ROAS of 17.24×!'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1440ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2837ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Last week, your ROAS was 6.34×, which is right at the average for your campaigns. However, the Summer Sale Campaign was the standout, crushing it with a ROAS of 17.24×!'
```

---

## Test 16: Which campaign generated the most leads?

**Answer**:
> The "Lead Gen - B2B" campaign generated the most leads last week with 253—your top performer! Overall, you had 5,044 leads, which was right on par with your average.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'leads', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Which campaign generated the most leads?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1713ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['leads'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='leads', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Which campaign generated the most leads?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['leads']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for leads
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for leads: 5044.47
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'leads': MetricValue(value=5044.47, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 5044.47
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for leads by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=5044.47 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 879.78}, {'date': '2025-10-23', 'value': 660.36}, {'date': '2025-10-24', 'value': 742.53}, {'date': '2025-10-25', 'value': 632.93}, {'date': '2025-10-26', 'value': 705.34}, {'date': '2025-10-27', 'value': 809.71}, {'date': '2025-10-28', 'value': 613.82}] breakdown=[{'label': 'Lead Gen - B2B', 'value': 252.59, 'spend': 749.92, 'clicks': 1419, 'conversions': 252.59, 'revenue': 1333.37, 'impressions': 45072}] workspace_avg=5044.47
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The "Lead Gen - B2B" campaign generated the most leads last week with 253—your top performer! Overall, you had 5,044 leads, which was right on par with your average.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 2142ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 4068ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The "Lead Gen - B2B" campaign generated the most leads last week with 253—your top performer! Overall, you had 5,044 leads, which was right on par with your average.'
```

---

## Test 17: Rank platforms by cost per conversion

**Answer**:
> Google had the lowest CPA at $3.97 last week, making it the most cost-efficient platform. Your overall CPA was $5.28, which is right at the average for your workspace.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpa', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'provider', 'breakdown': 'provider', 'top_n': 10, 'sort_order': 'asc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Rank platforms by cost per conversion', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1272ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='provider', breakdown='provider', derived='cpa', need_timeseries=True, need_previous=False, base_measures=['conversions', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=10, sort_order='asc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpa', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='provider', breakdown='provider', top_n=10, sort_order='asc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Rank platforms by cost per conversion', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpa']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpa
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpa: 5.277661300643196041287150457
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpa': MetricValue(value=Decimal('5.277661300643196041287150457'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 5.277661300643196041287150457
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpa by provider
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: asc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=5.277661300643196 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 5.077859116939377}, {'date': '2025-10-23', 'value': 5.403955094991365}, {'date': '2025-10-24', 'value': 5.03652698118533}, {'date': '2025-10-25', 'value': 4.962549765203165}, {'date': '2025-10-26', 'value': 5.654007994334908}, {'date': '2025-10-27', 'value': 5.345895624028586}, {'date': '2025-10-28', 'value': 5.52150227183911}] breakdown=[{'label': 'ProviderEnum.google', 'value': 3.9721632543673433, 'spend': 28160.85, 'clicks': 70200, 'conversions': 7089.55, 'revenue': 190536.21, 'impressions': 2024276}, {'label': 'ProviderEnum.meta', 'value': 5.310546715933942, 'spend': 17605.79, 'clicks': 34180, 'conversions': 3315.25, 'revenue': 166555.54, 'impressions': 1761164}, {'label': 'ProviderEnum.tiktok', 'value': 8.938337382606596, 'spend': 12582.14, 'clicks': 25524, 'conversions': 1407.66, 'revenue': 10309.01, 'impressions': 1034212}, {'label': 'ProviderEnum.other', 'value': 9.996856535098086, 'spend': 8459.34, 'clicks': 17148, 'conversions': 846.2, 'revenue': 56381.54, 'impressions': 989569}] workspace_avg=5.277661300643196
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Google had the lowest CPA at $3.97 last week, making it the most cost-efficient platform. Your overall CPA was $5.28, which is right at the average for your workspace.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1214ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2834ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Google had the lowest CPA at $3.97 last week, making it the most cost-efficient platform. Your overall CPA was $5.28, which is right at the average for your workspace.'
```

---

## Test 18: give me a breakdown of holiday campaign performance

**Answer**:
> Here's a breakdown of the holiday campaign performance from last week:

1. **Weekend Audience - Holiday Sale - Purchases**: This segment generated a revenue of $21,607.82. With a spend of $1,536.08, it achieved 3,222 clicks and 157 conversions from 152,246 impressions.

2. **Morning Audience - Holiday Sale - Purchases**: This group brought in $19,313.02 in revenue. It had a spend of $1,633.69, resulting in 2,813 clicks and 137 conversions from 152,828 impressions.

3. **Evening Audience - Holiday Sale - Purchases**: The evening audience contributed $14,546.16 to the revenue. The spend was $1,190.64, with 2,504 clicks and 106 conversions from 129,461 impressions.

Overall, we analyzed three segments in this breakdown, each contributing significantly to the holiday campaign's success.

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
  "question": "give me a breakdown of holiday campaign performance",
  "timeframe_description": "last week"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'give me a breakdown of holiday campaign performance', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1421ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Holiday Sale', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='give me a breakdown of holiday campaign performance', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('4360.4100'), 'revenue': Decimal('55467.0000'), 'clicks': 8539, 'impressions': 434535, 'conversions': Decimal('400.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 400, 'visitors': 7814, 'profit': Decimal('16818.4700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=55467.0, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for revenue by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 5, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity by name (exact first): 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using partial match for 'Holiday Sale': Holiday Sale - Purchases (f2d2c4ee-b550-43ff-a17b-3b6a559a61b9)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Routing named-entity same-level breakdown to child level: campaign→adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=55467.0 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 3474.11}, {'date': '2025-10-23', 'value': 6087.89}, {'date': '2025-10-24', 'value': 7677.52}, {'date': '2025-10-25', 'value': 13568.85}, {'date': '2025-10-26', 'value': 8844.85}, {'date': '2025-10-27', 'value': 7895.61}, {'date': '2025-10-28', 'value': 7918.17}] breakdown=[{'label': 'Weekend Audience - Holiday Sale - Purchases', 'value': 21607.82, 'spend': 1536.08, 'clicks': 3222, 'conversions': 157.0, 'revenue': 21607.82, 'impressions': 152246}, {'label': 'Morning Audience - Holiday Sale - Purchases', 'value': 19313.02, 'spend': 1633.69, 'clicks': 2813, 'conversions': 137.0, 'revenue': 19313.02, 'impressions': 152828}, {'label': 'Evening Audience - Holiday Sale - Purchases', 'value': 14546.16, 'spend': 1190.64, 'clicks': 2504, 'conversions': 106.0, 'revenue': 14546.16, 'impressions': 129461}] workspace_avg=423782.3
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here's a breakdown of the holiday campaign performance from last week:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1797ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3772ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here's a breakdown of the holiday campaign performance from last week:
```

---

## Test 19: what is my average order value?

**Answer**:
> Your average order value was $33.48 last week.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'aov', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'what is my average order value?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1173ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived='aov', need_timeseries=True, need_previous=False, base_measures=['purchases', 'revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='aov', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='what is my average order value?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['aov']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for aov
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for aov: 33.47765877272949901490363119
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'aov': MetricValue(value=Decimal('33.47765877272949901490363119'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 33.47765877272949901490363119
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=33.4776587727295 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 27.451563465831594}, {'date': '2025-10-23', 'value': 31.70210132412205}, {'date': '2025-10-24', 'value': 31.032586178433156}, {'date': '2025-10-25', 'value': 38.53765962555349}, {'date': '2025-10-26', 'value': 37.6667368950846}, {'date': '2025-10-27', 'value': 33.244980691887385}, {'date': '2025-10-28', 'value': 35.62836911698659}] breakdown=None workspace_avg=33.4776587727295
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your average order value was $33.48 last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 933ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2284ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your average order value was $33.48 last week.'
```

---

## Test 20: give me a list of the top 5 adsets last week by revenue

**Answer**:
> Here are the top 5 ad sets from last week based on revenue:

1. **Morning Audience - Summer Sale Campaign**: This ad set generated $10,549.28 in revenue. It had a spend of $512.05, with 1,445 clicks and 74 conversions from 38,994 impressions.

2. **Evening Audience - Summer Sale Campaign**: Bringing in $6,974.45, this ad set had a spend of $452.04. It achieved 1,207 clicks and 69 conversions from 39,264 impressions.

3. **Weekend Audience - Summer Sale Campaign**: This ad set earned $5,094.99 in revenue. It spent $356.75, with 826 clicks and 38 conversions from 26,496 impressions.

4. **Morning Audience - Website Traffic Push**: With a revenue of $4,877.75, this ad set spent $608.10. It garnered 1,583 clicks and 103.26 conversions from 43,936 impressions.

5. **Weekend Audience - Website Traffic Push**: This ad set generated $4,834.28 in revenue. It had a spend of $600.59, with 1,523 clicks and 82.13 conversions from 43,688 impressions.

In total, these five ad sets were the top performers in terms of revenue for last week.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'give me a list of the top 5 adsets last week by revenue', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1092ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='adset', breakdown='adset', derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='give me a list of the top 5 adsets last week by revenue', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=423782.3, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for revenue by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 5, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=423782.3 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 53736.71}, {'date': '2025-10-23', 'value': 55066.55}, {'date': '2025-10-24', 'value': 58272.68}, {'date': '2025-10-25', 'value': 69017.48}, {'date': '2025-10-26', 'value': 64361.53}, {'date': '2025-10-27', 'value': 62243.58}, {'date': '2025-10-28', 'value': 61083.77}] breakdown=[{'label': 'Morning Audience - Summer Sale Campaign', 'value': 10549.28, 'spend': 512.05, 'clicks': 1445, 'conversions': 74.0, 'revenue': 10549.28, 'impressions': 38994}, {'label': 'Evening Audience - Summer Sale Campaign', 'value': 6974.45, 'spend': 452.04, 'clicks': 1207, 'conversions': 69.0, 'revenue': 6974.45, 'impressions': 39264}, {'label': 'Weekend Audience - Summer Sale Campaign', 'value': 5094.99, 'spend': 356.75, 'clicks': 826, 'conversions': 38.0, 'revenue': 5094.99, 'impressions': 26496}, {'label': 'Morning Audience - Website Traffic Push', 'value': 4877.75, 'spend': 608.1, 'clicks': 1583, 'conversions': 103.26, 'revenue': 4877.75, 'impressions': 43936}, {'label': 'Weekend Audience - Website Traffic Push', 'value': 4834.28, 'spend': 600.59, 'clicks': 1523, 'conversions': 82.13, 'revenue': 4834.28, 'impressions': 43688}] workspace_avg=423782.3
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are the top 5 ad sets from last week based on revenue:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 4829ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 6146ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are the top 5 ad sets from last week based on revenue:
```

---

## Test 21: What was the revenue for the Holiday Sale campaign last week?

**Answer**:
> The revenue for the Holiday Sale campaign was $55,467.00 last week.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'What was the revenue for the Holiday Sale campaign last week?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 865ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Holiday Sale', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='What was the revenue for the Holiday Sale campaign last week?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('4360.4100'), 'revenue': Decimal('55467.0000'), 'clicks': 8539, 'impressions': 434535, 'conversions': Decimal('400.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 400, 'visitors': 7814, 'profit': Decimal('16818.4700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=55467.0, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=55467.0 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 3474.11}, {'date': '2025-10-23', 'value': 6087.89}, {'date': '2025-10-24', 'value': 7677.52}, {'date': '2025-10-25', 'value': 13568.85}, {'date': '2025-10-26', 'value': 8844.85}, {'date': '2025-10-27', 'value': 7895.61}, {'date': '2025-10-28', 'value': 7918.17}] breakdown=None workspace_avg=423782.3
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The revenue for the Holiday Sale campaign was $55,467.00 last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 719ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1873ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The revenue for the Holiday Sale campaign was $55,467.00 last week.'
```

---

## Test 22: wich day had the lowest cpc on holiday sale campaign?

**Answer**:
> The day with the lowest CPC for your Holiday Sale campaign was October 28, with a CPC of $0.43—your best performer last week! For a bit of context, your overall CPC was $0.51, which was above the workspace average of $0.45.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpc', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'day', 'breakdown': 'day', 'top_n': 1, 'sort_order': 'asc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'wich day had the lowest cpc on holiday sale campaign?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1225ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='day', breakdown='day', derived='cpc', need_timeseries=True, need_previous=False, base_measures=['clicks', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, top_n=1, sort_order='asc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpc', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='day', breakdown='day', top_n=1, sort_order='asc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Holiday Sale', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='wich day had the lowest cpc on holiday sale campaign?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('4360.4100'), 'revenue': Decimal('55467.0000'), 'clicks': 8539, 'impressions': 434535, 'conversions': Decimal('400.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 400, 'visitors': 7814, 'profit': Decimal('16818.4700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4543162962761472132306939042
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.5106464457196393020259983605'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4543162962761472132306939042
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
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.5106464457196394 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 0.6297817047817048}, {'date': '2025-10-23', 'value': 0.5838761238761239}, {'date': '2025-10-24', 'value': 0.5469913589945011}, {'date': '2025-10-25', 'value': 0.4448214285714286}, {'date': '2025-10-26', 'value': 0.48990188679245283}, {'date': '2025-10-27', 'value': 0.49471641791044774}, {'date': '2025-10-28', 'value': 0.4349238578680203}] breakdown=[{'label': '2025-10-28', 'value': 0.4349238578680203, 'spend': 514.08, 'clicks': 1182, 'conversions': 58.0, 'revenue': 7918.17, 'impressions': 60498}] workspace_avg=0.4543162962761472
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The day with the lowest CPC for your Holiday Sale campaign was October 28, with a CPC of $0.43—your best performer last week! For a bit of context, your overall CPC was $0.51, which was above the workspace average of $0.45.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1741ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3367ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The day with the lowest CPC for your Holiday Sale campaign was October 28, with a CPC of $0.43—your best performer last week! For a bit of context, your overall CPC was $0.51, which was above the workspace average of $0.45.'
```

---

## Test 23: roas last month for holiday sale campaign?

**Answer**:
> The ROAS for your Holiday Sale campaign was 11.77× in the last 30 days, which is excellent! That's way above your workspace average of 6.25×, so you're definitely seeing some strong returns.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 30, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'roas last month for holiday sale campaign?', 'timeframe_description': 'last month'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1026ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 29), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=30, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Holiday Sale', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='roas last month for holiday sale campaign?', timeframe_description='last month'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 29) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-29 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('19116.5500'), 'revenue': Decimal('224923.9900'), 'clicks': 37634, 'impressions': 1930318, 'conversions': Decimal('1689.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 1689, 'visitors': 34440, 'profit': Decimal('67851.8900')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.253916739497948732440957250
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('11.76593004490873091640489523'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.253916739497948732440957250
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=11.76593004490873 previous=None delta_pct=None timeseries=[{'date': '2025-09-29', 'value': 15.863174413391123}, {'date': '2025-09-30', 'value': 13.55246392507884}, {'date': '2025-10-01', 'value': 7.177618988826471}, {'date': '2025-10-02', 'value': 10.228955569942336}, {'date': '2025-10-03', 'value': 11.537762082672263}, {'date': '2025-10-04', 'value': 7.671428571428572}, {'date': '2025-10-05', 'value': 10.535678458072262}, {'date': '2025-10-06', 'value': 14.716415767668895}, {'date': '2025-10-07', 'value': 17.40983043866273}, {'date': '2025-10-08', 'value': 11.625562233809656}, {'date': '2025-10-09', 'value': 9.116998321745385}, {'date': '2025-10-10', 'value': 11.527550295126549}, {'date': '2025-10-11', 'value': 9.457304797596557}, {'date': '2025-10-12', 'value': 8.24877934077486}, {'date': '2025-10-13', 'value': 11.293794209053452}, {'date': '2025-10-14', 'value': 9.653219618721597}, {'date': '2025-10-15', 'value': 12.897733043399002}, {'date': '2025-10-16', 'value': 12.626816060922895}, {'date': '2025-10-17', 'value': 14.587122097878737}, {'date': '2025-10-18', 'value': 10.562403136110857}, {'date': '2025-10-19', 'value': 9.783093281976685}, {'date': '2025-10-20', 'value': 11.692413312962927}, {'date': '2025-10-21', 'value': 16.5265587759796}, {'date': '2025-10-22', 'value': 5.734274160270694}, {'date': '2025-10-23', 'value': 10.416264586113678}, {'date': '2025-10-24', 'value': 11.025850183823529}, {'date': '2025-10-25', 'value': 20.950575919463915}, {'date': '2025-10-26', 'value': 13.625908922849396}, {'date': '2025-10-27', 'value': 11.910351173595608}, {'date': '2025-10-28', 'value': 15.402602707749766}] breakdown=None workspace_avg=6.2539167394979485
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The ROAS for your Holiday Sale campaign was 11.77× in the last 30 days, which is excellent! That's way above your workspace average of 6.25×, so you're definitely seeing some strong returns.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1535ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2850ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The ROAS for your Holiday Sale campaign was 11.77× in the last 30 days, which is excellent! That's way above your workspace average of 6.25×, so you're definitely seeing some strong returns.'
```

---

## Test 24: wich had highest cpc, holiday campaign or app install campaign?

**Answer**:
> Last week, the Holiday Sale campaign had a higher cost per click (CPC) compared to the App Install campaign. Specifically, the CPC for the Holiday Sale was approximately $0.51, while the App Install campaign had a CPC of about $0.42. This means that the Holiday Sale campaign was more expensive per click than the App Install campaign.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.COMPARISON: 'comparison'>, 'metric': None, 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': 'entity_vs_entity', 'comparison_entities': ['Holiday Sale', 'App Install'], 'comparison_metrics': ['cpc'], 'question': 'wich had highest cpc, holiday campaign or app install campaign?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1192ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived='cpc', need_timeseries=True, need_previous=False, base_measures=['clicks', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.COMPARISON: 'comparison'>, metric=None, time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type='entity_vs_entity', comparison_entities=['Holiday Sale', 'App Install'], comparison_metrics=['cpc'], question='wich had highest cpc, holiday campaign or app install campaign?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.dsl.executor:[COMPARISON] Executing comparison plan for type: entity_vs_entity
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('4360.4100'), 'revenue': Decimal('55467.0000'), 'clicks': 8539, 'impressions': 434535, 'conversions': Decimal('400.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 400, 'visitors': 7814, 'profit': Decimal('16818.4700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4543162962761472132306939042
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.5106464457196393020259983605'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4543162962761472132306939042
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=App Install
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('6969.9000'), 'revenue': Decimal('3892.5800'), 'clicks': 16415, 'impressions': 483719, 'conversions': Decimal('1650.0000'), 'leads': Decimal('0'), 'installs': 1650, 'purchases': 0, 'visitors': 0, 'profit': Decimal('1107.1000')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4543162962761472132306939042
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.4246055437100213219616204691'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4543162962761472132306939042
INFO:app.dsl.executor:[COMPARISON] Completed execution for 2 items
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'comparison': [{'entity': 'Holiday Sale', 'cpc': Decimal('0.5106464457196393020259983605')}, {'entity': 'App Install', 'cpc': Decimal('0.4246055437100213219616204691')}], 'comparison_type': 'entity_vs_entity', 'metrics': ['cpc'], 'query_type': 'comparison'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Last week, the Holiday Sale campaign had a higher cost per click (CPC) compared to the App Install campaign. Specifically, the CPC for the Holiday Sale was approximately $0.51, while the App Install campaign had a CPC of about $0.42. This means that the Holiday Sale campaign was more expensive per click than the App Install campaign.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1823ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3330ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Last week, the Holiday Sale campaign had a higher cost per click (CPC) compared to the App Install campaign. Specifically, the CPC for the Holiday Sale was approximately $0.51, while the App Install campaign had a CPC of about $0.42. This means that the Holiday Sale campaign was more expensive per click than the App Install campaign.'
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.ENTITIES: 'entities'>, 'metric': None, 'time_range': None, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': 'google', 'level': 'campaign', 'entity_ids': None, 'status': 'active', 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'wich google campaigns are live?', 'timeframe_description': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 944ms
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
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1098ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your 4 campaigns:
```

---

## Test 26: what is my revenue this month?

**Answer**:
> Your revenue is $1,673,577.62 from October 01 to 28.

**DSL**:
```json
{
  "query_type": "metrics",
  "metric": "revenue",
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-28"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 10, 1), 'end': datetime.date(2025, 10, 28)}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'what is my revenue this month?', 'timeframe_description': 'this month'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 904ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 28)), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='what is my revenue this month?', timeframe_description='this month'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('268552.7100'), 'revenue': Decimal('1673577.6200'), 'clicks': 593809, 'impressions': 23402098, 'conversions': Decimal('50121.9000'), 'leads': Decimal('19608.4100'), 'installs': 11733, 'purchases': 6792, 'visitors': 426056, 'profit': Decimal('503172.8300')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 1673577.62
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=1673577.62, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 1673577.62
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=1673577.62 previous=None delta_pct=None timeseries=[{'date': '2025-10-01', 'value': 49365.68}, {'date': '2025-10-02', 'value': 65908.62}, {'date': '2025-10-03', 'value': 53994.53}, {'date': '2025-10-04', 'value': 48803.74}, {'date': '2025-10-05', 'value': 58890.95}, {'date': '2025-10-06', 'value': 55470.63}, {'date': '2025-10-07', 'value': 64787.44}, {'date': '2025-10-08', 'value': 53135.75}, {'date': '2025-10-09', 'value': 66933.45}, {'date': '2025-10-10', 'value': 59678.51}, {'date': '2025-10-11', 'value': 55425.65}, {'date': '2025-10-12', 'value': 59306.71}, {'date': '2025-10-13', 'value': 64012.74}, {'date': '2025-10-14', 'value': 59715.32}, {'date': '2025-10-15', 'value': 63802.67}, {'date': '2025-10-16', 'value': 62097.11}, {'date': '2025-10-17', 'value': 61303.64}, {'date': '2025-10-18', 'value': 58373.07}, {'date': '2025-10-19', 'value': 62505.74}, {'date': '2025-10-20', 'value': 58520.16}, {'date': '2025-10-21', 'value': 67763.21}, {'date': '2025-10-22', 'value': 53736.71}, {'date': '2025-10-23', 'value': 55066.55}, {'date': '2025-10-24', 'value': 58272.68}, {'date': '2025-10-25', 'value': 69017.48}, {'date': '2025-10-26', 'value': 64361.53}, {'date': '2025-10-27', 'value': 62243.58}, {'date': '2025-10-28', 'value': 61083.77}] breakdown=None workspace_avg=1673577.62
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your revenue is $1,673,577.62 from October 01 to 28.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1133ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2224ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your revenue is $1,673,577.62 from October 01 to 28.'
```

---

## Test 27: what was my revenue last month?

**Answer**:
> Your revenue was $1,803,597.38 in the last 30 days.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 30, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'what was my revenue last month?', 'timeframe_description': 'last month'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 902ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 29), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=30, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='what was my revenue last month?', timeframe_description='last month'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 29) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-29 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('288394.8500'), 'revenue': Decimal('1803597.3800'), 'clicks': 636793, 'impressions': 25074397, 'conversions': Decimal('53834.9400'), 'leads': Decimal('21204.2800'), 'installs': 12443, 'purchases': 7325, 'visitors': 457334, 'profit': Decimal('541927.9400')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 1803597.38
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=1803597.38, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 1803597.38
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=1803597.38 previous=None delta_pct=None timeseries=[{'date': '2025-09-29', 'value': 62494.18}, {'date': '2025-09-30', 'value': 67525.58}, {'date': '2025-10-01', 'value': 49365.68}, {'date': '2025-10-02', 'value': 65908.62}, {'date': '2025-10-03', 'value': 53994.53}, {'date': '2025-10-04', 'value': 48803.74}, {'date': '2025-10-05', 'value': 58890.95}, {'date': '2025-10-06', 'value': 55470.63}, {'date': '2025-10-07', 'value': 64787.44}, {'date': '2025-10-08', 'value': 53135.75}, {'date': '2025-10-09', 'value': 66933.45}, {'date': '2025-10-10', 'value': 59678.51}, {'date': '2025-10-11', 'value': 55425.65}, {'date': '2025-10-12', 'value': 59306.71}, {'date': '2025-10-13', 'value': 64012.74}, {'date': '2025-10-14', 'value': 59715.32}, {'date': '2025-10-15', 'value': 63802.67}, {'date': '2025-10-16', 'value': 62097.11}, {'date': '2025-10-17', 'value': 61303.64}, {'date': '2025-10-18', 'value': 58373.07}, {'date': '2025-10-19', 'value': 62505.74}, {'date': '2025-10-20', 'value': 58520.16}, {'date': '2025-10-21', 'value': 67763.21}, {'date': '2025-10-22', 'value': 53736.71}, {'date': '2025-10-23', 'value': 55066.55}, {'date': '2025-10-24', 'value': 58272.68}, {'date': '2025-10-25', 'value': 69017.48}, {'date': '2025-10-26', 'value': 64361.53}, {'date': '2025-10-27', 'value': 62243.58}, {'date': '2025-10-28', 'value': 61083.77}] breakdown=None workspace_avg=1803597.38
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your revenue was $1,803,597.38 in the last 30 days.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 911ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1997ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your revenue was $1,803,597.38 in the last 30 days.'
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
  "timeframe_description": "last year"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 365, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'what is my revenue this year?', 'timeframe_description': 'last year'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1058ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2024, 10, 29), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=365, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='what is my revenue this year?', timeframe_description='last year'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2024, 10, 29) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2024-10-29 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('288394.8500'), 'revenue': Decimal('1803597.3800'), 'clicks': 636793, 'impressions': 25074397, 'conversions': Decimal('53834.9400'), 'leads': Decimal('21204.2800'), 'installs': 12443, 'purchases': 7325, 'visitors': 457334, 'profit': Decimal('541927.9400')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 1803597.38
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=1803597.38, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 1803597.38
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=1803597.38 previous=None delta_pct=None timeseries=[{'date': '2025-09-29', 'value': 62494.18}, {'date': '2025-09-30', 'value': 67525.58}, {'date': '2025-10-01', 'value': 49365.68}, {'date': '2025-10-02', 'value': 65908.62}, {'date': '2025-10-03', 'value': 53994.53}, {'date': '2025-10-04', 'value': 48803.74}, {'date': '2025-10-05', 'value': 58890.95}, {'date': '2025-10-06', 'value': 55470.63}, {'date': '2025-10-07', 'value': 64787.44}, {'date': '2025-10-08', 'value': 53135.75}, {'date': '2025-10-09', 'value': 66933.45}, {'date': '2025-10-10', 'value': 59678.51}, {'date': '2025-10-11', 'value': 55425.65}, {'date': '2025-10-12', 'value': 59306.71}, {'date': '2025-10-13', 'value': 64012.74}, {'date': '2025-10-14', 'value': 59715.32}, {'date': '2025-10-15', 'value': 63802.67}, {'date': '2025-10-16', 'value': 62097.11}, {'date': '2025-10-17', 'value': 61303.64}, {'date': '2025-10-18', 'value': 58373.07}, {'date': '2025-10-19', 'value': 62505.74}, {'date': '2025-10-20', 'value': 58520.16}, {'date': '2025-10-21', 'value': 67763.21}, {'date': '2025-10-22', 'value': 53736.71}, {'date': '2025-10-23', 'value': 55066.55}, {'date': '2025-10-24', 'value': 58272.68}, {'date': '2025-10-25', 'value': 69017.48}, {'date': '2025-10-26', 'value': 64361.53}, {'date': '2025-10-27', 'value': 62243.58}, {'date': '2025-10-28', 'value': 61083.77}] breakdown=None workspace_avg=1803597.38
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your revenue was $1,803,597.38 in the last 365 days.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 773ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2027ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your revenue was $1,803,597.38 in the last 365 days.'
```

---

## Test 29: How does this week compare to last week?

**Answer**:
> This week, the revenue was $423,782.30, which is slightly lower compared to last week's revenue of $434,365.60. This represents a decrease of about 2.4%. So, last week performed better in terms of revenue.

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
  "timeframe_description": "this week"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.COMPARISON: 'comparison'>, 'metric': None, 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': True, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': 'time_vs_time', 'comparison_entities': None, 'comparison_metrics': ['revenue'], 'question': 'How does this week compare to last week?', 'timeframe_description': 'this week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 962ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=True, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.COMPARISON: 'comparison'>, metric=None, time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=True, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type='time_vs_time', comparison_entities=None, comparison_metrics=['revenue'], question='How does this week compare to last week?', timeframe_description='this week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.dsl.executor:[COMPARISON] Executing comparison plan for type: time_vs_time
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=423782.3, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 15) end=datetime.date(2025, 10, 21)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-15 to 2025-10-21
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('68068.3200'), 'revenue': Decimal('434365.6000'), 'clicks': 151565, 'impressions': 5890606, 'conversions': Decimal('12518.3200'), 'leads': Decimal('4660.8500'), 'installs': 3063, 'purchases': 1838, 'visitors': 106763, 'profit': Decimal('133316.9700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 434365.6
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=434365.6, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 434365.6
INFO:app.dsl.executor:[COMPARISON] time_vs_time computed for metrics=['revenue']
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'comparison': [{'period': 'current', 'revenue': 423782.3}, {'period': 'previous', 'revenue': 434365.6}], 'comparison_type': 'time_vs_time', 'metrics': ['revenue'], 'query_type': 'comparison'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'This week, the revenue was $423,782.30, which is slightly lower compared to last week's revenue of $434,365.60. This represents a decrease of about 2.4%. So, last week performed better in terms of revenue.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1638ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2800ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'This week, the revenue was $423,782.30, which is slightly lower compared to last week's revenue of $434,365.60. This represents a decrease of about 2.4%. So, last week performed better in terms of revenue.'
```

---

## Test 30: Compare Google vs Meta performance

**Answer**:
> In the last 30 days, when comparing Google and Meta based on key performance metrics, we see some interesting differences.

Starting with ROAS (Return on Ad Spend), Meta outperformed Google with a ROAS of 9.13 compared to Google's 6.60. This indicates that Meta was more efficient in generating revenue for each dollar spent on advertising.

Looking at revenue, Google generated a higher total revenue of $795,759.56, whereas Meta brought in $711,664.45. Despite Meta's higher efficiency in ad spend, Google's overall revenue was greater.

In terms of ad spend, Google spent significantly more, with a total of $120,567.37 compared to Meta's $77,949.85. This higher spend contributed to Google's larger revenue figure, despite Meta's better ROAS.

Overall, while Meta achieved a higher ROAS, Google led in total revenue, albeit with a higher ad spend.

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
    "roas",
    "revenue",
    "spend"
  ],
  "question": "Compare Google vs Meta performance",
  "timeframe_description": "last month"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.COMPARISON: 'comparison'>, 'metric': None, 'time_range': {'last_n_days': 30, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': 'provider_vs_provider', 'comparison_entities': None, 'comparison_metrics': ['roas', 'revenue', 'spend'], 'question': 'Compare Google vs Meta performance', 'timeframe_description': 'last month'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1240ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 29), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.COMPARISON: 'comparison'>, metric=None, time_range=TimeRange(last_n_days=30, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type='provider_vs_provider', comparison_entities=None, comparison_metrics=['roas', 'revenue', 'spend'], question='Compare Google vs Meta performance', timeframe_description='last month'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.dsl.executor:[COMPARISON] Executing comparison plan for type: provider_vs_provider
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['roas', 'revenue', 'spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 29) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=google, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-29 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('120567.3700'), 'revenue': Decimal('795759.5600'), 'clicks': 299647, 'impressions': 8582601, 'conversions': Decimal('29502.4400'), 'leads': Decimal('13729.8600'), 'installs': 7432, 'purchases': 3530, 'visitors': 203005, 'profit': Decimal('240976.8100')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.253916739497948732440957250
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.600123731653099839533698048'), previous=None, delta_pct=None), 'revenue': MetricValue(value=795759.56, previous=None, delta_pct=None), 'spend': MetricValue(value=120567.37, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.253916739497948732440957250
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['roas', 'revenue', 'spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 29) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=meta, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-29 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('77949.8500'), 'revenue': Decimal('711664.4500'), 'clicks': 154017, 'impressions': 7779210, 'conversions': Decimal('14610.9200'), 'leads': Decimal('7474.4200'), 'installs': 0, 'purchases': 3795, 'visitors': 139991, 'profit': Decimal('212632.6800')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.253916739497948732440957250
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('9.129773181090149628254576500'), previous=None, delta_pct=None), 'revenue': MetricValue(value=711664.45, previous=None, delta_pct=None), 'spend': MetricValue(value=77949.85, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.253916739497948732440957250
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['roas', 'revenue', 'spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 29) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=tiktok, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-29 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('52179.5600'), 'revenue': Decimal('46686.7700'), 'clicks': 107337, 'impressions': 4355569, 'conversions': Decimal('6009.1400'), 'leads': Decimal('0'), 'installs': 5011, 'purchases': 0, 'visitors': 48380, 'profit': Decimal('13983.0900')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.253916739497948732440957250
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('0.8947329184071310681807205733'), previous=None, delta_pct=None), 'revenue': MetricValue(value=46686.77, previous=None, delta_pct=None), 'spend': MetricValue(value=52179.56, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.253916739497948732440957250
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['roas', 'revenue', 'spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 29) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=other, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-29 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('37698.0700'), 'revenue': Decimal('249486.6000'), 'clicks': 75792, 'impressions': 4357017, 'conversions': Decimal('3712.4400'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 0, 'visitors': 65958, 'profit': Decimal('74335.3600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.253916739497948732440957250
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.618020498131601962646894125'), previous=None, delta_pct=None), 'revenue': MetricValue(value=249486.6, previous=None, delta_pct=None), 'spend': MetricValue(value=37698.07, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.253916739497948732440957250
INFO:app.dsl.executor:[COMPARISON] Completed execution for 4 items
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'comparison': [{'provider': 'google', 'roas': Decimal('6.600123731653099839533698048'), 'revenue': 795759.56, 'spend': 120567.37}, {'provider': 'meta', 'roas': Decimal('9.129773181090149628254576500'), 'revenue': 711664.45, 'spend': 77949.85}, {'provider': 'tiktok', 'roas': Decimal('0.8947329184071310681807205733'), 'revenue': 46686.77, 'spend': 52179.56}, {'provider': 'other', 'roas': Decimal('6.618020498131601962646894125'), 'revenue': 249486.6, 'spend': 37698.07}], 'comparison_type': 'provider_vs_provider', 'metrics': ['roas', 'revenue', 'spend'], 'query_type': 'comparison'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'In the last 30 days, when comparing Google and Meta based on key performance metrics, we see some interesting differences.
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 4274ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 5889ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'In the last 30 days, when comparing Google and Meta based on key performance metrics, we see some interesting differences.
```

---

## Test 31: Is my ROAS improving or declining?

**Answer**:
> Your ROAS was 6.34× last week, which is pretty much on par with the workspace average. It did decline slightly by 0.6% from the previous week, so it's holding steady but not improving.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': True, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Is my ROAS improving or declining?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 840ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived='roas', need_timeseries=True, need_previous=True, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=True, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Is my ROAS improving or declining?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Previous period dates: 2025-10-15 to 2025-10-21
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Previous period totals: {'spend': Decimal('68068.3200'), 'revenue': Decimal('434365.6000'), 'clicks': 151565, 'impressions': 5890606, 'conversions': Decimal('12518.3200'), 'leads': Decimal('4660.8500'), 'installs': 3063, 'purchases': 1838, 'visitors': 106763, 'profit': Decimal('133316.9700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.343275338387010441245764736'), previous=Decimal('6.381318063968671475952396063'), delta_pct=Decimal('-0.005961578031420281536894466984'))}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=6.34327533838701 previous=6.3813180639686715 delta_pct=-0.005961578031420282 timeseries=[{'date': '2025-10-22', 'value': 5.406129400923143}, {'date': '2025-10-23', 'value': 5.8664627604890764}, {'date': '2025-10-24', 'value': 6.161505000243192}, {'date': '2025-10-25', 'value': 7.76569736303204}, {'date': '2025-10-26', 'value': 6.6619532432258985}, {'date': '2025-10-27', 'value': 6.218785967772876}, {'date': '2025-10-28', 'value': 6.452658599580624}] breakdown=None workspace_avg=6.34327533838701
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your ROAS was 6.34× last week, which is pretty much on par with the workspace average. It did decline slightly by 0.6% from the previous week, so it's holding steady but not improving.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1105ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2153ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your ROAS was 6.34× last week, which is pretty much on par with the workspace average. It did decline slightly by 0.6% from the previous week, so it's holding steady but not improving.'
```

---

## Test 32: compare holiday campaign performance to app install campaign performance

**Answer**:
> In comparing the performance of the Holiday Sale campaign to the App Install campaign over the last week, we can see some clear differences across key metrics.

Firstly, looking at Return on Ad Spend (ROAS), the Holiday Sale campaign significantly outperformed the App Install campaign. The Holiday Sale achieved a ROAS of 12.72, meaning for every dollar spent, it generated $12.72 in revenue. In contrast, the App Install campaign had a ROAS of just 0.56, indicating it generated only $0.56 for every dollar spent.

In terms of revenue, the Holiday Sale campaign again came out on top, bringing in $55,467 compared to the App Install campaign's $3,892.58. This shows that the Holiday Sale campaign was much more effective in driving revenue.

Finally, when we look at spend, the Holiday Sale campaign spent $4,360.41, which is less than the $6,969.90 spent on the App Install campaign. Despite spending less, the Holiday Sale campaign achieved much higher returns.

Overall, the Holiday Sale campaign performed better across all metrics, making it the more successful campaign for the last week.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.COMPARISON: 'comparison'>, 'metric': None, 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': 'entity_vs_entity', 'comparison_entities': ['Holiday Sale', 'App Install'], 'comparison_metrics': ['roas', 'revenue', 'spend'], 'question': 'compare holiday campaign performance to app install campaign performance', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1818ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.COMPARISON: 'comparison'>, metric=None, time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type='entity_vs_entity', comparison_entities=['Holiday Sale', 'App Install'], comparison_metrics=['roas', 'revenue', 'spend'], question='compare holiday campaign performance to app install campaign performance', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.dsl.executor:[COMPARISON] Executing comparison plan for type: entity_vs_entity
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['roas', 'revenue', 'spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('4360.4100'), 'revenue': Decimal('55467.0000'), 'clicks': 8539, 'impressions': 434535, 'conversions': Decimal('400.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 400, 'visitors': 7814, 'profit': Decimal('16818.4700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('12.72059278829284402154843237'), previous=None, delta_pct=None), 'revenue': MetricValue(value=55467.0, previous=None, delta_pct=None), 'spend': MetricValue(value=4360.41, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['roas', 'revenue', 'spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=App Install
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('6969.9000'), 'revenue': Decimal('3892.5800'), 'clicks': 16415, 'impressions': 483719, 'conversions': Decimal('1650.0000'), 'leads': Decimal('0'), 'installs': 1650, 'purchases': 0, 'visitors': 0, 'profit': Decimal('1107.1000')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('0.5584843398040144047977732823'), previous=None, delta_pct=None), 'revenue': MetricValue(value=3892.58, previous=None, delta_pct=None), 'spend': MetricValue(value=6969.9, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.343275338387010441245764736
INFO:app.dsl.executor:[COMPARISON] Completed execution for 2 items
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'comparison': [{'entity': 'Holiday Sale', 'roas': Decimal('12.72059278829284402154843237'), 'revenue': 55467.0, 'spend': 4360.41}, {'entity': 'App Install', 'roas': Decimal('0.5584843398040144047977732823'), 'revenue': 3892.58, 'spend': 6969.9}], 'comparison_type': 'entity_vs_entity', 'metrics': ['roas', 'revenue', 'spend'], 'query_type': 'comparison'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'In comparing the performance of the Holiday Sale campaign to the App Install campaign over the last week, we can see some clear differences across key metrics.
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 6135ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 8301ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'In comparing the performance of the Holiday Sale campaign to the App Install campaign over the last week, we can see some clear differences across key metrics.
```

---

## Test 33: Which campaign had the highest ROAS last week?

**Answer**:
> The Summer Sale Campaign had the highest ROAS at 17.24× last week—crushing it as your top performer! For context, your overall ROAS was 6.34×, so this campaign really stood out.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Which campaign had the highest ROAS last week?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1057ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Which campaign had the highest ROAS last week?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.343275338387010441245764736'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for roas by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=6.34327533838701 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 5.406129400923143}, {'date': '2025-10-23', 'value': 5.8664627604890764}, {'date': '2025-10-24', 'value': 6.161505000243192}, {'date': '2025-10-25', 'value': 7.76569736303204}, {'date': '2025-10-26', 'value': 6.6619532432258985}, {'date': '2025-10-27', 'value': 6.218785967772876}, {'date': '2025-10-28', 'value': 6.452658599580624}] breakdown=[{'label': 'Summer Sale Campaign', 'value': 17.238995169897283, 'spend': 474.11, 'clicks': 1122, 'conversions': 61.0, 'revenue': 8173.18, 'impressions': 33284}] workspace_avg=6.34327533838701
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Summer Sale Campaign had the highest ROAS at 17.24× last week—crushing it as your top performer! For context, your overall ROAS was 6.34×, so this campaign really stood out.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1374ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2667ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Summer Sale Campaign had the highest ROAS at 17.24× last week—crushing it as your top performer! For context, your overall ROAS was 6.34×, so this campaign really stood out.'
```

---

## Test 34: Show me top 5 campaigns by revenue

**Answer**:
> Here are the top 5 campaigns by revenue from last week:

1. **Summer Sale Campaign**: This campaign led the pack with a revenue of $8,173.18.
2. **Black Friday Deals**: Coming in second, this campaign generated $5,347.10 in revenue.
3. **Blog Content Promotion**: This campaign brought in $4,666.99.
4. **Website Traffic Push**: Close behind, this campaign earned $4,512.27.
5. **General Conversions**: Rounding out the list, this campaign achieved $4,029.47 in revenue.

In total, we looked at 5 campaigns to determine these top performers.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Show me top 5 campaigns by revenue', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1263ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Show me top 5 campaigns by revenue', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=423782.3, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for revenue by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 5, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=423782.3 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 53736.71}, {'date': '2025-10-23', 'value': 55066.55}, {'date': '2025-10-24', 'value': 58272.68}, {'date': '2025-10-25', 'value': 69017.48}, {'date': '2025-10-26', 'value': 64361.53}, {'date': '2025-10-27', 'value': 62243.58}, {'date': '2025-10-28', 'value': 61083.77}] breakdown=[{'label': 'Summer Sale Campaign', 'value': 8173.18, 'spend': 474.11, 'clicks': 1122, 'conversions': 61.0, 'revenue': 8173.18, 'impressions': 33284}, {'label': 'Black Friday Deals', 'value': 5347.1, 'spend': 344.13, 'clicks': 658, 'conversions': 34.0, 'revenue': 5347.1, 'impressions': 34236}, {'label': 'Blog Content Promotion', 'value': 4666.99, 'spend': 499.75, 'clicks': 795, 'conversions': 87.63, 'revenue': 4666.99, 'impressions': 44601}, {'label': 'Website Traffic Push', 'value': 4512.27, 'spend': 513.38, 'clicks': 1339, 'conversions': 90.13, 'revenue': 4512.27, 'impressions': 37902}, {'label': 'General Conversions', 'value': 4029.47, 'spend': 265.77, 'clicks': 554, 'conversions': 50.92, 'revenue': 4029.47, 'impressions': 25870}] workspace_avg=423782.3
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are the top 5 campaigns by revenue from last week:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 3375ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 4851ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are the top 5 campaigns by revenue from last week:
```

---

## Test 35: List all active campaigns

**Answer**:
> Here are your 10 campaigns:
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.ENTITIES: 'entities'>, 'metric': None, 'time_range': None, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': 'campaign', 'entity_ids': None, 'status': 'active', 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'List all active campaigns', 'timeframe_description': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 894ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: None
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: campaign
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'entities': [{'name': 'App Install Campaign', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Black Friday Deals', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Brand Awareness', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'General Conversions', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Holiday Sale - Purchases', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Lead Gen - B2B', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Mobile Game Installs', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Newsletter Signup Campaign', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Product Launch Teaser', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}, {'name': 'Summer Sale Campaign', 'status': 'active', 'level': <LevelEnum.campaign: 'campaign'>}]}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your 10 campaigns:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1003ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your 10 campaigns:
```

---

## Test 36: Which adset had the highest cpc last week?

**Answer**:
> The "Weekend Audience - Black Friday Deals" adset had the highest CPC at $0.71 last week—your worst performer. For context, your overall average CPC was $0.45.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpc', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Which adset had the highest cpc last week?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 926ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='adset', breakdown='adset', derived='cpc', need_timeseries=True, need_previous=False, base_measures=['clicks', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpc', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Which adset had the highest cpc last week?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4543162962761472132306939042
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.4543162962761472132306939042'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4543162962761472132306939042
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpc by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.4543162962761472 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 0.4630559955278114}, {'date': '2025-10-23', 'value': 0.46385995255979445}, {'date': '2025-10-24', 'value': 0.44097263020469063}, {'date': '2025-10-25', 'value': 0.4323966137978009}, {'date': '2025-10-26', 'value': 0.4615891065456283}, {'date': '2025-10-27', 'value': 0.45648818753990694}, {'date': '2025-10-28', 'value': 0.4619357829502757}] breakdown=[{'label': 'Weekend Audience - Black Friday Deals', 'value': 0.7054907539118065, 'spend': 495.96, 'clicks': 703, 'conversions': 31.0, 'revenue': 3972.96, 'impressions': 49702}] workspace_avg=0.4543162962761472
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The "Weekend Audience - Black Friday Deals" adset had the highest CPC at $0.71 last week—your worst performer. For context, your overall average CPC was $0.45.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1089ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2209ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The "Weekend Audience - Black Friday Deals" adset had the highest CPC at $0.71 last week—your worst performer. For context, your overall average CPC was $0.45.'
```

---

## Test 37: Which adset had the highest cpc last week?

**Answer**:
> The Weekend Audience - Black Friday Deals adset had the highest CPC at $0.71 last week—your worst performer. For context, your overall average CPC was $0.45, so this adset was quite a bit higher than the norm.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpc', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Which adset had the highest cpc last week?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1078ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='adset', breakdown='adset', derived='cpc', need_timeseries=True, need_previous=False, base_measures=['clicks', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpc', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Which adset had the highest cpc last week?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4543162962761472132306939042
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.4543162962761472132306939042'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4543162962761472132306939042
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpc by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.4543162962761472 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 0.4630559955278114}, {'date': '2025-10-23', 'value': 0.46385995255979445}, {'date': '2025-10-24', 'value': 0.44097263020469063}, {'date': '2025-10-25', 'value': 0.4323966137978009}, {'date': '2025-10-26', 'value': 0.4615891065456283}, {'date': '2025-10-27', 'value': 0.45648818753990694}, {'date': '2025-10-28', 'value': 0.4619357829502757}] breakdown=[{'label': 'Weekend Audience - Black Friday Deals', 'value': 0.7054907539118065, 'spend': 495.96, 'clicks': 703, 'conversions': 31.0, 'revenue': 3972.96, 'impressions': 49702}] workspace_avg=0.4543162962761472
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Weekend Audience - Black Friday Deals adset had the highest CPC at $0.71 last week—your worst performer. For context, your overall average CPC was $0.45, so this adset was quite a bit higher than the norm.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1460ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2773ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Weekend Audience - Black Friday Deals adset had the highest CPC at $0.71 last week—your worst performer. For context, your overall average CPC was $0.45, so this adset was quite a bit higher than the norm.'
```

---

## Test 38: Which adset had the lowest ctr last week?

**Answer**:
> The Weekend Audience - Black Friday Deals adset had the lowest CTR at 1.4% last week—definitely needs some attention. For context, your overall CTR was 2.5%, so this adset is underperforming compared to the average.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'ctr', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 1, 'sort_order': 'asc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Which adset had the lowest ctr last week?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 847ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='adset', breakdown='adset', derived='ctr', need_timeseries=True, need_previous=False, base_measures=['clicks', 'impressions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='asc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='ctr', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=1, sort_order='asc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Which adset had the lowest ctr last week?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['ctr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for ctr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for ctr: 0.025313548925062414
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'ctr': MetricValue(value=0.025313548925062414, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.025313548925062414
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for ctr by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: asc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.025313548925062414 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 0.02509519127689}, {'date': '2025-10-23', 'value': 0.024331210344251276}, {'date': '2025-10-24', 'value': 0.025365635577885168}, {'date': '2025-10-25', 'value': 0.02567302059562307}, {'date': '2025-10-26', 'value': 0.02518955349620893}, {'date': '2025-10-27', 'value': 0.025784767865353792}, {'date': '2025-10-28', 'value': 0.0257844613799273}] breakdown=[{'label': 'Weekend Audience - Black Friday Deals', 'value': 0.01414430002816788, 'spend': 495.96, 'clicks': 703, 'conversions': 31.0, 'revenue': 3972.96, 'impressions': 49702}] workspace_avg=0.025313548925062414
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Weekend Audience - Black Friday Deals adset had the lowest CTR at 1.4% last week—definitely needs some attention. For context, your overall CTR was 2.5%, so this adset is underperforming compared to the average.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1258ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2320ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Weekend Audience - Black Friday Deals adset had the lowest CTR at 1.4% last week—definitely needs some attention. For context, your overall CTR was 2.5%, so this adset is underperforming compared to the average.'
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
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "what is my total CVR last month?",
  "timeframe_description": "last month"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cvr', 'time_range': {'last_n_days': 30, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'what is my total CVR last month?', 'timeframe_description': 'last month'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1170ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 29), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived='cvr', need_timeseries=True, need_previous=False, base_measures=['clicks', 'conversions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cvr', time_range=TimeRange(last_n_days=30, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='what is my total CVR last month?', timeframe_description='last month'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cvr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 29) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-29 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('288394.8500'), 'revenue': Decimal('1803597.3800'), 'clicks': 636793, 'impressions': 25074397, 'conversions': Decimal('53834.9400'), 'leads': Decimal('21204.2800'), 'installs': 12443, 'purchases': 7325, 'visitors': 457334, 'profit': Decimal('541927.9400')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cvr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cvr: 0.08454072202426848285078510599
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cvr': MetricValue(value=Decimal('0.08454072202426848285078510599'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.08454072202426848285078510599
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.08454072202426849 previous=None delta_pct=None timeseries=[{'date': '2025-09-29', 'value': 0.08648376685019936}, {'date': '2025-09-30', 'value': 0.08628399342945793}, {'date': '2025-10-01', 'value': 0.08748204456094365}, {'date': '2025-10-02', 'value': 0.08277745636872047}, {'date': '2025-10-03', 'value': 0.0860803078636893}, {'date': '2025-10-04', 'value': 0.08223615830501699}, {'date': '2025-10-05', 'value': 0.0804194368836732}, {'date': '2025-10-06', 'value': 0.0852395409869809}, {'date': '2025-10-07', 'value': 0.08661708093721782}, {'date': '2025-10-08', 'value': 0.08577834572490706}, {'date': '2025-10-09', 'value': 0.08876994084961462}, {'date': '2025-10-10', 'value': 0.08366620713424092}, {'date': '2025-10-11', 'value': 0.08273183089671188}, {'date': '2025-10-12', 'value': 0.08234864395945576}, {'date': '2025-10-13', 'value': 0.07736416477129138}, {'date': '2025-10-14', 'value': 0.09271550497866288}, {'date': '2025-10-15', 'value': 0.08358447274770556}, {'date': '2025-10-16', 'value': 0.0854068278142611}, {'date': '2025-10-17', 'value': 0.08938895781637717}, {'date': '2025-10-18', 'value': 0.07938539304610734}, {'date': '2025-10-19', 'value': 0.08434605688000354}, {'date': '2025-10-20', 'value': 0.08004111718397433}, {'date': '2025-10-21', 'value': 0.07565790645879733}, {'date': '2025-10-22', 'value': 0.09119118606167893}, {'date': '2025-10-23', 'value': 0.08583712196086184}, {'date': '2025-10-24', 'value': 0.0875549027836061}, {'date': '2025-10-25', 'value': 0.08713194512017125}, {'date': '2025-10-26', 'value': 0.08163927376970856}, {'date': '2025-10-27', 'value': 0.08539040408647268}, {'date': '2025-10-28', 'value': 0.08366125018298931}] breakdown=None workspace_avg=0.08454072202426849
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your total CVR was 8.5% in the last 30 days.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1251ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2596ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your total CVR was 8.5% in the last 30 days.'
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
  "timeframe_description": "last month"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cvr', 'time_range': {'last_n_days': 30, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': 'google', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'what is my cvr on google last month?', 'timeframe_description': 'last month'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 848ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 29), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived='cvr', need_timeseries=True, need_previous=False, base_measures=['clicks', 'conversions'], filters={'provider': 'google', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cvr', time_range=TimeRange(last_n_days=30, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider='google', level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='what is my cvr on google last month?', timeframe_description='last month'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cvr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 29) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=google, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-29 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('120567.3700'), 'revenue': Decimal('795759.5600'), 'clicks': 299647, 'impressions': 8582601, 'conversions': Decimal('29502.4400'), 'leads': Decimal('13729.8600'), 'installs': 7432, 'purchases': 3530, 'visitors': 203005, 'profit': Decimal('240976.8100')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cvr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cvr: 0.08454072202426848285078510599
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cvr': MetricValue(value=Decimal('0.09845731811097724989737924958'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.08454072202426848285078510599
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.09845731811097724 previous=None delta_pct=None timeseries=[{'date': '2025-09-29', 'value': 0.09875663229552507}, {'date': '2025-09-30', 'value': 0.09855470327008478}, {'date': '2025-10-01', 'value': 0.10772485521805933}, {'date': '2025-10-02', 'value': 0.10065891472868217}, {'date': '2025-10-03', 'value': 0.10608279545960383}, {'date': '2025-10-04', 'value': 0.10179387019230769}, {'date': '2025-10-05', 'value': 0.08903241046962108}, {'date': '2025-10-06', 'value': 0.10280654861343134}, {'date': '2025-10-07', 'value': 0.0996785676892472}, {'date': '2025-10-08', 'value': 0.0961483230987246}, {'date': '2025-10-09', 'value': 0.09913387291841101}, {'date': '2025-10-10', 'value': 0.09323698384201078}, {'date': '2025-10-11', 'value': 0.09735136423209818}, {'date': '2025-10-12', 'value': 0.10102682067345341}, {'date': '2025-10-13', 'value': 0.084277195344811}, {'date': '2025-10-14', 'value': 0.11318226894089647}, {'date': '2025-10-15', 'value': 0.09451615916308612}, {'date': '2025-10-16', 'value': 0.10257534795233804}, {'date': '2025-10-17', 'value': 0.10074461136512083}, {'date': '2025-10-18', 'value': 0.0939423566554639}, {'date': '2025-10-19', 'value': 0.0962782671873581}, {'date': '2025-10-20', 'value': 0.09387871342416797}, {'date': '2025-10-21', 'value': 0.08062324799102971}, {'date': '2025-10-22', 'value': 0.11142799270812234}, {'date': '2025-10-23', 'value': 0.09775048690759576}, {'date': '2025-10-24', 'value': 0.10142236699239957}, {'date': '2025-10-25', 'value': 0.09855603448275863}, {'date': '2025-10-26', 'value': 0.0984038575083645}, {'date': '2025-10-27', 'value': 0.09945663111289998}, {'date': '2025-10-28', 'value': 0.09980872069107363}] breakdown=None workspace_avg=0.08454072202426849
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your CVR was 9.8% in the last 30 days.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1049ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2107ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your CVR was 9.8% in the last 30 days.'
```

---

## Test 41: how much did i spent last month?

**Answer**:
> You spent $288,394.85 in the last 30 days.

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
  "timeframe_description": "last month"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'spend', 'time_range': {'last_n_days': 30, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'how much did i spent last month?', 'timeframe_description': 'last month'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 920ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 29), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='spend', time_range=TimeRange(last_n_days=30, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='how much did i spent last month?', timeframe_description='last month'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 29) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-29 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('288394.8500'), 'revenue': Decimal('1803597.3800'), 'clicks': 636793, 'impressions': 25074397, 'conversions': Decimal('53834.9400'), 'leads': Decimal('21204.2800'), 'installs': 12443, 'purchases': 7325, 'visitors': 457334, 'profit': Decimal('541927.9400')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 288394.85
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=288394.85, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 288394.85
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=288394.85 previous=None delta_pct=None timeseries=[{'date': '2025-09-29', 'value': 9905.34}, {'date': '2025-09-30', 'value': 9936.8}, {'date': '2025-10-01', 'value': 8967.77}, {'date': '2025-10-02', 'value': 9536.8}, {'date': '2025-10-03', 'value': 8453.33}, {'date': '2025-10-04', 'value': 9493.13}, {'date': '2025-10-05', 'value': 10412.57}, {'date': '2025-10-06', 'value': 9041.32}, {'date': '2025-10-07', 'value': 10133.74}, {'date': '2025-10-08', 'value': 9551.81}, {'date': '2025-10-09', 'value': 10079.91}, {'date': '2025-10-10', 'value': 10308.26}, {'date': '2025-10-11', 'value': 8213.11}, {'date': '2025-10-12', 'value': 9737.22}, {'date': '2025-10-13', 'value': 10139.91}, {'date': '2025-10-14', 'value': 9607.39}, {'date': '2025-10-15', 'value': 9542.43}, {'date': '2025-10-16', 'value': 9848.22}, {'date': '2025-10-17', 'value': 9940.11}, {'date': '2025-10-18', 'value': 9405.73}, {'date': '2025-10-19', 'value': 10312.94}, {'date': '2025-10-20', 'value': 9364.22}, {'date': '2025-10-21', 'value': 9654.67}, {'date': '2025-10-22', 'value': 9939.96}, {'date': '2025-10-23', 'value': 9386.67}, {'date': '2025-10-24', 'value': 9457.54}, {'date': '2025-10-25', 'value': 8887.48}, {'date': '2025-10-26', 'value': 9661.06}, {'date': '2025-10-27', 'value': 10008.96}, {'date': '2025-10-28', 'value': 9466.45}] breakdown=None workspace_avg=288394.85
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'You spent $288,394.85 in the last 30 days.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 708ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1795ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'You spent $288,394.85 in the last 30 days.'
```

---

## Test 42: wich campaign had the highest spend?

**Answer**:
> The "Lead Gen - B2B" campaign had the highest spend at $749.92 last week—your top performer! For context, your overall spend was $66,808.12, which was right on average.

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
  "timeframe_description": "last week"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'spend', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'wich campaign had the highest spend?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 907ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='spend', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='wich campaign had the highest spend?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 66808.12
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=66808.12, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 66808.12
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for spend by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=66808.12 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 9939.96}, {'date': '2025-10-23', 'value': 9386.67}, {'date': '2025-10-24', 'value': 9457.54}, {'date': '2025-10-25', 'value': 8887.48}, {'date': '2025-10-26', 'value': 9661.06}, {'date': '2025-10-27', 'value': 10008.96}, {'date': '2025-10-28', 'value': 9466.45}] breakdown=[{'label': 'Lead Gen - B2B', 'value': 749.92, 'spend': 749.92, 'clicks': 1419, 'conversions': 252.59, 'revenue': 1333.37, 'impressions': 45072}] workspace_avg=66808.12
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The "Lead Gen - B2B" campaign had the highest spend at $749.92 last week—your top performer! For context, your overall spend was $66,808.12, which was right on average.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1209ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2319ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The "Lead Gen - B2B" campaign had the highest spend at $749.92 last week—your top performer! For context, your overall spend was $66,808.12, which was right on average.'
```

---

## Test 43: wich ads in that campaign performed best?

**Answer**:
> The Video Ad - Evening Audience - Lead Gen - B2B had the highest spend at $690.99 last week—your best performer! For context, your overall campaign spend was $6,774.36, which is below the workspace average of $66,808.12.

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
  "timeframe_description": "last week"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'spend', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Lead Gen - B2B', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'wich ads in that campaign performed best?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1513ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='ad', breakdown='ad', derived=None, need_timeseries=True, need_previous=False, base_measures=['spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Lead Gen - B2B', 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='spend', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Lead Gen - B2B', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='wich ads in that campaign performed best?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Lead Gen - B2B
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Lead Gen - B2B'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Lead Gen - B2B (ID: 8e751a39-6438-486a-a116-c899baed8949, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Lead Gen - B2B
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 8e751a39-6438-486a-a116-c899baed8949 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Lead Gen - B2B': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('6774.3600'), 'revenue': Decimal('16552.3600'), 'clicks': 16872, 'impressions': 461562, 'conversions': Decimal('3125.6900'), 'leads': Decimal('3125.6900'), 'installs': 0, 'purchases': 0, 'visitors': 15144, 'profit': Decimal('4813.2600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 66808.12
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=6774.36, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 66808.12
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Lead Gen - B2B'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Lead Gen - B2B (ID: 8e751a39-6438-486a-a116-c899baed8949, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Lead Gen - B2B
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 8e751a39-6438-486a-a116-c899baed8949 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Lead Gen - B2B': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for spend by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Lead Gen - B2B
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity by name (exact first): 'Lead Gen - B2B'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Lead Gen - B2B'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Lead Gen - B2B (ID: 8e751a39-6438-486a-a116-c899baed8949, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Lead Gen - B2B
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 8e751a39-6438-486a-a116-c899baed8949 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Lead Gen - B2B': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=6774.36 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 1251.9}, {'date': '2025-10-23', 'value': 797.26}, {'date': '2025-10-24', 'value': 1030.75}, {'date': '2025-10-25', 'value': 756.49}, {'date': '2025-10-26', 'value': 892.61}, {'date': '2025-10-27', 'value': 1090.11}, {'date': '2025-10-28', 'value': 955.24}] breakdown=[{'label': 'Video Ad - Evening Audience - Lead Gen - B2B', 'value': 690.99, 'spend': 690.99, 'clicks': 1397, 'conversions': 223.83, 'revenue': 1439.26, 'impressions': 48344}] workspace_avg=66808.12
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Video Ad - Evening Audience - Lead Gen - B2B had the highest spend at $690.99 last week—your best performer! For context, your overall campaign spend was $6,774.36, which is below the workspace average of $66,808.12.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1194ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3131ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Video Ad - Evening Audience - Lead Gen - B2B had the highest spend at $690.99 last week—your best performer! For context, your overall campaign spend was $6,774.36, which is below the workspace average of $66,808.12.'
```

---

## Test 44: how many conversions did that campaign deliver?

**Answer**:
> The campaign delivered 3,126 conversions last week.

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
  "timeframe_description": "last week"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'conversions', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': 'campaign', 'entity_ids': None, 'status': None, 'entity_name': 'Lead Gen - B2B', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'how many conversions did that campaign deliver?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1140ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['conversions'], filters={'provider': None, 'level': 'campaign', 'entity_ids': None, 'status': None, 'entity_name': 'Lead Gen - B2B', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='conversions', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level='campaign', entity_ids=None, status=None, entity_name='Lead Gen - B2B', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='how many conversions did that campaign deliver?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['conversions']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=campaign, status=None, entity_name=Lead Gen - B2B
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Lead Gen - B2B'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Lead Gen - B2B (ID: 8e751a39-6438-486a-a116-c899baed8949, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Lead Gen - B2B
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 8e751a39-6438-486a-a116-c899baed8949 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Lead Gen - B2B': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('6774.3600'), 'revenue': Decimal('16552.3600'), 'clicks': 16872, 'impressions': 461562, 'conversions': Decimal('3125.6900'), 'leads': Decimal('3125.6900'), 'installs': 0, 'purchases': 0, 'visitors': 15144, 'profit': Decimal('4813.2600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for conversions
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for conversions: 12658.66
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'conversions': MetricValue(value=3125.69, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 12658.66
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Lead Gen - B2B'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Lead Gen - B2B (ID: 8e751a39-6438-486a-a116-c899baed8949, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Lead Gen - B2B
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 8e751a39-6438-486a-a116-c899baed8949 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Lead Gen - B2B': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=3125.69 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 586.51}, {'date': '2025-10-23', 'value': 311.48}, {'date': '2025-10-24', 'value': 520.79}, {'date': '2025-10-25', 'value': 371.49}, {'date': '2025-10-26', 'value': 489.45}, {'date': '2025-10-27', 'value': 457.04}, {'date': '2025-10-28', 'value': 388.93}] breakdown=None workspace_avg=12658.66
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The campaign delivered 3,126 conversions last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 813ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2246ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The campaign delivered 3,126 conversions last week.'
```

---

## Test 45: how much revenue in the last week?

**Answer**:
> Your revenue was $423,782.30 last week.

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
  "timeframe_description": "last week"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'how much revenue in the last week?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1103ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='how much revenue in the last week?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=423782.3, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=423782.3 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 53736.71}, {'date': '2025-10-23', 'value': 55066.55}, {'date': '2025-10-24', 'value': 58272.68}, {'date': '2025-10-25', 'value': 69017.48}, {'date': '2025-10-26', 'value': 64361.53}, {'date': '2025-10-27', 'value': 62243.58}, {'date': '2025-10-28', 'value': 61083.77}] breakdown=None workspace_avg=423782.3
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your revenue was $423,782.30 last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 604ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1886ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your revenue was $423,782.30 last week.'
```

---

## Test 46: wich campaign brought in the most?

**Answer**:
> The Summer Sale Campaign brought in the most revenue at $8,173.18 last week—your top performer! For context, your overall revenue was $423,782.30, which was right on average.

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
  "timeframe_description": "last week"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'wich campaign brought in the most?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1105ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='wich campaign brought in the most?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=423782.3, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for revenue by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=423782.3 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 53736.71}, {'date': '2025-10-23', 'value': 55066.55}, {'date': '2025-10-24', 'value': 58272.68}, {'date': '2025-10-25', 'value': 69017.48}, {'date': '2025-10-26', 'value': 64361.53}, {'date': '2025-10-27', 'value': 62243.58}, {'date': '2025-10-28', 'value': 61083.77}] breakdown=[{'label': 'Summer Sale Campaign', 'value': 8173.18, 'spend': 474.11, 'clicks': 1122, 'conversions': 61.0, 'revenue': 8173.18, 'impressions': 33284}] workspace_avg=423782.3
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Summer Sale Campaign brought in the most revenue at $8,173.18 last week—your top performer! For context, your overall revenue was $423,782.30, which was right on average.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1479ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2799ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Summer Sale Campaign brought in the most revenue at $8,173.18 last week—your top performer! For context, your overall revenue was $423,782.30, which was right on average.'
```

---

## Test 47: how many conversions did that campaign deliver?

**Answer**:
> The campaign delivered $98,282.65 in revenue last week.

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
    "entity_name": "Summer Sale Campaign",
    "metric_filters": null
  },
  "thresholds": null,
  "comparison_type": null,
  "comparison_entities": null,
  "comparison_metrics": null,
  "question": "how many conversions did that campaign deliver?",
  "timeframe_description": "last week"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Summer Sale Campaign', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'how many conversions did that campaign deliver?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1259ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Summer Sale Campaign', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Summer Sale Campaign', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='how many conversions did that campaign deliver?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Summer Sale Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Summer Sale Campaign'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Summer Sale Campaign (ID: d02a69cb-5368-488f-93ec-993c747a2299, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Summer Sale Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity d02a69cb-5368-488f-93ec-993c747a2299 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Summer Sale Campaign': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('5962.4200'), 'revenue': Decimal('98282.6500'), 'clicks': 15616, 'impressions': 449445, 'conversions': Decimal('789.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 789, 'visitors': 14324, 'profit': Decimal('30741.9900')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=98282.65, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Summer Sale Campaign'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Summer Sale Campaign (ID: d02a69cb-5368-488f-93ec-993c747a2299, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Summer Sale Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity d02a69cb-5368-488f-93ec-993c747a2299 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Summer Sale Campaign': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=98282.65 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 11349.1}, {'date': '2025-10-23', 'value': 11170.72}, {'date': '2025-10-24', 'value': 14225.01}, {'date': '2025-10-25', 'value': 17943.59}, {'date': '2025-10-26', 'value': 13313.63}, {'date': '2025-10-27', 'value': 17874.28}, {'date': '2025-10-28', 'value': 12406.32}] breakdown=None workspace_avg=423782.3
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The campaign delivered $98,282.65 in revenue last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 777ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2367ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The campaign delivered $98,282.65 in revenue last week.'
```

---

## Test 48: What's my ROAS for active campaigns?

**Answer**:
> Your ROAS for active campaigns was 5.98× last week, which is a bit below the workspace average of 6.34×. The Summer Sale Campaign was the top performer, hitting an impressive 17.24×.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': 'active', 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's my ROAS for active campaigns?", 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1532ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': 'active', 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status='active', entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's my ROAS for active campaigns?", timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=active, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('63619.6100'), 'revenue': Decimal('380617.5200'), 'clicks': 140640, 'impressions': 5482194, 'conversions': Decimal('11876.6000'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 99862, 'profit': Decimal('115394.2500')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('5.982707533101821906798862803'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for roas by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=active, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 5, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=5.982707533101822 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 5.020904357689605}, {'date': '2025-10-23', 'value': 5.521933584995087}, {'date': '2025-10-24', 'value': 5.698221775874147}, {'date': '2025-10-25', 'value': 7.3697316693553345}, {'date': '2025-10-26', 'value': 6.302231907098084}, {'date': '2025-10-27', 'value': 5.995647458989944}, {'date': '2025-10-28', 'value': 6.109445323966241}] breakdown=[{'label': 'Summer Sale Campaign', 'value': 17.238995169897283, 'spend': 474.11, 'clicks': 1122, 'conversions': 61.0, 'revenue': 8173.18, 'impressions': 33284}, {'label': 'Black Friday Deals', 'value': 15.538023421381455, 'spend': 344.13, 'clicks': 658, 'conversions': 34.0, 'revenue': 5347.1, 'impressions': 34236}, {'label': 'General Conversions', 'value': 15.161493020280695, 'spend': 265.77, 'clicks': 554, 'conversions': 50.92, 'revenue': 4029.47, 'impressions': 25870}, {'label': 'Website Traffic Push', 'value': 8.78933733296973, 'spend': 513.38, 'clicks': 1339, 'conversions': 90.13, 'revenue': 4512.27, 'impressions': 37902}, {'label': 'Holiday Sale - Purchases', 'value': 7.809964230965764, 'spend': 391.4, 'clicks': 696, 'conversions': 30.0, 'revenue': 3056.82, 'impressions': 37036}] workspace_avg=6.34327533838701
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your ROAS for active campaigns was 5.98× last week, which is a bit below the workspace average of 6.34×. The Summer Sale Campaign was the top performer, hitting an impressive 17.24×.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1927ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3667ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your ROAS for active campaigns was 5.98× last week, which is a bit below the workspace average of 6.34×. The Summer Sale Campaign was the top performer, hitting an impressive 17.24×.'
```

---

## Test 49: How much did I spend on Meta ads?

**Answer**:
> You spent $17,605.79 on Meta ads last week.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'spend', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': 'meta', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How much did I spend on Meta ads?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 828ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['spend'], filters={'provider': 'meta', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='spend', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider='meta', level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How much did I spend on Meta ads?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=meta, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('17605.7900'), 'revenue': Decimal('166555.5400'), 'clicks': 34180, 'impressions': 1761164, 'conversions': Decimal('3315.2500'), 'leads': Decimal('1666.1900'), 'installs': 0, 'purchases': 867, 'visitors': 31058, 'profit': Decimal('49744.0100')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 66808.12
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=17605.79, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 66808.12
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=17605.79 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 2378.6}, {'date': '2025-10-23', 'value': 2722.94}, {'date': '2025-10-24', 'value': 2394.18}, {'date': '2025-10-25', 'value': 2407.04}, {'date': '2025-10-26', 'value': 2531.83}, {'date': '2025-10-27', 'value': 3054.27}, {'date': '2025-10-28', 'value': 2116.93}] breakdown=None workspace_avg=66808.12
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'You spent $17,605.79 on Meta ads last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 804ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1847ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'You spent $17,605.79 on Meta ads last week.'
```

---

## Test 50: How much revenue on Google last week?

**Answer**:
> Your revenue on Google was $190,536.21 last week.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': 'google', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How much revenue on Google last week?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 2198ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': 'google', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider='google', level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How much revenue on Google last week?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=google, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('28160.8500'), 'revenue': Decimal('190536.2100'), 'clicks': 70200, 'impressions': 2024276, 'conversions': Decimal('7089.5500'), 'leads': Decimal('3378.2800'), 'installs': 1728, 'purchases': 850, 'visitors': 48129, 'profit': Decimal('58404.8400')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=190536.21, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=190536.21 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 23652.1}, {'date': '2025-10-23', 'value': 22964.37}, {'date': '2025-10-24', 'value': 29371.89}, {'date': '2025-10-25', 'value': 30873.15}, {'date': '2025-10-26', 'value': 30248.23}, {'date': '2025-10-27', 'value': 28020.44}, {'date': '2025-10-28', 'value': 25406.03}] breakdown=None workspace_avg=423782.3
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your revenue on Google was $190,536.21 last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 809ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3196ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your revenue on Google was $190,536.21 last week.'
```

---

## Test 51: What's my cost per install?

**Answer**:
> Your cost per install was $22.96 last week.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpi', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's my cost per install?", 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 2729ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived='cpi', need_timeseries=True, need_previous=False, base_measures=['installs', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpi', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's my cost per install?", timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpi']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpi
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpi: 22.95811683848797250859106529
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpi': MetricValue(value=Decimal('22.95811683848797250859106529'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 22.95811683848797250859106529
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=22.95811683848797 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 21.515064935064935}, {'date': '2025-10-23', 'value': 21.931471962616822}, {'date': '2025-10-24', 'value': 20.25169164882227}, {'date': '2025-10-25', 'value': 20.525357967667436}, {'date': '2025-10-26', 'value': 32.74935593220339}, {'date': '2025-10-27', 'value': 26.4088654353562}, {'date': '2025-10-28', 'value': 21.225224215246637}] breakdown=None workspace_avg=22.95811683848797
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your cost per install was $22.96 last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 657ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3566ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your cost per install was $22.96 last week.'
```

---

## Test 52: How many leads did I generate today?

**Answer**:
> You generated 614 leads today.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'leads', 'time_range': {'last_n_days': 1, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How many leads did I generate today?', 'timeframe_description': 'today'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1670ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 28), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['leads'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='leads', time_range=TimeRange(last_n_days=1, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How many leads did I generate today?', timeframe_description='today'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['leads']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 28) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-28 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('9466.4500'), 'revenue': Decimal('61083.7700'), 'clicks': 20493, 'impressions': 794781, 'conversions': Decimal('1714.4700'), 'leads': Decimal('613.8200'), 'installs': 446, 'purchases': 224, 'visitors': 14129, 'profit': Decimal('18180.0800')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for leads
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for leads: 613.82
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'leads': MetricValue(value=613.82, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 613.82
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=613.82 previous=None delta_pct=None timeseries=[{'date': '2025-10-28', 'value': 613.82}] breakdown=None workspace_avg=613.82
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'You generated 614 leads today.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 900ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2745ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'You generated 614 leads today.'
```

---

## Test 53: wich ad had the lowest cpc last week?

**Answer**:
> The Carousel Ad - Evening Audience - Summer Sale Campaign had the lowest CPC at $0.30 last week—your best performer! For context, the overall average CPC was $0.45, so this ad really stood out.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpc', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 1, 'sort_order': 'asc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'wich ad had the lowest cpc last week?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1141ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='ad', breakdown='ad', derived='cpc', need_timeseries=True, need_previous=False, base_measures=['clicks', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='asc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpc', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=1, sort_order='asc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='wich ad had the lowest cpc last week?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4543162962761472132306939042
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.4543162962761472132306939042'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4543162962761472132306939042
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpc by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: asc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.4543162962761472 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 0.4630559955278114}, {'date': '2025-10-23', 'value': 0.46385995255979445}, {'date': '2025-10-24', 'value': 0.44097263020469063}, {'date': '2025-10-25', 'value': 0.4323966137978009}, {'date': '2025-10-26', 'value': 0.4615891065456283}, {'date': '2025-10-27', 'value': 0.45648818753990694}, {'date': '2025-10-28', 'value': 0.4619357829502757}] breakdown=[{'label': 'Carousel Ad - Evening Audience - Summer Sale Campaign', 'value': 0.2964174972314507, 'spend': 535.33, 'clicks': 1806, 'conversions': 92.0, 'revenue': 13134.73, 'impressions': 39990}] workspace_avg=0.4543162962761472
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Carousel Ad - Evening Audience - Summer Sale Campaign had the lowest CPC at $0.30 last week—your best performer! For context, the overall average CPC was $0.45, so this ad really stood out.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1272ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2639ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Carousel Ad - Evening Audience - Summer Sale Campaign had the lowest CPC at $0.30 last week—your best performer! For context, the overall average CPC was $0.45, so this ad really stood out.'
```

---

## Test 54: how much revenue would i have last week if my cpc was 0.20?

**Answer**:
> Your revenue was $423,782.30 last week.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'cpc', 'operator': '=', 'value': 0.2}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'how much revenue would i have last week if my cpc was 0.20?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1001ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'cpc', 'operator': '=', 'value': 0.2}]}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'cpc', 'operator': '=', 'value': 0.2}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='how much revenue would i have last week if my cpc was 0.20?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=423782.3, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=423782.3 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 53736.71}, {'date': '2025-10-23', 'value': 55066.55}, {'date': '2025-10-24', 'value': 58272.68}, {'date': '2025-10-25', 'value': 69017.48}, {'date': '2025-10-26', 'value': 64361.53}, {'date': '2025-10-27', 'value': 62243.58}, {'date': '2025-10-28', 'value': 61083.77}] breakdown=None workspace_avg=423782.3
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your revenue was $423,782.30 last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 625ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1795ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your revenue was $423,782.30 last week.'
```

---

## Test 55: best performing ad set in Holiday Sale campaign yesterday?

**Answer**:
> The Morning Audience - Holiday Sale - Purchases ad set had the lowest ROAS at 11.03× yesterday—your worst performer. For a bit of context, your overall ROAS was 15.40×, which is well above the workspace average of 6.45×.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 1, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'best performing ad set in Holiday Sale campaign yesterday?', 'timeframe_description': 'yesterday'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1025ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 28), end=datetime.date(2025, 10, 28), group_by='adset', breakdown='adset', derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=1, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Holiday Sale', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='best performing ad set in Holiday Sale campaign yesterday?', timeframe_description='yesterday'))
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
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Morning Audience - Holiday Sale - Purchases ad set had the lowest ROAS at 11.03× yesterday—your worst performer. For a bit of context, your overall ROAS was 15.40×, which is well above the workspace average of 6.45×.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1473ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2954ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Morning Audience - Holiday Sale - Purchases ad set had the lowest ROAS at 11.03× yesterday—your worst performer. For a bit of context, your overall ROAS was 15.40×, which is well above the workspace average of 6.45×.'
```

---

## Test 56: all ad sets above roas 4 in the last 3 days

**Answer**:
> In the last 3 days, several ad sets have achieved a ROAS (Return on Ad Spend) above 4. Here's a rundown of those high-performing ad sets:

1. **Morning Audience - Summer Sale Campaign**: This ad set achieved an impressive ROAS of 34.51, with a spend of $194.24, generating $6,703.78 in revenue.

2. **Weekend Audience - General Conversions**: With a ROAS of 17.72, this ad set spent $137.87 and brought in $2,443.37 in revenue.

3. **Evening Audience - Blog Content Promotion**: This set reached a ROAS of 17.64, spending $139.32 and earning $2,457.03 in revenue.

4. **Weekend Audience - Black Friday Deals**: Achieving a ROAS of 13.17, this ad set spent $189.61 and generated $2,497.82 in revenue.

5. **Morning Audience - Black Friday Deals**: With a ROAS of 13.15, this ad set spent $127.08 and brought in $1,671.00 in revenue.

6. **Weekend Audience - Holiday Sale - Purchases**: This ad set achieved a ROAS of 13.05, with a spend of $137.84 and revenue of $1,799.42.

7. **Evening Audience - Holiday Sale - Purchases**: With a ROAS of 11.13, this ad set spent $169.93 and earned $1,891.91 in revenue.

8. **Weekend Audience - Summer Sale Campaign**: This set reached a ROAS of 10.02, spending $196.90 and generating $1,972.16 in revenue.

9. **Morning Audience - General Conversions**: Achieving a ROAS of 8.77, this ad set spent $238.28 and brought in $2,090.84 in revenue.

10. **Weekend Audience - Website Traffic Push**: With a ROAS of 8.51, this ad set spent $258.50 and earned $2,200.62 in revenue.

In total, there are 10 ad sets that have surpassed the ROAS threshold of 4 in the last 3 days. Each of these ad sets has demonstrated strong performance, contributing significantly to your campaign's success.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 3, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'roas', 'operator': '>', 'value': 4}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'all ad sets above roas 4 in the last 3 days', 'timeframe_description': 'last 3 days'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1504ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 26), end=datetime.date(2025, 10, 28), group_by='adset', breakdown='adset', derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'roas', 'operator': '>', 'value': 4}]}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=3, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'roas', 'operator': '>', 'value': 4}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='all ad sets above roas 4 in the last 3 days', timeframe_description='last 3 days'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 26) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-26 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('29136.4700'), 'revenue': Decimal('187688.8800'), 'clicks': 63349, 'impressions': 2476028, 'conversions': Decimal('5295.4500'), 'leads': Decimal('2128.8700'), 'installs': 1120, 'purchases': 758, 'visitors': 46297, 'profit': Decimal('55022.7500')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.441716515418648861718663929
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.441716515418648861718663929'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.441716515418648861718663929
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for roas by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 26) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-26 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=6.441716515418649 previous=None delta_pct=None timeseries=[{'date': '2025-10-26', 'value': 6.6619532432258985}, {'date': '2025-10-27', 'value': 6.218785967772876}, {'date': '2025-10-28', 'value': 6.452658599580624}] breakdown=[{'label': 'Morning Audience - Summer Sale Campaign', 'value': 34.51287067545305, 'spend': 194.24, 'clicks': 710, 'conversions': 41.0, 'revenue': 6703.78, 'impressions': 16441}, {'label': 'Weekend Audience - General Conversions', 'value': 17.72227460651338, 'spend': 137.87, 'clicks': 403, 'conversions': 31.46, 'revenue': 2443.37, 'impressions': 21945}, {'label': 'Evening Audience - Blog Content Promotion', 'value': 17.635874246339363, 'spend': 139.32, 'clicks': 377, 'conversions': 37.97, 'revenue': 2457.03, 'impressions': 16195}, {'label': 'Weekend Audience - Black Friday Deals', 'value': 13.173461315331469, 'spend': 189.61, 'clicks': 286, 'conversions': 15.0, 'revenue': 2497.82, 'impressions': 18734}, {'label': 'Morning Audience - Black Friday Deals', 'value': 13.149197355996224, 'spend': 127.08, 'clicks': 261, 'conversions': 12.0, 'revenue': 1671.0, 'impressions': 14710}, {'label': 'Weekend Audience - Holiday Sale - Purchases', 'value': 13.054410911201392, 'spend': 137.84, 'clicks': 361, 'conversions': 19.0, 'revenue': 1799.42, 'impressions': 16685}, {'label': 'Evening Audience - Holiday Sale - Purchases', 'value': 11.133466721591244, 'spend': 169.93, 'clicks': 363, 'conversions': 15.0, 'revenue': 1891.91, 'impressions': 19049}, {'label': 'Weekend Audience - Summer Sale Campaign', 'value': 10.01604875571356, 'spend': 196.9, 'clicks': 400, 'conversions': 14.0, 'revenue': 1972.16, 'impressions': 12920}, {'label': 'Morning Audience - General Conversions', 'value': 8.77471881819708, 'spend': 238.28, 'clicks': 289, 'conversions': 29.26, 'revenue': 2090.84, 'impressions': 20692}, {'label': 'Weekend Audience - Website Traffic Push', 'value': 8.51303675048356, 'spend': 258.5, 'clicks': 638, 'conversions': 31.53, 'revenue': 2200.62, 'impressions': 17971}] workspace_avg=6.441716515418649
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'In the last 3 days, several ad sets have achieved a ROAS (Return on Ad Spend) above 4. Here's a rundown of those high-performing ad sets:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 7022ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 8733ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'In the last 3 days, several ad sets have achieved a ROAS (Return on Ad Spend) above 4. Here's a rundown of those high-performing ad sets:
```

---

## Test 57: which campaign has the highest ctr?

**Answer**:
> The Website Traffic Push campaign had the highest CTR at 3.5% last week—your top performer! For context, your overall CTR was 2.5%, so this campaign is really standing out.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'ctr', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'which campaign has the highest ctr?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 885ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived='ctr', need_timeseries=True, need_previous=False, base_measures=['clicks', 'impressions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='ctr', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='which campaign has the highest ctr?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['ctr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for ctr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for ctr: 0.025313548925062414
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'ctr': MetricValue(value=0.025313548925062414, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.025313548925062414
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for ctr by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.025313548925062414 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 0.02509519127689}, {'date': '2025-10-23', 'value': 0.024331210344251276}, {'date': '2025-10-24', 'value': 0.025365635577885168}, {'date': '2025-10-25', 'value': 0.02567302059562307}, {'date': '2025-10-26', 'value': 0.02518955349620893}, {'date': '2025-10-27', 'value': 0.025784767865353792}, {'date': '2025-10-28', 'value': 0.0257844613799273}] breakdown=[{'label': 'Website Traffic Push', 'value': 0.03532795103160783, 'spend': 513.38, 'clicks': 1339, 'conversions': 90.13, 'revenue': 4512.27, 'impressions': 37902}] workspace_avg=0.025313548925062414
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Website Traffic Push campaign had the highest CTR at 3.5% last week—your top performer! For context, your overall CTR was 2.5%, so this campaign is really standing out.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1220ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2309ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Website Traffic Push campaign had the highest CTR at 3.5% last week—your top performer! For context, your overall CTR was 2.5%, so this campaign is really standing out.'
```

---

## Test 58: show me adsets with cpc below 1 dollar

**Answer**:
> Your CPC was $0.45 last week, which is right on average for your ad sets. Interestingly, the Weekend Audience - Black Friday Deals ad set had a CPC of $0.71, so it's above your $1 threshold but not your top performer.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpc', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'cpc', 'operator': '<', 'value': 1}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'show me adsets with cpc below 1 dollar', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1057ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='adset', breakdown='adset', derived='cpc', need_timeseries=True, need_previous=False, base_measures=['clicks', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'cpc', 'operator': '<', 'value': 1}]}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpc', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'cpc', 'operator': '<', 'value': 1}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='show me adsets with cpc below 1 dollar', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4543162962761472132306939042
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.4543162962761472132306939042'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4543162962761472132306939042
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpc by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.4543162962761472 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 0.4630559955278114}, {'date': '2025-10-23', 'value': 0.46385995255979445}, {'date': '2025-10-24', 'value': 0.44097263020469063}, {'date': '2025-10-25', 'value': 0.4323966137978009}, {'date': '2025-10-26', 'value': 0.4615891065456283}, {'date': '2025-10-27', 'value': 0.45648818753990694}, {'date': '2025-10-28', 'value': 0.4619357829502757}] breakdown=[{'label': 'Weekend Audience - Black Friday Deals', 'value': 0.7054907539118065, 'spend': 495.96, 'clicks': 703, 'conversions': 31.0, 'revenue': 3972.96, 'impressions': 49702}, {'label': 'Morning Audience - General Conversions', 'value': 0.66078, 'spend': 330.39, 'clicks': 500, 'conversions': 48.43, 'revenue': 3791.72, 'impressions': 32717}, {'label': 'Morning Audience - Holiday Sale - Purchases', 'value': 0.6549925925925926, 'spend': 442.12, 'clicks': 675, 'conversions': 33.0, 'revenue': 4534.1, 'impressions': 38226}, {'label': 'Evening Audience - General Conversions', 'value': 0.6295255474452555, 'spend': 344.98, 'clicks': 548, 'conversions': 45.83, 'revenue': 3596.44, 'impressions': 34426}, {'label': 'Evening Audience - Newsletter Signup Campaign', 'value': 0.5766370558375634, 'spend': 454.39, 'clicks': 788, 'conversions': 136.87, 'revenue': 568.7, 'impressions': 46099}, {'label': 'Evening Audience - Product Launch Teaser', 'value': 0.5677914110429448, 'spend': 277.65, 'clicks': 489, 'conversions': 16.44, 'revenue': 590.73, 'impressions': 30772}, {'label': 'Morning Audience - Black Friday Deals', 'value': 0.5640836940836941, 'spend': 390.91, 'clicks': 693, 'conversions': 27.0, 'revenue': 3826.97, 'impressions': 37082}, {'label': 'Evening Audience - Holiday Sale - Purchases', 'value': 0.5534536891679749, 'spend': 352.55, 'clicks': 637, 'conversions': 32.0, 'revenue': 4083.8, 'impressions': 38193}, {'label': 'Evening Audience - Black Friday Deals', 'value': 0.5527390180878553, 'spend': 427.82, 'clicks': 774, 'conversions': 43.0, 'revenue': 4021.14, 'impressions': 37390}, {'label': 'Weekend Audience - Product Launch Teaser', 'value': 0.5445614035087719, 'spend': 372.48, 'clicks': 684, 'conversions': 22.19, 'revenue': 828.4, 'impressions': 42928}] workspace_avg=0.4543162962761472
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Your CPC was $0.45 last week, which is right on average for your ad sets. Interestingly, the Weekend Audience - Black Friday Deals ad set had a CPC of $0.71, so it's above your $1 threshold but not your top performer.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1433ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2714ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Your CPC was $0.45 last week, which is right on average for your ad sets. Interestingly, the Weekend Audience - Black Friday Deals ad set had a CPC of $0.71, so it's above your $1 threshold but not your top performer.'
```

---

## Test 59: worst performing ad in App Install campaign?

**Answer**:
> The worst performing ad in your App Install campaign last week was the Image Ad - Morning Audience with a CTR of 3.1%—though it's still above your workspace average of 2.5%. Even your "worst" ad is doing pretty well, so overall, you're in a good spot!

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'ctr', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 1, 'sort_order': 'asc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'App Install Campaign', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'worst performing ad in App Install campaign?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1405ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='ad', breakdown='ad', derived='ctr', need_timeseries=True, need_previous=False, base_measures=['clicks', 'impressions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'App Install Campaign', 'metric_filters': None}, top_n=1, sort_order='asc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='ctr', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=1, sort_order='asc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='App Install Campaign', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='worst performing ad in App Install campaign?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['ctr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install Campaign'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install Campaign': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('6969.9000'), 'revenue': Decimal('3892.5800'), 'clicks': 16415, 'impressions': 483719, 'conversions': Decimal('1650.0000'), 'leads': Decimal('0'), 'installs': 1650, 'purchases': 0, 'visitors': 0, 'profit': Decimal('1107.1000')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for ctr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for ctr: 0.025313548925062414
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'ctr': MetricValue(value=0.03393499118289751, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.025313548925062414
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install Campaign'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install Campaign': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for ctr by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: asc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity by name (exact first): 'App Install Campaign'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install Campaign'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install Campaign': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.03393499118289751 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 0.03263327948303716}, {'date': '2025-10-23', 'value': 0.034363047955280966}, {'date': '2025-10-24', 'value': 0.03287059802549457}, {'date': '2025-10-25', 'value': 0.03831009140403997}, {'date': '2025-10-26', 'value': 0.030939358856640984}, {'date': '2025-10-27', 'value': 0.035853037711836025}, {'date': '2025-10-28', 'value': 0.03246856208911169}] breakdown=[{'label': 'Image Ad - Morning Audience - App Install Campaign', 'value': 0.030873902201019193, 'spend': 526.38, 'clicks': 1139, 'conversions': 147.0, 'revenue': 220.38, 'impressions': 36892}] workspace_avg=0.025313548925062414
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The worst performing ad in your App Install campaign last week was the Image Ad - Morning Audience with a CTR of 3.1%—though it's still above your workspace average of 2.5%. Even your "worst" ad is doing pretty well, so overall, you're in a good spot!'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1663ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3531ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The worst performing ad in your App Install campaign last week was the Image Ad - Morning Audience with a CTR of 3.1%—though it's still above your workspace average of 2.5%. Even your "worst" ad is doing pretty well, so overall, you're in a good spot!'
```

---

## Test 60: all campaigns with conversion rate above 5%

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cvr', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'cvr', 'operator': '>', 'value': 5}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'all campaigns with conversion rate above 5%', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1091ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived='cvr', need_timeseries=True, need_previous=False, base_measures=['clicks', 'conversions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'cvr', 'operator': '>', 'value': 5}]}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cvr', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'cvr', 'operator': '>', 'value': 5}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='all campaigns with conversion rate above 5%', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cvr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cvr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cvr: 0.08608288224573620215978021380
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cvr': MetricValue(value=Decimal('0.08608288224573620215978021380'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.08608288224573620215978021380
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cvr by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.08608288224573621 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 0.09119118606167893}, {'date': '2025-10-23', 'value': 0.08583712196086184}, {'date': '2025-10-24', 'value': 0.0875549027836061}, {'date': '2025-10-25', 'value': 0.08713194512017125}, {'date': '2025-10-26', 'value': 0.08163927376970856}, {'date': '2025-10-27', 'value': 0.08539040408647268}, {'date': '2025-10-28', 'value': 0.08366125018298931}] breakdown=[] workspace_avg=0.08608288224573621
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'No data available for last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: Nonems
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1289ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'No data available for last week.'
```

---

## Test 61: which adset spent the most money?

**Answer**:
> The Morning Audience - Lead Gen - B2B adset spent the most money at $690.53 last week—your top performer! For context, your overall spend was right on the average at $66,808.12.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'spend', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'which adset spent the most money?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1034ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='adset', breakdown='adset', derived=None, need_timeseries=True, need_previous=False, base_measures=['spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='spend', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='which adset spent the most money?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 66808.12
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=66808.12, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 66808.12
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for spend by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=66808.12 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 9939.96}, {'date': '2025-10-23', 'value': 9386.67}, {'date': '2025-10-24', 'value': 9457.54}, {'date': '2025-10-25', 'value': 8887.48}, {'date': '2025-10-26', 'value': 9661.06}, {'date': '2025-10-27', 'value': 10008.96}, {'date': '2025-10-28', 'value': 9466.45}] breakdown=[{'label': 'Morning Audience - Lead Gen - B2B', 'value': 690.53, 'spend': 690.53, 'clicks': 1941, 'conversions': 413.17, 'revenue': 2503.02, 'impressions': 44908}] workspace_avg=66808.12
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Morning Audience - Lead Gen - B2B adset spent the most money at $690.53 last week—your top performer! For context, your overall spend was right on the average at $66,808.12.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1076ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2344ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Morning Audience - Lead Gen - B2B adset spent the most money at $690.53 last week—your top performer! For context, your overall spend was right on the average at $66,808.12.'
```

---

## Test 62: show me ads with revenue above 1000

**Answer**:
> The Image Ad - Morning Audience from the Summer Sale Campaign brought in $14,390.73 last week, leading the pack for ads with revenue over $1,000. Overall, your total revenue was $423,782.30, which was right on par with your average.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'revenue', 'operator': '>', 'value': 1000}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'show me ads with revenue above 1000', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1410ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='ad', breakdown='ad', derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'revenue', 'operator': '>', 'value': 1000}]}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'revenue', 'operator': '>', 'value': 1000}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='show me ads with revenue above 1000', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=423782.3, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for revenue by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=423782.3 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 53736.71}, {'date': '2025-10-23', 'value': 55066.55}, {'date': '2025-10-24', 'value': 58272.68}, {'date': '2025-10-25', 'value': 69017.48}, {'date': '2025-10-26', 'value': 64361.53}, {'date': '2025-10-27', 'value': 62243.58}, {'date': '2025-10-28', 'value': 61083.77}] breakdown=[{'label': 'Image Ad - Morning Audience - Summer Sale Campaign', 'value': 14390.73, 'spend': 577.22, 'clicks': 1591, 'conversions': 111.0, 'revenue': 14390.73, 'impressions': 40561}, {'label': 'Carousel Ad - Evening Audience - Summer Sale Campaign', 'value': 13134.73, 'spend': 535.33, 'clicks': 1806, 'conversions': 92.0, 'revenue': 13134.73, 'impressions': 39990}, {'label': 'Video Ad - Weekend Audience - Holiday Sale - Purchases', 'value': 9600.53, 'spend': 517.69, 'clicks': 1087, 'conversions': 61.0, 'revenue': 9600.53, 'impressions': 51467}, {'label': 'Video Ad - Weekend Audience - Summer Sale Campaign', 'value': 9518.03, 'spend': 524.72, 'clicks': 1223, 'conversions': 77.0, 'revenue': 9518.03, 'impressions': 40143}, {'label': 'Carousel Ad - Weekend Audience - Summer Sale Campaign', 'value': 8064.3, 'spend': 609.99, 'clicks': 1298, 'conversions': 60.0, 'revenue': 8064.3, 'impressions': 42386}, {'label': 'Image Ad - Evening Audience - Summer Sale Campaign', 'value': 7453.51, 'spend': 472.94, 'clicks': 1340, 'conversions': 63.0, 'revenue': 7453.51, 'impressions': 37933}, {'label': 'Carousel Ad - Morning Audience - Blog Content Promotion', 'value': 7071.4, 'spend': 333.22, 'clicks': 612, 'conversions': 115.39, 'revenue': 7071.4, 'impressions': 30025}, {'label': 'Video Ad - Weekend Audience - Black Friday Deals', 'value': 7035.57, 'spend': 358.91, 'clicks': 937, 'conversions': 53.0, 'revenue': 7035.57, 'impressions': 45884}, {'label': 'Image Ad - Morning Audience - Holiday Sale - Purchases', 'value': 6314.29, 'spend': 343.64, 'clicks': 754, 'conversions': 46.0, 'revenue': 6314.29, 'impressions': 38408}, {'label': 'Video Ad - Morning Audience - Summer Sale Campaign', 'value': 6149.32, 'spend': 424.42, 'clicks': 1299, 'conversions': 64.0, 'revenue': 6149.32, 'impressions': 40109}] workspace_avg=423782.3
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Image Ad - Morning Audience from the Summer Sale Campaign brought in $14,390.73 last week, leading the pack for ads with revenue over $1,000. Overall, your total revenue was $423,782.30, which was right on par with your average.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1890ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3576ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Image Ad - Morning Audience from the Summer Sale Campaign brought in $14,390.73 last week, leading the pack for ads with revenue over $1,000. Overall, your total revenue was $423,782.30, which was right on par with your average.'
```

---

## Test 63: best performing campaign by profit margin

**Answer**:
> The Lead Gen - B2B campaign had the lowest POAS at 0.56× last week, making it your worst performer. For context, your overall POAS was 1.92×, so this campaign really needs some attention.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'poas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'best performing campaign by profit margin', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1153ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived='poas', need_timeseries=True, need_previous=False, base_measures=['profit', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='poas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='best performing campaign by profit margin', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['poas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for poas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for poas: 1.916253144078893403975444901
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'poas': MetricValue(value=Decimal('1.916253144078893403975444901'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 1.916253144078893403975444901
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for poas by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=1.9162531440788935 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 1.619574927866913}, {'date': '2025-10-23', 'value': 1.8571229200557813}, {'date': '2025-10-24', 'value': 1.900697221476198}, {'date': '2025-10-25', 'value': 2.418220913014713}, {'date': '2025-10-26', 'value': 1.9646011928297722}, {'date': '2025-10-27', 'value': 1.7846549491655477}, {'date': '2025-10-28', 'value': 1.9204749404475807}] breakdown=[{'label': 'Lead Gen - B2B', 'value': 0.5593663324087903, 'spend': 749.92, 'clicks': 1419, 'conversions': 252.59, 'revenue': 1333.37, 'impressions': 45072}] workspace_avg=1.9162531440788935
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Lead Gen - B2B campaign had the lowest POAS at 0.56× last week, making it your worst performer. For context, your overall POAS was 1.92×, so this campaign really needs some attention.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1257ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2704ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Lead Gen - B2B campaign had the lowest POAS at 0.56× last week, making it your worst performer. For context, your overall POAS was 1.92×, so this campaign really needs some attention.'
```

---

## Test 64: all adsets with clicks above 500

**Answer**:
> Here are the ad sets from last week that had more than 500 clicks:

1. **Morning Audience - Lead Gen - B2B**: This ad set achieved 1,941 clicks, with a spend of $690.53, resulting in a revenue of $2,503.02 from 44,908 impressions.

2. **Morning Audience - Website Traffic Push**: Garnered 1,583 clicks, spending $608.10, and generated $4,877.75 in revenue from 43,936 impressions.

3. **Weekend Audience - Website Traffic Push**: Brought in 1,523 clicks, with a spend of $600.59, and earned $4,834.28 in revenue from 43,688 impressions.

4. **Morning Audience - Mobile Game Installs**: Achieved 1,447 clicks, spending $660.85, and generated $383.27 in revenue from 52,161 impressions.

5. **Morning Audience - Summer Sale Campaign**: This ad set had 1,445 clicks, with a spend of $512.05, resulting in a substantial revenue of $10,549.28 from 38,994 impressions.

6. **Evening Audience - Lead Gen - B2B**: Recorded 1,416 clicks, spending $606.52, and brought in $1,552.88 in revenue from 44,162 impressions.

7. **Weekend Audience - App Install Campaign**: Managed to get 1,264 clicks, with a spend of $626.62, and generated $296.50 in revenue from 39,984 impressions.

8. **Evening Audience - Summer Sale Campaign**: This ad set achieved 1,207 clicks, spending $452.04, and earned $6,974.45 in revenue from 39,264 impressions.

9. **Weekend Audience - Brand Awareness**: Brought in 1,204 clicks, with a spend of $581.99, and generated $505.15 in revenue from 46,293 impressions.

10. **Morning Audience - Brand Awareness**: Recorded 1,187 clicks, spending $582.48, and brought in $735.11 in revenue from 48,897 impressions.

In total, all 10 ad sets exceeded 500 clicks last week, showcasing their effectiveness in driving traffic and engagement.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'clicks', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'clicks', 'operator': '>', 'value': 500}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'all adsets with clicks above 500', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1119ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='adset', breakdown='adset', derived=None, need_timeseries=True, need_previous=False, base_measures=['clicks'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'clicks', 'operator': '>', 'value': 500}]}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='clicks', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'clicks', 'operator': '>', 'value': 500}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='all adsets with clicks above 500', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['clicks']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for clicks
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for clicks: 147052.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'clicks': MetricValue(value=147052.0, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 147052.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for clicks by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=147052.0 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 21466.0}, {'date': '2025-10-23', 'value': 20236.0}, {'date': '2025-10-24', 'value': 21447.0}, {'date': '2025-10-25', 'value': 20554.0}, {'date': '2025-10-26', 'value': 20930.0}, {'date': '2025-10-27', 'value': 21926.0}, {'date': '2025-10-28', 'value': 20493.0}] breakdown=[{'label': 'Morning Audience - Lead Gen - B2B', 'value': 1941.0, 'spend': 690.53, 'clicks': 1941, 'conversions': 413.17, 'revenue': 2503.02, 'impressions': 44908}, {'label': 'Morning Audience - Website Traffic Push', 'value': 1583.0, 'spend': 608.1, 'clicks': 1583, 'conversions': 103.26, 'revenue': 4877.75, 'impressions': 43936}, {'label': 'Weekend Audience - Website Traffic Push', 'value': 1523.0, 'spend': 600.59, 'clicks': 1523, 'conversions': 82.13, 'revenue': 4834.28, 'impressions': 43688}, {'label': 'Morning Audience - Mobile Game Installs', 'value': 1447.0, 'spend': 660.85, 'clicks': 1447, 'conversions': 126.0, 'revenue': 383.27, 'impressions': 52161}, {'label': 'Morning Audience - Summer Sale Campaign', 'value': 1445.0, 'spend': 512.05, 'clicks': 1445, 'conversions': 74.0, 'revenue': 10549.28, 'impressions': 38994}, {'label': 'Evening Audience - Lead Gen - B2B', 'value': 1416.0, 'spend': 606.52, 'clicks': 1416, 'conversions': 294.03, 'revenue': 1552.88, 'impressions': 44162}, {'label': 'Weekend Audience - App Install Campaign', 'value': 1264.0, 'spend': 626.62, 'clicks': 1264, 'conversions': 114.0, 'revenue': 296.5, 'impressions': 39984}, {'label': 'Evening Audience - Summer Sale Campaign', 'value': 1207.0, 'spend': 452.04, 'clicks': 1207, 'conversions': 69.0, 'revenue': 6974.45, 'impressions': 39264}, {'label': 'Weekend Audience - Brand Awareness', 'value': 1204.0, 'spend': 581.99, 'clicks': 1204, 'conversions': 15.98, 'revenue': 505.15, 'impressions': 46293}, {'label': 'Morning Audience - Brand Awareness', 'value': 1187.0, 'spend': 582.48, 'clicks': 1187, 'conversions': 19.57, 'revenue': 735.11, 'impressions': 48897}] workspace_avg=147052.0
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are the ad sets from last week that had more than 500 clicks:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 4074ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 5436ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are the ad sets from last week that had more than 500 clicks:
```

---

## Test 65: which ad has the lowest cost per conversion?

**Answer**:
> The Video Ad - Weekend Audience - Lead Gen - B2B had the lowest cost per conversion at $1.69 last week—your best performer! For context, your overall average CPA was $5.28, so this ad is really crushing it.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpa', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 1, 'sort_order': 'asc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'which ad has the lowest cost per conversion?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 965ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='ad', breakdown='ad', derived='cpa', need_timeseries=True, need_previous=False, base_measures=['conversions', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='asc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpa', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=1, sort_order='asc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='which ad has the lowest cost per conversion?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpa']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpa
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpa: 5.277661300643196041287150457
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpa': MetricValue(value=Decimal('5.277661300643196041287150457'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 5.277661300643196041287150457
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpa by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: asc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=5.277661300643196 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 5.077859116939377}, {'date': '2025-10-23', 'value': 5.403955094991365}, {'date': '2025-10-24', 'value': 5.03652698118533}, {'date': '2025-10-25', 'value': 4.962549765203165}, {'date': '2025-10-26', 'value': 5.654007994334908}, {'date': '2025-10-27', 'value': 5.345895624028586}, {'date': '2025-10-28', 'value': 5.52150227183911}] breakdown=[{'label': 'Video Ad - Weekend Audience - Lead Gen - B2B', 'value': 1.6911668662240122, 'spend': 621.47, 'clicks': 1777, 'conversions': 367.48, 'revenue': 1963.88, 'impressions': 42018}] workspace_avg=5.277661300643196
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Video Ad - Weekend Audience - Lead Gen - B2B had the lowest cost per conversion at $1.69 last week—your best performer! For context, your overall average CPA was $5.28, so this ad is really crushing it.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1355ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2548ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Video Ad - Weekend Audience - Lead Gen - B2B had the lowest cost per conversion at $1.69 last week—your best performer! For context, your overall average CPA was $5.28, so this ad is really crushing it.'
```

---

## Test 66: show me campaigns with impressions over 10000

**Answer**:
> The "Lead Gen - B2B" campaign had 45,072 impressions last week, leading the pack among your campaigns. Overall, your campaigns averaged 5,809,221 impressions, so this one stood out with a solid performance.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'impressions', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'impressions', 'operator': '>', 'value': 10000}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'show me campaigns with impressions over 10000', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1294ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['impressions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'impressions', 'operator': '>', 'value': 10000}]}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='impressions', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'impressions', 'operator': '>', 'value': 10000}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='show me campaigns with impressions over 10000', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['impressions']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for impressions
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for impressions: 5809221.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'impressions': MetricValue(value=5809221.0, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 5809221.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for impressions by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=5809221.0 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 855383.0}, {'date': '2025-10-23', 'value': 831689.0}, {'date': '2025-10-24', 'value': 845514.0}, {'date': '2025-10-25', 'value': 800607.0}, {'date': '2025-10-26', 'value': 830900.0}, {'date': '2025-10-27', 'value': 850347.0}, {'date': '2025-10-28', 'value': 794781.0}] breakdown=[{'label': 'Lead Gen - B2B', 'value': 45072.0, 'spend': 749.92, 'clicks': 1419, 'conversions': 252.59, 'revenue': 1333.37, 'impressions': 45072}, {'label': 'Website Traffic Push', 'value': 37902.0, 'spend': 513.38, 'clicks': 1339, 'conversions': 90.13, 'revenue': 4512.27, 'impressions': 37902}, {'label': 'Blog Content Promotion', 'value': 44601.0, 'spend': 499.75, 'clicks': 795, 'conversions': 87.63, 'revenue': 4666.99, 'impressions': 44601}, {'label': 'Summer Sale Campaign', 'value': 33284.0, 'spend': 474.11, 'clicks': 1122, 'conversions': 61.0, 'revenue': 8173.18, 'impressions': 33284}, {'label': 'Holiday Sale - Purchases', 'value': 37036.0, 'spend': 391.4, 'clicks': 696, 'conversions': 30.0, 'revenue': 3056.82, 'impressions': 37036}, {'label': 'Product Launch Teaser', 'value': 43695.0, 'spend': 379.67, 'clicks': 588, 'conversions': 13.63, 'revenue': 450.41, 'impressions': 43695}, {'label': 'Newsletter Signup Campaign', 'value': 37549.0, 'spend': 371.45, 'clicks': 830, 'conversions': 153.99, 'revenue': 751.08, 'impressions': 37549}, {'label': 'Mobile Game Installs', 'value': 27442.0, 'spend': 371.21, 'clicks': 663, 'conversions': 59.0, 'revenue': 194.02, 'impressions': 27442}, {'label': 'Black Friday Deals', 'value': 34236.0, 'spend': 344.13, 'clicks': 658, 'conversions': 34.0, 'revenue': 5347.1, 'impressions': 34236}, {'label': 'Brand Awareness', 'value': 28790.0, 'spend': 317.08, 'clicks': 695, 'conversions': 16.22, 'revenue': 642.13, 'impressions': 28790}] workspace_avg=5809221.0
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The "Lead Gen - B2B" campaign had 45,072 impressions last week, leading the pack among your campaigns. Overall, your campaigns averaged 5,809,221 impressions, so this one stood out with a solid performance.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1490ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3024ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The "Lead Gen - B2B" campaign had 45,072 impressions last week, leading the pack among your campaigns. Overall, your campaigns averaged 5,809,221 impressions, so this one stood out with a solid performance.'
```

---

## Test 67: worst performing adset by roas

**Answer**:
> The Weekend Audience - Mobile Game Installs ad set had the lowest ROAS at 0.32× last week—definitely struggling. For context, your overall ROAS was 6.34×, so this ad set really needs some attention.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 1, 'sort_order': 'asc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'worst performing adset by roas', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1709ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='adset', breakdown='adset', derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='asc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=1, sort_order='asc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='worst performing adset by roas', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('6.343275338387010441245764736'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for roas by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: asc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=6.34327533838701 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 5.406129400923143}, {'date': '2025-10-23', 'value': 5.8664627604890764}, {'date': '2025-10-24', 'value': 6.161505000243192}, {'date': '2025-10-25', 'value': 7.76569736303204}, {'date': '2025-10-26', 'value': 6.6619532432258985}, {'date': '2025-10-27', 'value': 6.218785967772876}, {'date': '2025-10-28', 'value': 6.452658599580624}] breakdown=[{'label': 'Weekend Audience - Mobile Game Installs', 'value': 0.32327864473186263, 'spend': 449.21, 'clicks': 1081, 'conversions': 98.0, 'revenue': 145.22, 'impressions': 42110}] workspace_avg=6.34327533838701
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Weekend Audience - Mobile Game Installs ad set had the lowest ROAS at 0.32× last week—definitely struggling. For context, your overall ROAS was 6.34×, so this ad set really needs some attention.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1514ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3437ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Weekend Audience - Mobile Game Installs ad set had the lowest ROAS at 0.32× last week—definitely struggling. For context, your overall ROAS was 6.34×, so this ad set really needs some attention.'
```

---

## Test 68: all ads with ctr above 3%

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'ctr', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'ctr', 'operator': '>', 'value': 3}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'all ads with ctr above 3%', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1036ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='ad', breakdown='ad', derived='ctr', need_timeseries=True, need_previous=False, base_measures=['clicks', 'impressions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'ctr', 'operator': '>', 'value': 3}]}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='ctr', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'ctr', 'operator': '>', 'value': 3}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='all ads with ctr above 3%', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['ctr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for ctr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for ctr: 0.025313548925062414
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'ctr': MetricValue(value=0.025313548925062414, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.025313548925062414
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for ctr by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.025313548925062414 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 0.02509519127689}, {'date': '2025-10-23', 'value': 0.024331210344251276}, {'date': '2025-10-24', 'value': 0.025365635577885168}, {'date': '2025-10-25', 'value': 0.02567302059562307}, {'date': '2025-10-26', 'value': 0.02518955349620893}, {'date': '2025-10-27', 'value': 0.025784767865353792}, {'date': '2025-10-28', 'value': 0.0257844613799273}] breakdown=[] workspace_avg=0.025313548925062414
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'No data available for last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: Nonems
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1269ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'No data available for last week.'
```

---

## Test 69: which campaign generated the most leads?

**Answer**:
> The "Lead Gen - B2B" campaign generated the most leads last week with 253 leads—your top performer! Overall, your lead count was 5,044, which was right on par with your average.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'leads', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'which campaign generated the most leads?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 979ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['leads'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='leads', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='which campaign generated the most leads?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['leads']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for leads
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for leads: 5044.47
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'leads': MetricValue(value=5044.47, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 5044.47
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for leads by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=5044.47 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 879.78}, {'date': '2025-10-23', 'value': 660.36}, {'date': '2025-10-24', 'value': 742.53}, {'date': '2025-10-25', 'value': 632.93}, {'date': '2025-10-26', 'value': 705.34}, {'date': '2025-10-27', 'value': 809.71}, {'date': '2025-10-28', 'value': 613.82}] breakdown=[{'label': 'Lead Gen - B2B', 'value': 252.59, 'spend': 749.92, 'clicks': 1419, 'conversions': 252.59, 'revenue': 1333.37, 'impressions': 45072}] workspace_avg=5044.47
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The "Lead Gen - B2B" campaign generated the most leads last week with 253 leads—your top performer! Overall, your lead count was 5,044, which was right on par with your average.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1680ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2878ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The "Lead Gen - B2B" campaign generated the most leads last week with 253 leads—your top performer! Overall, your lead count was 5,044, which was right on par with your average.'
```

---

## Test 70: show me adsets with spend below 50 dollars

**Answer**:
> Last week, your ad sets with spend below $50 were performing at an average level, with the overall spend across all ad sets being $66,808.12. This means those lower-spending ad sets were well below the average spend, which might be worth looking into if you're aiming to optimize budget allocation.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'spend', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'spend', 'operator': '<', 'value': 50}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'show me adsets with spend below 50 dollars', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1321ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='adset', breakdown='adset', derived=None, need_timeseries=True, need_previous=False, base_measures=['spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'spend', 'operator': '<', 'value': 50}]}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='spend', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'spend', 'operator': '<', 'value': 50}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='show me adsets with spend below 50 dollars', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 66808.12
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=66808.12, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 66808.12
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for spend by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=66808.12 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 9939.96}, {'date': '2025-10-23', 'value': 9386.67}, {'date': '2025-10-24', 'value': 9457.54}, {'date': '2025-10-25', 'value': 8887.48}, {'date': '2025-10-26', 'value': 9661.06}, {'date': '2025-10-27', 'value': 10008.96}, {'date': '2025-10-28', 'value': 9466.45}] breakdown=[] workspace_avg=66808.12
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Last week, your ad sets with spend below $50 were performing at an average level, with the overall spend across all ad sets being $66,808.12. This means those lower-spending ad sets were well below the average spend, which might be worth looking into if you're aiming to optimize budget allocation.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1974ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3523ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Last week, your ad sets with spend below $50 were performing at an average level, with the overall spend across all ad sets being $66,808.12. This means those lower-spending ad sets were well below the average spend, which might be worth looking into if you're aiming to optimize budget allocation.'
```

---

## Test 71: best performing ad by revenue per click

**Answer**:
> The Video Ad - Morning Audience - Website Traffic Push had the lowest ARPV at $3.27 last week—your worst performer. For context, your overall ARPV was $4.01, so this ad could use some attention.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'arpv', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'best performing ad by revenue per click', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1117ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='ad', breakdown='ad', derived='arpv', need_timeseries=True, need_previous=False, base_measures=['revenue', 'visitors'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='arpv', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='best performing ad by revenue per click', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['arpv']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for arpv
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for arpv: 4.009558816572526089712658360
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'arpv': MetricValue(value=Decimal('4.009558816572526089712658360'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 4.009558816572526089712658360
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for arpv by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=4.009558816572526 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 3.6140096845786536}, {'date': '2025-10-23', 'value': 3.7429683251767263}, {'date': '2025-10-24', 'value': 3.8007226715366556}, {'date': '2025-10-25', 'value': 4.765413243112615}, {'date': '2025-10-26', 'value': 4.033435482860186}, {'date': '2025-10-27', 'value': 3.8395891678489913}, {'date': '2025-10-28', 'value': 4.323290395640172}] breakdown=[{'label': 'Video Ad - Morning Audience - Website Traffic Push', 'value': 3.2732636754763367, 'spend': 724.83, 'clicks': 1865, 'conversions': 98.54, 'revenue': 5325.6, 'impressions': 49913}] workspace_avg=4.009558816572526
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Video Ad - Morning Audience - Website Traffic Push had the lowest ARPV at $3.27 last week—your worst performer. For context, your overall ARPV was $4.01, so this ad could use some attention.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1346ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2717ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Video Ad - Morning Audience - Website Traffic Push had the lowest ARPV at $3.27 last week—your worst performer. For context, your overall ARPV was $4.01, so this ad could use some attention.'
```

---

## Test 72: all campaigns with cpm under 10 dollars

**Answer**:
> In the last week, there are two campaigns with a CPM under $10:

1. **Newsletter Signup Campaign**: This campaign had a CPM of $9.89. It spent $371.45, received 830 clicks, and generated $751.08 in revenue from 37,549 impressions.

2. **Product Launch Teaser**: This campaign achieved a CPM of $8.69. It spent $379.67, garnered 588 clicks, and brought in $450.41 in revenue from 43,695 impressions.

In total, there are 2 campaigns that met the criteria.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpm', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'cpm', 'operator': '<', 'value': 10}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'all campaigns with cpm under 10 dollars', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1005ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived='cpm', need_timeseries=True, need_previous=False, base_measures=['impressions', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'cpm', 'operator': '<', 'value': 10}]}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpm', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'cpm', 'operator': '<', 'value': 10}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='all campaigns with cpm under 10 dollars', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpm']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpm
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpm: 11.50035779323940335545850296
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpm': MetricValue(value=Decimal('11.50035779323940335545850296'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 11.50035779323940335545850296
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpm by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=11.500357793239404 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 11.620478779681148}, {'date': '2025-10-23', 'value': 11.286274076006777}, {'date': '2025-10-24', 'value': 11.1855510375937}, {'date': '2025-10-25', 'value': 11.100927171508618}, {'date': '2025-10-26', 'value': 11.627223492598388}, {'date': '2025-10-27', 'value': 11.770441948992588}, {'date': '2025-10-28', 'value': 11.910765355487865}] breakdown=[{'label': 'Newsletter Signup Campaign', 'value': 9.89240725452076, 'spend': 371.45, 'clicks': 830, 'conversions': 153.99, 'revenue': 751.08, 'impressions': 37549}, {'label': 'Product Launch Teaser', 'value': 8.68909486211237, 'spend': 379.67, 'clicks': 588, 'conversions': 13.63, 'revenue': 450.41, 'impressions': 43695}] workspace_avg=11.500357793239404
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'In the last week, there are two campaigns with a CPM under $10:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 2155ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3413ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'In the last week, there are two campaigns with a CPM under $10:
```

---

## Test 73: which adset has the highest conversion rate?

**Answer**:
> The "Morning Audience - Lead Gen - B2B" adset had the highest conversion rate at 21.3% last week—your top performer! For context, the overall average conversion rate across your adsets was 8.6%.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cvr', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'which adset has the highest conversion rate?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 982ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='adset', breakdown='adset', derived='cvr', need_timeseries=True, need_previous=False, base_measures=['clicks', 'conversions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cvr', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='which adset has the highest conversion rate?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cvr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cvr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cvr: 0.08608288224573620215978021380
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cvr': MetricValue(value=Decimal('0.08608288224573620215978021380'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.08608288224573620215978021380
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cvr by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.08608288224573621 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 0.09119118606167893}, {'date': '2025-10-23', 'value': 0.08583712196086184}, {'date': '2025-10-24', 'value': 0.0875549027836061}, {'date': '2025-10-25', 'value': 0.08713194512017125}, {'date': '2025-10-26', 'value': 0.08163927376970856}, {'date': '2025-10-27', 'value': 0.08539040408647268}, {'date': '2025-10-28', 'value': 0.08366125018298931}] breakdown=[{'label': 'Morning Audience - Lead Gen - B2B', 'value': 0.21286450283359093, 'spend': 690.53, 'clicks': 1941, 'conversions': 413.17, 'revenue': 2503.02, 'impressions': 44908}] workspace_avg=0.08608288224573621
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The "Morning Audience - Lead Gen - B2B" adset had the highest conversion rate at 21.3% last week—your top performer! For context, the overall average conversion rate across your adsets was 8.6%.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1058ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2251ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The "Morning Audience - Lead Gen - B2B" adset had the highest conversion rate at 21.3% last week—your top performer! For context, the overall average conversion rate across your adsets was 8.6%.'
```

---

## Test 74: show me ads with conversions above 20

**Answer**:
> The Video Ad - Weekend Audience - Lead Gen - B2B had 367 conversions last week, which was the highest among your ads. Overall, your ads averaged 12,659 conversions last week, so this one really stood out!

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'conversions', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'conversions', 'operator': '>', 'value': 20}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'show me ads with conversions above 20', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1168ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='ad', breakdown='ad', derived=None, need_timeseries=True, need_previous=False, base_measures=['conversions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'conversions', 'operator': '>', 'value': 20}]}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='conversions', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'conversions', 'operator': '>', 'value': 20}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='show me ads with conversions above 20', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['conversions']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for conversions
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for conversions: 12658.66
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'conversions': MetricValue(value=12658.66, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 12658.66
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for conversions by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=12658.66 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 1957.51}, {'date': '2025-10-23', 'value': 1737.0}, {'date': '2025-10-24', 'value': 1877.79}, {'date': '2025-10-25', 'value': 1790.91}, {'date': '2025-10-26', 'value': 1708.71}, {'date': '2025-10-27', 'value': 1872.27}, {'date': '2025-10-28', 'value': 1714.47}] breakdown=[{'label': 'Video Ad - Weekend Audience - Lead Gen - B2B', 'value': 367.48, 'spend': 621.47, 'clicks': 1777, 'conversions': 367.48, 'revenue': 1963.88, 'impressions': 42018}, {'label': 'Image Ad - Weekend Audience - Lead Gen - B2B', 'value': 261.36, 'spend': 500.51, 'clicks': 1214, 'conversions': 261.36, 'revenue': 898.52, 'impressions': 30355}, {'label': 'Image Ad - Morning Audience - Lead Gen - B2B', 'value': 260.06, 'spend': 649.49, 'clicks': 1645, 'conversions': 260.06, 'revenue': 1605.33, 'impressions': 43857}, {'label': 'Video Ad - Morning Audience - Lead Gen - B2B', 'value': 255.36, 'spend': 613.34, 'clicks': 1461, 'conversions': 255.36, 'revenue': 1897.61, 'impressions': 40018}, {'label': 'Carousel Ad - Weekend Audience - Lead Gen - B2B', 'value': 249.41, 'spend': 549.27, 'clicks': 1478, 'conversions': 249.41, 'revenue': 865.75, 'impressions': 38949}, {'label': 'Carousel Ad - Evening Audience - Lead Gen - B2B', 'value': 224.85, 'spend': 613.75, 'clicks': 1256, 'conversions': 224.85, 'revenue': 560.16, 'impressions': 38611}, {'label': 'Video Ad - Evening Audience - Lead Gen - B2B', 'value': 223.83, 'spend': 690.99, 'clicks': 1397, 'conversions': 223.83, 'revenue': 1439.26, 'impressions': 48344}, {'label': 'Image Ad - Evening Audience - Lead Gen - B2B', 'value': 202.15, 'spend': 450.99, 'clicks': 1146, 'conversions': 202.15, 'revenue': 1293.53, 'impressions': 33179}, {'label': 'Video Ad - Evening Audience - Newsletter Signup Campaign', 'value': 174.33, 'spend': 429.11, 'clicks': 821, 'conversions': 174.33, 'revenue': 974.67, 'impressions': 40242}, {'label': 'Video Ad - Morning Audience - App Install Campaign', 'value': 171.0, 'spend': 700.6, 'clicks': 1408, 'conversions': 171.0, 'revenue': 396.39, 'impressions': 42701}] workspace_avg=12658.66
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Video Ad - Weekend Audience - Lead Gen - B2B had 367 conversions last week, which was the highest among your ads. Overall, your ads averaged 12,659 conversions last week, so this one really stood out!'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1549ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2949ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Video Ad - Weekend Audience - Lead Gen - B2B had 367 conversions last week, which was the highest among your ads. Overall, your ads averaged 12,659 conversions last week, so this one really stood out!'
```

---

## Test 75: worst performing campaign by cost per lead

**Answer**:
> The General Conversions campaign had a CPL of $13.24 last week, which was right at the average for your workspace. So, while it's not the worst performer, it's also not standing out as a top performer either.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpl', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'asc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'worst performing campaign by cost per lead', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1656ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived='cpl', need_timeseries=True, need_previous=False, base_measures=['leads', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='asc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpl', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='asc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='worst performing campaign by cost per lead', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpl']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpl
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpl: 13.24383334621873060995505970
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpl': MetricValue(value=Decimal('13.24383334621873060995505970'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 13.24383334621873060995505970
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpl by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: asc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=13.24383334621873 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 11.298233649321421}, {'date': '2025-10-23', 'value': 14.214473923314555}, {'date': '2025-10-24', 'value': 12.736912986680673}, {'date': '2025-10-25', 'value': 14.041805570916216}, {'date': '2025-10-26', 'value': 13.697025547962685}, {'date': '2025-10-27', 'value': 12.3611663435057}, {'date': '2025-10-28', 'value': 15.422192173601381}] breakdown=[{'label': 'General Conversions', 'value': None, 'spend': 265.77, 'clicks': 554, 'conversions': 50.92, 'revenue': 4029.47, 'impressions': 25870}] workspace_avg=13.24383334621873
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The General Conversions campaign had a CPL of $13.24 last week, which was right at the average for your workspace. So, while it's not the worst performer, it's also not standing out as a top performer either.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1010ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2873ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The General Conversions campaign had a CPL of $13.24 last week, which was right at the average for your workspace. So, while it's not the worst performer, it's also not standing out as a top performer either.'
```

---

## Test 76: all adsets with revenue above 5000

**Answer**:
> Here are the ad sets from last week that generated revenue above $5,000:

1. **Morning Audience - Summer Sale Campaign**: This ad set brought in a revenue of $10,549.28. It had a spend of $512.05, with 1,445 clicks and 74 conversions from 38,994 impressions.

2. **Evening Audience - Summer Sale Campaign**: This ad set generated $6,974.45 in revenue. It had a spend of $452.04, with 1,207 clicks and 69 conversions from 39,264 impressions.

3. **Weekend Audience - Summer Sale Campaign**: This ad set achieved a revenue of $5,094.99. It had a spend of $356.75, with 826 clicks and 38 conversions from 26,496 impressions.

In total, there are 3 ad sets that met the criteria of having revenue above $5,000 last week.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'revenue', 'operator': '>', 'value': 5000}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'all adsets with revenue above 5000', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1800ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='adset', breakdown='adset', derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'revenue', 'operator': '>', 'value': 5000}]}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'revenue', 'operator': '>', 'value': 5000}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='all adsets with revenue above 5000', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=423782.3, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for revenue by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=423782.3 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 53736.71}, {'date': '2025-10-23', 'value': 55066.55}, {'date': '2025-10-24', 'value': 58272.68}, {'date': '2025-10-25', 'value': 69017.48}, {'date': '2025-10-26', 'value': 64361.53}, {'date': '2025-10-27', 'value': 62243.58}, {'date': '2025-10-28', 'value': 61083.77}] breakdown=[{'label': 'Morning Audience - Summer Sale Campaign', 'value': 10549.28, 'spend': 512.05, 'clicks': 1445, 'conversions': 74.0, 'revenue': 10549.28, 'impressions': 38994}, {'label': 'Evening Audience - Summer Sale Campaign', 'value': 6974.45, 'spend': 452.04, 'clicks': 1207, 'conversions': 69.0, 'revenue': 6974.45, 'impressions': 39264}, {'label': 'Weekend Audience - Summer Sale Campaign', 'value': 5094.99, 'spend': 356.75, 'clicks': 826, 'conversions': 38.0, 'revenue': 5094.99, 'impressions': 26496}] workspace_avg=423782.3
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are the ad sets from last week that generated revenue above $5,000:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 3678ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 5688ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are the ad sets from last week that generated revenue above $5,000:
```

---

## Test 77: which ad has the best profit margin?

**Answer**:
> The Video Ad - Morning Audience - Website Traffic Push had the best profit margin at 2.22× last week—crushing it! For context, your overall POAS was 1.92×, so this ad really stood out.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'poas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'which ad has the best profit margin?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1712ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='ad', breakdown='ad', derived='poas', need_timeseries=True, need_previous=False, base_measures=['profit', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='poas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='which ad has the best profit margin?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['poas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for poas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for poas: 1.916253144078893403975444901
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'poas': MetricValue(value=Decimal('1.916253144078893403975444901'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 1.916253144078893403975444901
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for poas by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=1.9162531440788935 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 1.619574927866913}, {'date': '2025-10-23', 'value': 1.8571229200557813}, {'date': '2025-10-24', 'value': 1.900697221476198}, {'date': '2025-10-25', 'value': 2.418220913014713}, {'date': '2025-10-26', 'value': 1.9646011928297722}, {'date': '2025-10-27', 'value': 1.7846549491655477}, {'date': '2025-10-28', 'value': 1.9204749404475807}] breakdown=[{'label': 'Video Ad - Morning Audience - Website Traffic Push', 'value': 2.21865816812218, 'spend': 724.83, 'clicks': 1865, 'conversions': 98.54, 'revenue': 5325.6, 'impressions': 49913}] workspace_avg=1.9162531440788935
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Video Ad - Morning Audience - Website Traffic Push had the best profit margin at 2.22× last week—crushing it! For context, your overall POAS was 1.92×, so this ad really stood out.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1471ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3427ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Video Ad - Morning Audience - Website Traffic Push had the best profit margin at 2.22× last week—crushing it! For context, your overall POAS was 1.92×, so this ad really stood out.'
```

---

## Test 78: show me campaigns with clicks over 1000

**Answer**:
> The "Lead Gen - B2B" campaign had 1,419 clicks last week, which is above the 1,000-click mark you were curious about. Overall, your campaigns averaged 147,052 clicks, so this one is right in line with your typical performance.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'clicks', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'clicks', 'operator': '>', 'value': 1000}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'show me campaigns with clicks over 1000', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1205ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['clicks'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'clicks', 'operator': '>', 'value': 1000}]}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='clicks', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'clicks', 'operator': '>', 'value': 1000}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='show me campaigns with clicks over 1000', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['clicks']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for clicks
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for clicks: 147052.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'clicks': MetricValue(value=147052.0, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 147052.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for clicks by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=147052.0 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 21466.0}, {'date': '2025-10-23', 'value': 20236.0}, {'date': '2025-10-24', 'value': 21447.0}, {'date': '2025-10-25', 'value': 20554.0}, {'date': '2025-10-26', 'value': 20930.0}, {'date': '2025-10-27', 'value': 21926.0}, {'date': '2025-10-28', 'value': 20493.0}] breakdown=[{'label': 'Lead Gen - B2B', 'value': 1419.0, 'spend': 749.92, 'clicks': 1419, 'conversions': 252.59, 'revenue': 1333.37, 'impressions': 45072}, {'label': 'Website Traffic Push', 'value': 1339.0, 'spend': 513.38, 'clicks': 1339, 'conversions': 90.13, 'revenue': 4512.27, 'impressions': 37902}, {'label': 'Summer Sale Campaign', 'value': 1122.0, 'spend': 474.11, 'clicks': 1122, 'conversions': 61.0, 'revenue': 8173.18, 'impressions': 33284}] workspace_avg=147052.0
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The "Lead Gen - B2B" campaign had 1,419 clicks last week, which is above the 1,000-click mark you were curious about. Overall, your campaigns averaged 147,052 clicks, so this one is right in line with your typical performance.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1244ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2685ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The "Lead Gen - B2B" campaign had 1,419 clicks last week, which is above the 1,000-click mark you were curious about. Overall, your campaigns averaged 147,052 clicks, so this one is right in line with your typical performance.'
```

---

## Test 79: best performing adset by average order value

**Answer**:
> The "Morning Audience - Lead Gen - B2B" ad set had the lowest average order value at $6.06 last week—definitely struggling compared to others. For context, your overall average order value was $33.48, so this ad set needs some attention.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'aov', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 1, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'best performing adset by average order value', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 2155ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='adset', breakdown='adset', derived='aov', need_timeseries=True, need_previous=False, base_measures=['purchases', 'revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='aov', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=1, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='best performing adset by average order value', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['aov']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for aov
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for aov: 33.47765877272949901490363119
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'aov': MetricValue(value=Decimal('33.47765877272949901490363119'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 33.47765877272949901490363119
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for aov by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=33.4776587727295 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 27.451563465831594}, {'date': '2025-10-23', 'value': 31.70210132412205}, {'date': '2025-10-24', 'value': 31.032586178433156}, {'date': '2025-10-25', 'value': 38.53765962555349}, {'date': '2025-10-26', 'value': 37.6667368950846}, {'date': '2025-10-27', 'value': 33.244980691887385}, {'date': '2025-10-28', 'value': 35.62836911698659}] breakdown=[{'label': 'Morning Audience - Lead Gen - B2B', 'value': 6.0580874700486484, 'spend': 690.53, 'clicks': 1941, 'conversions': 413.17, 'revenue': 2503.02, 'impressions': 44908}] workspace_avg=33.4776587727295
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The "Morning Audience - Lead Gen - B2B" ad set had the lowest average order value at $6.06 last week—definitely struggling compared to others. For context, your overall average order value was $33.48, so this ad set needs some attention.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1742ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 4121ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The "Morning Audience - Lead Gen - B2B" ad set had the lowest average order value at $6.06 last week—definitely struggling compared to others. For context, your overall average order value was $33.48, so this ad set needs some attention.'
```

---

## Test 80: all ads with spend above 200 dollars

**Answer**:
> Here is a list of all the ads with a spend above $200 from last week:

1. **Video Ad - Morning Audience - Website Traffic Push**: This ad had a spend of $724.83.
2. **Video Ad - Morning Audience - App Install Campaign**: The spend for this ad was $700.60.
3. **Video Ad - Evening Audience - Lead Gen - B2B**: This ad spent $690.99.
4. **Image Ad - Evening Audience - App Install Campaign**: The spend here was $689.87.
5. **Carousel Ad - Morning Audience - App Install Campaign**: This ad had a spend of $659.03.
6. **Image Ad - Morning Audience - Lead Gen - B2B**: The spend for this ad was $649.49.
7. **Carousel Ad - Weekend Audience - Mobile Game Installs**: This ad spent $643.42.
8. **Carousel Ad - Morning Audience - Summer Sale Campaign**: The spend here was $636.18.
9. **Video Ad - Weekend Audience - Lead Gen - B2B**: This ad had a spend of $621.47.
10. **Carousel Ad - Weekend Audience - App Install Campaign**: The spend for this ad was $618.47.

In total, there are 10 ads that had a spend above $200 last week.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'spend', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'ad', 'breakdown': 'ad', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'spend', 'operator': '>', 'value': 200}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'all ads with spend above 200 dollars', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1259ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='ad', breakdown='ad', derived=None, need_timeseries=True, need_previous=False, base_measures=['spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'spend', 'operator': '>', 'value': 200}]}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='spend', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='ad', breakdown='ad', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'spend', 'operator': '>', 'value': 200}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='all ads with spend above 200 dollars', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 66808.12
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=66808.12, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 66808.12
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for spend by ad
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=66808.12 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 9939.96}, {'date': '2025-10-23', 'value': 9386.67}, {'date': '2025-10-24', 'value': 9457.54}, {'date': '2025-10-25', 'value': 8887.48}, {'date': '2025-10-26', 'value': 9661.06}, {'date': '2025-10-27', 'value': 10008.96}, {'date': '2025-10-28', 'value': 9466.45}] breakdown=[{'label': 'Video Ad - Morning Audience - Website Traffic Push', 'value': 724.83, 'spend': 724.83, 'clicks': 1865, 'conversions': 98.54, 'revenue': 5325.6, 'impressions': 49913}, {'label': 'Video Ad - Morning Audience - App Install Campaign', 'value': 700.6, 'spend': 700.6, 'clicks': 1408, 'conversions': 171.0, 'revenue': 396.39, 'impressions': 42701}, {'label': 'Video Ad - Evening Audience - Lead Gen - B2B', 'value': 690.99, 'spend': 690.99, 'clicks': 1397, 'conversions': 223.83, 'revenue': 1439.26, 'impressions': 48344}, {'label': 'Image Ad - Evening Audience - App Install Campaign', 'value': 689.87, 'spend': 689.87, 'clicks': 1545, 'conversions': 156.0, 'revenue': 443.11, 'impressions': 43753}, {'label': 'Carousel Ad - Morning Audience - App Install Campaign', 'value': 659.03, 'spend': 659.03, 'clicks': 1566, 'conversions': 149.0, 'revenue': 285.37, 'impressions': 49918}, {'label': 'Image Ad - Morning Audience - Lead Gen - B2B', 'value': 649.49, 'spend': 649.49, 'clicks': 1645, 'conversions': 260.06, 'revenue': 1605.33, 'impressions': 43857}, {'label': 'Carousel Ad - Weekend Audience - Mobile Game Installs', 'value': 643.42, 'spend': 643.42, 'clicks': 1060, 'conversions': 98.0, 'revenue': 115.68, 'impressions': 40901}, {'label': 'Carousel Ad - Morning Audience - Summer Sale Campaign', 'value': 636.18, 'spend': 636.18, 'clicks': 1306, 'conversions': 52.0, 'revenue': 5364.27, 'impressions': 42146}, {'label': 'Video Ad - Weekend Audience - Lead Gen - B2B', 'value': 621.47, 'spend': 621.47, 'clicks': 1777, 'conversions': 367.48, 'revenue': 1963.88, 'impressions': 42018}, {'label': 'Carousel Ad - Weekend Audience - App Install Campaign', 'value': 618.47, 'spend': 618.47, 'clicks': 1727, 'conversions': 144.0, 'revenue': 314.0, 'impressions': 45809}] workspace_avg=66808.12
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here is a list of all the ads with a spend above $200 from last week:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 3668ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 5173ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here is a list of all the ads with a spend above $200 from last week:
```

---

## Test 81: which campaign has the lowest cost per acquisition?

**Answer**:
> The Newsletter Signup Campaign had the lowest CPA at $2.41 last week—your best performer! For context, your overall CPA was $5.28, so this campaign is really leading the pack.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpa', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 1, 'sort_order': 'asc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'which campaign has the lowest cost per acquisition?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1494ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived='cpa', need_timeseries=True, need_previous=False, base_measures=['conversions', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=1, sort_order='asc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpa', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=1, sort_order='asc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='which campaign has the lowest cost per acquisition?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpa']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpa
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpa: 5.277661300643196041287150457
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpa': MetricValue(value=Decimal('5.277661300643196041287150457'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 5.277661300643196041287150457
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpa by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 1, Sort order: asc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=5.277661300643196 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 5.077859116939377}, {'date': '2025-10-23', 'value': 5.403955094991365}, {'date': '2025-10-24', 'value': 5.03652698118533}, {'date': '2025-10-25', 'value': 4.962549765203165}, {'date': '2025-10-26', 'value': 5.654007994334908}, {'date': '2025-10-27', 'value': 5.345895624028586}, {'date': '2025-10-28', 'value': 5.52150227183911}] breakdown=[{'label': 'Newsletter Signup Campaign', 'value': 2.4121696214039874, 'spend': 371.45, 'clicks': 830, 'conversions': 153.99, 'revenue': 751.08, 'impressions': 37549}] workspace_avg=5.277661300643196
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Newsletter Signup Campaign had the lowest CPA at $2.41 last week—your best performer! For context, your overall CPA was $5.28, so this campaign is really leading the pack.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1866ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3576ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Newsletter Signup Campaign had the lowest CPA at $2.41 last week—your best performer! For context, your overall CPA was $5.28, so this campaign is really leading the pack.'
```

---

## Test 82: show me adsets with impressions over 5000

**Answer**:
> The "Morning Audience - Lead Gen - B2B" ad set had the highest impressions last week at 44,908. Overall, your ad sets were right on the average with 5,809,221 impressions. It's good to see consistent performance across the board!

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'impressions', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'impressions', 'operator': '>', 'value': 5000}]}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'show me adsets with impressions over 5000', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1787ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='adset', breakdown='adset', derived=None, need_timeseries=True, need_previous=False, base_measures=['impressions'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': [{'metric': 'impressions', 'operator': '>', 'value': 5000}]}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='impressions', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=[{'metric': 'impressions', 'operator': '>', 'value': 5000}]), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='show me adsets with impressions over 5000', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['impressions']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for impressions
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for impressions: 5809221.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'impressions': MetricValue(value=5809221.0, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 5809221.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for impressions by adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=5809221.0 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 855383.0}, {'date': '2025-10-23', 'value': 831689.0}, {'date': '2025-10-24', 'value': 845514.0}, {'date': '2025-10-25', 'value': 800607.0}, {'date': '2025-10-26', 'value': 830900.0}, {'date': '2025-10-27', 'value': 850347.0}, {'date': '2025-10-28', 'value': 794781.0}] breakdown=[{'label': 'Morning Audience - Lead Gen - B2B', 'value': 44908.0, 'spend': 690.53, 'clicks': 1941, 'conversions': 413.17, 'revenue': 2503.02, 'impressions': 44908}, {'label': 'Morning Audience - Mobile Game Installs', 'value': 52161.0, 'spend': 660.85, 'clicks': 1447, 'conversions': 126.0, 'revenue': 383.27, 'impressions': 52161}, {'label': 'Weekend Audience - App Install Campaign', 'value': 39984.0, 'spend': 626.62, 'clicks': 1264, 'conversions': 114.0, 'revenue': 296.5, 'impressions': 39984}, {'label': 'Morning Audience - Website Traffic Push', 'value': 43936.0, 'spend': 608.1, 'clicks': 1583, 'conversions': 103.26, 'revenue': 4877.75, 'impressions': 43936}, {'label': 'Evening Audience - Lead Gen - B2B', 'value': 44162.0, 'spend': 606.52, 'clicks': 1416, 'conversions': 294.03, 'revenue': 1552.88, 'impressions': 44162}, {'label': 'Weekend Audience - Website Traffic Push', 'value': 43688.0, 'spend': 600.59, 'clicks': 1523, 'conversions': 82.13, 'revenue': 4834.28, 'impressions': 43688}, {'label': 'Morning Audience - App Install Campaign', 'value': 37109.0, 'spend': 599.61, 'clicks': 1103, 'conversions': 115.0, 'revenue': 283.26, 'impressions': 37109}, {'label': 'Morning Audience - Brand Awareness', 'value': 48897.0, 'spend': 582.48, 'clicks': 1187, 'conversions': 19.57, 'revenue': 735.11, 'impressions': 48897}, {'label': 'Weekend Audience - Brand Awareness', 'value': 46293.0, 'spend': 581.99, 'clicks': 1204, 'conversions': 15.98, 'revenue': 505.15, 'impressions': 46293}, {'label': 'Morning Audience - Summer Sale Campaign', 'value': 38994.0, 'spend': 512.05, 'clicks': 1445, 'conversions': 74.0, 'revenue': 10549.28, 'impressions': 38994}] workspace_avg=5809221.0
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The "Morning Audience - Lead Gen - B2B" ad set had the highest impressions last week at 44,908. Overall, your ad sets were right on the average with 5,809,221 impressions. It's good to see consistent performance across the board!'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 2174ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 4178ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The "Morning Audience - Lead Gen - B2B" ad set had the highest impressions last week at 44,908. Overall, your ad sets were right on the average with 5,809,221 impressions. It's good to see consistent performance across the board!'
```

---

## Test 83: How is the Summer Sale campaign performing?

**Answer**:
> The Summer Sale campaign had a ROAS of 16.48× last week, which is way above your average of 6.34×—that's excellent! It's really outperforming the rest of your campaigns.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': 'campaign', 'entity_ids': None, 'status': None, 'entity_name': 'Summer Sale', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How is the Summer Sale campaign performing?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1097ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': 'campaign', 'entity_ids': None, 'status': None, 'entity_name': 'Summer Sale', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level='campaign', entity_ids=None, status=None, entity_name='Summer Sale', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How is the Summer Sale campaign performing?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=campaign, status=None, entity_name=Summer Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Summer Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Summer Sale Campaign (ID: d02a69cb-5368-488f-93ec-993c747a2299, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Summer Sale Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity d02a69cb-5368-488f-93ec-993c747a2299 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Summer Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('5962.4200'), 'revenue': Decimal('98282.6500'), 'clicks': 15616, 'impressions': 449445, 'conversions': Decimal('789.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 789, 'visitors': 14324, 'profit': Decimal('30741.9900')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('16.48368447710828824537687717'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Summer Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Summer Sale Campaign (ID: d02a69cb-5368-488f-93ec-993c747a2299, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Summer Sale Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity d02a69cb-5368-488f-93ec-993c747a2299 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Summer Sale': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=16.483684477108287 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 12.662731796576885}, {'date': '2025-10-23', 'value': 13.359867964694908}, {'date': '2025-10-24', 'value': 15.839533666640685}, {'date': '2025-10-25', 'value': 19.830677246806065}, {'date': '2025-10-26', 'value': 16.128154187210022}, {'date': '2025-10-27', 'value': 20.44106446485139}, {'date': '2025-10-28', 'value': 17.060630646736065}] breakdown=None workspace_avg=6.34327533838701
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Summer Sale campaign had a ROAS of 16.48× last week, which is way above your average of 6.34×—that's excellent! It's really outperforming the rest of your campaigns.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1344ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2739ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Summer Sale campaign had a ROAS of 16.48× last week, which is way above your average of 6.34×—that's excellent! It's really outperforming the rest of your campaigns.'
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.ENTITIES: 'entities'>, 'metric': None, 'time_range': None, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': 'campaign', 'entity_ids': None, 'status': None, 'entity_name': 'lead gen', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Show me all lead gen campaigns', 'timeframe_description': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1203ms
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
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1332ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your 1 campaigns:
```

---

## Test 85: What's the CPA for Morning Audience adsets?

**Answer**:
> The CPA for Morning Audience adsets was $11.46 last week.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'cpa', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': 'adset', 'entity_ids': None, 'status': None, 'entity_name': 'Morning Audience', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's the CPA for Morning Audience adsets?", 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1209ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived='cpa', need_timeseries=True, need_previous=False, base_measures=['conversions', 'spend'], filters={'provider': None, 'level': 'adset', 'entity_ids': None, 'status': None, 'entity_name': 'Morning Audience', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='cpa', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level='adset', entity_ids=None, status=None, entity_name='Morning Audience', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's the CPA for Morning Audience adsets?", timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['cpa']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=adset, status=None, entity_name=Morning Audience
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Morning Audience'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Morning Audience - Holiday Sale - Purchases (ID: 2097b889-0ce5-4e1c-854d-b6099229bd5c, Level: LevelEnum.adset)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using adset hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 4 descendants for Morning Audience - Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 2097b889-0ce5-4e1c-854d-b6099229bd5c from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 3 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Morning Audience': 3 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('1191.5700'), 'revenue': Decimal('14778.9200'), 'clicks': 2138, 'impressions': 114602, 'conversions': Decimal('104.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 104, 'visitors': 1957, 'profit': Decimal('4218.5100')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpa
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpa: 5.277661300643196041287150457
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpa': MetricValue(value=Decimal('11.45740384615384615384615385'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 5.277661300643196041287150457
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Morning Audience'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Morning Audience - Holiday Sale - Purchases (ID: 2097b889-0ce5-4e1c-854d-b6099229bd5c, Level: LevelEnum.adset)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using adset hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 4 descendants for Morning Audience - Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 2097b889-0ce5-4e1c-854d-b6099229bd5c from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 3 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Morning Audience': 3 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=11.457403846153847 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 13.6575}, {'date': '2025-10-23', 'value': 25.418}, {'date': '2025-10-24', 'value': 17.85181818181818}, {'date': '2025-10-25', 'value': 9.467272727272727}, {'date': '2025-10-26', 'value': 5.705454545454545}, {'date': '2025-10-27', 'value': 13.595833333333333}, {'date': '2025-10-28', 'value': 12.135384615384615}] breakdown=None workspace_avg=5.277661300643196
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The CPA for Morning Audience adsets was $11.46 last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 692ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2202ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The CPA for Morning Audience adsets was $11.46 last week.'
```

---

## Test 86: What's the revenue for Black Friday campaign?

**Answer**:
> The revenue for the Black Friday campaign was $50,828.08 last week.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'revenue', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Black Friday Deals', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's the revenue for Black Friday campaign?", 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1472ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Black Friday Deals', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='revenue', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Black Friday Deals', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's the revenue for Black Friday campaign?", timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Black Friday Deals
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Black Friday Deals'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Black Friday Deals (ID: a15bf796-74ca-4556-91f6-00d91bb89cea, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Black Friday Deals
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity a15bf796-74ca-4556-91f6-00d91bb89cea from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Black Friday Deals': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('4410.2600'), 'revenue': Decimal('50828.0800'), 'clicks': 8497, 'impressions': 438730, 'conversions': Decimal('403.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 403, 'visitors': 7775, 'profit': Decimal('15141.0900')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for revenue
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for revenue: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'revenue': MetricValue(value=50828.08, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 423782.3
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Black Friday Deals'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Black Friday Deals (ID: a15bf796-74ca-4556-91f6-00d91bb89cea, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Black Friday Deals
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity a15bf796-74ca-4556-91f6-00d91bb89cea from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Black Friday Deals': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=50828.08 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 6369.85}, {'date': '2025-10-23', 'value': 7512.19}, {'date': '2025-10-24', 'value': 4374.02}, {'date': '2025-10-25', 'value': 6957.24}, {'date': '2025-10-26', 'value': 7329.05}, {'date': '2025-10-27', 'value': 8993.1}, {'date': '2025-10-28', 'value': 9292.63}] breakdown=None workspace_avg=423782.3
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The revenue for the Black Friday campaign was $50,828.08 last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 1542ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 3287ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The revenue for the Black Friday campaign was $50,828.08 last week.'
```

---

## Test 87: Give me ROAS for App Install campaigns

**Answer**:
> Sure! Here's a breakdown of the ROAS for your App Install campaigns from last week:

1. **Weekend Audience - App Install Campaign**: This campaign had a ROAS of 0.62. With a spend of $2,342.82, it generated $1,455.13 in revenue.

2. **Evening Audience - App Install Campaign**: The ROAS for this campaign was 0.58. It spent $2,141.46 and brought in $1,252.05 in revenue.

3. **Morning Audience - App Install Campaign**: This campaign achieved a ROAS of 0.48. It had a spend of $2,485.62 and resulted in $1,185.40 in revenue.

In total, there were 3 campaigns analyzed for the last week. Let me know if you need any more details!

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'roas', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'App Install Campaign', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Give me ROAS for App Install campaigns', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1068ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived='roas', need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'App Install Campaign', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='roas', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='App Install Campaign', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Give me ROAS for App Install campaigns', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install Campaign'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install Campaign': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('6969.9000'), 'revenue': Decimal('3892.5800'), 'clicks': 16415, 'impressions': 483719, 'conversions': Decimal('1650.0000'), 'leads': Decimal('0'), 'installs': 1650, 'purchases': 0, 'visitors': 0, 'profit': Decimal('1107.1000')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('0.5584843398040144047977732823'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install Campaign'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install Campaign': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for roas by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 5, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity by name (exact first): 'App Install Campaign'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Routing named-entity same-level breakdown to child level: campaign→adset
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install Campaign'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install Campaign': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.5584843398040144 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 0.46945941601022106}, {'date': '2025-10-23', 'value': 0.5285763656392423}, {'date': '2025-10-24', 'value': 0.7004389951459127}, {'date': '2025-10-25', 'value': 0.5166284466584009}, {'date': '2025-10-26', 'value': 0.469401159946894}, {'date': '2025-10-27', 'value': 0.5984178369505745}, {'date': '2025-10-28', 'value': 0.5984936049981491}] breakdown=[{'label': 'Weekend Audience - App Install Campaign', 'value': 0.6211019199084864, 'spend': 2342.82, 'clicks': 5763, 'conversions': 542.0, 'revenue': 1455.13, 'impressions': 166390}, {'label': 'Evening Audience - App Install Campaign', 'value': 0.5846712056260682, 'spend': 2141.46, 'clicks': 5436, 'conversions': 526.0, 'revenue': 1252.05, 'impressions': 150709}, {'label': 'Morning Audience - App Install Campaign', 'value': 0.4769031469009744, 'spend': 2485.62, 'clicks': 5216, 'conversions': 582.0, 'revenue': 1185.4, 'impressions': 166620}] workspace_avg=6.34327533838701
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Sure! Here's a breakdown of the ROAS for your App Install campaigns from last week:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 3489ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 5014ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Sure! Here's a breakdown of the ROAS for your App Install campaigns from last week:
```

---

## Test 88: Show me Weekend Audience adsets

**Answer**:
> Here are your 10 adsets:
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.ENTITIES: 'entities'>, 'metric': None, 'time_range': None, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': 'adset', 'entity_ids': None, 'status': None, 'entity_name': 'Weekend Audience', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Show me Weekend Audience adsets', 'timeframe_description': None}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 972ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: None
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting entity list for level: adset
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'entities': [{'name': 'Weekend Audience - App Install Campaign', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}, {'name': 'Weekend Audience - Black Friday Deals', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}, {'name': 'Weekend Audience - Brand Awareness', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}, {'name': 'Weekend Audience - General Conversions', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}, {'name': 'Weekend Audience - Holiday Sale - Purchases', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}, {'name': 'Weekend Audience - Lead Gen - B2B', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}, {'name': 'Weekend Audience - Mobile Game Installs', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}, {'name': 'Weekend Audience - Newsletter Signup Campaign', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}, {'name': 'Weekend Audience - Product Launch Teaser', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}, {'name': 'Weekend Audience - Summer Sale Campaign', 'status': 'active', 'level': <LevelEnum.adset: 'adset'>}]}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your 10 adsets:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 0ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1083ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your 10 adsets:
```

---

## Test 89: What's the CTR for Evening Audience adsets?

**Answer**:
> The CTR for Evening Audience adsets was 2.0% last week.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'ctr', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': 'adset', 'entity_ids': None, 'status': None, 'entity_name': 'Evening Audience', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's the CTR for Evening Audience adsets?", 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1108ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived='ctr', need_timeseries=True, need_previous=False, base_measures=['clicks', 'impressions'], filters={'provider': None, 'level': 'adset', 'entity_ids': None, 'status': None, 'entity_name': 'Evening Audience', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='ctr', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level='adset', entity_ids=None, status=None, entity_name='Evening Audience', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's the CTR for Evening Audience adsets?", timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['ctr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=adset, status=None, entity_name=Evening Audience
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Evening Audience'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Evening Audience - Holiday Sale - Purchases (ID: a7408419-eb16-4c3b-80ec-d7cf998782c5, Level: LevelEnum.adset)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using adset hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 4 descendants for Evening Audience - Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity a7408419-eb16-4c3b-80ec-d7cf998782c5 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 3 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Evening Audience': 3 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('838.0900'), 'revenue': Decimal('10462.3600'), 'clicks': 1867, 'impressions': 91268, 'conversions': Decimal('74.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 74, 'visitors': 1707, 'profit': Decimal('2859.8600')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for ctr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for ctr: 0.025313548925062414
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'ctr': MetricValue(value=0.02045623876933865, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.025313548925062414
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Evening Audience'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Evening Audience - Holiday Sale - Purchases (ID: a7408419-eb16-4c3b-80ec-d7cf998782c5, Level: LevelEnum.adset)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using adset hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 4 descendants for Evening Audience - Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity a7408419-eb16-4c3b-80ec-d7cf998782c5 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 3 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Evening Audience': 3 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=0.02045623876933865 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 0.017182837740508283}, {'date': '2025-10-23', 'value': 0.021215733015494637}, {'date': '2025-10-24', 'value': 0.02082675923004102}, {'date': '2025-10-25', 'value': 0.01669613042624239}, {'date': '2025-10-26', 'value': 0.026903342116211343}, {'date': '2025-10-27', 'value': 0.025787374501444093}, {'date': '2025-10-28', 'value': 0.018198896324997063}] breakdown=None workspace_avg=0.025313548925062414
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The CTR for Evening Audience adsets was 2.0% last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 811ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2203ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The CTR for Evening Audience adsets was 2.0% last week.'
```

---

## Test 90: How much did Holiday Sale campaign spend last week?

**Answer**:
> The Holiday Sale campaign spent $4,360.41 last week.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': 'spend', 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'How much did Holiday Sale campaign spend last week?', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1104ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Holiday Sale', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric='spend', time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Holiday Sale', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='How much did Holiday Sale campaign spend last week?', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 1 metrics: ['spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('4360.4100'), 'revenue': Decimal('55467.0000'), 'clicks': 8539, 'impressions': 434535, 'conversions': Decimal('400.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 400, 'visitors': 7814, 'profit': Decimal('16818.4700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 66808.12
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=4360.41, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 66808.12
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 1 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: summary=4360.41 previous=None delta_pct=None timeseries=[{'date': '2025-10-22', 'value': 605.85}, {'date': '2025-10-23', 'value': 584.46}, {'date': '2025-10-24', 'value': 696.32}, {'date': '2025-10-25', 'value': 647.66}, {'date': '2025-10-26', 'value': 649.12}, {'date': '2025-10-27', 'value': 662.92}, {'date': '2025-10-28', 'value': 514.08}] breakdown=None workspace_avg=66808.12
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'The Holiday Sale campaign spent $4,360.41 last week.'
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 694ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2115ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'The Holiday Sale campaign spent $4,360.41 last week.'
```

---

## Test 91: Compare CPC, CTR, and ROAS for Holiday Sale and App Install campaigns last week

**Answer**:
> Last week, when comparing the Holiday Sale and App Install campaigns, we observed some interesting differences in their performance metrics.

For CPC (Cost Per Click), the App Install campaign had a lower cost at $0.42 compared to the Holiday Sale's $0.51. This indicates that the App Install campaign was more cost-effective in terms of attracting clicks.

Looking at CTR (Click-Through Rate), the App Install campaign again outperformed with a higher rate of 3.39%, while the Holiday Sale campaign had a CTR of 1.97%. This suggests that the App Install ads were more engaging and effective at encouraging users to click.

However, the ROAS (Return on Ad Spend) tells a different story. The Holiday Sale campaign achieved a significantly higher ROAS of 12.72, indicating a strong return on investment. In contrast, the App Install campaign had a much lower ROAS of 0.56, suggesting it was less effective in generating revenue relative to the ad spend.

In summary, while the App Install campaign was more efficient in terms of cost and engagement, the Holiday Sale campaign delivered far superior returns on investment.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.COMPARISON: 'comparison'>, 'metric': None, 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': 'entity_vs_entity', 'comparison_entities': ['Holiday Sale', 'App Install'], 'comparison_metrics': ['cpc', 'ctr', 'roas'], 'question': 'Compare CPC, CTR, and ROAS for Holiday Sale and App Install campaigns last week', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1618ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['clicks', 'impressions', 'revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.COMPARISON: 'comparison'>, metric=None, time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type='entity_vs_entity', comparison_entities=['Holiday Sale', 'App Install'], comparison_metrics=['cpc', 'ctr', 'roas'], question='Compare CPC, CTR, and ROAS for Holiday Sale and App Install campaigns last week', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.dsl.executor:[COMPARISON] Executing comparison plan for type: entity_vs_entity
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['cpc', 'ctr', 'roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('4360.4100'), 'revenue': Decimal('55467.0000'), 'clicks': 8539, 'impressions': 434535, 'conversions': Decimal('400.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 400, 'visitors': 7814, 'profit': Decimal('16818.4700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4543162962761472132306939042
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.5106464457196393020259983605'), previous=None, delta_pct=None), 'ctr': MetricValue(value=0.01965089118252845, previous=None, delta_pct=None), 'roas': MetricValue(value=Decimal('12.72059278829284402154843237'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4543162962761472132306939042
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['cpc', 'ctr', 'roas']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=App Install
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('6969.9000'), 'revenue': Decimal('3892.5800'), 'clicks': 16415, 'impressions': 483719, 'conversions': Decimal('1650.0000'), 'leads': Decimal('0'), 'installs': 1650, 'purchases': 0, 'visitors': 0, 'profit': Decimal('1107.1000')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4543162962761472132306939042
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.4246055437100213219616204691'), previous=None, delta_pct=None), 'ctr': MetricValue(value=0.03393499118289751, previous=None, delta_pct=None), 'roas': MetricValue(value=Decimal('0.5584843398040144047977732823'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4543162962761472132306939042
INFO:app.dsl.executor:[COMPARISON] Completed execution for 2 items
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'comparison': [{'entity': 'Holiday Sale', 'cpc': Decimal('0.5106464457196393020259983605'), 'ctr': 0.01965089118252845, 'roas': Decimal('12.72059278829284402154843237')}, {'entity': 'App Install', 'cpc': Decimal('0.4246055437100213219616204691'), 'ctr': 0.03393499118289751, 'roas': Decimal('0.5584843398040144047977732823')}], 'comparison_type': 'entity_vs_entity', 'metrics': ['cpc', 'ctr', 'roas'], 'query_type': 'comparison'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Last week, when comparing the Holiday Sale and App Install campaigns, we observed some interesting differences in their performance metrics.
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 4412ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 6341ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Last week, when comparing the Holiday Sale and App Install campaigns, we observed some interesting differences in their performance metrics.
```

---

## Test 92: What's the spend, revenue, and ROAS for all Google campaigns in September?

**Answer**:
> Here are your metrics from 2025-09-01 to 2025-09-30:

• SPEND: $8,272.52
• REVENUE: $56,264.09
• ROAS: 6.80×

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': ['spend', 'revenue', 'roas'], 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 9, 1), 'end': datetime.date(2025, 9, 30)}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': 'google', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's the spend, revenue, and ROAS for all Google campaigns in September?", 'timeframe_description': 'from 2025-09-01 to 2025-09-30'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1174ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 1), end=datetime.date(2025, 9, 30), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': 'google', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric=['spend', 'revenue', 'roas'], time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 9, 1), end=datetime.date(2025, 9, 30)), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider='google', level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's the spend, revenue, and ROAS for all Google campaigns in September?", timeframe_description='from 2025-09-01 to 2025-09-30'))
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
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'metrics': {'spend': {'summary': 8272.52, 'previous': None, 'delta_pct': None}, 'revenue': {'summary': 56264.09, 'previous': None, 'delta_pct': None}, 'roas': {'summary': Decimal('6.801324143066441664692258224'), 'previous': None, 'delta_pct': None}}, 'timeseries': [{'date': '2025-09-29', 'value': 4152.06}, {'date': '2025-09-30', 'value': 4120.46}], 'breakdown': None, 'query_type': 'multi_metrics'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your metrics from 2025-09-01 to 2025-09-30:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: Nonems
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1397ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your metrics from 2025-09-01 to 2025-09-30:
```

---

## Test 93: Show me clicks, conversions, and cost per conversion for Meta campaigns last 5 days

**Answer**:
> Here are your metrics in the last 5 days:

• CLICKS: 24,374
• CONVERSIONS: 2,344
• CPA: $5.34

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': ['clicks', 'conversions', 'cpa'], 'time_range': {'last_n_days': 5, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': 'meta', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Show me clicks, conversions, and cost per conversion for Meta campaigns last 5 days', 'timeframe_description': 'last 5 days'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 835ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 24), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['clicks', 'conversions', 'spend'], filters={'provider': 'meta', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric=['clicks', 'conversions', 'cpa'], time_range=TimeRange(last_n_days=5, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider='meta', level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Show me clicks, conversions, and cost per conversion for Meta campaigns last 5 days', timeframe_description='last 5 days'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['clicks', 'conversions', 'cpa']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 24) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=meta, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-24 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('12504.2500'), 'revenue': Decimal('125290.4200'), 'clicks': 24374, 'impressions': 1233768, 'conversions': Decimal('2343.5300'), 'leads': Decimal('1085.2300'), 'installs': 0, 'purchases': 668, 'visitors': 22135, 'profit': Decimal('37523.2500')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for clicks
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for clicks: 105350.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'clicks': MetricValue(value=24374.0, previous=None, delta_pct=None), 'conversions': MetricValue(value=2343.53, previous=None, delta_pct=None), 'cpa': MetricValue(value=Decimal('5.335647506112573766924255290'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 105350.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 3 metrics
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'metrics': {'clicks': {'summary': 24374.0, 'previous': None, 'delta_pct': None}, 'conversions': {'summary': 2343.53, 'previous': None, 'delta_pct': None}, 'cpa': {'summary': Decimal('5.335647506112573766924255290'), 'previous': None, 'delta_pct': None}}, 'timeseries': [{'date': '2025-10-24', 'value': 4205.0}, {'date': '2025-10-25', 'value': 4760.0}, {'date': '2025-10-26', 'value': 4894.0}, {'date': '2025-10-27', 'value': 5886.0}, {'date': '2025-10-28', 'value': 4629.0}], 'breakdown': None, 'query_type': 'multi_metrics'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your metrics in the last 5 days:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: Nonems
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1032ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your metrics in the last 5 days:
```

---

## Test 94: Give me CTR, CPC, and conversion rate for Summer Sale campaign last month

**Answer**:
> Here are your metrics in the last 30 days:

• CTR: 3.5%
• CPC: $0.41
• CVR: 5.0%

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
  "timeframe_description": "last month"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': ['ctr', 'cpc', 'cvr'], 'time_range': {'last_n_days': 30, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Summer Sale', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Give me CTR, CPC, and conversion rate for Summer Sale campaign last month', 'timeframe_description': 'last month'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1016ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 29), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['clicks', 'conversions', 'impressions', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Summer Sale', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric=['ctr', 'cpc', 'cvr'], time_range=TimeRange(last_n_days=30, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Summer Sale', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Give me CTR, CPC, and conversion rate for Summer Sale campaign last month', timeframe_description='last month'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['ctr', 'cpc', 'cvr']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 29) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Summer Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-29 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Summer Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Summer Sale Campaign (ID: d02a69cb-5368-488f-93ec-993c747a2299, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Summer Sale Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity d02a69cb-5368-488f-93ec-993c747a2299 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Summer Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('27041.5900'), 'revenue': Decimal('414036.1900'), 'clicks': 66750, 'impressions': 1910709, 'conversions': Decimal('3326.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 3326, 'visitors': 61240, 'profit': Decimal('126856.5100')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for ctr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for ctr: 0.025396144122628354
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'ctr': MetricValue(value=0.03493467608097309, previous=None, delta_pct=None), 'cpc': MetricValue(value=Decimal('0.4051174531835205992509363296'), previous=None, delta_pct=None), 'cvr': MetricValue(value=Decimal('0.04982771535580524344569288390'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.025396144122628354
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 3 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Summer Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Summer Sale Campaign (ID: d02a69cb-5368-488f-93ec-993c747a2299, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Summer Sale Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity d02a69cb-5368-488f-93ec-993c747a2299 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Summer Sale': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'metrics': {'ctr': {'summary': 0.03493467608097309, 'previous': None, 'delta_pct': None}, 'cpc': {'summary': Decimal('0.4051174531835205992509363296'), 'previous': None, 'delta_pct': None}, 'cvr': {'summary': Decimal('0.04982771535580524344569288390'), 'previous': None, 'delta_pct': None}}, 'timeseries': [{'date': '2025-09-29', 'value': 0.03364277577138425}, {'date': '2025-09-30', 'value': 0.0317864427471824}, {'date': '2025-10-01', 'value': 0.030866601752677702}, {'date': '2025-10-02', 'value': 0.037178472189881864}, {'date': '2025-10-03', 'value': 0.034906186939161046}, {'date': '2025-10-04', 'value': 0.03245268224685819}, {'date': '2025-10-05', 'value': 0.03764044145846058}, {'date': '2025-10-06', 'value': 0.03353455411762331}, {'date': '2025-10-07', 'value': 0.03308994448546504}, {'date': '2025-10-08', 'value': 0.027772114977496903}, {'date': '2025-10-09', 'value': 0.03384909164628484}, {'date': '2025-10-10', 'value': 0.036603750829162396}, {'date': '2025-10-11', 'value': 0.03518899760171488}, {'date': '2025-10-12', 'value': 0.038713641950020486}, {'date': '2025-10-13', 'value': 0.03758238861059847}, {'date': '2025-10-14', 'value': 0.03559504022827894}, {'date': '2025-10-15', 'value': 0.033847613843875364}, {'date': '2025-10-16', 'value': 0.03616204841647363}, {'date': '2025-10-17', 'value': 0.033036336871465094}, {'date': '2025-10-18', 'value': 0.038970990695128625}, {'date': '2025-10-19', 'value': 0.034915001197166236}, {'date': '2025-10-20', 'value': 0.038659394731861745}, {'date': '2025-10-21', 'value': 0.038405229144792295}, {'date': '2025-10-22', 'value': 0.03233697729531381}, {'date': '2025-10-23', 'value': 0.03407834280819251}, {'date': '2025-10-24', 'value': 0.034273958211742735}, {'date': '2025-10-25', 'value': 0.03761358341099721}, {'date': '2025-10-26', 'value': 0.0318005398584868}, {'date': '2025-10-27', 'value': 0.03949970041941282}, {'date': '2025-10-28', 'value': 0.03291524278042735}], 'breakdown': None, 'query_type': 'multi_metrics'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your metrics in the last 30 days:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: Nonems
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1299ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your metrics in the last 30 days:
```

---

## Test 95: Compare spend and revenue between Morning Audience and Evening Audience adsets this month to date

**Answer**:
> From October 1 to 28, let's take a look at how the Morning Audience and Evening Audience ad sets performed in terms of spend and revenue.

Starting with spend, the Evening Audience had a higher expenditure, totaling $4,882.90, compared to the Morning Audience's spend of $4,255.33. This indicates that more budget was allocated to the Evening Audience during this period.

When it comes to revenue, the Evening Audience also outperformed, generating $55,810.28, whereas the Morning Audience brought in $47,319.80. This suggests that the Evening Audience not only had a higher spend but also achieved greater revenue.

In summary, the Evening Audience ad set had both higher spend and revenue compared to the Morning Audience from October 1 to 28, indicating a stronger financial performance overall.

**DSL**:
```json
{
  "query_type": "comparison",
  "metric": null,
  "time_range": {
    "last_n_days": null,
    "start": "2025-10-01",
    "end": "2025-10-28"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.COMPARISON: 'comparison'>, 'metric': None, 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 10, 1), 'end': datetime.date(2025, 10, 28)}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': 'adset', 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': 'entity_vs_entity', 'comparison_entities': ['Morning Audience', 'Evening Audience'], 'comparison_metrics': ['spend', 'revenue'], 'question': 'Compare spend and revenue between Morning Audience and Evening Audience adsets this month to date', 'timeframe_description': 'this month'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1060ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['revenue', 'spend'], filters={'provider': None, 'level': 'adset', 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.COMPARISON: 'comparison'>, metric=None, time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 28)), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level='adset', entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type='entity_vs_entity', comparison_entities=['Morning Audience', 'Evening Audience'], comparison_metrics=['spend', 'revenue'], question='Compare spend and revenue between Morning Audience and Evening Audience adsets this month to date', timeframe_description='this month'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.dsl.executor:[COMPARISON] Executing comparison plan for type: entity_vs_entity
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 2 metrics: ['spend', 'revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=adset, status=None, entity_name=Morning Audience
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-28
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
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=adset, status=None, entity_name=Evening Audience
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-28
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
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'From October 1 to 28, let's take a look at how the Morning Audience and Evening Audience ad sets performed in terms of spend and revenue.
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 3502ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 4886ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'From October 1 to 28, let's take a look at how the Morning Audience and Evening Audience ad sets performed in terms of spend and revenue.
```

---

## Test 96: What's the ROAS, revenue, and profit for Black Friday campaign last week?

**Answer**:
> Here are your metrics last week:

• ROAS: 11.52×
• REVENUE: $50,828.08
• PROFIT: $15,141.09

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
  "timeframe_description": "last week"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': ['roas', 'revenue', 'profit'], 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Black Friday', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's the ROAS, revenue, and profit for Black Friday campaign last week?", 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 952ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['profit', 'revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Black Friday', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric=['roas', 'revenue', 'profit'], time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Black Friday', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's the ROAS, revenue, and profit for Black Friday campaign last week?", timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['roas', 'revenue', 'profit']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Black Friday
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Black Friday'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Black Friday Deals (ID: a15bf796-74ca-4556-91f6-00d91bb89cea, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Black Friday Deals
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity a15bf796-74ca-4556-91f6-00d91bb89cea from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Black Friday': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('4410.2600'), 'revenue': Decimal('50828.0800'), 'clicks': 8497, 'impressions': 438730, 'conversions': Decimal('403.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 403, 'visitors': 7775, 'profit': Decimal('15141.0900')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for roas
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for roas: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'roas': MetricValue(value=Decimal('11.52496224712375234113181536'), previous=None, delta_pct=None), 'revenue': MetricValue(value=50828.08, previous=None, delta_pct=None), 'profit': MetricValue(value=15141.09, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 6.343275338387010441245764736
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 3 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Black Friday'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Black Friday Deals (ID: a15bf796-74ca-4556-91f6-00d91bb89cea, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Black Friday Deals
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity a15bf796-74ca-4556-91f6-00d91bb89cea from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Black Friday': 12 descendants
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'metrics': {'roas': {'summary': Decimal('11.52496224712375234113181536'), 'previous': None, 'delta_pct': None}, 'revenue': {'summary': 50828.08, 'previous': None, 'delta_pct': None}, 'profit': {'summary': 15141.09, 'previous': None, 'delta_pct': None}}, 'timeseries': [{'date': '2025-10-22', 'value': Decimal('11.37960911819351150493068458')}, {'date': '2025-10-23', 'value': Decimal('10.27814034943698778201918209')}, {'date': '2025-10-24', 'value': Decimal('8.021015183745323846548815374')}, {'date': '2025-10-25', 'value': Decimal('14.52875579501315624608445057')}, {'date': '2025-10-26', 'value': Decimal('11.60412609446001361642837917')}, {'date': '2025-10-27', 'value': Decimal('10.01001769793301499315457308')}, {'date': '2025-10-28', 'value': Decimal('16.43462497568222414799356242')}], 'breakdown': None, 'query_type': 'multi_metrics'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your metrics last week:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: Nonems
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1236ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your metrics last week:
```

---

## Test 97: Show me CPC, clicks, and spend for all active campaigns last 5 days

**Answer**:
> Here are your metrics in the last 5 days:

• CPC: $0.45
• CLICKS: 100,659
• SPEND: $45,081.96

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': ['cpc', 'clicks', 'spend'], 'time_range': {'last_n_days': 5, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': 'active', 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Show me CPC, clicks, and spend for all active campaigns last 5 days', 'timeframe_description': 'last 5 days'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 976ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 24), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['clicks', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': 'active', 'entity_name': None, 'metric_filters': None}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric=['cpc', 'clicks', 'spend'], time_range=TimeRange(last_n_days=5, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status='active', entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Show me CPC, clicks, and spend for all active campaigns last 5 days', timeframe_description='last 5 days'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['cpc', 'clicks', 'spend']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 24) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=active, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-24 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('45081.9600'), 'revenue': Decimal('283059.6100'), 'clicks': 100659, 'impressions': 3882429, 'conversions': Decimal('8373.8500'), 'leads': Decimal('3504.3300'), 'installs': 2020, 'purchases': 1317, 'visitors': 71863, 'profit': Decimal('85117.6200')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpc: 0.4507023255813953488372093023
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpc': MetricValue(value=Decimal('0.4478681488987571901171281257'), previous=None, delta_pct=None), 'clicks': MetricValue(value=100659.0, previous=None, delta_pct=None), 'spend': MetricValue(value=45081.96, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.4507023255813953488372093023
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 3 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cpc by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 24) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=active, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-24 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'metrics': {'cpc': {'summary': Decimal('0.4478681488987571901171281257'), 'previous': None, 'delta_pct': None}, 'clicks': {'summary': 100659.0, 'previous': None, 'delta_pct': None}, 'spend': {'summary': 45081.96, 'previous': None, 'delta_pct': None}}, 'timeseries': [{'date': '2025-10-24', 'value': Decimal('0.4352257815515245079120030876')}, {'date': '2025-10-25', 'value': Decimal('0.4292217879080156353114371288')}, {'date': '2025-10-26', 'value': Decimal('0.4602913940613990941117262204')}, {'date': '2025-10-27', 'value': Decimal('0.4535267021736001151576219951')}, {'date': '2025-10-28', 'value': Decimal('0.4614220582961938425285589878')}], 'breakdown': [{'label': 'Holiday Sale - Purchases', 'value': Decimal('0.6624235294117647058823529412'), 'spend': Decimal('281.5300'), 'clicks': 425, 'conversions': Decimal('20.0000'), 'revenue': Decimal('1753.4400'), 'impressions': 22825}, {'label': 'Product Launch Teaser', 'value': Decimal('0.6272386058981233243967828418'), 'spend': Decimal('233.9600'), 'clicks': 373, 'conversions': Decimal('11.3000'), 'revenue': Decimal('375.3000'), 'impressions': 27305}, {'label': 'Lead Gen - B2B', 'value': Decimal('0.5902195791399817017383348582'), 'spend': Decimal('645.1100'), 'clicks': 1093, 'conversions': Decimal('191.4000'), 'revenue': Decimal('1256.9300'), 'impressions': 36215}, {'label': 'Mobile Game Installs', 'value': Decimal('0.5318947368421052631578947368'), 'spend': Decimal('252.6500'), 'clicks': 475, 'conversions': Decimal('49.0000'), 'revenue': Decimal('164.9100'), 'impressions': 19527}, {'label': 'Black Friday Deals', 'value': Decimal('0.5290'), 'spend': Decimal('248.6300'), 'clicks': 470, 'conversions': Decimal('23.0000'), 'revenue': Decimal('3769.2900'), 'impressions': 22841}, {'label': 'General Conversions', 'value': Decimal('0.5091966173361522198731501057'), 'spend': Decimal('240.8500'), 'clicks': 473, 'conversions': Decimal('44.1900'), 'revenue': Decimal('3512.1000'), 'impressions': 21549}, {'label': 'Newsletter Signup Campaign', 'value': Decimal('0.4960'), 'spend': Decimal('260.4000'), 'clicks': 525, 'conversions': Decimal('87.7500'), 'revenue': Decimal('243.4000'), 'impressions': 25757}, {'label': 'Brand Awareness', 'value': Decimal('0.4204952380952380952380952381'), 'spend': Decimal('220.7600'), 'clicks': 525, 'conversions': Decimal('9.3200'), 'revenue': Decimal('405.0700'), 'impressions': 20863}, {'label': 'App Install Campaign', 'value': Decimal('0.3883333333333333333333333333'), 'spend': Decimal('202.7100'), 'clicks': 522, 'conversions': Decimal('46.0000'), 'revenue': Decimal('109.2200'), 'impressions': 16823}, {'label': 'Summer Sale Campaign', 'value': Decimal('0.3858803611738148984198645598'), 'spend': Decimal('341.8900'), 'clicks': 886, 'conversions': Decimal('48.0000'), 'revenue': Decimal('6889.0000'), 'impressions': 24813}], 'query_type': 'multi_metrics'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your metrics in the last 5 days:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: Nonems
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1182ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your metrics in the last 5 days:
```

---

## Test 98: Compare CTR and conversion rate for Google vs Meta campaigns in September

**Answer**:
> ERROR

**DSL**:
```json
{}
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
```

---

## Test 99: What's the revenue, ROAS, and cost per lead for lead gen campaigns this month to date?

**Answer**:
> Here are your metrics from October 01 to 28:

• REVENUE: $60,191.63
• ROAS: 2.24×
• CPL: $2.28

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
    "end": "2025-10-28"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': ['revenue', 'roas', 'cpl'], 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 10, 1), 'end': datetime.date(2025, 10, 28)}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'lead gen', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's the revenue, ROAS, and cost per lead for lead gen campaigns this month to date?", 'timeframe_description': 'this month'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1548ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['leads', 'revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'lead gen', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric=['revenue', 'roas', 'cpl'], time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 28)), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='lead gen', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's the revenue, ROAS, and cost per lead for lead gen campaigns this month to date?", timeframe_description='this month'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['revenue', 'roas', 'cpl']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=lead gen
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-28
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
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=lead gen
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 5, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-28
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
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your metrics from October 01 to 28:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: Nonems
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2030ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your metrics from October 01 to 28:
```

---

## Test 100: Give me spend, clicks, and CPC for Holiday Sale and Summer Sale campaigns last month

**Answer**:
> In the last 30 days, the Holiday Sale and Summer Sale campaigns showed some interesting differences in performance across spend, clicks, and CPC metrics.

Starting with spend, the Summer Sale campaign had a higher expenditure, totaling $27,041.59 compared to the Holiday Sale's $19,116.55. This indicates a more substantial investment in the Summer Sale campaign.

When it comes to clicks, the Summer Sale campaign also outperformed with 66,750 clicks, significantly more than the Holiday Sale's 37,634 clicks. This suggests that the Summer Sale campaign was more effective in driving traffic.

Looking at the cost per click (CPC), the Summer Sale campaign again had the advantage, with a lower CPC of $0.41 compared to the Holiday Sale's $0.51. A lower CPC generally indicates a more cost-efficient campaign in terms of generating clicks.

Overall, the Summer Sale campaign performed better across all three metrics, achieving more clicks at a lower cost per click with a higher overall spend.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.COMPARISON: 'comparison'>, 'metric': None, 'time_range': {'last_n_days': 30, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': 'entity_vs_entity', 'comparison_entities': ['Holiday Sale', 'Summer Sale'], 'comparison_metrics': ['spend', 'clicks', 'cpc'], 'question': 'Give me spend, clicks, and CPC for Holiday Sale and Summer Sale campaigns last month', 'timeframe_description': 'last month'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1011ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 29), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['clicks', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.COMPARISON: 'comparison'>, metric=None, time_range=TimeRange(last_n_days=30, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type='entity_vs_entity', comparison_entities=['Holiday Sale', 'Summer Sale'], comparison_metrics=['spend', 'clicks', 'cpc'], question='Give me spend, clicks, and CPC for Holiday Sale and Summer Sale campaigns last month', timeframe_description='last month'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.dsl.executor:[COMPARISON] Executing comparison plan for type: entity_vs_entity
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['spend', 'clicks', 'cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 29) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-29 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('19116.5500'), 'revenue': Decimal('224923.9900'), 'clicks': 37634, 'impressions': 1930318, 'conversions': Decimal('1689.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 1689, 'visitors': 34440, 'profit': Decimal('67851.8900')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 288394.85
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=19116.55, previous=None, delta_pct=None), 'clicks': MetricValue(value=37634.0, previous=None, delta_pct=None), 'cpc': MetricValue(value=Decimal('0.5079595578466280491045331349'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 288394.85
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['spend', 'clicks', 'cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 29) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Summer Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-29 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Summer Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Summer Sale Campaign (ID: d02a69cb-5368-488f-93ec-993c747a2299, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Summer Sale Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity d02a69cb-5368-488f-93ec-993c747a2299 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Summer Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('27041.5900'), 'revenue': Decimal('414036.1900'), 'clicks': 66750, 'impressions': 1910709, 'conversions': Decimal('3326.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 3326, 'visitors': 61240, 'profit': Decimal('126856.5100')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 288394.85
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=27041.59, previous=None, delta_pct=None), 'clicks': MetricValue(value=66750.0, previous=None, delta_pct=None), 'cpc': MetricValue(value=Decimal('0.4051174531835205992509363296'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 288394.85
INFO:app.dsl.executor:[COMPARISON] Completed execution for 2 items
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'comparison': [{'entity': 'Holiday Sale', 'spend': 19116.55, 'clicks': 37634.0, 'cpc': Decimal('0.5079595578466280491045331349')}, {'entity': 'Summer Sale', 'spend': 27041.59, 'clicks': 66750.0, 'cpc': Decimal('0.4051174531835205992509363296')}], 'comparison_type': 'entity_vs_entity', 'metrics': ['spend', 'clicks', 'cpc'], 'query_type': 'comparison'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'In the last 30 days, the Holiday Sale and Summer Sale campaigns showed some interesting differences in performance across spend, clicks, and CPC metrics.
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 7207ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 8551ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'In the last 30 days, the Holiday Sale and Summer Sale campaigns showed some interesting differences in performance across spend, clicks, and CPC metrics.
```

---

## Test 101: Show me conversion rate, revenue, and profit for all campaigns last week

**Answer**:
> Here are your metrics last week:

• CVR: 8.6%
• REVENUE: $423,782.30
• PROFIT: $128,021.27

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': ['cvr', 'revenue', 'profit'], 'time_range': {'last_n_days': 7, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Show me conversion rate, revenue, and profit for all campaigns last week', 'timeframe_description': 'last week'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1614ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 22), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['clicks', 'conversions', 'profit', 'revenue'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric=['cvr', 'revenue', 'profit'], time_range=TimeRange(last_n_days=7, start=None, end=None), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=10, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Show me conversion rate, revenue, and profit for all campaigns last week', timeframe_description='last week'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['cvr', 'revenue', 'profit']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('66808.1200'), 'revenue': Decimal('423782.3000'), 'clicks': 147052, 'impressions': 5809221, 'conversions': Decimal('12658.6600'), 'leads': Decimal('5044.4700'), 'installs': 2910, 'purchases': 1717, 'visitors': 105693, 'profit': Decimal('128021.2700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cvr
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cvr: 0.08608288224573620215978021380
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cvr': MetricValue(value=Decimal('0.08608288224573620215978021380'), previous=None, delta_pct=None), 'revenue': MetricValue(value=423782.3, previous=None, delta_pct=None), 'profit': MetricValue(value=128021.27, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 0.08608288224573620215978021380
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 3 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for cvr by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 22) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-22 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'metrics': {'cvr': {'summary': Decimal('0.08608288224573620215978021380'), 'previous': None, 'delta_pct': None}, 'revenue': {'summary': 423782.3, 'previous': None, 'delta_pct': None}, 'profit': {'summary': 128021.27, 'previous': None, 'delta_pct': None}}, 'timeseries': [{'date': '2025-10-22', 'value': Decimal('0.09119118606167893412838908041')}, {'date': '2025-10-23', 'value': Decimal('0.08583712196086183040126507215')}, {'date': '2025-10-24', 'value': Decimal('0.08755490278360609875507063925')}, {'date': '2025-10-25', 'value': Decimal('0.08713194512017125620317213195')}, {'date': '2025-10-26', 'value': Decimal('0.08163927376970855231724796942')}, {'date': '2025-10-27', 'value': Decimal('0.08539040408647268083553771778')}, {'date': '2025-10-28', 'value': Decimal('0.08366125018298931342409603279')}], 'breakdown': [{'label': 'Lead Gen - B2B', 'value': Decimal('0.1780056377730796335447498238'), 'spend': Decimal('749.9200'), 'clicks': 1419, 'conversions': Decimal('252.5900'), 'revenue': Decimal('1333.3700'), 'impressions': 45072}, {'label': 'Website Traffic Push', 'value': Decimal('0.06731142643764002987303958178'), 'spend': Decimal('513.3800'), 'clicks': 1339, 'conversions': Decimal('90.1300'), 'revenue': Decimal('4512.2700'), 'impressions': 37902}, {'label': 'Blog Content Promotion', 'value': Decimal('0.1102264150943396226415094340'), 'spend': Decimal('499.7500'), 'clicks': 795, 'conversions': Decimal('87.6300'), 'revenue': Decimal('4666.9900'), 'impressions': 44601}, {'label': 'Summer Sale Campaign', 'value': Decimal('0.05436720142602495543672014260'), 'spend': Decimal('474.1100'), 'clicks': 1122, 'conversions': Decimal('61.0000'), 'revenue': Decimal('8173.1800'), 'impressions': 33284}, {'label': 'Holiday Sale - Purchases', 'value': Decimal('0.04310344827586206896551724138'), 'spend': Decimal('391.4000'), 'clicks': 696, 'conversions': Decimal('30.0000'), 'revenue': Decimal('3056.8200'), 'impressions': 37036}, {'label': 'Product Launch Teaser', 'value': Decimal('0.02318027210884353741496598639'), 'spend': Decimal('379.6700'), 'clicks': 588, 'conversions': Decimal('13.6300'), 'revenue': Decimal('450.4100'), 'impressions': 43695}, {'label': 'Newsletter Signup Campaign', 'value': Decimal('0.1855301204819277108433734940'), 'spend': Decimal('371.4500'), 'clicks': 830, 'conversions': Decimal('153.9900'), 'revenue': Decimal('751.0800'), 'impressions': 37549}, {'label': 'Mobile Game Installs', 'value': Decimal('0.08898944193061840120663650075'), 'spend': Decimal('371.2100'), 'clicks': 663, 'conversions': Decimal('59.0000'), 'revenue': Decimal('194.0200'), 'impressions': 27442}, {'label': 'Black Friday Deals', 'value': Decimal('0.05167173252279635258358662614'), 'spend': Decimal('344.1300'), 'clicks': 658, 'conversions': Decimal('34.0000'), 'revenue': Decimal('5347.1000'), 'impressions': 34236}, {'label': 'Brand Awareness', 'value': Decimal('0.02333812949640287769784172662'), 'spend': Decimal('317.0800'), 'clicks': 695, 'conversions': Decimal('16.2200'), 'revenue': Decimal('642.1300'), 'impressions': 28790}], 'query_type': 'multi_metrics'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your metrics last week:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: Nonems
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1829ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your metrics last week:
```

---

## Test 102: Compare CPA, ROAS, and revenue for App Install campaign vs Holiday Sale campaign last 5 days

**Answer**:
> Over the last 5 days, we've seen some interesting differences between the App Install Campaign and the Holiday Sale campaign across key metrics like CPA, ROAS, and revenue.

Starting with CPA (Cost Per Acquisition), the App Install Campaign performed better, with a lower CPA of $4.18 compared to the Holiday Sale's $9.61. This indicates that the App Install Campaign was more cost-effective in acquiring customers.

When we look at ROAS (Return on Ad Spend), the Holiday Sale campaign significantly outperformed the App Install Campaign. The Holiday Sale achieved a ROAS of 14.48, meaning it generated $14.48 for every dollar spent, compared to the App Install Campaign's ROAS of just 0.59. This suggests that the Holiday Sale was much more efficient in generating revenue relative to its ad spend.

In terms of total revenue, the Holiday Sale campaign also came out on top, generating $45,905 compared to the App Install Campaign's $2,848.31. This substantial difference highlights the Holiday Sale's success in driving overall sales.

In summary, while the App Install Campaign was more cost-effective per acquisition, the Holiday Sale campaign excelled in generating higher returns and overall revenue.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.COMPARISON: 'comparison'>, 'metric': None, 'time_range': {'last_n_days': 5, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'none', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': 'entity_vs_entity', 'comparison_entities': ['App Install Campaign', 'Holiday Sale'], 'comparison_metrics': ['cpa', 'roas', 'revenue'], 'question': 'Compare CPA, ROAS, and revenue for App Install campaign vs Holiday Sale campaign last 5 days', 'timeframe_description': 'last 5 days'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 979ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 24), end=datetime.date(2025, 10, 28), group_by='none', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['conversions', 'revenue', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.COMPARISON: 'comparison'>, metric=None, time_range=TimeRange(last_n_days=5, start=None, end=None), compare_to_previous=False, group_by='none', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type='entity_vs_entity', comparison_entities=['App Install Campaign', 'Holiday Sale'], comparison_metrics=['cpa', 'roas', 'revenue'], question='Compare CPA, ROAS, and revenue for App Install campaign vs Holiday Sale campaign last 5 days', timeframe_description='last 5 days'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.dsl.executor:[COMPARISON] Executing comparison plan for type: entity_vs_entity
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['cpa', 'roas', 'revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 24) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-24 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'App Install Campaign'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: App Install Campaign (ID: 3d2aef8f-cbe3-407e-9166-689eff73bafd, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for App Install Campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 3d2aef8f-cbe3-407e-9166-689eff73bafd from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'App Install Campaign': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('4862.0900'), 'revenue': Decimal('2848.3100'), 'clicks': 11655, 'impressions': 341459, 'conversions': Decimal('1163.0000'), 'leads': Decimal('0'), 'installs': 1163, 'purchases': 0, 'visitors': 0, 'profit': Decimal('796.7700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpa
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpa: 5.296820111220807326963515782
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpa': MetricValue(value=Decimal('4.180644883920894239036973345'), previous=None, delta_pct=None), 'roas': MetricValue(value=Decimal('0.5858200897145054904372399524'), previous=None, delta_pct=None), 'revenue': MetricValue(value=2848.31, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 5.296820111220807326963515782
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['cpa', 'roas', 'revenue']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 24) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Holiday Sale
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-24 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Holiday Sale'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Holiday Sale - Purchases (ID: f2d2c4ee-b550-43ff-a17b-3b6a559a61b9, Level: LevelEnum.campaign)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using campaign hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 13 descendants for Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity f2d2c4ee-b550-43ff-a17b-3b6a559a61b9 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 12 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Holiday Sale': 12 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('3170.1000'), 'revenue': Decimal('45905.0000'), 'clicks': 6576, 'impressions': 316693, 'conversions': Decimal('330.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 330, 'visitors': 6020, 'profit': Decimal('13807.6000')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for cpa
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for cpa: 5.296820111220807326963515782
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'cpa': MetricValue(value=Decimal('9.606363636363636363636363636'), previous=None, delta_pct=None), 'roas': MetricValue(value=Decimal('14.48061575344626352480994290'), previous=None, delta_pct=None), 'revenue': MetricValue(value=45905.0, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 5.296820111220807326963515782
INFO:app.dsl.executor:[COMPARISON] Completed execution for 2 items
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'comparison': [{'entity': 'App Install Campaign', 'cpa': Decimal('4.180644883920894239036973345'), 'roas': Decimal('0.5858200897145054904372399524'), 'revenue': 2848.31}, {'entity': 'Holiday Sale', 'cpa': Decimal('9.606363636363636363636363636'), 'roas': Decimal('14.48061575344626352480994290'), 'revenue': 45905.0}], 'comparison_type': 'entity_vs_entity', 'metrics': ['cpa', 'roas', 'revenue'], 'query_type': 'comparison'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Over the last 5 days, we've seen some interesting differences between the App Install Campaign and the Holiday Sale campaign across key metrics like CPA, ROAS, and revenue.
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 4813ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 6105ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Over the last 5 days, we've seen some interesting differences between the App Install Campaign and the Holiday Sale campaign across key metrics like CPA, ROAS, and revenue.
```

---

## Test 103: What's the CTR, CPC, and conversions for Weekend Audience adsets in September?

**Answer**:
> Here are your metrics from 2025-09-01 to 2025-09-30:

• CTR: 2.0%
• CPC: $0.45
• CONVERSIONS: 20

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': ['ctr', 'cpc', 'conversions'], 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 9, 1), 'end': datetime.date(2025, 9, 30)}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': 'adset', 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Weekend Audience', 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': "What's the CTR, CPC, and conversions for Weekend Audience adsets in September?", 'timeframe_description': 'from 2025-09-01 to 2025-09-30'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1641ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 1), end=datetime.date(2025, 9, 30), group_by='adset', breakdown='adset', derived=None, need_timeseries=True, need_previous=False, base_measures=['clicks', 'conversions', 'impressions', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': 'Weekend Audience', 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric=['ctr', 'cpc', 'conversions'], time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 9, 1), end=datetime.date(2025, 9, 30)), compare_to_previous=False, group_by='adset', breakdown='adset', top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name='Weekend Audience', metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question="What's the CTR, CPC, and conversions for Weekend Audience adsets in September?", timeframe_description='from 2025-09-01 to 2025-09-30'))
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
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 5, Sort order: desc
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
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: Nonems
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 2206ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your metrics from 2025-09-01 to 2025-09-30:
```

---

## Test 104: Give me spend, revenue, ROAS, and profit for all Meta campaigns this month to date

**Answer**:
> Here are your metrics from October 01 to 28:

• SPEND: $72,576.55
• REVENUE: $656,144.96
• ROAS: 9.04×
• PROFIT: $196,854.19

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
    "end": "2025-10-28"
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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.METRICS: 'metrics'>, 'metric': ['spend', 'revenue', 'roas', 'profit'], 'time_range': {'last_n_days': None, 'start': datetime.date(2025, 10, 1), 'end': datetime.date(2025, 10, 28)}, 'compare_to_previous': False, 'group_by': 'campaign', 'breakdown': 'campaign', 'top_n': 10, 'sort_order': 'desc', 'filters': {'provider': 'meta', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': None, 'comparison_entities': None, 'comparison_metrics': None, 'question': 'Give me spend, revenue, ROAS, and profit for all Meta campaigns this month to date', 'timeframe_description': 'this month'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1001ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 28), group_by='campaign', breakdown='campaign', derived=None, need_timeseries=True, need_previous=False, base_measures=['profit', 'revenue', 'spend'], filters={'provider': 'meta', 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=10, sort_order='desc', query=MetricQuery(query_type=<QueryType.METRICS: 'metrics'>, metric=['spend', 'revenue', 'roas', 'profit'], time_range=TimeRange(last_n_days=None, start=datetime.date(2025, 10, 1), end=datetime.date(2025, 10, 28)), compare_to_previous=False, group_by='campaign', breakdown='campaign', top_n=10, sort_order='desc', filters=Filters(provider='meta', level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type=None, comparison_entities=None, comparison_metrics=None, question='Give me spend, revenue, ROAS, and profit for all Meta campaigns this month to date', timeframe_description='this month'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 4 metrics: ['spend', 'revenue', 'roas', 'profit']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=meta, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('72576.5500'), 'revenue': Decimal('656144.9600'), 'clicks': 143052, 'impressions': 7253988, 'conversions': Decimal('13464.8300'), 'leads': Decimal('6839.4200'), 'installs': 0, 'purchases': 3509, 'visitors': 130033, 'profit': Decimal('196854.1900')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for spend
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for spend: 268552.71
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'spend': MetricValue(value=72576.55, previous=None, delta_pct=None), 'revenue': MetricValue(value=656144.96, previous=None, delta_pct=None), 'roas': MetricValue(value=Decimal('9.040729546940437372677538406'), previous=None, delta_pct=None), 'profit': MetricValue(value=196854.19, previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 268552.71
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting timeseries for 4 metrics
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting breakdown for spend by campaign
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 10, 1) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=meta, level=None, status=None, entity_name=None
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Top N: 10, Sort order: desc
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-10-01 to 2025-10-28
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'metrics': {'spend': {'summary': 72576.55, 'previous': None, 'delta_pct': None}, 'revenue': {'summary': 656144.96, 'previous': None, 'delta_pct': None}, 'roas': {'summary': Decimal('9.040729546940437372677538406'), 'previous': None, 'delta_pct': None}, 'profit': {'summary': 196854.19, 'previous': None, 'delta_pct': None}}, 'timeseries': [{'date': '2025-10-01', 'value': 2530.12}, {'date': '2025-10-02', 'value': 2393.98}, {'date': '2025-10-03', 'value': 2390.46}, {'date': '2025-10-04', 'value': 2401.8}, {'date': '2025-10-05', 'value': 2758.83}, {'date': '2025-10-06', 'value': 2273.11}, {'date': '2025-10-07', 'value': 2884.56}, {'date': '2025-10-08', 'value': 2575.61}, {'date': '2025-10-09', 'value': 2846.19}, {'date': '2025-10-10', 'value': 2664.13}, {'date': '2025-10-11', 'value': 2255.98}, {'date': '2025-10-12', 'value': 2776.25}, {'date': '2025-10-13', 'value': 3090.87}, {'date': '2025-10-14', 'value': 2495.08}, {'date': '2025-10-15', 'value': 2500.11}, {'date': '2025-10-16', 'value': 2617.36}, {'date': '2025-10-17', 'value': 2654.28}, {'date': '2025-10-18', 'value': 2480.58}, {'date': '2025-10-19', 'value': 3337.02}, {'date': '2025-10-20', 'value': 2454.67}, {'date': '2025-10-21', 'value': 2589.77}, {'date': '2025-10-22', 'value': 2378.6}, {'date': '2025-10-23', 'value': 2722.94}, {'date': '2025-10-24', 'value': 2394.18}, {'date': '2025-10-25', 'value': 2407.04}, {'date': '2025-10-26', 'value': 2531.83}, {'date': '2025-10-27', 'value': 3054.27}, {'date': '2025-10-28', 'value': 2116.93}], 'breakdown': [{'label': 'Blog Content Promotion', 'value': 1802.24, 'spend': Decimal('1802.2400'), 'clicks': 3146, 'conversions': Decimal('374.9700'), 'revenue': Decimal('20108.3900'), 'impressions': 161436}, {'label': 'Newsletter Signup Campaign', 'value': 1708.3, 'spend': Decimal('1708.3000'), 'clicks': 3323, 'conversions': Decimal('640.5600'), 'revenue': Decimal('3107.3600'), 'impressions': 171372}, {'label': 'Holiday Sale - Purchases', 'value': 1324.75, 'spend': Decimal('1324.7500'), 'clicks': 2782, 'conversions': Decimal('127.0000'), 'revenue': Decimal('16412.8400'), 'impressions': 142651}, {'label': 'Black Friday Deals', 'value': 1231.56, 'spend': Decimal('1231.5600'), 'clicks': 2362, 'conversions': Decimal('103.0000'), 'revenue': Decimal('14019.4500'), 'impressions': 121431}], 'query_type': 'multi_metrics'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'Here are your metrics from October 01 to 28:
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: Nonems
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 1236ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'Here are your metrics from October 01 to 28:
```

---

## Test 105: Compare clicks, CTR, and cost per click for Morning vs Evening Audience adsets last month

**Answer**:
> In the last 30 days, when comparing the Morning Audience and Evening Audience ad sets, the Evening Audience outperformed in several key areas. 

Firstly, the Evening Audience had more clicks, totaling 10,204, compared to the Morning Audience's 8,530 clicks. This indicates a higher level of engagement during the evening.

Looking at the click-through rate (CTR), the Evening Audience also had a slight edge with a CTR of 2.03%, while the Morning Audience had a CTR of 1.87%. This suggests that the ads were slightly more effective at capturing interest in the evening.

Lastly, the cost per click (CPC) was lower for the Evening Audience at $0.50, compared to $0.52 for the Morning Audience. This means the Evening Audience was not only more engaging but also more cost-effective.

Overall, the Evening Audience ad set performed better across all metrics: clicks, CTR, and CPC.

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
INFO:app.services.qa_service:[QA_PIPELINE] Translation complete: {'query_type': <QueryType.COMPARISON: 'comparison'>, 'metric': None, 'time_range': {'last_n_days': 30, 'start': None, 'end': None}, 'compare_to_previous': False, 'group_by': 'adset', 'breakdown': None, 'top_n': 5, 'sort_order': 'desc', 'filters': {'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, 'thresholds': None, 'comparison_type': 'entity_vs_entity', 'comparison_entities': ['Morning Audience', 'Evening Audience'], 'comparison_metrics': ['clicks', 'ctr', 'cpc'], 'question': 'Compare clicks, CTR, and cost per click for Morning vs Evening Audience adsets last month', 'timeframe_description': 'last month'}
INFO:app.services.qa_service:[QA_PIPELINE] Translation latency: 1257ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 3: Building execution plan
INFO:app.services.qa_service:[QA_PIPELINE] Plan built: Plan(start=datetime.date(2025, 9, 29), end=datetime.date(2025, 10, 28), group_by='adset', breakdown=None, derived=None, need_timeseries=True, need_previous=False, base_measures=['clicks', 'impressions', 'spend'], filters={'provider': None, 'level': None, 'entity_ids': None, 'status': None, 'entity_name': None, 'metric_filters': None}, top_n=5, sort_order='desc', query=MetricQuery(query_type=<QueryType.COMPARISON: 'comparison'>, metric=None, time_range=TimeRange(last_n_days=30, start=None, end=None), compare_to_previous=False, group_by='adset', breakdown=None, top_n=5, sort_order='desc', filters=Filters(provider=None, level=None, entity_ids=None, status=None, entity_name=None, metric_filters=None), thresholds=None, comparison_type='entity_vs_entity', comparison_entities=['Morning Audience', 'Evening Audience'], comparison_metrics=['clicks', 'ctr', 'cpc'], question='Compare clicks, CTR, and cost per click for Morning vs Evening Audience adsets last month', timeframe_description='last month'))
INFO:app.services.qa_service:[QA_PIPELINE] Step 4: Executing plan
INFO:app.dsl.executor:[COMPARISON] Executing comparison plan for type: entity_vs_entity
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['clicks', 'ctr', 'cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 29) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Morning Audience
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-29 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Morning Audience'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Morning Audience - Holiday Sale - Purchases (ID: 2097b889-0ce5-4e1c-854d-b6099229bd5c, Level: LevelEnum.adset)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using adset hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 4 descendants for Morning Audience - Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity 2097b889-0ce5-4e1c-854d-b6099229bd5c from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 3 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Morning Audience': 3 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('4446.2900'), 'revenue': Decimal('49034.6600'), 'clicks': 8530, 'impressions': 457320, 'conversions': Decimal('363.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 363, 'visitors': 7803, 'profit': Decimal('14678.1700')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for clicks
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for clicks: 636793.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'clicks': MetricValue(value=8530.0, previous=None, delta_pct=None), 'ctr': MetricValue(value=0.01865214729292399, previous=None, delta_pct=None), 'cpc': MetricValue(value=Decimal('0.5212532239155920281359906213'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 636793.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting summary for 3 metrics: ['clicks', 'ctr', 'cpc']
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Time range: last_n_days=None start=datetime.date(2025, 9, 29) end=datetime.date(2025, 10, 28)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Filters: provider=None, level=None, status=None, entity_name=Evening Audience
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolved dates: 2025-09-29 to 2025-10-28
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Resolving entity name: 'Evening Audience'
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found entity: Evening Audience - Holiday Sale - Purchases (ID: a7408419-eb16-4c3b-80ec-d7cf998782c5, Level: LevelEnum.adset)
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using adset hierarchy CTE
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Found 4 descendants for Evening Audience - Holiday Sale - Purchases
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Excluded parent entity a7408419-eb16-4c3b-80ec-d7cf998782c5 from descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Returning 3 descendant IDs for rollup
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Using hierarchy rollup for 'Evening Audience': 3 descendants
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Current period totals: {'spend': Decimal('5148.6000'), 'revenue': Decimal('61638.3000'), 'clicks': 10204, 'impressions': 503797, 'conversions': Decimal('453.0000'), 'leads': Decimal('0'), 'installs': 0, 'purchases': 453, 'visitors': 9338, 'profit': Decimal('18353.0100')}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Getting workspace average for clicks
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average for clicks: 636793.0
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Calculated metrics: {'clicks': MetricValue(value=10204.0, previous=None, delta_pct=None), 'ctr': MetricValue(value=0.020254189683543172, previous=None, delta_pct=None), 'cpc': MetricValue(value=Decimal('0.5045668365346922775382203058'), previous=None, delta_pct=None)}
INFO:app.services.unified_metric_service:[UNIFIED_METRICS] Workspace average: 636793.0
INFO:app.dsl.executor:[COMPARISON] Completed execution for 2 items
INFO:app.services.qa_service:[QA_PIPELINE] Execution complete: {'comparison': [{'entity': 'Morning Audience', 'clicks': 8530.0, 'ctr': 0.01865214729292399, 'cpc': Decimal('0.5212532239155920281359906213')}, {'entity': 'Evening Audience', 'clicks': 10204.0, 'ctr': 0.020254189683543172, 'cpc': Decimal('0.5045668365346922775382203058')}], 'comparison_type': 'entity_vs_entity', 'metrics': ['clicks', 'ctr', 'cpc'], 'query_type': 'comparison'}
INFO:app.services.qa_service:[QA_PIPELINE] Step 5: Building answer
INFO:app.services.qa_service:[QA_PIPELINE] Answer generated successfully
INFO:app.services.qa_service:[QA_PIPELINE] Answer: 'In the last 30 days, when comparing the Morning Audience and Evening Audience ad sets, the Evening Audience outperformed in several key areas. 
INFO:app.services.qa_service:[QA_PIPELINE] Answer generation latency: 4275ms
INFO:app.services.qa_service:[QA_PIPELINE] Step 6: Saving to conversation context
INFO:app.services.qa_service:[QA_PIPELINE] Step 7: Logging telemetry
INFO:app.services.qa_service:[QA_PIPELINE] ===== Pipeline complete =====
INFO:app.services.qa_service:[QA_PIPELINE] Total latency: 5855ms
INFO:app.services.qa_service:[QA_PIPELINE] Final answer: 'In the last 30 days, when comparing the Morning Audience and Evening Audience ad sets, the Evening Audience outperformed in several key areas. 
```

---

