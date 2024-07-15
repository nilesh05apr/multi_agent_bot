import re
import subprocess

def run_code_in_docker(code: str):
    """
    Run the provided Python code inside a Docker container for safety.

    Parameters:
    code (str): The Python code to execute.

    Returns:
    str: The output from executing the code.
    """
    try:
        code = re.escape(code)
        result = subprocess.run([
            'docker', 'run', '--rm', f"$PWD/code_execution:/code_execution", 'code_execution_image', code
        ], capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
    except subprocess.CalledProcessError as e:
        return f"Error executing code: {e.stderr}"