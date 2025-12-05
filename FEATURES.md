# SmartName - Feature Summary

## ✨ New Features Added

### 1. Office Document Support
- **DOCX (Word Documents)**: Extract and analyze text content
- **PPTX (PowerPoint)**: Extract and analyze presentation content
- Optional visual analysis with LibreOffice for better accuracy

### 2. Flexible Casing Styles
Choose from 6 different filename casing styles:
- `snake_case` (default): `my_awesome_file.txt`
- `kebab-case`: `my-awesome-file.txt`
- `camelCase`: `myAwesomeFile.txt`
- `PascalCase`: `MyAwesomeFile.txt`
- `lowercase with spaces`: `my awesome file.txt`
- `Title Case With Spaces`: `My Awesome File.txt`

## 📦 Installation

```bash
# Install all dependencies
pip install -r requirements.txt

# Or install individually
pip install pymupdf requests python-docx python-pptx

# Optional dependencies
brew install ffmpeg        # For video support
brew install libreoffice   # For DOCX/PPTX visual analysis
```

## 🚀 Usage Examples

### Basic Usage
```bash
# Dry run with default settings
python rename_files.py data/

# Actually rename files
python rename_files.py data/ --execute
```

### With Casing Styles
```bash
# kebab-case
python rename_files.py data/ --case kebab --execute

# Title Case
python rename_files.py data/ --case title --execute

# PascalCase
python rename_files.py data/ --case pascal --execute
```

### Advanced Options
```bash
# Specific model + casing + high quality
python rename_files.py papers/ \
  --model qwen2.5vl:latest \
  --case title \
  --dpi 300 \
  --execute
```

## 📄 Supported File Types

| Type | Extensions | Status |
|------|-----------|--------|
| Images | `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.webp` | ✅ |
| PDFs | `.pdf` | ✅ |
| Word | `.docx` | ✅ NEW |
| PowerPoint | `.pptx` | ✅ NEW |
| Videos | `.mov`, `.mp4`, `.avi`, `.mkv`, `.webm` | ✅ |
| Text/Code | `.txt`, `.md`, `.py`, `.js`, `.json`, `.ipynb` | ✅ |

## 🎯 Command Options

```
python rename_files.py DIRECTORY [OPTIONS]

Required:
  DIRECTORY              Directory containing files to rename

Optional:
  --model MODEL         Ollama model (default: llava:latest)
  --ollama-url URL      Ollama server URL
  --execute             Actually rename (default: dry-run)
  --dpi DPI             PDF rendering quality (default: 150)
  --case STYLE          Casing style (default: snake)
                        Choices: snake, kebab, camel, pascal, lower, title
```

## 📚 Documentation

- **README.md** - Complete documentation
- **QUICKSTART.md** - Quick start guide
- **CASING_GUIDE.md** - Detailed guide to casing styles
- **EXAMPLES.md** - Real-world usage examples
- **requirements.txt** - Python dependencies

## 🔧 Technical Details

### Casing Implementation
New `apply_casing()` function handles all casing transformations:
- Normalizes input text
- Applies selected style
- Preserves word boundaries
- Handles edge cases

### Office Document Processing
- **Text extraction**: Primary method using python-docx/python-pptx
- **Visual analysis**: Optional with LibreOffice (converts to PDF → image)
- **Fallback**: Graceful degradation if libraries unavailable

### File Processing Flow
```
1. Scan directory for supported files
2. For each file:
   - Determine file type
   - Extract content (text or visual)
   - Send to Ollama model
   - Generate descriptive name
   - Apply casing style
   - Sanitize filename
3. Preview changes (dry-run) or apply (--execute)
```

## 🎨 Example Outputs

### snake_case (Python convention)
```
the_logic_of_sense_by_gilles_deleuze.pdf
python_week04_args_kwargs_class.ipynb
smart_home_device_class_example.py
```

### kebab-case (Web-friendly)
```
the-logic-of-sense-by-gilles-deleuze.pdf
python-week04-args-kwargs-class.ipynb
smart-home-device-class-example.py
```

### Title Case (Professional)
```
The Logic Of Sense By Gilles Deleuze.pdf
Python Week04 Args Kwargs Class.ipynb
Smart Home Device Class Example.py
```

## 🧪 Testing

Test casing styles:
```bash
python test_casing.py
```

Test on your data:
```bash
# Try different models
python rename_files.py data/ --model llama3.2-vision:latest
python rename_files.py data/ --model qwen2.5vl:latest
python rename_files.py data/ --model riven/smolvlm:latest

# Try different cases
python rename_files.py data/ --case snake
python rename_files.py data/ --case kebab
python rename_files.py data/ --case title
```

## 🔄 Migration from Previous Version

If you used the old version, the new version is **backward compatible**:
- Default casing is still `snake_case`
- All previous file types still supported
- New file types added (DOCX, PPTX)
- New option `--case` is optional

Your old commands will work exactly the same:
```bash
# Old command (still works)
python rename_files.py data/ --execute

# New capabilities (optional)
python rename_files.py data/ --case kebab --execute
```

## 💡 Pro Tips

1. **Preview first**: Always run without `--execute` first
2. **Try styles**: Test different casing styles before committing
3. **Model selection**: Use fast models for testing, accurate models for final
4. **Batch by type**: Process different directories with appropriate styles
5. **Quality matters**: Use `--dpi 300` for important documents

## 🐛 Known Limitations

- Videos require ffmpeg
- DOCX/PPTX visual analysis requires LibreOffice
- Ollama must be running
- Vision model must be installed
- File names limited to 100 characters (configurable)

## 📝 Files Modified/Created

New files:
- `requirements.txt` - Python dependencies
- `CASING_GUIDE.md` - Casing styles documentation
- `EXAMPLES.md` - Usage examples
- `FEATURES.md` - This file
- `test_casing.py` - Casing test script

Modified files:
- `rename_files.py` - Added casing + DOCX/PPTX support
- `README.md` - Updated documentation
- `setup.sh` - Added new dependencies

## 🙏 Credits

Built with:
- Ollama - Vision language models
- PyMuPDF - PDF rendering
- python-docx - Word document processing
- python-pptx - PowerPoint processing
- ffmpeg - Video frame extraction
- LibreOffice - Office document conversion
