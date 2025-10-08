# AI Implementation Prompt: Phase 1.1 - Critical Fixes

**Copy this entire prompt to your AI IDE (Cursor, GitHub Copilot, etc.) to implement Phase 1.1 fixes.**

---

## Context

Phase 1 implementation is complete but testing revealed 6 critical issues. This Phase 1.1 addresses Priority 1 & 2 issues that prevent the system from being production-ready.

**Test Results**: 1/7 questions fully satisfactory (14%), 3/7 partial (43%), 3/7 failed (43%)

**Critical Issues to Fix**:
1. ❌ Missing timeframe context in answers
2. ❌ Wrong verb tense (is/was)
3. ❌ Analytical questions broken ("why" gets 1-sentence answer)
4. ⚠️ Robotic fallback language
5. ❌ Platform comparison failing ("compare google vs meta" returns null)

---

## Task Overview

Implement Phase 1.1 fixes to make the system production-ready:

1. **Enhance DSL Schema** - Add timeframe and tense context
2. **Fix Intent Classifier** - Analytical questions not working
3. **Add Timeframe/Tense Extraction** - Pass to GPT for natural answers
4. **Update All Prompts** - Include timeframe and tense instructions
5. **Fix Platform Comparison** - DSL translation issue
6. **Fix Fallback Templates** - Remove robotic language

---

## Detailed Implementation Steps

### STEP 1: Enhance DSL Schema with Timeframe Context 🕐

**Problem**: Answers don't mention "last week", "today", etc.

**Solution**: Add timeframe description to DSL and pass to GPT.

**Action**:

1. **Modify `backend/app/dsl/schema.py`** - Add timeframe_description field:

```python
class MetricQuery(BaseModel):
    """Enhanced with timeframe context for natural answers."""
    
    # Existing fields...
    
    # NEW in Phase 1.1
    question: Optional[str] = Field(None, description="Original user question for tense/context")
    timeframe_description: Optional[str] = Field(None, description="Natural language timeframe like 'last week', 'today'")
    
    @root_validator
    def set_timeframe_description(cls, values):
        """Auto-generate timeframe description from time_range."""
        time_range = values.get('time_range')
        if time_range and not values.get('timeframe_description'):
            if time_range.last_n_days == 1:
                values['timeframe_description'] = 'today'
            elif time_range.last_n_days == 7:
                values['timeframe_description'] = 'last week'
            elif time_range.last_n_days == 30:
                values['timeframe_description'] = 'last month'
            elif time_range.last_n_days == 90:
                values['timeframe_description'] = 'last quarter'
            elif time_range.last_n_days == 365:
                values['timeframe_description'] = 'last year'
            elif time_range.last_n_days:
                values['timeframe_description'] = f'last {time_range.last_n_days} days'
            elif time_range.start and time_range.end:
                # Format dates nicely
                values['timeframe_description'] = f'from {time_range.start} to {time_range.end}'
        return values
```

2. **Update `backend/app/nlp/translator.py`** - Pass original question to DSL:

```python
def translate(self, question: str, context: Optional[List[ConversationContext]] = None) -> MetricQuery:
    """Translate natural language to DSL with original question preserved."""
    
    # ... existing code ...
    
    # After getting response from OpenAI
    dsl_dict = json.loads(response.choices[0].message.content)
    
    # NEW: Add original question for tense detection
    dsl_dict['question'] = question
    
    # Validate and return
    return validate_dsl(dsl_dict)
```

---

### STEP 2: Fix Analytical Intent Detection 🔍

**Problem**: "why is my ROAS volatile" gets SIMPLE answer instead of ANALYTICAL.

**Root Cause**: Intent classifier might be failing on "volatile" keyword.

**Action**:

1. **Debug by adding logging** to `backend/app/answer/intent_classifier.py`:

```python
def classify_intent(question: str, query: MetricQuery) -> AnswerIntent:
    """Classify user intent - ENHANCED DEBUG VERSION."""
    question_lower = question.lower().strip()
    
    # Add debug logging
    logger = logging.getLogger(__name__)
    logger.info(f"[INTENT_DEBUG] Question: '{question}'")
    logger.info(f"[INTENT_DEBUG] Question lower: '{question_lower}'")
    
    # ANALYTICAL: Explicitly asking for explanation or analysis
    analytical_keywords = [
        "why", "explain", "analyze", "analysis",
        "trend", "trending", "pattern", "patterns",
        "insight", "insights", "understand",
        "what's happening", "what happened",
        "problem", "issue", "volatile", "volatility",
        "fluctuating", "swinging", "unstable", "erratic"  # NEW keywords
    ]
    
    # Check each keyword and log matches
    for kw in analytical_keywords:
        if kw in question_lower:
            logger.info(f"[INTENT_DEBUG] Matched analytical keyword: '{kw}'")
            return AnswerIntent.ANALYTICAL
    
    # ... rest of the function with similar debug logging ...
```

