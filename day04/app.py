# print("Hello World")

from ollama import chat
print(chat)   

messages=[
    #{"role": "admin", "content": "you are helpful assistant type whenever someone ask their name tell the name is Bhavani"},
    #{"role": "system", "content": "you are helpful assistant type whenever someone ask their name tell the name is Bhavani"},
    #{"role": "user", "content": "What is myname"}
    {"role": "system", "content": "You are a funny cricket expert and always reply funny responses and humours only in 50 words."},
    {"role": "user", "content": "What is best shot to play when bouncer is coming?"}
    #{"role": "user", "content": "What is best shot to play when bouncer is coming?"},
    
    ]
response = chat(model="llama3.1:latest", messages=messages)
print(response.message.content)

print("program ends")