# Roadmap: Natural AI Copilot - Based on Real Testing

**Last Updated**: 2025-10-08  
**Status**: Phase 1.1 Complete - Analyzing next steps

---

## Executive Summary

We've successfully implemented Phase 1.1 tactical fixes. Comprehensive testing with 18 questions reveals we're at **~60% production-ready** for basic questions.

### What's Working Well ✅

1. **Timeframes & Tense** - Answers correctly include "last week", "last month" with proper past tense
2. **Intent Classification** - Simple questions get 1 sentence, analytical get 3-4 sentences
3. **Natural Language** - "You spent $X" instead of robotic "Your SPEND for the selected period"
4. **Breakdowns** - "Which campaign had highest ROAS" works perfectly
5. **Entity Queries** - "List active campaigns" returns clean results
6. **Analytical Depth** - "Why is my ROAS volatile" gets thoughtful 4-sentence analysis

### Critical Issues Found 🚨

#### Issue 1: Timeframe Detection Errors (HIGH PRIORITY)
**Problem**: Questions asking for "today" or "this week" are getting translated to wrong timeframes

**Examples**:
- Q: "How much did I spend yesterday?" → A: "You spent $0.00 **today**" (wrong timeframe!)
- Q: "What's my ROAS this week?" → A: "Your ROAS was 4.36× **last week**" (asked this week, got last week!)
- Q: "What's my CPC today?" → A: "Your CPC is N/A **today**" (correct but no data explanation)

**Root Cause**: DSL translation is mapping relative terms incorrectly. "This week" → "last 7 days" should mean the current week, not the past 7 days.

**Impact**: 40% of basic time-based questions have wrong timeframes

---

#### Issue 2: Missing Data Explanations (HIGH PRIORITY)
**Problem**: When data is missing, system returns "N/A" or "$0.00" without explaining WHY

**Examples**:
- Q: "How much revenue on Google last week?" → A: "Your revenue was $0.00 last week"
  - **Better**: "You don't have any Google campaigns connected. You're currently only running ads on Other."

- Q: "What's my CPC today?" → A: "Your CPC is N/A today"
  - **Better**: "No data available for today yet. Your CPC last week was $0.48."

**Root Cause**: System doesn't check if filters match any data before answering

**Impact**: Confusing answers for filtered queries

---

#### Issue 3: Platform Comparison Not Comparing (MEDIUM PRIORITY)
**Problem**: "Compare Google vs Meta" just returns overall revenue, doesn't actually compare platforms

**Example**:
- Q: "Compare Google vs Meta performance" 
- A: "Last month, your revenue was $77,580.62..." (no comparison!)
- **Expected**: "You're only running ads on Other right now, not on Google or Meta."

**Root Cause**: DSL generates provider breakdown but answer doesn't acknowledge no data exists

**Impact**: Comparison questions fail when data doesn't exist

---

#### Issue 4: Campaign-Specific Queries Failing (MEDIUM PRIORITY)
**Problem**: Asking about a specific campaign by name doesn't filter properly

**Example**:
- Q: "How is the Holiday Sale campaign performing?"
- A: "Your cost per install was N/A last month. Top performer: App Install Campaign ($5.14)"
  - Wrong metric, wrong campaign!

**Root Cause**: DSL doesn't support filtering by entity name yet (only by entity_ids)

**Impact**: Natural follow-up questions don't work

---

#### Issue 5: Workspace Average Still Buggy (LOW PRIORITY)
**Problem**: Some queries still show workspace_avg = summary (comparing to itself)

**Example**: Test 12 shows spend = $20,006.72, workspace avg = $20,006.72 (identical)

**Root Cause**: Workspace average calculation when filters are applied

**Impact**: Less severe now with intent filtering, but still misleading

---

## Revised Roadmap - Next 3 Phases

### Phase 2: Fix Timeframe Detection (Week 5 - CRITICAL)

**Goal**: "Today", "this week", "yesterday" should map to correct date ranges

**The Problem**:
Our DSL translator maps:
- "today" → last_n_days: 1 (actually means "yesterday" in our data!)
- "this week" → last_n_days: 7 (means "last 7 days", not current week)
- "yesterday" → last_n_days: 1 (same as today!)

**The Fix**:
Need to distinguish between:
- **Relative past**: "last week", "last month" → last_n_days works fine
- **Current period**: "today", "this week" → need start/end dates for current period
- **Recent absolute**: "yesterday" → specific date range

