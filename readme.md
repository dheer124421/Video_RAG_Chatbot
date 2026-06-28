# 🎥 Video RAG Chatbot — Ask Questions About Any YouTube Interview

An AI-powered chatbot that lets users ask natural language questions about a 2-hour YouTube interview (Nikhil Kamath × Elon Musk) and get context-aware answers with clickable source timestamps — instead of manually scrubbing through the video.

## 🎯 Problem it solves

Long-form video content (interviews, podcasts, lectures) is hard to search. This project lets you ask a question in plain English and get an answer grounded in the actual transcript, with a direct timestamp to verify it yourself.

## 🖼️ Demo

> *(Add a screen recording: type a question → show the answer + clickable timestamp jumping to that point in the video)*

## 🏗️ How it works (RAG pipeline)

```
YouTube Transcript API (extract transcript)
   → Chunking (500-char chunks)
   → Sentence Transformers — all-MiniLM-L6-v2 (generate embeddings)
   → User question → embedded → cosine similarity search (Scikit-learn)
   → Top-5 relevant chunks retrieved
   → Gemini 2.5 Flash (generates grounded answer from retrieved context)
   → Flask UI (displays answer + clickable timestamps)
```

## 🛠️ Tech Stack

| Component | Tool |
|---|---|
| Backend | Python, Flask |
| Transcript Extraction | YouTube Transcript API |
| Embeddings | Sentence Transformers (all-MiniLM-L6-v2) |
| Retrieval | Scikit-learn (cosine similarity) |
| Answer Generation | Google Gemini 2.5 Flash |
| Frontend | HTML |

## ✨ What I built

- Independently designed and implemented the complete end-to-end RAG pipeline.
- Built the chunking strategy and generated embeddings for semantic search over transcript text.
- Implemented cosine similarity search to retrieve the most relevant transcript sections for a given question.
- Built the RAG workflow that feeds retrieved context into Gemini for grounded answer generation.
- Built a Flask web interface showing AI answers alongside clickable video timestamps.
- **Improved retrieval quality** by reducing chunk size from 1000 → 500 characters and expanding retrieved context from Top-3 → Top-5 chunks.
- Added multiple relevant timestamps (not just one) for better explainability and source verification.

## 📈 Outcome

- Built a fully working AI application that answers questions about a 2-hour video using semantic search + RAG.
- Improved answer relevance through iterative tuning of chunk size and retrieval depth.
- Added source verification, letting users validate AI answers against the original video directly.

## 🚀 How to run this

```bash
git clone https://github.com/dheer124421/Video_RAG_Chatbot.git
cd Video_RAG_Chatbot
pip install -r requirements.txt
cp .env.example .env   # add your GEMINI_API_KEY
python app.py
```

## 🧠 What I learned

Practical experience with embeddings, semantic search, cosine similarity, Retrieval-Augmented Generation design, prompt engineering, and building a Flask-based AI application end-to-end.

## 🔮 Possible improvements

- Support any YouTube video URL as input (currently hardcoded to one video)
- Add conversation memory for follow-up questions
- Deploy live with a public demo link
