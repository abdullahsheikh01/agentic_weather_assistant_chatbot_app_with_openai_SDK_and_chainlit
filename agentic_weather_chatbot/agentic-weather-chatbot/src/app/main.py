# Imports
import chainlit as cl
from agents import Runner 
from openai.types.responses import ResponseTextDeltaEvent # event.data type 

from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel, Agent, RunConfig, Runner, function_tool
from dotenv import load_dotenv
import os
import requests # To fetch data
from openai.types.responses import ResponseTextDeltaEvent


load_dotenv() # Loading Environment Variables

@function_tool # Decorator to make function a tool
def get_weather(city:str):
    """
    Get the weather for a given city.
    """
    try:
        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={os.getenv("WEATHER_API_KEY")}&q={city}") # Fetching Weather
        response.raise_for_status()
        return response.json()
    
    except Exception as e:
        print("Error: ",e)

external_client = AsyncOpenAI( # Making External client
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.getenv("GEMINI_API_KEY")
)

model = OpenAIChatCompletionsModel( # Configuring Model
        model = "gemini-2.5-flash-preview-05-20",
        openai_client=external_client
    )

weather_agent : Agent = Agent( # Making Weather Assistant
    name = "Weather Assistant",
    instructions="You have to use your tool of get_weather for the city for which city weather user demands",
    tools=[get_weather],
    model=model
)

config = RunConfig(
    model = model,
    tracing_disabled = True
)

@cl.on_chat_start
async def chat_start():
    cl.user_session.set("chat_history",[]) # Making session variable
    await cl.Message(content="Hi, Welcome to the Agentic Weather Assistant Chatbot\nCreated by: Abdullah Shaikh").send() # Welcome Messgae

@cl.on_message
async def handle_message(message:cl.Message):
    try:
        chat_historyy : list[dict[str,str]] = cl.user_session.get("chat_history") # Getting Session Variable Value
        chat_historyy.append({"role":"user","content":message.content}) # Appending User Prompt
        result = Runner.run_streamed( # Running on streamed
                weather_agent, chat_historyy, run_config=config
        )
        msg = cl.Message(content="Agent Start to think🤔\n") # Initial Message
        await msg.send()
        async for event in result.stream_events(): # Loop to get value token by token(performing streaming)
                if event.type == "raw_response_event" and hasattr(event.data,"delta") and isinstance(event.data,ResponseTextDeltaEvent):
                        await msg.stream_token(event.data.delta)
        chat_historyy.append({"role":"assistant","content":msg.content}) # Appending Assistant Respose
        cl.user_session.set("chat_history",chat_historyy) # Setting Session Variable with new prompt and response
        
    except Exception as e:
          cl.Message.send("Sorry Unknown Error Occured!") 
          print("Error:",e)