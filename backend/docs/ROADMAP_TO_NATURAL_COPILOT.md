# Roadmap: From Robotic Templates to Natural AI Copilot

**Goal**: Successfully answer questions 1-85 from `100-realistic-questions.md` with natural, context-appropriate responses.

**Philosophy**: Let AI do its thing. Focus on fundamentals over complexity. Maintain separation of concerns.

---

## Phase 0: Current State Analysis (Where We Are Now)

### ✅ **What's Working**

1. **DSL Translation** (Questions → Structured Queries)
   - 24 metrics supported (spend, revenue, ROAS, CPC, etc.)
   - Complex queries: breakdowns, comparisons, filters
   - Context-aware follow-ups
   - **Coverage**: ~70% of questions 1-60

2. **Query Execution**
   - Workspace-scoped (secure)
   - Derived metrics calculated correctly
   - Timeseries and breakdowns working
   - **Performance**: 10-50ms query time

3. **Architecture**
   - Clean separation: DSL → Plan → Execute → Answer
   - Single source of truth for formulas (`app/metrics/`)
   - Comprehensive testing (100+ tests)
   - **Quality**: Production-ready pipeline

### ❌ **Critical Problems**

#### **Problem 1: Workspace Average Bug** 🐛
```json
{
  "summary": 3.8777280833639898,
  "workspace_avg": 3.8777280833639898  // ← Same value! Bug!
}
```

**Root Cause**: `_calculate_workspace_avg()` is likely using the same filters as the main query instead of calculating a true workspace-wide average.

**Impact**: Rich context says "right in line with your workspace average" when it's actually just comparing to itself.

**Fix Required**: Ensure workspace avg calculation ignores query filters.

---

#### **Problem 2: Over-Contextualization** 📝

**User Question**: "what was my roas last month"

**Current Answer** (Too verbose):
> "Your ROAS is stable at 3.88×, which is right in line with your workspace average of 3.88×. Over time, it has shown some volatility, peaking at 5.80× and dipping as low as 1.38× recently. While the current performance is average, keeping an eye on these fluctuations could help you identify opportunities for improvement."

**Expected Answer** (Natural):
> "Your ROAS last month was 3.88×."

**Root Cause**: DSL v2.0.1 always includes full rich context (trends, workspace comparison, performance assessment) even for simple fact queries.

**Impact**: Answers feel like AI is overthinking simple questions.

---

#### **Problem 3: No Intent Detection** 🎯

The system treats all questions the same:
- Simple fact: "what was my roas" → Gets full analysis
- Comparative: "how does my roas compare" → Should get rich context
- Analytical: "why is my roas low" → Should get very rich context

**Missing**: Intent classification to match answer depth to question type.

---

#### **Problem 4: Robotic Phrasing** 🤖

Even with GPT rephrasing, answers sometimes sound formal:
- "Your ROAS for the selected period is..."
- "That's a +18.9% change vs the previous period."

**Natural alternatives**:
- "Your ROAS last week was 2.45×"
- "That's up 19% from the week before"

---

### 📊 **Coverage Gap Analysis**

Questions we can answer today:

| Category | Questions | Coverage | Quality |
|----------|-----------|----------|---------|
| **Basic Performance (1-20)** | 20 | 90% | Robotic |
| **Comparisons (21-40)** | 20 | 60% | Mixed |
| **Breakdowns (41-60)** | 20 | 70% | Good |
| **Filters (61-75)** | 15 | 50% | Needs work |
| **Scenarios (76-85)** | 10 | 0% | Not implemented |

**Gap Summary**:
- ✅ Can answer most basic metrics questions (1-20)
- ⚠️ Comparison answers need better phrasing (21-40)
- ✅ Breakdown/ranking queries work well (41-60)
- ⚠️ Filter queries need better DSL coverage (61-75)
- ❌ What-if scenarios not supported (76-85)

---

## Phase 1: Fix Critical Bugs (Week 1)

**Goal**: Fix workspace avg calculation and prevent over-contextualization.

📋 **IMPLEMENTATION GUIDE**: See [PHASE_1_IMPLEMENTATION_SPEC.md](./PHASE_1_IMPLEMENTATION_SPEC.md) for detailed specification.

🤖 **AI PROMPT**: See [AI_PROMPT_PHASE_1.md](./AI_PROMPT_PHASE_1.md) for copy-paste prompt to give an AI IDE.

