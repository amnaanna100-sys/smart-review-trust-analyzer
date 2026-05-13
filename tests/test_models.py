"""
Unit tests for ML models
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.models import ModelManager
from backend.preprocessing import TextPreprocessor


class TestTextPreprocessor:
    """Tests for text preprocessing"""
    
    @pytest.fixture
    def preprocessor(self):
        return TextPreprocessor()
    
    def test_clean_text(self, preprocessor):
        """Test text cleaning"""
        text = "This is a TEST! @#$%"
        cleaned = preprocessor.clean_text(text)
        assert cleaned.islower()
        assert '@' not in cleaned
        assert '!' not in cleaned
    
    def test_remove_urls(self, preprocessor):
        """Test URL removal"""
        text = "Check out http://example.com for more info"
        cleaned = preprocessor.clean_text(text)
        assert 'http' not in cleaned
    
    def test_remove_emails(self, preprocessor):
        """Test email removal"""
        text = "Contact us at test@example.com for help"
        cleaned = preprocessor.clean_text(text)
        assert '@' not in cleaned
    
    def test_tokenization(self, preprocessor):
        """Test tokenization"""
        text = "This is a test"
        tokens = preprocessor.tokenize(text)
        assert isinstance(tokens, list)
        assert len(tokens) > 0
    
    def test_preprocessing_pipeline(self, preprocessor):
        """Test complete preprocessing pipeline"""
        text = "This is an EXCELLENT product! Check http://example.com"
        processed = preprocessor.preprocess(text)
        assert isinstance(processed, str)
        assert len(processed) > 0
        assert processed.islower()
    
    def test_batch_preprocessing(self, preprocessor):
        """Test batch preprocessing"""
        texts = [
            "Great product!",
            "Not satisfied",
            "Amazing quality"
        ]
        processed = preprocessor.batch_preprocess(texts)
        assert len(processed) == len(texts)
        assert all(isinstance(t, str) for t in processed)


class TestModelManager:
    """Tests for model management"""
    
    @pytest.fixture
    def model_manager(self):
        return ModelManager()
    
    def test_model_loading(self, model_manager):
        """Test if models are loaded (or gracefully handle missing models)"""
        # This test will pass even if models aren't loaded,
        # as long as the manager initializes without error
        assert model_manager is not None
        assert hasattr(model_manager, 'models')
        assert isinstance(model_manager.models, dict)
    
    def test_vectorizer_initialization(self, model_manager):
        """Test vectorizer initialization"""
        assert hasattr(model_manager, 'vectorizer')
    
    def test_fake_detection_method_exists(self, model_manager):
        """Test fake detection method"""
        assert hasattr(model_manager, 'predict_fake')
        assert callable(model_manager.predict_fake)
    
    def test_sentiment_method_exists(self, model_manager):
        """Test sentiment method"""
        assert hasattr(model_manager, 'predict_sentiment')
        assert callable(model_manager.predict_sentiment)
    
    def test_spam_method_exists(self, model_manager):
        """Test spam detection method"""
        assert hasattr(model_manager, 'predict_spam')
        assert callable(model_manager.predict_spam)
    
    def test_rating_method_exists(self, model_manager):
        """Test rating prediction method"""
        assert hasattr(model_manager, 'predict_rating')
        assert callable(model_manager.predict_rating)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
