# SmartName - Quick Reference Card

## 🚀 One-Line Commands

```bash
# Preview (safe, no changes)
python rename_files.py data/

# Rename with default style (snake_case)
python rename_files.py data/ --execute

# Different casing styles
python rename_files.py data/ --case kebab --execute
python rename_files.py data/ --case title --execute
python rename_files.py data/ --case pascal --execute
```

## 📋 Casing Styles Quick Guide

| Flag | Style | Example |
|------|-------|---------|
| `--case snake` | snake_case | `my_awesome_file.txt` |
| `--case kebab` | kebab-case | `my-awesome-file.txt` |
| `--case camel` | camelCase | `myAwesomeFile.txt` |
| `--case pascal` | PascalCase | `MyAwesomeFile.txt` |
| `--case lower` | lowercase | `my awesome file.txt` |
| `--case title` | Title Case | `My Awesome File.txt` |

## 📂 Supported File Types

✅ Images: `.png` `.jpg` `.jpeg` `.gif` `.bmp` `.webp`  
✅ Documents: `.pdf` `.docx` `.pptx`  
✅ Videos: `.mov` `.mp4` `.avi` `.mkv` `.webm`  
✅ Text/Code: `.txt` `.md` `.py` `.js` `.json` `.ipynb`

## 🎯 Common Workflows

### Python Projects
```bash
python rename_files.py ~/Code/project/ --case snake --execute
```

### React Components
```bash
python rename_files.py ~/Code/react-app/ --case pascal --execute
```

### Web Assets
```bash
python rename_files.py ~/Website/images/ --case kebab --execute
```

### Academic Papers
```bash
python rename_files.py ~/Papers/ --case title --dpi 300 --execute
```

## 🛠️ All Options

```bash
python rename_files.py DIRECTORY \
  [--model MODEL] \
  [--case STYLE] \
  [--dpi DPI] \
  [--execute]
```

| Option | Description | Default |
|--------|-------------|---------|
| `DIRECTORY` | Path to files | Required |
| `--model` | Ollama model | `llava:latest` |
| `--case` | Casing style | `snake` |
| `--dpi` | PDF quality | `150` |
| `--execute` | Actually rename | Dry-run |

## 🤖 Recommended Models

| Model | Speed | Accuracy | Use Case |
|-------|-------|----------|----------|
| `riven/smolvlm:latest` | ⚡⚡⚡ | ⭐⭐ | Testing |
| `llama3.2-vision:latest` | ⚡⚡ | ⭐⭐⭐ | Balanced |
| `qwen2.5vl:latest` | ⚡ | ⭐⭐⭐⭐ | Production |

## 📦 Installation

```bash
# Required
pip install pymupdf requests python-docx python-pptx

# Optional
brew install ffmpeg libreoffice
```

## ⚡ Quick Troubleshooting

**404 Error?**
```bash
# Check available models
curl -s http://127.0.0.1:11434/api/tags | python3 -m json.tool

# Use a model you have
python rename_files.py data/ --model llama3.2-vision:latest
```

**DOCX not working?**
```bash
pip install python-docx python-pptx
```

**Video not working?**
```bash
brew install ffmpeg
```

## 🎓 Learn More

- `README.md` - Full documentation
- `QUICKSTART.md` - 5-minute guide
- `CASING_GUIDE.md` - Style details
- `EXAMPLES.md` - Real examples
- `CHANGELOG.md` - What's new

## 💡 Pro Tips

1. **Always preview first** - Skip `--execute` to see what will happen
2. **Try multiple styles** - Test different `--case` options
3. **Match your project** - Use conventions from your tech stack
4. **Batch by context** - Different styles for code vs documents

## 🎉 Example Session

```bash
# 1. Preview with different styles
python rename_files.py data/ --case snake
python rename_files.py data/ --case kebab
python rename_files.py data/ --case title

# 2. Pick your favorite
python rename_files.py data/ --case kebab

# 3. Execute
python rename_files.py data/ --case kebab --execute

# 4. Success! 🎉
```

---

**Questions?** Check the full docs in `README.md`
