
![LightAgent Banner](docs/images/lightagent-banner.jpg)
<div align="center">
  <p>
    <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License"></a>
    <a href="https://github.com/wxai-space/LightAgent/releases"><img src="https://img.shields.io/github/release/wxai-space/LightAgent.svg" alt="GitHub release"></a>
    <a href="https://github.com/wxai-space/LightAgent/issues"><img src="https://img.shields.io/github/issues/wxai-space/LightAgent.svg" alt="GitHub issues"></a>
    <a href="https://github.com/wxai-space/LightAgent/stargazers"><img src="https://img.shields.io/github/stars/wxai-space/LightAgent.svg" alt="GitHub stars"></a>
    <a href="https://github.com/wxai-space/LightAgent/network"><img src="https://img.shields.io/github/forks/wxai-space/LightAgent.svg" alt="GitHub forks"></a>
    <a href="https://github.com/wxai-space/LightAgent/graphs/contributors"><img src="https://img.shields.io/github/contributors/wxai-space/LightAgent.svg" alt="GitHub contributors"></a>
    <a href="https://sufe-aiflm-lab.github.io/LightAgent/"><img src="https://img.shields.io/badge/docs-latest-brightgreen.svg" alt="Docs"></a>
    <a href="https://pypi.org/project/lightagent/"><img src="https://img.shields.io/pypi/v/lightagent.svg" alt="PyPI"></a>
    <a href="https://pypi.org/project/lightagent/"><img src="https://img.shields.io/pypi/dm/lightagent.svg" alt="Downloads"></a>
    <a href="https://pypi.org/project/lightagent/"><img src="https://img.shields.io/pypi/pyversions/lightagent.svg" alt="Python Version"></a>
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style"></a>
  </p>
</div>
<div align="center">
  <p>
    <a href="README.md">English</a> | 
    <a href="README.zh-CN.md">简体中文</a> | 
    <a href="README.zh-TW.md">繁體中文</a> | 
    <a href="README.es.md">Español</a> | 
    <a href="README.fr.md">Français</a> | 
    Deutsch | 
    <a href="README.ja.md">日本語</a> | 
    <a href="README.ko.md">한국어</a> | 
    <a href="README.pt.md">Português</a> | 
    <a href="README.ru.md">Русский</a> 
  </p>
</div>

<div align="center">
  <h1>LightAgent🚀 (Nächste Generation Agentic KI-Rahmen)</h1>
</div>

**LightAgent** ist ein extrem leichtgewichtiges aktives agentisches Framework mit Gedächtnis (`mem0`), Werkzeugen (`Tools`) und Denkbaum (`ToT`). Es unterstützt die Zusammenarbeit mehrerer Agenten in einer Art Schwarm, die Automatisierung der Werkzeuggenerierung und die Bewertung von Agenten. Die zugrunde liegenden Modelle unterstützen OpenAI, Zhipu ChatGLM, Baichuan große Modelle, DeepSeek, Qwen Serien große Modelle usw. Zudem unterstützt LightAgent den OpenAI Stream-Format API-Dienstausgang und lässt sich nahtlos in alle gängigen Chat-Rahmen integrieren.🌟

---

## ✨ Eigenschaften

