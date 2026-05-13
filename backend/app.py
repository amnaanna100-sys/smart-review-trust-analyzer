"""
Smart Product Review Trust Analyzer - Main Flask Application
Author: Smart Review Team
Date: 2026-05-13
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
import sys
from dotenv import load_dotenv

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import Config
from models import ModelManager
from preprocessing import TextPreprocessor
from api_routes import register_routes

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS for API requests
CORS(app)

# Initialize components
model_manager = ModelManager()
text_preprocessor = TextPreprocessor()

# Register API routes
register_routes(app, model_manager, text_preprocessor)


@app.route('/')
def index():
    """Serve the main frontend page"""
    return render_template('index.html')


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Smart Review Trust Analyzer',
        'version': '1.0.0'
    }), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Endpoint not found',
        'status': 404
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error',
        'status': 500
    }), 500


if __name__ == '__main__':
    print("\n" + "="*60)
    print("🔍 Smart Product Review Trust Analyzer")
    print("="*60)
    print("Starting Flask application...")
    print(f"Debug Mode: {app.config['DEBUG']}")
    print(f"Environment: {app.config['ENVIRONMENT']}")
    print(f"Port: {app.config['PORT']}")
    print("="*60)
    print("\n✅ Application running at: http://localhost:5000")
    print("🔌 Health check: http://localhost:5000/health\n")
    
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
