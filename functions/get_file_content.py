import os
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    target = os.path.abspath(os.path.join(working_directory, file_path))

    if not target.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target):
        f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(target, "r") as f:
            contents = f.read()
        if len(contents) > 10000:
            contents = contents[:10000]
            contents += f"[...File {file_path} truncated at 10000 characters]"
        return contents
    except Exception as e:
        return f"Error listing files: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="read the content of a file.",
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
