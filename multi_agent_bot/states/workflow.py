from functools import partial
from typing import Sequence, TypedDict, Literal
from langchain_core.messages import BaseMessage, ToolMessage, AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from multi_agent_bot.agents.research_agent import ResearchAgent
from multi_agent_bot.agents.chart_agent import ChartAgent
from multi_agent_bot.tools.python_repl import PythonReplTool
from multi_agent_bot.tools.tavily_search import TavilySearchTool

class AgentState(TypedDict):
    messages: Sequence[BaseMessage]
    sender: str

def agent_node(state, agent, name):
    result = agent.invoke({"messages": state['messages']})
    if isinstance(result, ToolMessage):
        pass  # handle the ToolMessage if necessary
    else:
        result_message = AIMessage(content=result.content, sender=name)
    return {
        "messages": state["messages"] + [result_message],
        "sender": name,
    }

def create_workflow():
    llm = ChatOpenAI(model="gpt-4o")
    tools = [TavilySearchTool().get_tool(), PythonReplTool().get_tool()]

    research_agent = ResearchAgent(llm, tools).create_agent()
    research_node = partial(agent_node, agent=research_agent, name="Researcher")

    chart_agent = ChartAgent(llm, tools).create_agent()
    chart_node = partial(agent_node, agent=chart_agent, name="Chart Generator")

    workflow = StateGraph(AgentState)

    workflow.add_node("Researcher", research_node)
    workflow.add_node("Chart Generator", chart_node)
    workflow.add_node("call_tool", ToolNode(tools))

    def router(state) -> Literal["call_tool", "__end__", "continue"]:
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "call_tool"
        if "FINAL ANSWER" in last_message.content:
            return "__end__"
        return "continue"

    workflow.add_conditional_edges("Researcher", router, {"continue": "Chart Generator", "call_tool": "call_tool", "__end__": END})
    workflow.add_conditional_edges("Chart Generator", router, {"continue": "Researcher", "call_tool": "call_tool", "__end__": END})
    workflow.add_conditional_edges("call_tool", lambda x: x["sender"], {"Researcher": "Researcher", "Chart Generator": "Chart Generator"})
    workflow.add_edge(START, "Researcher")
    return workflow.compile()