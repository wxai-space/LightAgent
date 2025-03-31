import asyncio
import json
from LightAgent import LightAgent

# Initialize Agent
agent = LightAgent(model="gpt-4o-mini", api_key="your_api_key",
                   base_url="http://your_base_url/v1",
                   debug=True,
                   log_level="debug",
                   log_file="example.log")


def read_mcp_settings():
    with open("./mcp/lightagent_mcp_settings.json", "r") as f:
        mcp_settings_json = json.load(f)
    return mcp_settings_json


# 接入MCP 服务
mcp_settings = read_mcp_settings()
asyncio.run(agent.setup_mcp(mcp_setting=mcp_settings))

# Run Agent
response = agent.run("Please search the weather in Shanghai.", stream=False)
print(response)
