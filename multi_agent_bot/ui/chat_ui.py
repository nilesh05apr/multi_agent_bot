import gradio as gr
from multi_agent_bot.api.api import APIHandler
from multi_agent_bot.utils.logging import setup_logging
from langchain_core.messages import HumanMessage

class UI:
    def __init__(self):
        setup_logging()
        self.api_handler = APIHandler()

    def run(self):
        def process_input(prompt):
            research_agent = self.api_handler.get_research_agent()
            chart_agent = self.api_handler.get_chart_agent()

            research_result = research_agent.invoke({"messages": [HumanMessage(content=prompt)]})
            research_message = research_result.content

            chart_result = chart_agent.invoke({"messages": [HumanMessage(content=research_message)]})
            chart_message = chart_result.content
            
            return research_message, chart_message['data'] if 'data' in chart_message else chart_message
        
        demo = gr.Interface(
            fn=process_input,
            inputs="text",
            outputs=["text", "plot"],
            title="Research Assistant",
            description="This application takes a prompt and generates research code and plots using a multi-agent bot."
        )

        demo.launch()