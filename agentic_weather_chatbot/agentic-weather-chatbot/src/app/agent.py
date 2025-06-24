from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel, Agent, RunConfig, Runner, function_tool
from dotenv import load_dotenv
import os
import requests
import asyncio
from openai.types.responses import ResponseTextDeltaEvent

load_dotenv()

@function_tool
def get_weather(city:str):
    """
    Get the weather for a given city.
    """
    try:
        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={os.getenv("WEATHER_API_KEY")}&q={city}")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error: ",e)

external_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.getenv("GEMINI_API_KEY")
)

model = OpenAIChatCompletionsModel(
        model = "gemini-2.5-flash-preview-05-20",
        openai_client=external_client
    )

weather_agent : Agent = Agent(
    name = "Weather Assistant",
    instructions="You have to use your tool of get_weather for the city for which city weather user demands",
    tools=[get_weather],
    model=model
)

config = RunConfig(
    model = model,
    tracing_disabled = True
)


# async def main():
#     result  =  Runner.run_streamed( 
#         starting_agent=weather_agent,
#         input="What is the weather is in Tokyo?",
#         run_config=config
#     )
#     async for event in result.stream_events():
#         if event.type == "raw_response_event" and hasattr(event.data,"delta") and isinstance(event,ResponseTextDeltaEvent):
#             print(event.data.delta)

# if __name__ == "__main__":
#     asyncio.run(main())