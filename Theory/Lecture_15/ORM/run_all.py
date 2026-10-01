"""
Master Test Runner for Lecture 15: Data Modeling
Executes all Python and Node.js demonstrations sequentially with formatted outputs.
"""

import subprocess
import sys
import os

SCRIPTS = [
    ("Python", "Database.py", "1. SQLAlchemy Student Management System CRUD & Cascade Verification"),
    ("Python", "ecommerce_models.py", "2. PBL Activity: E-Commerce System SQLAlchemy Data Model"),
    ("Python", "test_fastapi_validation.py", "3. Section 5.1: FastAPI + Pydantic Data Model Validation"),
    ("Node", "mongoose_models.js", "4. Section 4.2 & 5.2 / Lab 4 & 5: Mongoose ODM & Blog Schemas"),
    ("Node", "ecommerce_mongoose.js", "5. PBL Activity: Mongoose E-Commerce ODM Validation"),
]

def run():
    print("=" * 78)
    print("      LECTURE 15: COMPLETE DATA MODELING DEMONSTRATION SUITE")
    print("=" * 78)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    failed = []

    for runtime, filename, description in SCRIPTS:
        print(f"\n>>> Running: {description} [{filename}]")
        print("-" * 78)
        
        filepath = os.path.join(current_dir, filename)
        cmd = [sys.executable, filepath] if runtime == "Python" else ["node", filepath]
        
        result = subprocess.run(cmd, cwd=current_dir, capture_output=False)
        if result.returncode != 0:
            print(f"[FAIL] {filename} exited with code {result.returncode}")
            failed.append(filename)
        else:
            print(f"[SUCCESS] {filename} executed cleanly.")
        print("-" * 78)

    print("\n" + "=" * 78)
    if not failed:
        print(">>> ALL LECTURE 15 DEMONSTRATIONS AND LAB EXERCISES PASSED SUCCESSFULLY! <<<")
    else:
        print(f">>> FAILED MODULES: {failed} <<<")
    print("=" * 78)


if __name__ == "__main__":
    run()
