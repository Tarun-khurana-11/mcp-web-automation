# Git Setup and Push Guide

## 🚀 Quick Push to GitHub

### Step 1: Configure Git

```bash
# Set your email (for commits)
git config --global user.email "tarun.khurana@ideafoundation.co.in"

# Set your name
git config --global user.name "Tarun Khurana"

# Verify configuration
git config --global --list
```

### Step 2: Initialize Repository (if not already done)

```bash
cd /home/tarun/Desktop/Ideafoundation/mcp

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: MCP Web Automation Agents with DeepAgent support"
```

### Step 3: Create GitHub Repository

**Option A: Using GitHub Website**

1. Go to https://github.com
2. Log in with your account
3. Click "+" → "New repository"
4. Repository name: `mcp-web-automation`
5. Description: "Intelligent web automation using MCP with LangChain and DeepAgents"
6. Choose: Public or Private
7. **DO NOT** initialize with README (you already have one)
8. Click "Create repository"

**Option B: Using GitHub CLI (if installed)**

```bash
gh repo create mcp-web-automation --public --source=. --remote=origin
```

### Step 4: Connect to Remote Repository

```bash
# Replace <USERNAME> with your GitHub username
git remote add origin https://github.com/<USERNAME>/mcp-web-automation.git

# Verify remote
git remote -v
```

### Step 5: Push to GitHub

```bash
# Push to main branch
git branch -M main
git push -u origin main
```

---

## 🔐 Authentication

### Option 1: Personal Access Token (Recommended)

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a name: "MCP Project"
4. Select scopes: `repo` (full control of private repositories)
5. Click "Generate token"
6. **COPY THE TOKEN** (you won't see it again!)

When prompted for password during push, use the token instead.

### Option 2: SSH Key

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "tarun.khurana@ideafoundation.co.in"

# Copy public key
cat ~/.ssh/id_ed25519.pub

# Add to GitHub:
# Settings → SSH and GPG keys → New SSH key → Paste key
```

Then use SSH URL:
```bash
git remote set-url origin git@github.com:<USERNAME>/mcp-web-automation.git
```

---

## 📝 Complete Commands (Copy-Paste)

```bash
# 1. Configure Git
git config --global user.email "tarun.khurana@ideafoundation.co.in"
git config --global user.name "Tarun Khurana"

# 2. Initialize and commit
cd /home/tarun/Desktop/Ideafoundation/mcp
git init
git add .
git commit -m "Initial commit: MCP Web Automation Agents"

# 3. Add remote (replace <USERNAME>)
git remote add origin https://github.com/<USERNAME>/mcp-web-automation.git

# 4. Push
git branch -M main
git push -u origin main
```

---

## 🔄 Future Updates

After initial push, use these commands to update:

```bash
# Check status
git status

# Add modified files
git add .

# Commit changes
git commit -m "Your commit message here"

# Push to GitHub
git push
```

---

## ⚠️ Important Notes

### Files That Will NOT Be Pushed (Protected)

✅ `.env` file - Contains API keys (in .gitignore)
✅ `venv/` folder - Virtual environment (in .gitignore)
✅ `__pycache__/` - Python cache (in .gitignore)
✅ Browser session data - User sessions (in .gitignore)

### Files That WILL Be Pushed

✅ `client.py` - Standard agent
✅ `client_deep_agent.py` - DeepAgent
✅ `get_tools.py` - Tool utility
✅ `requirements.txt` - Dependencies
✅ `README.md` - Documentation
✅ `.gitignore` - Git ignore rules

---

## 🛡️ Security Checklist

Before pushing, verify:

- [ ] `.env` file is in `.gitignore`
- [ ] No API keys in code
- [ ] No passwords in code
- [ ] `.gitignore` is committed
- [ ] Run: `git status` to check what will be pushed

---

## 📦 Repository Structure on GitHub

```
mcp-web-automation/
├── .gitignore
├── README.md
├── requirements.txt
├── client.py
├── client_deep_agent.py
├── get_tools.py
└── GIT_SETUP_GUIDE.md
```

**NOT included:**
- `.env` (API keys)
- `venv/` (virtual environment)
- `__pycache__/` (Python cache)

---

## 🎯 Next Steps After Push

1. ✅ Add repository description on GitHub
2. ✅ Add topics/tags: `mcp`, `langchain`, `playwright`, `deepagent`, `web-automation`
3. ✅ Enable Issues (for bug reports)
4. ✅ Add a LICENSE file (MIT, Apache, etc.)
5. ✅ Star your own repo! ⭐

---

**Ready to push! 🚀**
