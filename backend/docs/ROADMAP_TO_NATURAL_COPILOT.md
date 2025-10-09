# Roadmap: Natural AI Copilot - Based on Real Testing

**Last Updated**: 2025-10-08 (Post Fresh Data & Analysis)  
**Status**: Phases 1-4.5 COMPLETE ✅ | New Issues Identified | Revised Plan for Weeks 3-4

---

## 🎉 Executive Summary

**MAJOR MILESTONE ACHIEVED**: After Phases 1-4.5 and running 40+ test questions with fresh expanded data (12 campaigns, 105 ads, multi-platform), the system is performing **well** but new quality issues surfaced.

### Current Success Rate: ~82% (33/40 tests working correctly)

**What This Means**:
- ✅ Core Q&A functionality is **production-ready**
- ✅ All critical phases (1-3) are **complete and working**
- ✅ Natural language quality is **excellent**
- ✅ Missing data handling is **graceful and helpful**
- 🟡 6 edge cases need incremental improvements

---

## 🔥 NEW ISSUES IDENTIFIED (Post Fresh Data - Tests 1-40)

After re-seeding with richer data and re-running tests, **7 new quality issues** were identified:

### Issue 1: Entities Lists Not Actually Listed (Test 13)
**Priority**: HIGH | **Effort**: LOW | **Tests Affected**: 13

**Problem**: When asking "List all active campaigns", system returns summary instead of actual list.

**Current behavior**:
```
Answer: "You have 10 active campaigns, including the Holiday Sale - Purchases, 
Summer Sale Campaign, and Black Friday Deals, among others."
```

**Expected behavior**:
```
Answer: "Here are your 10 active campaigns:
1. Holiday Sale - Purchases
2. Summer Sale Campaign
3. Black Friday Deals
4. App Install Campaign
5. Mobile Game Installs
6. Lead Gen - B2B
7. Newsletter Signup Campaign
8. Brand Awareness
9. Product Launch Teaser
10. Website Traffic Push"
```

**Root cause**: Answer builder for entities queries uses LLM which summarizes instead of listing.

**Fix needed**: Update `SIMPLE_ANSWER_PROMPT` to explicitly format entities as numbered list when `query_type: "entities"`.

---

### Issue 2: Wrong Answer Structure for "Which X" Queries (Test 14)
**Priority**: HIGH | **Effort**: LOW | **Tests Affected**: 14

**Problem**: Answers don't lead with the answer, start with workspace context instead.

**Current behavior**:
```
Question: "Which ad has the highest CTR?"
Answer: "Last week, your highest CTR was 2.4%, which is right on par with the 
workspace average. However, the top performer was the 'Video Ad - Evening 
Audience - Lead Gen - B2B' with an impressive 4.3%..."
```

**Expected behavior** (intent-first):
```
Answer: "The Video Ad - Evening Audience - Lead Gen - B2B had the highest CTR 
at 4.3% last week—that's your top performer! For context, your overall CTR 
was 2.4%, right at the workspace average."
```

**Root cause**: Answer builder extracts workspace summary first, then mentions top performer as "However..."

**Fix needed**: For breakdown queries with `top_n=1`, answer should:
1. Lead with the top performer (intent-first)
2. Add workspace context as secondary info

---

### Issue 3: Metric Value Filtering Not Supported (Test 15) ⚠️ DSL LIMITATION
**Priority**: HIGH | **Effort**: HIGH | **Tests Affected**: 15

**Problem**: Cannot filter by metric value (e.g., "campaigns with ROAS above 4").

**Current behavior**:
```
Question: "Show me campaigns with ROAS above 4"
DSL: { "query_type": "entities", ... }  // Just lists campaigns!
Answer: "You have 10 campaigns, including..."
```

**Expected behavior**:
```
DSL: { 
  "query_type": "metrics", 
  "metric": "roas",
  "breakdown": "campaign",
  "metric_filter": {"roas": {"min": 4.0}}  // NEW field needed!
}
Answer: "3 campaigns have ROAS above 4:
- Summer Sale Campaign: 13.29×
- Holiday Sale - Purchases: 8.42×
- Black Friday Deals: 5.67×"
```

**Root cause**: DSL has no support for metric value filters! 
- `thresholds` only supports min_spend, min_clicks, min_conversions (input measures)
- Cannot filter by computed metric values (ROAS, CPC, CTR, etc.)

**Fix needed** (Complex - 2 days):
1. Add `metric_filters` to DSL schema
2. Update executor to compute metric first, then filter
3. Add few-shot examples for "X above/below Y" patterns
4. Handle in answer builder

