# print("Hello World")
from ollama import chat
messages=[
  
    {"role": "system", "content": "You are a funny cricket expert and always reply funny responses and humours only in 50 words."},
    {"role": "user", "content": "What is best shot to play when bouncer is coming?"}  
        ]
response = chat(model="llama3.2:latest", messages=messages,stream=True)
for chunk in response:
    print(chunk.message.content,end="",flush=True)
    
#print(response.message.content)
print("program ends")