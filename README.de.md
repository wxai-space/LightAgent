
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
  <h1>LightAgent🚀（Nächste Generation des Agentic AI-Frameworks）</h1>
</div>

**LightAgent** ist ein extrem leichtgewichtiges, speicherfähiges (`mem0`), werkzeugbasiertes (`Tools`), denkbaumgestütztes (`ToT`) aktives Agenten-Framework, das vollständig Open Source ist. Es unterstützt eine einfachere Multi-Agenten-Kollaboration als OpenAI Swarm, ermöglicht es, in einem Schritt Agenten mit Selbstlernfähigkeiten zu erstellen, und unterstützt die Anbindung an das MCP-Protokoll über stdio und sse. Das zugrunde liegende Modell unterstützt OpenAI, Zhiyu ChatGLM, DeepSeek, Jieyue Xingchen, Qwen Tongyi Qianwen große Modelle usw. Gleichzeitig unterstützt LightAgent die Ausgabe von OpenAI Stream-Format-API-Diensten und ermöglicht eine nahtlose Integration in alle gängigen Chat-Frameworks. 🌟

---

## ✨ Eigenschaften

- **Leicht und effizient** 🚀: Minimalistisches Design, schnelle Bereitstellung, geeignet für verschiedene Anwendungsfälle. (Kein LangChain, Kein LlamaIndex) 100% Python-Implementierung, keine zusätzlichen Abhängigkeiten, der Kerncode umfasst nur 1000 Zeilen und ist vollständig Open Source. 
- **Speicherunterstützung** 🧠: Unterstützt benutzerdefinierte Langzeitgedächtnisse für jeden Benutzer, native Unterstützung des `mem0`-Speichermoduls, das die personalisierte Erinnerung des Benutzers während des Gesprächs automatisch verwaltet und den Agenten intelligenter macht.
- **Selbstlernen** 📚️: Jeder Agent hat die Fähigkeit zum selbstständigen Lernen, und berechtigte Administratoren können jeden Agenten verwalten.
- **Werkzeugintegration** 🛠️: Unterstützt benutzerdefinierte Werkzeuge (`Tools`), automatisierte Werkzeuggenerierung, flexible Erweiterung zur Erfüllung vielfältiger Anforderungen.  
- **Komplexe Ziele** 🌳: Integriertes, reflektierendes Denkbaum-Modul (ToT), das komplexe Aufgabenzerlegungen und mehrstufiges Denken unterstützt, um die Aufgabenbearbeitungsfähigkeit zu verbessern.  
- **Multi-Agenten-Kooperation** 🤖: Einfachere Implementierung der Multi-Agenten-Kooperation als Swarm, integrierte LightSwarm-Funktion zur Absichtserkennung und Aufgabenübertragung, die es ermöglicht, Benutzereingaben intelligenter zu verarbeiten und Aufgaben bei Bedarf an andere Agenten zu übertragen. 
- **Unabhängige Ausführung** 🤖: Selbstständige Durchführung von Aufgaben ohne menschliches Eingreifen.  
- **Unterstützung mehrerer Modelle** 🔄: Kompatibel mit OpenAI, Zhiyu ChatGLM, Baichuan große Modelle, StepFun, DeepSeek, Qwen-Serie große Modelle.  
- **Stream-API** 🌊: Unterstützt die Ausgabe von OpenAI Stream-Format-API-Diensten, nahtlose Integration in gängige Chat-Frameworks zur Verbesserung der Benutzererfahrung.  
- **Werkzeuggenerator** 🚀: Geben Sie einfach Ihre API-Dokumentation an den [Werkzeuggenerator] weiter, und er wird automatisch Ihre maßgeschneiderten Werkzeuge erstellen, sodass Sie in nur einer Stunde Hunderte von personalisierten benutzerdefinierten Werkzeugen schnell erstellen können, um die Effizienz zu steigern und Ihr kreatives Potenzial freizusetzen.
- **Selbstlernender Agent** 🧠️: Jeder Agent hat die Fähigkeit, seine eigene Szenarienerinnerung zu entwickeln und aus den Gesprächen mit Benutzern zu lernen.
- **Adaptive Werkzeugmechanismen** 🛠️: Unterstützung für die Hinzufügung unbegrenzter Werkzeuge, Auswahl von Kandidatenwerkzeugen aus Tausenden von Werkzeugen durch das große Modell, Filtern irrelevanter Werkzeuge und anschließende Einreichung des Kontexts an das große Modell, was den Token-Verbrauch erheblich senken kann.


## 🚧 Bald verfügbar

- **Agent-Kooperation Kommunikation** 🛠️: Agenten können Informationen austauschen und Nachrichten übermitteln, um komplexe Informationskommunikation und Aufgabenkoordination zu realisieren.
- **Agentenbewertung** 📊: Integriertes Agentenbewertungstool zur einfachen Bewertung und Optimierung Ihrer erstellten Agenten, um sie an Geschäftsszenarien anzupassen und das Intelligenzniveau kontinuierlich zu verbessern.  


