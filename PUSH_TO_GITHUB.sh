#!/bin/bash
# Quick script to push to GitHub
# Account: tarun-khurana-11

echo "════════════════════════════════════════════════════════"
echo "  Pushing MCP Project to GitHub"
echo "════════════════════════════════════════════════════════"
echo ""

# Check if already initialized
if [ -d .git ]; then
    echo "✓ Git repository already initialized"
else
    echo "→ Initializing Git repository..."
    git init
    echo "✓ Done!"
fi

echo ""
echo "→ Adding files to Git..."
git add .

echo ""
echo "→ Creating commit..."
git commit -m "Initial commit: MCP Web Automation Agents with DeepAgent support"

echo ""
echo "→ Checking remote..."
if git remote get-url origin 2>/dev/null; then
    echo "✓ Remote already configured"
else
    echo "→ Adding remote repository..."
    git remote add origin https://github.com/tarun-khurana-11/mcp-web-automation.git
fi

echo ""
echo "→ Setting branch to main..."
git branch -M main

echo ""
echo "════════════════════════════════════════════════════════"
echo "  Ready to push!"
echo "════════════════════════════════════════════════════════"
echo ""
echo "Repository: https://github.com/tarun-khurana-11/mcp-web-automation"
echo ""
echo "Run this command to push:"
echo "  git push -u origin main"
echo ""
echo "When prompted:"
echo "  Username: tarun-khurana-11"
echo "  Password: [Your Personal Access Token]"
echo ""
echo "Get token from: https://github.com/settings/tokens"
echo ""
