# Project 03: SmartName – AI-Powered File Renamer

**Course:** Human-AI Interaction
**Group Size:** 2–3 students

## 🎯 Assignment Overview

Design and build **SmartName**, an AI-assisted command-line tool that helps users organize "mixed media" files. Maintaining tidy file systems can be challenging, especially for users who benefit from explicit structure and reduced cognitive load. Files often arrive with opaque names (`IMG_8342.mov`, `ScreenShot 2025-10-12.png`, `Final-v3-draft.docx`).

Your task is to create a system that:

1.  Analyzes heterogeneous file formats (images, videos, PDFs, code, Office documents).
2.  Uses local multimodal AI (Ollama) to understand the *content* of each file.
3.  Proposes multiple, context-aware naming suggestions.
4.  Provides a **Casing & Preference Engine** that allows users to select their preferred file naming convention (e.g., `snake_case`, `Title Case`, `kebab-case`).

This assignment explores how to build inclusive, preference-aware tools that put the user in control, reduce executive function demands, and use AI to provide structure rather than ambiguity.

### Learning Objectives

  - Apply multimodal AI techniques (vision, language, text extraction) to a practical organization task.
  - Design inclusive human-AI interfaces that respect user preferences and reduce cognitive load.
  - Engineer a robust data pipeline that can route and process heterogeneous file formats.
  - Implement a "preference-aware" system (the Casing Engine) as a core feature of the UI.
  - Reflect on the ethical and privacy benefits of using local AI models for personal files.

## 📚 Background & Context

### Why a Preference-Aware Renamer?

For many users, especially those in neurodiverse populations who rely on explicit structure, a cluttered file system is a significant source of friction. The core problem isn't just the renaming; it's the *cognitive load* of deciding on a name and the *motor load* of applying it consistently.

**Common Pain Points:**

  * **Mixed Media Chaos:** A single project folder can contain PDFs, scanned notes, Word docs, Python scripts, and images, all with different naming conventions.
  * **Unreadable Sources:** Many files are "opaque." You can't tell what `IMG_4501.jpg` or `W04.ipynb` is without opening it.
  * **Scanned vs. Text:** A PDF might be a text-searchable document or a "scanned" image. Your tool must handle both.
  * **Rigid Conventions:** A developer might need `snake_case` for code, while a researcher needs `Title Case` for papers, and a web designer needs `kebab-case` for assets. A one-size-fits-all tool fails everyone.

SmartName should act as an intelligent "teammate" that does the heavy lifting of analysis and suggestion, but leaves the final choice of *style* and *content* to the user.

### Technology Stack

You will orchestrate several components:

  * **Ollama:** Local LLM/VLM host (macOS/Linux/Windows) for privacy-friendly inference.
  * **Multimodal Models:** e.g., `llama3.2-vision`, `gemma3`, or `mistral-small3.2`.
  * **Python Tooling:**
      * `requests` (for Ollama API)
      * `argparse` (for the CLI UI)
      * `PyMuPDF` (for PDF analysis)
      * `python-docx` & `python-pptx` (for Office file text extraction)
      * `ffmpeg` (for video frame extraction)

## 🗂️ Sample Data Requirement

Before you begin, you **must** create a test folder (e.g., `data/`) containing at least one of each of the following. Your tool will be graded on its ability to handle this mixed folder:

  * **Image:** (`.png`, `.jpg`)
  * **Text-based PDF:** A searchable PDF you can copy/paste from.
  * **Scanned PDF:** A PDF that is just an image of a document.
  * **Office Files:** (`.docx`, `.pptx`)
  * **Code File:** (`.py`, `.js`)
  * **Markdown File:** (`.md`)
  * **Jupyter Notebook:** (`.ipynb`)
  * **Video File:** (`.mp4`, `.mov`) (optional, for bonus)

## 🚀 Starter Architecture (Suggested)

We recommend a single-script (`rename_files.py`) approach managed by a robust CLI.

```
smartname/
├── rename_files.py     # Main script with all logic
│   ├── (CLI) main()
│   ├── (API) call_ollama_vision()
│   ├── (API) call_ollama_text()
│   ├── (Extractors) extract_pdf_image()
│   ├── (Extractors) extract_docx_content()
│   ├── (Extractors) extract_pptx_content()
│   ├── (Extractors) extract_video_frame()
│   ├── (Extractors) read_text_snippet()
│   ├── (Routing) generate_filename_for_file()
│   ├── (UX) apply_casing()
│   └── (UX) sanitize_filename()
│
├── data/
│   ├── report-draft.docx
│   ├── class-notes.md
│   ├── scanned-receipt.pdf
│   ├── academic-paper.pdf
│   ├── my_script.py
│   └── photo.jpg
│
└── README.md
```

## 📝 Assignment Tasks

### Part 1: Foundations & Core Pipeline (30 pts)

