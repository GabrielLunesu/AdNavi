"""
Translator Tests
================

Test LLM-based translation with mocked OpenAI client.

Tests:
- Translation with mock responses
- Error handling (API failures, invalid JSON)
- Canonicalization
- Schema validation

Mocking:
- Mock OpenAI client to avoid API calls during tests
- Provide known responses for reproducibility
"""

import pytest
from unittest.mock import Mock, MagicMock
from app.nlp.translator import Translator, TranslationError
from app.dsl.validate import DSLValidationError


class TestTranslator:
    """Test translator with mocked LLM."""
    
    @pytest.fixture
    def mock_client(self):
        """Create a mock OpenAI client."""
        client = Mock()
        return client
    
    def test_successful_translation(self, mock_client):
        """Test successful translation to valid DSL."""
        # Mock response
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = '''
        {
            "metric": "roas",
            "time_range": {"last_n_days": 7},
            "compare_to_previous": false,
            "group_by": "none",
            "breakdown": null,
            "top_n": 5,
            "filters": {}
        }
        '''
        mock_client.chat.completions.create.return_value = mock_response
        
        # Test translation
        translator = Translator(client=mock_client)
        dsl, latency = translator.to_dsl("What's my ROAS this week?", log_latency=True)
        
        assert dsl.metric == "roas"
        assert dsl.time_range.last_n_days == 7
        assert latency is not None
        assert latency > 0
    
    def test_invalid_json_response(self, mock_client):
        """Test handling of invalid JSON from LLM."""
        # Mock invalid JSON response
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "This is not JSON"
        mock_client.chat.completions.create.return_value = mock_response
        
        translator = Translator(client=mock_client)
        
        with pytest.raises(TranslationError) as exc_info:
            translator.to_dsl("Some question")
        
        assert "parse JSON" in str(exc_info.value).lower()
    
    def test_api_failure(self, mock_client):
        """Test handling of OpenAI API failure."""
        # Mock API exception
        mock_client.chat.completions.create.side_effect = Exception("API Error")
        
        translator = Translator(client=mock_client)
        
        with pytest.raises(TranslationError) as exc_info:
            translator.to_dsl("Some question")
        
        assert "API call failed" in str(exc_info.value)
    
    def test_invalid_dsl_schema(self, mock_client):
        """Test handling of LLM output that doesn't match DSL schema."""
        # Mock response with invalid metric
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = '''
        {
            "metric": "invalid_metric",
            "time_range": {"last_n_days": 7}
        }
        '''
        mock_client.chat.completions.create.return_value = mock_response
        
        translator = Translator(client=mock_client)
        
        with pytest.raises(DSLValidationError):
            translator.to_dsl("Some question")


class TestCanonicalization:
    """Test question canonicalization."""
    
    def test_metric_synonyms(self):
        """Test metric synonym mapping."""
        from app.dsl.canonicalize import canonicalize_question
        
        # Test various synonyms
        assert "roas" in canonicalize_question("What's my return on ad spend?")
        assert "cpa" in canonicalize_question("Show me cost per acquisition")
        assert "cvr" in canonicalize_question("What's the conversion rate?")
        assert "spend" in canonicalize_question("How much did we spend?")
    
    def test_time_phrases(self):
        """Test time phrase normalization."""
        from app.dsl.canonicalize import canonicalize_question
        
        # Test time phrase mapping
        assert "last 7 days" in canonicalize_question("What's my ROAS this week?")
        assert "last 30 days" in canonicalize_question("Show me revenue this month")
        assert "last 7 days" in canonicalize_question("How's my spend past week?")


# Run tests:
# pytest backend/app/tests/test_translator.py -v
