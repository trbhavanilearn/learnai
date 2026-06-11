# 🚀 Day 2 - Ollama, WSL & AI Fundamentals

## 📚 Topics Covered

### 1️⃣ Docker – Build, Deploy & Execute

Docker is a containerization platform used to:

* 🔨 Build applications
* 🚀 Deploy applications
* ▶️ Execute applications consistently across environments

### Workflow

```text
Application Code
        ↓
   Docker Image
        ↓
    Container
        ↓
 Deployment
```

---

## 2️⃣ How AI Thinks

AI does not think exactly like humans, but it attempts to mimic certain human reasoning patterns.

### AI Process

```text
Input
   ↓
Understanding Context
   ↓
Pattern Matching
   ↓
Probability Calculation
   ↓
Response Generation
```

### Key Points

* Learns from large datasets
* Recognizes patterns
* Predicts the most likely response
* Improves output through training

---

## 3️⃣ WSL (Windows Subsystem for Linux)

WSL allows Linux to run directly inside Windows without installing a separate operating system.

### Benefits

✅ Linux commands on Windows

✅ Development-friendly environment

✅ Better compatibility with Docker and DevOps tools

✅ Lightweight and easy to use

---

## 4️⃣ How ChatGPT Generates Responses

When a question is asked:

### Step 1

Understand the question.

### Step 2

Analyze context and intent.

### Step 3

Search learned patterns from training data.

### Step 4

Predict the next most appropriate words.

### Step 5

Generate a complete response.

---

## 5️⃣ What is Ollama?

Ollama is a platform used to run Large Language Models (LLMs) locally on your machine.

### Simple Comparison

| Tool   | Purpose                             |
| ------ | ----------------------------------- |
| Docker | Runs applications inside containers |
| Ollama | Runs AI models locally              |

### Benefits

* No internet required after model download
* Faster local execution
* Better privacy
* Easy model management

---

## 6️⃣ How to Install Ollama

### Download

Visit:

https://ollama.com

### Install

Follow the installation wizard for your operating system.

### Verify Installation

```bash
ollama --version
```

---

## 7️⃣ Ollama Installation Verification

Check whether Ollama is installed correctly:

```bash
ollama --version
```

Example:

```text
ollama version 0.xx.x
```

---

## 8️⃣ Check Ollama Version

```bash
ollama --version
```

Displays the currently installed Ollama version.

---

## 9️⃣ List Available Models

```bash
ollama list
```

Displays all downloaded models available locally.

Example:

```text
NAME               SIZE
llama3.1:latest    4.7 GB
```

---

## 🔟 Run Llama 3.1 Model

```bash
ollama run llama3.1:latest
```

This command:

* Loads the model
* Starts a local AI chat session
* Allows interaction without using ChatGPT

---

## 1️⃣1️⃣ Exit Ollama Chat

```bash
/bye
```

Used to exit the current Ollama session.

---

## 1️⃣2️⃣ Clear Terminal Screen

```bash
cls
```

Used in Windows Command Prompt to clear the terminal.

---

## 1️⃣3️⃣ Ask Questions to Ollama

Example Questions:

```text
What is AI?
```

```text
Explain Docker.
```

```text
What is Python?
```

```text
Write a sample automation script.
```

The model generates responses based on its training data.

---

## 1️⃣4️⃣ Different Questions Produce Different Responses

AI dynamically generates answers based on:

* Question wording
* Context
* Model knowledge
* Conversation history

Example:

```text
What is Python?
```

Produces a definition.

```text
Teach me Python.
```

Produces a learning guide.

---

## 1️⃣5️⃣ How Ollama / AI Models Think

Models do not "think" like humans.

They:

1. Break input into tokens.
2. Analyze relationships between words.
3. Use learned patterns.
4. Predict the most probable next word.
5. Build a complete response.

### Simplified Flow

```text
Question
    ↓
Tokenization
    ↓
Pattern Analysis
    ↓
Prediction
    ↓
Response
```

---

## 1️⃣6️⃣ How Ollama Works Without Wi-Fi

### Initial Requirement

Internet is required only to:

* Download Ollama
* Download AI models

### After Download

Everything runs locally on your machine.

```text
Downloaded Model
       +
Local CPU / GPU
       ↓
 AI Response
```

### Benefits

✅ Offline usage

✅ Better privacy

✅ No internet dependency

✅ Faster response generation

---

# 🎯 Day 2 Key Takeaways

✅ Understood Docker's role in Build, Deploy and Execution

✅ Learned the purpose of WSL

✅ Explored how ChatGPT generates responses

✅ Installed Ollama successfully

✅ Ran local AI models using Ollama

✅ Practiced essential Ollama commands

✅ Learned why different questions generate different responses

✅ Understood how AI models work internally

✅ Learned how Ollama can function without Wi-Fi after model download

---

# 🌟 Day 2 Outcome

Successfully learned:

* Docker Basics
* WSL Fundamentals
* AI Response Generation
* Ollama Installation
* Ollama Commands
* Running LLMs Locally
* Offline AI Usage
* AI Thinking Process

🚀 Ready for Day 3 Learning Journey!
