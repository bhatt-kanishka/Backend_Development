# Task 5: Server-Side Rendering (SSR) with FastAPI and Jinja2

## Overview
This task demonstrates **Server-Side Rendering (SSR)** in Python using **FastAPI** coupled with the **Jinja2** templating engine. In SSR, the backend dynamically constructs complete HTML documents populated with database or application state before transmitting them over HTTP to the client browser.

**Location:** [`Theory/ssr_demmo_Task_5/`](file:///d:/Desktop/Backend%20Development/Theory/ssr_demmo_Task_5/)

---

## Directory Structure

```text
ssr_demmo_Task_5/
├── Readme.md
├── main.py            # FastAPI application with Jinja2 template renderer
├── Templates/         # Jinja2 HTML templates directory
│   ├── home.html      # Basic template with variable placeholder
│   └── students.html  # Dynamic table rendering with loops and conditionals
└── venv/              # Python virtual environment
```

---

## How It Works

### 1. Template Setup in [`main.py`](file:///d:/Desktop/Backend%20Development/Theory/ssr_demmo_Task_5/main.py)
```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="Templates")

students = [
    {"id": 1, "name": "Aarav", "branch": "CSE"},
    {"id": 2, "name": "Diya", "branch": "ECE"},
    {"id": 3, "name": "Rohan", "branch": "IT"},
]

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="students.html",
        context={"students": students}
    )
```

### 2. Jinja2 Templating Features in [`students.html`](file:///d:/Desktop/Backend%20Development/Theory/ssr_demmo_Task_5/Templates/students.html)
- **Conditional Evaluation**:
  ```jinja2
  {% if students|length == 0 %}
    <p>No students found.</p>
  {% else %}
  ```
- **Filter Pipelines**: `{{ students|length }}` calculates the total item count.
- **Iteration Loops**:
  ```jinja2
  {% for student in students %}
  <tr>
    <td>{{ student.id }}</td>
    <td>{{ student.name }}</td>
    <td>{{ student.branch }}</td>
  </tr>
  {% endfor %}
  ```

---

## Setup and Running

### 1. Activate Virtual Environment
```bash
# In Windows PowerShell:
.\venv\Scripts\Activate.ps1
```

### 2. Install Required Packages
```bash
pip install fastapi uvicorn jinja2
```

### 3. Start the Server
```bash
python main.py
```
Output:
```text
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
```

### 4. Open in Browser
Visit `http://127.0.0.1:8000/` to inspect the generated HTML table rendered on the server side.
