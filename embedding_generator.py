import json
from sentence_transformers import SentenceTransformer

print("Loading model...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("Model loaded.")

with open(
    "chunks.json",
    "r",
    encoding="utf-8"
) as f:
    chunks = json.load(f)

result = []

for i, chunk in enumerate(chunks):

    embedding = model.encode(
        chunk["text"]
    ).tolist()

    result.append({
        "text": chunk["text"],
        "start": chunk["start"],
        "end": chunk["end"],
        "embedding": embedding
    })

    print(
        f"Processed {i+1}/{len(chunks)}"
    )

with open(
    "embeddings.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        result,
        f,
        ensure_ascii=False
    )
    

print(
    len(result[0]["embedding"])
)

print("Done!")