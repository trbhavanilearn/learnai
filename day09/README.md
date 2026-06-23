# 🚀 Day 08 & Day 09 - Generative AI, Vector Databases & RAG Fundamentals

# 🎯 Learning Objectives

During Day 08 and Day 09, we explored:

* Human Intelligence vs Artificial Intelligence
* Large Language Models (LLMs)
* Generative AI
* Ollama Platform
* Llama Models
* Gradio
* Machine Learning vs Generative AI
* Semantic Search
* Vector Databases
* Embeddings
* ChromaDB
* RAG (Retrieval Augmented Generation) Concepts
* Kubernetes & Docker
* Prompt, Context and Response Flow

---

# 🧠 Human Intelligence

Humans possess intelligence that allows them to:

* Learn from experience
* Reason logically
* Solve problems
* Understand language
* Make decisions
* Adapt to new situations

Example:

```text
Touching fire causes pain.
```

A human remembers this experience and avoids touching fire again.

---

# 🤖 Artificial Intelligence (AI)

Artificial Intelligence attempts to mimic certain aspects of human intelligence.

AI systems can:

* Understand text
* Recognize patterns
* Generate responses
* Predict outcomes
* Learn from data

Important:

```text
AI does not think exactly like humans.
```

Instead:

```text
AI uses mathematics, statistics,
and learned patterns from data.
```

---

# AI Mimics Human Intelligence

Human:

```text
Question
 ↓
Understanding
 ↓
Thinking
 ↓
Answer
```

AI:

```text
Question
 ↓
Pattern Matching
 ↓
Probability Calculation
 ↓
Response
```

---

# 🐳 Docker

Docker is used for:

* Creating Containers
* Packaging Applications
* Deploying Applications

Purpose:

```text
Build
 ↓
Deploy
 ↓
Execute
```

Applications run consistently across environments.

---

# ☸ Kubernetes

Kubernetes is used for:

```text
Managing Containers
```

and

```text
Orchestrating Containers
```

---

# Docker vs Kubernetes

| Docker             | Kubernetes                |
| ------------------ | ------------------------- |
| Creates Containers | Manages Containers        |
| Runs Applications  | Manages Large Deployments |
| Single Machine     | Multiple Machines         |
| Packaging          | Orchestration             |

---

# 🦙 What is Ollama?

Ollama is a platform used to run Large Language Models locally.

Example:

```bash
ollama run llama3.2:latest
```

Benefits:

* Local execution
* Offline usage
* No API costs
* Better privacy

---

# Popular Ollama Commands

Run Model:

```bash
ollama run llama3.2:latest
```

List Models:

```bash
ollama list
```

Check Version:

```bash
ollama --version
```

---

# What is Llama?

Llama is an open-source family of Large Language Models created by:

Meta

Examples:

* Llama 3.1
* Llama 3.2

---

# Llama 3.2

Llama 3.2 is a modern Large Language Model capable of:

* Answering Questions
* Summarization
* Translation
* Content Generation
* Chatbot Development

Example:

```bash
ollama run llama3.2:latest
```

---

# What is an LLM?

LLM stands for:

```text
Large Language Model
```

LLMs are trained on massive amounts of text.

Examples:

* Books
* Articles
* Documentation
* Websites
* Conversations

Purpose:

```text
Generate Human Language
```

---

# What is Generative AI?

Generative AI means:

```text
Generating Something New
```

Examples:

* Generate Text
* Generate Code
* Generate Images
* Generate Music
* Generate Videos

---

# Machine Learning vs Generative AI

Machine Learning:

```text
Data
 ↓
Pattern Learning
 ↓
Prediction
```

Example:

```text
Predict House Price
```

---

Generative AI:

```text
Prompt
 ↓
Generation
 ↓
New Content
```

Example:

```text
Write a Story
Generate Code
Create Summary
```

---

# Gradio

Gradio is a Python library used to create AI applications quickly.

Installation:

```bash
pip install gradio
```

Uses:

* Chatbots
* AI Applications
* Machine Learning Demos
* User Interfaces

---

# Ollama Python Library

Installation:

```bash
pip install ollama
```

Import:

```python
import ollama
```

Used to communicate with local AI models.

---

# LLM Roles

Three important roles:

## System

Controls behavior.

Example:

```python
{
  "role":"system",
  "content":"You are a cricket expert."
}
```

---

## User

Represents the human.

Example:

```python
{
  "role":"user",
  "content":"What is cricket?"
}
```

---

## Assistant

Represents previous AI responses.

Example:

```python
{
  "role":"assistant",
  "content":"Cricket is a bat-and-ball sport."
}
```

---

# Why Conversation Context Matters

LLMs do not automatically remember previous messages.

We must provide:

```text
Conversation History
```

Example:

```text
User: My name is Bhavani

Assistant: Nice to meet you.

User: What is my name?
```

Without context:

```text
I don't know.
```

With context:

