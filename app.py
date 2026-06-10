from ollama import chat
from pprint import pprint
print(chat)
messages=[
     
        {"role": "user", "content": "What is AI?"}
        
    ]
response=chat(model="llama3.1:latest",messages=messages)
#print(response.message.content)
pprint(response.model_dump())