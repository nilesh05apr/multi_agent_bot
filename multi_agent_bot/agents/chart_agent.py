from multi_agent_bot.agents.base import BaseAgent
from multi_agent_bot.prompts.chart_prompt import ChartPrompt

class ChartAgent(BaseAgent):
    def __init__(self, llm, tools):
        system_message = "Any charts you display will be visible by the user."
        super().__init__(llm, tools, system_message)

    def create_agent(self):
        prompt = ChartPrompt(self.system_message, self.tools).create_prompt()
        return prompt | self.llm.bind_tools(self.tools)