# 🚀 AI Masterclass: From Foundations to RAG Architecture

Welcome to my personal AI Learning Roadmap. This repository is a comprehensive guide designed for Web Developers (Laravel/Java/PHP) who want to transition into **AI Engineering** and **Generative AI**.

## 🌟 Overview
This project documents my journey of mastering Large Language Models (LLMs), Prompt Engineering, and building scalable **RAG (Retrieval-Augmented Generation)** systems.

> **Status:** Level 3 (In-Progress: RAG & Vector Databases)

---

## 🗺️ Learning Roadmap

### 🔴 Level 1: Foundations of GenAI
- Understanding Transformer Architecture (Attention Mechanism).
- Tokenization & Positional Encoding.
- Difference between Traditional ML and Generative AI.

### 🟠 Level 2: Behavior & Prompting
- **Advanced Prompting:** Chain of Thought (CoT), ReAct, and Role Prompting.
- **Optimization:** Prompt Compression & Context Window management.
- **Guardrails:** Defending against adversarial attacks.

### 🔵 Level 3: RAG (Retrieval-Augmented Generation) - *Current Focus*
- **Chunking Strategies:** Recursive Character, Semantic, and Overlapping Chunking.
- **Embedding Models:** Vector representations using OpenAI and Open-Source models (HuggingFace).
- **Vector Databases:** Managing high-dimensional data with ChromaDB/Pinecone.

---

## 🛠️ Tech Stack & Tools
- **Languages:** Python (AI Logic), PHP/Laravel (Backend ERP Integration).
- **AI Frameworks:** LangChain, FastAPI.
- **Models:** OpenAI (GPT-4), Sentence-Transformers (all-MiniLM-L6-v2).
- **Database:** MySQL (SQL Data) + Vector DB (AI Memory).

---

## 💻 Featured Code Snippets

### 🧩 Smart Text Chunking
Implementing `RecursiveCharacterTextSplitter` to maintain semantic context with 15% overlap.

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 600,
    chunk_overlap = 100
)
chunks = splitter.split_text(raw_document)
