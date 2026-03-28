from langchain_text_splitters import RecursiveCharacterTextSplitter


def find_page_for_position(pos, mapping):
    if not mapping:
        return None, None

    for m in mapping:
        if m["start"] <= pos < m["end"]:
            return m["page"], m["source"]

    return mapping[-1]["page"], mapping[-1]["source"]


def chunk_pages(pages, chunk_size=1000, overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        add_start_index=True
    )

    full_text = ""
    mapping = []

    # собираем текст + mapping
    for page in pages:
        start = len(full_text)
        full_text += page["text"] + "\n"
        end = len(full_text)

        mapping.append({
            "start": start,
            "end": end,
            "page": page["page"],
            "source": page["source"]
        })

    # разбиваем с позициями
    docs = splitter.create_documents([full_text])

    result = []

    for i, doc in enumerate(docs):
        chunk = doc.page_content
        chunk_start = doc.metadata["start_index"]
        chunk_end = chunk_start + len(chunk)

        #  находим страницы
        page_start, source = find_page_for_position(chunk_start, mapping)
        page_end, _ = find_page_for_position(chunk_end - 1, mapping)

        result.append({
            "text": chunk,
            "chunk_index": i,
            "page_start": page_start,
            "source": source
        })

    return result