**Decision**: Phase 6 (Week 4+) - This is an architectural enhancement

---

### Issue 4: Vague Comparisons Default to Wrong Metric (Test 20)
**Priority**: MEDIUM | **Effort**: LOW | **Tests Affected**: 20

**Problem**: When user asks "How does this week compare to last week?" without specifying metric, LLM picks arbitrary metric (CPA).

**Current behavior**:
```
Question: "How does this week compare to last week?"
DSL: { "metric": "cpa", ... }  // Why CPA?!
Answer: "This week, your CPA is $5.47, which is a slight improvement..."
```

**Expected behavior**:
```
DSL: { "metric": "revenue", ... }  // Default to revenue or profit!
Answer: "This week, you generated $278K in revenue, up 5% from last week..."
```

**Root cause**: No guidance in prompts on which metric to use for vague comparisons.

**Fix needed**: Add rule to system prompt:
```
VAGUE COMPARISON QUESTIONS:
If user asks "how does X compare" or "compare this week vs last week" without 
specifying a metric, DEFAULT to:
1. revenue (most important business metric)
2. profit (if profit is commonly used in workspace)
3. spend (for budget-focused questions)

DO NOT default to cost metrics (CPA, CPC) unless explicitly mentioned.
```

---

### Issue 5: Metric Value Thresholds Only Support Base Measures ⚠️ LIMITATION
**Priority**: LOW | **Effort**: LOW | **Tests Affected**: None yet, but will occur

**Problem**: `thresholds` only supports base measures (spend, clicks, conversions), not derived metrics (ROAS, CPC, CTR).

**Current support**:
```json
{
  "thresholds": {
    "min_spend": 50.0,        // ✅ Works
    "min_clicks": 100,         // ✅ Works
    "min_conversions": 5       // ✅ Works
  }
}
```

**Not supported** (but users will ask for):
```json
{
  "thresholds": {
    "min_roas": 2.0,  // ❌ Doesn't exist
    "max_cpc": 0.50,  // ❌ Doesn't exist
    "min_ctr": 0.02   // ❌ Doesn't exist
  }
}
```

**Fix needed**: Same as Issue 3 - requires `metric_filters` support (Phase 6)

---

### Issue 6: Named Entity Filtering Not Supported (Test 18)
**Priority**: HIGH | **Effort**: MEDIUM | **Tests Affected**: 18

**Problem**: Cannot filter by campaign/adset/ad name.

**Current behavior**:
```
Question: "give me a breakdown of holiday campaign performance"
Result: ERROR or lists all campaigns
```

**Expected behavior**:
```
Answer: "The Holiday Sale - Purchases campaign generated $X revenue last week 
with a ROAS of Y..."
```

**Root cause**: DSL only supports `entity_ids` (UUIDs), not `entity_name`.

**Fix needed**: See `NAMED_ENTITY_FILTERING_PLAN.md` for full implementation plan (Week 3-4)

---

### Issue 7: Time-of-Day Analysis Not Supported (Test 39) ⚠️ DATA LIMITATION
**Priority**: LOW | **Effort**: HIGH | **Tests Affected**: 39

**Problem**: Questions about hourly patterns can't be answered (data granularity limitation).

**Example**:
```
Question: "What time on average do I get the best CPC?"
Current: Returns daily average CPC (ignores time-of-day aspect)
Expected: "Your best CPC is typically between 2-4pm" OR "We don't have hourly data"
```

**Root cause**: MetricFact stores data at daily granularity only (no hour dimension).

**Fix needed**: Requires data collection changes (Phase 7+)

---

## 🏆 What's Working Exceptionally Well (Tests 1-40)

### 1. ✅ Timeframe Detection & Tense (Phase 2 - COMPLETE)
**Status**: Working perfectly across all 46 tests

**Examples from tests**:
- Test 3: "What's my ROAS this week?" → "Your ROAS is **4.36× this week**" ✅
- Test 6: "How many clicks did I get last week?" → "You had **6,156 clicks last week**" ✅
- Test 37: "what is my total CVR last month?" → "Your total CVR was **8.5% last month**" ✅

**Achievement**: 
- "This week" correctly shows current week, not "last 7 days"
- "Last week" shows past week
- "Yesterday" shows yesterday
- Past tense for past periods ("was"), present tense for current ("is")

---

### 2. ✅ Graceful Missing Data Handling (Phase 3 - COMPLETE)
**Status**: Excellent explanatory answers when data doesn't exist

