# 📁 IT Ticket Severity Calculator - Project Structure

## Essential Files & Folders

### 🚀 Quick Start Files
- **`START_SERVER_HERE.bat`** - Double-click to start the server
- **`run_server.py`** - Python script to start the server
- **`requirements.txt`** - Python dependencies

### 📚 Documentation
- **`README.md`** - Main project documentation
- **`API_DOCUMENTATION.md`** - Complete API reference
- **`TESTING_GUIDE.md`** - How to test the API
- **`VSCODE_SETUP_GUIDE.md`** - VS Code setup instructions
- **`NGROK_SETUP.md`** - How to share via ngrok
- **`FINAL_SEVERITY_CONFIGURATION.md`** - Severity threshold details

### 🧪 Testing Files
- **`test_api_endpoints.py`** - Automated API tests
- **`test_api_curl.bat`** - Windows curl tests
- **`IT_Ticket_Severity_API.postman_collection.json`** - Postman collection

### 📂 Core Directories

#### `/api/`
- **`app.py`** - FastAPI web server and REST API

#### `/models/`
- **`severity_model.pkl`** - Trained Random Forest model
- **`severity_scaler.pkl`** - Score scaling model
- **`embeddings_info.pkl`** - Embedding model info
- **`it_ticket_severity_dataset.csv`** - Training dataset

#### `/src/`
Source code organized by functionality:
- **`config/`** - Configuration files
- **`features/`** - Feature extraction (embeddings, TF-IDF)
- **`models/`** - Model training, prediction, evaluation
- **`preprocessing/`** - Text cleaning, language detection, translation
- **`scoring/`** - Severity score scaling
- **`utils/`** - Logging and utilities

#### `/static/`
- **`index.html`** - Web interface

#### `/.vscode/`
VS Code configuration:
- **`launch.json`** - Debug configurations
- **`settings.json`** - Project settings
- **`tasks.json`** - Quick tasks

#### `/logs/`
Application logs (auto-generated, can be deleted)

#### `/tests/`
Unit tests for the application

#### `/data/`
Empty - data files were removed after training

## 🗑️ Deleted Files

The following unnecessary files were removed:
- ❌ Jupyter notebooks (development only)
- ❌ Raw training data (already trained)
- ❌ Processed data files
- ❌ Old log files
- ❌ Duplicate documentation
- ❌ Test HTML page
- ❌ Linux/Mac scripts (Windows only)
- ❌ Python cache files

## 📊 Current Size

The project is now optimized with only essential files:
- Core application code
- Trained models
- Documentation
- Testing tools
- Web interface

## 🎯 What You Need

**To run the server:**
1. `START_SERVER_HERE.bat` or `python run_server.py`
2. Models in `/models/` folder
3. Source code in `/src/` folder
4. Web interface in `/static/` folder

**To test:**
1. `test_api_endpoints.py`
2. `test_api_curl.bat`
3. Postman collection

**To learn:**
1. `README.md`
2. `API_DOCUMENTATION.md`
3. Other documentation files

Everything else is optional!
