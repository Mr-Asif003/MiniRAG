# 🧠 MiniRAG — Personal Information RAG Assistant

> A lightweight **Retrieval-Augmented Generation (RAG)** application that allows users to provide their personal information and ask questions about themselves. MiniRAG retrieves the most relevant information from the user's data and uses an LLM to generate context-aware answers.

---

## 🚀 Overview

**MiniRAG** is a simple yet practical **Retrieval-Augmented Generation application** built with Python.

The application allows a user to provide information about themselves, such as:

* 👤 Personal details
* 🎓 Education
* 💼 Skills
* 💻 Projects
* 🏆 Achievements
* 📜 Experience
* 🎯 Goals
* 📚 Interests
* 📝 Other relevant information

After processing the information, MiniRAG converts the data into vector representations and stores them in a **FAISS vector store**.

When the user asks a question, the application:

1. Processes the user's query.
2. Searches the vector database for relevant information.
3. Retrieves the most relevant pieces of information.
4. Passes the retrieved context to the LLM.
5. Generates an answer based only on the retrieved information.

### Example

**User Information**

```text
Name: Asif Khan
Education: B.Tech Computer Science
Skills: Java, Python, Spring Boot, React
Projects: MiniRAG, Era
Achievement: SIH Finalist
```

**User Query**

```text
What projects have I worked on?
```

**MiniRAG**

```text
You have worked on projects including MiniRAG and Era.
```

The goal is to make the LLM answer questions **from the user's provided information rather than relying on unrelated external knowledge.**

---

# ✨ Features

* 📄 Upload/provide user information
* 🔍 Semantic search using vector embeddings
* 🧠 Retrieval-Augmented Generation
* ⚡ FAISS-powered vector search
* 🤗 Hugging Face model integration
* 🔗 LangChain-based RAG pipeline
* 🖥️ Interactive Streamlit interface
* 💬 Natural-language question answering
* 🔐 Environment-variable based API configuration
* 🚫 Reduces hallucination by restricting answers to retrieved context
* 🧩 Modular architecture that can be extended to larger RAG systems

---

# 🏗️ Tech Stack

| Technology       | Purpose                                |
| ---------------- | -------------------------------------- |
| 🐍 Python        | Core programming language              |
| 🎈 Streamlit     | Web UI                                 |
| 🔗 LangChain     | RAG pipeline and document processing   |
| 🤗 Hugging Face  | LLM / model inference                  |
| 🔎 FAISS         | Vector similarity search               |
| 🧮 Embeddings    | Convert text into vectors              |
| 📚 Vector Store  | Store and retrieve document embeddings |
| 🔐 python-dotenv | Environment variable management        |

---

# 🧠 What is RAG?

**Retrieval-Augmented Generation (RAG)** is an architecture where an LLM first retrieves relevant information from an external knowledge source and then uses that information to generate the final response.

Instead of asking the LLM:

```text
Question → LLM → Answer
```

MiniRAG follows:

```text
User Query
     │
     ▼
Query Embedding
     │
     ▼
FAISS Vector Search
     │
     ▼
Relevant User Information
     │
     ▼
Context + Query
     │
     ▼
Hugging Face LLM
     │
     ▼
Generated Answer
```

This allows the application to answer questions about information that may not be part of the model's original training data.

---

# 🔄 MiniRAG Workflow

## 1️⃣ User Provides Information

The user provides information about themselves.

Example:

```text
I am a Computer Science student.

I know Java, Python, React and Spring Boot.

I have worked on a project called MiniRAG.

I am interested in Artificial Intelligence
and Backend Development.
```

---

## 2️⃣ Document Creation

The provided information is converted into documents that can be processed by the RAG pipeline.

```text
User Information
       ↓
Documents
```

---

## 3️⃣ Text Splitting

Large documents can be divided into smaller chunks.

```text
Large Document
      ↓
 ┌──────────┐
 │ Chunk 1  │
 ├──────────┤
 │ Chunk 2  │
 ├──────────┤
 │ Chunk 3  │
 └──────────┘
```

Chunking makes retrieval more precise because the vector search can retrieve smaller relevant pieces instead of an entire document.

---

# 4️⃣ Generate Embeddings

Each document chunk is converted into a numerical vector.

```text
"Java Developer"
       ↓
Embedding Model
       ↓
[0.12, -0.45, 0.82, ...]
```

Semantically similar text produces vectors that are closer together in vector space.

