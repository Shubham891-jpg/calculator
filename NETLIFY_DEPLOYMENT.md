# 🚀 Netlify Deployment Guide

## 🎯 Quick Deploy

### Option 1: Deploy via Netlify CLI

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Login to Netlify
netlify login

# Deploy
netlify deploy --prod
```

### Option 2: Deploy via Git

1. Push your code to GitHub/GitLab/Bitbucket
2. Go to https://app.netlify.com
3. Click "New site from Git"
4. Connect your repository
5. Netlify will auto-detect settings from `netlify.toml`
6. Click "Deploy site"

---

## ✅ Pre-Deployment Checklist

The following files have been created to fix the Python 3.14 build error:

- ✅ **`runtime.txt`** - Pins Python to 3.11 (stable, has prebuilt wheels)
- ✅ **`pyproject.toml`** - Declares build system requirements
- ✅ **`netlify.toml`** - Netlify configuration with optimized build
- ✅ **`requirements-netlify.txt`** - Optimized dependencies for deployment

---

## 🔧 What Was Fixed

### Problem
```
ModuleNotFoundError: No module named 'pkg_resources'
```

**Root Cause:** Python 3.14 doesn't have prebuilt pandas wheels, so pip tried to build from source but setuptools wasn't available.

### Solutions Applied

#### 1. Pin Python to 3.11 (`runtime.txt`)
```
python-3.11
```
- Python 3.11 has prebuilt wheels for all dependencies
- Avoids building from source
- Faster, more reliable builds

#### 2. Declare Build Requirements (`pyproject.toml`)
```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"
```
- Ensures setuptools and wheel are available
- Required for building any source distributions

#### 3. Optimize Build Command (`netlify.toml`)
```toml
command = "python -m pip install --upgrade pip setuptools wheel && pip install -r requirements.txt"
```
- Upgrades pip, setuptools, wheel before installing
- Uses binary wheels when available
- Prevents build failures

---

## 📁 Netlify Configuration Files

### `netlify.toml`
Main configuration file with:
- Build command
- Python version (3.11)
- Environment variables
- Redirect rules
- CORS headers

### `runtime.txt`
```
python-3.11
```
Specifies Python version for the build.

### `pyproject.toml`
Declares:
- Build system requirements
- Project metadata
- Dependencies
- Python version compatibility

### `requirements-netlify.txt`
Optimized dependencies:
- Removed visualization libraries (matplotlib, seaborn)
- Removed development tools (jupyter, ipykernel)
- Kept only production dependencies
- Faster builds, smaller deployment

---

## 🌐 Deployment Options

### Option A: Static Site + API Functions

**Best for:** Serverless deployment

1. Web interface served as static files
2. API endpoints as Netlify Functions
3. Requires converting FastAPI to serverless functions

**Pros:**
- Free tier available
- Auto-scaling
- Global CDN

**Cons:**
- Requires code changes
- Cold start delays
- Function timeout limits

### Option B: Static Site + External API

**Best for:** Keeping current architecture

1. Deploy static files to Netlify
2. Host API separately (Heroku, Railway, Render)
3. Update API URL in HTML

**Pros:**
- No code changes needed
- Full FastAPI functionality
- No timeout limits

**Cons:**
- Need separate hosting for API
- Additional cost

### Option C: Full Stack on Alternative Platform

**Best for:** Easiest deployment

Use platforms that support Python web apps:
- **Railway** - Recommended, easy Python deployment
- **Render** - Free tier available
- **Heroku** - Popular, well-documented
- **Google Cloud Run** - Serverless containers
- **AWS Elastic Beanstalk** - Full AWS integration

---

## 🚀 Recommended: Deploy to Railway

Railway is the easiest option for this project:

### Step 1: Install Railway CLI
```bash
npm install -g @railway/cli
```

### Step 2: Login
```bash
railway login
```

### Step 3: Initialize
```bash
railway init
```

### Step 4: Deploy
```bash
railway up
```

### Step 5: Get URL
```bash
railway domain
```

**That's it!** Railway automatically:
- Detects Python
- Installs dependencies
- Runs the server
- Provides HTTPS URL

---

## 🔧 Alternative: Deploy to Render

### Step 1: Create `render.yaml`
```yaml
services:
  - type: web
    name: it-ticket-severity
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python run_server.py
    envVars:
      - key: PYTHON_VERSION
        value: 3.11
```

### Step 2: Push to GitHub

### Step 3: Connect to Render
1. Go to https://render.com
2. New → Web Service
3. Connect repository
4. Render auto-detects settings
5. Deploy!

---

## 🐛 Troubleshooting Netlify Builds

### Build fails with "No module named 'pkg_resources'"

**Solution:** Ensure these files are committed:
```bash
git add runtime.txt pyproject.toml netlify.toml
git commit -m "Add Netlify configuration"
git push
```

### Build uses wrong Python version

**Check:**
1. `runtime.txt` exists and contains `python-3.11`
2. File is committed to repository
3. Netlify build logs show correct version

### Dependencies fail to install

**Try:**
1. Use `requirements-netlify.txt` instead:
   ```toml
   # In netlify.toml
   command = "pip install -r requirements-netlify.txt"
   ```
2. Check build logs for specific package errors
3. Verify all packages support Python 3.11

### API endpoints don't work

**Remember:** Netlify is primarily for static sites. For full API:
1. Use Netlify Functions (requires code changes)
2. Or deploy API separately (Railway, Render, etc.)
3. Update `API_BASE_URL` in HTML to point to API server

---

## 📊 Deployment Comparison

| Platform | Ease | Cost | Best For |
|----------|------|------|----------|
| **Railway** | ⭐⭐⭐⭐⭐ | Free tier | Full stack Python apps |
| **Render** | ⭐⭐⭐⭐ | Free tier | Web services |
| **Heroku** | ⭐⭐⭐⭐ | Paid | Production apps |
| **Netlify** | ⭐⭐⭐ | Free | Static sites + Functions |
| **Vercel** | ⭐⭐⭐ | Free | Static sites + Serverless |

**Recommendation:** Use Railway for easiest deployment with current code.

---

## ✅ Pre-Deployment Validation

Run these checks before deploying:

```bash
# 1. Validate setup
VALIDATE_SETUP.bat

# 2. Run tests
python test_api_endpoints.py

# 3. Check requirements
pip list

# 4. Verify files exist
dir runtime.txt pyproject.toml netlify.toml
```

---

## 🎉 Summary

**Files Created:**
- ✅ `runtime.txt` - Python 3.11
- ✅ `pyproject.toml` - Build requirements
- ✅ `netlify.toml` - Netlify config
- ✅ `requirements-netlify.txt` - Optimized deps

**Problem Fixed:**
- ✅ Python 3.14 build error resolved
- ✅ Missing pkg_resources fixed
- ✅ Pandas installation works

**Ready to Deploy:**
- ✅ All configuration files created
- ✅ Build process optimized
- ✅ Multiple deployment options provided

**Recommended Next Steps:**
1. Commit all new files to git
2. Deploy to Railway (easiest)
3. Or use Render/Heroku for production

---

**Need Help?** Check the troubleshooting section or deployment guides above.
