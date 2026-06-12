import gradio as gr
import ollama

def predict(message, history):
    # 1. Format the history into the structure Ollama expects
    # Gradio history is [[user, bot], [user, bot]]
    messages = []
    for item in history:
        role = item["role"]
        content_blocks = item.get("content", [])
        if content_blocks and isinstance(content_blocks, list):
            text = content_blocks[0].get("text", "")

            if text:
                messages.append(
                    {
                        "role": role,
                        "content": text
                    }
                )
    
    # 2. Add the current user prompt
    messages.append({"role": "user", "content": message})
    
    # 3. Stream from Ollama
    # Ensure the model name matches what you pulled (e.g., 'llama3.2:3b')
    stream = ollama.chat(
        model='llama3.2',
        messages=messages,
        stream=True
    )
    
    # 4. Yield the response chunks
    partial_response = ""
    for chunk in stream:
        content = chunk['message']['content']
        partial_response += content
        yield partial_response

# Launch the interface
demo = gr.ChatInterface(
    fn=predict,
    title="Bhavan ChatBot",
    description="Chatting locally with Llama 3.2 via Ollama."
)

demo.launch()