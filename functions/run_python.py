import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    target = os.path.abspath(os.path.join(working_directory, file_path))

    #checks if the filepath is in the working directory
    if not target.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    try:
        if not os.path.exists(target):
            return f'Error: File "{file_path}" not found.'
    except Exception as e:
        return f"Error: {e}"

    if not target.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(['python3', file_path], capture_output=True, text=True, timeout=30, cwd=abs_working_directory)
        out = "STDOUT:" + result.stdout + "\n" + "STDERR:" + result.stderr + "\n"
        if not result.stdout.strip() and not result.stderr.strip():
            return "No output produced."
        if result.returncode != 0:
            out += "Process exited with code " + str(result.returncode)
        return out
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a file in python",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the path to the file to get the content of",
            ),
        },
        required=["file_path"]
    ),
)
