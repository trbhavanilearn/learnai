import gradio as gr
import ollama
import requests
from pprint import pprint


TOOLS=[{
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Only Call this when the user asks about weather, temperature, humidity, or conditions for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Name of the city"
                    }
                },
                "required": ["city"]
            }
        }
    }]

def execute_tool(tool_name, arguments):
    if tool_name == "get_weather":
        print("Executing get_weather with arguments:", arguments)
        city = arguments.get("city")        
        return get_weather(city)
    return "no execute tool found"

def get_weather(city):

    try:

        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(
            url,
            timeout=10
        )

        data = response.json()

        current = data["current_condition"][0]

        return f"""

        City: {city}


        Temperature: {current['temp_C']}°C

        Humidity: {current['humidity']}%

        Condition: {current['weatherDesc'][0]['value']}

        Wind Speed: {current['windspeedKmph']} km/h

        """

    except Exception as e:
        print("Error in get_weather:", str(e))
        return f"Error getting weather for {city}: {str(e)}"
def predict(message, history):
    # 1. Format the history into the structure Ollama expects
    # Gradio history is [[user, bot], [user, bot]]
    #messages = []
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant.   "
                " Use the get_weather"
                "whenever the user asks about weather, temperature, "
                "humidity, or conditions for a city, Otherwise, answer normally "
                "without calling any tool."
            )
        }
    ]
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
    print(messages)
    messages.append({"role": "user", "content": message})
    print(message)
    response=ollama.chat(
        model='llama3.2',
        messages=messages,
        tools=[get_weather]
        )
    pprint(response)
    tool_calls = response["message"].get("tool_calls")
    if not tool_calls:
        # No tool needed — just stream this same response back out
        yield response["message"]["content"]
        return
    messages.append(response["message"])
    for tool in tool_calls:
        tool_name = tool["function"]["name"]
        arguments = tool["function"].get("arguments", {})
        result = execute_tool(tool_name, arguments)

        messages.append({
            "role": "tool",
            "name": tool_name,   # lets the model match result -> tool
            "content": result
        })
    #messages.append(response["message"]["content"])
    # 3. Stream from Ollama
    # Ensure the model name matches what you pulled (e.g., 'llama3.2:3b')
    
    stream = ollama.chat(
        model='llama3.2',
        #model='learnlessdaily/learnlessdaily-chatbot:latest',
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
    title="Bhavani ChatBot",
    description="Chatting locally with Llama 3.2 via Ollama."
)

demo.launch()