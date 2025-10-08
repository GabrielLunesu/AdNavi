"""
Tests for Intent Classifier

WHAT: Verify intent classification works correctly
WHY: Ensures questions are routed to appropriate answer depth
WHERE: Tests app/answer/intent_classifier.py
"""

import pytest
from app.answer.intent_classifier import classify_intent, AnswerIntent, explain_intent
from app.dsl.schema import MetricQuery, TimeRange, Filters


class TestSimpleIntent:
    """Test SIMPLE intent classification."""
    
    def test_what_was_my_metric(self):
        """Simple fact questions should be classified as SIMPLE."""
        questions = [
            "what was my roas last month",
            "what's my cpc today",
            "what is my conversion rate",
        ]
        
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=30),
            compare_to_previous=False,
            breakdown=None
        )
        
        for question in questions:
            intent = classify_intent(question, query)
            assert intent == AnswerIntent.SIMPLE, \
                f"'{question}' should be SIMPLE, got {intent}"
    
    def test_how_much_did_i(self):
        """'How much' questions should be SIMPLE."""
        questions = [
            "how much did I spend yesterday",
            "how much revenue did I make",
            "how many clicks did I get"
        ]
        
        query = MetricQuery(
            metric="spend",
            time_range=TimeRange(last_n_days=1),
            compare_to_previous=False,
            breakdown=None
        )
        
        for question in questions:
            intent = classify_intent(question, query)
            assert intent == AnswerIntent.SIMPLE
    
    def test_show_me_queries(self):
        """'Show me' should be SIMPLE if no breakdown."""
        question = "show me my roas"
        
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7),
            compare_to_previous=False,
            breakdown=None
        )
        
        intent = classify_intent(question, query)
        assert intent == AnswerIntent.SIMPLE


class TestComparativeIntent:
    """Test COMPARATIVE intent classification."""
    
    def test_explicit_comparison_keywords(self):
        """Questions with 'compare', 'vs', etc. should be COMPARATIVE."""
        questions = [
            "compare google vs meta",
            "how does this week compare to last week",
            "is google better than meta",
            "which platform is worse"
        ]
        
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7)
        )
        
        for question in questions:
            intent = classify_intent(question, query)
            assert intent == AnswerIntent.COMPARATIVE, \
                f"'{question}' should be COMPARATIVE, got {intent}"
    
    def test_which_questions(self):
        """'Which X' questions are typically comparative."""
        questions = [
            "which campaign had highest roas",
            "which platform performed best",
            "what campaign spent the most"
        ]
        
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7),
            breakdown="campaign",
            top_n=1
        )
        
        for question in questions:
            intent = classify_intent(question, query)
            assert intent == AnswerIntent.COMPARATIVE
    
    def test_dsl_has_comparison(self):
        """If DSL has compare_to_previous, should be COMPARATIVE."""
        question = "what was my roas"  # Looks simple
        
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7),
            compare_to_previous=True  # But DSL has comparison
        )
        
        intent = classify_intent(question, query)
        assert intent == AnswerIntent.COMPARATIVE
    
    def test_dsl_has_breakdown(self):
        """If DSL has breakdown, should be COMPARATIVE."""
        question = "show me roas"  # Looks simple
        
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7),
            breakdown="campaign"  # But DSL has breakdown
        )
        
        intent = classify_intent(question, query)
        assert intent == AnswerIntent.COMPARATIVE


class TestAnalyticalIntent:
    """Test ANALYTICAL intent classification."""
    
    def test_why_questions(self):
        """'Why' questions should always be ANALYTICAL."""
        questions = [
            "why is my roas low",
            "why did my cpc increase",
            "why is performance bad"
        ]
        
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7)
        )
        
        for question in questions:
            intent = classify_intent(question, query)
            assert intent == AnswerIntent.ANALYTICAL, \
                f"'{question}' should be ANALYTICAL, got {intent}"
    
    def test_explain_questions(self):
        """'Explain' questions should be ANALYTICAL."""
        questions = [
            "explain the trend in my roas",
            "explain why performance dropped",
            "can you explain this pattern"
        ]
        
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=30)
        )
        
        for question in questions:
            intent = classify_intent(question, query)
            assert intent == AnswerIntent.ANALYTICAL
    
    def test_analyze_questions(self):
        """'Analyze' questions should be ANALYTICAL."""
        questions = [
            "analyze my campaign performance",
            "give me an analysis of roas",
            "what's the analysis"
        ]
        
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=30)
        )
        
        for question in questions:
            intent = classify_intent(question, query)
            assert intent == AnswerIntent.ANALYTICAL
    
    def test_trend_questions(self):
        """Questions about trends should be ANALYTICAL."""
        questions = [
            "what's the trend in my roas",
            "show me the pattern",
            "is there a trend here"
        ]
        
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=30)
        )
        
        for question in questions:
            intent = classify_intent(question, query)
            assert intent == AnswerIntent.ANALYTICAL


class TestEdgeCases:
    """Test edge cases and ambiguous questions."""
    
    def test_empty_question(self):
        """Empty question should default to COMPARATIVE."""
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7)
        )
        
        intent = classify_intent("", query)
        assert intent == AnswerIntent.COMPARATIVE  # Safe default
    
    def test_ambiguous_question(self):
        """Ambiguous questions default to COMPARATIVE."""
        question = "roas"  # Just a metric name
        
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7)
        )
        
        intent = classify_intent(question, query)
        assert intent == AnswerIntent.COMPARATIVE
    
    def test_what_is_better_google_or_meta(self):
        """'What's better' should be COMPARATIVE, not SIMPLE."""
        question = "what's better, google or meta"
        
        query = MetricQuery(
            metric="roas",
            time_range=TimeRange(last_n_days=7),
            breakdown="provider"
        )
        
        intent = classify_intent(question, query)
        assert intent == AnswerIntent.COMPARATIVE  # Not SIMPLE!


class TestExplainIntent:
    """Test explain_intent helper function."""
    
    def test_explain_all_intents(self):
        """Verify all intents have explanations."""
        for intent in AnswerIntent:
            explanation = explain_intent(intent)
            assert explanation is not None
            assert len(explanation) > 0
            assert isinstance(explanation, str)
    
    def test_simple_explanation(self):
        """Verify SIMPLE intent explanation."""
        explanation = explain_intent(AnswerIntent.SIMPLE)
        assert "1 sentence" in explanation
        assert "no extra context" in explanation
    
    def test_comparative_explanation(self):
        """Verify COMPARATIVE intent explanation."""
        explanation = explain_intent(AnswerIntent.COMPARATIVE)
        assert "comparison" in explanation
        assert "moderate context" in explanation
    
    def test_analytical_explanation(self):
        """Verify ANALYTICAL intent explanation."""
        explanation = explain_intent(AnswerIntent.ANALYTICAL)
        assert "full rich context" in explanation
        assert "insights" in explanation