---

# 5️⃣ Store Vectors in FAISS

The generated embeddings are stored in a **FAISS vector index**.

```text
Document
   ↓
Embedding
   ↓
FAISS
   ↓
Vector Index
```

FAISS allows the application to efficiently search for vectors that are similar to the user's query.

---

# 6️⃣ User Asks a Question

Example:

```text
What technologies do I know?
```

The query is converted into an embedding.

```text
User Query
    ↓
Embedding Model
    ↓
Query Vector
```

---

# 7️⃣ Similarity Search

The query vector is compared against the vectors stored in FAISS.

```text
Query Vector
      │
      ▼
┌───────────────┐
│ FAISS Search  │
└───────┬───────┘
        │
        ▼
Relevant Chunks
```

For example:

```text
Chunk 2 → Java, Python, React
Chunk 7 → Spring Boot, MongoDB
Chunk 9 → Artificial Intelligence
```

---

# 8️⃣ Context Construction

The retrieved information becomes the context for the LLM.

```text
Context:

The user knows Java, Python, React,
Spring Boot and MongoDB.
```

---

# 9️⃣ LLM Generation

The context and question are sent to the Hugging Face model.

```text
Context
   +
Question
   │
   ▼
Hugging Face LLM
   │
   ▼
Answer
```

---

# 🔟 Final Answer

The application returns the generated response through Streamlit.

```text
Question:
What technologies do I know?

Answer:
You know Java, Python, React, Spring Boot
and MongoDB.
```

---

# 🏛️ Architecture

```text
                    ┌─────────────────────┐
                    │       User          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Streamlit UI    │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
             User Information        User Query
                    │                     │
                    ▼                     ▼
             Document Loader       Query Processing
                    │                     │
                    ▼                     ▼
              Text Splitter         Query Embedding
                    │                     │
                    ▼                     │
             Embedding Model              │
                    │                     │
                    ▼                     │
              FAISS Vector Store ◄────────┘
                    │
                    ▼
              Similarity Search
                    │
                    ▼
              Relevant Context
                    │
                    ▼
              Prompt Construction
                    │
                    ▼
           Hugging Face LLM
                    │
                    ▼
              Generated Answer
                    │
                    ▼
              Streamlit UI
                    │
                    ▼
                  User
```

---

# 📂 Project Structure

```text
MiniRAG/
│
├── app.py
│
├── requirements.txt
│
├── .env
├── .gitignore
│
├── data/
│   └── user_information.txt
│
├── vectorstore/
│   └── faiss_index/
│
├── utils/
│   ├── document_loader.py
│   ├── embeddings.py
│   └── rag.py
│
└── README.md
```

> The exact structure can be adjusted according to the current implementation.

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate into the project:

```bash
cd MiniRAG
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

# 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Example dependencies:

```text
streamlit
langchain
langchain-community
langchain-huggingface
huggingface_hub
faiss-cpu
python-dotenv
```

---

# 🔑 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
HF_TOKEN=your_huggingface_token
HF_MODEL=your_huggingface_model
```

Example:

```env
HF_TOKEN=hf_xxxxxxxxxxxxxxxxx
HF_MODEL=Qwen/Qwen3.8-27B
```

Never commit your `.env` file to GitHub.

Add it to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

---

# ▶️ 5. Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser.

Usually:

```text
http://localhost:8501
```

---

# 💬 Example Queries

After adding your information, you can ask questions such as:

```text
What is my educational background?
```

```text
What programming languages do I know?
```

```text
What projects have I worked on?
```

```text
What are my technical skills?
```

```text
What achievements do I have?
```

```text
What technologies have I used in my projects?
```

```text
What am I interested in?
```

The system retrieves relevant information from the user's knowledge base before generating the answer.

---

# 🔍 Example RAG Prompt

The application follows the principle:

```text
You are a helpful RAG assistant.

Answer the user's question using ONLY
the information provided in the context.

If the answer is not present in the context,
say:

"I don't have enough information in the provided data."
```

For example:

```text
Context:
--------------------------------
The user knows Java, Python and React.

The user has worked on a RAG project
using LangChain and FAISS.
--------------------------------

Question:
What technologies have I used?

Answer:
You have used Java, Python, React,
LangChain and FAISS.
```

---

# 🧩 Core Components

## Streamlit

Streamlit provides the interactive frontend.

It handles:

* User input
* Information submission
* Query input
* Displaying responses
* Application state

