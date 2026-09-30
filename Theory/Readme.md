# Backend Development: Theory Modules and Practical Tasks

## Overview
This directory encompasses all practical tasks, lecture assignments, and architectural demonstrations for the **Backend Development Theory** curriculum. The curriculum explores diverse backend paradigms, comparing Python frameworks (**Flask**, **FastAPI**) with modern JavaScript runtime ecosystems (**Node.js**, **Express.js**), along with storage mechanisms and developer productivity tooling.

---

## Directory Navigation

```text
Theory/
├── Readme.md                    # Master Theory curriculum documentation (this file)
├── demo.js                      # Python Flask reference script
├── task-2/                      # Task 2: Flask REST API with JSON responses
│   ├── app.py
│   └── Readme.md
├── Task_3/                      # Task 3: FastAPI REST API with Uvicorn & Swagger UI
│   ├── main.py
│   └── Readme.md
├── Task_4/                      # Task 4: Nodemon Developer Workflow & Process Watching
│   └── Readme.md
├── ssr_demmo_Task_5/            # Task 5: Server-Side Rendering (SSR) with FastAPI & Jinja2
│   ├── main.py
│   ├── Templates/
│   └── Readme.md
├── Task-6/                      # Task 6: Client-Side State & Storage Architecture
│   └── lecture7/                # Lecture 7: Web Storage API (localStorage vs sessionStorage)
│       ├── index.html
│       ├── style.css
│       ├── script.js
│       └── Readme.md
├── express-demo/                # Express.js HTTP Server & Route Basics
│   ├── server.js
│   └── Readme.md
└── Unit-1/                      # Unit 1 Academic Module Resources
```

---

## Curriculum Modules Summary

### 1. [Task 2: Flask REST API](file:///d:/Desktop/Backend%20Development/Theory/task-2/Readme.md)
* **Technology**: Python 3, Flask.
* **Core Concepts**: Microframework architecture, routing, JSON serialization with `jsonify()`, path variable casting (`<int:id>`), HTTP status codes (200 OK, 404 Not Found).
* **Run**: `python app.py` (Port 5000).

### 2. [Task 3: FastAPI REST API](file:///d:/Desktop/Backend%20Development/Theory/Task_3/Readme.md)
* **Technology**: Python 3, FastAPI, Uvicorn ASGI server.
* **Core Concepts**: Modern asynchronous Python, type hints, automatic OpenAPI/Swagger UI generation (`/docs`), hot reloading.
* **Run**: `uvicorn main:app --reload` or `python main.py` (Port 8000).

### 3. [Task 4: Nodemon Process Watching](file:///d:/Desktop/Backend%20Development/Theory/Task_4/Readme.md)
* **Technology**: Node.js, Nodemon, Chokidar.
* **Core Concepts**: Developer experience (DX), file system watchers, automatic process termination and restart upon code changes.
* **Usage**: `npx nodemon <file>.js`.

### 4. [Task 5: Server-Side Rendering (SSR)](file:///d:/Desktop/Backend%20Development/Theory/ssr_demmo_Task_5/Readme.md)
* **Technology**: Python 3, FastAPI, Jinja2 Templates.
* **Core Concepts**: SSR vs. Client-Side Rendering (CSR), template inheritance, conditional rendering (`{% if %}`), and data loops (`{% for %}`).
* **Run**: `python main.py` (Port 8000).

### 5. [Task 6 / Lecture 7: Web Storage API](file:///d:/Desktop/Backend%20Development/Theory/Task-6/lecture7/Readme.md)
* **Technology**: HTML5, Vanilla JavaScript, CSS3.
* **Core Concepts**: Browser data persistence, comparing `localStorage` (long-term) with `sessionStorage` (tab lifecycle), JSON serialization, DOM manipulation in a To-Do list app.
* **Run**: Open `index.html` in browser.

### 6. [Express Demo](file:///d:/Desktop/Backend%20Development/Theory/express-demo/Readme.md)
* **Technology**: Node.js, Express.js.
* **Core Concepts**: Server bootstrapping, HTTP routing, endpoint design, handler callbacks.
* **Run**: `node server.js` (Port 3000).

---

## Key Framework Comparison

| Framework | Language | Architecture | Speed / Throughput | Documentation | Typical Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Flask** | Python | WSGI (Synchronous) | Moderate | Manual / Extension | Lightweight microservices, MVPs |
| **FastAPI** | Python | ASGI (Asynchronous) | Very High | Auto Swagger & ReDoc | High-performance async APIs, AI/ML backends |
| **Express.js** | JavaScript (Node.js) | Event Loop (Single-threaded) | Very High | Manual / Community | Scalable real-time web apps, full-stack JS |