## Integrierte „Denkfluss“-Methode
Durch systematische, strukturierte und flexible Denkprozesse kann die Methode effektiv auf Herausforderungen in komplexen Szenarien reagieren.
Hier sind die spezifischen Umsetzungsschritte:
```text
Problemdefinition: Klärung des Kernproblems und der Ziele.

Informationssammlung: Systematische Sammlung relevanter Informationen und Daten.

Problemanalyse: Zerlegung komplexer Probleme in mehrere Teilprobleme oder Module.

Multidimensionale Analyse: Analyse jedes Teilproblems aus verschiedenen Perspektiven und Ebenen.

Beziehungen herstellen: Identifizierung der Zusammenhänge und Abhängigkeiten zwischen den Teilproblemen.

Lösungen generieren: Vorschlag möglicher Lösungen für jedes Teilproblem.

Bewertung und Auswahl: Bewertung der Machbarkeit und Auswirkungen der Lösungen, Auswahl der optimalen Lösung.

Implementierung und Feedback: Umsetzung der ausgewählten Lösung und Anpassung basierend auf dem Feedback.
```

---
## 🌟 Warum LightAgent wählen?

- **Open Source und kostenlos** 💖: Vollständig Open Source, gemeinschaftsgetrieben, kontinuierliche Updates, Beiträge sind willkommen!  
- **Einfach zu bedienen** 🎯: Ausführliche Dokumentation, reichhaltige Beispiele, schnelle Einarbeitung, einfache Integration in Ihr Projekt.  
- **Gemeinschaftsunterstützung** 👥: Aktive Entwicklergemeinschaft, die Ihnen jederzeit Hilfe und Antworten bietet.  
- **Hohe Leistung** ⚡: Optimiertes Design, effiziente Ausführung, erfüllt die Anforderungen an hochgradige Parallelität.  

---

## 🛠️ Schnellstart

### Installation der neuesten Version von LightAgent

```bash
pip install lightagent
```

(Optional) Installieren Sie das Mem0-Paket über pip:

```bash
pip install mem0ai
```