**Examples from tests**:
- Test 2: "How much did I spend yesterday?" → "**No data available for yesterday yet.** Your ad spend last week was available - try asking about a longer timeframe." ✅
- Test 11: "What's my ROAS for Google campaigns only?" → "**You don't have any Google campaigns connected.** You're currently only running ads on Other." ✅
- Test 40: "How much revenue on Google last week?" → "**You don't have any Google campaigns connected.** You're currently only running ads on Other." ✅

**Achievement**:
- Platform validation working (detects when Google/Meta/TikTok missing)
- Helpful suggestions instead of "$0.00" or "N/A"
- Lists available alternatives

---

### 3. ✅ Intent-Based Answer Depth (Phase 1 - COMPLETE)
**Status**: Answers appropriately match question complexity

**Examples from tests**:
- Test 3 (Simple): "What's my ROAS this week?" → "Your ROAS is 4.36× this week." (1 sentence) ✅
- Test 10 (Comparative): "Which campaign had the highest ROAS last week?" → "Last week, your top campaign was the 'Holiday Sale - Purchases' with an impressive ROAS of 11.58×, which is way above the workspace average of 4.36×. That's a fantastic performance!" (2-3 sentences) ✅
- Test 27 (Analytical): "Is my ROAS improving or declining?" → "Your ROAS was 3.88× last month, which is a solid improvement of 46.8% from 2.64× the month before—great job! Plus, you're right at the workspace average, so you're performing really well compared to others." (3 sentences with trend analysis) ✅

**Achievement**:
- Simple questions get concise answers
- Comparative questions include workspace context
- Analytical questions provide insights

---

### 4. ✅ Natural Conversational Language
**Status**: Answers sound human, not robotic

**Examples from tests**:
- Test 7: "Your profit was $3,536.59 last week" (not "Your PROFIT for the selected period is...")
- Test 20: "Your total revenue this month is $77,580.62" (natural)
- Test 25: "This week, you had 522 conversions, which is down 43% from 915 last week—definitely a dip." (conversational tone)

**Achievement**: All answers use natural language with appropriate tone

---

### 5. ✅ Breakdowns & Entity Queries
**Status**: Working perfectly for all hierarchy levels

**Examples from tests**:
- Test 10: "Which campaign had the highest ROAS last week?" → Correctly identifies Holiday Sale campaign ✅
- Test 13: "List all active campaigns" → "You currently have three active campaigns: Holiday Sale - Purchases, App Install Campaign, and Lead Gen - B2B." ✅
- Test 31: "Which adset had the highest cpc last week?" → Correctly identifies AdSet 2 ✅
- Test 33: "Which adset had the highest ctr last week?" → Correctly identifies AdSet 1 ✅

**Achievement**: Campaign, adset, and ad-level breakdowns all working

---

### 6. ✅ Metric Variety & Derived Metrics
**Status**: All 24 metrics working correctly

**Examples from tests**:
- Test 1: CPC ✅
- Test 5: CVR ✅
- Test 9: CPL ✅
- Test 19: AOV ✅
- Test 41: CPI ✅

**Achievement**: Base measures and derived metrics all computed correctly

---

## 🔍 Issues Found in 46-Test Run (6 issues, 13% of tests)

### Issue 1: "Lowest/Worst" Queries Confusing (4 tests affected)
**Priority**: MEDIUM | **Effort**: Low | **Tests**: 32, 34, 36, 43

**Problem**: When user asks "Which adset had the LOWEST cpc/ctr?", the answer talks about workspace average and "top performer" context, which is confusing for "worst performer" questions.

**Examples**:
- Test 32: "Which adset had the **lowest** ctr last week?" 
  - Answer: "...your top performer, AdSet 1 for the Holiday Sale, had a CTR of 1.9%"
  - **Confusing**: User asked for worst, not best

- Test 34: "Which adset had the **lowest** cpc last week?"
  - Answer: "Your lowest CPC last week was $0.47...For context, the **top performer** was AdSet 2 at $0.54..."
  - **Confusing**: For CPC, lower is better, so $0.47 IS the top performer, not $0.54

**Root Cause**: 
1. DSL correctly interprets "lowest" as getting minimum value
2. But answer builder always uses "top performer" language (designed for "highest" queries)
3. For inverse metrics (CPC, CPA, CPL, CPI, CPM), "lowest" = best, "highest" = worst

**Fix Needed**: 
- Detect if metric is inverse (lower is better) or normal (higher is better)
- Adjust language: "best performer" vs "worst performer" based on metric type and query intent

---

### Issue 2: "Breakdown of X Performance" Returns Entity List (1 test affected)
**Priority**: MEDIUM | **Effort**: Medium | **Tests**: 18

