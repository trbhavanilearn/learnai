# 🚀 Day 5 - Generative AI Learning with Python, Ollama & Gradio

## 🎯 Learning Objectives

Today we explored:

* Python Functions
* Returning Multiple Values
* Tuples
* Generators
* Yield Keyword
* Streaming Responses
* Ollama Integration
* Iteration & StopIteration Concept
* Gradio Installation
* Building a Simple Chatbot
* ChatInterface in Gradio

---

# 📚 Topics Covered

## 1️⃣ Returning Multiple Values from a Function

Python allows a function to return multiple values.

### Example

```python
def get_details():
    return "Bhavani", "Python"
```

### Usage

```python
result = get_details()

print(result)
print(type(result))
```

### Output

```text
('Bhavani', 'Python')
<class 'tuple'>
```

### Important Learning

Whenever multiple values are returned:

```python
return value1, value2
```

Python automatically converts them into a:

```text
Tuple
```

---

# 2️⃣ How ChatGPT Streams Responses

When using ChatGPT, responses appear gradually instead of all at once.

Example:

```text
Hello...
How are...
you today?
```

This is called:

## Streaming

Benefits:

* Faster user experience
* Immediate feedback
* Better interaction
* Reduced waiting time

---

# 3️⃣ Understanding Generators

Generators produce data one item at a time instead of loading everything into memory.

### Example

```python
def display_conversation(conversation):
    for msg1, msg2 in conversation:
        print("Prabhu :", msg1)
        print("Bharathi:", msg2)
```

### Sample Data

```python
conversation = [
    ("Hi", "Hello"),
    ("How are you?", "I am good")
]

display_conversation(conversation)
```

---

# 4️⃣ Purpose of yield

The `yield` keyword converts a function into a Generator.

### Example

```python
def conversation_fancy():

    yield "Hi"

    yield "I am Bhavani"

    yield "From LearnLessDaily"
```

### Usage

```python
for message in conversation_fancy():
    print(message)
```

### Output

```text
Hi
I am Bhavani
From LearnLessDaily
```

---

## Difference Between return and yield

| return                        | yield                                  |
| ----------------------------- | -------------------------------------- |
| Returns entire result at once | Returns one value at a time            |
| Function ends immediately     | Function pauses and resumes            |
| Memory intensive              | Memory efficient                       |
| Used for small datasets       | Ideal for large datasets and streaming |

---

# 5️⃣ Streaming Responses Using Ollama

Today we integrated Ollama with Python.

### Sample Program

```python
from ollama import chat

messages = [

    {
        "role": "system",
        "content": "You are a funny cricket expert and always reply funny responses and humour only in 50 words."
    },

    {
        "role": "user",
        "content": "What is best shot to play when bouncer is coming?"
    }

]

response = chat(
    model="llama3.2:latest",
    messages=messages,
    stream=True
)

for chunk in response:
    print(chunk.message.content, end="", flush=True)

print()
print("Program Ends")
```

---

# Understanding stream=True

```python
stream=True
```

Instead of waiting for the complete response:

```text
[Full Response]
```

Ollama sends:

```text
Chunk 1
Chunk 2
Chunk 3
Chunk 4
...
```

This creates a real-time typing effect similar to ChatGPT.

---

# Important Methods Used

## chat()

```python
chat()
```

Used to communicate with Ollama models.

### Parameters

| Parameter | Purpose              |
| --------- | -------------------- |
| model     | Model name           |
| messages  | Conversation history |
| stream    | Enable streaming     |

Example:

```python
response = chat(
    model="llama3.2:latest",
    messages=messages,
    stream=True
)
```

---

# 6️⃣ How Iteration Stops Automatically

Generators don't run forever.

When all yield statements are exhausted:

```python
yield "Hi"
yield "Hello"
yield "Bye"
```

Python automatically raises:

```text
StopIteration
```

Internally:

```python
next(generator)
```

Eventually becomes:

```text
StopIteration
```

This signals that no more data is available.

---

# Generator Lifecycle

```text
Generator Created
       ↓
First yield
       ↓
Second yield
       ↓
Third yield
       ↓
No more yields
       ↓
StopIteration
```

---

# 7️⃣ Installing Gradio

Gradio helps create AI web applications quickly.

### Installation

```bash
pip install gradio
```

### Verify Installation

```bash
pip show gradio
```

---

# What is Gradio?

Gradio is a Python library used to:

* Build AI Applications
* Create Chatbots
* Create User Interfaces
* Demo Machine Learning Models

Without HTML, CSS, or JavaScript.

---

# 8️⃣ Developed a Simple Chatbot

Using:

* Ollama
* Python
* Gradio

We built a simple chatbot capable of:

* Accepting user questions
* Sending prompts to Ollama
* Displaying model responses

---

# 9️⃣ ChatInterface in Gradio

One of the most useful Gradio components.

### Purpose

Creates a ready-made chatbot UI.

### Example

```python
import gradio as gr
```

```python
gr.ChatInterface()
```

---

# Sample ChatInterface Program

```python
import gradio as gr
from ollama import chat


def predict(message, history):

    response = chat(
        model="llama3.2:latest",
        messages=[
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response.message.content


demo = gr.ChatInterface(
    fn=predict,
    title="My AI Assistant",
    description="Simple Chatbot using Ollama"
)

demo.launch()
```

---

# Important ChatInterface Parameters

| Parameter   | Purpose                                     |
| ----------- | ------------------------------------------- |
| fn          | Function executed when user submits message |
| title       | Application title                           |
| description | Application description                     |
| chatbot     | Chat window                                 |
| textbox     | User input box                              |

---

# Project Flow

```text
User Question
      ↓
Gradio ChatInterface
      ↓
predict()
      ↓
Ollama Model
      ↓
Response Generated
      ↓
Displayed in Browser
```

---

# Commands Used Today

## Install Ollama Package

```bash
pip install ollama
```

## Install Gradio

```bash
pip install gradio
```

## Verify Ollama

```bash
ollama --version
```

## List Models

```bash
ollama list
```

## Run Llama Model

```bash
ollama run llama3.2:latest
```

---

# Key Learnings

✅ Multiple return values become Tuples

✅ Learned Generator Functions

✅ Understood yield keyword

✅ Explored Streaming Responses

✅ Learned how ChatGPT-like streaming works

✅ Integrated Ollama with Python

✅ Understood Iteration and StopIteration

✅ Installed Gradio

✅ Built a Simple Chatbot

✅ Learned ChatInterface

✅ Connected UI with Ollama Model

---

# 🌟 Day 5 Outcome

Successfully learned:

* Python Tuples
* Generators
* Yield
* Streaming Architecture
* Ollama Python SDK
* AI Response Streaming
* Gradio Basics
* ChatInterface
* Chatbot Development

🚀 Ready for Day 6 Learning Journey!
