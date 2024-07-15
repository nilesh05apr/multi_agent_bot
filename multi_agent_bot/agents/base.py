from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, llm, tools, system_message):
        self.llm = llm
        self.tools = tools
        self.system_message = system_message

    @abstractmethod
    def create_agent(self):
        pass