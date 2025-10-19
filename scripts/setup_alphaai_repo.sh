#!/bin/bash
# Setup script: create GitHub repo and push local files
set -e
REPO_OWNER="DD505818"
REPO_NAME="AlphaAi"
VISIBILITY="public" # or "private"
echo "Preparing to create repo ${REPO_OWNER}/${REPO_NAME} and push current directory..."
if ! command -v gh >/dev/null 2>&1; then
  echo "gh CLI not found. Install GitHub CLI and run 'gh auth login' before continuing."
  exit 1
fi
# Initialize git if needed
if [ ! -d .git ]; then
  git init
  git branch -M main
fi
git add .
git commit -m "Initial commit - Alpha.Ai full package" || true
echo "Creating repository on GitHub..."
gh repo create ${REPO_OWNER}/${REPO_NAME} --${VISIBILITY} --source=. --remote=origin --push
echo "Repository created and pushed: https://github.com/${REPO_OWNER}/${REPO_NAME}"