Oder Sie können Mem0 mit einem Klick auf einer Hosting-Plattform verwenden, [klicken Sie hier](https://www.mem0.ai/).


### Hello World Beispielcode

```python
from LightAgent import LightAgent

# Initialisieren des Agenten
agent = LightAgent(model="gpt-4o-mini", api_key="your_api_key", base_url= "your_base_url")

# Ausführen des Agenten
response = agent.run("Hallo, wer bist du?")
print(response)
```

### Festlegen des Selbstbewusstseins des Modells durch System-Prompt

```python
from LightAgent import LightAgent

# Initialisieren des Agenten
agent = LightAgent(
     role="Bitte erinnere dich, dass du LightAgent bist, ein nützlicher Assistent, der den Benutzern hilft, mehrere Werkzeuge zu verwenden.",  # Systemrollenbeschreibung
     model="deepseek-chat",  # Unterstützte Modelle: openai, chatglm, deepseek, qwen usw.
     api_key="your_api_key",  # Ersetzen Sie durch Ihren API-Schlüssel des großen Modells
     base_url="your_base_url",  # Ersetzen Sie durch die API-URL Ihres großen Modells
 )
# Ausführen des Agenten
response = agent.run("Darf ich fragen, wer du bist?")
print(response)
```

### Beispielcode zur Verwendung von Werkzeugen

```python
from LightAgent import LightAgent


# Definieren des Werkzeugs
def get_weather(city_name: str) -> str:
    """
    Holen Sie sich das aktuelle Wetter für `city_name`
    """
    return f"Suchergebnis: {city_name} Wetter ist klar"
# Definieren Sie die Werkzeuginformationen innerhalb der Funktion
get_weather.tool_info = {
    "tool_name": "get_weather",
    "tool_description": "Holen Sie sich die aktuellen Wetterinformationen für die angegebene Stadt",
    "tool_params": [
        {"name": "city_name", "description": "Der Name der Stadt, die abgefragt werden soll", "type": "string", "required": True},
    ]
}

tools = [get_weather]

# Initialisieren des Agenten
agent = LightAgent(model="qwen-turbo-2024-11-01", api_key="your_api_key", base_url= "your_base_url", tools=tools)

# Ausführen des Agenten
response = agent.run("Bitte helfen Sie mir, das Wetter in Shanghai zu überprüfen")
print(response)
```
Unterstützt die benutzerdefinierte Erstellung einer unbegrenzten Anzahl von Werkzeugen.

Beispiele für mehrere Werkzeuge: tools = [search_news,get_weather,get_stock_realtime_data,get_stock_kline_data]

---

## Funktionale Details

### 1. Abnehmbares, vollautomatisches Gedächtnismodul (`mem0`)
LightAgent unterstützt die externe Erweiterung des `mem0`-Gedächtnismoduls, das automatisch Kontextgedächtnis und Historienverwaltung durchführt, ohne dass Entwickler manuell Gedächtnis hinzufügen oder abrufen müssen. Durch das Gedächtnismodul kann der Agent die Konsistenz des Kontexts über mehrere Dialoge hinweg aufrechterhalten.

```python
# Aktivieren des Gedächtnismoduls

# Oder verwenden Sie ein benutzerdefiniertes Gedächtnismodul, hier als Beispiel mem0 https://github.com/mem0ai/mem0/
from mem0 import Memory
from LightAgent import LightAgent
import os
from loguru import logger

class CustomMemory:
    def __init__(self):
        self.memories = []
        os.environ["OPENAI_API_KEY"] = "your_api_key"
        os.environ["OPENAI_API_BASE"] = "your_base_url"
        # Initialisieren von Mem0
        config = {
            "version": "v1.1"
        }
        # Wenn Sie qdrant als Vektorspeicher für das Gedächtnis verwenden möchten, ändern Sie die Konfiguration wie folgt
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
        """Speichern von Erinnerungen. Entwickler können die interne Implementierung der Speichermethode anpassen, das aktuelle Beispiel ist die Methode zum Hinzufügen von Erinnerungen von mem0."""
        result = self.m.add(data, user_id=user_id)
        return result

    def retrieve(self, query: str, user_id):
        """Abrufen relevanter Erinnerungen. Entwickler können die interne Implementierung der Abrufmethode anpassen, das aktuelle Beispiel ist die Methode zum Suchen von Erinnerungen von mem0."""
        result = self.m.search(query, user_id=user_id)
        return result

agent = LightAgent(
        role="Bitte erinnere dich, dass du LightAgent bist, ein nützlicher Assistent, der den Benutzern hilft, mehrere Werkzeuge zu verwenden.",  # Systemrollenbeschreibung
        model="deepseek-chat",  # Unterstützte Modelle: openai, chatglm, deepseek, qwen usw.
        api_key="your_api_key",  # Ersetzen Sie durch Ihren API-Schlüssel des großen Modells
        base_url="your_base_url",  # Ersetzen Sie durch die API-URL Ihres großen Modells
        memory=CustomMemory(),  # Aktivieren der Gedächtnisfunktion
        tree_of_thought=False,  # Aktivieren der Denkbaumfunktion
    )

# Gedächtnistests & Wenn Werkzeuge hinzugefügt werden müssen, können Sie die Werkzeuge selbst zum Agenten hinzufügen, um die Werkzeugaufrufe mit Gedächtnis zu realisieren

user_id = "user_01"
logger.info("\n=========== nächstes Gespräch ===========")
query = "Erzählen Sie mir von den Sehenswürdigkeiten in Sanya, viele meiner Freunde sind nach Sanya gereist, ich möchte auch dorthin."
print(agent.run(query, stream=False, user_id=user_id))
logger.info("\n=========== nächstes Gespräch ===========")
query = "Wo möchte ich reisen?"
print(agent.run(query, stream=False, user_id=user_id))
```

Die Ausgabe sieht wie folgt aus:
```python
=========== nächstes Gespräch ===========
2025-01-01 21:55:15.886 | INFO     | __main__:run_conversation:115 - 
Beginne, das Problem zu durchdenken: Erzählen Sie mir von den Sehenswürdigkeiten in Sanya, viele meiner Freunde sind nach Sanya gereist, ich möchte auch dorthin.
2025-01-01 21:55:28.676 | INFO     | __main__:run_conversation:118 - Endgültige Antwort: 
Sanya ist eine beliebte Touristenstadt in der Provinz Hainan, China, bekannt für ihre schönen Strände, tropisches Klima und reichhaltige Tourismusressourcen. Hier sind einige Sehenswürdigkeiten in Sanya, die einen Besuch wert sind:

1. **Yalong Bay**: Bekannt als "Hawaii des Ostens", hat einen langen Strand und klares Wasser, ideal zum Schwimmen, Tauchen und Sonnenbaden.

2. **Tianya Haijiao**: Dies ist eine berühmte Kulturlandschaft, die Touristen mit ihrer majestätischen Meereslandschaft und romantischen Legenden anzieht. Auf den großen Steinen sind die Worte "Tianya" und "Haijiao" eingraviert, die ewige Liebe symbolisieren.

3. **Nanshan Kultur Tourismusgebiet**: Hier gibt es eine 108 Meter hohe Nanshan Meeres-Guan Yin-Statue, die höchste Meeres-Guan Yin-Statue der Welt. Touristen können hier die buddhistische Kultur erleben und Tempel und Gärten besuchen.

4. **Wuzhizhou Island**: Diese kleine Insel ist bekannt für ihre unberührte Natur und reichhaltigen Wasseraktivitäten. Touristen können hier tauchen, schnorcheln und angeln.

5. **Dadonghai**: Dies ist ein Strand in der Innenstadt von Sanya, der aufgrund seiner bequemen Verkehrsanbindung und des lebhaften Nachtlebens bei Touristen beliebt ist.

6. **Sanya Bay**: Dies ist ein 22 Kilometer langer Strand, der ein guter Ort ist, um den Sonnenuntergang zu beobachten. Der Strand hier ist relativ ruhig und eignet sich für Touristen, die Ruhe mögen.

7. **Yanuoda Regenwald Kultur Tourismusgebiet**: Dies ist ein tropischer Regenwaldpark, in dem Touristen die natürliche Schönheit des tropischen Regenwaldes erleben und an verschiedenen Abenteueraktivitäten teilnehmen können.

8. **Luhuitou Park**: Dies ist ein Park auf einem Hügel, von dem aus man die gesamte Innenstadt von Sanya und die Sanya Bay überblicken kann. Hier gibt es auch eine schöne Legende über Rehe.

9. **Xidao**: Dies ist eine relativ unberührte kleine Insel, die Touristen mit ihren ruhigen Stränden und reichhaltigen Meereslebewesen anzieht.

10. **Sanya Qian Guqing**: Dies ist ein großes Kulturthemenpark, der die Geschichte und Kultur von Hainan durch Aufführungen und Ausstellungen präsentiert.

Neben den oben genannten Sehenswürdigkeiten gibt es in Sanya viele andere Orte, die es wert sind, erkundet zu werden, wie tropische Botanische Gärten und Fischmärkte. Die Küche in Sanya ist ebenfalls ein Highlight, insbesondere frische Meeresfrüchte und tropische Früchte. Bei der Reiseplanung wird empfohlen, die Wettervorhersage und die Öffnungszeiten der Sehenswürdigkeiten im Voraus zu überprüfen, um ein angenehmes Reiseerlebnis zu gewährleisten.
2025-01-01 21:55:28.676 | INFO     | __main__:<module>:191 - 
=========== nächstes Gespräch ===========
2025-01-01 21:55:28.676 | INFO     | __main__:run_conversation:115 - 
Beginne, das Problem zu durchdenken: Wo möchte ich reisen?
Relevante Erinnerungen gefunden:
Benutzer möchte nach Sanya reisen
Freunde des Benutzers sind nach Sanya gereist。
2025-01-01 21:55:38.797 | INFO     | __main__:run_conversation:118 - Endgültige Antwort: 
Basierend auf den zuvor erwähnten Informationen möchte der Benutzer nach Sanya reisen, und seine Freunde haben bereits Sanya besucht. Daher könnte Sanya ein geeignetes Reiseziel für den Benutzer sein. Hier sind einige Reiseinformationen über Sanya zur Referenz für den Benutzer:

### Reiseempfehlungen für Sanya:
1. **Yalong Bay**: Bekannt als "Hawaii des Ostens", hat schöne Strände und klares Wasser, ideal zum Schwimmen und Sonnenbaden.
2. **Tianya Haijiao**: Das Wahrzeichen von Sanya, zieht Touristen mit seinen einzigartigen Felsen und romantischen Legenden an.
3. **Nanshan Kultur Tourismusgebiet**: Hier gibt es den berühmten Nanshan-Tempel und die 108 Meter hohe Meeres-Guan Yin-Statue, die wichtige buddhistische Kulturstätten sind.
4. **Wuzhizhou Island**: Ideal zum Tauchen und für Wassersport, die Insel hat reichhaltige Meereslebewesen und Korallenriffe.
5. **Dadonghai**: Ein Strand in der Innenstadt von Sanya, der für Familien und Paare geeignet ist.

### Weitere Empfehlungen:
Wenn der Benutzer bereits über Sanya informiert ist oder andere Reiseziele erkunden möchte, hier sind einige andere beliebte Reiseziele:
1. **Guilin**: Bekannt für seine einzigartige Karstlandschaft und die Landschaft des Li-Flusses.
2. **Lijiang**: Die Altstadt und der Jade Dragon Snow Mountain sind die Hauptattraktionen, geeignet für Reisende, die an Geschichte und Natur interessiert sind.
3. **Zhangjiajie**: Berühmt für seine einzigartigen Säulen und Naturlandschaften, ist einer der Drehorte für den Film "Avatar".

Der Benutzer kann je nach seinen Interessen und Zeitplan ein passendes Reiseziel auswählen. Wenn der Benutzer detailliertere Informationen oder Hilfe bei der Reiseplanung benötigt, lassen Sie es uns bitte wissen!
```

### 2. Werkzeugintegration (unbegrenzte benutzerdefinierte Werkzeugunterstützung)
Nutzen Sie die Anpassung von Werkzeugen (`Tools`) und integrieren Sie Ihre maßgeschneiderten Werkzeuge einfach über die `tools`-Methode. Diese Werkzeuge können beliebige Python-Funktionen sein und unterstützen Typannotationen für Parameter, um Flexibilität und Genauigkeit zu gewährleisten. Darüber hinaus bieten wir einen intelligenten, KI-gesteuerten Werkzeuggenerator, der Ihnen hilft, Werkzeuge automatisiert zu erstellen und Ihre Kreativität freizusetzen.

```python

import requests
from LightAgent import LightAgent

# Definieren des Werkzeugs
def get_weather(
        city_name: str
) -> str:
    """
    Holen Sie sich Wetterinformationen für die Stadt
    :param city_name: Stadtname
    :return: Wetterinformationen
    """
    if not isinstance(city_name, str):
        raise TypeError("Der Stadtname muss ein String sein")

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
        ret = "Fehler beim Abrufen der Wetterdaten!\n" + traceback.format_exc()

    return str(ret)
# Definieren Sie die Werkzeuginformationen innerhalb der Funktion
get_weather.tool_info = {
    "tool_name": "get_weather",
    "tool_description": "Holen Sie sich die aktuellen Wetterinformationen für die angegebene Stadt",
    "tool_params": [
        {"name": "city_name", "description": "Der Name der Stadt, die abgefragt werden soll", "type": "string", "required": True},
    ]
}

def search_news(
        keyword: str,
        max_results: int = 5
) -> str:
    """
    Suchen Sie Nachrichten basierend auf Schlüsselwörtern
    :param keyword: Suchbegriff
    :param max_results: Maximale Anzahl der zurückgegebenen Ergebnisse, standardmäßig 5
    :return: Nachrichten Suchergebnisse
    """
    results = f"Durch die Suche nach {keyword} habe ich {max_results} relevante Informationen gefunden."
    return str(results)

# Definieren Sie die Werkzeuginformationen innerhalb der Funktion
search_news.tool_info = {
    "tool_name": "search_news",
    "tool_description": "Suchen Sie Nachrichten basierend auf Schlüsselwörtern",
    "tool_params": [
        {"name": "keyword", "description": "Suchbegriff", "type": "string", "required": True},
        {"name": "max_results", "description": "Maximale Anzahl der zurückgegebenen Ergebnisse", "type": "int", "required": False},
    ]
}

def get_user_info(
        user_id: str
) -> str:
    """
    Holen Sie sich Benutzerinformationen
    :param user_id: Benutzer-ID
    :return: Benutzerinformationen
    """
    if not isinstance(user_id, str):
        raise TypeError("Die Benutzer-ID muss ein String sein")

    try:
        # Angenommen, wir verwenden eine Benutzerinformations-API, hier mit einer Beispiel-URL
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
        user_info = "Fehler beim Abrufen der Benutzerdaten!\n" + traceback.format_exc()

    return str(user_info)

# Definieren Sie die Werkzeuginformationen innerhalb der Funktion
get_user_info.tool_info = {
    "tool_name": "get_user_info",
    "tool_description": "Holen Sie sich die Informationen des angegebenen Benutzers",
    "tool_params": [
        {"name": "user_id", "description": "Benutzer-ID", "type": "string", "required": True},
    ]
}

# Benutzerdefinierte Werkzeuge
tools = [get_weather, search_news, get_user_info]  # Enthält alle Werkzeuge

# Initialisieren des Agenten
# Ersetzen Sie durch Ihre Modellparameter model, api_key, base_url
agent = LightAgent(model="qwen-turbo-2024-11-01", api_key="your_api_key", base_url= "your_base_url", tools=tools)

query = "Wie ist das aktuelle Wetter in Sanya?"
response = agent.run(query, stream=False)  # Verwenden Sie den Agenten, um die Abfrage auszuführen
print(response)
```

### 3. Werkzeuggenerator
Der Werkzeuggenerator ist ein Modul zur automatischen Erstellung von Werkzeugcode. Er kann basierend auf der vom Benutzer bereitgestellten Textbeschreibung automatisch den entsprechenden Werkzeugcode generieren und in einem angegebenen Verzeichnis speichern. Diese Funktion ist besonders nützlich für Szenarien, in denen schnell API-Aufrufwerkzeuge, Datenverarbeitungswerkzeuge usw. erstellt werden müssen.

Verwendungsbeispiel

Hier ist ein Beispielcode zur Verwendung des Werkzeuggenerators:

```python
import json
import os
import sys
from LightAgent import LightAgent

# Initialisieren von LightAgent
agent = LightAgent(
    name="Agent A",  # Agentenname
    instructions="Du bist ein hilfreicher Agent.",  # Rollenbeschreibung
    role="Bitte erinnere dich, dass du der Werkzeuggenerator bist. Deine Aufgabe ist es, basierend auf der vom Benutzer bereitgestellten Textbeschreibung automatisch den entsprechenden Werkzeugcode zu generieren und in einem angegebenen Verzeichnis zu speichern. Bitte stelle sicher, dass der generierte Code genau, verwendbar und den Anforderungen des Benutzers entspricht.",  # Rollenbeschreibung des Werkzeuggenerators
    model="deepseek-chat",  # Ersetzen Sie durch Ihr Modell. Unterstützte Modelle: openai, chatglm, deepseek, qwen usw.
    api_key="your_api_key",  # Ersetzen Sie durch Ihren API-Schlüssel
    base_url="your_base_url",  # Ersetzen Sie durch Ihre API-URL
)

# Beispieltextbeschreibung
text = """
Die Sina Aktien-API bietet die Funktion, Marktdaten für Aktien abzurufen, einschließlich Aktienkurse, Echtzeit-Handelsdaten, K-Linien-Daten usw.

Funktionen der Sina Aktien-API
1. Abrufen von Aktienkursdaten:
Echtzeitkursdaten: Mit der Echtzeitkurs-API können Sie die neuesten Angebote, Handelsvolumen, Preisänderungen usw. für Aktien abrufen.
Minutenkursdaten: Mit der Minutenkurs-API können Sie die Handelsdaten für Aktien im Minutentakt abrufen, einschließlich Eröffnungspreis, Schlusskurs, Höchstpreis, Tiefstpreis usw.

2. Abrufen von historischen K-Linien-Daten für Aktien:
K-Linien-Daten: Über die K-Linien-API können Sie historische Handelsdaten für Aktien abrufen, einschließlich Eröffnungspreis, Schlusskurs, Höchstpreis, Tiefstpreis, Handelsvolumen usw. Sie können verschiedene Zeitperioden und gleitende Durchschnittsperioden auswählen.
Anpassungsdaten: Sie können die Anpassungsdaten für K-Linien abrufen, einschließlich Voranpassung und Nachanpassung, um die Preisbewegungen von Aktien genauer zu analysieren.

Beispiel zum Abrufen von Daten über die Sina Aktien-API
1. Abrufen von Aktienkursdaten:
API-Adresse: http://hq.sinajs.cn/list=[Aktiencode]
Beispiel: Um die Echtzeitkursdaten für die Aktie mit dem Code "sh600519" (Kweichow Moutai) abzurufen, können Sie die folgende API-Adresse verwenden: http://hq.sinajs.cn/list=sh600519
Durch das Senden einer HTTP GET-Anfrage an die oben genannte API-Adresse erhalten Sie eine Antwort, die die Echtzeitkursdaten dieser Aktie enthält.

2. Abrufen von historischen K-Linien-Daten für Aktien:
API-Adresse: http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol=[Aktiencode]&scale=[Zeitperiode]&ma=[Durchschnittsperiode]&datalen=[Datenlänge]
Beispiel: Um die täglichen K-Linien-Daten für die Aktie mit dem Code "sh600519" (Kweichow Moutai) abzurufen, können Sie die folgende API-Adresse verwenden: http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol=sh600519&scale=240&ma=no&datalen=1023
Durch das Senden einer HTTP GET-Anfrage an die oben genannte API-Adresse erhalten Sie eine Antwort, die die historischen K-Linien-Daten dieser Aktie enthält.
"""

# Erstellen des Pfads zum Werkzeugsverzeichnis
project_root = os.path.dirname(os.path.abspath(__file__))
tools_directory = os.path.join(project_root, "tools")

# Wenn das Werkzeugsverzeichnis nicht existiert, erstellen Sie es
if not os.path.exists(tools_directory):
    os.makedirs(tools_directory)

print(f"Werkzeugsverzeichnis erstellt: {tools_directory}")

# Verwenden Sie den Agenten, um Werkzeugcode zu generieren
agent.create_tool(text, tools_directory=tools_directory)
```
Nach der Ausführung werden im Werkzeugsverzeichnis zwei Dateien generiert: get_stock_kline_data.py und get_stock_realtime_data.py

### 4. Denkbaum (ToT)
Integriertes Denkbaum-Modul, das komplexe Aufgabenzerlegungen und mehrstufiges Denken unterstützt. Durch den Denkbaum kann der Agent komplexe Aufgaben besser bearbeiten.

```python
# Aktivieren Sie den Denkbaum
agent = LightAgent(
    model="qwen-turbo-2024-11-01", 
    api_key="your_api_key", 
    base_url= "your_base_url", 
    tree_of_thought=True,  # Aktivieren Sie den Denkbaum
    tot_model="deepseek-r1", 
    tot_api_key="sk-uXx0H0B***17778F1",  # Ersetzen Sie dies durch Ihren deepseek r1 API-Schlüssel
    tot_base_url="https://api.deepseek.com/v1",  # API-URL
    filter_tools=False,  # Deaktivieren Sie die adaptive Werkzeugmechanismus
)
```
Nachdem ToT aktiviert ist, wird standardmäßig der adaptive Werkzeugmechanismus aktiviert. Wenn Sie ihn deaktivieren möchten, fügen Sie beim Initialisieren von LightAgent den Parameter filter_tools=False hinzu.



### 5. Multi-Agenten-Kooperation
Unterstützt swarmähnliche Multi-Agenten-Kooperation zur Verbesserung der Effizienz bei der Aufgabenbearbeitung. Mehrere Agenten können gemeinsam komplexe Aufgaben erledigen.

```python
from LightAgent import LightAgent, LightSwarm
# Setzen Sie die Umgebungsvariablen OPENAI_API_KEY und OPENAI_BASE_URL
# Standardmäßig wird das Modell gpt-4o-mini verwendet

# Erstellen Sie eine LightSwarm-Instanz
light_swarm = LightSwarm()

# Erstellen Sie mehrere Agenten
agent_a = LightAgent(
    name="Agent A",
    instructions="Ich bin Agent A, der Empfangsmitarbeiter.",
    role="Empfangsmitarbeiter, verantwortlich für die Begrüßung von Besuchern und die Bereitstellung grundlegender Informationen. Bitte geben Sie bei jeder Antwort zuerst Ihre Identität an und helfen Sie den Benutzern, zu anderen Rollen zu navigieren, ohne direkt auf geschäftliche Fragen der Kunden zu antworten. Wenn ich das Problem des Benutzers nicht lösen kann, antworte bitte: Es tut mir leid, ich kann derzeit nicht helfen!",
)

agent_b = LightAgent(
    name="Agent B",
    instructions="Ich bin Agent B, verantwortlich für die Buchung von Besprechungsräumen.",
    role="Besprechungsraum-Administrator, verantwortlich für die Buchung, Stornierung und Abfrage der Besprechungsräume 1, 2 und 3. Bitte geben Sie bei jeder Antwort zuerst Ihre Identität an und antworten Sie höflich auf die Fragen der Benutzer.",
)

agent_c = LightAgent(
    name="Agent C",
    instructions="Ich bin Agent C, der technische Supportmitarbeiter, verantwortlich für technische Probleme. Bitte geben Sie bei jeder Antwort zuerst Ihre Identität an und beantworten Sie die technischen Fragen der Benutzer so detailliert wie möglich. Wenn das Problem über meine Fähigkeiten hinausgeht, leiten Sie den Benutzer an den höheren technischen Support weiter.",
    role="Technischer Supportmitarbeiter, verantwortlich für die Beratung und Lösung von technischen Problemen im Zusammenhang mit Hardware, Software und Netzwerken.",
)

agent_d = LightAgent(
    name="Agent D",
    instructions="Ich bin Agent D, der Personalmitarbeiter, verantwortlich für Personalangelegenheiten. Bitte geben Sie bei jeder Antwort zuerst Ihre Identität an und beantworten Sie die Fragen der Benutzer so detailliert wie möglich. Wenn das Problem weiter bearbeitet werden muss, leiten Sie den Benutzer an die Personalabteilung weiter.",
    role="Personalmitarbeiter, verantwortlich für die Beratung und Bearbeitung von Mitarbeiteranfragen zu Einstellungen, Kündigungen, Urlaub und Leistungen.",
)

# Automatische Registrierung der Agenten in der LightSwarm-Instanz
light_swarm.register_agent(agent_a, agent_b, agent_c, agent_d)

# Ausführen von Agent A
res = light_swarm.run(agent=agent_a, query="Hallo, ich bin Alice, ich möchte wissen, ob Wang Xiaoming eingestellt wurde.", stream=False)
print(res)
```
Die Ausgabe sieht wie folgt aus:
```python
Hallo, ich bin der Personalmitarbeiter Agent D. Bezüglich der Frage, ob Wang Xiaoming eingestellt wurde, muss ich unsere Systemaufzeichnungen überprüfen. Bitte einen Moment Geduld.
(Überprüfung der Systemaufzeichnungen...)
Laut unseren Aufzeichnungen hat Wang Xiaoming am 5. Januar 2025 seine Einstellung abgeschlossen. Er hat alle erforderlichen Dokumente unterzeichnet und wurde einer Mitarbeiter-ID und einem Bürostandort zugewiesen. Wenn Sie weitere Informationen benötigen oder andere Fragen haben, wenden Sie sich bitte jederzeit an die Personalabteilung. Wir sind jederzeit bereit, Ihnen zu helfen.
```

### 6. Stream-API 
Unterstützt die Ausgabe von OpenAI Stream-Format-API-Diensten, nahtlose Integration in gängige Chat-Frameworks.

```python
# Aktivieren der Streaming-Ausgabe
response = agent.run("Bitte generiere einen Artikel über KI", stream=True)
for chunk in response:
    print(chunk)
```


### 7. Agentenbewertung (Bald verfügbar)
Integriertes Agentenbewertungstool zur einfachen Bewertung und Optimierung der Agentenleistung.



## Unterstützung für gängige Agentenmodelle
Kompatibel mit verschiedenen großen Modellen, einschließlich OpenAI, Zhiyu ChatGLM, DeepSeek, Qwen-Serie große Modelle.

#### Derzeit getestete kompatible große Modelle
Openai-Serie
 - gpt-3.5-turbo
 - gpt-4
 - gpt-4o
 - gpt-4o-mini
 - gpt-4.1
 - gpt-4.1-mini
 - gpt-4.1-nano

Deepseek-Serie
 - DeepSeek-chat (API)
 - DeepSeekv2.5
 - DeepSeekv3

StepFun
 - step-1-8k
 - step-1-32k
 - step-1-128k (Probleme bei der Verwendung mehrerer Werkzeuge)
 - step-1-256k (Probleme bei der Verwendung mehrerer Werkzeuge)
 - step-1-flash (dieses Modell wird empfohlen, da es ein gutes Preis-Leistungs-Verhältnis bietet)
 - step-2-16k (Probleme bei der Verwendung mehrerer Werkzeuge)


Qwen-Serie
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
 - qwq-32b




---

## Anwendungsszenarien

- **Intelligenter Kundenservice**: Bereitstellung effizienter Kundenunterstützung durch mehrstufige Dialoge und Werkzeugintegration.
- **Datenanalyse**: Verarbeitung komplexer Datenanalyseaufgaben mithilfe von Denkbaum und Multi-Agenten-Kooperation.
- **Automatisierte Werkzeuge**: Schnelles Erstellen maßgeschneiderter Werkzeuge durch automatisierte Werkzeuggenerierung.
- **Bildungsunterstützung**: Bereitstellung personalisierter Lernerfahrungen durch Gedächtnismodule und Stream-APIs.

---
 
## 🛠️ Beitragshinweise

Wir begrüßen alle Arten von Beiträgen! Egal ob Code, Dokumentation, Tests oder Feedback, alles ist eine große Hilfe für das Projekt. Wenn Sie gute Ideen haben oder einen Fehler finden, reichen Sie bitte ein Issue oder einen Pull Request ein. Hier sind die Schritte zur Mitwirkung:

1. **Forken Sie dieses Projekt**: Klicken Sie auf die Schaltfläche `Fork` in der oberen rechten Ecke, um das Projekt in Ihr GitHub-Repository zu kopieren.
2. **Erstellen Sie einen Branch**: Erstellen Sie lokal Ihren Entwicklungsbranch:  
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Änderungen einreichen**: Nach Abschluss der Entwicklung Ihre Änderungen einreichen:  
   ```bash
   git commit -m 'Fügen Sie eine Funktion hinzu'
   ```
4. **Branch pushen**: Pushen Sie den Branch in Ihr Remote-Repository:  
   ```bash
   git push origin feature/YourFeature
   ```
5. **Pull Request einreichen**: Reichen Sie einen Pull Request auf GitHub ein und beschreiben Sie Ihre Änderungen.

Wir werden Ihren Beitrag so schnell wie möglich überprüfen. Vielen Dank für Ihre Unterstützung!❤️

---

## 🙏 Danksagung

Die Entwicklung und Implementierung von LightAgent wäre ohne die Inspiration und Unterstützung folgender Open-Source-Projekte nicht möglich gewesen. Ein besonderer Dank geht an diese hervorragenden Projekte und Teams:

- **mem0**: Vielen Dank an [mem0](https://github.com/mem0ai/mem0) für das bereitgestellte Gedächtnismodul, das LightAgent eine starke Unterstützung für das Kontextmanagement bietet.  
- **Swarm**: Vielen Dank an [Swarm](https://github.com/openai/swarm) für die Designideen zur Multi-Agenten-Kooperation, die die Grundlage für die Multi-Agenten-Funktionalität von LightAgent bilden.  
- **ChatGLM3**: Vielen Dank an [ChatGLM3](https://github.com/THUDM/ChatGLM3) für die Unterstützung leistungsstarker chinesischer großer Modelle und die Designinspiration.  
- **Qwen**: Vielen Dank an [Qwen](https://github.com/QwenLM/Qwen) für die Unterstützung leistungsstarker chinesischer großer Modelle.  
- **DeepSeek-V3**: Vielen Dank an [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) für die Unterstützung leistungsstarker chinesischer großer Modelle.  
- **StepFun**: Vielen Dank an [step](https://www.stepfun.com/) für die Unterstützung leistungsstarker chinesischer großer Modelle.  

---

## 📄 Lizenz

LightAgent verwendet die [Apache 2.0 Lizenz](LICENSE). Sie können dieses Projekt frei verwenden, ändern und verteilen, müssen jedoch die Lizenzbedingungen einhalten.

---

## 📬 Kontaktieren Sie uns

Bei Fragen oder Anregungen können Sie uns jederzeit kontaktieren:

- **E-Mail**: service@wanxingai.com  
- **GitHub Issues**：[https://github.com/wxai-space/lightagent/issues](https://github.com/wxai-space/lightagent/issues)  

Wir freuen uns auf Ihr Feedback, um LightAgent noch leistungsfähiger zu machen!🚀

- **Weitere Werkzeuge** 🛠️: Kontinuierliche Integration weiterer nützlicher Werkzeuge zur Erfüllung zusätzlicher Anwendungsanforderungen.
- **Weitere Modellunterstützung** 🔄: Kontinuierliche Erweiterung der Unterstützung für weitere große Modelle zur Erfüllung zusätzlicher Anwendungsszenarien.
- **Weitere Funktionen** 🎯: Weitere nützliche Funktionen, kontinuierliche Updates, bleiben Sie dran!
- **Weitere Dokumentation** 📚: Ausführliche Dokumentation, reichhaltige Beispiele, schnelle Einarbeitung, einfache Integration in Ihr Projekt.
- **Weitere Gemeinschaftsunterstützung** 👥: Aktive Entwicklergemeinschaft, die Ihnen jederzeit Hilfe und Antworten bietet.
- **Weitere Leistungsoptimierung** ⚡: Kontinuierliche Optimierung der Leistung zur Erfüllung der Anforderungen an hochgradige Parallelität.
- **Weitere Open-Source-Beiträge** 🌟: Beiträge zum Code sind willkommen, um LightAgent gemeinsam zu verbessern!

---

<p align="center">
  <strong>LightAgent - Machen Sie Intelligenz leichter, machen Sie die Zukunft einfacher.</strong> 🌈
</p>

 
**LightAgent** —— Ein leichtgewichtiges, flexibles und leistungsstarkes aktives Agent-Framework, das Ihnen hilft, intelligente Anwendungen schnell zu erstellen!