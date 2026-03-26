import json
import uuid

def write_jsonl(chunks, output_file):
    with open(output_file, "a", encoding="utf-8") as f:
        for chunk in chunks:
            record = {
                "id": str(uuid.uuid4()),
                "text": chunk["text"],
                "metadata": {
                    "source_file": chunk["source"],
                    "page_start": chunk["page_start"],
                    "chunk_index": chunk["chunk_index"]
                }
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")