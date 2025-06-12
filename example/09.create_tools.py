# -*- coding: utf-8 -*-
import json
import os
import sys
from LightAgent import LightAgent

# Initialize LightAgent
agent = LightAgent(
    name="Agent A",  # Agent name
    instructions="You are a helpful agent.",  # Role description
    role="Please remember that you are a tool generator; your task is to automatically generate corresponding tool code based on the text description provided by the user and save it to the specified directory. Please ensure that the generated code is accurate, usable, and meets the user's needs.",  # Tool generator's role description
    model="gpt-4.1",  # Replace with your model. Supported models: openai, chatglm, deepseek, qwen, etc.
    api_key="your_api_key",  # Replace with your API Key
    base_url="your_base_url",  # Replace with your API URL
)

# Sample text description
text = """
### 天气查询工具函数说明文档

#### 功能描述
该函数用于获取指定城市的实时天气信息，通过调用公共天气API（wttr.in）并返回格式化后的天气数据。

#### 参数说明
- **city_name** (str):
  需要查询的城市名称（必须是字符串类型）
  示例: `"Beijing"`, `"New York"`

#### 返回值
- 返回类型为字符串，包含以下两种可能：
  1. 成功时：返回包含天气数据的JSON格式字符串
  2. 失败时：返回错误信息字符串（包含异常堆栈跟踪）

#### 数据内容
成功返回的天气数据包含以下字段：
- `temp_C`: 当前温度（摄氏度）
- `FeelsLikeC`: 体感温度（摄氏度）
- `humidity`: 湿度百分比
- `weatherDesc`: 天气现象描述
- `observation_time`: 数据观测时间

#### 异常处理
1. **输入验证**：
   - 如果`city_name`不是字符串类型，抛出`TypeError`

2. **API请求异常**：
   - 网络请求失败或数据解析异常时，捕获所有错误并返回包含错误详情的字符串

#### 实现细节
1. **API端点**：
   ```python
   f"https://wttr.in/{city_name}?format=j1"
   ```
   - 使用`j1`格式获取JSON数据

2. **数据筛选**：
   ```python
   key_selection = {
       "current_condition": ["temp_C", "FeelsLikeC", ...]
   }
   ```
   - 从API返回的完整数据中仅提取关键字段

3. **错误处理**：
   ```python
   except:
       ret = "Error encountered while fetching weather data!\n" + traceback.format_exc()
   ```
   - 保留完整的错误堆栈信息便于调试

"""

# Build the path to the tools directory
tools_directory = os.path.join("tools")

# Create tools directory if it does not exist
if not os.path.exists(tools_directory):
    os.makedirs(tools_directory)

print(f"Tools directory has been created: {tools_directory}")

# Use agent to generate tool code
agent.create_tool(text, tools_directory=tools_directory)