import gradio as gr
from ollama import chat

def generate_response(message, history):
    messages = []
    messages.extend(history)
    #for message in history:
    #    print("Hisotry message : ",message)
        #messages.append({"role": "user", "content": user_msg})
        #messages.append({"role": "assistant", "content": assistant_msg})
    messages.append({"role": "user", "content": message})
    response = ""

    stream = chat(
        model="llama3.2",
        messages=messages,
        stream=True,
    )

    for chunk in stream:
        response += chunk["message"]["content"]
        yield response


"""
chatbot=generate_response("What is the weather in Chennai",[])
print(next(chatbot))
for messaging in chatbot:#range(20):
    print(next(chatbot))"""

demo=gr.ChatInterface(fn=generate_response,title="Bhavani Chatbot")
demo.launch()

