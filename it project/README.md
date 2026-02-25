# IT Ticket Severity Calculator

AI-powered severity assessment for IT support tickets with multilingual support (English/Hindi).

## 🚀 Deploy to Render (100% FREE)

### Quick Deploy (3 Steps):

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Deploy to Render"
   git push
   ```

2. **Go to Render:**
   - Visit https://render.com
   - Sign up (free, no credit card required)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Deploy:**
   - Render auto-detects `render.yaml`
   - Uses Docker automatically
   - Click "Create Web Service"
   - Wait 3-5 minutes

**Done!** Your app will be live at `https://your-app.onrender.com`

---

## ✨ Features

- 🤖 AI-powered severity prediction (Random Forest)
- 🌍 Multilingual: English & Hindi
- 📊 Severity scoring: High (90-100), Medium (80-89), Low (10-79)
- 🌐 Web interface + REST API
- 🚀 Docker ready

---

## 📁 Project Structure

```
project-root/
├── Dockerfile          # Docker configuration
├── render.yaml         # Render deployment config
├── .dockerignore       # Docker ignore rules
├── README.md           # This file
└── ticket/             # Application code
    ├── api/            # FastAPI server
    ├── models/         # Trained ML models
    ├── src/            # Source code
    ├── static/         # Web interface
    ├── requirements.txt
    └── run_server.py
```

---

## 🧪 Test Locally

```bash
# Build Docker image
docker build -t it-ticket-severity .

# Run container
docker run -p 8000:8000 it-ticket-severity
```

Access at: http://localhost:8000

---

## 💰 Cost

**100% FREE** on Render:
- No credit card required
- 750 hours/month (24/7 uptime)
- Free SSL certificate
- Auto-deploy from GitHub

---

## 📊 API Endpoints

Once deployed, access:
- **Web Interface:** `https://your-app.onrender.com`
- **API Docs:** `https://your-app.onrender.com/docs`
- **Health Check:** `https://your-app.onrender.com/health`

---

## 🎯 Example Usage

### Web Interface
1. Open your app URL
2. Enter ticket description
3. Click "Analyze Severity"
4. Get instant results

### API
```bash
curl -X POST "https://your-app.onrender.com/predict" \
  -H "Content-Type: application/json" \
  -d '{"ticket_text": "Server is down"}'
```

---

## 🔍 Verify Locally

Before deploying, test locally:

```bash
# Start server
cd ticket
python run_server.py

# In another terminal, run tests
python test_api.py
```

Or open http://localhost:8000 in your browser.

---

**Status:** ✅ Ready to Deploy  
**Platform:** Render (100% FREE)  
**Time:** 3 minutes  
**Cost:** $0 forever
