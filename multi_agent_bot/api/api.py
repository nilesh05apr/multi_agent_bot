import os
from langchain_openai import ChatOpenAI
from multi_agent_bot.agents.research_agent import ResearchAgent
from multi_agent_bot.agents.chart_agent import ChartAgent
from multi_agent_bot.tools.python_repl import PythonReplTool
from multi_agent_bot.tools.tavily_search import TavilySearchTool
from multi_agent_bot.utils.config import load_config
from multi_agent_bot.utils.logging import setup_logging

class APIHandler:
    def __init__(self):
        config = load_config()
        os.environ["OPENAI_API_KEY"] = config["API_KEYS"]["OPENAI"]
        os.environ["LANGCHAIN_API_KEY"] = config["API_KEYS"]["LANGCHAIN"]
        os.environ["TAVILY_API_KEY"] = config["API_KEYS"]["TAVILY"]
        
        self.llm = ChatOpenAI(model="gpt-4o")
        
        self.tools = [TavilySearchTool().get_tool(), PythonReplTool().get_tool()]
        
        self.research_agent = ResearchAgent(self.llm, self.tools).create_agent()
        self.chart_agent = ChartAgent(self.llm, self.tools).create_agent()

    def get_research_agent(self):
        return self.research_agent

    def get_chart_agent(self):
        return self.chart_agent

    def get_tools(self):
        return self.tools