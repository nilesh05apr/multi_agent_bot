from multi_agent_bot.prompts.base import BasePrompt
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class ChartPrompt(BasePrompt):
    def create_prompt(self):
        return ChatPromptTemplate.from_messages([
            (
                "system",
                "You are a helpful AI assistant, collaborating with other assistants."
                " Use the provided tools to progress towards answering the question."
                " If you are unable to fully answer, that's OK, another assistant with different tools "
                " will help where you left off. Execute what you can to make progress."
                " If you or any of the other assistants have the final answer or deliverable,"
                " prefix your response with FINAL ANSWER so the team knows to stop."
                " You have access to the following tools: {tool_names}.\n{system_message}",
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]).partial(system_message=self.system_message).partial(tool_names=", ".join([tool.name for tool in self.tools]))