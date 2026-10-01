# Unit 1 — Task 2: Student Management REST API

> **Course Unit:** Unit 1: Foundations of Backend Development  
> **Topic:** Practical REST API Implementation & HTTP Routing  
> **Location:** [`Theory/Unit-1/Task-2/`](file:///d:/Desktop/Backend%20Development/Theory/Unit-1/Task-2/)

This module references the practical laboratory task for Unit 1, demonstrating microframework HTTP request processing, JSON serialization, and dynamic routing in a Student Management API.

---

## Practical Implementation Link

The complete runnable codebase, route handlers, and documentation for Task 2 are located in:

👉 **[`Theory/task-2/`](file:///d:/Desktop/Backend%20Development/Theory/task-2/)**

### Key Features Implemented:
* **`GET /students`** — Fetches complete collection of enrolled student records in JSON format.
* **`GET /students/<int:student_id>`** — Retrieves individual student profile by integer primary key path variable.
* **Structured 404 Error Handling** — Returns clean JSON error responses for unmapped or non-existent student resources.

---

## How to Run

```powershell
cd "Theory/task-2"
python app.py
```
Server listens on: `http://127.0.0.1:5000`
