"""
Sync Examples Script - API-Centric Structure

Extracts marked code blocks from chapters/ and generates examples.json
for the Svelte frontend.

New structure:
- chapters/load/*.py -> load_csv_pandas, load_csv_polars, etc.
- chapters/transform/*.py -> filter_pandas, join_polars, etc.
- chapters/output/*.py -> write_csv_pandas, etc.
"""
import os
import re
import json
import subprocess
from collections import defaultdict

# Determine project root relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
CHAPTERS_DIR = os.path.join(PROJECT_ROOT, "chapters")
OUTPUT_FILE = os.path.join(PROJECT_ROOT, "webapp/src/data/examples.json")

# Regex for markers:
# Python: # <key> ... # </key>
# SQL: -- <key> ... -- </key>
MARKER_REGEX = re.compile(r'^\s*(?:#|--)\s*<(\w+)>\s*$')
END_MARKER_REGEX = re.compile(r'^\s*(?:#|--)\s*</(\w+)>\s*$')


def get_language(filename):
    if filename.endswith(".sql"):
        return "sql"
    return "python"


def parse_file(filepath):
    """Extract all marked code blocks from a file."""
    results = {}
    current_key = None
    buffer = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for line in lines:
        # Check for start marker
        start_match = MARKER_REGEX.match(line)
        if start_match:
            current_key = start_match.group(1)
            buffer = []
            continue
            
        # Check for end marker
        end_match = END_MARKER_REGEX.match(line)
        if end_match:
            if current_key == end_match.group(1):
                code_block = "".join(buffer).strip()
                results[current_key] = code_block
                current_key = None
            continue
            
        if current_key:
            buffer.append(line)
            
    return results


def main():
    """
    New output structure:
    {
        "load_csv_pandas": { "code": "...", "language": "python" },
        "load_csv_polars": { "code": "...", "language": "python" },
        ...
    }
    """
    all_examples = {}
    
    # Walk through all directories in chapters/
    for root, dirs, files in os.walk(CHAPTERS_DIR):
        for file in files:
            if not (file.endswith(".py") or file.endswith(".sql")):
                continue
                
            language = get_language(file)
            filepath = os.path.join(root, file)
            
            snippets = parse_file(filepath)
            
            # For Python files, we also try to run them to capture output
            file_output = ""
            if language == "python":
                print(f"Executing {file.relative_to(PROJECT_ROOT) if hasattr(file, 'relative_to') else file} ...", end=" ", flush=True)
                try:
                    res = subprocess.run(
                        ["uv", "run", filepath],
                        capture_output=True,
                        text=True,
                        check=True,
                        timeout=30
                    )
                    file_output = res.stdout
                    print("✅")
                except subprocess.CalledProcessError as e:
                    print("❌ (Execution failed)")
                    file_output = f"Execution failed (Exit {e.returncode}):\n{e.stderr}"
                except Exception as e:
                    print("❌ (System error)")
                    file_output = f"System error: {str(e)}"

            for key, code in snippets.items():
                all_examples[key] = {
                    "code": code,
                    "language": language,
                    "output": file_output
                }

    # Ensure output dir exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_examples, f, indent=2)
    
    print(f"Generated {OUTPUT_FILE} with {len(all_examples)} examples.")


if __name__ == "__main__":
    main()