**Problem**: When user asks "give me a breakdown of holiday campaign performance", system just lists campaigns without showing performance metrics.

**Example**:
- Test 18: "give me a breakdown of holiday campaign performance"
  - Answer: "You have four campaigns running: Holiday Sale - Purchases, App Install Campaign, Lead Gen - B2B, and Brand Awareness."
  - **Expected**: Revenue, ROAS, spend breakdown for the Holiday campaign

**Root Cause**: 
- DSL translates to entities query (just list campaigns)
- Doesn't recognize "breakdown of performance" as metrics query with breakdown

**Fix Needed**: 
- Update prompts to recognize "breakdown of X performance" → metrics query with default metric (revenue/ROAS) and breakdown by entity
- Add few-shot example for this pattern

---

### Issue 3: What-If Scenarios Not Supported (1 test affected)
**Priority**: LOW (Future Feature) | **Effort**: High | **Tests**: 45

**Problem**: Hypothetical "what if" questions return actual data instead of simulation.

**Example**:
- Test 45: "how much revenue would i have last week if my cpc was 0.20?"
  - Answer: "Your revenue was $12,691.04 last week." (actual, not simulated)
  - **Expected**: Simulation based on different CPC

**Root Cause**: System doesn't support what-if analysis (requires simulation layer)

**Decision**: Out of scope for now. Phase 5 or later.

---

### Issue 4: Time-of-Day Analysis Not Supported (1 test affected)
**Priority**: LOW (Future Feature) | **Effort**: High | **Tests**: 44

**Problem**: Questions about hourly/time-of-day patterns can't be answered with current data granularity.

**Example**:
- Test 44: "What time on average do i get the best cpc?"
  - Answer: "Last week, your CPC was $0.47..." (ignores time-of-day aspect)
  - **Expected**: "Your best CPC is typically between 2-4pm" or "We don't have hourly data yet"

**Root Cause**: 
- MetricFact stores data at daily granularity only
- No hour-of-day dimension

**Decision**: Out of scope for now. Requires hourly data collection.

---

### Issue 5: Empty Question Handling (1 test affected)
**Priority**: LOW (Edge Case) | **Effort**: Low | **Tests**: 46

**Problem**: Empty question string returns a default answer instead of error.

**Example**:
- Test 46: "" (empty string)
  - Answer: "Your revenue was $12,691.04 last week."
  - **Expected**: "Please ask a question" or validation error

**Root Cause**: LLM falls back to default when no question provided

**Decision**: Add validation to reject empty questions before sending to LLM.

---

## 📊 Test Results Breakdown (46 Tests)

### Overall Success Rate: 87% (40/46)

| Category | Tests | Passed | Issues | Success Rate |
|----------|-------|--------|--------|--------------|
| **Basic Metrics** | 10 | 8 | 2 (no data today/yesterday) | 80% |
| **Comparisons** | 4 | 4 | 0 | 100% ✅ |
| **Breakdowns** | 12 | 11 | 1 (lowest/worst language) | 92% |
| **Entity Queries** | 3 | 3 | 0 | 100% ✅ |
| **Analytical** | 2 | 2 | 0 | 100% ✅ |
| **Platform Filters** | 3 | 3 | 0 (graceful missing data) | 100% ✅ |
| **Derived Metrics** | 8 | 8 | 0 | 100% ✅ |
| **Edge Cases** | 4 | 1 | 3 (what-if, time-of-day, empty) | 25% |

### Success by Phase Implementation

| Phase | Features | Status | Tests Affected | Success |
|-------|----------|--------|----------------|---------|
| Phase 1 | Intent classification, natural language | ✅ COMPLETE | All 46 | 100% |
| Phase 2 | Timeframe detection, correct tense | ✅ COMPLETE | All 46 | 100% |
| Phase 3 | Missing data explanations | ✅ COMPLETE | 11, 39, 40 | 100% |
| **NEW** | Lowest/worst language | 🔴 NEEDS FIX | 32, 34, 36, 43 | 0% |
| **NEW** | Performance breakdown intent | 🔴 NEEDS FIX | 18 | 0% |
| **Future** | What-if scenarios | ⚪ NOT STARTED | 45 | N/A |
| **Future** | Time-of-day analysis | ⚪ NOT STARTED | 44 | N/A |

---

## 🎯 Revised Roadmap - Next 3 Phases (Weeks 3-5)

Based on fresh data analysis and user feedback, here's the prioritized fix plan:

### Phase 5: Answer Quality Improvements (Week 3 - Day 1-2, 6 hours)
**Goal**: Fix answer structure and formatting issues (Tests 13, 14, 20)

