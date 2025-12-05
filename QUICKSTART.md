# Quick Start Guide

## Setup (First Time Only)

### 1. Install Ollama
```bash
# Download and install from https://ollama.ai
# Or use homebrew:
brew install ollama
```

### 2. Start Ollama
```bash
# Option A: Open Ollama app from Applications folder
# Option B: Run in terminal
ollama serve
```

### 3. Run Setup Script
```bash
./setup.sh
```

This will:
- Check if Ollama is running
- Download the llava model (~4GB)
- Install Python dependencies (pymupdf, requests)

## Usage

### Preview renames (Safe - No Changes)
```bash
python rename_files.py data/
```

This shows you what files would be renamed without actually changing anything.

### Actually rename files
```bash
python rename_files.py data/ --execute
```

## What's in the data folder?

Your `data/` folder currently contains:
- `IMG_3837.MOV` - A video file
- `W04.ipynb` - A Jupyter notebook
- `the-logic-of-sense.pdf` - A PDF document
- `the-logic-of-sense.txt` - A text file
- `smart-home.py` - A Python script

The script will analyze each file's content and suggest descriptive names like:
- Video → Based on visual content in the frame
- PDF → Based on title/content of first page
- Text/Code → Based on actual content

## Troubleshooting

### "Ollama is not installed"
Download from https://ollama.ai and install

### "Ollama is not running"
Start the Ollama app or run `ollama serve` in a terminal

### "llava model not found"
Run: `ollama pull llava:latest`

### "Could not extract video frame"
Install ffmpeg: `brew install ffmpeg`

## Advanced Options

### Use a different model
```bash
# Smaller, faster
python rename_files.py data/ --model llava:7b

# Larger, more accurate
python rename_files.py data/ --model llava:13b
```

### Higher quality PDF analysis
```bash
python rename_files.py data/ --dpi 300 --execute
```

## Example Output

```
Found 5 files to process
Model: llava:latest
Mode: DRY RUN

Analyzing: W04.ipynb
  Suggested: week_4_data_analysis_notebook.ipynb

Analyzing: the-logic-of-sense.pdf
  Suggested: deleuze_logic_of_sense_philosophy.pdf

Analyzing: IMG_3837.MOV
  Suggested: sunset_beach_waves_video.mov

============================================================
RENAME SUMMARY
============================================================

W04.ipynb
  → week_4_data_analysis_notebook.ipynb

the-logic-of-sense.pdf
  → deleuze_logic_of_sense_philosophy.pdf

IMG_3837.MOV
  → sunset_beach_waves_video.mov
============================================================
This was a DRY RUN. Use --execute to actually rename files.
============================================================
```
