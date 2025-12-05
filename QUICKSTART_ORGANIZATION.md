# SmartName - Quick Start Guide

## Installation

1. **Clone the repository**:
```bash
git clone https://github.com/hamedyaghoobian/smartname.git
cd smartname
```

2. **Install dependencies**:
```bash
pip install pymupdf requests python-docx python-pptx
```

3. **Install Ollama** (if not already installed):
   - Visit [ollama.ai](https://ollama.ai) and follow installation instructions

4. **Download a vision model**:
```bash
# Recommended models
ollama pull llama3.2-vision:latest   # Best balance
ollama pull qwen2.5vl:latest         # High accuracy
ollama pull riven/smolvlm:latest     # Fast & lightweight
```

## Usage

### File Renaming (Original Feature)

```bash
# Preview renames (dry-run)
python rename_files.py data/

# Actually rename files
python rename_files.py data/ --execute

# Use different casing style
python rename_files.py data/ --case kebab --execute
```

### File Organization (NEW!)

```bash
# Preview organization (dry-run)
python rename_files.py data/ --organize --model llama3.2-vision:latest

# Actually organize files into folders
python rename_files.py data/ --organize --model llama3.2-vision:latest --execute

# Organize AND rename files within folders
python rename_files.py data/ --organize --rename-in-folders --model llama3.2-vision:latest --execute

# Use custom categories
python rename_files.py data/ --organize --categories work personal academic --execute
```

## Default Categories

Files are organized into these semantic folders:
- **books**: Textbooks, ebooks, book pages, manuals
- **photos**: Personal photos, portraits, landscapes
- **figures**: Charts, graphs, diagrams, scientific figures
- **documents**: Forms, letters, reports, receipts
- **presentations**: Slides, presentation materials
- **screenshots**: Screen captures, UI screenshots
- **art**: Artwork, illustrations, paintings
- **code**: Code snippets, programming files
- **other**: Uncategorized files

## Important Notes

⚠️ **Model Selection**: The default model is `llava:latest`. If you don't have this model, specify one you have installed:
```bash
# Check available models
ollama list

# Use a specific model
python rename_files.py data/ --organize --model llama3.2-vision:latest --execute
```

✅ **Dry-run by default**: The tool will NOT modify files unless you use `--execute`

🔒 **Safe**: Automatic collision prevention with numbered suffixes

## Examples

```bash
# Example 1: Organize academic papers and books
python rename_files.py ~/Downloads --organize --model qwen2.5vl:latest --execute

# Example 2: Organize and rename with kebab-case
python rename_files.py ~/Desktop --organize --rename-in-folders --case kebab --execute

# Example 3: Custom categories for work files
python rename_files.py ~/Documents --organize --categories invoices receipts contracts --execute
```

## Troubleshooting

**404 Error**: Model not found
- Solution: Check `ollama list` and use `--model` flag with an installed model

**Syntax Warning**: Invalid escape sequence
- Solution: Update to latest version from GitHub

**Server Error**: Ollama not running
- Solution: Start Ollama service

## More Information

See [README.md](README.md) for complete documentation.
