# Backend Development: Theory Modules and Practical Tasks

## Overview
This directory encompasses all practical tasks, lecture assignments, and architectural demonstrations for the **Backend Development Theory** curriculum. The curriculum explores diverse backend paradigms, comparing Python frameworks (**Flask**, **FastAPI**, **SQLAlchemy**) with modern JavaScript runtime ecosystems (**Node.js**, **Express.js**, **Mongoose**), along with storage mechanisms, validation pipelines, and developer tooling.

---

## Directory Navigation

```text
Theory/
├── Readme.md                    # Master Theory curriculum documentation (this file)
├── demo.js                      # Python Flask reference script
│
├── Unit-1/                      # Unit 1: Foundations of Backend Web Development
│   └── Readme.md
│
├── task-2/                      # Task 2: Flask REST API with JSON responses
│   ├── app.py
│   └── Readme.md
│
├── Task_3/                      # Task 3: FastAPI REST API with Uvicorn & Swagger UI
│   ├── main.py
│   └── Readme.md
│
├── Task_4/                      # Task 4: Nodemon Developer Workflow & Process Watching
│   └── Readme.md
│
├── ssr_demmo_Task_5/            # Task 5: Server-Side Rendering (SSR) with FastAPI & Jinja2
│   ├── main.py
│   ├── Templates/
│   └── Readme.md
│
├── Task-6/                      # Task 6: Client-Side State & Storage Architecture
│   ├── Readme.md
│   └── lecture7/                # Lecture 7: Web Storage API (localStorage vs sessionStorage)
│       ├── index.html
│       ├── style.css
│       ├── script.js
│       └── Readme.md
│
├── express-demo/                # Express.js HTTP Server & Route Basics
│   ├── server.js
│   └── Readme.md
│
├── Lecture_15/                  # Lecture 15: Data Modeling (Designing Models for Applications)
│   ├── Readme.md
│   └── ORM/                     # SQLAlchemy ORM, Mongoose ODM, Pydantic Validation & PBL
│       ├── Readme.md
│       ├── Database.py
│       ├── ecommerce_models.py
│       ├── ecommerce_mongoose.js
│       ├── fastapi_pydantic_validation.py
│       ├── test_fastapi_validation.py
│       ├── mongoose_models.js
│       ├── physical_schema.sql
│       ├── save_to_mongodb.js
│       └── run_all.py
│
└── Lecture_16/                  # Lecture 16: CRUD Operations in Databases
    └── Readme.md
```

---

## Curriculum Modules Summary

### 1. [Unit 1: Foundations of Backend Development](file:///d:/Desktop/Backend%20Development/Theory/Unit-1/Readme.md)
* **Core Concepts**: Client-server architecture, HTTP request-response lifecycle, status code classes (2xx, 4xx, 5xx), REST architectural constraints.

### 2. [Task 2: Flask REST API](file:///d:/Desktop/Backend%20Development/Theory/task-2/Readme.md)
* **Technology**: Python 3, Flask.
* **Core Concepts**: Microframework architecture, routing, JSON serialization with `jsonify()`, path variable casting (`<int:id>`), HTTP status codes (200 OK, 404 Not Found).
* **Run**: `python app.py` (Port 5000).

### 3. [Task 3: FastAPI REST API](file:///d:/Desktop/Backend%20Development/Theory/Task_3/Readme.md)
* **Technology**: Python 3, FastAPI, Uvicorn ASGI server.
* **Core Concepts**: Modern asynchronous Python, type hints, automatic OpenAPI/Swagger UI generation (`/docs`), hot reloading.
* **Run**: `uvicorn main:app --reload` or `python main.py` (Port 8000).

### 4. [Task 4: Nodemon Process Watching](file:///d:/Desktop/Backend%20Development/Theory/Task_4/Readme.md)
* **Technology**: Node.js, Nodemon, Chokidar.
* **Core Concepts**: Developer experience (DX), file system watchers, automatic process termination and restart upon code changes.
* **Usage**: `npx nodemon <file>.js`.

### 5. [Task 5: Server-Side Rendering (SSR)](file:///d:/Desktop/Backend%20Development/Theory/ssr_demmo_Task_5/Readme.md)
* **Technology**: Python 3, FastAPI, Jinja2 Templates.
* **Core Concepts**: SSR vs. Client-Side Rendering (CSR), template inheritance, conditional rendering (`{% if %}`), and data loops (`{% for %}`).
* **Run**: `python main.py` (Port 8000).

### 6. [Task 6 / Lecture 7: Web Storage API](file:///d:/Desktop/Backend%20Development/Theory/Task-6/lecture7/Readme.md)
* **Technology**: HTML5, Vanilla JavaScript, CSS3.
* **Core Concepts**: Browser data persistence, comparing `localStorage` (long-term) with `sessionStorage` (tab lifecycle), JSON serialization, DOM manipulation in a To-Do list app.
* **Run**: Open `index.html` in browser.

### 7. [Express Demo](file:///d:/Desktop/Backend%20Development/Theory/express-demo/Readme.md)
* **Technology**: Node.js, Express.js.
* **Core Concepts**: Server bootstrapping, HTTP routing, endpoint design, handler callbacks.
* **Run**: `node server.js` (Port 3000).

### 8. [Lecture 15: Data Modeling (ORM & ODM)](file:///d:/Desktop/Backend%20Development/Theory/Lecture_15/ORM/Readme.md)
* **Technology**: Python (SQLAlchemy, FastAPI, Pydantic), Node.js (Mongoose), SQLite, PostgreSQL.
* **Core Concepts**:
  - Three levels of modeling: Conceptual (ER), Logical (Types & Constraints), Physical (SQL DDL & Indexes).
  - Student Management System ORM with bidirectional relationships (`back_populates`) and cascade deletion verification.
  - E-Commerce System data modeling across Customer, Product, Cart, and Order entities.
  - Request validation using Pydantic (`EmailStr`, regex patterns, 422 error handling).
  - Object Document Modeling (ODM) with Mongoose schemas and built-in validators.
* **Run**: `python run_all.py` inside [`Theory/Lecture_15/ORM/`](file:///d:/Desktop/Backend%20Development/Theory/Lecture_15/ORM/).

### 9. [Lecture 16: Database CRUD Operations](file:///d:/Desktop/Backend%20Development/Theory/Lecture_16/Readme.md)
* **Core Concepts**: ACID transaction management, connection pooling, pagination, and SQL vs NoSQL CRUD patterns.

---

## Framework & Tooling Comparison

| Framework | Language | Architecture | Throughput | Documentation | Typical Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Flask** | Python | WSGI (Sync) | Moderate | Manual / Extension | Lightweight microservices, MVPs |
| **FastAPI** | Python | ASGI (Async) | Very High | Auto Swagger & ReDoc | High-performance async APIs, AI/ML backends |
| **Express.js** | Node.js | Event Loop | Very High | Manual / Community | Real-time web apps, full-stack JavaScript |
| **SQLAlchemy**| Python | ORM / Core | High | Official / Sphinx | Enterprise relational database modeling |
| **Mongoose** | Node.js | ODM / Schema | Very High | Official | MongoDB document modeling & validation |
