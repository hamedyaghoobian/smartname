# SmartName v2.0 - What's New

## 🎉 Major Updates

### 1. Office Document Support (NEW!)

#### DOCX Files
- Text extraction from Word documents
- Optional visual analysis with LibreOffice
- Handles complex formatting and tables

```bash
python rename_files.py documents/ --execute

Before: research-paper-final-v3.docx
After:  large_language_models_and_high_agency_user_interactions.docx
```

#### PPTX Files
- Text extraction from PowerPoint presentations
- Analyzes slides, titles, and content
- Optional visual rendering for better accuracy

```bash
python rename_files.py presentations/ --execute

Before: presentation-Q4-2024.pptx
After:  quarterly_business_review_revenue_growth.pptx
```

### 2. Flexible Casing Styles (NEW!)

Choose from **6 different naming conventions**:

```bash
# Traditional Python style
--case snake
→ my_awesome_file.txt

# Modern web style
--case kebab
→ my-awesome-file.txt

# JavaScript style
--case camel
→ myAwesomeFile.txt

# Component style
--case pascal
→ MyAwesomeFile.txt

# Casual/readable
--case lower
→ my awesome file.txt

# Professional/formal
--case title
→ My Awesome File.txt
```

### 3. Enhanced Model Support

Now tested with multiple Ollama models:
- ✅ llama3.2-vision:latest (balanced)
- ✅ qwen2.5vl:latest (accurate)
- ✅ riven/smolvlm:latest (fast)
- ✅ benhaotang/Nanonets-OCR-s:latest (OCR-focused)
- ✅ llava:latest (classic)

## 📊 Before & After Examples

### Example 1: Academic Paper (DOCX)
```bash
python rename_files.py papers/ --case title --execute
```

**Before:**
```
jhtr-review-assignment-8315-Research+Article-33006.docx
```

**After:**
```
Large Language Models And High Agency User Interactions.docx
```

### Example 2: Code Files (Python)
```bash
python rename_files.py scripts/ --case snake --execute
```

**Before:**
```
W04.ipynb
smart-home.py
```

**After:**
```
python_week04_args_kwargs_class.ipynb
smart_home_device_class_example.py
```

### Example 3: Web Project (React)
```bash
python rename_files.py components/ --case pascal --execute
```

**Before:**
```
component1.jsx
component2.jsx
```

**After:**
```
UserProfileCard.jsx
NavigationMenu.jsx
```

## 🆚 Version Comparison

| Feature | v1.0 | v2.0 |
|---------|------|------|
| Images | ✅ | ✅ |
| PDFs | ✅ | ✅ |
| Videos | ✅ | ✅ |
| Text/Code | ✅ | ✅ |
| **DOCX** | ❌ | ✅ NEW |
| **PPTX** | ❌ | ✅ NEW |
| **Casing Styles** | 1 (snake) | 6 (all styles) NEW |
| **Model Choice** | Limited | Full support |
| Dry-run | ✅ | ✅ |
| Collision Prevention | ✅ | ✅ |

## 🚀 New Use Cases

### 1. Academic Research Workflow
```bash
# Organize research papers with formal naming
python rename_files.py ~/Research/ --case title --dpi 300 --execute

# Result:
# paper1.pdf → The Impact Of Machine Learning On Healthcare.pdf
# draft.docx → Quantum Computing Applications In Cryptography.docx
```

### 2. Software Development
```bash
# Python projects
python rename_files.py ~/Projects/backend/ --case snake --execute

# JavaScript projects
python rename_files.py ~/Projects/frontend/ --case camel --execute

# React components
python rename_files.py ~/Projects/components/ --case pascal --execute
```

### 3. Content Creation
```bash
# Blog images
python rename_files.py ~/Blog/images/ --case kebab --execute

# Presentations
python rename_files.py ~/Presentations/ --case title --execute
```

### 4. Personal Organization
```bash
# Photos with descriptive names
python rename_files.py ~/Photos/2024/ --case kebab --execute

# Documents with readable names
python rename_files.py ~/Documents/ --case title --execute
```

## 📚 New Documentation

Added comprehensive guides:

1. **CASING_GUIDE.md** - Complete guide to all 6 casing styles
2. **CASING_COMPARISON.md** - Side-by-side style comparison
3. **EXAMPLES.md** - Real-world usage examples
4. **FEATURES.md** - Technical feature summary
5. **IMPLEMENTATION_SUMMARY.md** - What was built

## 🔧 Technical Improvements

### Better File Processing
- DOCX text extraction with python-docx
- PPTX slide analysis with python-pptx
- Optional LibreOffice integration for visual analysis
- Improved error handling

### Casing Implementation
- New `apply_casing()` function
- Supports 6 different styles
- Intelligent word boundary detection
- Preserves readability

### Enhanced CLI
- Added `--case` option with 6 choices
- Better help text
- Improved output formatting
- Shows case style in summary

## 📦 Installation Updates

### New Requirements
```bash
pip install pymupdf requests python-docx python-pptx
```

### Optional Dependencies
```bash
brew install ffmpeg        # Video support
brew install libreoffice   # DOCX/PPTX visual analysis
```

### Quick Setup
```bash
./setup.sh  # Automatically checks and installs everything
```

## 💡 Pro Tips

### Tip 1: Preview Multiple Styles
```bash
# Try before you commit
python rename_files.py data/ --case snake
python rename_files.py data/ --case kebab
python rename_files.py data/ --case title

# Pick your favorite
python rename_files.py data/ --case kebab --execute
```

### Tip 2: Match Your Project
```bash
# Python project? Use snake_case
python rename_files.py python-project/ --case snake --execute

# React app? Use PascalCase
python rename_files.py react-app/components/ --case pascal --execute

# Website? Use kebab-case
python rename_files.py website/assets/ --case kebab --execute
```

### Tip 3: Organize by Context
```bash
# Technical files: no spaces
python rename_files.py code/ --case snake --execute

# Documents: readable with spaces
python rename_files.py documents/ --case title --execute
```

## 🎯 Migration Guide

### If You're Upgrading

**Good news**: v2.0 is fully backward compatible!

```bash
# Your old commands still work exactly the same
python rename_files.py data/ --execute

# Just with new options available
python rename_files.py data/ --case kebab --execute
```

### New File Types

If you have DOCX or PPTX files:
```bash
# Install new dependencies
pip install python-docx python-pptx

# Then run normally
python rename_files.py documents/ --execute
```

## 🐛 Bug Fixes & Improvements

- Better filename sanitization
- Improved error messages
- Enhanced collision detection
- More robust text extraction
- Better handling of special characters

## 🙏 Thanks

Built with:
- Ollama (AI models)
- PyMuPDF (PDF processing)
- python-docx (Word documents)
- python-pptx (PowerPoint)
- ffmpeg (video frames)
- LibreOffice (document conversion)

## 🔜 What's Next?

Possible future features:
- XLSX (Excel) support
- Batch processing with different rules
- Custom casing patterns
- GUI interface
- API server mode
- More AI model integrations

## 📝 Changelog

### v2.0 (2024-10-26)
- ✨ Added DOCX support
- ✨ Added PPTX support
- ✨ Added 6 casing styles
- ✨ Enhanced model support
- 📚 Comprehensive documentation
- 🐛 Various bug fixes

### v1.0 (Initial Release)
- Basic file renaming
- Image, PDF, video, text support
- snake_case naming
- Dry-run mode

---

**Enjoy organizing your files with intelligent, meaningful names!** 🎉
