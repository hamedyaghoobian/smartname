#!/bin/bash
# Quick setup script for SmartName

echo "==================================="
echo "SmartName Setup"
echo "==================================="
echo ""

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "❌ Ollama is not installed"
    echo ""
    echo "Please install Ollama:"
    echo "1. Visit: https://ollama.ai"
    echo "2. Download and install for macOS"
    echo "3. Run this script again"
    exit 1
else
    echo "✓ Ollama is installed"
fi

# Check if Ollama is running
if ! curl -s http://127.0.0.1:11434/api/tags > /dev/null 2>&1; then
    echo "❌ Ollama is not running"
    echo ""
    echo "Please start Ollama:"
    echo "- Open the Ollama app from Applications"
    echo "- Or run: ollama serve"
    exit 1
else
    echo "✓ Ollama is running"
fi

# Check for llava model
if ollama list | grep -q "llava"; then
    echo "✓ llava model is installed"
else
    echo "⚠ llava model not found"
    echo ""
    echo "Downloading llava model (this may take a few minutes)..."
    ollama pull llava:latest
    
    if [ $? -eq 0 ]; then
        echo "✓ llava model installed"
    else
        echo "❌ Failed to download llava model"
        exit 1
    fi
fi

# Check Python dependencies
echo ""
echo "Checking Python dependencies..."

if python -c "import fitz" 2> /dev/null; then
    echo "✓ PyMuPDF is installed"
else
    echo "⚠ PyMuPDF not found, installing..."
    pip install pymupdf
fi

if python -c "import requests" 2> /dev/null; then
    echo "✓ requests is installed"
else
    echo "⚠ requests not found, installing..."
    pip install requests
fi

if python -c "import docx" 2> /dev/null; then
    echo "✓ python-docx is installed"
else
    echo "⚠ python-docx not found, installing..."
    pip install python-docx
fi

if python -c "import pptx" 2> /dev/null; then
    echo "✓ python-pptx is installed"
else
    echo "⚠ python-pptx not found, installing..."
    pip install python-pptx
fi

# Check for ffmpeg (optional)
if command -v ffmpeg &> /dev/null; then
    echo "✓ ffmpeg is installed (video support enabled)"
else
    echo "⚠ ffmpeg not found (video support disabled)"
    echo "  To enable video support: brew install ffmpeg"
fi

# Check for LibreOffice (optional)
if command -v soffice &> /dev/null; then
    echo "✓ LibreOffice is installed (DOCX/PPTX visual analysis enabled)"
else
    echo "⚠ LibreOffice not found (DOCX/PPTX will use text extraction only)"
    echo "  To enable visual analysis: brew install libreoffice"
fi

echo ""
echo "==================================="
echo "Setup Complete!"
echo "==================================="
echo ""
echo "Try it out:"
echo "  python rename_files.py data/          # Dry run"
echo "  python rename_files.py data/ --execute  # Actually rename"
echo ""
