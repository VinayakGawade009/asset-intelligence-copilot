import os
import sys
import time
import traceback
from pathlib import Path
from dotenv import load_dotenv

# Set unbuffered stdout so prints appear immediately
sys.stdout.reconfigure(line_buffering=True)

# Load .env file from project root
project_root = Path(__file__).resolve().parent.parent
dotenv_path = project_root / ".env"
load_dotenv(dotenv_path=dotenv_path)

api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
fast_model = os.getenv("GEMMA_MODEL_FAST")
strong_model = os.getenv("GEMMA_MODEL_STRONG")

print(f"Loaded configuration from: {dotenv_path}", flush=True)
print(f"GEMMA_MODEL_FAST: {fast_model}", flush=True)
print(f"GEMMA_MODEL_STRONG: {strong_model}", flush=True)
print("=" * 60, flush=True)

from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)

# 1. Plain call with GEMMA_MODEL_FAST
def test_plain_call_fast():
    print("\n--- Test 1: Plain call (GEMMA_MODEL_FAST) ---", flush=True)
    start_time = time.time()
    try:
        response = client.models.generate_content(
            model=fast_model,
            contents="Say hello.",
        )
        elapsed = time.time() - start_time
        reply_text = response.text.strip() if response.text else ""
        print(f"Reply: {reply_text}", flush=True)
        print(f"Status: PASS | Time: {elapsed:.2f}s", flush=True)
        return True
    except Exception as e:
        elapsed = time.time() - start_time
        print(f"Status: FAIL | Time: {elapsed:.2f}s", flush=True)
        print(f"Error Message:\n{traceback.format_exc()}", flush=True)
        return False

# 2. Plain call with GEMMA_MODEL_STRONG
def test_plain_call_strong():
    print("\n--- Test 2: Plain call (GEMMA_MODEL_STRONG) ---", flush=True)
    start_time = time.time()
    try:
        response = client.models.generate_content(
            model=strong_model,
            contents="Say hello.",
        )
        elapsed = time.time() - start_time
        reply_text = response.text.strip() if response.text else ""
        print(f"Reply: {reply_text}", flush=True)
        print(f"Status: PASS | Time: {elapsed:.2f}s", flush=True)
        return True
    except Exception as e:
        elapsed = time.time() - start_time
        print(f"Status: FAIL | Time: {elapsed:.2f}s", flush=True)
        print(f"Error Message:\n{traceback.format_exc()}", flush=True)
        return False

# 3. Tool calling function definition
def get_threshold(well_type: str) -> str:
    """Get the operating threshold for a given well type.

    Args:
        well_type: The type of well (e.g. T200).
    """
    return f"Threshold for {well_type} is 150 psi"

def test_tool_calling_fast():
    print("\n--- Test 3: Tool calling (GEMMA_MODEL_FAST) ---", flush=True)
    start_time = time.time()
    try:
        response = client.models.generate_content(
            model=fast_model,
            contents="What is the threshold for T200 wells?",
            config=types.GenerateContentConfig(
                tools=[get_threshold],
                automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
            ),
        )
        elapsed = time.time() - start_time
        
        function_calls = response.function_calls
        if function_calls:
            for call in function_calls:
                print(f"Function Call Returned: name='{call.name}', arguments={call.args}", flush=True)
            print(f"Status: PASS | Time: {elapsed:.2f}s", flush=True)
            return True
        else:
            print(f"No function call found in model response: {response.text}", flush=True)
            print(f"Status: FAIL | Time: {elapsed:.2f}s", flush=True)
            return False
    except Exception as e:
        elapsed = time.time() - start_time
        print(f"Status: FAIL | Time: {elapsed:.2f}s", flush=True)
        print(f"Error Message:\n{traceback.format_exc()}", flush=True)
        return False

def main():
    res1 = test_plain_call_fast()
    res2 = test_plain_call_strong()
    res3 = test_tool_calling_fast()

    print("\n" + "=" * 60, flush=True)
    print("Smoke Test Summary:", flush=True)
    print(f"  Test 1 (Plain call FAST)  : {'PASS' if res1 else 'FAIL'}", flush=True)
    print(f"  Test 2 (Plain call STRONG): {'PASS' if res2 else 'FAIL'}", flush=True)
    print(f"  Test 3 (Tool calling FAST): {'PASS' if res3 else 'FAIL'}", flush=True)
    print("=" * 60, flush=True)

if __name__ == "__main__":
    main()