**What to Fix**:
1. **Entities lists** (Test 13): Return formatted numbered lists, not summaries
2. **Intent-first answers** (Test 14): Lead with the answer for "which X" queries
3. **Vague comparison defaults** (Test 20): Default to revenue/profit, not CPA

---

#### Fix 1.1: Entities List Formatting (2 hours)
**Files**: `backend/app/answer/answer_builder.py`, `backend/app/nlp/prompts.py`

**Problem**: "List all active campaigns" returns "You have 10 campaigns, including..."  
**Expected**: Numbered list of all campaigns

**Implementation**:
```python
# In _extract_entities_facts()
if dsl.query_type == QueryType.ENTITIES:
    entity_list = result.get("entities", [])
    facts = {
        "query_type": "entities",
        "entity_count": len(entity_list),
        "entity_names": [e["name"] for e in entity_list],
        "level": dsl.filters.level if dsl.filters else "entities"
    }
```

**Update SIMPLE_ANSWER_PROMPT**:
```
For entities queries (query_type="entities"):
- Format as numbered list if asking to "list" or "show"
- Example: "Here are your 10 active campaigns:
  1. Holiday Sale
  2. Summer Sale
  ..."
```

---

#### Fix 1.2: Intent-First Answer Structure (2 hours)
**Files**: `backend/app/answer/context_extractor.py`, `backend/app/nlp/prompts.py`

**Problem**: "Which ad had highest CTR?" starts with workspace summary  
**Expected**: Lead with the answer

**Implementation**:
1. Detect "which X" queries: `breakdown != null and top_n == 1`
2. Mark as `intent_first_query = True` in facts
3. Update all three prompts with:
```
For "which X had highest/lowest Y" queries (top_n=1):
STRUCTURE:
1. Lead with the answer: "X had the highest/lowest Y at VALUE"
2. Add performance judgment: "—your top/worst performer"
3. Add context last: "For reference, your overall Y was Z"

GOOD: "Summer Sale had the highest ROAS at 13.29× last week—crushing it! 
       For context, your overall ROAS was 6.14×"

BAD: "Your ROAS was 6.14× last week. However, Summer Sale was your top 
      performer at 13.29×"  // Don't use "However" structure!
```

---

#### Fix 1.3: Default Metric for Vague Comparisons (1 hour)
**Files**: `backend/app/nlp/prompts.py` (system prompt)

**Problem**: "How does this week compare to last week?" defaults to CPA  
**Expected**: Default to revenue

**Implementation**: Add to system prompt:
```
VAGUE COMPARISON QUESTIONS (CRITICAL):
If user asks "how does X compare" or "compare this week vs last week" WITHOUT 
specifying a metric, use this priority order:

1. revenue (DEFAULT - most important business metric)
2. profit (if user commonly asks about profit)
3. spend (only if user explicitly mentions budget)

NEVER default to cost efficiency metrics (CPA, CPC, CPM) unless explicitly mentioned.

Examples:
- "How does this week compare to last week?" → metric: "revenue"
- "Compare this month vs last month" → metric: "revenue"
- "How are we doing vs last period?" → metric: "revenue"
```

**Tests Fixed**: 13, 14, 20

---

### Phase 6: Named Entity Filtering (Week 3-4, 9 hours)
**Goal**: Enable filtering by campaign/adset/ad name (Test 18)

**Full Plan**: See `NAMED_ENTITY_FILTERING_PLAN.md`

**Summary**:
- Add `entity_name` filter to DSL schema
- Update executor with `.ilike()` name matching
- Add 4 few-shot examples for name-based queries
- Update canonicalization to preserve entity names

**Tests Fixed**: 18

---

### Phase 7: Metric Value Filtering (Week 5+, 16 hours) ⚠️ COMPLEX
**Goal**: Support "campaigns with ROAS above 4" queries (Test 15)

**Why Complex**: Requires architectural changes to DSL

**Current Limitation**:
- `thresholds` only filters by input measures (spend, clicks, conversions)
- Cannot filter by computed metrics (ROAS, CPC, CTR)

**Solution Approach**:
1. Add `metric_filters` field to DSL:
   ```json
   {
     "metric": "roas",
     "breakdown": "campaign",
     "metric_filters": {
       "min": 4.0,    // Only campaigns with ROAS >= 4.0
       "max": null
     }
   }
   ```

2. Update executor to:
   - Compute metric for all entities
   - Filter results where metric meets criteria
   - Return only matching entities

3. Add few-shot examples:
   ```json
   {
     "question": "Show me campaigns with ROAS above 4",
     "dsl": {
       "metric": "roas",
       "breakdown": "campaign",
       "metric_filters": {"min": 4.0}
     }
   }
   ```

