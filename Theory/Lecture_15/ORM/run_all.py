"""
Master Test Runner for Lecture 15: Data Modeling
Runs all scripts cleanly with simple, human-readable output.
"""

import subprocess
import sys
import os

SCRIPTS = [
    ("Python", "Database.py", "1. SQLAlchemy Student Management System (Database.py)"),
    ("Python", "ecommerce_models.py", "2. E-Commerce System (ecommerce_models.py)"),
    ("Python", "test_fastapi_validation.py", "3. FastAPI & Pydantic Validation (test_fastapi_validation.py)"),
    ("Node", "mongoose_models.js", "4. Mongoose Student & Blog Validation (mongoose_models.js)"),
    ("Node", "ecommerce_mongoose.js", "5. E-Commerce Mongoose Validation (ecommerce_mongoose.js)"),
]

def run():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    failed = []

    for runtime, filename, label in SCRIPTS:
        print(f"\n--- {label} ---", flush=True)
        filepath = os.path.join(current_dir, filename)
        cmd = [sys.executable, filepath] if runtime == "Python" else ["node", filepath]
        
        result = subprocess.run(cmd, cwd=current_dir, capture_output=False)
        if result.returncode != 0:
            print(f"Error running {filename} (exit code {result.returncode})", flush=True)
            failed.append(filename)

    print("\n--------------------------------------------------", flush=True)
    if not failed:
        print("All Lecture 15 tasks executed successfully.", flush=True)
    else:
        print(f"Some tasks failed: {failed}", flush=True)
    print("--------------------------------------------------", flush=True)


if __name__ == "__main__":
    run()