1.  **Environment Setup (10 pts):**
      * Set up your Python environment and install all required dependencies (`PyMuPDF`, `python-docx`, `python-pptx`, `requests`).
      * Install Ollama and pull at least one vision model (e.g., `llama3.2-vision`).
      * Demonstrate a successful API call to Ollama from your Python script.
2.  **CLI Skeleton (10 pts):**
      * Using `argparse`, create your main CLI interface. It must support:
          * A `directory` argument (e.g., `python rename_files.py data/`).
          * An `--execute` flag. The tool must default to a "dry run" (preview) mode for safety.
          * A `--model` argument to specify the Ollama model.
3.  **Basic File Routing (10 pts):**
      * Implement the core `generate_filename_for_file()` router.
      * Successfully handle basic types:
          * **Images (`.png`, `.jpg`):** Base64-encode and send to a VLM.
          * **Text/Code (`.txt`, `.md`, `.py`):** Read a snippet of text and send to a text/VLM model.

### Part 2: Advanced Ingest & Casing Engine (40 pts)

1.  **Robust PDF & Office Handling (20 pts):**
      * **PDFs:** Your tool must handle both types.
          * **Text-based:** *Attempt* to extract text first.
          * **Scanned:** If text extraction fails or is minimal, fall back to rendering the first page as an image (using `PyMuPDF`/`fitz`) and send that image to the VLM.
      * **Office (`.docx`, `.pptx`):** Use `python-docx` and `python-pptx` to extract text content from the files. Send this text to the LLM for analysis.
2.  **The Casing & Preference Engine (20 pts):**
      * This is the core HAI feature. Implement a `--case` argument in your CLI.
      * Write an `apply_casing()` function that supports all 6 of the following styles:
        1.  `snake_case` (default)
        2.  `kebab-case`
        3.  `camelCase`
        4.  `PascalCase`
        5.  `lowercase with spaces`
        6.  `Title Case With Spaces`
      * Ensure all final suggestions are run through this casing engine based on the user's choice.

### Part 3: Evaluation & Reflection (30 pts)

1.  **User Evaluation (15 pts):**
      * Conduct a brief user study with **two** participants (classmates, friends, etc.).
      * Give them your test folder and your script. Ask them to organize the folder using your tool.
      * Collect qualitative feedback:
          * Did they trust the AI's suggestions?
          * Was the "dry run" mode helpful?
          * Which casing style did they prefer and why?
          * What was confusing? What was empowering?
2.  **Reflection & Documentation (15 pts):**
      * Write a `README.md` for your project that explains *how* to use it, including all CLI options.
      * Create a `CASING_GUIDE.md` that explains the 6 casing styles and provides examples for each (similar to your provided files).
      * Write a short reflection (2-3 paragraphs) on the privacy implications of this tool and why using local Ollama models is a critical *human-centered* design choice.

## 🎁 Bonus Opportunities (Up to +10 pts)

  * **Video Support (+5 pts):** Install `ffmpeg`. Use `subprocess` to call `ffmpeg` to extract a single frame from video files (`.mp4`, `.mov`) and send it to the VLM for analysis.
  * **Visual Office Analysis (+5 pts):** Implement the advanced visual analysis for `.docx`/`.pptx`. Use `subprocess` to call `libreoffice --headless --convert-to pdf` to turn the Office file into a PDF, then use your existing PDF-to-image pipeline. This is complex but provides great results for visual-heavy slides.

## 📦 Deliverables

  - **Code:** Your complete `rename_files.py` script.
  - **Documentation:**
      - `README.md` (explaining setup and usage)
      - `CASING_GUIDE.md` (explaining the 6 casing styles)
  - **Test Data:** A `.zip` of your mixed-media test folder.
  - **Evaluation Report (PDF/MD):** A brief write-up summarizing your experiments, thoughts, and your final reflections on the project.
  - **Demo:** A short video (or `EXAMPLES.md` file with screenshots) showing your tool renaming every file in your test folder using at least two different casing styles.

## 💡 Guiding Tips

  * **Start Simple:** Get one file type (e.g., `.png`) working end-to-end first. Get the CLI, the API call, the sanitization, and the casing all working for just that one file type before adding more.
  * **Safety First:** The "dry run" is the most important feature. Print your intended changes in a clear, table-like format. Test this thoroughly before you ever use `--execute`.
  * **How to Detect a Scanned PDF?** A simple heuristic: try to extract text from page 1 using `page.get_text()`. If the resulting text is empty or very short (e.g., \< 100 characters), it's a good bet it's a scanned image. In that case, fall back to the image-rendering path.
  * **Prompting is Key:** Your prompts to Ollama should be very specific. Don't just ask "what is this?" Ask: `"Analyze this file's content and suggest a concise, 5-8 word, descriptive filename. Use underscores instead of spaces. Do not include the file extension. Respond with *only* the filename and nothing else."`
  * **Dependencies are Tricky:** `ffmpeg` and `libreoffice` are system-level dependencies, not Python packages. Make them *optional* features (or bonus) so your core tool works without them. The text-based extraction for `.docx` and `.pptx` is the reliable, dependency-light path.