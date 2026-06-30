# 🚀 Day 12 - Retrieval Augmented Generation (RAG), Vector Databases & ETL Pipeline

# 🎯 Learning Objectives

Today we explored the complete workflow of building a **Retrieval-Augmented Generation (RAG)** application.

Topics covered:

* What is RAG?
* Vector Databases
* PDF Ingestion
* Chunking
* Chunking Strategies
* Embeddings
* Knowledge Base
* ETL Pipeline for RAG
* Airflow
* LangChain Ecosystem
* Hugging Face
* UV Project Setup
* RAG Ingestion Pipeline
* Tool Calling
* RAG Fine-Tuning

---

# 📚 What is RAG?

RAG stands for:

```text
Retrieval Augmented Generation
```

RAG combines the power of a **Vector Database** with a **Large Language Model (LLM)**.

Instead of relying only on the model's training knowledge, RAG retrieves relevant information from external documents before generating an answer.

---

# RAG Breakdown

## 1. Retrieval

Retrieve the most relevant information from a **Knowledge Base** stored in a Vector Database.

```text
Question
      ↓
Vector Search
      ↓
Relevant Chunks
```

---

## 2. Augmentation

The retrieved information is added to the user's prompt.

```text
User Question
        +
Retrieved Context
```

This additional information is called **Context**.

---

## 3. Generation

The LLM receives:

```text
Prompt + Context
```

and generates a more accurate response.

---

# Complete RAG Architecture

```text
PDF Files
     │
     ▼
Chunking
     │
     ▼
Embedding Model
     │
     ▼
Embedding Vectors
     │
     ▼
Vector Database
     │
     ▼
Similarity Search
     │
     ▼
Relevant Chunks
     │
     ▼
Prompt + Context
     │
     ▼
Large Language Model
     │
     ▼
Final Response
```

---

# 📄 PDF Files

Most enterprise knowledge exists in:

* PDF documents
* User Manuals
* Company Policies
* Technical Documentation
* Research Papers

These documents become the knowledge source for a RAG application.

Project Structure:

```text
project/
│
├── data/
│     ├── employee_handbook.pdf
│     ├── policy.pdf
│     └── product_manual.pdf
│
└── app_etl_rag/
```

---

# ✂️ What is Chunking?

Large Language Models cannot efficiently process very large documents in one request.

Therefore, documents are divided into **smaller pieces** called **Chunks**.

Example:

Large PDF

```text
100 Pages
```

↓

Chunk 1

↓

Chunk 2

↓

Chunk 3

↓

Chunk N

---

# Why Chunking?

Advantages:

* Faster retrieval
* Better search accuracy
* Lower memory usage
* Better embedding quality
* More relevant context

---

# Chunking Strategies

## Fixed Size Chunking

Split every 500 characters.

Example:

```text
Chunk 1 → 500 Characters

Chunk 2 → 500 Characters

Chunk 3 → 500 Characters
```

---

## Overlapping Chunking

Some text is repeated between chunks to preserve context.

Example:

```text
Chunk 1

Python is a programming language...

---------------------

Chunk 2

programming language...
used for AI...
```

---

## Sentence-Based Chunking

Split using complete sentences.

---

## Paragraph-Based Chunking

Each paragraph becomes one chunk.

---

## Semantic Chunking

Split based on meaning instead of fixed size.

This generally provides the highest quality retrieval.

---

# 🧠 Embeddings

Every chunk is converted into numbers using an **Embedding Model**.

Example:

Chunk:

```text
Python is easy to learn.
```

↓

Embedding

```text
[0.32, -0.11, 0.92, ...]
```

This numerical representation is called a **Vector**.

---

# One Chunk = One Vector

Important Concept:

```text
One Chunk
      ↓
Embedding Model
      ↓
One Vector
```

Every chunk stored inside the Vector Database has its own embedding vector.

---

# Knowledge Base

A Knowledge Base contains the organization's documents.

Examples:

* HR Policies
* Banking Documents
* Medical Records
* Product Manuals
* Company Guidelines

The knowledge base becomes searchable using vector similarity.

---

# 🗄️ Vector Database

A Vector Database stores embedding vectors instead of plain text.

Each record typically contains:

* Chunk ID
* Chunk Text
* Embedding Vector
* Metadata

Example:

| Chunk ID | Chunk Text    | Embedding |
| -------- | ------------- | --------- |
| 1        | Python Basics | Vector    |
| 2        | AI Overview   | Vector    |
| 3        | RAG Pipeline  | Vector    |

---

# Popular Vector Databases

## ChromaDB

Best suited for:

* Local Development
* Learning
* Prototyping

---

## Pinecone

Cloud-based managed Vector Database.

---

## PostgreSQL + pgvector

Traditional relational database with vector support.

---

## Snowflake Cortex

Enterprise AI platform with vector capabilities.

---

# ETL Pipeline for RAG

ETL stands for:

```text
Extract
Transform
Load
```

---

## Extract

