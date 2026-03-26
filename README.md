# pdf-chunker

**pdf-chunker** is a CLI tool for batch processing university PDF documents. It extracts text from PDFs, normalizes it, and splits it into semantic chunks ready for vectorization.

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
pdf-chunker --input_dir ./pdfs --output_file result.jsonl
```

### Arguments:

* `--input_dir` (required) — Path to the directory containing PDF files to process
* `--output_file` (required) — Path to the output `.jsonl` file
* `--chunk_size` (optional) — Size of each text chunk in characters (default: 1000)
* `--overlap` (optional) — Overlap between chunks (default: 200)

### Example:

```bash
pdf-chunker --input_dir ./pdfs --output_file output.jsonl --chunk_size 1500 --overlap 300
```

This example will create chunks of 1500 characters with an overlap of 300 characters.

## Dependencies

The following libraries are required:

* `click==8.1.7`
* `PyMuPDF==1.27.2`
* `langchain-text-splitters==1.1.1`