**Tests Fixed**: 15

**Decision**: Phase 7 (Week 5+) due to complexity

---

### OLD Phase 4: Better Language for Inverse Metrics (1-2 days)
**Status**: ✅ COMPLETE (Phase 4.5)  
**Goal**: Fix confusing language when asking for "lowest" on metrics where lower is better

**The Fix**:

**Step 1: Classify Metrics by Direction** (30 min)
```python
# In app/metrics/registry.py
INVERSE_METRICS = {'cpc', 'cpa', 'cpl', 'cpi', 'cpp', 'cpm'}  # Lower is better
NORMAL_METRICS = {'roas', 'poas', 'ctr', 'cvr', 'revenue', 'profit', ...}  # Higher is better
```

**Step 2: Detect Query Intent** (1 hour)
- When breakdown query has top_n=1:
  - Check if metric is inverse
  - Check if question contains "lowest", "worst", "minimum"
  - Determine: "looking for best" vs "looking for worst"

**Step 3: Pass Intent to Answer Builder** (1 hour)
- Add `query_intent` field to context: "best_performer" or "worst_performer"
- Update all three prompts with guidance:
  ```
  If query_intent = "best_performer" and metric is inverse:
    "X had the lowest CPC at $0.47—that's your best performer"
  If query_intent = "worst_performer" and metric is inverse:
    "X had the highest CPC at $0.54—that's your worst performer, you might want to review it"
  ```

**Step 4: Test** (30 min)
- Test 32: "lowest ctr" → Should say "worst performer" (CTR is normal metric)
- Test 34: "lowest cpc" → Should say "best performer" (CPC is inverse metric)
- Test 43: "lowest cpc" → Should say "best performer"

**Success Criteria**:
- ✅ "Which ad had the lowest CPC?" → "X had the lowest CPC at $0.47—that's your best performer!"
- ✅ "Which ad had the highest CPC?" → "X had the highest CPC at $0.70—that's your worst performer, might be worth reviewing"
- ✅ "Which ad had the lowest CTR?" → "X had the lowest CTR at 1.2%—that's your worst performer"

**Effort**: 3 hours  
**Impact**: HIGH (fixes 4 tests, 9% improvement)  
**Complexity**: LOW (just better language)

---

### Phase 5: "Performance Breakdown" Intent Detection (1 day)
**Goal**: Recognize "breakdown of X performance" as metrics query, not just entity list

**The Problem**:
- User: "Give me a breakdown of holiday campaign performance"
- System: Lists campaigns (entities query)
- Expected: Show revenue/ROAS/spend breakdown for holiday campaign

**The Fix**:

**Step 1: Add Few-Shot Examples** (1 hour)
Add to `app/nlp/prompts.py`:
```json
{
  "question": "Give me a breakdown of holiday campaign performance",
  "dsl": {
    "query_type": "metrics",
    "metric": "revenue",
    "breakdown": "campaign",
    "filters": {"level": "campaign"},
    "top_n": 5
  }
}
```

**Step 2: Update Canonicalization** (1 hour)
- "breakdown of performance" → "show me performance by"
- "how is X performing" → "show me revenue for X"

**Step 3: Test** (30 min)
- "Give me a breakdown of holiday campaign performance" → Should show metrics
- "How are my campaigns performing?" → Should show campaign breakdown with metrics

**Success Criteria**:
- ✅ "Breakdown of campaign performance" → Shows revenue/ROAS/spend by campaign
- ✅ "How is X performing?" → Shows metrics for entity X

**Effort**: 2.5 hours  
**Impact**: MEDIUM (fixes 1 test, improves UX)  
**Complexity**: LOW (just prompt engineering)

---

## ✅ What We're NOT Fixing Yet (Future Phases)

### Out of Scope for Now

1. **What-If Scenarios** (Test 45)
   - "What if my CPC was $0.20?" requires simulation layer
   - **Decision**: Phase 6 or later (requires new architecture)
   - **Effort**: HIGH (3-5 days)

2. **Time-of-Day Analysis** (Test 44)
   - "What time do I get the best CPC?" requires hourly data
   - **Decision**: When we have hourly granularity data
   - **Effort**: HIGH (requires data collection changes)

3. **Empty Question Validation** (Test 46)
   - Edge case, low priority
   - **Decision**: Quick fix in Phase 4 (add input validation)
   - **Effort**: LOW (15 min)

