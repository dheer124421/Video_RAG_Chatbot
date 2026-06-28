import json

with open("transcript.json", "r", encoding="utf-8") as f:
    transcript = json.load(f)

# print(transcript)

chunks = []

current_text = ""
chunk_start = None
chunk_end = None

for item in transcript:

    if chunk_start is None:
        chunk_start = item["start"]

    current_text += " " + item["text"]
    chunk_end = item["end"]

    if len(current_text) >= 500:

        chunks.append({
            "text": current_text.strip(),
            "start": chunk_start,
            "end": chunk_end
        })

        current_text = ""
        chunk_start = None

if current_text:

    chunks.append({
        "text": current_text.strip(),
        "start": chunk_start,
        "end": chunk_end
    })

print("Total chunks:", len(chunks))

with open(
    "chunks.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        chunks,
        f,
        indent=2,
        ensure_ascii=False
    )

# print("\nFirst Chunk:")
# print(chunks[0])

# print("\nLast Chunk:")
# print(chunks[-1])

# print("\nLength of First Chunk:")
# print(len(chunks[0]["text"]))

# print(chunks[0])

# print(chunks[0]["start"])
# print(chunks[0]["end"])

# print(chunks[1]["start"])
# print(chunks[1]["end"])