### Task 1.1: Fix Workspace Average Calculation 🐛

**File**: `backend/app/dsl/executor.py`

**Current Code** (line ~654):
```python
query = (
    db.query(...)
    .join(E, E.id == MF.entity_id)
    .filter(E.workspace_id == workspace_id)
)
```

**Problem**: This is correct. But check if filters are being applied elsewhere.

**Action**:
1. Add debug logging to `_calculate_workspace_avg()` to see what's being calculated
2. Verify filters are NOT being applied to workspace avg query
3. Add test case: Query with filters should have different workspace_avg than summary
4. Document expected behavior in function docstring

**Test**:
```python
def test_workspace_avg_ignores_filters():
    """Workspace avg should be calculated across ALL entities, not just filtered ones."""
    query = MetricQuery(
        metric="roas",
        time_range=TimeRange(last_n_days=30),
        filters=Filters(provider="google")  # Filter to Google only
    )
    result = execute_plan(db, workspace_id, plan)
    
    # Summary: Google ROAS only
    # workspace_avg: All platforms ROAS
    assert result.summary != result.workspace_avg  # Should be different!
```

**Success Criteria**: Workspace avg is calculated without query filters.

---

### Task 1.2: Intent-Based Answer Depth 🎯

**Goal**: Match answer complexity to question intent.

**New File**: `backend/app/answer/intent_classifier.py`

```python
"""
Intent Classifier - Determines answer depth based on question type

WHAT: Classifies user questions into intent categories
WHY: Match answer complexity to what user actually wants
WHERE: Called by AnswerBuilder before context extraction

Intent Levels:
- SIMPLE: "what was my roas" → Just the number
- COMPARATIVE: "how does my roas compare" → Include comparison context
- ANALYTICAL: "why is my roas low" → Full rich context
"""

from enum import Enum
from typing import Optional

class AnswerIntent(str, Enum):
    SIMPLE = "simple"          # Just give me the number
    COMPARATIVE = "comparative" # Compare to something
    ANALYTICAL = "analytical"   # Explain the why/how

def classify_intent(question: str, query: MetricQuery) -> AnswerIntent:
    """
    Classify user intent from question and DSL.
    
    SIMPLE intent signals:
    - Question starts with "what/how much/how many"
    - No comparison in DSL (compare_to_previous=False)
    - No breakdown requested
    - Examples: "what was my roas", "how much did I spend"
    
    COMPARATIVE intent signals:
    - Question contains "compare/vs/versus/better/worse"
    - DSL has compare_to_previous=True OR breakdown present
    - Examples: "compare google vs meta", "how does this week compare"
    
    ANALYTICAL intent signals:
    - Question contains "why/explain/analyze/trend"
    - User explicitly asks for insights
    - Examples: "why is my roas low", "explain the trend"
    
    Returns:
        AnswerIntent: Classification for answer depth
    """
    question_lower = question.lower()
    
    # Analytical: explicitly asking for explanation
    analytical_keywords = ["why", "explain", "analyze", "trend", "pattern", "insight"]
    if any(kw in question_lower for kw in analytical_keywords):
        return AnswerIntent.ANALYTICAL
    
    # Comparative: asking to compare things
    comparative_keywords = ["compare", "vs", "versus", "better", "worse", "higher", "lower"]
    has_comparison = query.compare_to_previous or query.breakdown is not None
    if any(kw in question_lower for kw in comparative_keywords) or has_comparison:
        return AnswerIntent.COMPARATIVE
    
    # Simple: just asking for a value
    simple_keywords = ["what", "how much", "how many", "show me"]
    if any(question_lower.startswith(kw) for kw in simple_keywords):
        return AnswerIntent.SIMPLE
    
    # Default to comparative (safe middle ground)
    return AnswerIntent.COMPARATIVE
```

**Modify**: `backend/app/answer/answer_builder.py`

```python
def build_answer(self, dsl, result, ...):
    # Classify intent
    intent = classify_intent(dsl.question, dsl)
    
    if dsl.query_type == "metrics":
        context = extract_rich_context(result, dsl, workspace_avg=...)
        
        # Filter context based on intent
        if intent == AnswerIntent.SIMPLE:
            # Only include basic value, no comparisons/trends
            simplified_context = {
                "metric_name": context.metric_name,
                "metric_value": context.metric_value,
                "metric_value_raw": context.metric_value_raw
            }
            user_prompt = self._build_simple_prompt(simplified_context, dsl)
        elif intent == AnswerIntent.COMPARATIVE:
            # Include comparison + top performer, skip trends
            # ... filter context ...
        else:  # ANALYTICAL
            # Include everything (current behavior)
            user_prompt = self._build_rich_context_prompt(context, dsl)
```

