import json


def export_chunks(chunks, filename="chunks.json"):

    data = []

    for i, doc in enumerate(chunks):

        data.append({
            "chunk_id": i,
            "content": doc.page_content,
            "metadata": doc.metadata
        })

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

    print("Chunks exported")