import re
import traceback
from typing import List, Dict, Any, Callable, Union, Iterable, Optional, Generator
from copy import deepcopy
import importlib.util
import random
import json
from datetime import datetime
from openai import OpenAI
import logging
import os
import httpx
import importlib
from openai.types.chat import ChatCompletionChunk
import asyncio

# 全局工具注册表
_FUNCTION_MAPPINGS = {}  # 工具名称 -> 工具函数
_FUNCTION_INFO = {}   # 工具名称 -> 工具info信息
_OPENAI_FUNCTION_SCHEMAS = []  # OpenAI 格式的工具描述
_PROMPT_FUNCTION_SCHEMAS = []  # prompt 格式的工具描述

__version__ = "0.2.9"  # 你可以根据需要设置版本号


def register_tool_manually(tools: List[Union[str, Callable]]) -> bool:
    """
    手动注册多个工具，从函数属性中提取工具信息
    :param tools: 工具函数列表
    """
    for func in tools:
        if not hasattr(func, "tool_info"):
            # raise ValueError(f"Function `{func.__name__}` does not have tool_info attribute.")
            continue

        tool_info = func.tool_info
        tool_name = tool_info["tool_name"]

        # 注册到全局字典
        _FUNCTION_INFO[tool_name] = tool_info
        _FUNCTION_MAPPINGS[tool_name] = func  # 注册工具

        # 构建 OpenAI 格式的工具描述
        tool_params_openai = {}
        tool_required = []
        for param in tool_info["tool_params"]:
            tool_params_openai[param["name"]] = {
                "type": param["type"],
                "description": param["description"],
            }
            if param["required"]:
                tool_required.append(param["name"])

        tool_def_openai = {
            "type": "function",
            "function": {
                "name": tool_name,
                "description": tool_info["tool_description"],
                "parameters": {
                    "type": "object",
                    "properties": tool_params_openai,
                    "required": tool_required,
                },
            }
        }

        _OPENAI_FUNCTION_SCHEMAS.append(tool_def_openai)
    return True


