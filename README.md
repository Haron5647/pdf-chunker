# pdf-chunker

**pdf-chunker** is a CLI tool for batch processing PDF documents. It extracts text from PDFs, normalizes it, splits it into chunks, and saves each document into a separate `.jsonl` file.

## Installation

To install the project, clone the repository and install the dependencies.

### Install dependencies

Run the following command in the project root:

```bash
pip install .
```

Or, if you want to use a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
.venv\Scripts\activate     # Windows
pip install .
```

## Usage

The tool provides a CLI command for processing PDF documents.

### Example usage:

```bash
pdf-chunker --input_dir ./pdfs --output_dir ./out
```

### Arguments:

* `--input_dir` — Path to the directory containing PDF files to process

* `--input_file` — Path to a single PDF file
  One of these arguments must be provided

* `--output_dir` (required) — Directory where `.jsonl` files will be saved

* `--chunk_size` (optional) — Size of each text chunk in characters (default: 1000)

* `--overlap` (optional) — Overlap between chunks (default: 200)

* `--recreate` (optional) — Overwrite existing `.jsonl` files

* `--clear_dir` (optional) — Remove all files and subdirectories inside `output_dir` before processing

### Example:

```bash
pdf-chunker --input_dir ./pdfs --output_dir ./out --chunk_size 1500 --overlap 300 --recreate
```

This example will process all PDF files in the directory, split them into chunks of 1500 characters with an overlap of 300 characters, and overwrite existing output files.

## Output

Each input PDF file produces a separate `.jsonl` file in the output directory.

Example structure:

```bash
out/
 ├── file1.jsonl
 ├── file2.jsonl
 └── file3.jsonl
```

Each line in a `.jsonl` file contains:

```json
{
  "id": "uuid",
  "text": "chunk text",
  "metadata": {
    "source_file": "file.pdf",
    "page_start": 1,
    "chunk_index": 0
  }
}
```

## Dependencies

The following libraries are required:

* `click==8.1.7`
* `PyMuPDF==1.27.2`
* `langchain-text-splitters==1.1.1`

## Requirements

- Python 3.10 or higher