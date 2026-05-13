# 🔍 Smart Product Review Trust Analyzer
## Fake Review Detection System using Machine Learning

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)](https://flask.palletsprojects.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0%2B-orange)](https://scikit-learn.org/)

---

## 📖 Project Overview

Online shopping platforms (Amazon, Daraz, eBay) face challenges with:
- 🚫 **Fake Reviews**: Paid or manipulated reviews
- 📢 **Spam Reviews**: Promotional or irrelevant content
- 😕 **Biased Reviews**: Misleading sentiment or ratings

**Solution**: A full-stack ML system that analyzes product reviews and computes a **Product Trust Score** to help customers make informed purchasing decisions.

---

## 🎯 Key Features

✅ **Fake Review Detection** - SVM, Logistic Regression, Random Forest  
✅ **Sentiment Analysis** - Positive/Negative/Neutral classification  
✅ **Spam Detection** - Identifies promotional/spam reviews  
✅ **Rating Prediction** - Predicts 1-5 star ratings  
✅ **Trust Score** - Aggregated product trustworthiness (0-100)  
✅ **Batch Processing** - Upload CSV files for analysis  
✅ **RESTful API** - Easy integration with external systems  

---

## 🏗 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     FRONTEND (HTML/CSS/JS)                  │
│              Text Input / CSV File Upload                   │
└─────────────────────────────────────────────────────────────┘
                           ⬇
┌─────────────────────────────────────────────────────────────┐
│                  BACKEND (Flask API)                        │
│  /predict_fake | /predict_sentiment | /predict_spam        │
│  /predict_rating | /overall_score                           │
└─────────────────────────────────────────────────────────────┘
                           ⬇
┌─────────────────────────────────────────────────────────────┐
│                    ML LAYER (Scikit-learn)                  │
│  Fake Detection │ Sentiment │ Spam │ Rating Prediction      │
└─────────────────────────────────────────────────────────────┘
                           ⬇
┌─────────────────────────────────────────────────────────────┐
│                  OUTPUT LAYER                               │
│  Trust Score | Confidence | Visualizations                  │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 Machine Learning Models

### 1️⃣ Fake Review Detection Model
- **Input**: Review text
- **Output**: Fake / Genuine
- **Algorithms**: SVM (primary), Logistic Regression, Random Forest

### 2️⃣ Sentiment Analysis Model
- **Input**: Review text
- **Output**: Positive / Negative / Neutral
- **Algorithms**: Naive Bayes, Logistic Regression

### 3️⃣ Spam Detection Model
- **Input**: Review text
- **Output**: Spam / Not Spam
- **Algorithms**: Random Forest, SVM

### 4️⃣ Rating Prediction Model
- **Input**: Review text
- **Output**: Rating (1-5 stars)
- **Algorithms**: Linear Regression, Random Forest Regressor

---

## 📁 Project Structure

```
smart-review-trust-analyzer/
├── ml_models/
│   ├── notebooks/              # Google Colab notebooks
│   │   ├── fake_review_model.ipynb
│   │   ├── sentiment_model.ipynb
│   │   ├── spam_model.ipynb
│   │   └── rating_model.ipynb
│   └── trained_models/         # Saved .pkl files
│       ├── fake_review_model.pkl
│       ├── sentiment_model.pkl
│       ├── spam_model.pkl
│       ├── rating_model.pkl
│       └── vectorizer.pkl
│
├── backend/
│   ├── app.py                  # Main Flask application
│   ├── config.py               # Configuration settings
│   ├── models.py               # Model loading & inference
│   ├── preprocessing.py        # Text preprocessing
│   ├── api_routes.py           # API endpoints
│   └── requirements.txt         # Python dependencies
│
├── frontend/
│   ├── index.html              # Main page
│   ├── css/
│   │   └── style.css           # Styling
│   ├── js/
│   │   └── script.js           # JavaScript logic
│   └── assets/                 # Images, icons
│
├── data/
│   ├── training_data.csv       # Training dataset
│   ├── test_data.csv           # Test dataset
│   └── sample_reviews.csv      # Sample reviews for demo
│
├── preprocessing/
│   ├── data_cleaner.py         # Text cleaning utilities
│   └── feature_extractor.py    # TF-IDF vectorization
│
├── tests/
│   ├── test_models.py          # Model testing
│   └── test_api.py             # API endpoint testing
│
├── docs/
│   ├── SETUP.md                # Setup instructions
│   ├── API_DOCUMENTATION.md    # API reference
│   └── MODEL_DETAILS.md        # Model specifications
│
├── .gitignore                  # Exclude large files
├── requirements.txt            # Project dependencies
└── README.md                   # This file
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/amnaanna100-sys/smart-review-trust-analyzer.git
   cd smart-review-trust-analyzer
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download trained models**
   - Place `.pkl` files in `backend/models/trained_models/`

5. **Run the application**
   ```bash
   cd backend
   python app.py
   ```

6. **Access the application**
   - Open browser: `http://localhost:5000`

---

## 🔌 API Endpoints

### 1. Predict Fake Review
```
POST /api/predict_fake
Body: {"review_text": "Great product!"}
Response: {"prediction": "Genuine", "confidence": 0.92}
```

### 2. Sentiment Analysis
```
POST /api/predict_sentiment
Body: {"review_text": "Great product!"}
Response: {"sentiment": "Positive", "confidence": 0.89}
```

### 3. Spam Detection
```
POST /api/predict_spam
Body: {"review_text": "Buy now! Limited offer!"}
Response: {"spam": "Spam", "confidence": 0.95}
```

### 4. Rating Prediction
```
POST /api/predict_rating
Body: {"review_text": "Excellent quality"}
Response: {"predicted_rating": 4.8, "confidence": 0.87}
```

### 5. Overall Trust Score
```
POST /api/overall_score
Body: {"reviews": ["Great!", "Awesome", "Best product"]}
Response: {
  "trust_score": 85,
  "fake_percentage": 5,
  "spam_percentage": 2,
  "avg_sentiment": "Positive",
  "avg_rating": 4.5
}
```

---

## 🧠 Data Preprocessing Pipeline

1. **Text Cleaning**
   - Remove URLs and email addresses
   - Remove special characters and punctuation
   - Convert to lowercase
   - Remove extra whitespace

2. **Tokenization**
   - Split text into tokens

3. **Stopword Removal**
   - Remove common English stopwords

4. **Lemmatization/Stemming**
   - Normalize word forms

5. **Vectorization**
   - TF-IDF or Word embeddings

---

## 📊 Trust Score Calculation

```
Trust Score Formula:

Trust_Score = (Genuine_Ratio × 40) + (Sentiment_Score × 30) + 
              ((1 - Spam_Ratio) × 20) + (Rating_Consistency × 10)

Where:
- Genuine_Ratio: % of genuine reviews (0-1)
- Sentiment_Score: Average positive sentiment (0-1)
- Spam_Ratio: % of spam reviews (0-1)
- Rating_Consistency: Consistency of ratings (0-1)
```

---

## 📈 Project Phases

| Phase | Task | Status |
|-------|------|--------|
| 1 | ML Model Development | 🔲 Todo |
| 2 | Backend API Development | 🔲 Todo |
| 3 | Frontend UI Development | 🔲 Todo |
| 4 | Data Preparation | 🔲 Todo |
| 5 | Integration & Testing | 🔲 Todo |
| 6 | Deployment | 🔲 Todo |

---

## 💻 Technology Stack

### Frontend
- HTML5
- CSS3 (Bootstrap 5)
- JavaScript (Vanilla or React optional)

### Backend
- Flask 2.0+
- Python 3.8+

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- NLTK / spaCy
- TF-IDF Vectorizer

### Training
- Google Colab
- Joblib / Pickle (model serialization)

### Deployment (Optional)
- Render or Railway
- Docker (optional)

---

## 📚 References & Resources

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [NLTK Documentation](https://www.nltk.org/)
- [Google Colab Guide](https://colab.research.google.com/)

---

## 👥 Team Members

- **Developer**: amnaanna100-sys

---

## 📝 License

This project is open-source and available under the MIT License.

---

## 📧 Contact & Support

For issues, questions, or contributions, please open a GitHub issue or reach out directly.

---

**Last Updated**: 2026-05-13
