# 🚀 IT Ticket Severity Calculator - REST API Documentation

## Base URL
```
http://localhost:8000
```

## Overview
The IT Ticket Severity Calculator API provides AI-powered severity assessment for IT support tickets. It supports both English and Hindi languages and returns severity scores from 10-100 with corresponding categories.

---

## 📋 API Endpoints

### 1. Health Check
**GET** `/health`

Check if the API service is running and healthy.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-02-05T18:59:02.311723",
  "model_info": {
    "model_type": "RandomForestRegressor",
    "embedding_model": "paraphrase-multilingual-MiniLM-L12-v2",
    "embedding_dim": 384,
    "n_estimators": 100,
    "max_depth": 10
  }
}
```

**cURL Example:**
```bash
curl -X GET "http://localhost:8000/health"
```

---

### 2. Single Ticket Prediction
**POST** `/predict`

Predict severity score for a single IT ticket.

**Request Body:**
```json
{
  "ticket_text": "Server is down and users cannot access email"
}
```

**Response:**
```json
{
  "severity_score": 54.58,
  "severity_category": "Medium",
  "confidence": 0.85,
  "detected_language": "en",
  "processed_text": "server down users access email",
  "timestamp": "2026-02-05T18:59:30.484205"
}
```

**cURL Example:**
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"ticket_text": "Server is down and users cannot access email"}'
```

**PowerShell Example:**
```powershell
$body = '{"ticket_text": "Database server crashed and all applications are offline"}'
Invoke-RestMethod -Uri "http://localhost:8000/predict" -Method POST -ContentType "application/json" -Body $body
```

---

### 3. Batch Predictions
**POST** `/predict/batch`

Predict severity scores for multiple tickets at once (max 100 tickets).

**Request Body:**
```json
{
  "tickets": [
    "Server is completely down",
    "Printer not working in office",
    "Need password reset for user account",
    "सर्वर डाउन है"
  ]
}
```

**Response:**
```json
{
  "predictions": [
    {
      "severity_score": 78.5,
      "severity_category": "High",
      "confidence": 0.92,
      "detected_language": "en",
      "processed_text": "server completely down",
      "timestamp": "2026-02-05T19:00:15.123456"
    },
    {
      "severity_score": 45.2,
      "severity_category": "Medium",
      "confidence": 0.78,
      "detected_language": "en",
      "processed_text": "printer working office",
      "timestamp": "2026-02-05T19:00:15.234567"
    }
  ],
  "total_tickets": 4,
  "processing_time_seconds": 1.23
}
```

**cURL Example:**
```bash
curl -X POST "http://localhost:8000/predict/batch" \
     -H "Content-Type: application/json" \
     -d '{"tickets": ["Server down", "Printer issue", "Password reset needed"]}'
```

---

### 4. Model Information
**GET** `/model/info`

Get detailed information about the loaded AI model.

**Response:**
```json
{
  "model_info": {
    "model_type": "RandomForestRegressor",
    "scaler_info": {
      "is_fitted": true,
      "min_score": 10,
      "max_score": 100,
      "original_min": 35.07,
      "original_max": 80.81,
      "score_range": 90
    },
    "embedding_model": "paraphrase-multilingual-MiniLM-L12-v2",
    "embedding_dim": 384,
    "model_dir": "models",
    "n_estimators": 100,
    "max_depth": 10
  },
  "timestamp": "2026-02-05T19:01:00.000000"
}
```

**cURL Example:**
```bash
curl -X GET "http://localhost:8000/model/info"
```

---

### 5. API Information
**GET** `/api`

Get general API information and available endpoints.

**Response:**
```json
{
  "message": "IT Ticket Severity Score Calculator API",
  "version": "1.0.0",
  "description": "Bilingual (English/Hindi) ML service for predicting IT ticket severity scores",
  "endpoints": {
    "predict": "/predict - Predict severity for a single ticket",
    "predict_batch": "/predict/batch - Predict severity for multiple tickets",
    "health": "/health - Health check",
    "docs": "/docs - API documentation"
  }
}
```

