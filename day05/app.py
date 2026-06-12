def conversation(msg):
    return msg

def conversationfancy():    
    #return "Hi I am Bhavani", "Hi I am from Python"
    yield "hi"
    yield "I am Bhavani"
    yield "From Learnlessdaily"

def display_conversation(conversation):
    for msg1,msg2 in conversation:
        print("Prabhu : ",msg1)
        print("Bharathi:",msg2)

#a,b=conversationfancy()

#msg_stream=conversationfancy()
#print(next(msg_stream))
#print(next(msg_stream))
#print(next(msg_stream))
#print(next(msg_stream))
#print(conversationfancy())
#print(type(conversationfancy()))
conversation=[
["Hi","hi"],
["how are you","i am fine & what about you"],
["I am good Bye","Bye"],
["ok","ok"]
]
#display_conversation(conversation)

message1,message2=["how are you","i am fine & what about you"]
#print(message1,":",message2)

def displayarrconversation(messages):
    for message in messages:
        print(f"{message.get('role')} : {message.get('content')}")
messages=[]

message={"role":"User","content":"Hi"}
messages.append(message)
message={"role":"Bhavani","content":"Hi User"}
messages.append(message)

message={"role":"User","content":"How are you"}
messages.append(message)
message={"role":"Bhavani","content":"I am fine, How are you"}
messages.append(message)

displayarrconversation(messages)
#print("Messages : ",messages)



