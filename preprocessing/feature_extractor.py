"""
Feature extraction and vectorization utilities
"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from typing import List, Tuple


class FeatureExtractor:
    """Feature extraction for text data"""
    
    def __init__(self, vectorizer_type: str = 'tfidf', max_features: int = 5000):
        """
        Initialize feature extractor
        
        Args:
            vectorizer_type: 'tfidf' or 'count'
            max_features: Maximum number of features
        """
        self.max_features = max_features
        self.vectorizer_type = vectorizer_type
        
        if vectorizer_type == 'tfidf':
            self.vectorizer = TfidfVectorizer(
                max_features=max_features,
                min_df=2,
                max_df=0.95,
                ngram_range=(1, 2),
                stop_words='english'
            )
        else:
            self.vectorizer = CountVectorizer(
                max_features=max_features,
                min_df=2,
                max_df=0.95,
                ngram_range=(1, 2),
                stop_words='english'
            )
    
    def fit(self, texts: List[str]):
        """
        Fit vectorizer on texts
        
        Args:
            texts: List of text documents
        """
        self.vectorizer.fit(texts)
        return self
    
    def transform(self, texts: List[str]):
        """
        Transform texts to feature vectors
        
        Args:
            texts: List of text documents
            
        Returns:
            Sparse matrix of features
        """
        return self.vectorizer.transform(texts)
    
    def fit_transform(self, texts: List[str]):
        """
        Fit and transform in one step
        
        Args:
            texts: List of text documents
            
        Returns:
            Sparse matrix of features
        """
        return self.vectorizer.fit_transform(texts)
    
    def get_feature_names(self) -> List[str]:
        """
        Get feature names
        
        Returns:
            List of feature names
        """
        return self.vectorizer.get_feature_names_out().tolist()
    
    def get_top_features(self, text: str, n: int = 10) -> List[Tuple[str, float]]:
        """
        Get top features for a text
        
        Args:
            text: Input text
            n: Number of top features
            
        Returns:
            List of (feature_name, score) tuples
        """
        X = self.vectorizer.transform([text])
        feature_names = self.get_feature_names()
        
        # Get indices and values
        indices = X.nonzero()[1]
        values = X.data
        
        # Sort by values (descending)
        sorted_indices = np.argsort(values)[::-1][:n]
        
        # Get top features
        top_features = [(feature_names[indices[i]], values[i]) 
                       for i in sorted_indices]
        
        return top_features
    
    def get_vocabulary_size(self) -> int:
        """
        Get vocabulary size
        
        Returns:
            Number of unique features
        """
        return len(self.vectorizer.get_feature_names_out())
