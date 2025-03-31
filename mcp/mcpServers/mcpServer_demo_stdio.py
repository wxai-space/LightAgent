# server.py
import httpx
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


@mcp.tool()
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate bmi given weight in kg and height in meters"""
    return weight_kg / (height_m ** 2)


@mcp.tool()
async def fetch_weather(city: str) -> str:
    """Fetch current weather for a city"""
    async with httpx.AsyncClient() as client:

        if not isinstance(city, str):
            raise TypeError("City name must be a string")

        key_selection = {
            "current_condition": ["temp_C", "FeelsLikeC", "humidity", "weatherDesc", "observation_time"],
        }
        try:
            resp = await client.get(f"https://wttr.in/{city}?format=j1")
            resp.raise_for_status()
            resp = resp.json()
            ret = {k: {_v: resp[k][0][_v] for _v in v} for k, v in key_selection.items()}
        except:
            import traceback
            ret = "Error encountered while fetching weather data!\n" + traceback.format_exc()

        return str(ret)


if __name__ == "__main__":
    mcp.run()