2. **Add test case** to verify fix:

```python
def test_volatile_questions(self):
    """Test volatile and similar analytical keywords."""
    questions = [
        "why is my roas volatile",
        "why is my cpc fluctuating",
        "what's causing the swings in my roas",
        "my roas is unstable"
    ]
    
    query = MetricQuery(
        metric="roas",
        time_range=TimeRange(last_n_days=30)
    )
    
    for question in questions:
        intent = classify_intent(question, query)
        assert intent == AnswerIntent.ANALYTICAL, \
            f"'{question}' should be ANALYTICAL, got {intent}"
```

---

### STEP 3: Add Tense Detection Function 🕰️

**Problem**: Using "is" instead of "was" for past events.

**Solution**: Detect tense from question and timeframe.

**Action**:

1. **Create new function** in `backend/app/answer/intent_classifier.py`:

```python
from enum import Enum

class VerbTense(str, Enum):
    """Verb tense for answer generation."""
    PAST = "past"
    PRESENT = "present"
    FUTURE = "future"

def detect_tense(question: str, timeframe_desc: Optional[str] = None) -> VerbTense:
    """
    Detect appropriate verb tense for the answer.
    
    Rules:
    - "was", "did", "had" + past timeframes → PAST
    - "is", "are", "do" + "today", "now" → PRESENT
    - "will", "going to" → FUTURE
    - Default based on timeframe
    """
    question_lower = question.lower()
    
    # Past tense indicators
    past_indicators = ["was", "were", "did", "had", "spent", "made", "got", "generated"]
    past_timeframes = ["yesterday", "last week", "last month", "last year", "ago"]
    
    # Check question for past tense
    if any(word in question_lower for word in past_indicators):
        return VerbTense.PAST
    
    # Check timeframe for past
    if timeframe_desc:
        if any(tf in timeframe_desc.lower() for tf in past_timeframes):
            return VerbTense.PAST
    
    # Present tense indicators
    present_indicators = ["is", "are", "am", "do", "does", "have", "has"]
    present_timeframes = ["today", "now", "current", "this hour"]
    
    if any(word in question_lower for word in present_indicators):
        if timeframe_desc and any(tf in timeframe_desc.lower() for tf in present_timeframes):
            return VerbTense.PRESENT
        # "is" with past timeframe should be PAST
        elif timeframe_desc and any(tf in timeframe_desc.lower() for tf in past_timeframes):
            return VerbTense.PAST
    
    # Future tense indicators
    future_indicators = ["will", "going to", "gonna", "shall"]
    if any(word in question_lower for word in future_indicators):
        return VerbTense.FUTURE
    
    # Default based on timeframe
    if timeframe_desc:
        if "last" in timeframe_desc or "ago" in timeframe_desc or "yesterday" in timeframe_desc:
            return VerbTense.PAST
        elif "next" in timeframe_desc or "tomorrow" in timeframe_desc:
            return VerbTense.FUTURE
    
    # Default to present
    return VerbTense.PRESENT
```

---

### STEP 4: Update Answer Builder to Pass Context 🏗️

**Action**:

1. **Modify `backend/app/answer/answer_builder.py`** to pass timeframe and tense:

```python
def build_answer(self, dsl: MetricQuery, result: Union[MetricResult, Dict[str, Any]], 
                 window: Optional[Dict[str, date]] = None, log_latency: bool = False) -> tuple[str, Optional[int]]:
    """Build answer with timeframe and tense awareness."""
    
    start_time = time.time() if log_latency else None
    
    try:
        # Step 1: Classify intent (existing)
        question = getattr(dsl, 'question', None) or f"What is my {dsl.metric}?"
        intent = classify_intent(question, dsl)
        
        # NEW Step 1.5: Detect tense and get timeframe
        timeframe_desc = getattr(dsl, 'timeframe_description', None) or ""
        tense = detect_tense(question, timeframe_desc)
        
        logger.info(
            f"[INTENT] Classified as {intent.value} with {tense.value} tense: {explain_intent(intent)}",
            extra={"question": question, "intent": intent.value, "tense": tense.value, "timeframe": timeframe_desc}
        )
        
        # Step 2: Extract context and build prompt based on intent
        if dsl.query_type == "metrics":
            context = extract_rich_context(result=result, query=dsl, 
                                         workspace_avg=result.workspace_avg if isinstance(result, MetricResult) else None)
            
            # Filter context based on intent
            if intent == AnswerIntent.SIMPLE:
                filtered_context = {
                    "metric_name": context.metric_name,
                    "metric_value": context.metric_value,
                    "metric_value_raw": context.metric_value_raw,
                    "timeframe": timeframe_desc,  # NEW
                    "tense": tense.value  # NEW
                }
                system_prompt = SIMPLE_ANSWER_PROMPT
                user_prompt = self._build_simple_prompt(filtered_context, question)
```