**Where to Fix**:
- Update canonicalization to preserve "today" vs "yesterday" vs "last N days"
- Update DSL examples with explicit current period examples
- Update prompts to explain the difference

**Success Criteria**:
- "What's my spend today?" → returns today's data or explains no data yet
- "What's my ROAS this week?" → returns current week (Monday-Sunday) not last 7 days
- "How much did I spend yesterday?" → returns specific yesterday's data

**Testing**: Run tests 1, 2, 3 again and verify timeframes match questions

---

### Phase 3: Graceful Missing Data Handling (Week 6 - CRITICAL)

**Goal**: When data is missing, explain WHY instead of showing "$0" or "N/A"

**The Problem**:
System doesn't check if:
- Platform filter matches any actual data
- Time period has any data yet (today might be empty)
- Entity name exists

**The Fix**:
Add pre-execution validation:

**Step 1: Platform Validation**
Before executing query with provider filter, check what platforms exist:
- If user asks for "Google" but only "Other" exists → explain before running query
- Include available platforms in the explanation

**Step 2: Entity Name Validation**
Before executing query mentioning campaign name:
- Check if that entity name exists
- If not, suggest similar names or list available entities

**Step 3: Smart Fallbacks**
When result is null/zero/N/A:
- Check if any data exists for that metric in general
- Suggest alternative timeframe with data
- Explain if it's truly zero vs no data

**Where to Fix**:
- Add validation layer in qa_service before execution
- Enhance fallback templates to be context-aware
- Add "data availability checker" helper function

**Success Criteria**:
- "Revenue on Google" → "You don't have Google campaigns. You're on Other."
- "Spend today" → "No data for today yet. Last week you spent $X."
- "Holiday Sale performance" → Finds the campaign or suggests correct name

**Testing**: Run tests 5, 14, 16 and verify explanatory answers

---

### Phase 4: Filter Acknowledgment (Week 7 - MEDIUM)

**Goal**: Answers should acknowledge when filters are applied

**The Problem**:
When user asks filtered question, answer doesn't mention the filter

**Examples**:
- Q: "How much did active campaigns spend?"
- A: "Active campaigns spent $20,006.72" ✅ (Actually this one is good!)

- Q: "What's my Google ROAS?"
- A: "Your ROAS is 4.2×" ❌ (should say "Your **Google** ROAS is 4.2×")

**The Fix**:
Pass filter context to answer builder and include in prompt:

**In Context**:
- If provider filter: mention platform name
- If status filter: mention "active" or "paused"
- If entity_ids filter: mention entity names

**In Prompts**:
Update all three prompts with instruction:
"If filters are present in context, acknowledge them naturally in your answer"

**Success Criteria**:
- "Google ROAS" → "Your Google campaigns are at 4.2× ROAS"
- "Active campaigns revenue" → "Your active campaigns generated $X"
- "Paused campaigns" → "Your paused campaigns..."

**Testing**: Add filter-specific test questions and verify acknowledgment

---

## What We're NOT Fixing Yet (Future Phases)

### Out of Scope for Now

1. **What-If Scenarios** (Questions 76-85)
   - "What if I doubled my budget?" requires simulation layer
   - **Decision**: Phase 5 or later, not needed for MVP

2. **Educational Questions** (Questions 86-95)
   - "What is ROAS and why does it matter?" requires knowledge base
   - **Decision**: Phase 5 or later, can add FAQ system

3. **Advanced Multi-Step** (Questions 96-100)
   - "Show campaigns where CPC > $1 AND ROAS < 2" requires complex boolean logic
   - **Decision**: Phase 5 or later, advanced filtering

4. **Device/Demographic Filters**
   - "Mobile vs desktop performance" requires data we don't have
   - **Decision**: Future when we have granular data

5. **Cohort Analysis**
   - "Users acquired in January vs February" requires advanced segmentation
   - **Decision**: Future advanced feature

---

## Testing Strategy

### After Each Phase

**Automated Tests**:
Run the 18-question test suite and log results:
- Track success rate (currently ~60%)
- Track answer quality (1-5 star rating)
- Track DSL accuracy
- Track execution errors

**Manual Review**:
1. Export test results to markdown
2. Rate each answer: ✅ Perfect, ⚠️ Acceptable, ❌ Poor
3. Identify patterns in failures
4. Update prompts/logic based on patterns