**New Prompts**:

```python
SIMPLE_ANSWER_PROMPT = """You are a helpful marketing analytics assistant.

The user asked a simple factual question. Give them a direct, concise answer.

RULES:
1. Answer in ONE sentence
2. State the metric value clearly
3. NO comparisons, NO analysis, NO recommendations
4. Be conversational but brief

Examples:
- "Your ROAS last month was 3.88×"
- "You spent $1,234 yesterday"
- "Your CPC this week is $0.48"

Remember: Keep it simple. They asked for a fact, not an analysis."""
```

**Test**:
```bash
# Simple intent
Q: "what was my roas last month"
A: "Your ROAS last month was 3.88×"  # ✅ Just the fact

# Comparative intent
Q: "how does my roas compare to last month"
A: "Your ROAS is 3.88× this month, up 12% from last month's 3.46×"  # ✅ Comparison

# Analytical intent  
Q: "why is my roas so volatile"
A: "Your ROAS has been volatile, ranging from 1.38× to 5.80× over the past month..."  # ✅ Full analysis
```

**Success Criteria**:
- ✅ Simple questions get 1-sentence answers
- ✅ Comparative questions get comparison context
- ✅ Analytical questions get full rich context

---

## Phase 2: Natural Language Polish (Week 2)

**Goal**: Make answers feel human, not robotic.

### Task 2.1: Enhance GPT Prompts for Naturalness

**Modify**: `backend/app/nlp/prompts.py`

Update `SIMPLE_ANSWER_PROMPT`, `COMPARATIVE_ANSWER_PROMPT`, `ANALYTICAL_ANSWER_PROMPT` with better examples:

```python
COMPARATIVE_ANSWER_PROMPT = """You are a helpful marketing analytics colleague.

The user wants to compare metrics. Give them a clear comparison in natural language.

TONE: Conversational, like explaining to a friend over coffee
STYLE: Use contractions (it's, you're), avoid formal business speak

Good examples:
- "Your ROAS jumped to 2.45× this week—that's 19% better than last week"
- "Google's crushing it at $0.32 CPC while Meta's at $0.51"
- "Summer Sale is your top performer at 3.20× ROAS, way ahead of the others"

Bad examples (too formal):
- "Your ROAS for the selected period is 2.45×. That represents a +19.0% change."
- "The Google platform demonstrates superior performance..."

Remember: Speak like a human, not a report."""
```

### Task 2.2: Remove Template Fallbacks

**Current**: If GPT fails, system uses robotic templates

**Change**: Make GPT calls more reliable so fallbacks are rarely used
- Increase timeout from 5s to 10s
- Add retry logic (1 retry with exponential backoff)
- Only use fallback as last resort

**Modify**: `backend/app/answer/answer_builder.py`

```python
async def build_answer(self, ...):
    max_retries = 1
    for attempt in range(max_retries + 1):
        try:
            response = self.client.chat.completions.create(...)
            return response.choices[0].message.content.strip()
        except Exception as e:
            if attempt < max_retries:
                await asyncio.sleep(0.5 * (2 ** attempt))  # Exponential backoff
                continue
            else:
                logger.error(f"All retries exhausted: {e}")
                return self.build_fallback(result, dsl)  # Last resort
```

---

## Phase 3: Expand Question Coverage (Week 3)

**Goal**: Handle questions 61-75 (filters & segments).

### Task 3.1: Better Filter Support

**Current Gap**: Questions like "What's my ROAS for Google campaigns only?" work, but answers don't acknowledge the filter.

**Example**:
```
Q: "What's my ROAS for Google campaigns?"
A: "Your ROAS is 4.2×"  # ❌ Doesn't mention it's Google-only

Better:
A: "Your Google campaigns are at 4.2× ROAS"  # ✅ Acknowledges filter
```

**Solution**: Include filters in context sent to GPT

**Modify**: `backend/app/answer/context_extractor.py`

```python
class RichContext:
    # ... existing fields ...
    filters_applied: Optional[Dict[str, str]] = None  # NEW
```

