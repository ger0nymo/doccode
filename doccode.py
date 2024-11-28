#!/usr/bin/env python3

import openai
import os
import sys
import time
import threading

from openai import OpenAI

os.environ[
    "OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def read_file(file_path):
    print("📖 Unrolling the scroll to read your code...")
    time.sleep(1)
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    print("📝 Etching the newfound wisdom into your code...")
    time.sleep(1)
    with open(file_path, 'w') as file:
        file.write(content)

def generate_documentation(code, file_extension):
    print("✨ Summoning the AI wizards to document your code...")

    # Start loading animation in a separate thread
    stop_loading = [False]
    def loading_animation():
        animation = "|/-\\"
        idx = 0
        while not stop_loading[0]:
            print(f"\r🔄 Casting spell... {animation[idx % len(animation)]}", end='', flush=True)
            idx += 1
            time.sleep(0.1)
        print('\r', end='')

    loading_thread = threading.Thread(target=loading_animation)
    loading_thread.start()

    prompt = (
        f"Please add comprehensive docstrings and inline comments to the following code, "
        f"using the appropriate comment syntax for a '{file_extension}' file. "
        f"Do not include any extra formatting like code blocks (```), "
        f"and provide only the updated code with the added documentation. "
        f"Do not include any additional explanations or text.\n\n{code}"
    )

    messages = [
        {"role": "system",
         "content": f"You are a helpful assistant proficient in documenting code files with extension '{file_extension}'."},
        {"role": "user", "content": prompt}
    ]

    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        documented_code = response.choices[0].message.content
        print("\n🚀 The documentation spell was successful!")
        return documented_code
    except Exception as e:
        print(f"\n⚠️ An error occurred while casting the spell: {e}")
        return code  # Return the original code if there's an error
    finally:
        # Stop the loading animation
        stop_loading[0] = True
        loading_thread.join()

def main(file_path):
    code = read_file(file_path)
    file_extension = os.path.splitext(file_path)[1]
    documented_code = generate_documentation(code, file_extension)
    write_file(file_path, documented_code)
    print(f"🎉 Voila! Documentation has been magically added to {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: doccode <path_to_code_file>")
    else:
        main(sys.argv[1])
