from langchain_core.tools import tool
from langchain_experimental.utilities import PythonREPL
from multi_agent_bot.tools.base import BaseTool
from multi_agent_bot.utils.code_executor import run_code_in_docker


class PythonReplTool(BaseTool):
    def __init__(self):
        self.repl = PythonREPL()

    @tool()
    def execute(self, code: str):
        """Executes the given Python code and returns the result."""
        try:
            result = run_code_in_docker(code)
            result_str = f"Successfully executed:\n```python\n{code}\n```\nStdout: {result}"
            return result_str + "\n\nIf you have completed all tasks, respond with FINAL ANSWER."    
            # result = self.repl.run(code)
        except BaseException as e:
            return f"Failed to execute. Error: {repr(e)}"

    def get_tool(self):
        return self.execute  # return the method reference