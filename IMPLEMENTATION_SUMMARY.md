# 🎉 SmartName - Complete Implementation

## What Was Built

A powerful file renaming tool that uses Ollama vision language models to generate intelligent, content-based filenames.

## ✨ Key Features

### 1. **Multi-Format Support**
- ✅ Images (PNG, JPG, GIF, BMP, WebP)
- ✅ PDFs 
- ✅ **NEW:** Word Documents (DOCX)
- ✅ **NEW:** PowerPoint (PPTX)
- ✅ Videos (MOV, MP4, AVI, MKV, WebM)
- ✅ Text/Code (TXT, MD, PY, JS, JSON, IPYNB)

### 2. **Flexible Casing Styles**
Choose from 6 different naming conventions:

| Style | Example | Use Case |
|-------|---------|----------|
| **snake_case** | `my_awesome_file.txt` | Python, technical |
| **kebab-case** | `my-awesome-file.txt` | Web, URLs |
| **camelCase** | `myAwesomeFile.txt` | JavaScript |
| **PascalCase** | `MyAwesomeFile.txt` | Classes, components |
| **lowercase** | `my awesome file.txt` | Personal |
| **Title Case** | `My Awesome File.txt` | Professional |

### 3. **Smart & Safe**
- Dry-run by default (preview before renaming)
- Collision prevention (adds `_1`, `_2` if needed)
- Multiple Ollama model support
- Configurable quality settings

## 🚀 Quick Start

### Installation
```bash
# Install dependencies
pip install pymupdf requests python-docx python-pptx

# Optional
brew install ffmpeg libreoffice
```

### Basic Usage
```bash
# Preview renames (safe)
python rename_files.py data/

# Actually rename
python rename_files.py data/ --execute

# With different casing
python rename_files.py data/ --case kebab --execute
python rename_files.py data/ --case title --execute
python rename_files.py data/ --case pascal --execute
```

## 📊 Real Results from Your Data

### Example 1: snake_case (default)
```
jhtr-review-assignment-8315-Research+Article-33006.docx
→ large_language_models_and_high_agency_user_interactions.docx

The_Logic_of_Sense_by_Gilles_Deleuze.pdf
→ the_logic_of_sense_by_gilles_deleuze.pdf
```

### Example 2: kebab-case
```
smart_home_device_class_example.py
→ smart-home-device-management-example.py

python_week04_args_kwargs_class.ipynb
→ week04-args-kwargs-class-example.ipynb
```

### Example 3: Title Case
```
jhtr-review-assignment-8315-Research+Article-33006.docx
→ Large Language Models And High Agency User Interactions.docx

smart_home_device_class_example.py
→ Smart Home Device Class Example.py
```

### Example 4: PascalCase
```
smart_home_device_class_example.py
→ SmartHomeDeviceClassExample.py

python_week04_args_kwargs_class.ipynb
→ PythonFunctionArgsKwargsExample.ipynb
```

## 🎯 Use Cases

### Academic Research
```bash
python rename_files.py ~/Papers/ --case title --dpi 300 --execute
```
Result: `The Impact Of Machine Learning On Healthcare.pdf`

### Python Projects
```bash
python rename_files.py ~/Code/ --case snake --execute
```
Result: `data_analysis_with_pandas.py`

### Web Development
```bash
python rename_files.py ~/Assets/ --case kebab --execute
```
Result: `user-profile-card-component.jsx`

### React Components
```bash
python rename_files.py ~/Components/ --case pascal --execute
```
Result: `NavigationMenuBar.jsx`

## 📁 Project Structure

```
smartname/
├── rename_files.py           # Main script
├── ollama_ocr_pdf.py         # PDF OCR tool
├── test_casing.py            # Test casing styles
├── setup.sh                  # Setup script
├── requirements.txt          # Dependencies
├── README.md                 # Main docs
├── QUICKSTART.md            # Quick guide
├── CASING_GUIDE.md          # Casing details
├── EXAMPLES.md              # Usage examples
├── FEATURES.md              # Feature summary
└── data/                    # Your test files
```

## 🔧 Available Options

```
python rename_files.py DIRECTORY [OPTIONS]

Required:
  DIRECTORY              Path to directory with files

Options:
  --model MODEL         Ollama model (default: llava:latest)
  --case STYLE          Casing style (default: snake)
                        Choices: snake, kebab, camel, pascal, lower, title
  --execute             Actually rename files (default: dry-run)
  --dpi DPI             PDF quality (default: 150)
  --ollama-url URL      Ollama server URL
```

## 🎓 Documentation

All documentation included:

1. **README.md** - Complete guide with installation and usage
2. **QUICKSTART.md** - Get started in 5 minutes
3. **CASING_GUIDE.md** - Detailed guide to all 6 casing styles
4. **EXAMPLES.md** - Real-world usage scenarios
5. **FEATURES.md** - Technical feature summary

## ✅ What Works

- ✅ All image formats
- ✅ PDF documents (visual analysis)
- ✅ **DOCX files (text extraction)**
- ✅ **PPTX files (text extraction)**
- ✅ Text and code files
- ✅ Jupyter notebooks
- ✅ **6 different casing styles**
- ✅ Multiple Ollama models
- ✅ Dry-run mode
- ✅ Collision prevention

## 🔜 Optional Enhancements

If you want even more features:

- Install `ffmpeg` for video support
- Install `libreoffice` for DOCX/PPTX visual analysis
- Use larger models for better accuracy
- Increase DPI for higher quality PDF analysis

## 🎯 Next Steps

1. **Test different casing styles:**
   ```bash
   python rename_files.py data/ --case snake
   python rename_files.py data/ --case kebab
   python rename_files.py data/ --case title
   ```

2. **Choose your favorite and execute:**
   ```bash
   python rename_files.py data/ --case kebab --execute
   ```

3. **Organize your entire file system:**
   ```bash
   python rename_files.py ~/Documents/ --case title --execute
   python rename_files.py ~/Code/ --case snake --execute
   python rename_files.py ~/Pictures/ --case kebab --execute
   ```

## 🙌 Success!

You now have a powerful, flexible file renaming tool that:
- Understands file content (not just metadata)
- Supports 10+ file formats
- Offers 6 different naming conventions
- Works with multiple AI models
- Protects you with dry-run mode
- Handles collisions gracefully

Enjoy organizing your files with intelligent, meaningful names! 🎉