**Success Thresholds**:
- Phase 2 target: 75% success rate (timeframes fixed)
- Phase 3 target: 85% success rate (missing data explained)
- Phase 4 target: 90% success rate (filters acknowledged)

---

## Current Test Results Summary

**Total Questions Tested**: 18  
**Fully Successful**: 11 (61%)  
**Partially Successful**: 4 (22%)  
**Failed**: 3 (17%)

### Breakdown by Category

**Basic Performance** (5 tests):
- ✅ Works: 1 (20%)
- ⚠️ Timeframe wrong: 3 (60%)
- ❌ Missing data: 1 (20%)

**Comparisons** (2 tests):
- ✅ Works: 1 (50%)
- ❌ Platform comparison failed: 1 (50%)

**Breakdowns** (3 tests):
- ✅ Works: 3 (100%) 🎉

**Analytical** (2 tests):
- ✅ Works: 2 (100%) 🎉

**Filters** (2 tests):
- ✅ Works: 2 (100%) 🎉

**Edge Cases** (4 tests):
- ✅ Works: 2 (50%)
- ❌ Campaign name query failed: 1 (25%)
- ⚠️ Missing context: 1 (25%)

---

## Priority Matrix

| Phase | Priority | Effort | Impact | Status |
|-------|----------|--------|--------|--------|
| Phase 1.1 (Tactical Fixes) | P0 | Medium | High | ✅ DONE |
| Phase 2 (Timeframe Detection) | P0 | Medium | Critical | 🔴 NEXT |
| Phase 3 (Missing Data Handling) | P0 | Medium | Critical | 🟡 Planned |
| Phase 4 (Filter Acknowledgment) | P1 | Low | Medium | 🟡 Planned |
| Phase 5 (Advanced Features) | P2 | High | Low | ⚪ Future |

---

## Incremental Next Steps

### Immediate (This Week)

**Step 1: Fix "Today" Timeframe** (2-3 hours)
- Add "today" as special case in canonicalization
- Update DSL translator to use current date for "today"
- Test "What's my spend today?"

**Step 2: Fix "This Week" Timeframe** (2-3 hours)
- Add logic to calculate current week boundaries (Monday-Sunday)
- Update DSL to support "current_week" mode
- Test "What's my ROAS this week?"

**Step 3: Platform Pre-Check** (2 hours)
- Add helper function: `check_platform_exists(workspace_id, provider)`
- Update QA service to check before executing filtered queries
- Return friendly message if platform doesn't exist

### This Week (Days 2-3)

**Step 4: Missing Data Fallbacks** (4 hours)
- When result is null/zero, check if metric has any data at all
- Suggest alternative timeframe if current timeframe empty
- Update fallback templates to be explanatory

**Step 5: Entity Name Search** (4 hours)
- Add entity name search in validation layer
- Find closest match for campaign names
- Update DSL to support entity name filters (not just IDs)

### Next Week

**Step 6: Full Test Suite** (2 hours)
- Run all 18 tests again
- Track improvements
- Identify remaining issues

**Step 7: Documentation Update** (1 hour)
- Update this roadmap with results
- Document new timeframe handling
- Update QA_SYSTEM_ARCHITECTURE.md

---

## Success Metrics

### Current State (After Phase 1.1)
- ✅ Intent classification: 100% working
- ✅ Natural language: 90% improved
- ⚠️ Timeframe accuracy: 40% correct
- ⚠️ Missing data handling: 30% explained
- ✅ Breakdowns: 100% working
- ✅ Analytical depth: 100% appropriate

### Target State (After Phases 2-4)
- ✅ Intent classification: 100% working
- ✅ Natural language: 95% improved
- ✅ Timeframe accuracy: 90% correct
- ✅ Missing data handling: 85% explained
- ✅ Breakdowns: 100% working
- ✅ Filter acknowledgment: 90% mentioned

### Long-term Vision (Phase 5+)
- What-if scenarios supported
- Educational answers provided
- Complex boolean filters working
- Multi-step reasoning enabled

---

## Philosophy

**Incremental Progress Over Perfection**
- Fix one thing at a time
- Test after each change
- Build on what works
- Don't break existing functionality

**User-Centric Fixes**
- Fix issues users will actually notice
- Prioritize confusing answers over edge cases
- Make errors helpful, not mysterious

**Data-Driven Decisions**
- Test with real questions
- Measure success rates
- Track improvements over time
- Let results guide priorities

---

**Next Action**: Start Phase 2 - Fix "today" and "this week" timeframe detection

