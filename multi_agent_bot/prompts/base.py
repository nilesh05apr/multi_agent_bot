from abc import ABC, abstractmethod
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class BasePrompt(ABC):
    def __init__(self, system_message, tools):
        self.system_message = system_message
        self.tools = tools

    @abstractmethod
    def create_prompt(self):
        pass