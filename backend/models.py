"""
Model management module for loading and inference
"""

import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer


class ModelManager:
    """Manages loading and inference of ML models"""
    
    def __init__(self, model_path='./models/trained_models/'):
        """
        Initialize model manager
        
        Args:
            model_path (str): Path to saved models
        """
        self.model_path = model_path
        self.models = {}
        self.vectorizer = None
        self._load_models()
    
    def _load_models(self):
        """
        Load all trained models from disk
        """
        try:
            # Load individual models
            model_files = {
                'fake_detection': 'fake_review_model.pkl',
                'sentiment': 'sentiment_model.pkl',
                'spam_detection': 'spam_model.pkl',
                'rating_prediction': 'rating_model.pkl'
            }
            
            for model_name, filename in model_files.items():
                filepath = os.path.join(self.model_path, filename)
                if os.path.exists(filepath):
                    self.models[model_name] = joblib.load(filepath)
                    print(f"✅ Loaded {model_name} from {filepath}")
                else:
                    print(f"⚠️  Model not found: {filepath}")
            
            # Load vectorizer
            vectorizer_path = os.path.join(self.model_path, 'vectorizer.pkl')
            if os.path.exists(vectorizer_path):
                self.vectorizer = joblib.load(vectorizer_path)
                print(f"✅ Loaded vectorizer from {vectorizer_path}")
            else:
                print(f"⚠️  Vectorizer not found: {vectorizer_path}")
        
        except Exception as e:
            print(f"❌ Error loading models: {str(e)}")
    
    def predict_fake(self, text):
        """
        Predict if review is fake or genuine
        
        Args:
            text (str): Review text
            
        Returns:
            dict: Prediction and confidence
        """
        if 'fake_detection' not in self.models:
            return {'error': 'Model not loaded', 'prediction': None}
        
        try:
            # Vectorize text
            X = self.vectorizer.transform([text])
            
            # Get prediction
            model = self.models['fake_detection']
            prediction = model.predict(X)[0]
            confidence = max(model.predict_proba(X)[0])
            
            return {
                'prediction': 'Fake' if prediction == 1 else 'Genuine',
                'confidence': float(confidence),
                'class_label': int(prediction)
            }
        except Exception as e:
            return {'error': str(e), 'prediction': None}
    
    def predict_sentiment(self, text):
        """
        Predict sentiment of review
        
        Args:
            text (str): Review text
            
        Returns:
            dict: Sentiment prediction and confidence
        """
        if 'sentiment' not in self.models:
            return {'error': 'Model not loaded', 'sentiment': None}
        
        try:
            X = self.vectorizer.transform([text])
            model = self.models['sentiment']
            prediction = model.predict(X)[0]
            confidence = max(model.predict_proba(X)[0])
            
            sentiment_map = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}
            
            return {
                'sentiment': sentiment_map.get(prediction, 'Unknown'),
                'confidence': float(confidence),
                'class_label': int(prediction)
            }
        except Exception as e:
            return {'error': str(e), 'sentiment': None}
    
    def predict_spam(self, text):
        """
        Predict if review is spam
        
        Args:
            text (str): Review text
            
        Returns:
            dict: Spam prediction and confidence
        """
        if 'spam_detection' not in self.models:
            return {'error': 'Model not loaded', 'spam': None}
        
        try:
            X = self.vectorizer.transform([text])
            model = self.models['spam_detection']
            prediction = model.predict(X)[0]
            confidence = max(model.predict_proba(X)[0])
            
            return {
                'spam': 'Spam' if prediction == 1 else 'Not Spam',
                'confidence': float(confidence),
                'class_label': int(prediction)
            }
        except Exception as e:
            return {'error': str(e), 'spam': None}
    
    def predict_rating(self, text):
        """
        Predict rating (1-5 stars)
        
        Args:
            text (str): Review text
            
        Returns:
            dict: Predicted rating and confidence
        """
        if 'rating_prediction' not in self.models:
            return {'error': 'Model not loaded', 'rating': None}
        
        try:
            X = self.vectorizer.transform([text])
            model = self.models['rating_prediction']
            prediction = model.predict(X)[0]
            
            # Clamp rating to 1-5
            rating = max(1, min(5, prediction))
            
            return {
                'predicted_rating': float(rating),
                'confidence': 0.85  # For regression models
            }
        except Exception as e:
            return {'error': str(e), 'rating': None}
