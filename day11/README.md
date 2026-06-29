# 🚀 Day 11 – Modern AI Development, LLMs, UV & Embeddings

## 🎯 Learning Objectives

Today we explored the foundations of modern AI development, including:

* ChatGPT as a User Interface
* Multiple AI Models
* Open-Source LLMs
* Meta's Llama Models
* Thinking Models
* Tokens
* Encoding
* Embeddings
* UV Package Manager
* PyPDF Library
* Modern Python Project Management

---

# 💬 What is ChatGPT?

ChatGPT is an AI-powered conversational **User Interface (UI)** that allows users to interact with different Artificial Intelligence models.

Think of ChatGPT as a smart interface, while the actual intelligence comes from the Large Language Models (LLMs) running behind it.

```text
User
   │
   ▼
ChatGPT (UI)
   │
   ▼
Large Language Model
   │
   ▼
Generated Response
```

### ChatGPT Provides

* Natural conversation
* Code generation
* Text summarization
* Translation
* Explanation of concepts
* Problem solving

---

# 🤖 ChatGPT Supports Multiple Models

Different models are optimized for different tasks.

Examples:

* Fast response models
* Coding models
* Vision models
* Reasoning (Thinking) models
* Multimodal models

Each model has different strengths in terms of:

* Speed
* Accuracy
* Reasoning
* Creativity
* Context length

---

# 🌍 Open-Source Models

Open-source models can be downloaded and run locally without relying on cloud APIs.

Popular examples:

* Llama
* Mistral
* Gemma
* DeepSeek
* Qwen

Advantages:

* Offline execution
* No API cost
* Better privacy
* Customization
* Fine-tuning

---

# 🦙 Meta's Llama Models

Meta (formerly Facebook) developed the **Llama** family of Large Language Models.

Popular versions:

* Llama 3
* Llama 3.1
* Llama 3.2

Run locally using Ollama:

```bash
ollama run llama3.2:latest
```

Applications:

* AI Chatbots
* Content Generation
* Question Answering
* Code Assistant
* Summarization

---

# 🧠 Thinking Models

Thinking Models perform additional internal reasoning before generating an answer.

Instead of immediately predicting the next word, they analyze the problem first.

Workflow:

```text
Question
   │
   ▼
Reasoning
   │
   ▼
Planning
   │
   ▼
Answer
```

Best suited for:

* Mathematics
* Coding
* Logical reasoning
* Multi-step problems

---

# 🔤 What is a Token?

Large Language Models process **tokens**, not entire sentences.

Example:

Sentence:

```
Artificial Intelligence is amazing.
```

Possible Tokens:

```
Artificial
Intelligence
is
amazing
.
```

The tokenizer converts text into manageable pieces before processing.

---

# Why Tokens Matter

Tokens determine:

* Input length
* Output length
* Processing time
* Memory usage
* Context window

Example:

```
100 Tokens
      ↓
Model Processes
      ↓
100 Token Response
```

---

# 🔢 What is Encoding?

Encoding is the process of converting data into a machine-readable format.

Computers understand numbers, not plain text.

Example:

```
Hello
```

can be encoded internally into numbers.

Workflow:

```text
Text
   │
   ▼
Encoding
   │
   ▼
Numbers
```

---

# 🧠 What are Embeddings?

Embeddings are numerical vectors that represent the **meaning** of text.

Example:

```
I love Python
```

becomes

```
[0.45, -0.18, 0.92, ...]
```

Unlike simple encoding, embeddings capture semantic meaning.

---

# Encoding vs Embeddings

| Encoding                                   | Embeddings                    |
| ------------------------------------------ | ----------------------------- |
| Converts text into machine-readable format | Converts meaning into vectors |
| Basic representation                       | Semantic representation       |
| Does not preserve meaning                  | Preserves contextual meaning  |

---

# Why Embeddings?

Embeddings allow AI to understand similar meanings.

Example:

```
I love football.
```

and

```
Football is my favourite sport.
```

Although the words differ, the embeddings are very similar because the meanings are alike.

---

# Multi-Dimensional Vectors

Embeddings consist of hundreds or thousands of numerical values.

Common dimensions:

* 384
* 512
* 768
* 1024
* 1536

Example:

```
[0.21, -0.44, 0.81, ..., 0.09]
```

Each value is one dimension in the vector.

---

# Embedding Generation Flow

```text
User Question
      │
      ▼
Tokenizer
      │
      ▼
Encoding
      │
      ▼
Embedding Model
      │
      ▼
Vector (384 Dimensions)
```

---