Read PDF files.

---

## Transform

* Clean text
* Chunk documents
* Generate embeddings

---

## Load

Store embeddings inside the Vector Database.

---

# ETL Workflow

```text
PDF Files
      │
      ▼
Extract Text
      │
      ▼
Chunking
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
```

---

# Big Data & RAG

Large organizations may have millions of documents.

Example:

```text
10 TB Documents
```

Workflow:

```text
Big Data
      ↓
Chunking
      ↓
Embedding Model
      ↓
Embedding Vectors
      ↓
Vector Database
```

This enables efficient semantic search over massive datasets.

---

# Apache Airflow

Airflow is used to schedule and monitor ETL pipelines.

Typical responsibilities:

* Schedule ingestion jobs
* Monitor workflows
* Retry failed tasks
* Automate document processing

Example Pipeline:

```text
Daily PDF Upload
        ↓
Airflow
        ↓
Extract
        ↓
Chunk
        ↓
Generate Embeddings
        ↓
Update Vector DB
```

---

# LangChain Ecosystem

LangChain is one of the most popular frameworks for building LLM applications.

It provides utilities for:

* Chunking
* Prompt Templates
* RAG
* Agents
* Memory
* Tool Calling
* Document Loaders

It is widely used for production-grade Generative AI applications.

---

# Hugging Face

Hugging Face provides:

* Open-source models
* Embedding models
* Tokenizers
* Datasets
* Transformers

In RAG applications, Hugging Face embedding models are commonly used to generate vectors for document chunks.

---

# Project Setup

Initialize the project:

```bash
uv init --package app-etl-rag --python 3.12
```

Open in Visual Studio Code:

```bash
code .
```

Store PDF files inside:

```text
data/
```

Install project dependencies:

```bash
uv sync
```

Activate the virtual environment:

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

---

# Installing Packages with UV

Instead of using:

```bash
pip install package_name
```

use:

```bash
uv add package_name
```

Examples:

```bash
uv add chromadb

uv add langchain

uv add sentence-transformers

uv add pypdf
```

Synchronize:

```bash
uv sync
```

---

# Run the ETL Pipeline

Execute the ingestion process:

```bash
uv run python -m app_etl_rag.rag_ingestion
```

This pipeline:

* Reads PDFs
* Splits into chunks
* Generates embeddings
* Stores vectors in ChromaDB

---

# RAG Tool Calling

Tool Calling allows an LLM to invoke external tools while answering a question.

Examples:

* Search a Vector Database
* Query SQL
* Call an API
* Execute Python code
* Read documents

Instead of answering directly, the model decides which tool to use, gathers additional information, and then generates the final response.

---

# RAG Fine-Tuning

Fine-tuning and RAG are different concepts.

## RAG

* Uses external knowledge
* No model retraining
* Faster to update
* Best for frequently changing information

## Fine-Tuning

* Retrains the model on new datasets
* Changes model behavior
* Requires additional compute resources
* Best for specialized domains or tasks

In many enterprise applications, RAG is preferred because updating documents in the Vector Database is easier than retraining the model.

---

# Complete RAG Pipeline

```text
PDF Documents
        │
        ▼
Extract Text
        │
        ▼
Chunking
        │
        ▼
Embedding Model
        │
        ▼
Vector Database (ChromaDB)
        │
        ▼
Similarity Search
        │
        ▼
Relevant Chunks
        │
        ▼
Prompt + Context
        │
        ▼
Large Language Model
        │
        ▼
Final Response
```

---

# Commands Learned Today

## Create Project

```bash
uv init --package app-etl-rag --python 3.12
```

## Open Project

```bash
code .
```

## Synchronize Dependencies

```bash
uv sync
```

## Add Packages

```bash
uv add chromadb

uv add langchain

uv add sentence-transformers

uv add pypdf
```

## Run ETL Pipeline

```bash
uv run python -m app_etl_rag.rag_ingestion
```

---

# 🎯 Key Learnings

✅ Understood the complete RAG architecture

✅ Learned Retrieval, Augmentation, and Generation

✅ Understood PDF ingestion for knowledge bases

✅ Learned why chunking is essential

✅ Explored different chunking strategies

✅ Learned that one chunk becomes one embedding vector

✅ Explored ChromaDB and other vector databases

✅ Understood the ETL pipeline for RAG

✅ Learned the role of Apache Airflow in scheduling ETL jobs

✅ Explored LangChain for chunking and RAG workflows

✅ Learned about Hugging Face embedding models

✅ Built the foundation for enterprise RAG applications

---

# 🌟 Day 12 Outcome

Successfully learned the complete document ingestion pipeline for Retrieval-Augmented Generation (RAG). You now understand how enterprise AI systems process PDF documents, split them into chunks, generate embeddings, store vectors in databases, retrieve relevant information, and use LLMs to generate accurate, context-aware responses. This forms the foundation for building intelligent document search systems, enterprise chatbots, and AI knowledge assistants.
