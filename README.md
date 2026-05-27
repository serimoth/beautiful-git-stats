# 🚀 Git Stats CLI

[![PyPI version](https://badge.fury.io/py/beautiful-git-stats.svg)](https://badge.fury.io/py/beautiful-git-stats)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**Beautiful Git repository statistics and insights right in your terminal** ✨

Get instant insights into your Git repositories with gorgeous, colorful terminal output. Perfect for developers, team leads, and anyone who wants to understand their codebase better.

## 🎯 Features

- 📊 **Repository Summary** - Total commits, authors, files, and line changes
- 👥 **Top Contributors** - See who's contributing the most
- 🔥 **Hotspots** - Find the most frequently changed files
- 📅 **Activity Patterns** - Discover when your team is most active
- 🎨 **Beautiful Output** - Rich, colorful terminal UI
- ⚡ **Fast & Lightweight** - Analyze repos in seconds
- 🔍 **Flexible Filtering** - Filter by author, date range, and more

## 📦 Installation

### Via pip (Recommended)

```bash
pip install beautiful-git-stats
```

### From source

```bash
git clone https://github.com/serimoth/beautiful-git-stats.git
cd beautiful-git-stats
pip install -e .
```

## 🚀 Quick Start

```bash
# Show repository summary
git-stats summary

# Show top 10 contributors
git-stats contributors

# Show most changed files (hotspots)
git-stats hotspots

# Show activity patterns by day and hour
git-stats activity
```

## 📖 Usage Examples

### Repository Summary

Get a quick overview of your repository:

```bash
git-stats summary /path/to/repo
```

Output:
```
┌─────────────────────────────────────┐
│      📊 Repository Summary          │
├─────────────────┬───────────────────┤
│ Total Commits   │ 1,234             │
│ Total Authors   │ 15                │
│ Total Files     │ 456               │
│ Lines Added     │ +45,678           │
│ Lines Deleted   │ -12,345           │
│ First Commit    │ 2023-01-15        │
│ Last Commit     │ 2026-05-20        │
│ Active Days     │ 234               │
└─────────────────┴───────────────────┘
```

### Filter by Author

```bash
git-stats summary --author "John Doe"
```

### Filter by Date Range

```bash
git-stats summary --since 2026-01-01 --until 2026-05-20
```

### Top Contributors

See who's contributing the most:

```bash
git-stats contributors --limit 5
```

### Find Hotspots

Identify files that change frequently (potential refactoring candidates):

```bash
git-stats hotspots --limit 10
```

### Activity Patterns

Understand when your team is most productive:

```bash
git-stats activity
```

## 🎨 Screenshots

![Git Stats Summary](https://via.placeholder.com/800x400?text=Git+Stats+Summary)
![Git Stats Contributors](https://via.placeholder.com/800x400?text=Top+Contributors)

## 🛠️ Advanced Usage

### Analyze Multiple Repositories

```bash
for repo in ~/projects/*; do
  echo "Analyzing $repo"
  git-stats summary "$repo"
done
```

### Export to JSON (Coming Soon)

```bash
git-stats summary --format json > stats.json
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🐛 Report bugs
2. 💡 Suggest new features
3. 🔧 Submit pull requests
4. 📖 Improve documentation
5. ⭐ Star this repo if you find it useful!

### Development Setup

```bash
git clone https://github.com/serimoth/beautiful-git-stats.git
cd beautiful-git-stats
pip install -e ".[dev]"
pytest
```

## 💖 Support This Project

If you find Git Stats CLI useful, consider supporting its development:

- ⭐ Star this repository
- 🐦 Share on Twitter
- ☕ [Support on Ko-fi](https://ko-fi.com/gitstatcli)

Your support helps maintain and improve this tool!

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details

## 🙏 Acknowledgments

Built with:
- [GitPython](https://github.com/gitpython-developers/GitPython) - Git repository interaction
- [Rich](https://github.com/Textualize/rich) - Beautiful terminal output
- [Click](https://github.com/pallets/click) - CLI framework

## 📬 Contact

- GitHub: [@serimoth](https://github.com/serimoth)
- Email: seri_moth@yahoo.com

---

Made with ❤️ by developers, for developers
