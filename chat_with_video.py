# ask question in the terminal and get the ans and timestamp

import json

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

import google.generativeai as genai

genai.configure(
    api_key="API_KEY"
)

gemini_model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

with open(
    "embeddings.json",
    "r",
    encoding="utf-8"
) as f:
    data = json.load(f)

question = input(
    "Ask a question: "
)

question_embedding = embedding_model.encode(
    question
)

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

context = "\n\n".join(
    chunk["text"]
    for chunk in top_chunks
)

prompt = f"""

Context:
{context}

Question:
{question}

Answer the question using only the provided context.Context is Conversation between nikhil kamath and elon musk, in the majority of case nikhil will ask the question and elon will answer that questions. When in any question mention his, he means elon. 

If the answer is not available in the context,
say:
'I could not find the answer in this video.'
"""

response = gemini_model.generate_content(
    prompt
)

answer = response.text

timestamp = top_chunks[0]["start"]

print("\nANSWER:\n")
print(answer)

print("\nTIMESTAMP:")
print(timestamp)