2. **Update prompt builders** to include timeframe/tense:

```python
def _build_simple_prompt(self, context: Dict[str, Any], question: str) -> str:
    """Build prompt with timeframe and tense."""
    return f"""The user asked: "{question}"

Answer with ONE sentence stating the fact.

CONTEXT:
{json.dumps(context, indent=2)}

CRITICAL INSTRUCTIONS:
- Include the timeframe in your answer (e.g., "last week", "yesterday", "today")
- Use {context.get('tense', 'present')} tense (was/is/will be)
- If tense is "past", use "was" not "is"
- If timeframe is empty, don't mention time period

Examples:
- Past: "Your ROAS was 3.88× last week"
- Present: "Your ROAS is 3.88× today"
- With timeframe: "You spent $1,234 yesterday"
- Without timeframe: "Your ROAS is 3.88×"

Remember: Just the fact. One sentence. Include timeframe. Use correct tense."""
```

---

### STEP 5: Update GPT Prompts with Tense/Timeframe 📝

**Action**:

1. **Update `backend/app/nlp/prompts.py`** - All three prompts:

```python
SIMPLE_ANSWER_PROMPT = """You are a helpful marketing analytics assistant.

The user asked a SIMPLE factual question. They want a quick answer, not analysis.

YOUR TASK: Give them a direct, concise answer in ONE sentence.

CRITICAL RULES:
1. Answer in EXACTLY ONE sentence
2. State the metric value clearly
3. Include the timeframe from context (e.g., "last week", "yesterday")
4. Use the correct verb tense based on context.tense:
   - past: "was", "were", "spent", "had"
   - present: "is", "are", "spend", "have"
   - future: "will be", "will have"
5. NO comparisons unless explicitly in context
6. NO analysis, NO trends, NO recommendations
7. NO workspace average mentions
8. Be conversational but BRIEF
9. Use the formatted values (not raw numbers)

TENSE EXAMPLES:
- Past + timeframe: "Your ROAS was 3.88× last week"
- Past + timeframe: "You spent $1,234 yesterday"
- Present + timeframe: "Your CPC is $0.48 today"
- Present no timeframe: "Your conversion rate is 4.2%"
- Past no timeframe: "Your ROAS was 3.88×"

BAD Examples (wrong tense):
- "Your ROAS is 3.88× last week" ❌ Wrong tense (is → was)
- "You spend $1,234 yesterday" ❌ Wrong tense (spend → spent)

Remember: Match the tense, include timeframe, one sentence only."""
```

Similar updates for COMPARATIVE and ANALYTICAL prompts...

---

### STEP 6: Fix Platform Comparison 🔧

**Problem**: "compare google vs meta performance" returns null.

**Solution**: The DSL translator needs to handle platform comparison better.

**Action**:

1. **Check DSL translation** - Add few-shot example in `backend/app/nlp/prompts.py`:

```python
# Add to DSL_EXAMPLES
{
    "question": "compare google vs meta performance",
    "dsl": {
        "query_type": "metrics",
        "metric": "roas",  # Default metric for comparison
        "time_range": {"last_n_days": 30},
        "breakdown": "provider",  # KEY: breakdown by provider
        "group_by": "provider",
        "top_n": 10,
        "filters": {}
    }
},
{
    "question": "which platform performs better",
    "dsl": {
        "query_type": "metrics",
        "metric": "roas",
        "time_range": {"last_n_days": 30},
        "breakdown": "provider",
        "group_by": "provider",
        "top_n": 5,
        "filters": {}
    }
},
```

2. **Verify provider breakdown** is supported in executor.

---

### STEP 7: Fix Robotic Fallback Templates 🤖

**Problem**: Fallback uses "Your SPEND for the selected period is $0.00"

**Action**:

