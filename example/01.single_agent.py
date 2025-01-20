from LightAgent import LightAgent

# Initialize Agent
agent = LightAgent(model="gpt-4o-mini", api_key="your_api_key", base_url="your_base_url")

# Run Agent
response = agent.run("Hello, who are you?")
print(response)