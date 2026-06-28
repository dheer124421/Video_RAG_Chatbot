# searching the context/chunk throught the embedding 

import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading model...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("Loading embeddings...")

with open(
    "embeddings.json",
    "r",
    encoding="utf-8"
) as f:
    data = json.load(f)

question = input(
    "Ask a question: "
)

print("Generating question embedding...")

question_embedding = model.encode(question)

results = []

for chunk in data:

    similarity = cosine_similarity(
        [question_embedding],
        [chunk["embedding"]]
    )[0][0]

    results.append({
        "similarity": similarity,
        "text": chunk["text"],
        "start": chunk["start"],
        "end": chunk["end"]
    })

results.sort(
    key=lambda x: x["similarity"],
    reverse=True
)

top_chunks = results[:3]

print(top_chunks[0]["start"])

print("\nTop 3 Chunks:\n")

for i, chunk in enumerate(top_chunks, start=1):

    print(f"\nChunk {i}")
    print(f"Similarity: {chunk['similarity']:.4f}")
    print(f"Start: {chunk['start']}")
    print(f"End: {chunk['end']}")
    print(chunk["text"][:300])

context = "\n\n".join(
    [chunk["text"] for chunk in top_chunks]
)

print(context)