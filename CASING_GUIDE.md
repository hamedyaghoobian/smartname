# Casing Styles Guide

## Overview

SmartName supports 6 different casing styles for your renamed files. Choose the style that matches your project's naming conventions or personal preference.

## Available Styles

### 1. snake_case (default)
```bash
python rename_files.py data/ --case snake
```
**Result**: `the_logic_of_sense_by_gilles_deleuze.pdf`

- All lowercase
- Words separated by underscores
- Most common for Python files, database names
- Works well with all file systems

### 2. kebab-case
```bash
python rename_files.py data/ --case kebab
```
**Result**: `the-logic-of-sense-by-gilles-deleuze.pdf`

- All lowercase
- Words separated by hyphens
- Popular for URLs, web projects
- Good for readability

### 3. camelCase
```bash
python rename_files.py data/ --case camel
```
**Result**: `theLogicOfSenseByGillesDeleuze.pdf`

- First word lowercase, rest capitalized
- No separators
- Common in JavaScript, Java
- Compact but still readable

### 4. PascalCase
```bash
python rename_files.py data/ --case pascal
```
**Result**: `TheLogicOfSenseByGillesDeleuze.pdf`

- All words capitalized
- No separators
- Common for classes, components
- Professional looking

### 5. lowercase with spaces
```bash
python rename_files.py data/ --case lower
```
**Result**: `the logic of sense by gilles deleuze.pdf`

- All lowercase
- Natural spaces between words
- Human-readable
- May cause issues with some tools

### 6. Title Case With Spaces
```bash
python rename_files.py data/ --case title
```
**Result**: `The Logic Of Sense By Gilles Deleuze.pdf`

- Each word capitalized
- Natural spaces between words
- Very readable, formal
- May cause issues with some tools

## Practical Examples

### Academic Papers
```bash
# Formal, professional
python rename_files.py papers/ --case title --execute

# Output:
# paper1.pdf → The Impact Of Machine Learning On Healthcare.pdf
# paper2.pdf → Quantum Computing Applications In Cryptography.pdf
```

### Code Projects
```bash
# Standard Python convention
python rename_files.py scripts/ --case snake --execute

# Output:
# script1.py → data_analysis_with_pandas.py
# script2.py → web_scraper_for_news_sites.py
```

### Web Projects
```bash
# URL-friendly
python rename_files.py images/ --case kebab --execute

# Output:
# img1.jpg → beautiful-sunset-over-ocean.jpg
# img2.jpg → modern-office-workspace-setup.jpg
```

### React/JavaScript Components
```bash
# Component naming
python rename_files.py components/ --case pascal --execute

# Output:
# component1.jsx → UserProfileCard.jsx
# component2.jsx → NavigationMenu.jsx
```

## Combining with Other Options

### Model + Casing
```bash
# Use a specific model with kebab-case
python rename_files.py data/ --model qwen2.5vl:latest --case kebab --execute
```

### High-Quality PDF + Title Case
```bash
# Better PDF quality with professional casing
python rename_files.py documents/ --dpi 300 --case title --execute
```

### Dry Run with Different Styles
Try different styles before committing:
```bash
# Preview snake_case
python rename_files.py data/ --case snake

# Preview kebab-case
python rename_files.py data/ --case kebab

# Preview Title Case
python rename_files.py data/ --case title

# Then execute your favorite
python rename_files.py data/ --case kebab --execute
```

## Best Practices

### Choose based on context:

- **Python projects**: `--case snake`
- **JavaScript/TypeScript**: `--case camel` or `--case pascal`
- **Web assets**: `--case kebab`
- **Academic/Professional**: `--case title`
- **Database files**: `--case snake`
- **Documentation**: `--case kebab` or `--case title`

### Avoid spaces for:
- Command-line tools
- Scripts and automation
- Cross-platform compatibility

Use `snake`, `kebab`, `camel`, or `pascal` for technical files.

### Use spaces for:
- Documents meant for sharing
- Files for non-technical users
- Personal organization

Use `lower` or `title` for human-readable names.

## Quick Reference

| Style | Example | Best For |
|-------|---------|----------|
| `snake` | `my_awesome_file.txt` | Python, databases, technical |
| `kebab` | `my-awesome-file.txt` | Web, URLs, modern projects |
| `camel` | `myAwesomeFile.txt` | JavaScript variables |
| `pascal` | `MyAwesomeFile.txt` | Classes, components |
| `lower` | `my awesome file.txt` | Personal, casual |
| `title` | `My Awesome File.txt` | Professional, formal |