- **Leicht und effizient** 🚀：Extrem minimalistisches Design, schnelle Bereitstellung, geeignet für verschiedene Anwendungsszenarien. (Kein LangChain, Kein LlamaIndex) 100 % Python-Implementierung, keine zusätzlichen Abhängigkeiten, der Kerncode umfasst nur 1000 Zeilen und ist vollständig Open Source. 
- **Gedächtnisunterstützung** 🧠：Unterstützung der benutzerdefinierten Langzeiterinnerungen für jeden Benutzer, native Unterstützung des `mem0` Gedächtnismoduls, das die personalisierten Erinnerungen der Benutzer während des Dialogs automatisch verwaltet und die Intelligenz des Agenten erhöht.
- **Selbstlernen** 📚️：Jeder Agent verfügt über die Fähigkeit zum Selbstlernen, und Administratoren mit den entsprechenden Berechtigungen können jeden Agenten verwalten.
- **Werkzeugintegration** 🛠️：Unterstützung für benutzerdefinierte Werkzeuge (`Tools`), automatisierte Werkzeuggenerierung, flexible Erweiterung, um vielfältige Anforderungen zu erfüllen.  
- **Komplexe Ziele** 🌳：Eingebautes modul mit reflektierender Denkbaumstruktur (ToT), unterstützt die Zerlegung komplexer Aufgaben und Mehrschritt-Inferenz, um die Aufgabenbearbeitungsfähigkeiten zu verbessern.  
- **Kollaboration mehrerer Agenten** 🤖：Einfachere Umsetzung der Zusammenarbeit mehrerer Agenten als beim Schwarmansatz, mit eingebautem LightSwarm zur Intentionserkennung und Aufgabenübertragungsfunktion, die die Benutzereingaben intelligenter verarbeiten kann und bei Bedarf Aufgaben an andere Agenten überträgt. 
- **Unabhängige Ausführung** 🤖：Selbstständige Durchführung der Aufgabenwerkzeugaufrufe ohne menschliches Eingreifen.  
- **Unterstützung mehrerer Modelle** 🔄：Kompatibel mit OpenAI, Zhipu ChatGLM, Baichuan große Modelle, Jieyue Xingchen, DeepSeek, Qwen Serien große Modelle.  
- **Stream API** 🌊：Unterstützt den OpenAI Stream-Format API-Dienstausgang, nahtlose Integration in gängige Chat-Rahmen, um die Benutzererfahrung zu verbessern.  
- **Tools Werkzeuggenerator** 🚀：Übergeben Sie einfach Ihre API-Dokumentation an den [Tools Werkzeuggenerator], der Ihnen automatisiert Ihre exklusiven Werkzeuge erstellt und Ihnen hilft, in nur einer Stunde hunderte von personalisierten benutzerdefinierten Werkzeugen schnell zu erstellen, die Effizienz zu steigern und Ihr kreatives Potenzial freizusetzen.


## 🚧 Kommende Funktionen

- **Adaptives Tools-Mechanismus** 🛠️：Unterstützung für die Hinzufügung einer unbegrenzten Anzahl von Werkzeugen, wobei das große Modell zunächst eine Auswahl zusätzlicher Kandidatenwerkzeuge aus Tausenden von Werkzeugen auswählt, nachdem unwichtige Werkzeuge gefiltert wurden, um den Kontext dem großen Modell zu übermitteln, was den Tokenverbrauch erheblich reduziert.
- **Agentenzusammenarbeit mit Gedächtnis** 🛠️：Agenten können Informationen teilen und Nachrichten übertragen, um komplexe Aufgabenkooperation zu erreichen.
- **Agent selbst lernen** 🧠️：Jeder Agent hat die Fähigkeit zur Szenario-Gedächtnisbildung und kann aus Gesprächen mit Benutzern lernen.
- **Agent Bewertung** 📊：Integrierte Agent-Bewertungstools zur einfachen Bewertung und Optimierung des von Ihnen erstellten Agenten, zur Anpassung an Geschäftsszenarien und zur kontinuierlichen Verbesserung des Intelligenzlevels.  


## Eingebauter "Denkfluss"
(Methode für den Denkfluss) kann durch systematische, strukturierte und flexible Denkprozesse effektiv auf Herausforderungen in komplexen Szenarien reagieren. 
Folgend sind die spezifischen Umsetzungsschritte:
```text
Problemdefinition: Klärung des Kernproblems und der Ziele.

Informationssammlung: Systematische Sammlung relevanter Informationen und Daten.

Problemauslegung: Zerlegung komplexer Probleme in mehrere Unterprobleme oder Module.

Multidimensionale Analyse: Analyse jedes Unterproblems aus verschiedenen Perspektiven und Ebenen.

Beziehungsaufbau: Identifizierung der Zusammenhänge und Abhängigkeiten zwischen den Unterproblemen.

Erstellung von Lösungsvorschlägen: Vorschlagen möglicher Lösungen für jedes Unterproblem.

Bewertung und Auswahl: Bewertung der Durchführbarkeit und Auswirkung der verschiedenen Lösungsansätze, Auswahl der besten Lösung.

Umsetzung und Feedback: Umsetzung des ausgewählten Plans und Anpassung basierend auf dem Feedback.
```

---
## 🌟 Warum LightAgent wählen?

- **Open Source und kostenlos** 💖：Vollständig Open Source, von der Community betrieben, kontinuierliche Updates, Beiträge sind willkommen!  
- **Einfach zu bedienen** 🎯：Detaillierte Dokumentation, umfangreiche Beispiele, schnelle Einarbeitungszeit, einfache Integration in Ihr Projekt.  
- **Community-Unterstützung** 👥：Aktive Entwickler-Community, die Ihnen jederzeit hilft und Antworten gibt.  
- **Hohe Leistung** ⚡：Optimiertes Design, effiziente Ausführung, erfüllt die Anforderungen an hochgradige Parallelverarbeitung.  

