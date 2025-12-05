from __future__ import annotations

import argparse
import base64
import json
import tempfile
from pathlib import Path
from typing import Iterable

import fitz  # PyMuPDF
import requests


def render_pdf_to_images(
    pdf_path: Path,
    output_dir: Path,
    dpi: int = 220,
    start_page: int | None = None,
    end_page: int | None = None,
    max_pages: int | None = None,
) -> list[Path]:
    """Render each page of the PDF to a PNG image and return their paths."""
    output_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    total = doc.page_count

    start_idx = 0 if start_page is None else max(0, start_page - 1)
    end_idx = total if end_page is None else min(total, end_page)

    image_paths: list[Path] = []
    zoom = dpi / 72.0
    matrix = fitz.Matrix(zoom, zoom)

    for page_number in range(start_idx, end_idx):
        if max_pages is not None and len(image_paths) >= max_pages:
            break
        page = doc.load_page(page_number)
        pix = page.get_pixmap(matrix=matrix)
        image_path = output_dir / f"page_{page_number + 1:04d}.png"
        pix.save(image_path)
        image_paths.append(image_path)

    doc.close()
    return image_paths


def encode_image_to_base64(image_path: Path) -> str:
    return base64.b64encode(image_path.read_bytes()).decode("utf-8")


def call_ollama_generate(
    model: str,
    prompt: str,
    images: Iterable[Path],
    ollama_url: str = "http://127.0.0.1:11434",
    format_json: bool = False,
) -> str:
    payload: dict[str, object] = {
        "model": model,
        "prompt": prompt,
        "images": [encode_image_to_base64(path) for path in images],
        "stream": False,
    }
    if format_json:
        payload["format"] = "json"

    response = requests.post(f"{ollama_url}/api/generate", json=payload, timeout=600)
    response.raise_for_status()
    data = response.json()

    if format_json and isinstance(data.get("response"), str):
        try:
            parsed = json.loads(data["response"])
        except json.JSONDecodeError:
            return data["response"].strip()
        return json.dumps(parsed, indent=2)

    return str(data.get("response", "")).strip()


def process_pdf_with_ollama(
    pdf_path: Path,
    output_text: Path,
    model: str,
    prompt_template: str,
    ollama_url: str,
    dpi: int,
    temp_dir: Path | None,
    start_page: int | None,
    end_page: int | None,
    max_pages: int | None,
) -> None:
    temp_root = temp_dir or Path(tempfile.gettempdir()) / "ollama_pdf"
    images_dir = temp_root / pdf_path.stem

    print(f"Rendering PDF pages to '{images_dir}' (dpi={dpi})...")
    image_paths = render_pdf_to_images(
        pdf_path,
        images_dir,
        dpi=dpi,
        start_page=start_page,
        end_page=end_page,
        max_pages=max_pages,
    )
    print(f"Rendered {len(image_paths)} pages.")

    output_text.parent.mkdir(parents=True, exist_ok=True)
    outputs: list[str] = []

    for idx, image_path in enumerate(image_paths, start=1):
        page_no = start_page + idx - 1 if start_page else idx
        page_prompt = prompt_template.format(page=page_no)
        print(f"Transcribing page {page_no}: {image_path.name}")
        text = call_ollama_generate(model, page_prompt, [image_path], ollama_url)
        outputs.append(f"# Page {page_no}\n{text}\n")

    output_text.write_text("\n".join(outputs), encoding="utf-8")
    print(f"OCR output written to '{output_text}'.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Use Ollama OCR model to transcribe a PDF")
    parser.add_argument("pdf_path", type=Path, help="Path to the source PDF")
    parser.add_argument("output_text", type=Path, help="Where to write the transcribed text")
    parser.add_argument(
        "--model",
        default="benhaotang/Nanonets-OCR-s:latest",
        help="Ollama model identifier",
    )
    parser.add_argument(
        "--ollama-url",
        default="http://127.0.0.1:11434",
        help="Base URL for the Ollama server",
    )
    parser.add_argument(
        "--prompt",
        default="<image>\nPlease transcribe this page preserving layout in markdown.",
        help="Prompt template (may use {page} placeholder)",
    )
    parser.add_argument("--dpi", type=int, default=220, help="Rendering DPI for PDF pages")
    parser.add_argument("--temp-dir", type=Path, help="Directory for intermediate page images")
    parser.add_argument("--start-page", type=int, help="1-based index of first page to process")
    parser.add_argument("--end-page", type=int, help="1-based index of last page to process (inclusive)")
    parser.add_argument("--max-pages", type=int, help="Maximum number of pages to process")

    args = parser.parse_args()

    prompt_template = args.prompt
    if "{page}" not in prompt_template:
        prompt_template = f"{prompt_template}\n(Page {{page}})"

    process_pdf_with_ollama(
        pdf_path=args.pdf_path,
        output_text=args.output_text,
        model=args.model,
        prompt_template=prompt_template,
        ollama_url=args.ollama_url,
        dpi=args.dpi,
        temp_dir=args.temp_dir,
        start_page=args.start_page,
        end_page=args.end_page,
        max_pages=args.max_pages,
    )


if __name__ == "__main__":
    main()
