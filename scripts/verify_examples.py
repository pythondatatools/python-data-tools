#!/usr/bin/env python3
"""
Verify Examples Script

Iterates through all .py files in the chapters/ directory and runs them 
using 'uv run' to ensure they are reproducible and syntactically correct.
"""
import os
import subprocess
import sys
from pathlib import Path

# Determine project root relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
CHAPTERS_DIR = os.path.join(PROJECT_ROOT, "chapters")

def verify_script(filepath):
    """Run a script with 'uv run' and return success/failure."""
    print(f"VERIFYING: {filepath.relative_to(PROJECT_ROOT)} ...", end=" ", flush=True)
    
    try:
        # We use 'uv run --script' to ensure it uses the inline metadata
        result = subprocess.run(
            ["uv", "run", str(filepath)],
            capture_output=True,
            text=True,
            check=True
        )
        print("✅ PASS")
        return True
    except subprocess.CalledProcessError as e:
        print("❌ FAIL")
        print("-" * 40)
        print(f"STDOUT:\n{e.stdout}")
        print(f"STDERR:\n{e.stderr}")
        print("-" * 40)
        return False
    except FileNotFoundError:
        print("❌ FAIL (uv command not found)")
        return False

def main():
    scripts = list(Path(CHAPTERS_DIR).rglob("*.py"))
    
    if not scripts:
        print("No Python scripts found in chapters/ directory.")
        return

    print(f"Found {len(scripts)} scripts. Starting verification...\n")
    
    failures = 0
    for script in scripts:
        if not verify_script(script):
            failures += 1
            
    print("\n" + "=" * 40)
    if failures == 0:
        print(f"ALL {len(scripts)} SCRIPTS PASSED!")
        sys.exit(0)
    else:
        print(f"{failures} SCRIPTS FAILED verification.")
        sys.exit(1)

if __name__ == "__main__":
    main()
