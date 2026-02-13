# 🚀 Running IT Ticket Severity Calculator in VS Code

## 📋 Prerequisites

1. **VS Code Installed** - Download from https://code.visualstudio.com/
2. **Python Extension** - Install from VS Code Extensions marketplace
3. **Python 3.8+** - Verify with `python --version`

---

## 🎯 Quick Start (3 Steps)

### Step 1: Open Project in VS Code

1. Open VS Code
2. Click **File** → **Open Folder**
3. Navigate to and select the `it-ticket-severity-calculator` folder
4. Click **Select Folder**

### Step 2: Open Integrated Terminal

- Press **Ctrl + `** (backtick) or
- Click **Terminal** → **New Terminal** from the menu
- Or press **Ctrl + Shift + `**

### Step 3: Run the Server

In the terminal, type:
```bash
python run_server.py
```

**That's it!** 🎉 The server will start and you'll see:
```
🚀 Starting IT Ticket Severity Calculator Server...
🌐 Server will be available at: http://localhost:8000
```

---

## 🖥️ Method 1: Using VS Code Terminal (Recommended)

### Start the Server:
1. Open terminal in VS Code (**Ctrl + `**)
2. Make sure you're in the project folder
3. Run:
   ```bash
   python run_server.py
   ```

### Stop the Server:
- Press **Ctrl + C** in the terminal

### View Output:
- All logs appear directly in the terminal
- Easy to see errors and status messages

---

## 🎮 Method 2: Using VS Code Run Button

### Setup (One-time):

1. **Create Launch Configuration:**
   - Press **Ctrl + Shift + D** (opens Run and Debug panel)
   - Click **"create a launch.json file"**
   - Select **Python**
   - Replace content with the configuration below

2. **Run the Server:**
   - Press **F5** or click the green **▶ Start Debugging** button
   - Server starts with debugging enabled

### Stop the Server:
- Press **Shift + F5** or click the red **■ Stop** button

---

## 📁 Method 3: Using VS Code Tasks

### Setup (One-time):

1. Press **Ctrl + Shift + P**
2. Type **"Tasks: Configure Task"**
3. Select **"Create tasks.json from template"**
4. Select **"Others"**
5. Replace content with the configuration below

### Run the Server:
1. Press **Ctrl + Shift + P**
2. Type **"Tasks: Run Task"**
3. Select **"Start IT Ticket Server"**

---

## 🔧 VS Code Configuration Files

I've created these configuration files for you:

### 1. `.vscode/launch.json` - For debugging
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Start IT Ticket Server",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/run_server.py",
            "console": "integratedTerminal",
            "justMyCode": false,
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            }
        },
        {
            "name": "Test API Endpoints",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/test_api_endpoints.py",
            "console": "integratedTerminal"
        },
        {
            "name": "Train Model",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/src/models/train_model.py",
            "console": "integratedTerminal"
        }
    ]
}
```

### 2. `.vscode/tasks.json` - For running tasks
```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Start IT Ticket Server",
            "type": "shell",
            "command": "python",
            "args": ["run_server.py"],
            "problemMatcher": [],
            "presentation": {
                "reveal": "always",
                "panel": "new"
            }
        },
        {
            "label": "Test API",
            "type": "shell",
            "command": "python",
            "args": ["test_api_endpoints.py"],
            "problemMatcher": []
        },
        {
            "label": "Stop Server",
            "type": "shell",
            "command": "taskkill",
            "args": ["/F", "/IM", "python.exe"],
            "windows": {
                "command": "taskkill",
                "args": ["/F", "/IM", "python.exe"]
            },
            "linux": {
                "command": "pkill",
                "args": ["-f", "run_server.py"]
            },
            "osx": {
                "command": "pkill",
                "args": ["-f", "run_server.py"]
            }
        }
    ]
}
```

### 3. `.vscode/settings.json` - Project settings
```json
{
    "python.defaultInterpreterPath": "python",
    "python.terminal.activateEnvironment": true,
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true,
        "**/.pytest_cache": true
    },
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": false,
    "python.formatting.provider": "black",
    "editor.formatOnSave": false
}
```

---

## 🎯 Common VS Code Shortcuts

| Action | Shortcut |
|--------|----------|
| Open Terminal | **Ctrl + `** |
| New Terminal | **Ctrl + Shift + `** |
| Run/Debug | **F5** |
| Stop Debugging | **Shift + F5** |
| Command Palette | **Ctrl + Shift + P** |
| Open File | **Ctrl + P** |
| Split Terminal | **Ctrl + Shift + 5** |
| Clear Terminal | **Ctrl + K** |

---

## 📊 Viewing the Application

Once the server is running:

1. **Web Interface:**
   - Open browser to http://localhost:8000
   - Or **Ctrl + Click** the URL in VS Code terminal

2. **API Documentation:**
   - http://localhost:8000/docs (Swagger UI)
   - http://localhost:8000/redoc (Alternative docs)

3. **Health Check:**
   - http://localhost:8000/health

---

## 🐛 Debugging in VS Code

### Set Breakpoints:
1. Open any Python file (e.g., `api/app.py`)
2. Click in the left margin next to line numbers
3. Red dot appears = breakpoint set

### Start Debugging:
1. Press **F5**
2. Make a request to the API
3. VS Code pauses at breakpoints
4. Inspect variables, step through code

### Debug Controls:
- **F5** - Continue
- **F10** - Step Over
- **F11** - Step Into
- **Shift + F11** - Step Out
- **Shift + F5** - Stop

---

## 📝 Running Tests in VS Code

### Method 1: Terminal
```bash
# Test predictions
python test_prediction.py

# Test API endpoints
python test_api_endpoints.py

# Test with cURL (Windows)
test_api_curl.bat
```

### Method 2: Python Test Explorer
1. Install **Python Test Explorer** extension
2. Tests appear in the Testing panel
3. Click ▶ to run individual tests

---

## 🔍 Useful VS Code Extensions

### Recommended:
1. **Python** (Microsoft) - Essential
2. **Pylance** (Microsoft) - IntelliSense
3. **Python Test Explorer** - Run tests easily
4. **REST Client** - Test API in VS Code
5. **Thunder Client** - Alternative API testing

### Optional:
6. **GitLens** - Git integration
7. **Error Lens** - Inline error display
8. **Better Comments** - Colorful comments
9. **Bracket Pair Colorizer** - Matching brackets

---

## 🌐 Testing API in VS Code

### Using REST Client Extension:

1. Install **REST Client** extension
2. Create file: `test_requests.http`
3. Add requests:

```http
### Health Check
GET http://localhost:8000/health

### Single Prediction
POST http://localhost:8000/predict
Content-Type: application/json

{
  "ticket_text": "Server is down and users cannot access email"
}

### Batch Prediction
POST http://localhost:8000/predict/batch
Content-Type: application/json

{
  "tickets": [
    "Server is down",
    "Printer not working",
    "Password reset needed"
  ]
}
```

4. Click **Send Request** above each request

---

## 🎨 VS Code Terminal Tips

### Multiple Terminals:
1. Click **+** in terminal panel for new terminal
2. Use dropdown to switch between terminals
3. Run server in one, tests in another

### Split Terminal:
1. Click split icon in terminal
2. Or press **Ctrl + Shift + 5**
3. View multiple terminals side-by-side

### Terminal Colors:
- Server logs appear in different colors
- Errors in red
- Info in cyan
- Success in green

---

## 🚨 Troubleshooting in VS Code

### Server Won't Start:
1. Check terminal for error messages
2. Verify Python is installed: `python --version`
3. Install dependencies: `pip install -r requirements.txt`
4. Check if port 8000 is in use

### Can't See Output:
1. Make sure terminal is visible (**Ctrl + `**)
2. Check Output panel (**Ctrl + Shift + U**)
3. Look at Problems panel (**Ctrl + Shift + M**)

### Import Errors:
1. Check Python interpreter (bottom-left in VS Code)
2. Select correct Python environment
3. Reload VS Code window (**Ctrl + Shift + P** → "Reload Window")

### Port Already in Use:
```bash
# Windows - Kill process on port 8000
netstat -ano | findstr :8000
taskkill /PID <process_id> /F

# Or use the Stop Server task
```

---

## 📚 Quick Reference

### Start Server:
```bash
python run_server.py
```

### Stop Server:
- **Ctrl + C** in terminal

### Test Server:
```bash
python test_api_endpoints.py
```

### View in Browser:
- http://localhost:8000

### API Docs:
- http://localhost:8000/docs

---

## 🎉 You're Ready!

The easiest way to get started:

1. **Open VS Code**
2. **Open project folder**
3. **Open terminal** (Ctrl + `)
4. **Run:** `python run_server.py`
5. **Open browser:** http://localhost:8000

**That's it!** 🚀

For more help, check:
- `README.md` - Project overview
- `GETTING_STARTED.md` - Quick start guide
- `API_DOCUMENTATION.md` - API reference
- `TESTING_GUIDE.md` - Testing instructions