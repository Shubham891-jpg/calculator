# 🧪 IT Ticket Severity Calculator - Testing Guide

## 📋 Quick Start for Testers

### Prerequisites
- Server must be running on `http://localhost:8000`
- Check server status: Visit http://localhost:8000/health

### Testing Options

| Method | File | Description |
|--------|------|-------------|
| **Web Interface** | http://localhost:8000 | User-friendly web testing |
| **Interactive API** | http://localhost:8000/docs | Swagger UI for API testing |
| **Python Script** | `test_api_endpoints.py` | Automated comprehensive testing |
| **cURL Script (Linux/Mac)** | `test_api_curl.sh` | Command-line testing |
| **cURL Script (Windows)** | `test_api_curl.bat` | Windows command-line testing |
| **Postman Collection** | `IT_Ticket_Severity_API.postman_collection.json` | Import into Postman |

---

## 🚀 Quick Test Commands

### 1. Health Check
```bash
curl http://localhost:8000/health
```
**Expected**: `{"status": "healthy", ...}`

### 2. Simple Prediction
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"ticket_text": "Server is down"}'
```
**Expected**: `{"severity_score": 48.5, "severity_category": "Medium", ...}`

### 3. Batch Prediction
```bash
curl -X POST "http://localhost:8000/predict/batch" \
     -H "Content-Type: application/json" \
     -d '{"tickets": ["Server down", "Printer issue"]}'
```

---

## 📊 Test Scenarios

### High Severity (Expected: 90-100)
```json
{"ticket_text": "All servers are down, complete system failure, no one can work"}
{"ticket_text": "Database corrupted, all data at risk, immediate action required"}
{"ticket_text": "Security breach detected, unauthorized access to sensitive data"}
```

### Medium Severity (Expected: 80-89)
```json
{"ticket_text": "Database is extremely slow, all applications timing out"}
{"ticket_text": "Office printer is not working, affecting multiple users"}
{"ticket_text": "Application crashes when trying to save documents"}
```

### Low Severity (Expected: 10-79)
```json
{"ticket_text": "User needs password reset for their account"}
{"ticket_text": "Please install Microsoft Office on my computer"}
{"ticket_text": "Minor display issue on one monitor"}
{"ticket_text": "How do I change my desktop wallpaper?"}
```

### Hindi Language Tests
```json
{"ticket_text": "सर्वर पूरी तरह से बंद है और कोई भी काम नहीं कर सकता"}
{"ticket_text": "डेटाबेस बहुत धीमा है"}
{"ticket_text": "प्रिंटर काम नहीं कर रहा है"}
```

---

## 🔧 Automated Testing

### Run Python Test Suite
```bash
cd it-ticket-severity-calculator
python test_api_endpoints.py
```

**Expected Output:**
```
🧪 Testing IT Ticket Severity Prediction
==================================================
✅ PASS Health Check
✅ PASS Critical Severity (English)
✅ PASS High Severity (English)
...
📊 Results: 15/15 tests passed
🎉 All tests passed! API is working correctly.
```

### Run cURL Test Script
```bash
# Linux/Mac
chmod +x test_api_curl.sh
./test_api_curl.sh

# Windows
test_api_curl.bat
```

---

## 📱 Interactive Testing

### Swagger UI (Recommended)
1. Open http://localhost:8000/docs
2. Click on any endpoint (e.g., `/predict`)
3. Click "Try it out"
4. Enter test data
5. Click "Execute"
6. View response

### Web Interface
1. Open http://localhost:8000
2. Enter ticket description in text area
3. Click "Analyze Severity"
4. View results with score and category

### Postman
1. Import `IT_Ticket_Severity_API.postman_collection.json`
2. Run individual requests or entire collection
3. Modify request bodies to test different scenarios

---

## ✅ Testing Checklist

### Basic Functionality
- [ ] Health check returns "healthy"
- [ ] Single prediction works with English text
- [ ] Single prediction works with Hindi text
- [ ] Batch prediction processes multiple tickets
- [ ] Model info endpoint returns details
- [ ] API info endpoint works

### Severity Categories
- [ ] High severity tickets score 90-100
- [ ] Medium severity tickets score 80-89
- [ ] Low severity tickets score 10-79

### Language Support
- [ ] English text detected as "en"
- [ ] Hindi text detected as "hi"
- [ ] Mixed language text handled gracefully
- [ ] Special characters don't break processing

### Edge Cases
- [ ] Empty text returns appropriate error
- [ ] Very long text (>5000 chars) handled
- [ ] Special characters processed correctly
- [ ] Numbers-only text works
- [ ] Batch with 100 tickets works
- [ ] Invalid JSON returns proper error

### Performance
- [ ] First request completes within 30 seconds
- [ ] Subsequent requests complete within 2 seconds
- [ ] Concurrent requests handled properly
- [ ] Memory usage remains stable

### Error Handling
- [ ] Invalid endpoints return 404
- [ ] Malformed JSON returns 400
- [ ] Server errors return 500 with details
- [ ] Timeout handling works properly

---

## 🐛 Common Issues & Solutions

### Server Not Responding
```bash
# Check if server is running
curl http://localhost:8000/health

# If not running, start server
python run_server.py
```

### Model Loading Errors
- Ensure model files exist in `models/` directory
- Check server logs for detailed error messages
- Verify all dependencies are installed

### Slow First Request
- First prediction may take 10-30 seconds (model loading)
- Subsequent requests should be much faster
- This is normal behavior

### JSON Format Errors
- Ensure proper JSON formatting
- Use double quotes for strings
- Escape special characters properly

---

## 📈 Performance Benchmarks

### Expected Response Times
- **Health Check**: < 100ms
- **First Prediction**: 5-30 seconds (model loading)
- **Subsequent Predictions**: 100-500ms
- **Batch Predictions**: 200ms per ticket

### Expected Accuracy
- **English Tickets**: High accuracy for common IT issues
- **Hindi Tickets**: Good accuracy with language detection
- **Mixed Content**: Reasonable handling of mixed languages

---

## 📞 Reporting Issues

When reporting issues, please include:

1. **Request Details**: Exact cURL command or request body
2. **Response**: Full response including status code
3. **Server Logs**: Any error messages from server console
4. **Environment**: OS, Python version, browser (if using web interface)
5. **Steps to Reproduce**: Exact steps that led to the issue

### Example Issue Report
```
Issue: Prediction returns wrong severity category

Request:
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"ticket_text": "Server completely down"}'

Response:
{"severity_score": 25.0, "severity_category": "Low", ...}

Expected: High or Critical severity (60-100 range)
Actual: Low severity (25.0)

Environment: Windows 10, Python 3.12, Chrome browser
```

---

## 🎯 Success Criteria

The API is working correctly if:

✅ All health checks pass  
✅ Predictions return scores between 10-100  
✅ Categories match score ranges  
✅ Both English and Hindi work  
✅ Response times are reasonable  
✅ Error handling works properly  
✅ Web interface loads and functions  

---

**Happy Testing! 🚀**