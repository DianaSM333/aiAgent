import os
import sys
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # using user input for the ai
    if len(sys.argv) == 2:
        contents = sys.argv[1]
    else:
        raise Exception("ERROR: no prompt")
    client = genai.Client(api_key=api_key)
    result = client.models.generate_content(model="gemini-2.0-flash-001", contents=contents)
    print(result.text)
    print(f"Prompt tokens: {result.usage_metadata.prompt_token_count}")
    print(f"Response tokens: { result.usage_metadata.candidates_token_count}")

main()
