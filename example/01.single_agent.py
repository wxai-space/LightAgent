from LightAgent import LightAgent

# Initialize Agent
agent = LightAgent(model="gpt-4o-mini", api_key="your_api_key", base_url="http://your_base_url/v1")

# Run Agent
response = agent.run("Hello, who are you?")
print(response)