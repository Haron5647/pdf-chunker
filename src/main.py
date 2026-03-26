import click
from pathlib import Path

from src.extract import extract_pdf
from src.clean import clean_pages
from src.chunk import chunk_pages
from src.write import write_jsonl

@click.command()
@click.option("--input_dir", required=True)
@click.option("--output_file", required=True)
@click.option("--chunk_size", default=1000)
@click.option("--overlap", default=200)
def main(input_dir, output_file, chunk_size,overlap):


    for file in Path(input_dir).glob("*.pdf"):

        pages = extract_pdf(file)
        if not pages:
            continue

        cleaned = clean_pages(pages)
        chunks = chunk_pages(cleaned, chunk_size,overlap)
        write_jsonl(chunks, output_file)


if __name__ == "__main__":
    main()