4. **Entity Name Filtering**
   - "How is Holiday Sale campaign performing?" requires entity name search
   - **Decision**: Phase 6 (after performance breakdown)
   - **Effort**: MEDIUM (2 days)

5. **Multi-Metric Queries**
   - "Show me ROAS and CPC by campaign" requires multiple metrics in one query
   - **Decision**: Phase 7 (nice-to-have)
   - **Effort**: MEDIUM (2-3 days)

---

## 📈 Incremental Implementation Plan

### Week 1: Phase 4 - Inverse Metrics Language Fix

**Day 1 (2-3 hours)**:
- [x] Morning: Add metric classification to registry (INVERSE vs NORMAL)
- [x] Morning: Add query intent detection (best vs worst performer)
- [x] Afternoon: Update answer builder to use correct language
- [x] Afternoon: Update all three prompts with inverse metric guidance

**Day 2 (1 hour)**:
- [x] Test all "lowest" queries (tests 32, 34, 36, 43)
- [x] Verify language is now clear and correct
- [x] Run full 46-test suite to ensure no regressions

**Expected Result**: Success rate 87% → 96% (9% improvement)

---

### Week 2: Phase 5 - Performance Breakdown Intent

**Day 1 (2 hours)**:
- [ ] Add 3-4 few-shot examples for "breakdown of performance" pattern
- [ ] Update canonicalization for performance-related phrases

**Day 2 (1 hour)**:
- [ ] Test "breakdown of X performance" queries
- [ ] Test "how is X performing" queries
- [ ] Run full test suite

**Expected Result**: Success rate 96% → 98% (2% improvement)

---

### Week 3: Polish & Edge Cases

**Day 1 (30 min)**:
- [ ] Add empty question validation (reject before LLM call)
- [ ] Add "question too vague" handling

**Day 2 (1 hour)**:
- [ ] Final full test run (46 questions)
- [ ] Document all improvements in QA_SYSTEM_ARCHITECTURE.md
- [ ] Update ADNAVI_BUILD_LOG.md

**Expected Result**: Success rate 98%+ (production-ready)

---

## 🎯 Success Metrics

### Current State (After Phases 1-3)
- ✅ Intent classification: 100% working
- ✅ Natural language: 100% working
- ✅ Timeframe accuracy: 100% working
- ✅ Missing data handling: 100% working
- ✅ Breakdowns: 100% working
- ✅ Analytical depth: 100% working
- ⚠️ Inverse metric language: Confusing (4 tests)
- ⚠️ Performance breakdown intent: Not detected (1 test)

### Target State (After Phases 4-5)
- ✅ Intent classification: 100% working
- ✅ Natural language: 100% working
- ✅ Timeframe accuracy: 100% working
- ✅ Missing data handling: 100% working
- ✅ Breakdowns: 100% working
- ✅ Analytical depth: 100% working
- ✅ Inverse metric language: Clear (fixed)
- ✅ Performance breakdown intent: Detected (fixed)

### Long-term Vision (Phase 6+)
- What-if scenarios supported
- Time-of-day analysis (when we have hourly data)
- Entity name filtering and search
- Multi-metric queries
- Educational answers ("What is ROAS?")

---

## 🏁 Priority Matrix (Updated - Post Fresh Data Analysis)

| Phase | Priority | Effort | Impact | Tests Fixed | Status |
|-------|----------|--------|--------|-------------|--------|
| Phase 1 (Intent & Natural Language) | P0 | Medium | High | All | ✅ DONE |
| Phase 2 (Timeframe Detection) | P0 | Medium | Critical | All | ✅ DONE |
| Phase 3 (Missing Data Handling) | P0 | Medium | Critical | 11, 35 | ✅ DONE |
| Phase 4 (Inverse Metrics Language) | P1 | Low | Medium | 26, 29, 30, 38 | ✅ DONE |
| Phase 4.5 (Sort Order Support) | P1 | Low | High | 26, 29, 30, 38 | ✅ DONE |
| **Phase 5 (Answer Quality)** | P1 | Low | High | 13, 14, 20 | 🔴 NEXT (Week 3) |
| **Phase 6 (Named Entity Filtering)** | P1 | Medium | High | 18 | 🟡 Week 3-4 |
| Phase 7 (Metric Value Filtering) | P2 | High | Medium | 15 | ⚪ Week 5+ |
| Phase 8 (What-If Scenarios) | P3 | High | Low | 40 | ⚪ Future |
| Phase 9 (Time-of-Day Analysis) | P3 | High | Low | 39 | ⚪ Needs Data |

---

## 🎓 Philosophy (Unchanged)

