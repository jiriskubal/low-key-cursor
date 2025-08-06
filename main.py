import os
from dotenv import load_dotenv
from google import genai
import sys
import argparse


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)






def main():
    parser = argparse.ArgumentParser(
                        prog="AI Coding Agent",
                        description="Help me coding, i hope :)",
                        epilog="Vzdy AI podekuj! ")
    parser.add_argument('user_prompt', type=str, help='Input question to process')
    parser.add_argument('--verbose', dest='verbose', action='store_const', const=True, default=False, help='Enable verbose output (default: True)')
    

    args = parser.parse_args()
    
    prompt = args.user_prompt
    verbose_mode = args.verbose

    if len(sys.argv) ==1:
        print("error message")
        return sys.exit(1)
    prompt = sys.argv[-1]
    

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=prompt
    )
    if verbose_mode:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print(response.text)


if __name__ == "__main__":
    main()
