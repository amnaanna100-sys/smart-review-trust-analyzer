"""
API routes for the Smart Review Analyzer
"""

from flask import request, jsonify
import json


def register_routes(app, model_manager, text_preprocessor):
    """
    Register all API routes
    
    Args:
        app: Flask application
        model_manager: ModelManager instance
        text_preprocessor: TextPreprocessor instance
    """
    
    @app.route('/api/predict_fake', methods=['POST'])
    def predict_fake():
        """Fake review detection endpoint"""
        try:
            data = request.get_json()
            review_text = data.get('review_text', '').strip()
            
            if not review_text:
                return jsonify({'error': 'Empty review text'}), 400
            
            # Preprocess text
            processed_text = text_preprocessor.preprocess(review_text)
            
            # Get prediction
            result = model_manager.predict_fake(processed_text)
            
            return jsonify(result), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    
    @app.route('/api/predict_sentiment', methods=['POST'])
    def predict_sentiment():
        """Sentiment analysis endpoint"""
        try:
            data = request.get_json()
            review_text = data.get('review_text', '').strip()
            
            if not review_text:
                return jsonify({'error': 'Empty review text'}), 400
            
            # Preprocess text
            processed_text = text_preprocessor.preprocess(review_text)
            
            # Get prediction
            result = model_manager.predict_sentiment(processed_text)
            
            return jsonify(result), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    
    @app.route('/api/predict_spam', methods=['POST'])
    def predict_spam():
        """Spam detection endpoint"""
        try:
            data = request.get_json()
            review_text = data.get('review_text', '').strip()
            
            if not review_text:
                return jsonify({'error': 'Empty review text'}), 400
            
            # Preprocess text
            processed_text = text_preprocessor.preprocess(review_text)
            
            # Get prediction
            result = model_manager.predict_spam(processed_text)
            
            return jsonify(result), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    
    @app.route('/api/predict_rating', methods=['POST'])
    def predict_rating():
        """Rating prediction endpoint"""
        try:
            data = request.get_json()
            review_text = data.get('review_text', '').strip()
            
            if not review_text:
                return jsonify({'error': 'Empty review text'}), 400
            
            # Preprocess text
            processed_text = text_preprocessor.preprocess(review_text)
            
            # Get prediction
            result = model_manager.predict_rating(processed_text)
            
            return jsonify(result), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    
    @app.route('/api/overall_score', methods=['POST'])
    def overall_score():
        """Calculate overall product trust score"""
        try:
            data = request.get_json()
            reviews = data.get('reviews', [])
            
            if not reviews or len(reviews) == 0:
                return jsonify({'error': 'No reviews provided'}), 400
            
            # Analyze all reviews
            fake_count = 0
            spam_count = 0
            sentiments = []
            ratings = []
            
            for review in reviews:
                if not isinstance(review, str):
                    continue
                
                processed = text_preprocessor.preprocess(review)
                
                # Get predictions
                fake_pred = model_manager.predict_fake(processed)
                spam_pred = model_manager.predict_spam(processed)
                sentiment_pred = model_manager.predict_sentiment(processed)
                rating_pred = model_manager.predict_rating(processed)
                
                # Count
                if fake_pred.get('prediction') == 'Fake':
                    fake_count += 1
                if spam_pred.get('spam') == 'Spam':
                    spam_count += 1
                
                # Collect sentiments and ratings
                sentiment = sentiment_pred.get('sentiment')
                if sentiment:
                    sentiments.append(sentiment)
                
                rating = rating_pred.get('predicted_rating')
                if rating:
                    ratings.append(rating)
            
            # Calculate percentages
            total = len(reviews)
            fake_percentage = (fake_count / total) * 100 if total > 0 else 0
            spam_percentage = (spam_count / total) * 100 if total > 0 else 0
            genuine_percentage = 100 - fake_percentage
            
            # Calculate average sentiment
            positive_count = sentiments.count('Positive')
            avg_sentiment_score = (positive_count / len(sentiments)) if sentiments else 0
            
            # Calculate average rating
            avg_rating = sum(ratings) / len(ratings) if ratings else 0
            
            # Calculate trust score
            trust_score = (
                (genuine_percentage / 100) * 40 +
                avg_sentiment_score * 30 +
                ((100 - spam_percentage) / 100) * 20 +
                (avg_rating / 5) * 10
            )
            
            return jsonify({
                'trust_score': round(trust_score, 2),
                'fake_percentage': round(fake_percentage, 2),
                'spam_percentage': round(spam_percentage, 2),
                'genuine_percentage': round(genuine_percentage, 2),
                'avg_sentiment': 'Positive' if avg_sentiment_score > 0.5 else 'Negative' if avg_sentiment_score < 0.33 else 'Neutral',
                'avg_rating': round(avg_rating, 2),
                'total_reviews': total
            }), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500
