from src.extract import extract_pdf
from src.clean import clean_pages
from src.chunk import chunk_pages
from src.write import write_jsonl
from pathlib import Path

def process_file(file, output_dir, chunk_size, overlap,recreate=False):
    output_file = Path(output_dir) / f"{file.stem}.jsonl"

    if output_file.exists():
        if recreate:
            print(f"Rewriting: {output_file}")
            output_file.unlink()
        else:
            print(f"Skipping existing file: {output_file}")
            return

    pages = extract_pdf(file)
    if not pages:
        return

    cleaned = clean_pages(pages)
    chunks = chunk_pages(cleaned, chunk_size, overlap)

    output_file = Path(output_dir) / f"{file.stem}.jsonl"
    write_jsonl(chunks, output_file)