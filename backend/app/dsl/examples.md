# DSL Examples for Few-Shot Learning

This document provides example question → DSL JSON pairs for training the LLM translator.

These examples are embedded in the system prompt to guide structured output generation.

---

## Example 1: Simple Metric Query

**Question:** "What's my ROAS this week?"

**DSL:**
```json
{
  "metric": "roas",
  "time_range": {"last_n_days": 7},
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "filters": {}
}
```

**Why:** Simple aggregate query for a derived metric over the past 7 days.

---

## Example 2: Comparison Query

**Question:** "How did conversions change vs last month?"

**DSL:**
```json
{
  "metric": "conversions",
  "time_range": {"last_n_days": 30},
  "compare_to_previous": true,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "filters": {}
}
```

**Why:** Aggregate with previous period comparison (`compare_to_previous: true`).

---

## Example 3: Breakdown by Campaign

**Question:** "Which campaigns drove the most revenue last week?"

**DSL:**
```json
{
  "metric": "revenue",
  "time_range": {"last_n_days": 7},
  "compare_to_previous": false,
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 10,
  "filters": {}
}
```

**Why:** Breakdown analysis showing top 10 campaigns by revenue.

---

## Example 4: Specific Date Range

**Question:** "Show me spend from September 1st to September 30th"

**DSL:**
```json
{
  "metric": "spend",
  "time_range": {
    "start": "2025-09-01",
    "end": "2025-09-30"
  },
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "filters": {}
}
```

**Why:** Explicit date range using `start` and `end` instead of `last_n_days`.

---

## Example 5: Filtered by Provider

**Question:** "What's my Google Ads CPA for the past 14 days?"

**DSL:**
```json
{
  "metric": "cpa",
  "time_range": {"last_n_days": 14},
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "filters": {
    "provider": "google"
  }
}
```

**Why:** Provider filter applied (`filters.provider: "google"`).

---

## Example 6: Active Campaigns Only

**Question:** "Show me revenue from active campaigns this month"

**DSL:**
```json
{
  "metric": "revenue",
  "time_range": {"last_n_days": 30},
  "compare_to_previous": false,
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 5,
  "filters": {
    "status": "active"
  }
}
```

**Why:** Status filter (`filters.status: "active"`) with campaign breakdown.

---

## Example 7: CVR with Comparison

**Question:** "How's my conversion rate compared to yesterday?"

**DSL:**
```json
{
  "metric": "cvr",
  "time_range": {"last_n_days": 1},
  "compare_to_previous": true,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "filters": {}
}
```

**Why:** Derived metric (CVR) with 1-day window and previous period comparison.

---

## Example 8: Top Ad Sets by Clicks

**Question:** "Which ad sets got the most clicks in the last 7 days?"

**DSL:**
```json
{
  "metric": "clicks",
  "time_range": {"last_n_days": 7},
  "compare_to_previous": false,
  "group_by": "adset",
  "breakdown": "adset",
  "top_n": 10,
  "filters": {}
}
```

**Why:** Ad set level breakdown with `top_n: 10` for top performers.

---

## Example 9: Meta Impressions, Last Month

**Question:** "How many impressions did my Meta campaigns get last month?"

**DSL:**
```json
{
  "metric": "impressions",
  "time_range": {"last_n_days": 30},
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "filters": {
    "provider": "meta",
    "level": "campaign"
  }
}
```

**Why:** Multiple filters applied (provider + level).

---

## Example 10: Spend Breakdown by Ad Level

**Question:** "Show me top 5 ads by spend yesterday"

**DSL:**
```json
{
  "metric": "spend",
  "time_range": {"last_n_days": 1},
  "compare_to_previous": false,
  "group_by": "ad",
  "breakdown": "ad",
  "top_n": 5,
  "filters": {}
}
```

**Why:** Ad-level breakdown with `top_n: 5` for yesterday's data.

---

## Example 11: ROAS with Previous Period and Breakdown

**Question:** "Which campaigns had the best ROAS this quarter vs last quarter?"

**DSL:**
```json
{
  "metric": "roas",
  "time_range": {"last_n_days": 90},
  "compare_to_previous": true,
  "group_by": "campaign",
  "breakdown": "campaign",
  "top_n": 10,
  "filters": {}
}
```

**Why:** Combination of comparison + breakdown for driver analysis.

---

## Example 12: Simple Yesterday Query

**Question:** "What did I spend yesterday?"

**DSL:**
```json
{
  "metric": "spend",
  "time_range": {"last_n_days": 1},
  "compare_to_previous": false,
  "group_by": "none",
  "breakdown": null,
  "top_n": 5,
  "filters": {}
}
```

**Why:** Simple single-day aggregate.

---

## Notes for LLM

1. **Metric field:** Must be one of: spend, revenue, clicks, impressions, conversions, roas, cpa, cvr
2. **Time range:** Use `last_n_days` for relative, or `start`/`end` for absolute dates (YYYY-MM-DD)
3. **Compare to previous:** Set to `true` only when user explicitly asks for comparison or change
4. **Group by and breakdown:** Usually the same value; set to "none" if no breakdown requested
5. **Top N:** Default to 5; increase to 10-20 if user asks for "top X" or "best/worst"
6. **Filters:** Only include if explicitly mentioned (provider, level, status)
7. **Default time range:** If not specified, use `{"last_n_days": 7}`

---

## Anti-Patterns (What NOT to do)

❌ **Invalid metric:**
```json
{"metric": "roi", ...}  // Use "roas" instead
```

❌ **Invalid time range:**
```json
{"time_range": "last week"}  // Must be object: {"last_n_days": 7}
```

❌ **Missing required fields:**
```json
{"metric": "spend"}  // Must include time_range
```

❌ **Invalid breakdown without group_by:**
```json
{"breakdown": "campaign", "group_by": "none"}  // group_by must match breakdown
```
