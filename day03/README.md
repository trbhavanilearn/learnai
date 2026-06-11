# Day 3 Learning Summary

## Overview

| # | Topic | Details |
|---|--------|---------|
| 1 | Git Profile Creation | Created and configured Git profile for version control. |
| 2 | Git Add | Used `git add .` to stage all modified files. |
| 3 | Git Commit | Used `git commit -m "Day3 learnings"` to commit changes with a meaningful message. |
| 4 | Git Push | Used `git push` to upload commits to the remote repository. |
| 5 | Pip Upgrade | Upgraded Python package manager (pip) to the latest version. |
| 6 | Ollama Installation | Installed Ollama Python package using pip. |
| 7 | Repository Creation | Created a new Git repository for project version control. |
| 8 | Root Folder Best Practice | Learned to always execute commands from the project root folder. |
| 9 | Markdown Syntax | Explored Markdown (`.md`) syntax for documentation. |
| 10 | README.md Purpose | Understood the importance of `README.md` as the project's primary documentation file. |
| 11 | Ollama Sample Program | Executed a sample Ollama-based AI interaction program. |
| 12 | SSH Key Generation | Generated SSH key for secure GitHub authentication. |
| 13 | Git Username Configuration | Configured global Git username. |
| 14 | Git Email Configuration | Configured global Git email address. |

---

## Commands Practiced

| Purpose | Command |
|----------|----------|
| Create Virtual Environment | `python -m venv .venv` | 
| Activate Virtual Environment | `source .venv/Scripts/activate` |
| pip list  | `pip list` |
| pip upgrade  | `python.exe -m pip install --upgrade pip` |
| pip freeze  | `pip freeze` |
| pip freeze to requirements.txt  | `pip freeze > requirements.txt` |
| Stage All Files | `git add .` |
| Commit Changes | `git commit -m "Day3 learnings"` |
| Push Changes | `git push` |
| Clone Changes | `git clone git@github.com:trbhavanilearn/learnai.git` |
| Generate SSH Key | `ssh-keygen -t ed25519 -C "trbhavanilearn@gmail.com"` |
| Set Git Username | `git config --global user.name "Bhavani"` |
| Set Git Email | `git config --global user.email "trbhavanilearn@gmail.com"` |
| Upgrade Pip | `python -m pip install --upgrade pip` |
| Install Ollama | `pip install ollama` |

---

## Ollama Python Sample Program

```python
from ollama import chat
from pprint import pprint

print(chat)

messages = [
    {
        "role": "user",
        "content": "What is AI?"
    }
]

response = chat(
    model="llama3.1:latest",
    messages=messages
)

# print(response.message.content)
pprint(response.model_dump())
```

---

## Key Learnings

| Area | Learning Outcome |
|--------|------------------|
| Git | Basic Git workflow: Add → Commit → Push |
| GitHub | Repository creation and remote code management |
| Authentication | SSH key generation and Git configuration |
| Python | Package management using pip |
| Ollama | Running local LLM models from Python |
| Documentation | Creating structured project documentation using Markdown |
| Best Practices | Working from the root folder to avoid path-related issues |

---

## Professional Summary

Successfully configured Git and GitHub integration, generated SSH credentials, learned essential Git commands, upgraded Python tooling, installed and tested Ollama, practiced Markdown documentation standards, and executed a Python-based AI interaction program using the Ollama library.

**Status:** ✅ Completed Day 3 Learning Activities
