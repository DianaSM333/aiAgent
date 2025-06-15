import os
from google.genai import types
def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    target = os.path.abspath(os.path.join(working_directory, file_path))

    if not target.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        if not os.path.exists(target):
            os.makedirs(file_path)
    except Exception as e:
        print(f"Error: {e}")

    try:
        with open(target, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        print(f"Error: {e}")

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="write to the given file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content of the file to write",
            ),
        },
        required=["file_path", "content"],
    ),
)