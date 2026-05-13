# Smart Product Review Trust Analyzer - Setup Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)
- Git

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/amnaanna100-sys/smart-review-trust-analyzer.git
cd smart-review-trust-analyzer
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download NLTK Data

```bash
python -m nltk.downloader punkt stopwords wordnet
```

### 5. Train/Download Models

#### Option A: Use Pre-trained Models

```bash
# Download pre-trained models and place in:
# ml_models/trained_models/
```

#### Option B: Train Models in Google Colab

1. Open Google Colab: https://colab.research.google.com/
2. Upload notebooks from `ml_models/notebooks/`
3. Follow instructions in notebooks to train models
4. Download trained `.pkl` files
5. Place models in `backend/models/trained_models/`

### 6. Configure Environment

Create `.env` file in project root:

```bash
DEBUG=True
ENVIRONMENT=development
HOST=0.0.0.0
PORT=5000
SECRET_KEY=your-secret-key-here
MODEL_PATH=./backend/models/trained_models/
```

### 7. Run the Application

```bash
cd backend
python app.py
```

Application will be available at: `http://localhost:5000`

## Docker Setup (Optional)

### Build Docker Image

```bash
docker build -t smart-review-analyzer .
```

### Run with Docker

```bash
docker run -p 5000:5000 smart-review-analyzer
```

### Using Docker Compose

```bash
docker-compose up -d
```

## Troubleshooting

### Issue: Models not loading

**Solution**: Ensure `.pkl` files are in `backend/models/trained_models/`

### Issue: NLTK data not found

**Solution**: Run `python -m nltk.downloader punkt stopwords wordnet`

### Issue: Port 5000 already in use

**Solution**: Change port in `config.py` or `.env` file

### Issue: ImportError for dependencies

**Solution**: Reinstall requirements: `pip install -r requirements.txt --force-reinstall`

## Testing

### Run Unit Tests

```bash
pytest tests/ -v
```

### Run API Tests

```bash
pytest tests/test_api.py -v
```

### Test Single Endpoint

```bash
curl -X POST http://localhost:5000/api/predict_fake \
  -H "Content-Type: application/json" \
  -d '{"review_text": "Great product!"}'
```

## Production Deployment

### Using Gunicorn

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 backend.app:app
```

### Using Render.com

1. Push code to GitHub
2. Connect GitHub repository to Render
3. Set start command: `gunicorn backend.app:app`
4. Set environment variables in Render dashboard
5. Deploy

### Using Railway.app

1. Create account on Railway
2. Connect GitHub repository
3. Set start command in `Procfile`: `python backend/app.py`
4. Configure environment variables
5. Deploy

## Next Steps

1. Train ML models using Colab notebooks
2. Place trained models in correct directory
3. Test API endpoints
4. Deploy to production
5. Set up monitoring and logging

For more details, see:
- `API_DOCUMENTATION.md` - API reference
- `MODEL_DETAILS.md` - Model specifications
