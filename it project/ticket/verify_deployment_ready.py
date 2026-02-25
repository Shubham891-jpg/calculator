#!/usr/bin/env python3
"""
Deployment Readiness Verification Script
Run this before deploying to Render to ensure everything is configured correctly
"""

import os
import sys
from pathlib import Path

def check_file_exists(filepath, description, critical=True):
    """Check if a file exists"""
    if os.path.exists(filepath):
        size = os.path.getsize(filepath)
        size_kb = size / 1024
        print(f"✅ {description}: {filepath} ({size_kb:.2f} KB)")
        return True
    else:
        symbol = "❌" if critical else "⚠️"
        print(f"{symbol} {description}: {filepath} NOT FOUND")
        return not critical

def check_file_content(filepath, search_text, description):
    """Check if file contains specific text"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            if search_text in content:
                print(f"✅ {description}")
                return True
            else:
                print(f"❌ {description} - NOT FOUND")
                return False
    except Exception as e:
        print(f"❌ {description} - ERROR: {e}")
        return False

def main():
    print("=" * 70)
    print("🔍 RENDER DEPLOYMENT READINESS CHECK")
    print("=" * 70)
    print()
    
    all_checks_passed = True
    
    # Check current directory
    current_dir = Path.cwd()
    print(f"📍 Current Directory: {current_dir}")
    print()
    
    # 1. Check Model Files (CRITICAL)
    print("1️⃣  CHECKING MODEL FILES (CRITICAL)")
    print("-" * 70)
    model_files = [
        ("models/severity_model.pkl", "Trained ML Model", True),
        ("models/severity_scaler.pkl", "Severity Scaler", True),
        ("models/embeddings_info.pkl", "Embeddings Info", True),
        ("models/it_ticket_severity_dataset.csv", "Training Dataset", False),
    ]
    
    for filepath, desc, critical in model_files:
        if not check_file_exists(filepath, desc, critical):
            all_checks_passed = False
    print()
    
    # 2. Check Configuration Files
    print("2️⃣  CHECKING CONFIGURATION FILES")
    print("-" * 70)
    config_files = [
        ("Dockerfile", "Docker Configuration", True),
        ("render.yaml", "Render Config", True),
        (".dockerignore", "Docker Ignore", True),
        ("requirements.txt", "Python Dependencies", True),
        ("README.md", "Documentation", False),
    ]
    
    for filepath, desc, critical in config_files:
        if not check_file_exists(filepath, desc, critical):
            all_checks_passed = False
    print()
    
    # 3. Check Application Files
    print("3️⃣  CHECKING APPLICATION FILES")
    print("-" * 70)
    app_files = [
        ("run_server.py", "Server Startup Script", True),
        ("api/app.py", "FastAPI Application", True),
        ("static/index.html", "Web Interface", True),
    ]
    
    for filepath, desc, critical in app_files:
        if not check_file_exists(filepath, desc, critical):
            all_checks_passed = False
    print()
    
    # 4. Check File Contents
    print("4️⃣  CHECKING FILE CONFIGURATIONS")
    print("-" * 70)
    
    checks = [
        ("run_server.py", 'os.environ.get("PORT"', "PORT environment variable support"),
        ("run_server.py", '"0.0.0.0"', "Server binds to 0.0.0.0"),
        ("api/app.py", "CORSMiddleware", "CORS enabled"),
        ("static/index.html", "window.location.origin", "Dynamic API URL"),
        ("Dockerfile", "python:3.11", "Python 3.11 base image"),
        ("Dockerfile", "run_server.py", "Correct startup command"),
        ("render.yaml", "env: docker", "Docker environment"),
        ("render.yaml", "healthCheckPath: /health", "Health check configured"),
        ("requirements.txt", "numpy>=1.26", "Python 3.11+ compatible numpy"),
    ]
    
    for filepath, search_text, desc in checks:
        if not check_file_content(filepath, search_text, desc):
            all_checks_passed = False
    print()
    
    # 5. Check .gitignore
    print("5️⃣  CHECKING GIT CONFIGURATION")
    print("-" * 70)
    
    if os.path.exists(".gitignore"):
        with open(".gitignore", 'r') as f:
            gitignore_content = f.read()
            
        # Check that models are NOT ignored
        if "models/*.pkl" in gitignore_content or "*.pkl" in gitignore_content:
            print("❌ .gitignore blocks model files - models will NOT be deployed!")
            print("   Remove '*.pkl' and 'models/*.pkl' from .gitignore")
            all_checks_passed = False
        else:
            print("✅ .gitignore does not block model files")
    else:
        print("⚠️  .gitignore not found")
    print()
    
    # 6. Check if models are tracked by git
    print("6️⃣  CHECKING GIT TRACKING")
    print("-" * 70)
    
    if os.path.exists(".git"):
        import subprocess
        try:
            # Check if models are tracked
            result = subprocess.run(
                ["git", "ls-files", "models/"],
                capture_output=True,
                text=True,
                check=True
            )
            
            tracked_files = result.stdout.strip().split('\n')
            tracked_models = [f for f in tracked_files if f.endswith('.pkl')]
            
            if len(tracked_models) >= 3:
                print(f"✅ Model files are tracked by git ({len(tracked_models)} .pkl files)")
                for model in tracked_models:
                    print(f"   - {model}")
            else:
                print(f"❌ Not all model files are tracked by git")
                print(f"   Found: {len(tracked_models)} .pkl files")
                print(f"   Expected: 3 .pkl files")
                print(f"   Run: git add models/")
                all_checks_passed = False
        except subprocess.CalledProcessError:
            print("⚠️  Could not check git tracking (git command failed)")
        except FileNotFoundError:
            print("⚠️  Git not installed or not in PATH")
    else:
        print("❌ Not a git repository - initialize with 'git init'")
        all_checks_passed = False
    print()
    
    # Final Summary
    print("=" * 70)
    if all_checks_passed:
        print("🎉 ALL CHECKS PASSED! READY FOR DEPLOYMENT")
        print()
        print("Next steps:")
        print("1. git add .")
        print("2. git commit -m 'Ready for Render deployment'")
        print("3. git push origin main")
        print("4. Go to render.com and deploy!")
    else:
        print("❌ SOME CHECKS FAILED - FIX ISSUES BEFORE DEPLOYING")
        print()
        print("Review the errors above and fix them before deploying to Render.")
    print("=" * 70)
    
    return 0 if all_checks_passed else 1

if __name__ == "__main__":
    sys.exit(main())
