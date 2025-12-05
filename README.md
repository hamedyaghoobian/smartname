# SmartName - Intelligent File Renaming with Ollama

Automatically rename files based on their content using Ollama vision language models.

## Features

- **Multi-format support**: Images, PDFs, Videos, Text files, Notebooks, Code files, DOCX, PPTX
- **Content-aware**: Analyzes actual file content to generate meaningful names
- **Smart organization**: Automatically organize files into semantic folders (books, photos, figures, etc.)
- **Flexible casing**: Choose from 6 different naming styles (snake_case, kebab-case, camelCase, etc.)
- **Safe by default**: Dry-run mode prevents accidental renames
- **Customizable**: Choose your preferred Ollama model and categories

## Installation

### Prerequisites

1. **Ollama**: Install from [ollama.ai](https://ollama.ai)
2. **Python 3.9+**
3. **Dependencies**:

```bash
pip install pymupdf requests python-docx python-pptx
```

4. **Optional - For video support**:
```bash
brew install ffmpeg  # macOS
```

5. **Optional - For DOCX/PPTX visual analysis**:
```bash
brew install libreoffice  # macOS
```

### Download a Vision Model

```bash
# Recommended models (you may already have these!)
ollama pull llama3.2-vision:latest   # Best balance
ollama pull qwen2.5vl:latest         # High accuracy
ollama pull riven/smolvlm:latest     # Fast & lightweight

# Alternative models
ollama pull llava:latest
ollama pull llava:13b
ollama pull bakllava
```

### Check What Models You Have

```bash
# If ollama is in PATH
ollama list

# Or check via API
curl -s http://127.0.0.1:11434/api/tags | python3 -m json.tool
```

## Usage

### Basic Usage (Dry Run)

Preview what files would be renamed without making changes:

```bash
python rename_files.py data/
```

### Actually Rename Files

Once you're happy with the suggestions, use `--execute`:

```bash
python rename_files.py data/ --execute
```

### Custom Model

Use a different Ollama model:

```bash
python rename_files.py data/ --model llava:13b
```

### Custom Ollama Server

If Ollama is running on a different host:

```bash
python rename_files.py data/ --ollama-url http://localhost:11434
```

### Options

```
positional arguments:
  directory             Directory containing files to rename/organize

optional arguments:
  --model MODEL         Ollama model to use (default: llava:latest)
  --ollama-url URL      Ollama server URL (default: http://127.0.0.1:11434)
  --execute             Actually rename/organize files (default is dry-run)
  --dpi DPI             DPI for PDF rendering (default: 150)
  --case STYLE          Casing style: snake, kebab, camel, pascal, lower, title
                        (default: snake)
  --organize            Organize files into categorized folders
  --rename-in-folders   Also rename files within folders (requires --organize)
  --categories CAT...   Custom categories for organization
```

## File Organization

Use the `--organize` flag to automatically categorize and organize files into folders based on their content.

### Default Categories

The VLM will categorize files into these semantic folders:
- **books**: Textbooks, ebooks, book pages, manuals
- **photos**: Personal photos, portraits, landscapes, snapshots
- **figures**: Charts, graphs, diagrams, scientific figures, infographics
- **documents**: Forms, letters, reports, receipts, official documents
- **presentations**: Slides, presentation materials, slide decks
- **screenshots**: Screen captures, UI screenshots, app interfaces
- **art**: Artwork, illustrations, paintings, creative images
- **code**: Code snippets, programming files
- **other**: Uncategorized files

### Organization Examples

```bash
# Dry run - preview organization
python rename_files.py data/ --organize

# Actually organize files into folders
python rename_files.py data/ --organize --execute

# Organize AND rename files within folders
python rename_files.py data/ --organize --rename-in-folders --execute

# Use custom categories
python rename_files.py data/ --organize --categories work personal projects --execute

# Organize with specific model
python rename_files.py data/ --organize --model qwen2.5vl:latest --execute
```

## Supported File Types

- **Images**: `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.webp`
- **PDFs**: `.pdf` (analyzes first page)
- **Office Documents**: `.docx`, `.pptx` (text extraction or visual with LibreOffice)
- **Videos**: `.mov`, `.mp4`, `.avi`, `.mkv`, `.webm` (requires ffmpeg)
- **Text/Code**: `.txt`, `.md`, `.ipynb`, `.py`, `.js`, `.json`

## Casing Styles

Choose how you want your filenames formatted:

- **snake** (default): `python_week04_args_kwargs_class.py`
- **kebab**: `python-week04-args-kwargs-class.py`
- **camel**: `pythonWeek04ArgsKwargsClass.py`
- **pascal**: `PythonWeek04ArgsKwargsClass.py`
- **lower**: `python week04 args kwargs class.py`
- **title**: `Python Week04 Args Kwargs Class.py`

## Examples

```bash
# Dry run with default snake_case
python rename_files.py data/

# Actually rename with kebab-case
python rename_files.py data/ --case kebab --execute

# Use camelCase style
python rename_files.py data/ --case camel --execute

# Use PascalCase with specific model
python rename_files.py data/ --case pascal --model qwen2.5vl:latest --execute

# Higher quality PDF analysis with Title Case
python rename_files.py data/ --dpi 300 --case title --execute
```

## How It Works

1. **Scans** the directory for supported files
2. **Analyzes** each file:
   - Images: Sent directly to vision model
   - PDFs: First page rendered as image, then analyzed
   - Videos: Frame extracted at 1 second, then analyzed
   - Text/Code: Content sent to language model
3. **Generates** descriptive filename (5-8 words)
4. **Sanitizes** the name (removes invalid characters, limits length)
5. **Renames** the file (only with `--execute` flag)

## Safety Features

- **Dry-run by default**: Must explicitly use `--execute` to rename
- **Collision prevention**: Adds `_1`, `_2`, etc. if name already exists
- **Extension preservation**: Original file extensions are kept
- **Error handling**: Skips problematic files and continues

## OCR Tool

This repo also includes `ollama_ocr_pdf.py` for OCR extraction from PDFs:

```bash
python ollama_ocr_pdf.py document.pdf output.txt
```

## License

MIT
