# 🔗 GitHub Setup Guide

## Current Status
Your code is committed locally but needs to be pushed to GitHub.

## Issue
The repository `https://github.com/Shubham891-jpg/ticket2.git` was not found.

---

## 📝 Step-by-Step Setup

### Step 1: Create GitHub Repository

1. **Go to GitHub:**
   - Visit: https://github.com/new
   - Or click the "+" icon in top-right → "New repository"

2. **Repository Settings:**
   ```
   Repository name: severity
   Description: IT Ticket Severity Calculator - AI-powered severity assessment
   Visibility: ✅ Public (required for free Render deployment)
   
   ❌ Do NOT check:
      - Add a README file
      - Add .gitignore
      - Choose a license
   ```

3. **Click "Create repository"**

### Step 2: Copy Repository URL

After creating, GitHub will show you the repository URL:
```
https://github.com/Shubham891-jpg/severity.git
```

Copy this URL!

### Step 3: Update Git Remote

Open terminal in the `ticket` folder and run:

```bash
# Update the remote URL (replace with your actual URL)
git remote set-url origin https://github.com/Shubham891-jpg/severity.git

# Verify it's updated
git remote -v

# Push to GitHub
git push -u origin main
```

### Step 4: Verify on GitHub

Go to your repository URL and verify:
- ✅ All files are there
- ✅ `models/` folder with .pkl files (1.8 MB total)
- ✅ `Dockerfile` exists
- ✅ `render.yaml` exists

---

## 🚀 Quick Commands

```bash
# If you need to authenticate
git config --global user.name "Shubham jha"
git config --global user.email "shubhamjha2434@gmail.com"

# Update remote (replace YOUR-REPO-NAME)
git remote set-url origin https://github.com/Shubham891-jpg/YOUR-REPO-NAME.git

# Push to GitHub
git push -u origin main
```

---

## 🔐 Authentication

If GitHub asks for authentication:

**Option 1: Personal Access Token (Recommended)**
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Select scopes: `repo` (full control)
4. Copy the token
5. When pushing, use token as password

**Option 2: GitHub CLI**
```bash
# Install GitHub CLI
winget install GitHub.cli

# Authenticate
gh auth login
```

**Option 3: SSH Key**
1. Generate SSH key: `ssh-keygen -t ed25519 -C "shubhamjha2434@gmail.com"`
2. Add to GitHub: https://github.com/settings/keys
3. Update remote: `git remote set-url origin git@github.com:Shubham891-jpg/YOUR-REPO.git`

---

## ⚠️ Troubleshooting

### "Repository not found"
- Make sure the repository exists on GitHub
- Check if the URL is correct
- Verify you're logged into the correct GitHub account

### "Authentication failed"
- Use a Personal Access Token instead of password
- Or use GitHub CLI: `gh auth login`

### "Permission denied"
- Make sure you own the repository
- Or you have write access to it

---

## ✅ After Successful Push

Once pushed to GitHub, you can deploy on Render:

1. Go to https://render.com
2. Sign up (free, no credit card)
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Render auto-detects `render.yaml`
6. Click "Create Web Service"
7. Wait 3-5 minutes
8. Your app will be live!

---

## 📞 Need Help?

If you're stuck, you can:
1. Run the automated script: `setup_github.bat`
2. Check GitHub's guide: https://docs.github.com/en/get-started/quickstart/create-a-repo
3. Verify your git config: `git config --list`
