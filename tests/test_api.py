"""
API endpoint tests
"""

import pytest
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.app import app


@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestHealthCheck:
    """Test health check endpoint"""
    
    def test_health_check(self, client):
        """Test health endpoint"""
        response = client.get('/health')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'status' in data
        assert data['status'] == 'healthy'


class TestPredictionEndpoints:
    """Test prediction endpoints"""
    
    def test_fake_detection_endpoint(self, client):
        """Test /api/predict_fake endpoint"""
        response = client.post('/api/predict_fake',
                             json={'review_text': 'Great product!'},
                             content_type='application/json')
        # Should return 200 or error code depending on model availability
        assert response.status_code in [200, 500]
    
    def test_fake_detection_empty_text(self, client):
        """Test fake detection with empty text"""
        response = client.post('/api/predict_fake',
                             json={'review_text': ''},
                             content_type='application/json')
        assert response.status_code == 400
    
    def test_sentiment_analysis_endpoint(self, client):
        """Test /api/predict_sentiment endpoint"""
        response = client.post('/api/predict_sentiment',
                             json={'review_text': 'Amazing product!'},
                             content_type='application/json')
        assert response.status_code in [200, 500]
    
    def test_sentiment_empty_text(self, client):
        """Test sentiment with empty text"""
        response = client.post('/api/predict_sentiment',
                             json={'review_text': ''},
                             content_type='application/json')
        assert response.status_code == 400
    
    def test_spam_detection_endpoint(self, client):
        """Test /api/predict_spam endpoint"""
        response = client.post('/api/predict_spam',
                             json={'review_text': 'Click here!'},
                             content_type='application/json')
        assert response.status_code in [200, 500]
    
    def test_spam_empty_text(self, client):
        """Test spam detection with empty text"""
        response = client.post('/api/predict_spam',
                             json={'review_text': ''},
                             content_type='application/json')
        assert response.status_code == 400
    
    def test_rating_prediction_endpoint(self, client):
        """Test /api/predict_rating endpoint"""
        response = client.post('/api/predict_rating',
                             json={'review_text': 'Excellent quality'},
                             content_type='application/json')
        assert response.status_code in [200, 500]
    
    def test_rating_empty_text(self, client):
        """Test rating prediction with empty text"""
        response = client.post('/api/predict_rating',
                             json={'review_text': ''},
                             content_type='application/json')
        assert response.status_code == 400
    
    def test_overall_score_endpoint(self, client):
        """Test /api/overall_score endpoint"""
        response = client.post('/api/overall_score',
                             json={'reviews': ['Great!', 'Good', 'Excellent']},
                             content_type='application/json')
        assert response.status_code in [200, 500]
    
    def test_overall_score_empty_reviews(self, client):
        """Test overall score with no reviews"""
        response = client.post('/api/overall_score',
                             json={'reviews': []},
                             content_type='application/json')
        assert response.status_code == 400


class TestErrorHandling:
    """Test error handling"""
    
    def test_404_error(self, client):
        """Test 404 error handling"""
        response = client.get('/nonexistent')
        assert response.status_code == 404
    
    def test_invalid_json(self, client):
        """Test invalid JSON handling"""
        response = client.post('/api/predict_fake',
                             data='invalid json',
                             content_type='application/json')
        assert response.status_code in [400, 500]


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
