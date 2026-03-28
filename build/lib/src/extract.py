import fitz
from pathlib import Path

def extract_pdf(file):
    pages = []

    try:
        doc = fitz.open(file)

        for i, page in enumerate(doc):
            text = page.get_text()

            if not text.strip():
                continue

            pages.append({
                "text": text,
                "page": i + 1,
                "source": file.name
            })

        if not pages:
            print(f"WARNING: No text found in {str(file)}")
            return None

        return pages

    except Exception:
        print(f"ERROR reading {file}")
        return None
