from langchain_community.tools.tavily_search import TavilySearchResults
from multi_agent_bot.tools.base import BaseTool

class TavilySearchTool(BaseTool):
    def get_tool(self):
        """Returns a TavilySearchResults tool instance."""
        return TavilySearchResults(max_results=5)