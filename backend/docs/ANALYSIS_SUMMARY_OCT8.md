# QA System Analysis Summary - October 8, 2025

**Test Data**: Fresh seed with 12 campaigns, 105 ads, 3,150 metric facts  
**Test Results**: `qa_test_results-phase-5-4.md` (40 questions)  
**Success Rate**: 82% (33/40 tests working correctly)

---

## 🔍 Issues Identified & Root Causes

### Issue 1: Entities Lists Not Actually Listed (Test 13) ⚠️ HIGH PRIORITY
**Test**: "List all active campaigns"  
**Current**: "You have 10 active campaigns, including..."  
**Expected**: Numbered list of all 10 campaigns  
**Root Cause**: Answer builder uses LLM which summarizes instead of formatting as list  
**Fix**: Update prompts to explicitly format entities as numbered lists  
**Effort**: 2 hours  

---

### Issue 2: Wrong Answer Structure (Test 14) ⚠️ HIGH PRIORITY
**Test**: "Which ad has the highest CTR?"  
**Current**: "Your highest CTR was 2.4%... However, top performer was..."  
**Expected**: "Video Ad... had the highest CTR at 4.3%—your top performer!"  
**Root Cause**: Answers lead with workspace context, not the answer  
**Fix**: Intent-first structure for `top_n=1` queries  
**Effort**: 2 hours  

---

### Issue 3: Metric Value Filtering Not Supported (Test 15) ⚠️ DSL LIMITATION
**Test**: "Show me campaigns with ROAS above 4"  
**Current**: Returns entities query (just lists campaigns)  
**Expected**: Metrics query with breakdown filtered by ROAS > 4  
**Root Cause**: DSL has NO support for metric value filters!  
- `thresholds` only supports min_spend, min_clicks, min_conversions (input measures)
- Cannot filter by computed metrics (ROAS, CPC, CTR)  
**Fix**: Add `metric_filters` field to DSL (complex architectural change)  
**Effort**: 16 hours (Phase 7, Week 5+)  

---

### Issue 4: Vague Comparisons Default to Wrong Metric (Test 20) ⚠️ MEDIUM PRIORITY
**Test**: "How does this week compare to last week?"  
**Current**: Defaults to CPA  
**Expected**: Default to revenue or profit  
**Root Cause**: No guidance in prompts on default metric  
**Fix**: Add rule to system prompt: "Default to revenue for vague comparisons"  
**Effort**: 1 hour  

---

### Issue 5: Named Entity Filtering Not Supported (Test 18) ⚠️ HIGH PRIORITY
**Test**: "give me a breakdown of holiday campaign performance"  
**Current**: ERROR or lists all campaigns  
**Expected**: Metrics for "Holiday Sale - Purchases" campaign  
**Root Cause**: DSL only supports `entity_ids` (UUIDs), not `entity_name`  
**Fix**: Add `entity_name` filter + executor `.ilike()` matching  
**Effort**: 9 hours (Week 3-4)  
**Plan**: See `NAMED_ENTITY_FILTERING_PLAN.md`  

---

### Issue 6: Time-of-Day Analysis Not Supported (Test 39) ⚠️ DATA LIMITATION
**Test**: "What time on average do I get the best CPC?"  
**Current**: Returns daily CPC (ignores time-of-day)  
**Expected**: "Your best CPC is typically between 2-4pm" OR "We don't have hourly data"  
**Root Cause**: MetricFact stores daily data only (no hour dimension)  
**Fix**: Requires data collection changes + schema changes  
**Effort**: HIGH (out of scope)  

---

### Issue 7: What-If Scenarios Not Supported (Test 40) ⚠️ FEATURE GAP
**Test**: "how much revenue would I have last week if my cpc was 0.20?"  
**Current**: Returns actual revenue (ignores hypothetical)  
**Expected**: Simulation based on different CPC  
**Root Cause**: No simulation/what-if engine  
**Fix**: Requires separate scenario modeling system  
**Effort**: HIGH (Phase 8, future)  

---

## 📋 Updated Roadmap Summary

### ✅ Phases 1-4.5 Complete
- ✅ Intent classification (simple/comparative/analytical)
- ✅ Timeframe detection (today, yesterday, this week, last week)
- ✅ Missing data handling (graceful explanations)
- ✅ Inverse metrics language (lowest CPC = best performer)
- ✅ Sort order support (asc/desc for lowest/highest)