```python
def extract_rich_context(result, query, workspace_avg):
    context = RichContext()
    # ... existing extraction ...
    
    # Extract filters
    if query.filters:
        filters_dict = {}
        if query.filters.provider:
            filters_dict["platform"] = query.filters.provider.capitalize()
        if query.filters.status:
            filters_dict["status"] = query.filters.status
        if query.filters.level:
            filters_dict["entity_type"] = query.filters.level
        
        if filters_dict:
            context.filters_applied = filters_dict
    
    return context
```

**Update prompt to acknowledge filters**:
```python
"""
...
- If filters_applied exists, mention it in your answer
  Example: "Your Google campaigns are at 4.2× ROAS"
  Example: "Active campaigns spent $1,234 yesterday"
...
"""
```

### Task 3.2: Goal-Aware Answers

**Future Enhancement** (not in Phase 3):
Some questions ask about campaign-type specific metrics:
- "How are my retargeting campaigns performing?"
- "What's my conversion rate on mobile?"

These require entity metadata (tags, device targeting) not yet in our data model.

**Action**: Document as future enhancement, skip for now.

---

## Phase 4: Testing & Validation (Week 4)

**Goal**: Systematically test questions 1-85 and measure success rate.

### Task 4.1: Create Test Harness

**New File**: `backend/app/tests/test_realistic_questions.py`

```python
"""
Test harness for 100 realistic questions.

Loads questions from docs/100-realistic-questions.md
Tests DSL generation, execution, and answer quality.
"""

import pytest
from app.services.qa_service import QAService

# Load questions from markdown
BASIC_QUESTIONS = [
    "What's my CPC today?",
    "How much did I spend yesterday?",
    "What's my ROAS this week?",
    # ... 1-20 ...
]

COMPARISON_QUESTIONS = [
    "How does this week compare to last week?",
    "Compare Google vs Meta performance this month",
    # ... 21-40 ...
]

@pytest.mark.parametrize("question", BASIC_QUESTIONS)
async def test_basic_questions(question, qa_service, workspace_id):
    """Test that basic questions get simple, direct answers."""
    result = await qa_service.answer(
        question=question,
        workspace_id=workspace_id,
        user_id="test_user"
    )
    
    # Success criteria:
    assert result["answer"] is not None
    assert len(result["answer"]) < 200  # Should be concise
    assert result["executed_dsl"]["query_type"] == "metrics"
    
    # Answer quality checks:
    answer = result["answer"]
    assert not answer.startswith("Your")  # Avoid robotic "Your X is..."
    # Add more quality checks...
```

### Task 4.2: Manual Quality Review

**Process**:
1. Run test harness to get answers for all questions 1-60
2. Export to CSV: question, DSL, answer, data
3. Manual review: Rate each answer 1-5 stars
4. Identify patterns in low-rated answers
5. Iterate on prompts/intent classification

**Success Criteria**:
- 80% of questions 1-60 get 4+ star ratings
- 90% generate valid DSL
- 95% execute without errors

---

## Phase 5: What-If Scenarios (Future - Week 5+)

**Goal**: Handle questions 76-85 (simulations, what-if analysis).

**Examples**:
- "How much revenue would I have if my AOV was 40% higher?"
- "What if I doubled my budget on Campaign X?"
- "What's my break-even ROAS?"

**Challenges**:
- Requires computation layer beyond current query engine
- Need to fetch current data, then simulate changes
- May need multi-step LLM planning ("first get current AOV, then calculate 40% increase, then project revenue")

**Approach**:
1. **Simple Calculations**: Build calculator functions (e.g., `calculate_breakeven_roas`)
2. **Simulation Endpoint**: New `/qa/simulate` endpoint for what-if queries
3. **Multi-Step Planning**: LLM breaks question into steps, executes each

**Timeline**: After Phase 4 is solid (not a priority for initial launch)

---

## Implementation Priority

### ✅ **Phase 1 (Week 1)**: CRITICAL - Fix Bugs
- [ ] Fix workspace avg calculation bug
- [ ] Implement intent classification
- [ ] Add simple/comparative/analytical answer modes
- [ ] Test with 10 representative questions

### ⚠️ **Phase 2 (Week 2)**: HIGH - Polish
- [ ] Enhance GPT prompts for naturalness
- [ ] Add retry logic for GPT calls
- [ ] Update tests for new answer styles
- [ ] Test with 20 questions

