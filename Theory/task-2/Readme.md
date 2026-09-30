# Task 2: Student Management REST API with Flask

## Overview
This task demonstrates creating a lightweight **RESTful API** in Python using the **Flask** microframework. It implements basic routing, JSON response serialization with `jsonify`, path variable type casting (`<int:student_id>`), and HTTP 404 error handling for non-existent entities.

**Location:** [`Theory/task-2/`](file:///d:/Desktop/Backend%20Development/Theory/task-2/)

---

## Directory Structure

```text
task-2/
├── Readme.md
├── app.py             # Flask application entry point with route definitions
└── backend-project/   # Python virtual environment directory
    └── venv/
```

---

## Code Architecture

In [`app.py`](file:///d:/Desktop/Backend%20Development/Theory/task-2/app.py):

* **Framework Import**: `from flask import Flask, jsonify`
* **In-Memory Data Store**:
  ```python
  students = [
      {"id": 1, "name": "Aarav", "branch": "CSE"},
      {"id": 2, "name": "Diya", "branch": "ECE"},
      {"id": 3, "name": "Rohan", "branch": "IT"}
  ]
  ```
* **Dynamic Route Matching**:
  Uses `<int:student_id>` converter to automatically cast the path segment to an integer before passing it to the handler function.
* **Error Handling**:
  Returns a custom error dictionary with status code `404` when an ID is not found:
  ```python
  return jsonify({"error": "Student not found"}), 404
  ```

---

## API Endpoints

| Method | Route | Description | Success Response (200) | Failure Response (404) |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/` | API status check | `"Student Management API"` | N/A |
| `GET` | `/students` | Retrieve all student records | `[ { "id": 1, "name": "Aarav", "branch": "CSE" }, ... ]` | N/A |
| `GET` | `/students/<id>` | Fetch student record by numeric ID | `{ "id": 2, "name": "Diya", "branch": "ECE" }` | `{ "error": "Student not found" }` |

---

## Setup and Execution

### 1. Activate Virtual Environment (or create one)
```bash
# If using the existing environment in backend-project:
.\backend-project\venv\Scripts\Activate.ps1

# Or create a fresh virtual environment:
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install Flask
```bash
pip install flask
```

### 3. Run the Server
```bash
python app.py
```
Output:
```text
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### 4. Test the Endpoints
Using curl, PowerShell, or any browser:
```bash
# Get all students
curl http://127.0.0.1:5000/students

# Get student with ID 2
curl http://127.0.0.1:5000/students/2

# Test 404 error
curl http://127.0.0.1:5000/students/999
```
