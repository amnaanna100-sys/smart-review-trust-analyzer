"""
Tests for data preprocessing utilities
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.preprocessing import TextPreprocessor


class TestTextCleaning:
    """Test text cleaning functionality"""
    
    @pytest.fixture
    def preprocessor(self):
        return TextPreprocessor()
    
    def test_lowercase_conversion(self, preprocessor):
        """Test conversion to lowercase"""
        text = "THIS IS A TEST"
        result = preprocessor.clean_text(text)
        assert result.islower()
    
    def test_special_character_removal(self, preprocessor):
        """Test special character removal"""
        text = "Test@#$%^&*()"
        result = preprocessor.clean_text(text)
        assert '@' not in result
        assert '#' not in result
    
    def test_url_removal(self, preprocessor):
        """Test URL removal"""
        text = "Visit http://example.com for more"
        result = preprocessor.clean_text(text)
        assert 'http' not in result
    
    def test_email_removal(self, preprocessor):
        """Test email removal"""
        text = "Contact test@example.com now"
        result = preprocessor.clean_text(text)
        assert 'example' not in result
    
    def test_whitespace_normalization(self, preprocessor):
        """Test whitespace normalization"""
        text = "Test    with    multiple    spaces"
        result = preprocessor.clean_text(text)
        assert '    ' not in result


class TestTokenization:
    """Test tokenization"""
    
    @pytest.fixture
    def preprocessor(self):
        return TextPreprocessor()
    
    def test_tokenization_returns_list(self, preprocessor):
        """Test that tokenization returns list"""
        text = "This is a test"
        result = preprocessor.tokenize(text)
        assert isinstance(result, list)
    
    def test_tokenization_splits_words(self, preprocessor):
        """Test that tokenization splits words"""
        text = "one two three"
        result = preprocessor.tokenize(text)
        assert len(result) == 3


class TestStopwordRemoval:
    """Test stopword removal"""
    
    @pytest.fixture
    def preprocessor(self):
        return TextPreprocessor()
    
    def test_stopword_removal(self, preprocessor):
        """Test stopword removal"""
        tokens = ['the', 'cat', 'is', 'sitting']
        result = preprocessor.remove_stopwords(tokens)
        assert 'the' not in result
        assert 'is' not in result
        assert 'cat' in result


class TestStemming:
    """Test stemming"""
    
    @pytest.fixture
    def preprocessor(self):
        return TextPreprocessor()
    
    def test_stemming(self, preprocessor):
        """Test stemming functionality"""
        tokens = ['running', 'runs', 'ran']
        result = preprocessor.stem_tokens(tokens)
        # All should reduce to similar stems
        assert all(isinstance(t, str) for t in result)


class TestLemmatization:
    """Test lemmatization"""
    
    @pytest.fixture
    def preprocessor(self):
        return TextPreprocessor()
    
    def test_lemmatization(self, preprocessor):
        """Test lemmatization functionality"""
        tokens = ['running', 'runs']
        result = preprocessor.lemmatize_tokens(tokens)
        assert all(isinstance(t, str) for t in result)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
