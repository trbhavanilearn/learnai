# print("Hello World")

from ollama import chat
print(chat)   

messages=[{"role": "user", "content": "What is AI?"}]
response = chat(model="llama3.2:latest", messages=messages)
print(response.message.content)

print("program ends")