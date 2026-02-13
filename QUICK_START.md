# 🚀 Quick Start Guide

## ⚡ Fastest Way to Start

### Option 1: Double-Click (Easiest)
1. Double-click **`START_SERVER_HERE.bat`**
2. Wait 10 seconds for server to start
3. Open browser to http://localhost:8000
4. Done! 🎉

### Option 2: Command Line
```bash
python run_server.py
```

## ✅ Verify Everything Works

Run the validation script:
```bash
VALIDATE_SETUP.bat
```

This checks:
- ✅ Python installation
- ✅ Required packages
- ✅ Model files
- ✅ Static files
- ✅ Port availability

## 🧪 Test the API

Run automated tests:
```bash
python test_api_endpoints.py
```

Expected result: **5/5 tests passed** ✅

## 🌐 Access the Application

Once the server is running:

- **Web Interface**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 📱 Share with ngrok

1. Start the server (keep it running)
2. Open new terminal and run:
   ```bash
   ngrok http 8000
   ```
3. Copy the ngrok URL (e.g., https://abc123.ngrok.io)
4. Share that URL with anyone!

See **NGROK_SETUP.md** for details.

## 🐛 Having Issues?

Run the troubleshooter:
```bash
TROUBLESHOOT.bat
```

Or check these common solutions:

### Server won't start
```bash
# Check if Python is installed
python --version

# Install dependencies
python -m pip install -r requirements.txt
```

### Port 8000 already in use
```bash
# Kill existing Python processes
taskkill /F /IM python.exe
```

### Import errors
```bash
# Reinstall dependencies
python -m pip install -r requirements.txt --force-reinstall
```

### Web interface can't connect
1. Clear browser cache (Ctrl+Shift+Delete)
2. Try http://127.0.0.1:8000 instead
3. Check Windows Firewall settings

## 📊 Test Examples

### High Severity (90-100)
```
"All servers are down, complete system failure"
```
Expected: Score 90-100, Category: High

### Medium Severity (80-89)
```
"Database is extremely slow, applications timing out"
```
Expected: Score 80-89, Category: Medium

### Low Severity (10-79)
```
"User needs password reset"
```
Expected: Score 10-79, Category: Low

## 🎯 What's Included

- ✅ Trained AI model (Random Forest)
- ✅ Web interface (HTML/JavaScript)
- ✅ REST API (FastAPI)
- ✅ Multilingual support (English/Hindi)
- ✅ Automatic severity scoring (10-100)
- ✅ Complete documentation

## 📚 More Information

- **README.md** - Full project documentation
- **API_DOCUMENTATION.md** - Complete API reference
- **TESTING_GUIDE.md** - Testing instructions
- **VSCODE_SETUP_GUIDE.md** - VS Code setup
- **NGROK_SETUP.md** - Sharing via ngrok
- **PROJECT_STRUCTURE.md** - File organization

## 🎉 You're Ready!

The application is fully configured and tested. Just run **START_SERVER_HERE.bat** and you're good to go!

---

**Need help?** Check the troubleshooting guide or documentation files.
