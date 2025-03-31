from LightAgent import LightAgent


# Define Tool
def get_weather(city_name: str) -> str:
    """
    Get the current weather for `city_name`
    """
    return f"Query result: {city_name} is sunny."


# Define tool information inside the function
get_weather.tool_info = {
    "tool_name": "get_weather",
    "tool_description": "Get current weather information for the specified city.",
    "tool_params": [
        {"name": "city_name", "description": "The name of the city to query", "type": "string", "required": True},
    ]
}

tools = [get_weather]

# Initialize Agent
agent = LightAgent(model="qwen-turbo-2024-11-01", api_key="your_api_key", base_url="http://your_base_url/v1",
                   tools=tools)

# Run Agent
response = agent.run("Please check the weather in Shanghai.")
print(response)