---

## 📊 Severity Score Ranges

| Score Range | Category | Description | Examples |
|-------------|----------|-------------|----------|
| **90-100** | **High** | Critical system issues, major outages | "Server completely down", "Database corrupted" |
| **80-89** | **Medium** | Moderate functionality affected | "Printer not working", "App crashes occasionally" |
| **10-79** | **Low** | Minor issues, individual users | "Password reset", "Display glitch", "Software installation" |

---

## 🌐 Language Support

The API automatically detects and processes text in:
- **English** (`en`)
- **Hindi** (`hi`)

Other languages default to English processing.

---

## 🧪 Test Examples

### High Severity Examples (90-100):
```bash
# English - Server outage
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"ticket_text": "All servers are down, complete system failure, no one can work"}'

# Hindi - Server down
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"ticket_text": "सर्वर पूरी तरह से बंद है और कोई भी काम नहीं कर सकता"}'
```

### Medium Severity Examples (80-89):
```bash
# Performance issue
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"ticket_text": "Database is extremely slow, all applications timing out"}'

# Hardware issue
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"ticket_text": "Office printer is not working, affecting multiple users"}'
```

### Low Severity Examples (10-79):
```bash
# User account issue
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"ticket_text": "User needs password reset for their account"}'

# Software request
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"ticket_text": "Please install Microsoft Office on my computer"}'
```

---

## 📱 Interactive API Documentation

Visit these URLs in your browser for interactive API testing:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

These interfaces allow you to:
- Test all endpoints directly in the browser
- See detailed request/response schemas
- Try different examples interactively

---

## ⚡ Performance Notes

- **First Request**: May take 5-10 seconds (model loading)
- **Subsequent Requests**: ~100-500ms per prediction
- **Batch Processing**: More efficient for multiple tickets
- **Concurrent Requests**: Supported (FastAPI handles async requests)

---

## 🔧 Error Handling

### Common Error Responses:

**400 Bad Request** - Invalid input:
```json
{
  "detail": "Ticket text cannot be empty"
}
```

**503 Service Unavailable** - Model not loaded:
```json
{
  "detail": "Model not initialized"
}
```

**500 Internal Server Error** - Processing error:
```json
{
  "detail": "Prediction failed: [error details]"
}
```

---

## 🧪 Testing Checklist

### Basic Functionality:
- [ ] Health check returns "healthy" status
- [ ] Single prediction works with English text
- [ ] Single prediction works with Hindi text
- [ ] Batch prediction works with multiple tickets
- [ ] Model info endpoint returns details

### Edge Cases:
- [ ] Empty text handling
- [ ] Very long text (>5000 characters)
- [ ] Special characters and symbols
- [ ] Mixed language text
- [ ] Batch with 100 tickets (maximum)

### Performance:
- [ ] Response time under 1 second (after first request)
- [ ] Concurrent requests handling
- [ ] Memory usage stability

---

## 📞 Support

If you encounter any issues during testing:

1. **Check Server Status**: Visit http://localhost:8000/health
2. **View Logs**: Check the server console output
3. **Verify Input**: Ensure JSON format is correct
4. **Test Examples**: Try the provided cURL examples first

---

## 🎯 Quick Test Script

Save this as `test_api.sh` (Linux/Mac) or `test_api.bat` (Windows):

```bash
#!/bin/bash
echo "Testing IT Ticket Severity Calculator API..."

echo "1. Health Check:"
curl -s http://localhost:8000/health | jq .

echo -e "\n2. Single Prediction:"
curl -s -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"ticket_text": "Server is down"}' | jq .

echo -e "\n3. Batch Prediction:"
curl -s -X POST "http://localhost:8000/predict/batch" \
     -H "Content-Type: application/json" \
     -d '{"tickets": ["Server down", "Printer issue"]}' | jq .

echo -e "\nAPI Testing Complete!"
```

**Run with:** `chmod +x test_api.sh && ./test_api.sh`

---

**🚀 Happy Testing!**