# Why Embeddings are Important

Embeddings are used for:

* Semantic Search
* Similarity Search
* Vector Databases
* Retrieval-Augmented Generation (RAG)
* AI Chatbots
* Recommendation Systems

---

# AI Workflow

```text
User Prompt
      │
      ▼
Tokenizer
      │
      ▼
Encoding
      │
      ▼
Embedding
      │
      ▼
Similarity Search
      │
      ▼
Relevant Context
      │
      ▼
Large Language Model
      │
      ▼
Generated Response
```

---

# ⚡ What is UV?

**UV** is a modern Python package manager developed by **Astral**.

It replaces many traditional Python tools with a single fast utility.

Traditional Tools:

* pip
* virtualenv
* venv
* pip-tools

UV combines these into one.

---

# Why UV?

Benefits:

* Extremely fast
* Dependency management
* Virtual environments
* Project creation
* Lock files
* Reproducible builds

---

# Install UV

PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Check Version:

```bash
uv --version
```

---

# Create a Project

```bash
uv init --package myapp --python 3.14
```

---

# Synchronize Project

```bash
uv sync
```

Creates:

* Virtual Environment
* Installs Dependencies
* Synchronizes Packages

---

# Install Packages

Preferred Method:

```bash
uv add pypdf
```

Other examples:

```bash
uv add pandas
uv add gradio
uv add ollama
uv add chromadb
```

---

# Remove Packages

```bash
uv remove pandas
```

---

# Run Python Application

```bash
uv run app.py
```

---

# View Installed Packages

```bash
uv pip list
```

---

# Package Details

```bash
uv pip show pypdf
```

---

# Upgrade Packages

```bash
uv lock --upgrade
uv sync
```

---

# Generate Lock File

```bash
uv lock
```

---

# Install Using pip (Supported)

```bash
uv pip install numpy
```

---

# PyPDF

Install:

```bash
pip install pypdf
```

Import:

```python
from pypdf import PdfReader
```

Example:

```python
reader = PdfReader("sample.pdf")

print(len(reader.pages))
```

Uses:

* Read PDFs
* Extract Text
* Count Pages
* Split PDFs
* Merge PDFs

---

# UV vs Traditional Python

| Traditional      | UV             |
| ---------------- | -------------- |
| pip install      | uv add         |
| python app.py    | uv run app.py  |
| pip list         | uv pip list    |
| pip show         | uv pip show    |
| requirements.txt | pyproject.toml |
| virtualenv       | uv sync        |

---

# Complete UV Commands

## Install UV

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Check Version

```bash
uv --version
```

## Create Project

```bash
uv init --package myapp --python 3.14
```

## Synchronize

```bash
uv sync
```

## Add Package

```bash
uv add pypdf
```

## Add Multiple Packages

```bash
uv add pandas
uv add gradio
uv add ollama
uv add chromadb
```

## Remove Package

```bash
uv remove pandas
```

## Run Project

```bash
uv run app.py
```

## List Packages

```bash
uv pip list
```

## Package Information

```bash
uv pip show pypdf
```

## Generate Lock File

```bash
uv lock
```

## Upgrade Dependencies

```bash
uv lock --upgrade
uv sync
```

---

# Project Structure

```text
myapp/
│
├── pyproject.toml
├── uv.lock
├── README.md
├── .venv/
├── src/
└── app.py
```

---

# 🎯 Key Learnings

✅ ChatGPT is a conversational User Interface.

✅ Multiple AI models power ChatGPT.

✅ Meta developed the Llama family of open-source LLMs.

✅ Thinking models perform deeper reasoning before answering.

✅ LLMs process tokens, not full sentences.

✅ Encoding converts text into a machine-readable format.

✅ Embeddings convert text into semantic vectors.

✅ Embeddings enable semantic search and Retrieval-Augmented Generation (RAG).

✅ UV is a fast, modern replacement for many traditional Python development tools.

✅ Learned project creation, dependency management, and package installation using UV.

✅ Learned to read PDF documents using the `pypdf` library.

---

# 🌟 Day 11 Outcome

Successfully learned the complete modern AI development workflow:

* 💬 ChatGPT & LLMs
* 🦙 Open-Source Models (Llama)
* 🧠 Thinking Models
* 🔤 Tokens
* 🔢 Encoding
* 📐 Embeddings
* ⚡ UV Package Manager
* 📄 PDF Processing

These concepts provide the foundation for building **RAG (Retrieval-Augmented Generation)** applications, document-based chatbots, AI assistants, and production-ready Generative AI systems.
