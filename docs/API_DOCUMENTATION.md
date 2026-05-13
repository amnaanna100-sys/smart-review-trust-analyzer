# API Documentation

## Base URL

```
http://localhost:5000
```

## Endpoints

### 1. Health Check

**Endpoint**: `GET /health`

**Description**: Check if API is running

**Response**:
```json
{
  "status": "healthy",
  "service": "Smart Review Trust Analyzer",
  "version": "1.0.0"
}
```

**Status Code**: `200 OK`

---

### 2. Fake Review Detection

**Endpoint**: `POST /api/predict_fake`

**Description**: Detect if a review is fake or genuine

**Request Body**:
```json
{
  "review_text": "This is an excellent product!"
}
```

**Response**:
```json
{
  "prediction": "Genuine",
  "confidence": 0.92,
  "class_label": 0
}
```

**Status Codes**:
- `200 OK`: Successful prediction
- `400 Bad Request`: Empty review text
- `500 Internal Server Error`: Model not loaded

---

### 3. Sentiment Analysis

**Endpoint**: `POST /api/predict_sentiment`

**Description**: Classify sentiment of review (Positive, Negative, Neutral)

**Request Body**:
```json
{
  "review_text": "This product is amazing!"
}
```

**Response**:
```json
{
  "sentiment": "Positive",
  "confidence": 0.89,
  "class_label": 2
}
```

**Sentiment Values**:
- `0`: Negative
- `1`: Neutral
- `2`: Positive

---

### 4. Spam Detection

**Endpoint**: `POST /api/predict_spam`

**Description**: Identify spam or promotional reviews

**Request Body**:
```json
{
  "review_text": "BUY NOW LIMITED OFFER!!!"
}
```

**Response**:
```json
{
  "spam": "Spam",
  "confidence": 0.95,
  "class_label": 1
}
```

**Spam Values**:
- `0`: Not Spam
- `1`: Spam

---

### 5. Rating Prediction

**Endpoint**: `POST /api/predict_rating`

**Description**: Predict star rating (1-5) from review text

**Request Body**:
```json
{
  "review_text": "Excellent quality and fast shipping"
}
```

**Response**:
```json
{
  "predicted_rating": 4.8,
  "confidence": 0.87
}
```

**Rating Range**: 1.0 to 5.0

---

### 6. Overall Trust Score

**Endpoint**: `POST /api/overall_score`

**Description**: Calculate product trust score from multiple reviews

**Request Body**:
```json
{
  "reviews": [
    "Great product!",
    "Excellent quality",
    "Very satisfied"
  ]
}
```

**Response**:
```json
{
  "trust_score": 85.5,
  "fake_percentage": 5.0,
  "spam_percentage": 2.0,
  "genuine_percentage": 95.0,
  "avg_sentiment": "Positive",
  "avg_rating": 4.5,
  "total_reviews": 3
}
```

**Trust Score Formula**:
```
Trust_Score = (Genuine_Ratio × 40) + (Sentiment_Score × 30) + 
              ((1 - Spam_Ratio) × 20) + (Rating_Consistency × 10)
```

**Range**: 0-100

---

## Error Responses

### 400 Bad Request

```json
{
  "error": "Empty review text"
}
```

### 404 Not Found

```json
{
  "error": "Endpoint not found",
  "status": 404
}
```

### 500 Internal Server Error

```json
{
  "error": "Model not loaded",
  "prediction": null
}
```

---

## Request Headers

All POST requests should include:

```
Content-Type: application/json
```

---

## Example Usage

### Using cURL

```bash
# Fake detection
curl -X POST http://localhost:5000/api/predict_fake \
  -H "Content-Type: application/json" \
  -d '{"review_text": "Great product!"}'

# Sentiment analysis
curl -X POST http://localhost:5000/api/predict_sentiment \
  -H "Content-Type: application/json" \
  -d '{"review_text": "Excellent quality!"}'

# Overall score
curl -X POST http://localhost:5000/api/overall_score \
  -H "Content-Type: application/json" \
  -d '{"reviews": ["Great!", "Good", "Excellent"]}'
```

### Using Python requests

```python
import requests

api_url = 'http://localhost:5000/api'

# Predict fake
response = requests.post(
    f'{api_url}/predict_fake',
    json={'review_text': 'Amazing product!'}
)
print(response.json())

# Get sentiment
response = requests.post(
    f'{api_url}/predict_sentiment',
    json={'review_text': 'Love it!'}
)
print(response.json())
```

### Using JavaScript/Fetch

```javascript
const apiUrl = 'http://localhost:5000/api';

// Predict fake
fetch(`${apiUrl}/predict_fake`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ review_text: 'Great!' })
})
.then(res => res.json())
.then(data => console.log(data));
```

---

## Rate Limiting

Currently no rate limiting. Future versions will implement:
- 100 requests per minute per IP
- 1000 requests per hour per API key

---

## Versioning

Current Version: `1.0.0`

API endpoints follow pattern: `/api/v1/endpoint`

(Currently using `/api/endpoint` for v1.0.0)

---

## Support

For issues or questions, open a GitHub issue or contact the development team.
