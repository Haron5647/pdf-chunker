import re

def clean_text(text: str) -> str:
    text = re.sub(r"-\n", "", text)  # склейка слов
    text = re.sub(r"^\s*\d+\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"Страница\s*\d+", "", text, flags=re.IGNORECASE)
    text = re.sub(r"Page\s*\d+", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\n(?=\S)", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def clean_pages(pages: list[dict]) -> list[dict]:
    cleaned = []

    for page in pages:
        text = page["text"]

        cleaned_text = clean_text(text)


        if not cleaned_text:
            continue

        cleaned.append({
            "text": cleaned_text,
            "page": page["page"],
            "source": page["source"]
        })

    return cleaned