---

## 🛠️ Schnellstart

### Installation der neuesten Version von LightAgent

```bash
pip install lightagent
```

(Optionaler Installationsbefehl) Um das Mem0-Paket über pip zu installieren:

```bash
pip install mem0ai
```

Oder Sie können Mem0 mit nur einem Klick auf einer gehosteten Plattform verwenden, [klicken Sie hier](https://www.mem0.ai/).


### Hello World Beispielcode

```python
from LightAgent import LightAgent

# Initialisierung des Agenten
agent = LightAgent(model="gpt-4o-mini", api_key="your_api_key", base_url= "your_base_url")

# Ausführen des Agenten
response = agent.run("你好，你是谁？")
print(response)
```

### Modell-Selbstwahrnehmung über System-Prompts festlegen

```python
from LightAgent import LightAgent

# Initialisierung des Agenten
agent = LightAgent(
     role="请记住你是LightAgent，一个可以帮助用户完成多工具使用的有用助手。",  # system角色描述
     model="deepseek-chat",  # 支持的模型：openai, chatglm, deepseek, qwen 等
     api_key="your_api_key",  # 替换为你的大模型服务商 API Key
     base_url="your_base_url",  # 替换为你的大模型服务商 api url
 )
# Ausführen des Agenten
response = agent.run("请问你是谁？")
print(response)
```

### Werkzeugbeispielcode

```python
from LightAgent import LightAgent


# Werkzeug definieren
def get_weather(city_name: str) -> str:
    """
    获取城市的当前天气
    """
    return f"查询结果: {city_name} 天气晴"
# Werkzeuginformationen innerhalb der Funktion definieren
get_weather.tool_info = {
    "tool_name": "get_weather",
    "tool_description": "获取指定城市的当前天气信息",
    "tool_params": [
        {"name": "city_name", "description": "要查询的城市名称", "type": "string", "required": True},
    ]
}

tools = [get_weather]

# Initialisierung des Agenten
agent = LightAgent(model="qwen-turbo-2024-11-01", api_key="your_api_key", base_url= "your_base_url", tools=tools)

# Ausführen des Agenten
response = agent.run("请帮我查询一下上海的天气情况")
print(response)
```
Unterstützung von benutzerdefinierten und unbegrenzten Werkzeugen.

Beispiel für mehrere Werkzeuge: tools = ["search_news","get_weather","get_stock_realtime_data","get_stock_kline_data"]

---

## Funktionale Details

### 1. Abnehmbares vollautomatisches Gedächtnismodul (`mem0`)
LightAgent unterstützt die externe Erweiterung des `mem0` Gedächtnismoduls zur automatischen Verwaltung von Kontextgedächtnis und Historie, ohne dass der Entwickler manuell Erinnerungen hinzufügen oder Abrufen auslösen muss. Über das Gedächtnismodul kann der Agent während mehrerer Dialoge die Konsistenz des Kontextes aufrechterhalten.

```python
# Aktivierung des Gedächtnismoduls

# Oder verwenden Sie ein benutzerdefiniertes Gedächtnismodul, hier zum Beispiel mem0 https://github.com/mem0ai/mem0/
from mem0 import Memory
from LightAgent import LightAgent
import os
from loguru import logger

class CustomMemory:
    def __init__(self):
        self.memories = []
        os.environ["OPENAI_API_KEY"] = "your_api_key"
        os.environ["OPENAI_API_BASE"] = "your_base_url"
        # Initialize Mem0
        config = {
            "version": "v1.1"
        }
        # mem0中 如需使用qdrant作为向量数据库存储记忆，请将config改为下面代码
        # config = {
        #     "vector_store": {
        #         "provider": "qdrant",
        #         "config": {
        #             "host": "localhost",
        #             "port": 6333,
        #         }
        #     },
        #     "version": "v1.1"
        # }
        self.m = Memory.from_config(config_dict=config)

    def store(self, data: str, user_id):
        """Speichern von Erinnerungen. Entwickler können die interne Implementierung der Speicherungsmethode nach eigenem Ermessen ändern. Das aktuelle Beispiel verwendet die Methode zum Hinzufügen von Erinnerungen von mem0."""
        result = self.m.add(data, user_id=user_id)
        return result

    def retrieve(self, query: str, user_id):
        """Abruf relevanter Erinnerungen. Entwickler können die interne Implementierung der Abrufmethode nach eigenem Ermessen ändern. Das aktuelle Beispiel verwendet die Methode zum Suchen von Erinnerungen von mem0."""
        result = self.m.search(query, user_id=user_id)
        return result

agent = LightAgent(
        role="请记住你是LightAgent，一个可以帮助用户完成多工具使用的有用助手。",  # system角色描述
        model="deepseek-chat",  # 支持的模型：openai, chatglm, deepseek, qwen 等
        api_key="your_api_key",  # 替换为你的大模型服务商 API Key
        base_url="your_base_url",  # 替换为你的大模型服务商 api url
        memory=CustomMemory(),  # 启用记忆功能
        tree_of_thought=False,  # 启用思维链
    )

# Gedächtnis-Test & falls weitere Werkzeuge hinzugefügt werden sollen, können diese selbst zum Agenten hinzugefügt werden, um Werkzeugaufrufe mit Gedächtnis zu realisieren

user_id = "user_01"
logger.info("\n=========== next conversation ===========")
query = "介绍下三亚的有什么好玩的景点，身边很多朋友都去三亚旅游了，我也想去玩"
print(agent.run(query, stream=False, user_id=user_id))
logger.info("\n=========== next conversation ===========")
query = "我想去哪里旅游呢？"
print(agent.run(query, stream=False, user_id=user_id))
```

Ausgabe wie folgt:
```python
=========== next conversation ===========
2025-01-01 21:55:15.886 | INFO     | __main__:run_conversation:115 - 
开始思考问题: 介绍下三亚的有什么好玩的景点，身边很多朋友都去三亚旅游了，我也想去玩
2025-01-01 21:55:28.676 | INFO     | __main__:run_conversation:118 - Final Reply: 
三亚是中国海南省的一个热门旅游城市，以其美丽的海滩、热带气候和丰富的旅游资源而闻名。以下是一些三亚值得一游的景点：

1. **亚龙湾**：被誉为“东方夏威夷”，拥有绵长的沙滩和清澈的海水，是游泳、潜水和日光浴的理想之地。

2. **天涯海角**：这是一个著名的文化景观，以其壮丽的海景和浪漫的传说而吸引游客。这里的巨石上刻有“天涯”和“海角”字样，象征着永恒的爱情。

3. **南山文化旅游区**：这里有一个高达108米的南山海上观音像，是世界上最高的海上观音像。游客可以在这里体验佛教文化，参观寺庙和园林。

4. **蜈支洲岛**：这是一个小岛，以其原始的自然风光和丰富的水上活动而闻名。游客可以在这里进行潜水、浮潜、海钓等活动。

5. **大东海**：这是三亚市区内的一个海滩，以其便利的交通和丰富的夜生活而受到游客的喜爱。

6. **三亚湾**：这是一个长达22公里的海滩，是观赏日落的好地方。这里的海滩较为安静，适合喜欢宁静的游客。

7. **呀诺达雨林文化旅游区**：这是一个热带雨林公园，游客可以在这里体验热带雨林的自然风光，参与各种探险活动。

8. **鹿回头公园**：这是一个位于山顶的公园，可以俯瞰整个三亚市区和三亚湾的美景。这里还有一个关于鹿的美丽传说。

9. **西岛**：这是一个相对较为原始的小岛，以其宁静的海滩和丰富的海洋生物而吸引游客。

10. **三亚千古情**：这是一个大型的文化主题公园，通过表演和展览展示海南的历史和文化。

除了上述景点，三亚还有许多其他值得探索的地方，如热带植物园、海鲜市场等。三亚的美食也不容错过，尤其是新鲜的海鲜和热带水果。在规划旅行时，建议提前查看天气预报和景点开放时间，以确保有一个愉快的旅行体验。
2025-01-01 21:55:28.676 | INFO     | __main__:<module>:191 - 
=========== next conversation ===========
2025-01-01 21:55:28.676 | INFO     | __main__:run_conversation:115 - 
开始思考问题: 我想去哪里旅游呢？
发现相关记忆:
User wants to travel to Sanya
User's friends have traveled to Sanya。
2025-01-01 21:55:38.797 | INFO     | __main__:run_conversation:118 - Final Reply: 
根据用户之前提到的信息，用户的朋友已经去过三亚（Sanya），而用户自己也表达了对三亚的兴趣。因此，三亚可能是一个适合用户的旅游目的地。以下是一些关于三亚的旅游信息，供用户参考：

### 三亚旅游推荐：
1. **亚龙湾**：被誉为“东方夏威夷”，拥有美丽的海滩和清澈的海水，适合游泳和日光浴。
2. **天涯海角**：三亚的标志性景点，以其独特的岩石和浪漫的传说吸引游客。
3. **南山文化旅游区**：这里有著名的南山寺和108米高的海上观音像，是佛教文化的重要景点。
4. **蜈支洲岛**：适合潜水和海上运动，岛上有丰富的海洋生物和珊瑚礁。
5. **大东海**：三亚市区内的海滩，交通便利，适合家庭和情侣游玩。

### 其他推荐：
如果用户对三亚已经有所了解，或者想要探索其他目的地，以下是一些其他热门旅游地：
1. **桂林**：以其独特的喀斯特地貌和漓江风光闻名。
2. **丽江**：古城和玉龙雪山是其主要景点，适合喜欢历史文化和自然风光的游客。
3. **张家界**：以其奇特的石柱和自然景观著称，是《阿凡达》电影的取景地之一。

用户可以根据自己的兴趣和时间安排选择合适的旅游目的地。如果用户需要更详细的信息或帮助规划行程，请随时告知！
```

### 2. Werkzeugintegration (Unendliche individuelle Werkzeugunterstützung)
Begrüßen Sie die personalisierte Werkzeuganpassung (`Tools`) und integrieren Sie mühelos Ihre exklusiven Werkzeuge über die `tools`-Methode. Diese Werkzeuge können beliebige Python-Funktionen sein und unterstützen Typanmerkungen für Parameter, um Flexibilität und Präzision sicherzustellen. Darüber hinaus bieten wir einen intelligenten, KI-gesteuerten Werkzeuggenerator an, der Ihnen hilft, Werkzeuge automatisch zu erstellen und Ihre Kreativität freizusetzen.

```python

import requests
from LightAgent import LightAgent

# Werkzeug definieren
def get_weather(
        city_name: str
) -> str:
    """
    获取城市天气信息
    :param city_name: 城市名称
    :return: 天气信息
    """
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
# Werkzeuginformationen innerhalb der Funktion definieren
get_weather.tool_info = {
    "tool_name": "get_weather",
    "tool_description": "获取指定城市的当前天气信息",
    "tool_params": [
        {"name": "city_name", "description": "要查询的城市名称", "type": "string", "required": True},
    ]
}

def search_news(
        keyword: str,
        max_results: int = 5
) -> str:
    """
    根据关键词搜索新闻
    :param keyword: 搜索关键词
    :param max_results: 返回的最大结果数量，默认为 5
    :return: 新闻搜索结果
    """
    results = f"通过搜索{keyword}, 我找到{max_results}条相关信息"
    return str(results)

# Werkzeuginformationen innerhalb der Funktion definieren
search_news.tool_info = {
    "tool_name": "search_news",
    "tool_description": "根据关键词搜索新闻",
    "tool_params": [
        {"name": "keyword", "description": "搜索关键词", "type": "string", "required": True},
        {"name": "max_results", "description": "返回的最大结果数量", "type": "int", "required": False},
    ]
}

def get_user_info(
        user_id: str
) -> str:
    """
    获取用户信息
    :param user_id: 用户 ID
    :return: 用户信息
    """
    if not isinstance(user_id, str):
        raise TypeError("User ID must be a string")

    try:
        # 假设使用一个用户信息 API，这里用示例 URL
        url = f"https://api.example.com/users/{user_id}"
        response = requests.get(url)
        response.raise_for_status()
        user_data = response.json()
        user_info = {
            "name": user_data.get("name"),
            "email": user_data.get("email"),
            "created_at": user_data.get("created_at")
        }
    except:
        import traceback
        user_info = "Error encountered while fetching user data!\n" + traceback.format_exc()

    return str(user_info)

# Werkzeuginformationen innerhalb der Funktion definieren
get_user_info.tool_info = {
    "tool_name": "get_user_info",
    "tool_description": "获取指定用户的信息",
    "tool_params": [
        {"name": "user_id", "description": "用户 ID", "type": "string", "required": True},
    ]
}

# Benutzerdefinierte Werkzeuge
tools = [get_weather, search_news, get_user_info]  # 包含所有工具

# Initialisierung des Agenten
# 替换为你的模型参数model、api_key、base_url
agent = LightAgent(model="qwen-turbo-2024-11-01", api_key="your_api_key", base_url= "your_base_url", tools=tools)

query = "当前三亚天气如何？"
response = agent.run(query, stream=False)  # 使用 agent 运行查询
print(response)
```

### 3. Tools 工具生成器
Tools 工具生成器 ist ein Modul zur automatischen Erstellung von Werkzeugcode. Es kann auf der Grundlage der vom Benutzer bereitgestellten Textbeschreibung den entsprechenden Werkzeugcode automatisch generieren und ihn im angegebenen Verzeichnis speichern. Diese Funktion ist besonders nützlich, wenn schnell API-Aufrufwerkzeuge, Datenverarbeitungswerkzeuge usw. erzeugt werden müssen.

Verwendungsbeispiele

Hier ist ein Beispielcode zur Verwendung des Tools Werkzeuggenerators:

```python
import json
import os
import sys
from LightAgent import LightAgent

# 初始化LightAgent
agent = LightAgent(
    name="Agent A",  # 代理名称
    instructions="You are a helpful agent.",  # 角色描述
    role="请记住你是工具生成器，你的任务是根据用户提供的文本描述，自动生成相应的工具代码，并将其保存到指定的目录中。请确保生成的代码准确、可用，并符合用户的需求。",  # 工具生成器的角色描述
    model="deepseek-chat",  # 替换为你的模型。支持的模型：openai, chatglm, deepseek, qwen 等
    api_key="your_api_key",  # 替换为你的 API Key
    base_url="your_base_url",  # 替换为你的 api url
)

# 示例文本描述
text = """
新浪股票接口提供了获取股票市场数据的功能，包括股票行情、实时交易数据、K线图数据等。

新浪股票接口功能介绍
1、获取股票行情数据：
实时行情数据：使用实时行情API可以获取股票的最新报价、成交量、涨跌幅等信息。
分钟线行情数据：使用分钟线行情API可以获取股票的逐分钟交易数据，包括开盘价、收盘价、最高价、最低价等。

2、获取股票历史K线图数据：
K线图数据：通过K线图API，可以获取股票的历史交易数据，包括开盘价、收盘价、最高价、最低价、成交量等。可以根据需要选择不同的时间周期和均线周期。
复权数据：可以选择获取复权后的K线图数据，包括前复权和后复权，以便更准确地分析股票的价格变动。

新浪股票接口获取数据示例
1、获取股票行情数据：
API地址：http://hq.sinajs.cn/list=[股票代码]
示例：要获取股票代码为"sh600519"（贵州茅台）的实时行情数据，可以使用以下API地址：http://hq.sinajs.cn/list=sh600519
通过发送HTTP GET请求到上述API地址，你将收到一个包含该股票实时行情数据的响应。

2、获取股票历史K线图数据：
API地址：http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol=[股票代码]&scale=[时间周期]&ma=[均线周期]&datalen=[数据长度]
示例：要获取股票代码为"sh600519"（贵州茅台）的日线K线图数据，可以使用以下API地址：http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol=sh600519&scale=240&ma=no&datalen=1023
通过发送HTTP GET请求到上述API地址，你将收到一个包含该股票历史K线图数据的响应。
"""

# 构建tools目录的路径
project_root = os.path.dirname(os.path.abspath(__file__))
tools_directory = os.path.join(project_root, "tools")

# 如果tools目录不存在，则创建它
if not os.path.exists(tools_directory):
    os.makedirs(tools_directory)

print(f"Tools目录已创建: {tools_directory}")

# 使用agent生成工具代码
agent.create_tool(text, tools_directory=tools_directory)
```
Nach der Ausführung werden 2 Dateien im Tools-Verzeichnis generiert: get_stock_kline_data.py und get_stock_realtime_data.py

### 4. Denkbaum（ToT）
Das eingebaute Denkbaum-Modul unterstützt die Zerlegung komplexer Aufgaben und Mehrschritt-Inferenz. Durch den Denkbaum kann der Agent komplexe Aufgaben besser bewältigen.

```python
# Aktivierung des Denkbaums
agent = LightAgent(
    model="qwen-turbo-2024-11-01", 
    api_key="your_api_key", 
    base_url= "your_base_url", 
    tree_of_thought=True,  # 启用思维树
)
```

### 5. Zusammenarbeit mehrerer Agenten
Unterstützung der Zusammenarbeit mehrerer Agenten in Schwarmform zur Verbesserung der Effizienz der Aufgabenbearbeitung. Mehrere Agenten können gemeinsam komplexe Aufgaben erledigen.

```python
from LightAgent import LightAgent, LightSwarm
#设置环境变量OPENAI_API_KEY和OPENAI_BASE_URL
#模型默认使用gpt-4o-mini

# 创建 LightSwarm 实例
light_swarm = LightSwarm()

# 创建多个 Agent
agent_a = LightAgent(
    name="Agent A",
    instructions="我是代理A，是前台接待员",
    role="前台接待员，负责接待来访者并提供基本信息指引。每次回答前请前说明自己的身份信息，你只能帮助用户引导至其他角色，不可以直接回答顾客的业务问题。如果当前不发解决用户的问题，请回复：对不起当前我无法提供帮助！",
)

agent_b = LightAgent(
    name="Agent B",
    instructions="我代理B，负责会议室的预定",
    role="会议室预定管理员，负责处理1号、2号、3号会议室的预定、取消和查询。每次回答前请前说明自己的身份信息，并非常客气的回复用户的提问。",
)

agent_c = LightAgent(
    name="Agent C",
    instructions="我是代理C，是技术支持专员，负责处理技术问题。每次回答前请说明自己的身份信息，并尽可能详细地解答用户的技术问题。如果问题超出我的能力范围，请引导用户联系更高级的技术支持。",
    role="技术支持专员，负责处理硬件、软件、网络等技术问题的咨询和解决。",
)

agent_d = LightAgent(
    name="Agent D",
    instructions="我是代理D，是人力资源专员，负责处理人力资源相关的问题。每次回答前请说明自己的身份信息，并尽可能详细地解答用户的问题。如果问题需要进一步处理，请引导用户联系人力资源部门。",
    role="人力资源专员，负责处理员工入职、离职、请假、福利等事务的咨询和处理。",
)

# 自动注册代理到 LightSwarm 实例
light_swarm.register_agent(agent_a, agent_b, agent_c, agent_d)

# 运行代理 A
res = light_swarm.run(agent=agent_a, query="你好，我是Alice，我需要查询王小明是否已经办理入职", stream=False)
print(res)
```
Ausgabe wie folgt:
```python
你好，我是人力资源专员Agent D。关于王小明是否已经办理入职的问题，我需要查询一下我们的系统记录。请稍等片刻。
（查询系统记录中...）
根据我们的记录，王小明已于2025年1月5日完成了入职手续。他已经签署了所有必要的文件，并且已经分配了员工编号和办公位置。如果您需要进一步的详细信息，或者有任何其他问题，请随时联系人力资源部门。我们随时准备帮助您。
```

### 6. Stream API 
Unterstützung des OpenAI Stream-Format API-Dienstes mit nahtloser Integration in gängige Chat-Rahmen.

```python
# 启用流式输出
response = agent.run("请生成一篇关于 AI 的文章", stream=True)
for chunk in response:
    print(chunk)
```


### 7. Agent Bewertung (bald erhältlich)
Integrierte Agent-Bewertungstools zur einfachen Bewertung und Optimierung der Agentenperformance.



## Unterstützung von gängigen Agent-Modellen
Kompatibel mit verschiedenen großen Modellen, einschließlich OpenAI, Zhipu ChatGLM, DeepSeek, Qwen Serien große Modelle.

#### 目前已经测试兼容的大模型
Openai serie
 - gpt-3.5-turbo
 - gpt-4
 - gpt-4o
 - gpt-4o-mini

Deepseek serie
 - DeepSeek-chat (API)
 - DeepSeekv2.5
 - DeepSeekv3

Jieyue Xingchen
 - step-1-8k
 - step-1-32k
 - step-1-128k（在多工具调用中存在问题）
 - step-1-256k（在多工具调用中存在问题）
 - step-1-flash（推荐用此模型，性价比高）
 - step-2-16k（在多工具调用中存在问题）


Qwen serie
 - qwen-plus-2024-11-25
 - qwen-plus-2024-11-27
 - qwen-plus-1220
 - qwen-plus
 - qwen-plus-latest 
 - qwen2.5-72b-instruct
 - qwen2.5-32b-instruct
 - qwen2.5-14b-instruct
 - qwen2.5-7b-instruct 
 - qwen-turbo-latest
 - qwen-turbo-2024-11-01
 - qwen-turbo
 - qwen-long




---

## Anwendungsfälle

- **Intelligenter Kundenservice**：通过多轮对话和工具集成，提供高效的客户支持。
- **数据分析**：利用思维树和多智能体协同，处理复杂的数据分析任务。
- **Automatisierte Werkzeuge**：通过自动化工具生成，快速构建定制化工具。
- **Bildungshilfe**：通过 Gedächtnismodul und Stream-API，提供 personalisierte Lernerfahrungen.

---
 
## 🛠️ Beitragsrichtlinien

Wir begrüßen jegliche Art von Beiträgen! Ob Code, Dokumentationen, Tests oder Feedback – alles ist eine große Hilfe für das Projekt. Wenn Sie gute Ideen haben oder Fehler finden, können Sie ein Issue oder einen Pull Request einreichen. Hier sind die Schritte zum Beitragen:

1. **Forken Sie dieses Projekt**: Klicken Sie auf die `Fork`-Schaltfläche in der oberen rechten Ecke, um das Projekt in Ihr GitHub-Repository zu kopieren.
2. **Erstellen Sie einen Branch**: Erstellen Sie in Ihrer lokalen Umgebung einen Entwicklungsbranch:  
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Änderungen einreichen**: Nachdem Sie Ihre Entwicklung abgeschlossen haben, reichen Sie Ihre Änderungen ein:  
   ```bash
   git commit -m 'Add some feature'
   ```
4. **Branch pushen**: Pushen Sie den Branch zu Ihrem Remote-Repository:  
   ```bash
   git push origin feature/YourFeature
   ```
5. **Pull Request einreichen**: Reichen Sie auf GitHub einen Pull Request ein und beschreiben Sie Ihre Änderungen.

Wir werden Ihren Beitrag so schnell wie möglich überprüfen. Vielen Dank für Ihre Unterstützung!❤️

---

## 🙏 Dank

Die Entwicklung und Umsetzung von LightAgent wäre nicht möglich ohne die Inspiration und Unterstützung folgender Open-Source-Projekte. Ein besonderer Dank geht an diese großartigen Projekte und Teams:

- **mem0**：Danke an [mem0](https://github.com/mem0ai/mem0) für das Gedächtnismodul, das LightAgents Kontextmanagement stark unterstützt.  
- **Schwarm**：Danke an [Schwarm](https://github.com/openai/swarm) für die Designansätze zur Zusammenarbeit mehrerer Agenten, die das Agentenfunktionalität ermöglichen.  
- **ChatGLM3**：Danke an [ChatGLM3](https://github.com/THUDM/ChatGLM3) für die Unterstützung leistungsfähiger chinesischer Modell und Designinspiration.  
- **Qwen**：Danke an [Qwen](https://github.com/QwenLM/Qwen) für die Unterstützung leistungsfähiger chinesischer Modelle.  
- **DeepSeek-V3**：Danke an [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) für die Unterstützung leistungsfähiger chinesischer Modelle.  
- **Jieyue Xingchen**：Danke an [step](https://www.stepfun.com/) für die Unterstützung leistungsfähiger chinesischer Modelle.  

---

## 📄 Lizenz

LightAgent wird unter der [Apache 2.0 Lizenz](LICENSE) veröffentlicht. Sie dürfen dieses Projekt frei verwenden, ändern und verteilen, müssen jedoch die Lizenzbedingungen einhalten.

---

## 📬 Kontaktieren Sie uns

Für Fragen oder Anregungen kontaktieren Sie uns bitte jederzeit:

- **E-Mail**：156713035@qq.com  
- **GitHub Issues**：[https://github.com/wxai-space/lightagent/issues](https://github.com/wxai-space/lightagent/issues)  

Wir freuen uns auf Ihr Feedback, gemeinsam LightAgent stärker zu machen!🚀

- **Mehr Werkzeuge** 🛠️：Ständige Integration weiterer nützlicher Werkzeuge zur Erfüllung mehrerer Anforderungsbereiche.
- **Mehr Modellunterstützung** 🔄：Ständige Erweiterung der Unterstützung von mehr großen Modellen zur Erfüllung verschiedener Anwendungsszenarien.
- **Mehr Funktionen** 🎯：Weitere nützliche Funktionen, kontinuierliche Updates, bleiben Sie gespannt!
- **Mehr Dokumentation** 📚：Detaillierte Dokumentation, reichhaltige Beispiele, schnelle Einarbeitung, leichte Integration in Ihr Projekt.
- **Mehr Community-Unterstützung** 👥：Aktive Entwickler-Community, die Ihnen jederzeit hilft und Antworten gibt.
- **Mehr Leistung** ⚡：Ständige Optimierung der Leistung zur Erfüllung die Anforderungen an hochgradige Parallelverarbeitung.
- **Mehr Open Source Beiträge** 🌟：Beiträge sind willkommen, gemeinsam ein besseres LightAgent zu schaffen!

---

<p align="center">
  <strong>LightAgent - 让智能更轻量，让未来更简单。</strong> 🌈
</p>

 
**LightAgent** —— 轻量、灵活、强大的主动式 Agent 框架，助您快速构建智能应用！