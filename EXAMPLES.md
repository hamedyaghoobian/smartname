# Complete Feature Demo

## What's New

✨ **Added in latest version:**

1. **DOCX Support** - Rename Word documents based on content
2. **PPTX Support** - Rename PowerPoint presentations based on content
3. **6 Casing Styles** - Choose your preferred naming convention
4. **Better Office Integration** - Visual analysis with LibreOffice (optional)

## Full Feature Test

### 1. Install All Dependencies

```bash
# Core dependencies
pip install pymupdf requests python-docx python-pptx

# Optional: Video support
brew install ffmpeg

# Optional: Office visual analysis
brew install libreoffice
```

### 2. Test Different Casing Styles

**snake_case (default)**
```bash
python rename_files.py data/ --model llama3.2-vision:latest --case snake
```
Result: `the_logic_of_sense_by_gilles_deleuze.pdf`

**kebab-case**
```bash
python rename_files.py data/ --model llama3.2-vision:latest --case kebab
```
Result: `the-logic-of-sense-by-gilles-deleuze.pdf`

**Title Case**
```bash
python rename_files.py data/ --model llama3.2-vision:latest --case title
```
Result: `The Logic Of Sense By Gilles Deleuze.pdf`

### 3. Supported File Types

Now handles **10+ file formats**:

| Category | Extensions | Analysis Method |
|----------|------------|-----------------|
| Images | `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.webp` | Direct vision model |
| Documents | `.pdf` | First page to image |
| Office | `.docx`, `.pptx` | Text extraction or visual |
| Video | `.mov`, `.mp4`, `.avi`, `.mkv`, `.webm` | Frame extraction |
| Text/Code | `.txt`, `.md`, `.py`, `.js`, `.json`, `.ipynb` | Content analysis |

### 4. Office Document Examples

**DOCX - Word Documents**
```bash
python rename_files.py docs/ --case title --execute
```

Before: `research-paper-draft-final-v3.docx`
After: `Large Language Models And High Agency User Interactions.docx`

**PPTX - PowerPoint**
```bash
python rename_files.py presentations/ --case kebab --execute
```

Before: `presentation-Q4-2024.pptx`
After: `quarterly-business-review-revenue-growth.pptx`

### 5. Mix Multiple Options

**Academic Papers (High Quality + Title Case)**
```bash
python rename_files.py papers/ \
  --model qwen2.5vl:latest \
  --dpi 300 \
  --case title \
  --execute
```

**Code Files (Fast Model + snake_case)**
```bash
python rename_files.py scripts/ \
  --model riven/smolvlm:latest \
  --case snake \
  --execute
```

**Web Assets (kebab-case)**
```bash
python rename_files.py images/ \
  --model llama3.2-vision:latest \
  --case kebab \
  --execute
```

### 6. Batch Processing Different Folders

```bash
# Process multiple directories with different styles
python rename_files.py ~/Documents/Papers/ --case title --execute
python rename_files.py ~/Projects/scripts/ --case snake --execute
python rename_files.py ~/Pictures/photos/ --case kebab --execute
python rename_files.py ~/Code/components/ --case pascal --execute
```

## Real-World Example Output

```
Found 6 files to process
Model: llama3.2-vision:latest
Case style: title
Mode: RENAMING

Analyzing: paper1.pdf
  Suggested: Deep Learning For Medical Image Analysis.pdf

Analyzing: research-doc.docx
  Suggested: Large Language Models And High Agency User Interactions.docx

Analyzing: presentation.pptx
  Suggested: Quarterly Business Review Revenue Growth.pptx

Analyzing: IMG_1234.jpg
  Suggested: Beautiful Sunset Over Mountain Lake.jpg

Analyzing: video_clip.mov
  Suggested: Family Vacation Beach Holiday Fun.mov

Analyzing: notebook.ipynb
  Suggested: Data Analysis With Pandas And Matplotlib.ipynb

============================================================
RENAME SUMMARY
============================================================

paper1.pdf
  → Deep Learning For Medical Image Analysis.pdf
  ✓ Renamed

research-doc.docx
  → Large Language Models And High Agency User Interactions.docx
  ✓ Renamed

presentation.pptx
  → Quarterly Business Review Revenue Growth.pptx
  ✓ Renamed

IMG_1234.jpg
  → Beautiful Sunset Over Mountain Lake.jpg
  ✓ Renamed

video_clip.mov
  → Family Vacation Beach Holiday Fun.mov
  ✓ Renamed

notebook.ipynb
  → Data Analysis With Pandas And Matplotlib.ipynb
  ✓ Renamed
```

## Tips & Tricks

### 1. Preview Multiple Styles
```bash
# Try different styles without renaming
python rename_files.py data/ --case snake   # Preview 1
python rename_files.py data/ --case kebab   # Preview 2
python rename_files.py data/ --case title   # Preview 3
# Then execute your favorite
python rename_files.py data/ --case kebab --execute
```

### 2. Model Selection
```bash
# Fast & lightweight (good for testing)
--model riven/smolvlm:latest

# Balanced (recommended)
--model llama3.2-vision:latest

# High accuracy (slow but thorough)
--model qwen2.5vl:latest

# OCR-focused (for text-heavy documents)
--model benhaotang/Nanonets-OCR-s:latest
```

### 3. Organize by Project Type

Python projects:
```bash
python rename_files.py . --case snake --execute
```

Web/React projects:
```bash
python rename_files.py src/ --case camel --execute
```

Documentation:
```bash
python rename_files.py docs/ --case title --execute
```

### 4. Quality vs Speed

Fast (low DPI, small model):
```bash
python rename_files.py data/ --dpi 100 --model riven/smolvlm:latest --execute
```

Balanced (default):
```bash
python rename_files.py data/ --execute
```

High quality (high DPI, large model):
```bash
python rename_files.py data/ --dpi 300 --model qwen2.5vl:latest --execute
```

## Troubleshooting

**DOCX not working?**
```bash
pip install python-docx
```

**PPTX not working?**
```bash
pip install python-pptx
```

**Video not working?**
```bash
brew install ffmpeg
```

**Want visual DOCX/PPTX analysis?**
```bash
brew install libreoffice
```

## See Also

- [README.md](README.md) - Main documentation
- [QUICKSTART.md](QUICKSTART.md) - Quick start guide
- [CASING_GUIDE.md](CASING_GUIDE.md) - Detailed casing style guide