def load_tool(tool_name: str, tools_directory: str = "tools"):
    """
    根据工具名称从 tools 目录中加载对应的工具函数
    """
    tool_path = os.path.join(tools_directory, f"{tool_name}.py")
    if not os.path.exists(tool_path):
        raise FileNotFoundError(f"Tool '{tool_name}' not found in {tools_directory}")

    # 动态加载模块
    spec = importlib.util.spec_from_file_location(tool_name, tool_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # 获取工具函数
    if hasattr(module, tool_name):
        tool_func = getattr(module, tool_name)
        if callable(tool_func) and hasattr(tool_func, "tool_info"):
            return tool_func
    raise AttributeError(f"Tool '{tool_name}' is not properly defined in {tool_path}")

from typing import Dict, Any, Union, Generator, AsyncGenerator
import inspect
import traceback

async def dispatch_tool(tool_name: str, tool_params: Dict[str, Any]) -> Union[str, Generator[str, None, None], AsyncGenerator[str, None]]:
    """
    调用工具执行，支持同步/异步工具及流式输出。
    """
    if tool_name not in _FUNCTION_MAPPINGS:
        return f"Tool `{tool_name}` not found."

    tool_call = _FUNCTION_MAPPINGS[tool_name]
    try:
        # 区分同步/异步工具
        if inspect.iscoroutinefunction(tool_call):
            result = await tool_call(**tool_params)
        else:
            result = tool_call(**tool_params)

        # 处理不同类型的流式输出
        if inspect.isasyncgen(result):
            return async_stream_generator(result)
        elif inspect.isgenerator(result):
            return stream_generator(result)
        else:
            return str(result)
    except Exception as e:
        return traceback.format_exc()

async def async_stream_generator(async_gen: AsyncGenerator) -> AsyncGenerator[str, None]:
    async for chunk in async_gen:
        yield chunk

def stream_generator(sync_gen: Generator) -> Generator[str, None, None]:
    for chunk in sync_gen:
        yield chunk


def dispatch_tool_old(tool_name: str, tool_params: Dict[str, Any]) -> str:
    """
    调用工具执行
    """
    if tool_name not in _FUNCTION_MAPPINGS:
        return f"Tool `{tool_name}` not found."

    tool_call = _FUNCTION_MAPPINGS[tool_name]
    try:
        # print(f"Calling tool: {tool_name} with params: {tool_params}")  # 调试信息
        return str(tool_call(**tool_params))
    except Exception as e:
        # print(f"Tool call failed: {e}")  # 调试信息
        return traceback.format_exc()


def get_tools() -> List[Dict[str, Any]]:
    """
    获取所有工具的描述（OpenAI 格式）
    """
    return deepcopy(_OPENAI_FUNCTION_SCHEMAS)


def get_tools_str() -> str:
    """
    将 _OPENAI_FUNCTION_SCHEMAS 转换为格式化的 JSON 字符串。
    Returns:
        str: 格式化的 JSON 字符串。
    """
    # 使用 json.dumps 将字典转换为格式化的 JSON 字符串
    tools_str = json.dumps(_OPENAI_FUNCTION_SCHEMAS, indent=4, ensure_ascii=False)
    return tools_str


class LightAgent:
    __version__ = "0.2.9"  # 将版本号放在类中

    def __init__(
            self,
            *,
            name: Optional[str] = None,  # 代理名称
            instructions: Optional[str] = None,  # 代理指令
            role: Optional[str] = None,
            model: str,
            api_key: str | None = None,
            base_url: str | httpx.URL | None = None,
            websocket_base_url: str | httpx.URL | None = None,
            memory=None,  # 支持外部传入记忆模块
            tree_of_thought: bool = False,  # 是否启用链式思考
            tot_model: str | None = None,
            tot_api_key: str | None = None,
            tot_base_url: str | httpx.URL | None = None,
            self_learning: bool = False,  # 是否启用agent自我学习
            tools: List[Union[str, Callable]] = None,  # 支持混合输入
            debug: bool = False,  # 是否启用调试模式
            log_level: str = "INFO",  # 日志级别（INFO, DEBUG, ERROR）
            log_file: Optional[str] = None  # 日志文件路径
    ) -> None:
        """
        初始化 LightAgent。

        :param name: 代理名称。
        :param instructions: 代理指令。
        :param role: Agent 的角色描述。
        :param model: 使用的模型名称。
        :param api_key: API 密钥。
        :param base_url: API 的基础 URL。
        :param websocket_base_url: WebSocket 的基础 URL。
        :param memory: 外部传入的记忆模块，需实现 `retrieve` 和 `store` 方法。
        :param tree_of_thought: 是否启用思维链功能。
        :param tot_model: 使用的模型名称。
        :param tot_api_key: API 密钥。
        :param tot_base_url: API 的基础 URL。
        :param tools: 工具列表，支持函数名称（字符串）或函数对象。
        :param debug: 是否启用调试模式。
        :param log_level: 日志级别（INFO, DEBUG, ERROR）。
        :param log_file: 日志文件路径。
        """
        if not model:
            model = "gpt-4o-mini"  # 默认模型
        if not api_key:
            api_key = os.environ.get("OPENAI_API_KEY")
        if not base_url:
            base_url = os.environ.get("OPENAI_BASE_URL")
        self.loaded_tools = {}  # 用于存储已加载的工具函数
        if not name:
            random_suffix = random.randint(10000000, 99999999)  # 生成一个8位随机数
            name = f"LightAgent{random_suffix}"
        self.name = name
        if not instructions:
            instructions = "You are a helpful agent."
        self.instructions = instructions
        self.role = role
        self.model = model
        self.memory = memory
        self.tree_of_thought = tree_of_thought
        self.self_learning = self_learning

        self.debug = debug
        self.log_level = log_level.upper()
        # 确保 log 目录存在
        log_dir = 'logs'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        # 将 log_file 路径设置为 log 目录下的文件
        if debug:
            self.log_file = os.path.join(log_dir, log_file)
            # Set up the logger
            self.logger = self._setup_logger(log_level, self.log_file)
        if tools is None:
            self.tools = []
        if tools:
            self.tools = tools
            # 初始化工具列表
            self.load_tools(tools)
            # register_tool_manually(tools)
        if api_key is None:
            raise ValueError(
                "The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable"
            )
        self.api_key = api_key
        self.websocket_base_url = websocket_base_url

        if base_url is None:
            base_url = f"https://api.openai.com/v1"

        self.client = OpenAI(
            base_url = base_url,
            api_key = self.api_key
        )
        if self.tree_of_thought:
            if tot_api_key is None:
                tot_api_key = api_key
            if tot_base_url is None:
                tot_base_url = base_url
            if not tot_model:
                tot_model = "deepseek-r1"  # 默认思维推理模型为deepseek-r1
            self.tot_model = tot_model
            self.tot_client = OpenAI(
                base_url = tot_base_url,
                api_key = tot_api_key
            )

    def get_tool(self, tool_name: str) -> Callable:
        """
        用于外部可以获取已加载的工具函数
        :param tool_name: 工具名称
        :return: 工具函数
        """
        if tool_name in self.loaded_tools:
            return self.loaded_tools[tool_name]
        raise ValueError(f"Tool `{tool_name}` is not loaded.")

    def get_tools(self) -> List[str]:
        """
        用于外部可以获取已加载的工具函数列表
        :return: 工具函数
        """

        return list(_FUNCTION_MAPPINGS.keys())

    def load_tools(self, tool_names: List[Union[str, Callable]], tools_directory: str = "tools"):
        """
        根据工具名称列表加载对应的工具函数，并注册到全局工具注册表中
        """
        for tool_name in tool_names:
            try:
                tool_func = load_tool(tool_name, tools_directory)
                # globals()[tool_name] = tool_func  # 添加到全局命名空间
                self.loaded_tools[tool_name] = tool_func  # 存储工具函数
                # print(f"Tool `{tool_name}` loaded successfully and added to _loaded_tools.")  # 调试信息

                # 注册工具函数
                if hasattr(tool_func, "tool_info"):
                    tool_info = tool_func.tool_info
                    _FUNCTION_INFO[tool_name] = tool_info  # 注册工具info信息
                    _FUNCTION_MAPPINGS[tool_name] = tool_func

                    # 构建 OpenAI 格式的工具描述
                    tool_params_openai = {}
                    tool_required = []
                    for param in tool_info["tool_params"]:
                        tool_params_openai[param["name"]] = {
                            "type": param["type"],
                            "description": param["description"],
                        }
                        if param["required"]:
                            tool_required.append(param["name"])

                    tool_def_openai = {
                        "type": "function",
                        "function": {
                            "name": tool_name,
                            "description": tool_info["tool_description"],
                            "parameters": {
                                "type": "object",
                                "properties": tool_params_openai,
                                "required": tool_required,
                            },
                        }
                    }
                    _OPENAI_FUNCTION_SCHEMAS.append(tool_def_openai)

                self.log("DEBUG", "load_tools success", {"tools": tool_name})
            except Exception as e:
                if register_tool_manually([tool_name]):
                    self.log("DEBUG", "register_tool_manually success", {"tools": tool_name})
                else:
                    self.log("DEBUG", "load_tools error", {"e": e})

    def _setup_logger(self, log_level: str, log_file: Optional[str] = None) -> logging.Logger:
        """
        设置日志记录器。

        :param log_level: 日志级别（INFO, DEBUG, ERROR）。
        :param log_file: 日志文件路径。
        :return: 配置好的日志记录器。
        """
        logger = logging.getLogger(self.name)
        logger.setLevel(log_level.upper())
        logger.propagate = False  # 禁用传播到根日志记录器

        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

        # 输出到控制台
        # 仅在调试模式下输出到控制台
        if self.debug:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        # 输出到文件（如果指定了文件路径）
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger

    def log(self, level, action, data):
        """
        记录日志。

        :param level: 日志级别（INFO, DEBUG, ERROR）。
        :param action: 日志动作（如 chat, call_tool, retrieve_memory）。
        :param data: 日志数据。
        """
        if not self.debug:
            return
        log_message = f"{action}: {data}"
        if level == "DEBUG":
            self.logger.debug(log_message)
        elif level == "INFO":
            self.logger.info(log_message)
        elif level == "ERROR":
            self.logger.error(log_message)

    def run(
            self,
            query: str,
            light_swarm=None,
            stream: bool = False,
            max_retry: int = 10,
            user_id: str = "default_user",
            history: list = None,
            metadata: Optional[Dict] = None,
    ) -> Union[Generator[str, None, None], str]:
        """
        运行代理，处理用户输入。

        :param query: 用户输入。
        :param light_swarm: LightSwarm 实例，用于任务转移。
        :param stream: 是否启用流式输出。
        :param max_retry: 最大重试次数。
        :param user_id: 用户 ID。
        :param history: 历史对话 。
        :param metadata: 元数据。
        :return: 代理的回复。
        """
        self.log("INFO", "run", {"query": query, "user_id": user_id, "light_swarm": light_swarm, "stream": stream})
        if history is None:
            history = []
        # 构建消息列表，先添加系统提示信息
        params = {}

        # 1. 判断是否需要转移任务
        # if light_swarm:
        #     intent = self._detect_intent(query, light_swarm)
        #     if intent and intent.get("transfer_to"):
        #         target_agent_name = intent["transfer_to"]
        #         self.log("INFO", "detect_intent", {"intent": intent})
        #         print(light_swarm.agents[target_agent_name])
        #         self._transfer_to_agent(light_swarm.agents[target_agent_name], query, stream=stream)
        #         return  # 立即结束当前生成器

        # 1. 判断是否需要转移任务
        if light_swarm:
            result = self._handle_task_transfer(query, light_swarm, stream)
            if result is not None:
                return result

        # 2. 正常处理任务
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")
        system_prompt = f"##代理名称：{self.name} ##代理指令 /n{self.instructions}  ##身份 /n {self.role} /n 请一步一步思考来完成用户的要求。尽可能完成用户的回答，如果有补充信息，请参考补充信息来调用工具，直到获取所有满足用户的提问所需的答案。 /n 今日的日期: {current_date} 当前时间: {current_time}"
        params = dict(model=self.model, stream=stream)
        memory = ''
        # 3. 从记忆中检索相关内容&保存记忆
        if self.memory:
            related_memories = self.memory.retrieve(query=query, user_id=user_id)
            memory = memory + self._build_context(related_memories)
            self.memory.store(data=query, user_id=user_id)
            if self.self_learning:
                agent_memories = self.memory.retrieve(query=query, user_id=self.name)
                memory = memory + self._build_agent_memory(agent_memories)
                self.memory.store(data=query, user_id=self.name)

        query = f"{memory}\n##用户提问：\n{query}"
        # print(query)

        # 4. 拼接tools工具
        if self.tools:
            self.log("DEBUG", "register_tools", {"tools": list(_FUNCTION_MAPPINGS.keys())})
            tools = get_tools()
            params["tools"] = tools
            params["tool_choice"] = "auto"

        # 5. 思维链
        if self.tree_of_thought:
            tot_response = self.run_thought(query=query)
            system_prompt = system_prompt + f" /n ##以下是问题的补充说明 /n {tot_response}"
            self.log("DEBUG", "tree_of_thought", {"response": tot_response})

        # 6. 调用核心运行逻辑
        params["messages"] = [{"role": "system", "content": system_prompt}]
        # 将历史对话添加到消息列表中
        for item in history:
            params["messages"].append({"role": item["role"], "content": item["content"]})
        # 最后添加当前用户的查询信息
        params["messages"].append({"role": "user", "content": query})
        response = self.client.chat.completions.create(**params)

        result = self._core_run_logic(response, params, stream, max_retry)

        return result

    def _run_logic_non_stream(self, response, params, max_retry) -> Union[str, None]:
        """
        非流式处理逻辑。
        """
        for _ in range(max_retry):
            if response.choices[0].message.tool_calls:
                # 初始化一个列表，用于存储所有工具调用的结果
                tool_responses = []
                # 初始化变量
                output = ""
                function_call_name = ""
                tool_calls = response.choices[0].message.tool_calls
                self.log("DEBUG", "non_stream tool_calls", {"tool_calls": tool_calls})

                # 遍历所有工具调用
                for tool_call in tool_calls:
                    function_call = tool_call.function

                    # 尝试自动修复常见转义问题
                    fixed_args = function_call.arguments.replace('\\"', '"').replace('\\\\', '\\')
                    self.log("DEBUG", "non_stream function_call", {"function_call": fixed_args})

                    function_args = json.loads(fixed_args)
                    # 解析函数参数
                    # function_args = json.loads(function_call.arguments)

                    # 调用工具并获取响应
                    tool_response = asyncio.run(dispatch_tool(function_call.name, function_args))
                    function_call_name = function_call.name
                    combined_response = ""
                    single_tool_response = ""

                    # 如果工具返回的是生成器（流式输出），则将所有 chunk 叠加
                    if isinstance(tool_response, Generator):
                        # print(f"Streaming response from tool: {function_call.name}")
                        for chunk in tool_response:
                            # print("Received chunk:", chunk)  # 打印每个 chunk
                            if function_call_name == 'finish':
                                content = chunk.choices[0].delta.content or ""
                                combined_response += content  # 将每个 chunk 叠加
                            else:
                                combined_response += chunk  # 将每个 chunk 叠加
                        if combined_response == "":
                            combined_response = "".join(tool_response)

                        # 将 combined_response 解析为 JSON 对象（如果它是 JSON 字符串）
                        try:
                            combined_response = json.loads(combined_response)  # 解析 JSON
                        except json.JSONDecodeError:
                            pass  # 如果不是 JSON 字符串，保持原样

                        # 将 JSON 对象中的 Unicode 编码转换为中文字符
                        if isinstance(combined_response, dict):
                            combined_response = json.dumps(combined_response, ensure_ascii=False)  # 确保中文字符不转义
                        single_tool_response = combined_response  # 处理单个工具的方法

                    else:
                        # print(f"Non-streaming response from tool: {function_call.name}")
                        combined_response = tool_response
                        # print("tool_response type:",type(combined_response))
                        # 如果是 JSON 字符串，解析并转换为中文
                        if isinstance(combined_response, str):
                            try:
                                combined_response = json.loads(combined_response)  # 解析 JSON
                                combined_response = json.dumps(combined_response, ensure_ascii=False)  # 转换为中文
                            except json.JSONDecodeError:
                                combined_response = tool_response
                                pass  # 如果不是 JSON 字符串，保持原样
                        single_tool_response = combined_response  # 处理单个工具的方法


                    self.log("DEBUG", "non_stream single_tool_response", {"single_tool_response": single_tool_response})

                    # 将单个工具的响应结果添加到列表中
                    tool_responses.append(single_tool_response)

                # 将所有工具调用的结果合并为一个字符串
                self.log("DEBUG", "non_stream tool_responses", {"tool_responses": tool_responses})

                combined_tool_response = "\n".join(tool_responses)

                # 将工具调用和响应添加到消息列表中
                params["messages"].append(
                    {
                        "role": "assistant",
                        "content": f"使用工具： \n {json.dumps([tool_call.function.model_dump() for tool_call in tool_calls],ensure_ascii=False)}\n",
                    }
                )
                params["messages"].append(
                    {
                        "role": "user",
                        "content": f"工具响应内容：\n {combined_tool_response} \n 请给出下一步输出",
                    }
                )
            else:
                # 返回最终回复
                reply = response.choices[0].message.content
                self.log("INFO", "final_reply", {"reply": reply})
                return reply

            # 更新响应
            if function_call_name == 'finish':
                return  # 如果最后调用了finish工具，则结束生成器
            # print("params:",params)
            self.log("DEBUG", "chat-completions params", {"params": params})

            try:
                response = self.client.chat.completions.create(**params)
            except Exception as e:
                print(f"An error occurred: {e}")

        # 重试次数用尽
        self.log("ERROR", "max_retry_reached", {"message": "Failed to generate a valid response."})
        return "Failed to generate a valid response."

    def _run_logic_stream(self, response, params, max_retry) -> Generator[str, None, None]:
        """
        流式处理逻辑。
        """
        for _ in range(max_retry):
            # 初始化变量
            output = ""
            function_call_name = ""
            function_call_arguments = ""
            tool_calls = []  # 用于存储所有工具调用的信息
            tool_responses = []  # 用于存储所有工具调用的结果

            for chunk in response:
                content = chunk.choices[0].delta.content or ""
                if content:
                    yield chunk  # 流式返回内容
                    output += content

                try:
                    # 检查是否有工具调用
                    if chunk.choices and chunk.choices[0].delta.tool_calls:
                        tool_call_delta = chunk.choices[0].delta.tool_calls[0]

                        # 获取工具调用的索引，确保它是有效的整数
                        tool_call_index = tool_call_delta.index if hasattr(tool_call_delta,
                                                                           "index") and tool_call_delta.index is not None else 0

                        # 如果工具调用信息尚未记录，初始化一个空字典
                        if len(tool_calls) <= tool_call_index:
                            tool_calls.append({"name": "", "arguments": "", "index": tool_call_index})

                        # 更新工具调用的名称
                        if hasattr(tool_call_delta.function, "name") and tool_call_delta.function.name:
                            tool_calls[tool_call_index]["name"] = tool_call_delta.function.name

                        # 更新工具调用的参数
                        if hasattr(tool_call_delta.function, "arguments") and tool_call_delta.function.arguments:
                            tool_calls[tool_call_index]["arguments"] += tool_call_delta.function.arguments

                except (IndexError, AttributeError, KeyError):
                    pass

                # 如果流式输出结束
                if chunk.choices[0].finish_reason == "stop" and not any(tool_call["name"] for tool_call in tool_calls):
                    self.log("INFO", "stream_response", {"output": output})
                    return  # 结束生成器

                # 如果工具调用结束
                elif chunk.choices[0].finish_reason == "tool_calls" or (
                        chunk.choices[0].finish_reason == "stop" and any(
                    tool_call["name"] for tool_call in tool_calls)):
                    # 遍历所有工具调用
                    self.log("DEBUG", "tool_calls", {"tool_calls": tool_calls})
                    for tool_call in tool_calls:
                        if tool_call["name"]:  # 确保工具调用有名称
                            function_call = {
                                "name": tool_call["name"],
                                "title": _FUNCTION_INFO.get(tool_call["name"], {}).get('tool_title') or '',
                                "arguments": tool_call["arguments"],
                            }
                            self.log("INFO", "tool_call", {"function_call": function_call})
                            # 将工具的调用信息推送给开发者
                            yield function_call

                            # 解析参数并调用工具
                            try:
                                # 使用正则表达式将多个 JSON 对象拆分开
                                json_objects = re.findall(r'\{.*?\}', function_call["arguments"])

                                # 解析每个 JSON 对象并调用工具
                                # for json_obj in json_objects:
                                #     function_args = json.loads(json_obj)
                                #     tool_response = dispatch_tool(function_call["name"], function_args)
                                #     tool_responses.append(tool_response)

                                for json_obj in json_objects:
                                    function_args = json.loads(json_obj)
                                    # tool_response = dispatch_tool(function_call["name"], function_args)
                                    tool_response = asyncio.run(dispatch_tool(function_call["name"], function_args))
                                    function_call_name = function_call["name"]
                                    combined_response = ""
                                    single_tool_response = ""

                                    # 如果工具返回的是生成器（流式输出），则将所有 chunk 叠加
                                    if isinstance(tool_response, Generator):
                                        # print(f"Streaming response from tool: {function_call['name']}")
                                        for chunk in tool_response:
                                            # 将工具返回的数据继续流出
                                            if isinstance(chunk, ChatCompletionChunk):
                                                yield chunk
                                            else:
                                                tool_output = {
                                                    "name": tool_call["name"],
                                                    "title": _FUNCTION_INFO.get(tool_call["name"], {}).get(
                                                        'tool_title') or '',
                                                    "output": chunk,
                                                }
                                                self.log("INFO", "tool_call", {"tool_output": tool_output})
                                                yield tool_output
                                            # 将工具的调用信息推送给开发者
                                            if function_call_name == 'finish':
                                                content = chunk.choices[0].delta.content or ""
                                                combined_response += content  # 将每个 chunk 叠加
                                            else:
                                                combined_response += chunk  # 将每个 chunk 叠加
                                        single_tool_response = combined_response  # 处理单个工具的方法
                                    else:
                                        # print(f"Non-streaming response from tool: {tool_response}")
                                        combined_response = tool_response
                                        single_tool_response = combined_response  # 处理单个工具的方法
                                    self.log("INFO", "stream single_tool_response", {"single_tool_response": single_tool_response})
                                    # 将单个工具的响应结果添加到列表中
                                    tool_responses.append(single_tool_response)

                            except json.JSONDecodeError as e:
                                self.log("ERROR", "json_decode_error",
                                         {"error": str(e), "arguments": function_call["arguments"]})
                                continue

                    # 将所有工具调用的结果合并为一个字符串
                    combined_tool_response = "\n".join(tool_responses)

                    # 将工具调用和响应添加到消息列表中
                    params["messages"].append(
                        {
                            "role": "assistant",
                            "content": json.dumps(
                                [{"name": tool_call["name"], "arguments": tool_call["arguments"]} for tool_call in
                                 tool_calls]
                            ),
                        }
                    )
                    params["messages"].append(
                        {
                            "role": "user",
                            "content": combined_tool_response,
                        }
                    )

                    break

            # 更新响应
            if function_call_name == 'finish':
                return  # 如果最后调用了finish工具，则结束生成器
            self.log("DEBUG", "chat-completions params", {"params": params})
            response = self.client.chat.completions.create(**params)

        # 重试次数用尽
        self.log("ERROR", "max_retry_reached", {"message": "Failed to generate a valid response."})
        yield "Failed to generate a valid response."

    def _core_run_logic(self, response, params, stream, max_retry) -> Union[Generator[str, None, None], str]:
        """
        核心运行逻辑。
        """
        if stream:
            return self._run_logic_stream(response, params, max_retry)
        else:
            return self._run_logic_non_stream(response, params, max_retry)

    def _handle_task_transfer(
            self,
            query: str,
            light_swarm: 'LightSwarm',
            stream: bool = False,
    ) -> Union[Generator[str, None, None], str, None]:
        """
        处理任务转移逻辑。

        :param query: 用户输入。
        :param light_swarm: LightSwarm 实例。
        :param stream: 是否启用流式输出。
        :return: 如果任务需要转移，返回生成器或字符串；否则返回 None。
        """
        intent = self._detect_intent(query, light_swarm)
        if intent and intent.get("transfer_to"):
            target_agent_name = intent["transfer_to"]
            self.log("INFO", "detect_intent", {"intent": intent})
            if target_agent_name == self.name:
                self.log("INFO", "self_transfer_detected", {"target_agent": target_agent_name})
                return None  # 如果是自身，直接返回 None
            if stream:
                return self._handle_task_transfer_stream(light_swarm.agents[target_agent_name], query, light_swarm)
            else:
                return self._handle_task_transfer_non_stream(light_swarm.agents[target_agent_name], query, light_swarm)
        return None

    def _handle_task_transfer_stream(
            self,
            target_agent: 'LightAgent',
            context: str,
            light_swarm: 'LightSwarm',
    ) -> Generator[str, None, None]:
        """
        处理任务转移逻辑（流式输出）。

        :param target_agent: 目标代理。
        :param context: 共享的上下文信息。
        :param light_swarm: LightSwarm 实例。
        :return: 生成器，用于流式输出。
        """
        self.log("INFO", "transfer_to_agent", {"from": self.name, "to": target_agent.name, "context": context})

        # 检查目标代理是否有效
        if not hasattr(target_agent, 'run'):
            self.log("ERROR", "invalid_target_agent", {"target_agent": target_agent})
            yield "Failed to transfer task: invalid target agent"
            return

        try:
            yield from target_agent.run(context, light_swarm=light_swarm, stream=True)
        except Exception as e:
            self.log("ERROR", "run_failed", {"error": str(e)})
            raise  # 重新抛出异常以便调试

    def _handle_task_transfer_non_stream(
            self,
            target_agent: 'LightAgent',
            context: str,
            light_swarm: 'LightSwarm',
    ) -> str:
        """
        处理任务转移逻辑（非流式输出）。

        :param target_agent: 目标代理。
        :param context: 共享的上下文信息。
        :param light_swarm: LightSwarm 实例。
        :return: 字符串，表示非流式输出结果。
        """
        self.log("INFO", "transfer_to_agent", {"from": self.name, "to": target_agent.name, "context": context})

        # 检查目标代理是否有效
        if not hasattr(target_agent, 'run'):
            self.log("ERROR", "invalid_target_agent", {"target_agent": target_agent})
            return "Failed to transfer task: invalid target agent"

        try:
            result = target_agent.run(context, light_swarm=light_swarm, stream=False)
            if isinstance(result, Generator):
                return "".join(result)  # 将生成器转换为字符串
            return result
        except Exception as e:
            self.log("ERROR", "run_failed", {"error": str(e)})
            raise  # 重新抛出异常以便调试

    def _build_context(self, related_memories):
        """
        构建上下文，将用户输入和记忆内容结合。
        :param related_memories: 从记忆中检索到的相关内容。
        :return: 结合记忆后的上下文。
        """
        if not related_memories or not related_memories["memories"]:
            return ""

        memory_context = "\n".join([m["memory"] for m in related_memories["memories"]])
        if not memory_context:
            return ""

        prompt = f"\n##用户偏好 \n用户之前提到了\n{memory_context}。"
        self.log("DEBUG", "related_memories", {"memory_context": memory_context})
        return prompt

    def _build_agent_memory(self, agent_memories):
        """
        构建上下文，将用户输入和记忆内容结合。

        :param agent_memories: 从记忆中检索到的相关内容。
        :return: 结合记忆后的上下文。
        """
        if not agent_memories or not agent_memories["memories"]:
            return ""

        memory_context = "\n".join([m["memory"] for m in agent_memories["memories"]])
        if not memory_context:
            return ""

        prompt = f"\n##以下是解决该问题的相关补充信息：\n{memory_context}。"
        self.log("DEBUG", "agent_memories", {"memory_context": memory_context})
        return prompt

    def run_thought(self, query: str, stream=False, tools=None):
        """使用思维树的方式 让大模型先根据get_tools_str生成一个解答用户query的工具使用计划"""
        tot_model = self.tot_model  # self.model
        tools = get_tools_str()
        if not isinstance(tools, str):
            tools = str(tools)  # 确保 tools 是字符串
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")
        system_prompt = f"""你是一个智能助手，请根据用户输入的问题，结合工具使用计划，生成一个思维树，并按照思维树依次调用工具步骤，最终生成一个最终回答。/n 今日的日期: {current_date} 当前时间: {current_time} /n 工具列表: {tools}"""
        self.log("DEBUG", "run_thought", {"system_prompt": system_prompt})

        # 第一次请求，生成初始的工具使用计划
        params = dict(model=tot_model,
                      messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": query}],
                      stream=False)
        response = self.tot_client.chat.completions.create(**params)
        initial_content = response.choices[0].message.content
        self.log("DEBUG", "initial_response", {"response": initial_content})

        # 第二次请求，请求大模型反思并生成新的工具使用规划
        reflection_prompt = "请反思你的回答，重新给出新的工具使用规划。仅输出新的工具使用规划，不要输出其他分析和回答。"
        reflection_params = dict(model=tot_model, messages=[
            {"role": "user", "content": f"{system_prompt} /n 开始思考问题: {query}"},
            {"role": "assistant", "content": initial_content},
            {"role": "user", "content": reflection_prompt}
        ], stream=False)
        self.log("DEBUG", "reflection_params", {"params": reflection_params})

        reflection_response = self.tot_client.chat.completions.create(**reflection_params)
        refined_content = reflection_response.choices[0].message.content
        self.log("DEBUG", "refined_response", {"response": refined_content})
        return refined_content

    def _detect_intent(self, query: str, light_swarm=None) -> Optional[Dict]:
        """
        使用大模型判断用户意图。

        :param query: 用户输入。
        :param light_swarm: LightSwarm 实例，用于获取所有代理信息。
        :return: 意图信息，例如 {"transfer_to": "Agent B"}。
        """
        if not light_swarm:
            return None

        # 获取所有代理的信息
        agents_info = []
        for agent_name, agent in light_swarm.agents.items():
            agents_info.append(f"代理名称: {agent_name}, 代理指令: {agent.instructions}")

        # 将代理信息拼接为字符串
        agents_info_str = "\n".join(agents_info)

        # 构建提示词
        prompt = f"""请分析以下用户输入的意图，如果需要转移任务，请返回目标代理的名称格式如下。
        transfer to agent_name
        以下是所有可用代理的信息：
    {agents_info_str}
    用户输入: {query}
请返回目标代理的名称：
"""

        # 调用大模型进行意图判断
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": prompt}]
        )
        intent = response.choices[0].message.content
        self.log("DEBUG", "detect_intent", {"intent": intent})

        # # 使用正则表达式解析意图
        # match = re.search(r"transfer to (\w+)", intent, re.IGNORECASE)
        # if match:
        #     target_agent_name = match.group(1)
        #     if target_agent_name in light_swarm.agents:
        #         return {"transfer_to": target_agent_name}
        # return None

        # 解析意图
        for agent_name in light_swarm.agents.keys():
            if f"transfer to {agent_name}" in intent:
                return {"transfer_to": agent_name}
        return None

    def _transfer_to_agent(
            self,
            target_agent: 'LightAgent',
            context: str,
            light_swarm=None,
            stream: bool = False,
    ) -> Union[Generator[str, None, None], str]:
        """
        将任务转移给另一个代理，支持流式和非流式输出。

        :param target_agent: 目标代理。
        :param context: 共享的上下文信息。
        :param light_swarm: LightSwarm 实例。
        :param stream: 是否启用流式输出。
        :return: 如果 stream=True，返回生成器；否则返回完整结果字符串。
        """
        self.log("INFO", "transfer_to_agent", {"from": self.name, "to": target_agent.name, "context": context})

        # 检查目标代理是否有效
        if not hasattr(target_agent, 'run'):
            self.log("ERROR", "invalid_target_agent", {"target_agent": target_agent})
            return "Failed to transfer task: invalid target agent"
        #
        # # 调用目标代理的 run 方法
        # if stream:
        #     yield from target_agent.run(context, light_swarm=light_swarm, stream=stream)
        # else:
        #     result = target_agent.run(context, light_swarm=light_swarm, stream=stream)
        #     if isinstance(result, Generator):
        #         return "".join(result)  # 将生成器转换为字符串
        #     return result
        try:
            if stream:
                yield from target_agent.run(context, light_swarm=light_swarm, stream=stream)
            else:
                result = target_agent.run(context, light_swarm=light_swarm, stream=stream)
                if isinstance(result, Generator):
                    return "".join(result)  # 将生成器转换为字符串
                return result
        except Exception as e:
            self.log("ERROR", "run_failed", {"error": str(e)})
            raise  # 重新抛出异常以便调试

    def create_tool(self, user_input: str, tools_directory: str = "tools"):
        """
        根据用户输入的文本生成 Python 代码，并将其保存为工具
        """
        # 调用大模型生成 Python 代码
        system_prompt = """
        The user will provide some exam text. Please parse the "tool_name" and "code" and output them in JSON format. 

        EXAMPLE INPUT: 
        请根据文档生成一个天气调用的工具，API介绍如下

        EXAMPLE JSON OUTPUT:
        {'tools': [{
            "tool_name": "get_weather",
            "tool_code": "import requests
            def get_weather(
        city_name: str
) -> str:
    /"/"/"
    Get the current weather for `city_name`
    /"/"/"
    if not isinstance(city_name, str):
        raise TypeError("City name must be a string")

    key_selection = {
        "current_condition": ["temp_C", "FeelsLikeC", "humidity", "weatherDesc", "observation_time"],
    }
    try:
        resp = requests.get(f"https://wttr.in/{city_name}?format=j1")
        resp.raise_for_status()
        resp = resp.json()
        ret = {k: {_v: resp[k][0][_v] for _v in v} for k, v in key_selection.items()}
    except:
        import traceback
        ret = "Error encountered while fetching weather data!\n" + traceback.format_exc()

    return str(ret)

# 在函数内部定义工具信息
get_weather.tool_info = {
    "tool_name": "get_weather",
    "tool_title": "天气查询",
    "tool_description": "获取指定城市的当前天气信息",
    "tool_params": [
        {"name": "city_name", "description": "要查询的城市名称", "type": "string", "required": True},
    ]
}"
        }]}
        """
        params = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant that generates Python code in JSON format."},
                {"role": "user", "content": f"Generate Python tools based on the following description. "
                                            f"Return a JSON array where each item contains 'tool_name' and 'tool_code'. "
                                            f"\n {system_prompt} "
                                            f"Description:\n{user_input}"},
            ],
            "response_format": {"type": "json_object"},
        }
        try:
            response = self.client.chat.completions.create(**params)
            response_data = json.loads(response.choices[0].message.content)

            # 确保返回的数据是 JSON 对象
            if not isinstance(response_data, dict):
                raise ValueError("Response is not a JSON object.")

            # 遍历每个工具
            for tool_data in response_data["tools"]:
                tool_name = tool_data.get("tool_name")
                tool_code = tool_data.get("tool_code")

                if not tool_name or not tool_code:
                    self.log("ERROR", "invalid_tool_data", {"tool_data": tool_data})
                    continue

                # 保存生成的代码到 tools 目录
                tool_path = os.path.join(tools_directory, f"{tool_name}.py")
                with open(tool_path, "w", encoding="utf-8") as f:
                    f.write(tool_code)
                self.log("INFO", "tool_created", {"tool_name": tool_name, "tool_path": tool_path})

                # 加载新创建的工具
                self.load_tools([tool_name], tools_directory)
        except Exception as e:
            self.log("ERROR", "tool_creation_failed", {"error": str(e)})


class LightSwarm:
    def __init__(self):
        self.agents: Dict[str, LightAgent] = {}

    def register_agent(self, *agents: LightAgent):
        """
        注册一个或多个代理。

        :param agents: 要注册的代理实例，支持多个代理。
        """
        for agent in agents:
            if agent.name in self.agents:
                # print(f"Agent '{agent.name}' is already registered.")
                agent.log("INFO", "register_agent", {"agent_name": agent.name, "status": "already_registered"})
            else:
                self.agents[agent.name] = agent
                # print(f"Agent '{agent.name}' registered.")
                agent.log("INFO", "register_agent", {"agent_name": agent.name, "status": "registered"})

    def run(self, agent: LightAgent, query: str, stream=False):
        """
        运行指定代理。

        :param agent_name: 代理名称。
        :param query: 用户输入。
        :return: 代理的回复。
        """
        if agent.name not in self.agents:
            raise ValueError(f"Agent '{agent.name}' not found.")
        return agent.run(query, light_swarm=self, stream=stream)


if __name__ == "__main__":
    # Example of registering and using a tool
    print("This is LightAgent")
    # print(dispatch_tool("example_tool", {"param1": "test"}))