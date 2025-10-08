# AI Implementation Prompt: Phase 1.1 Enhanced - Deep DSL & Context Improvements

**This is an ALTERNATIVE approach with deeper architectural changes for better long-term results.**

---

## Overview

Beyond fixing immediate issues, this enhanced approach improves the core DSL and context system for more natural, context-aware answers. This addresses root causes rather than symptoms.

---

## Enhanced Architecture Proposal

### 1. Rich Context DSL Extension 🏗️

**Current Problem**: DSL lacks rich context needed for natural answers.

**Enhanced Solution**: Extend DSL with comprehensive context fields.

```python
# backend/app/dsl/schema.py

class TimeContext(BaseModel):
    """Rich time context for natural language generation."""
    last_n_days: Optional[int]
    start: Optional[date]
    end: Optional[date]
    
    # NEW rich context fields
    natural_description: str  # "last week", "yesterday", "in October"
    tense: str  # "past", "present", "future"
    is_comparison: bool = False
    comparison_description: Optional[str]  # "compared to the previous week"
    
    # Granularity hints
    is_single_day: bool = False
    is_current_period: bool = False  # "today", "this week"
    period_type: Optional[str]  # "day", "week", "month", "quarter", "year"

class QueryContext(BaseModel):
    """Full query context for natural answer generation."""
    original_question: str
    detected_intent: str
    key_entities: List[str]  # ["google", "meta"] from the question
    question_type: str  # "factual", "comparison", "analysis", "diagnostic"
    expected_answer_style: str  # "number", "comparison", "explanation", "list"
    
    # Linguistic context
    verb_tense: str  # "past", "present", "future"
    formality_level: str  # "casual", "professional", "technical"
    urgency_indicators: List[str]  # ["urgent", "asap", "quickly"]
    
    # Domain context
    user_expertise_level: str  # "beginner", "intermediate", "expert"
    industry_context: Optional[str]  # "ecommerce", "saas", "local"

class MetricQuery(BaseModel):
    """Enhanced DSL with rich context."""
    # Existing fields...
    
    # NEW context-rich fields
    context: QueryContext
    time_context: TimeContext  # Replaces simple time_range
    
    # Answer hints
    answer_preferences: Dict[str, Any] = {
        "include_timeframe": True,
        "include_comparison": False,
        "include_workspace_avg": False,
        "max_sentences": 1,
        "tone": "conversational"
    }
```

---

### 2. Enhanced Intent Classification with NLP 🧠

**Current Problem**: Simple keyword matching misses nuances.

**Enhanced Solution**: Multi-layer intent classification.

```python
# backend/app/answer/advanced_intent_classifier.py

from dataclasses import dataclass
from typing import List, Dict, Tuple

@dataclass
class DetailedIntent:
    """Rich intent classification result."""
    primary_intent: str  # SIMPLE/COMPARATIVE/ANALYTICAL
    sub_intent: str  # "trend_analysis", "root_cause", "performance_check"
    
    # Detailed aspects
    wants_comparison: bool
    wants_trend: bool
    wants_explanation: bool
    wants_recommendation: bool
    
    # Answer style preferences
    preferred_length: str  # "brief", "moderate", "detailed"
    preferred_tone: str  # "casual", "professional", "technical"
    
    # Confidence scores
    confidence: float
    alternative_intents: List[Tuple[str, float]]

class AdvancedIntentClassifier:
    """Multi-layer intent classification system."""
    
    def __init__(self):
        self.intent_patterns = self._load_intent_patterns()
        self.context_rules = self._load_context_rules()
    
    def classify(self, question: str, dsl: MetricQuery, 
                 conversation_history: List[Dict] = None) -> DetailedIntent:
        """
        Advanced classification using multiple signals:
        1. Linguistic analysis (question structure)
        2. Keyword matching (enhanced)
        3. DSL structure analysis
        4. Conversation context
        5. Domain rules
        """
        
        # Layer 1: Linguistic analysis
        linguistic_features = self._extract_linguistic_features(question)
        
        # Layer 2: Enhanced keyword matching with context
        keyword_signals = self._match_contextual_keywords(question, linguistic_features)
        
        # Layer 3: DSL structure analysis
        dsl_signals = self._analyze_dsl_structure(dsl)
        
        # Layer 4: Conversation context
        context_signals = self._analyze_conversation_context(
            question, conversation_history or []
        )
        
        # Layer 5: Domain-specific rules
        domain_signals = self._apply_domain_rules(question, dsl)
        
        # Combine all signals
        intent = self._combine_signals(
            linguistic_features,
            keyword_signals,
            dsl_signals,
            context_signals,
            domain_signals
        )
        
        return intent
    
    def _extract_linguistic_features(self, question: str) -> Dict:
        """Extract linguistic features from question."""
        features = {
            "question_type": self._get_question_type(question),
            "has_comparison_structure": self._has_comparison_structure(question),
            "complexity_score": self._calculate_complexity(question),
            "urgency_level": self._detect_urgency(question),
            "formality_level": self._detect_formality(question)
        }
        return features
    
    def _get_question_type(self, question: str) -> str:
        """Determine question type from structure."""
        q_lower = question.lower().strip()
        
        if q_lower.startswith(("what", "how much", "how many")):
            if "compare" in q_lower or "vs" in q_lower:
                return "comparative_factual"
            return "simple_factual"
        
        elif q_lower.startswith("why"):
            if "not" in q_lower:
                return "negative_diagnostic"  # "why is X not working"
            return "explanatory"
        
        elif q_lower.startswith("when"):
            return "temporal_query"
        
        elif q_lower.startswith(("is", "are", "does", "do")):
            return "yes_no_question"
        
        elif "should i" in q_lower:
            return "recommendation_seeking"
        
        return "unknown"
```

