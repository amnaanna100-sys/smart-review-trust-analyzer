"""
Configuration settings for Flask application
"""

import os
from datetime import timedelta


class Config:
    """Base configuration"""
    
    # Flask Settings
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 5000))
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # CORS Settings
    CORS_HEADERS = 'Content-Type'
    
    # Model Settings
    MODEL_PATH = os.getenv('MODEL_PATH', './models/trained_models/')
    MAX_REVIEW_LENGTH = 512  # Maximum characters in a review
    
    # Upload Settings
    MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS = {'csv', 'txt'}
    UPLOAD_FOLDER = './uploads/'
    
    # Batch Processing
    BATCH_SIZE = 32
    
    # Model Confidence Threshold
    CONFIDENCE_THRESHOLD = 0.5
    
    # Trust Score Weights (must sum to 100)
    TRUST_SCORE_WEIGHTS = {
        'genuine_ratio': 40,        # % of genuine reviews
        'sentiment_score': 30,      # Average sentiment polarity
        'spam_ratio': 20,           # % of non-spam reviews
        'rating_consistency': 10    # Rating variance/consistency
    }
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    ENVIRONMENT = 'development'


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    ENVIRONMENT = 'production'
    SECRET_KEY = os.getenv('SECRET_KEY')
    

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    ENVIRONMENT = 'testing'
