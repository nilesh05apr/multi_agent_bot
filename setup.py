from setuptools import setup, find_packages

setup(
    name="multi_agent_bot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "langchain_openai",
        "langsmith",
        "pandas",
        "langchain_experimental",
        "matplotlib",
        "langgraph",
        "streamlit",
        "gradio",
        "pyyaml",
        "plotly",
    ],
)