**Incremental Progress Over Perfection**
- ✅ Fix one thing at a time
- ✅ Test after each change
- ✅ Build on what works
- ✅ Don't break existing functionality

**User-Centric Fixes**
- ✅ Fix issues users will actually notice
- ✅ Prioritize confusing answers over edge cases
- ✅ Make errors helpful, not mysterious

**Data-Driven Decisions**
- ✅ Test with real questions (46 comprehensive tests)
- ✅ Measure success rates (currently 87%)
- ✅ Track improvements over time
- ✅ Let results guide priorities

---

## 🚀 Next Actions (Week 3)

### Immediate Priority: Phase 5 - Answer Quality (6 hours)

**Day 1 Morning (2 hours)**: Fix entities list formatting
1. Update `_extract_entities_facts()` in `answer_builder.py`
2. Add numbered list formatting to `SIMPLE_ANSWER_PROMPT`
3. Test: "List all active campaigns" should return numbered list

**Day 1 Afternoon (2 hours)**: Fix intent-first answer structure
1. Add detection for `top_n=1` queries in `context_extractor.py`
2. Update all three prompts with "lead with answer" guidance
3. Test: "Which ad had highest CTR?" should lead with the ad name

**Day 2 Morning (1 hour)**: Fix vague comparison defaults
1. Add "VAGUE COMPARISON QUESTIONS" rule to system prompt
2. Test: "How does this week compare to last week?" should use revenue

**Day 2 Afternoon (1 hour)**: Validation & Testing
1. Run full 40-test suite
2. Verify Tests 13, 14, 20 now pass
3. Check for regressions

---

### Week 3-4: Phase 6 - Named Entity Filtering (9 hours)

See `NAMED_ENTITY_FILTERING_PLAN.md` for detailed implementation plan.

**Summary**:
- Day 1: DSL schema + executor changes (4 hours)
- Day 2: NLP translation + canonicalization (3 hours)
- Day 3: Testing & validation (2 hours)

---

## 📝 Test Coverage Summary

The 40-question test suite covers:
- ✅ All 24 metrics (base + derived)
- ✅ All hierarchy levels (campaign, adset, ad)
- ✅ All query types (metrics, entities, providers)
- ✅ Timeframe variations (today, yesterday, this week, last week, last month)
- ✅ Platform filters (Google, Meta, TikTok, Other)
- ✅ Status filters (active campaigns)
- ✅ Comparisons and analytical questions
- ✅ Sort order (lowest/highest)
- ✅ Edge cases (empty questions, what-if scenarios)

**Fresh data** (Oct 8, 2025):
- 12 campaigns across 4 providers
- 35 adsets, 105 ads
- 3,150 metric facts (30 days)
- Rich, multi-platform test environment

---

## 📊 Current State Summary

### What's Complete ✅
- ✅ **Phases 1-4.5 DONE**: Intent classification, timeframe detection, missing data handling, sort order, inverse metrics language
- ✅ **Core functionality**: All basic queries working (82% success rate)
- ✅ **Natural language**: Conversational, context-aware answers
- ✅ **Multi-platform**: Google, Meta, TikTok, Other all supported

### What Needs Work 🔧
- 🔴 **Answer quality** (Tests 13, 14, 20): Formatting and structure issues
- 🟡 **Named entity filtering** (Test 18): Cannot query by campaign name
- 🟡 **Metric value filtering** (Test 15): Cannot filter "ROAS above 4"
- ⚪ **Time-of-day** (Test 39): Data granularity limitation
- ⚪ **What-if scenarios** (Test 40): Out of scope

### Success Rate Projection
- **Current**: 82% (33/40 tests)
- **After Phase 5**: 87% (35/40 tests) - +3 tests fixed
- **After Phase 6**: 90% (36/40 tests) - +1 test fixed
- **After Phase 7**: 93% (37/40 tests) - +1 test fixed
- **Remaining**: 3 tests are limitations (time-of-day, what-if, data constraints)

---

**Status**: System is **82% production-ready** with clear path to **90%+** in Weeks 3-4 through incremental improvements.

---

## 📚 Reference Documents

- **Named Entity Filtering Plan**: `/backend/docs/NAMED_ENTITY_FILTERING_PLAN.md` (NEW)
- **QA System Architecture**: `/backend/docs/QA_SYSTEM_ARCHITECTURE.md`
- **Phase 4.5 Implementation**: `/backend/PHASE_4_5_SORT_ORDER_IMPLEMENTATION.md`
- **Phase 4.5 Final Fixes**: `/backend/PHASE_4_5_FINAL_FIXES.md`
- **Build Log**: `/docs/ADNAVI_BUILD_LOG.md`