1. **Update `backend/app/services/qa_service.py`** fallback template:

```python
def _build_fallback_answer(self, dsl: MetricQuery, result: Any) -> str:
    """Build natural fallback answer when LLM fails."""
    
    # Get timeframe and tense
    timeframe = getattr(dsl, 'timeframe_description', '')
    question = getattr(dsl, 'question', '')
    tense = detect_tense(question, timeframe)
    
    if dsl.query_type == "metrics" and isinstance(result, MetricResult):
        metric_name = dsl.metric.upper()
        
        # Natural metric names
        natural_names = {
            "ROAS": "ROAS",
            "CPC": "cost per click", 
            "CPA": "cost per acquisition",
            "CTR": "click-through rate",
            "SPEND": "ad spend",
            "REVENUE": "revenue"
        }
        
        metric_display = natural_names.get(metric_name, metric_name.lower())
        
        # Format value
        value = format_metric_value(dsl.metric, result.summary)
        
        # Build natural sentence based on tense
        if tense == VerbTense.PAST:
            verb = "was" if metric_name not in ["SPEND", "REVENUE"] else ""
            if metric_name == "SPEND":
                return f"You spent {value}{' ' + timeframe if timeframe else ''}."
            elif metric_name == "REVENUE":
                return f"You generated {value} in revenue{' ' + timeframe if timeframe else ''}."
            else:
                return f"Your {metric_display} was {value}{' ' + timeframe if timeframe else ''}."
        else:
            verb = "is"
            return f"Your {metric_display} is {value}{' ' + timeframe if timeframe else ''}."
```

---

## Testing Checklist

After implementing all fixes, test these specific cases:

```bash
# Test 1: Timeframe context (was issue #1)
curl -X 'POST' 'http://localhost:8000/qa/?workspace_id=914019de-2190-4fcc-855a-d1e719d05cdc' \
  -H 'Content-Type: application/json' -b cookies.txt \
  -d '{"question": "what was my ROAS last week"}'
# Expected: "Your ROAS was 4.36× last week" ✅

# Test 2: Analytical intent (was issue #3)
curl -X 'POST' 'http://localhost:8000/qa/?workspace_id=914019de-2190-4fcc-855a-d1e719d05cdc' \
  -H 'Content-Type: application/json' -b cookies.txt \
  -d '{"question": "why is my ROAS volatile"}'
# Expected: 3-4 sentence analytical answer ✅

# Test 3: Platform comparison (was issue #5)
curl -X 'POST' 'http://localhost:8000/qa/?workspace_id=914019de-2190-4fcc-855a-d1e719d05cdc' \
  -H 'Content-Type: application/json' -b cookies.txt \
  -d '{"question": "compare google vs meta performance"}'
# Expected: Comparison answer with both platforms ✅

# Test 4: Natural fallback (was issue #4)
# Trigger fallback by breaking GPT temporarily
# Expected: "You spent $0.00 yesterday" not "Your SPEND for..." ✅
```

---

## Success Criteria

### Before Phase 1.1
- ❌ "Your ROAS is 4.36×" (missing timeframe, wrong tense)
- ❌ "why is volatile" → 1 sentence
- ❌ "compare platforms" → null
- ❌ "Your SPEND for the selected period"

### After Phase 1.1
- ✅ "Your ROAS was 4.36× last week"
- ✅ "why is volatile" → 3-4 sentence analysis
- ✅ "compare platforms" → comparison answer
- ✅ "You spent $1,234 yesterday"

---

## Implementation Order

1. **First**: Add DSL schema changes (timeframe_description, question)
2. **Second**: Fix analytical intent classifier (add keywords + debug)
3. **Third**: Add tense detection function
4. **Fourth**: Update answer builder to use timeframe/tense
5. **Fifth**: Update all 3 GPT prompts
6. **Sixth**: Fix platform comparison examples
7. **Last**: Fix fallback templates

---

## Quick Test Commands

```bash
# Run intent classifier tests
pytest backend/app/tests/test_intent_classifier.py -v -k "volatile"

# Run manual test script
python -m app.tests.test_phase1_manual

# Test specific question
curl -X 'POST' 'http://localhost:8000/qa/?workspace_id=YOUR_WORKSPACE_ID' \
  -H 'Content-Type: application/json' \
  -d '{"question": "YOUR TEST QUESTION"}'
```

---

_Ready to implement? Start with STEP 1 (DSL Schema enhancement) and work through all steps in order._

_Full test results: `backend/PHASE_1_TESTING_RESULTS.md`_
