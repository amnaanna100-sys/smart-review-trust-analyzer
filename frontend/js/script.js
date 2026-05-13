/**
 * Smart Review Analyzer - Frontend JavaScript
 */

const API_BASE_URL = 'http://localhost:5000/api';

// DOM Elements
const singleReviewForm = document.getElementById('singleReviewForm');
const reviewText = document.getElementById('reviewText');
const resultsContainer = document.getElementById('resultsContainer');
const noResultsMessage = document.getElementById('noResultsMessage');
const loadingSpinner = document.getElementById('loadingSpinner');
const trustScoreDashboard = document.getElementById('trustScoreDashboard');

// Event Listeners
singleReviewForm.addEventListener('submit', handleSingleReview);

/**
 * Handle single review submission
 */
async function handleSingleReview(e) {
    e.preventDefault();
    
    const text = reviewText.value.trim();
    if (!text) {
        alert('Please enter a review!');
        return;
    }
    
    showLoading(true);
    
    try {
        // Get all predictions
        const [fakeRes, sentimentRes, spamRes, ratingRes] = await Promise.all([
            fetch(`${API_BASE_URL}/predict_fake`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ review_text: text })
            }).then(r => r.json()),
            
            fetch(`${API_BASE_URL}/predict_sentiment`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ review_text: text })
            }).then(r => r.json()),
            
            fetch(`${API_BASE_URL}/predict_spam`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ review_text: text })
            }).then(r => r.json()),
            
            fetch(`${API_BASE_URL}/predict_rating`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ review_text: text })
            }).then(r => r.json())
        ]);
        
        // Display results
        displayResults(fakeRes, sentimentRes, spamRes, ratingRes);
        
    } catch (error) {
        console.error('Error:', error);
        alert('Error analyzing review. Please try again.');
    } finally {
        showLoading(false);
    }
}

/**
 * Display prediction results
 */
function displayResults(fakeRes, sentimentRes, spamRes, ratingRes) {
    // Hide no results message
    noResultsMessage.style.display = 'none';
    resultsContainer.style.display = 'block';
    
    // Fake Detection
    if (fakeRes.prediction) {
        const fakeResult = document.getElementById('fakeResult');
        const fakeConfidence = document.getElementById('fakeConfidence');
        const fakeConfidenceText = document.getElementById('fakeConfidenceText');
        
        const confidence = (fakeRes.confidence * 100).toFixed(2);
        fakeResult.textContent = fakeRes.prediction;
        fakeResult.className = fakeRes.prediction === 'Genuine' ? 'text-success' : 'text-danger';
        fakeConfidence.style.width = confidence + '%';
        fakeConfidence.className = fakeRes.prediction === 'Genuine' ? 'progress-bar bg-success' : 'progress-bar bg-danger';
        fakeConfidenceText.textContent = `Confidence: ${confidence}%`;
    }
    
    // Sentiment
    if (sentimentRes.sentiment) {
        const sentimentResult = document.getElementById('sentimentResult');
        const sentimentConfidence = document.getElementById('sentimentConfidence');
        const sentimentConfidenceText = document.getElementById('sentimentConfidenceText');
        
        const confidence = (sentimentRes.confidence * 100).toFixed(2);
        sentimentResult.textContent = sentimentRes.sentiment;
        
        let sentimentClass = 'text-info';
        if (sentimentRes.sentiment === 'Positive') sentimentClass = 'text-success';
        if (sentimentRes.sentiment === 'Negative') sentimentClass = 'text-danger';
        sentimentResult.className = sentimentClass;
        
        sentimentConfidence.style.width = confidence + '%';
        sentimentConfidenceText.textContent = `Confidence: ${confidence}%`;
    }
    
    // Spam
    if (spamRes.spam) {
        const spamResult = document.getElementById('spamResult');
        const spamConfidence = document.getElementById('spamConfidence');
        const spamConfidenceText = document.getElementById('spamConfidenceText');
        
        const confidence = (spamRes.confidence * 100).toFixed(2);
        spamResult.textContent = spamRes.spam;
        spamResult.className = spamRes.spam === 'Spam' ? 'text-danger' : 'text-success';
        spamConfidence.style.width = confidence + '%';
        spamConfidenceText.textContent = `Confidence: ${confidence}%`;
    }
    
    // Rating
    if (ratingRes.predicted_rating) {
        const ratingResult = document.getElementById('ratingResult');
        const starRating = document.getElementById('starRating');
        
        const rating = parseFloat(ratingRes.predicted_rating).toFixed(1);
        ratingResult.textContent = `${rating} / 5.0`;
        
        // Generate stars
        const fullStars = Math.floor(rating);
        const hasHalfStar = rating % 1 >= 0.5;
        let stars = '⭐'.repeat(fullStars);
        if (hasHalfStar) stars += '✨';
        starRating.textContent = stars;
    }
}

/**
 * Show/hide loading spinner
 */
function showLoading(show) {
    loadingSpinner.style.display = show ? 'flex' : 'none';
}

/**
 * Format number as percentage
 */
function toPercentage(value) {
    return (value * 100).toFixed(2) + '%';
}
