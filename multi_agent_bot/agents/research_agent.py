from multi_agent_bot.agents.base import BaseAgent
from multi_agent_bot.prompts.research_prompt import ResearchPrompt

class ResearchAgent(BaseAgent):
    def __init__(self, llm, tools):
        system_message = "You should provide accurate data for the chart_generator to use."
        super().__init__(llm, tools, system_message)
    
    def create_agent(self):
        prompt = ResearchPrompt(self.system_message, self.tools).create_prompt()
        return prompt | self.llm.bind_tools(self.tools)