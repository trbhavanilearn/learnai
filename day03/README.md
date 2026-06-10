1.created git profile
2.git commands git add .
3.git commit -m "Day3 learnings"
4.git push
5.pip upgrade
6.pip install ollama
7.repo creation
8.always work from root folder
9.md syntax
10.readme.md purpose
11.Tried Sample program using ollama
from ollama import chat
from pprint import pprint
print(chat)
messages=[
     
        {"role": "user", "content": "What is AI?"}
        
    ]
response=chat(model="llama3.1:latest",messages=messages)
#print(response.message.content)
pprint(response.model_dump())
