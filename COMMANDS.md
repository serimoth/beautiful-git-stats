# Git Stats CLI - Commands Cheat Sheet

## Installation
```bash
pip install git-stats-cli
```

## Basic Commands

### Repository Summary
```bash
git-stats summary
git-stats summary /path/to/repo
git-stats summary --author "John Doe"
git-stats summary --since 2026-01-01 --until 2026-05-20
```

### Top Contributors
```bash
git-stats contributors
git-stats contributors --limit 5
```

### Hotspots (Most Changed Files)
```bash
git-stats hotspots
git-stats hotspots --limit 20
```

### Activity Patterns
```bash
git-stats activity
```

## Development Commands

### Setup Development Environment
```bash
git clone https://github.com/yourusername/git-stats-cli.git
cd git-stats-cli
pip install -e .
```

### Run Locally
```bash
python -m gitstats.cli summary
```

### Build Package
```bash
pip install build
python -m build
```

### Upload to PyPI
```bash
pip install twine
python -m twine upload dist/*
```

## Git Commands for This Project

### Initial Setup
```bash
git init
git add .
git commit -m "Initial commit: Git Stats CLI v1.0.0"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/git-stats-cli.git
git push -u origin main
```

### Update After Changes
```bash
git add .
git commit -m "Your commit message"
git push
```

### Create New Release
```bash
git tag v1.0.1
git push origin v1.0.1
```

## Marketing Commands

### Check PyPI Stats
```bash
# Visit: https://pypistats.org/packages/git-stats-cli
```

### Check GitHub Stats
```bash
# Stars, forks, watchers on GitHub repo page
```