---

### 3. Context-Aware Answer Builder 🎯

**Enhanced Solution**: Rich context throughout the pipeline.

```python
# backend/app/answer/context_aware_builder.py

class ContextAwareAnswerBuilder:
    """Enhanced answer builder with deep context awareness."""
    
    def build_answer(self, dsl: MetricQuery, result: MetricResult,
                     detailed_intent: DetailedIntent) -> str:
        """Build answer using rich context and detailed intent."""
        
        # Step 1: Select answer strategy based on detailed intent
        strategy = self._select_answer_strategy(detailed_intent)
        
        # Step 2: Extract comprehensive context
        context = self._extract_comprehensive_context(
            dsl=dsl,
            result=result,
            intent=detailed_intent
        )
        
        # Step 3: Build context-aware prompt
        prompt = self._build_contextual_prompt(
            strategy=strategy,
            context=context,
            preferences=dsl.answer_preferences
        )
        
        # Step 4: Generate with fallback layers
        answer = self._generate_with_fallbacks(prompt, context)
        
        # Step 5: Post-process for quality
        answer = self._post_process_answer(
            answer=answer,
            context=context,
            intent=detailed_intent
        )
        
        return answer
    
    def _extract_comprehensive_context(self, dsl, result, intent):
        """Extract all relevant context for answer generation."""
        
        context = {
            # Temporal context
            "time": {
                "period": dsl.time_context.natural_description,
                "tense": dsl.context.verb_tense,
                "is_current": dsl.time_context.is_current_period,
                "granularity": dsl.time_context.period_type
            },
            
            # Metric context
            "metric": {
                "name": dsl.metric,
                "value": result.summary,
                "formatted_value": format_metric_value(dsl.metric, result.summary),
                "performance_level": self._assess_performance(result),
                "is_zero": result.summary == 0,
                "has_data": result.summary is not None
            },
            
            # Comparison context (if applicable)
            "comparison": self._extract_comparison_context(dsl, result, intent),
            
            # Linguistic context
            "language": {
                "original_question": dsl.context.original_question,
                "key_phrases": self._extract_key_phrases(dsl.context.original_question),
                "formality": dsl.context.formality_level,
                "expertise": dsl.context.user_expertise_level
            },
            
            # Answer preferences
            "preferences": {
                "length": intent.preferred_length,
                "tone": intent.preferred_tone,
                "include_details": intent.wants_explanation,
                "include_recommendation": intent.wants_recommendation
            }
        }
        
        return context
```

---

### 4. Smart Fallback System 🛡️

**Enhanced Solution**: Intelligent fallbacks that maintain quality.

```python
class SmartFallbackSystem:
    """Multi-tier fallback system for robust answers."""
    
    def __init__(self):
        self.fallback_tiers = [
            self._tier1_enhanced_template,
            self._tier2_rule_based,
            self._tier3_simple_template,
            self._tier4_safe_default
        ]
    
    def generate_answer(self, context: Dict, intent: DetailedIntent) -> str:
        """Generate answer with intelligent fallbacks."""
        
        for tier_func in self.fallback_tiers:
            try:
                answer = tier_func(context, intent)
                if self._validate_answer(answer, context, intent):
                    return answer
            except Exception as e:
                logger.warning(f"Fallback tier failed: {e}")
                continue
        
        # Ultimate fallback
        return self._tier4_safe_default(context, intent)
    
    def _tier1_enhanced_template(self, context: Dict, intent: DetailedIntent) -> str:
        """Smart template with natural language generation."""
        
        templates = {
            ("SIMPLE", "past"): "Your {metric} was {value} {timeframe}.",
            ("SIMPLE", "present"): "Your {metric} is {value} {timeframe}.",
            ("COMPARATIVE", "past"): "Your {metric} was {value} {timeframe}, "
                                     "{comparison_phrase} {comparison_value}.",
            ("ANALYTICAL", "past"): "Your {metric} {trend_description} to {value} "
                                   "{timeframe}. {explanation} {recommendation}"
        }
        
        # Select and fill template
        key = (intent.primary_intent, context["time"]["tense"])
        template = templates.get(key, templates[("SIMPLE", "present")])
        
        return self._fill_template_naturally(template, context)
```

