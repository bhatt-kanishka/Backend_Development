# Task 3: Introduction to RESTful APIs with FastAPI and Uvicorn

## Overview
This task demonstrates setting up and running a high-performance, asynchronous REST API using **FastAPI** and the **Uvicorn** ASGI web server in Python.

**Location:** [`Theory/Task_3/`](file:///d:/Desktop/Backend%20Development/Theory/Task_3/)

---

## Directory Structure

```text
Task_3/
├── Readme.md
├── main.py            # FastAPI application definition and Uvicorn runner
├── .gitignore         # Git ignore rules for Python artifacts
└── venv/              # Python virtual environment
```

---

## Technical Details

### [`main.py`](file:///d:/Desktop/Backend%20Development/Theory/Task_3/main.py)
```python
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, REST!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
```

### Key Highlights
1. **Modern Python Standards**: FastAPI utilizes Python 3 type hints for automatic request validation, serialization, and interactive schema generation.
2. **ASGI Performance**: Runs on Uvicorn, an ultra-fast ASGI server implementation based on `uvloop` and `httptools`.
3. **Hot Reloading**: Enabled via `reload=True` inside `uvicorn.run()`, ensuring changes in code immediately reflect without restarting the process manually.
4. **Built-in Interactive Documentation**:
   - **Swagger UI**: Automatically available at `http://127.0.0.1:8000/docs`
   - **ReDoc**: Automatically available at `http://127.0.0.1:8000/redoc`

---

## API Endpoints

| Method | Endpoint | Response Body | Description |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | `{"message": "Hello, REST!"}` | Basic API health check / root endpoint |
| `GET` | `/docs` | Interactive HTML | Interactive Swagger UI API documentation |
| `GET` | `/redoc` | Interactive HTML | ReDoc alternative documentation format |

---

## Setup and Running

### 1. Activate Virtual Environment
```bash
# In Windows PowerShell:
.\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies
```bash
pip install fastapi uvicorn
```

### 3. Start the Server
You can launch the server using either:
```bash
python main.py
```
Or directly using the Uvicorn CLI:
```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

### 4. Verify in Browser
- Visit `http://127.0.0.1:8000/` to see the JSON output.
- Visit `http://127.0.0.1:8000/docs` to test endpoints via Swagger UI.