```text
Your name is Bhavani.
```

---

# Scikit-Learn

Scikit-Learn is a Machine Learning library.

Installation:

```bash
pip install scikit-learn
```

Purpose:

* Model Training
* Data Prediction
* Pattern Detection

Usually works with:

```text
Small Datasets
Medium Datasets
```

---

# Machine Learning Algorithm

An algorithm is a mathematical method used to identify patterns in data.

Example:

```text
Study Hours → Marks
```

Algorithm learns:

```text
More Study Hours
=
Higher Marks
```

---

# Linear Regression

Import:

```python
from sklearn.linear_model import LinearRegression
```

Purpose:

Predict numerical values.

Examples:

* Salary Prediction
* House Price Prediction
* Sales Forecasting

---

# SQL Search vs GenAI Search

Traditional SQL Search:

```sql
SELECT * FROM employees
WHERE name='Bhavani'
```

Uses:

```text
Exact Match Search
```

---

# Generative AI Search

Uses:

```text
Similarity Search
Semantic Search
```

Example:

Query:

```text
How do I learn Python?
```

Can also find:

```text
Best way to study Python
Python learning roadmap
Python beginner guide
```

Even if exact words are different.

---

# Why Vector Databases?

Generative AI requires semantic search.

Normal databases cannot efficiently perform semantic similarity searches.

Solution:

```text
Vector Database
```

---

# Popular Vector Databases

## ChromaDB

Used for:

```text
Local Development
```

Installation:

```bash
pip install chromadb
```

---

## Other Popular Vector Databases

### Pinecone

Cloud-based vector database.

---

### PostgreSQL + PGVector

Traditional database with vector support.

---

### Snowflake Cortex

Enterprise AI platform.

---

### Azure Cosmos DB

Microsoft cloud database supporting AI workloads.

---

# What are Embeddings?

Embeddings convert text into numbers.

Example:

```text
I love cricket
```

becomes:

```text
[0.23, -0.78, 0.54, ...]
```

These numbers represent the meaning of the text.

---

# Why Embeddings?

Computers cannot understand text directly.

They understand:

```text
Numbers
```

Therefore:

```text
Text
 ↓
Embedding Model
 ↓
Vector Numbers
```

---

# Multi-Dimensional Vectors

Embeddings are vectors.

Example:

```text
[0.2, 0.5, 0.8]
```

Real AI embeddings contain hundreds of dimensions.

Example:

```text
384 Dimensions
768 Dimensions
1024 Dimensions
1536 Dimensions
```

---

# Example

Sentence:

```text
Python is easy to learn
```

Embedding:

```text
[0.45, 0.67, -0.12, ...]
```

Dimension Count:

```text
384
```

Every sentence becomes a vector representation.

---

# Retrieval Augmented Generation (RAG)

Modern AI applications often use RAG.

Flow:

```text
Question
 ↓
Embedding
 ↓
Vector Search
 ↓
Relevant Context
 ↓
LLM
 ↓
Response
```

---

# Prompt, Context and Response

The question we ask is called:

```text
Prompt
```

Example:

```text
What is Python?
```

---

Additional information supplied is called:

```text
Context
```

Example:

```text
Python training document
Company knowledge base
PDF content
```

---

Together:

```text
Prompt + Context
```

are sent to:

```text
LLM
```

The LLM generates:

```text
Response
```

---

# Complete Generative AI Flow

```text
User Question (Prompt)
            ↓
     Convert to Embedding
            ↓
      Search Vector DB
            ↓
      Retrieve Context
            ↓
Prompt + Context
            ↓
            LLM
            ↓
      Generated Response
```

---

# Commands Learned

Install Ollama Library:

```bash
pip install ollama
```

Install Gradio:

```bash
pip install gradio
```

Install Scikit-Learn:

```bash
pip install scikit-learn
```

Install ChromaDB:

```bash
pip install chromadb
```

Run Llama:

```bash
ollama run llama3.2:latest
```

List Models:

```bash
ollama list
```

---

# 🎯 Key Learnings

✅ Human Intelligence vs AI

✅ AI mimics human intelligence

✅ Docker and Kubernetes concepts

✅ Ollama platform

✅ Llama open-source models

✅ Large Language Models

✅ Generative AI

✅ Gradio library

✅ Roles: System, User, Assistant

✅ Importance of Context

✅ Scikit-Learn

✅ Linear Regression

✅ Semantic Search

✅ Similarity Search

✅ Vector Databases

✅ ChromaDB

✅ Embeddings

✅ Prompt + Context + LLM

✅ RAG Architecture

---

# 🌟 Day 08 & Day 09 Outcome

Successfully learned the complete foundation of:

* Generative AI
* Large Language Models
* Ollama
* Vector Databases
* Embeddings
* Semantic Search
* ChromaDB
* Retrieval Augmented Generation (RAG)

🚀 Ready for Day 10 - Building a Complete RAG Application!