---

### 5. Platform Comparison Enhancement 🔄

**Enhanced Solution**: Native multi-dimensional comparison support.

```python
class ComparisonEngine:
    """Enhanced comparison handling for platform and other dimensions."""
    
    def handle_comparison_query(self, question: str, workspace_id: str) -> Dict:
        """Smart comparison query handling."""
        
        # Detect comparison type
        comparison_type = self._detect_comparison_type(question)
        
        if comparison_type == "platform":
            return self._handle_platform_comparison(question, workspace_id)
        elif comparison_type == "temporal":
            return self._handle_temporal_comparison(question, workspace_id)
        elif comparison_type == "entity":
            return self._handle_entity_comparison(question, workspace_id)
        
    def _handle_platform_comparison(self, question: str, workspace_id: str) -> Dict:
        """Enhanced platform comparison."""
        
        # Extract platforms
        platforms = self._extract_platforms(question)
        
        # Infer metric if not specified
        metric = self._infer_comparison_metric(question, platforms)
        
        # Build optimized DSL
        dsl = {
            "query_type": "metrics",
            "metric": metric,
            "time_range": {"last_n_days": 30},
            "breakdown": "provider",
            "filters": {
                "provider": platforms if len(platforms) > 0 else None
            },
            "comparison_mode": "side_by_side",  # NEW
            "include_winner": True,  # NEW
            "include_insights": True  # NEW
        }
        
        return dsl
```

---

## Implementation Strategy

### Phase 1: Immediate Fixes (2-3 days)
1. Implement basic timeframe/tense fixes from first document
2. Fix analytical intent detection
3. Fix platform comparison

### Phase 2: Enhanced Context (1 week)
1. Implement TimeContext and QueryContext
2. Update DSL schema
3. Enhance translator to populate context

### Phase 3: Advanced Classification (1 week)
1. Implement DetailedIntent
2. Build AdvancedIntentClassifier
3. Integrate with answer builder

### Phase 4: Smart Systems (1 week)
1. Implement SmartFallbackSystem
2. Build ComparisonEngine
3. Create ContextAwareAnswerBuilder

---

## Benefits of Enhanced Approach

1. **Better Intent Understanding**: Multi-layer classification catches nuances
2. **Richer Context**: More information for natural answers
3. **Smarter Fallbacks**: Quality maintained even when LLM fails
4. **Future-Proof**: Architecture ready for more advanced features
5. **Testable**: Each component independently testable

---

## Testing Strategy

```python
# Comprehensive test suite
class TestEnhancedSystem:
    
    def test_timeframe_context(self):
        """Test rich timeframe handling."""
        test_cases = [
            ("what was my ROAS last week", "Your ROAS was 4.36× last week"),
            ("how did I do in October", "Your ROAS was 4.36× in October"),
            ("compare this week to last week", "This week's ROAS of 4.36× is up 15% from last week's 3.78×")
        ]
    
    def test_detailed_intent(self):
        """Test advanced intent classification."""
        classifier = AdvancedIntentClassifier()
        
        result = classifier.classify("why is my ROAS volatile lately")
        assert result.primary_intent == "ANALYTICAL"
        assert result.sub_intent == "volatility_analysis"
        assert result.wants_explanation == True
        assert result.preferred_length == "detailed"
    
    def test_smart_fallbacks(self):
        """Test fallback quality."""
        fallback = SmartFallbackSystem()
        
        # Even with minimal context, should produce natural answer
        context = {"metric": "roas", "value": 4.36, "timeframe": "last week"}
        answer = fallback.generate_answer(context, DetailedIntent(...))
        
        assert "Your ROAS was 4.36× last week" in answer
        assert "selected period" not in answer  # No robotic language
```

---

## Migration Path

1. **Start Simple**: Implement Phase 1.1 fixes first
2. **Gradual Enhancement**: Add enhanced features incrementally
3. **A/B Testing**: Compare basic vs enhanced approaches
4. **Iterate**: Refine based on real usage

---

_This enhanced approach provides a more robust, scalable solution for natural language answers._
