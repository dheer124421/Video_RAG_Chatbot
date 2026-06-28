# used in the final front end , main backend logic 

import json
import os
from dotenv import load_dotenv

load_dotenv()
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

import google.generativeai as genai

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
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

def ask_video(question):

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

    top_chunks = results[:5]

    context = "\n\n".join(
        chunk["text"]
        for chunk in top_chunks
    )

    prompt = f"""

    Context:
    {context}

    Question:
    {question}

    You are answering questions about a YouTube interview between
    Nikhil Kamath and Elon Musk.

    Important:
    - Answer only using the provided context.
    - In most cases, Nikhil Kamath asks the questions and Elon Musk answers them.
    - If the question refers to "he", "his", or "him", assume it refers to Elon Musk.
    - Keep answers concise and factual.
    - If the answer is partially available, provide the best answer possible.
    - Do not invent information that is not present in the context,until and unless logic or consept will be same.
    - If you get the main logic or understanding of context but question words are not same but similar which allign with the context, required to give answer.
    - If the answer cannot be found logically match answer in the context, this is the last option, reply exactly:

    I could not find the answer in this video.

    """

    try:

        response = gemini_model.generate_content(
            prompt
        )

        answer = response.text

    except Exception as e:

        answer = (
             "AI response unavailable. "
            "Showing the most relevant transcript context:\n\n"
            + context[:1000]
        )

    timestamps = []

    for chunk in top_chunks:

        seen = set()
        timestamps = []

        for chunk in top_chunks:

            ts = int(chunk["start"])

            if ts not in seen:

                timestamps.append(ts)
                seen.add(ts)

    return {
        "answer": answer,
        "timestamps": timestamps
    }

if __name__ == "__main__":

    result = ask_video(
        "What did Elon say about entrepreneurship?"
    )

    print(result)