---

## LangChain

LangChain is used to build and connect the RAG components.

It helps manage:

```text
Documents
   ↓
Text Splitting
   ↓
Embeddings
   ↓
Vector Store
   ↓
Retriever
   ↓
LLM
```

---

## Hugging Face

Hugging Face provides access to the language model used to generate the final answer.

The application can use different models without changing the overall RAG architecture.

---

## FAISS

**FAISS (Facebook AI Similarity Search)** is a library for efficient similarity search over vectors.

In MiniRAG, FAISS is responsible for finding user-information chunks that are semantically similar to the user's query.

---

# 🧠 Why Use Vector Search?

Traditional keyword search might look for:

```text
"Java"
```

But semantic search can understand that:

```text
"What programming languages can I code in?"
```

may be related to:

```text
"I have experience working with Java."
```

even though the exact words are different.

This is one of the major advantages of embedding-based retrieval.

---

# 🛡️ Hallucination Control

MiniRAG attempts to reduce hallucinations by instructing the LLM to answer using only retrieved context.

If the information is unavailable:

```text
I don't have enough information in the provided data.
```

This creates a controlled knowledge boundary around the user's information.

> Note: Prompt instructions can reduce hallucinations but cannot guarantee that an LLM will never generate unsupported information. Production systems should additionally consider retrieval-quality checks, citations, evaluation, and output validation.

---

# 📈 Future Improvements

MiniRAG can be extended into a production-grade RAG system.

### 🔹 Better Retrieval

* Hybrid search
* Metadata filtering
* MMR retrieval
* Reranking
* Query expansion
* Multi-query retrieval

### 🔹 Better RAG

* Conversational RAG
* Chat history
* Source citations
* Retrieval evaluation
* Context compression
* Query rewriting

### 🔹 Better Storage

Current:

```text
FAISS
```

Possible future options:

```text
FAISS
Chroma
Pinecone
Qdrant
Weaviate
Milvus
pgvector
```

### 🔹 Authentication

Add:

```text
User
 ↓
Authentication
 ↓
Personal Knowledge Base
 ↓
RAG
```

This would allow multiple users to maintain separate knowledge bases.

### 🔹 Production Deployment

Possible deployment architecture:

```text
                Internet
                   │
                   ▼
             Streamlit App
                   │
                   ▼
             RAG Backend
             /         \
            /           \
           ▼             ▼
      Vector DB        LLM API
           │             │
           ▼             ▼
     User Knowledge   Hugging Face
```

---

# 🎯 Learning Outcomes

Building MiniRAG provides practical experience with:

* Python
* Streamlit
* LangChain
* Large Language Models
* Hugging Face
* Embeddings
* Vector databases
* FAISS
* Semantic search
* Document processing
* Retrieval-Augmented Generation
* Prompt engineering
* LLM application architecture

---

# 🧪 RAG Pipeline Summary

The complete pipeline can be remembered as:

```text
LOAD
  ↓
SPLIT
  ↓
EMBED
  ↓
STORE
  ↓
RETRIEVE
  ↓
AUGMENT
  ↓
GENERATE
```

Or:

```text
Documents
    ↓
Chunks
    ↓
Embeddings
    ↓
FAISS
    ↓
Retriever
    ↓
Relevant Context
    ↓
Prompt
    ↓
Hugging Face LLM
    ↓
Answer
```

---

# 🚀 Future Vision

MiniRAG is designed as a starting point for building more advanced AI applications.

The next evolution can be:

```text
MiniRAG
   │
   ├── Multi-user RAG
   │
   ├── Conversational RAG
   │
   ├── Hybrid Search
   │
   ├── Reranking
   │
   ├── Agentic RAG
   │
   ├── LangGraph
   │
   ├── Tool Calling
   │
   └── Multi-Agent AI System
```

This makes MiniRAG a practical foundation for learning how modern **LLM-powered applications and AI agents** are designed.

---

# 👨‍💻 Author

**Asif Khan**

B.Tech Computer Science Engineering

Interested in:

* 🤖 Artificial Intelligence
* 🧠 Generative AI
* 🔗 RAG & AI Agents
* 💻 Full-Stack Development
* ⚙️ Backend & Scalable Systems

---

# ⭐ If You Like This Project

If you find MiniRAG useful for learning RAG and LLM application development, consider giving the repository a ⭐.

---

## 📄 License

This project is intended for educational and experimental purposes.
