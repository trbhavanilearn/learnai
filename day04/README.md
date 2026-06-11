# 🚀 Day 3 - Ollama, JSON, XML, CSV & Prompt Engineering

## 🎯 Learning Objectives

Today we explored:

* Python application execution (`app.py`)
* Ollama Python SDK
* JSON Basics
* XML Basics
* CSV Basics
* Markdown Documentation
* Prompt Engineering
* System/User Roles
* How LLMs behave
* How ChatGPT and Ollama generate responses

---

# 📂 Project Structure

```text
project/
│
├── app.py
├── roles.json
├── roles.xml
├── roles.csv
├── README.md
└── requirements.txt
```

---

# 🐍 Python Application

## app.py

```python
from ollama import chat

messages = [
    {
        "role": "system",
        "content": "You are a funny cricket expert and always reply funny responses and humours only in 50 words."
    },
    {
        "role": "user",
        "content": "What is best shot to play when bouncer is coming?"
    }
]

response = chat(
    model="llama3.1:latest",
    messages=messages
)

print(response.message.content)

print("Program Ends")
```

---

# 📦 Installing Ollama Python Package

```bash
pip install ollama
```

Verify Installation:

```bash
pip show ollama
```

---

# 🤖 Install Llama Model

List available models:

```bash
ollama list
```

Install Llama 3.2:

```bash
ollama run llama3.2:latest
```

Download only:

```bash
ollama pull llama3.2:latest
```

---

# 🔍 Useful Ollama Commands

## Check Version

```bash
ollama --version
```

## List Models

```bash
ollama list
```

## Run Model

```bash
ollama run llama3.2:latest
```

## Exit Chat

```bash
/bye
```

## Clear Terminal

```bash
cls
```

---

# 📝 Markdown Basics

## Install Markdown All In One (VS Code)

1. Open VS Code
2. Click Extensions
3. Search

```text
Markdown All in One
```

4. Install Extension

Benefits:

* Auto Preview
* Table Formatting
* Shortcuts
* TOC Generation

---

# 📄 What is README.md?

README.md is the documentation file of a project.

Example:

```text
README.md
```

Extension:

```text
.md
```

stands for

```text
Markdown
```

---

# Markdown Syntax

## Heading

```md
# Main Heading
## Sub Heading
### Small Heading
```

## Bold

```md
**Bold Text**
```

## Italic

```md
*Italic Text*
```

## Code Block

````md
```python
print("Hello")
```
````

---

# 📘 JSON Basics

JSON = JavaScript Object Notation

Used for:

* APIs
* Configuration
* Data Exchange

---

## JSON Object

Curly Braces

```json
{
    "name": "Bhavani"
}
```

Meaning:

```text
{} = Object
```

---

## JSON Array

Square Brackets

```json
[
    "Python",
    "Java",
    "JavaScript"
]
```

Meaning:

```text
[] = Array
```

---

# Simple JSON

```json
{
    "name": "Bhavani",
    "age": 30
}
```

---

# Complex JSON

```json
{
    "name": "Bhavani",
    "skills": [
        "Python",
        "Playwright",
        "Pytest"
    ]
}
```

---

# Very Complex JSON

```json
{
  "employee": {
    "name": "Bhavani",
    "skills": [
      {
        "language": "Python",
        "experience": 5
      },
      {
        "language": "Java",
        "experience": 3
      }
    ],
    "address": {
      "city": "Chennai",
      "country": "India"
    }
  }
}
```

---

# 📄 Sample JSON File

```json
{
  "roles": [
    {
      "id": 1,
      "name": "Admin"
    },
    {
      "id": 2,
      "name": "User"
    }
  ]
}
```

---

# 📄 Sample XML File

```xml
<roles>

    <role>
        <id>1</id>
        <name>Admin</name>
    </role>

    <role>
        <id>2</id>
        <name>User</name>
    </role>

</roles>
```

---

# 📄 Sample CSV File

```csv
id,name
1,Admin
2,User
```

---

# 🎭 Roles Used in LLMs

## 1. User Role

Represents the human asking questions.

Example:

```json
{
    "role": "user",
    "content": "What is Python?"
}
```

Purpose:

* Ask questions
* Provide instructions
* Give context

---

## 2. System Role

Defines model behaviour.

Example:

```json
{
    "role": "system",
    "content": "You are a cricket expert."
}
```

Purpose:

* Set personality
* Set tone
* Define restrictions
* Define behaviour

---

## 3. Assistant Role

Normally generated automatically.

Example:

```json
{
    "role": "assistant",
    "content": "Python is a programming language."
}
```

Purpose:

* Model response
* Conversation continuity
* Context preservation

Normally developers do not manually add assistant messages unless maintaining conversation history.

---

# 🧠 How ChatGPT Works

User Question

↓

Tokenization

↓

Context Understanding

↓

Pattern Matching

↓

Probability Prediction

↓

Response Generation

---

# 🕵️ How It Works In Incognito

Incognito mode typically means:

* No previous chat history
* No stored conversation context
* Every chat starts fresh

The model still works because the model itself is already trained.

It does not need your personal history to answer general questions.

---

# 🏷️ Teaching Ollama Your Name

Method 1 (Temporary)

```python
{
    "role":"system",
    "content":"Whenever user asks their name, answer Bhavani."
}
```

Works only for current session.

---

Method 2 (Persistent)

Create your own:

* Custom Model
* Modelfile

Example:

```text
FROM llama3.2

SYSTEM You are an assistant.
Always remember the user's name is Bhavani.
```

Build:

```bash
ollama create mymodel -f Modelfile
```

Run:

```bash
ollama run mymodel
```

---

# 🎯 How Prompts Behave

Prompt quality directly affects output quality.

---

## Weak Prompt

```text
Tell me about cricket.
```

Result:

Generic answer.

---

## Better Prompt

```text
Explain cricket to a beginner in 50 words.
```

Result:

Focused answer.

---

## Advanced Prompt

```text
You are a funny cricket coach.
Explain how to play a bouncer shot in exactly 50 words.
```

Result:

Specific, targeted response.

---

# 📚 Key Learnings

✅ Installed Ollama

✅ Learned Ollama commands

✅ Understood JSON Objects and Arrays

✅ Created JSON files

✅ Created XML files

✅ Created CSV files

✅ Learned Markdown documentation

✅ Explored User, System and Assistant roles

✅ Understood Prompt Engineering

✅ Learned how ChatGPT and Ollama generate responses

✅ Learned how context affects model behaviour

---

# 🌟 Day 3 Outcome

Successfully built a foundation in:

* Ollama
* Prompt Engineering
* JSON
* XML
* CSV
* Markdown
* Python Integration
* LLM Roles
* Local AI Models

🚀 Ready for Day 4 Learning Journey!