### 🔴 Phase 5: Answer Quality (Week 3, Day 1-2, 6 hours)
**Priority**: HIGH | **Tests Fixed**: 13, 14, 20

1. **Entities list formatting** (2h): Return numbered lists
2. **Intent-first answers** (2h): Lead with the answer for "which X" queries
3. **Vague comparison defaults** (1h): Default to revenue, not CPA

### 🟡 Phase 6: Named Entity Filtering (Week 3-4, 9 hours)
**Priority**: HIGH | **Tests Fixed**: 18

- Add `entity_name` filter to DSL
- Update executor with case-insensitive partial matching
- Add few-shot examples + canonicalization
- **Full plan**: `NAMED_ENTITY_FILTERING_PLAN.md`

### ⚪ Phase 7: Metric Value Filtering (Week 5+, 16 hours)
**Priority**: MEDIUM | **Tests Fixed**: 15

- Add `metric_filters` to DSL (architectural change)
- Compute metrics then filter by value
- Complex but enables "ROAS above 4" queries

### ⚪ Phase 8-9: Out of Scope
- Time-of-day analysis (requires hourly data)
- What-if scenarios (requires simulation engine)

---

## 📊 Success Rate Projections

| Phase | Tests Passing | Success Rate | Improvement |
|-------|---------------|--------------|-------------|
| **Current (4.5)** | 33/40 | 82% | Baseline |
| After Phase 5 | 36/40 | 90% | +8% |
| After Phase 6 | 37/40 | 93% | +3% |
| After Phase 7 | 38/40 | 95% | +2% |
| **Remaining** | 2/40 | 5% | Data/feature limitations |

---

## 🎯 Key Insights from Analysis

### What We Learned
1. **Answer quality** matters more than DSL accuracy
   - Test 14: DSL is correct, but answer structure is confusing
   - Test 13: Query works, but answer formatting is wrong

2. **Default assumptions** need explicit guidance
   - Test 20: LLM picks arbitrary metric without guidance
   - Solution: Add explicit rules to system prompt

3. **Named entity filtering** is critical for natural queries
   - Users naturally say "Holiday Sale campaign", not UUIDs
   - This is a must-have for production UX

4. **DSL limitations** surfaced with richer data
   - Test 15: Cannot filter by metric values (ROAS > 4)
   - This is an architectural gap, not a prompt issue

### What's Working Well ✅
- Multi-platform data (Google, Meta, TikTok, Other)
- Sort order handling (lowest/highest)
- Basic metrics queries (all 24 metrics)
- Timeframe detection (100% accurate)
- Natural language quality (conversational, not robotic)

---

## 🚀 Recommended Next Steps

### Immediate (Week 3, Day 1-2)
1. ✅ Fix entities list formatting
2. ✅ Fix intent-first answer structure
3. ✅ Fix vague comparison defaults
4. ✅ Run test suite, verify 3 more tests pass

### Week 3-4
1. ✅ Implement named entity filtering (see plan)
2. ✅ Test "Holiday Sale campaign performance" queries
3. ✅ Run test suite, verify 1 more test passes

### Week 5+ (Optional)
1. Consider metric value filtering (if users request it)
2. Document data limitations (time-of-day, what-if)

---

## 📚 Documentation Created

1. **`ROADMAP_TO_NATURAL_COPILOT.md`** (UPDATED)
   - Added 7 new issues with root cause analysis
   - Updated phases 5-7 with detailed implementation plans
   - Updated priority matrix and success projections

2. **`NAMED_ENTITY_FILTERING_PLAN.md`** (NEW)
   - Complete 3-day implementation plan
   - DSL schema changes, executor updates, prompt updates
   - Unit tests and integration tests
   - Risk mitigation and future enhancements

3. **`ANALYSIS_SUMMARY_OCT8.md`** (THIS FILE)
   - Executive summary of all findings
   - Clear action items with effort estimates
   - Success rate projections

---

**Bottom Line**: System is 82% production-ready with clear, incremental path to 90%+ in 2 weeks. Focus on answer quality first (Phase 5), then enable name-based queries (Phase 6).