### 📊 **Phase 3 (Week 3)**: MEDIUM - Coverage
- [ ] Add filter acknowledgment in answers
- [ ] Document unsupported question types
- [ ] Test with questions 1-75

### 🧪 **Phase 4 (Week 4)**: MEDIUM - Validation
- [ ] Build test harness
- [ ] Run full suite 1-85
- [ ] Manual quality review
- [ ] Iterate based on feedback

### 🔮 **Phase 5 (Future)**: LOW - Advanced Features
- [ ] What-if scenarios (76-85)
- [ ] Educational questions (86-95)
- [ ] Advanced multi-step (96-100)

---

## Success Metrics

### Week 1 Targets
- ✅ Workspace avg bug fixed (verified with test)
- ✅ Simple questions get 1-sentence answers
- ✅ 10/10 test questions pass quality check

### Week 2 Targets
- ✅ Answers sound natural (not robotic)
- ✅ <5% fallback rate (GPT succeeds 95%+ of time)
- ✅ 18/20 test questions pass quality check

### Week 3 Targets
- ✅ Filtered questions acknowledged ("Your Google campaigns...")
- ✅ Questions 1-75: 80% coverage, 70% quality

### Week 4 Targets
- ✅ Questions 1-60: 90% coverage, 80% quality
- ✅ Test harness integrated in CI/CD
- ✅ Manual review process documented

---

## Architecture Principles

### Separation of Concerns

```
┌─────────────────────────────────────────────────┐
│ Question Understanding (app/nlp/)               │
│ - Canonicalize                                  │
│ - Translate to DSL                              │
│ - Validate                                      │
└─────────────────┬───────────────────────────────┘
                  ▼
┌─────────────────────────────────────────────────┐
│ Query Execution (app/dsl/)                      │
│ - Plan query                                    │
│ - Execute against DB                            │
│ - Return structured results                     │
└─────────────────┬───────────────────────────────┘
                  ▼
┌─────────────────────────────────────────────────┐
│ Answer Generation (app/answer/)                 │
│ - Classify intent (NEW)                         │
│ - Extract appropriate context                   │
│ - Generate natural language                     │
└─────────────────────────────────────────────────┘
```

Each layer should be:
- **Independently testable**
- **Clearly documented**
- **Single responsibility**
- **Minimal dependencies**

---

## Documentation Updates

### After Each Phase

**Update `QA_SYSTEM_ARCHITECTURE.md`**:
- Add Intent Classification section (Phase 1)
- Update Answer Generation flow diagram (Phase 1)
- Document new answer modes (Phase 1)
- Add test coverage stats (Phase 4)

**Update `ADNAVI_BUILD_LOG.md`**:
- Changelog entry for each phase
- Example before/after for major changes
- Known issues / tech debt

**Create New Docs**:
- `INTENT_CLASSIFICATION.md`: Deep dive on intent detection
- `ANSWER_QUALITY_RUBRIC.md`: How we measure answer quality
- `TESTING_GUIDE.md`: How to run test harness, interpret results

---

## Next Steps (Immediate Action)

### Step 1: Debug Workspace Avg (Today)
```bash
# Add debug logging
cd backend
# Edit app/dsl/executor.py, add logs to _calculate_workspace_avg
# Run a test query and check logs
```

### Step 2: Implement Intent Classification (Tomorrow)
```bash
# Create new file
touch app/answer/intent_classifier.py
# Implement classify_intent() function
# Add tests
# Wire into AnswerBuilder
```

### Step 3: Create Simple Answer Mode (Day 3)
```bash
# Update prompts.py with SIMPLE_ANSWER_PROMPT
# Modify AnswerBuilder to use intent
# Test with "what was my roas last month"
```

### Step 4: Test & Iterate (Day 4-5)
```bash
# Test 10 questions manually
# Collect feedback
# Adjust prompts/thresholds
# Repeat
```

---

## Questions to Answer

Before starting implementation:

1. **Workspace Avg Bug**: Confirm it's actually a bug by checking the calculation logic
2. **Intent Thresholds**: What keywords/patterns reliably indicate each intent?
3. **Answer Length**: What's acceptable range for simple/comparative/analytical?
4. **Fallback Rate**: What % GPT failure rate is acceptable?
5. **Test Data**: Do we have enough diverse data to test all question types?

---

_This roadmap is a living document. Update it as we learn and iterate._

_Last updated: 2025-10-08_

