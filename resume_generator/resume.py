import json
import os
from formatter import format_resume

def load_resume(file_path="resume.json"):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("❌ resume.json not found.")
        return None

def save_output(content, filename):
    os.makedirs("output", exist_ok=True)
    with open(f"output/{filename}", "w", encoding="utf-8") as file:
        file.write(content)
    print(f"✅ Resume saved to output/{filename}")

def main():
    data = load_resume()
    if data:
        formatted = format_resume(data)
        print("\n==== YOUR RESUME ====\n")
        print(formatted)

        # Save to txt and markdown
        save_output(formatted, "resume.txt")
        save_output(formatted, "resume.md")

if __name__ == "__main__":
    main()
