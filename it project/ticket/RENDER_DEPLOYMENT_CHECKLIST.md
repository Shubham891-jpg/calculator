# ✅ Render Deployment Checklist

## Pre-Deployment Verification

### 1. Model Files (CRITICAL!)
- [x] `models/severity_model.pkl` exists (1.3 MB)
- [x] `models/severity_scaler.pkl` exists (0.6 KB)
- [x] `models/embeddings_info.pkl` exists (0.09 KB)
- [x] `models/it_ticket_severity_dataset.csv` exists (456 KB)
- [x] Model files are NOT in .gitignore
- [x] Model files are staged for commit

### 2. Configuration Files
- [x] `Dockerfile` exists in repository root
- [x] `render.yaml` exists in repository root
- [x] `.dockerignore` exists and configured
- [x] `requirements.txt` has all dependencies
- [x] Python 3.11 compatible packages (numpy>=1.26.0)

### 3. Application Files
- [x] `run_server.py` handles PORT environment variable
- [x] Server binds to 0.0.0.0 (not 127.0.0.1)
- [x] `api/app.py` has CORS enabled
- [x] `static/index.html` uses dynamic API URL
- [x] Health check endpoint at `/health`

### 4. Git Repository
- [x] All files committed to git
- [x] Models directory committed (not ignored)
- [x] Repository pushed to GitHub
- [x] Branch is 'main' (matches render.yaml)

### 5. Render Configuration
- [x] `render.yaml` specifies `env: docker`
- [x] `dockerfilePath: ./Dockerfile`
- [x] `dockerContext: .`
- [x] `healthCheckPath: /health`
- [x] `plan: free`

## Deployment Steps

1. **Commit and Push:**
   ```bash
   git add .
   git commit -m "Ready for Render deployment with models"
   git push origin main
   ```

2. **Go to Render:**
   - Visit https://render.com
   - Sign up (free, no credit card)
   - Click "New +" → "Web Service"

3. **Connect Repository:**
   - Select your GitHub repository
   - Render will auto-detect `render.yaml`

4. **Deploy:**
   - Click "Create Web Service"
   - Wait 3-5 minutes for build
   - Check logs for any errors

5. **Verify:**
   - Visit `https://your-app.onrender.com/health`
   - Should return: `{"status":"healthy",...}`
   - Test web interface at `https://your-app.onrender.com`

## Expected Build Process

1. Render clones your repository
2. Reads `render.yaml` configuration
3. Builds Docker image using `Dockerfile`
4. Installs Python dependencies from `requirements.txt`
5. Downloads NLTK data
6. Starts server with `python run_server.py`
7. Health check passes at `/health`
8. App goes live!

## Troubleshooting

### If build fails:
- Check Render logs for specific error
- Verify all model files are in repository
- Ensure Dockerfile syntax is correct
- Check requirements.txt for version conflicts

### If health check fails:
- Server might not be binding to 0.0.0.0
- PORT environment variable not being used
- Model files missing or not loading
- Check Render logs for startup errors

### If predictions fail:
- Model files might be corrupted
- NLTK data not downloaded
- Check `/model/info` endpoint for details

## Post-Deployment Testing

```bash
# Replace YOUR_APP_URL with your actual Render URL
export API_URL="https://your-app.onrender.com"

# Test health
curl $API_URL/health

# Test prediction
curl -X POST "$API_URL/predict" \
  -H "Content-Type: application/json" \
  -d '{"ticket_text":"Server is down"}'

# Test web interface
# Open $API_URL in browser
```

## Status: ✅ READY FOR DEPLOYMENT

All checks passed! Your application is ready to deploy to Render.
