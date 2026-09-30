# Backend Development Repository

Welcome to the **Backend Development** repository. This repository serves as a centralized hub for hands-on laboratory experiments, academic coursework, and architectural demonstrations covering modern backend engineering practices.

It encompasses practical implementations across multiple runtime environments (**Node.js** and **Python**), web frameworks (**Express.js**, **FastAPI**, **Flask**), templating engines (**EJS**, **Jinja2**), state management techniques (Cookies, Sessions, Web Storage API), and database integration (**MongoDB**, **PostgreSQL**).

---

## Table of Contents

- [Backend Development Repository](#backend-development-repository)
  - [Table of Contents](#table-of-contents)
  - [Technology Stack Matrix](#technology-stack-matrix)
  - [Repository Architecture](#repository-architecture)
  - [Folder & Module Documentation](#folder--module-documentation)
    - [1. Laboratory Experiments (`Lab/`)](#1-laboratory-experiments-lab)
    - [2. Theory Practical Tasks (`Theory/`)](#2-theory-practical-tasks-theory)
    - [3. Standalone Applications & Demos](#3-standalone-applications--demos)
    - [4. Database Environments (`postgres/` \& `psql/`)](#4-database-environments-postgres--psql)
    - [5. Root Files \& Assets](#5-root-files--assets)
  - [Prerequisites \& Global Setup](#prerequisites--global-setup)
    - [Node.js Setup](#nodejs-setup)
    - [Python Setup](#python-setup)
  - [Quick-Start Execution Cheat Sheet](#quick-start-execution-cheat-sheet)

---

## Technology Stack Matrix

| Category | Technologies / Libraries | Description / Usage |
| :--- | :--- | :--- |
| **Runtimes** | Node.js, Python 3.14 | Core execution environments |
| **Web Frameworks** | Express.js 5.x, FastAPI, Flask | HTTP server routing, REST API creation, request lifecycle |
| **ASGI / WSGI Servers** | Uvicorn, Werkzeug | High-concurrency ASGI server for FastAPI; WSGI server for Flask |
| **Templating (SSR)** | EJS (Node.js), Jinja2 (Python) | Server-Side Rendering of dynamic HTML views with embedded data |
| **Databases** | MongoDB (NoSQL), PostgreSQL (SQL) | Document-oriented and relational database management |
| **Database Drivers** | `mongodb` (Node.js), `psycopg2` (Python) | Native database connectivity and operations |
| **State Management** | `cookie-parser`, `express-session`, Web Storage API | Client cookies, server sessions, `localStorage`, `sessionStorage` |
| **Developer Tooling** | Nodemon, npm, Python venv | Process watching, hot-reloading, package management |
| **Frontend Basics** | HTML5 Semantic Elements, CSS3, JavaScript | User interfaces for full-stack and lab demonstrations |

---

## Repository Architecture

```text
Backend Development/
├── Readme.md                             # Master repository guide (this file)
├── package.json                          # Root Node.js dependencies (express)
├── package-lock.json                     # Root npm lockfile
├── mongodb-compass_1.45.4_amd64.deb      # MongoDB Compass GUI debian package
│
├── Lab/                                  # Laboratory experiments & assessments
│   ├── Experiment_1_Readme.md            # Documentation for Experiment 1
│   ├── Experiment-1.html                 # Experiment 1: Semantic HTML5 elements & forms
│   │
│   ├── Experiment_12A/                   # Experiment 12A: Express REST API & EJS SSR
│   │   ├── Readme.md
│   │   └── nodejs-express-lab/           # Express server, route params, calculations, EJS views
│   │
│   ├── Experiment12_B/                   # Experiment 12B: State Management
│   │   ├── Readme.md
│   │   ├── Cookies_example.js            # Client-side cookie management (cookie-parser)
│   │   └── session_example.js            # Server-side session tracking (express-session)
│   │
│   └── lab_Assessment_B/                 # Lab Assessment: Eisenhower Matrix Todo App
│       ├── Readme.md                     # Assessment documentation & API specifications
│       ├── app.js                        # Full-stack Node/Express/MongoDB app
│       ├── package.json
│       ├── public/                       # CSS styles & client assets
│       └── views/                        # EJS dynamic UI templates
│
├── Theory/                               # Theory tasks and practical modules
│   ├── Readme.md                         # Theory master documentation
│   ├── demo.js                           # Python Flask reference script
│   │
│   ├── task-2/                           # Task 2: Student Management REST API in Flask
│   │   ├── Readme.md
│   │   ├── app.py                        # Flask API with dynamic routes and 404 handling
│   │   └── backend-project/venv/         # Python virtual environment
│   │
│   ├── Task_3/                           # Task 3: REST API with FastAPI & Uvicorn
│   │   ├── Readme.md
│   │   ├── main.py                       # FastAPI app with auto Swagger UI at /docs
│   │   └── venv/                         # Python virtual environment
│   │
│   ├── Task_4/                           # Task 4: Nodemon Developer Workflow & Tooling
│   │   └── Readme.md
│   │
│   ├── ssr_demmo_Task_5/                 # Task 5: Server-Side Rendering (FastAPI + Jinja2)
│   │   ├── Readme.md
│   │   ├── main.py                       # FastAPI SSR server
│   │   ├── Templates/                    # Jinja2 HTML templates (students.html, home.html)
│   │   └── venv/                         # Python virtual environment
│   │
│   ├── Task-6/                           # Task 6: Client-Side Web Storage Architecture
│   │   └── lecture7/                     # Lecture 7: To-Do App (localStorage vs sessionStorage)
│   │       ├── Readme.md
│   │       ├── index.html
│   │       ├── style.css
│   │       └── script.js
│   │
│   ├── express-demo/                     # Theory Express.js intro server
│   │   ├── Readme.md
│   │   └── server.js
│   │
│   └── Unit-1/                           # Academic Unit 1 resources
│
├── express-demo/                         # Root standalone Express server demo
│   ├── Readme.md
│   └── server.js
│
├── nodejs-express-lab/                   # Root standalone Node.js, Express & EJS lab
│   ├── Readme.md
│   ├── app.js
│   ├── script.js
│   └── views/
│
├── postgres/                             # PostgreSQL Python development virtual environment
│   ├── Readme.md                         # PostgreSQL setup, driver installation, and sample code
│   └── pyvenv.cfg
│
└── psql/                                 # PostgreSQL CLI administration virtual environment
    ├── Readme.md                         # psql commands cheat sheet and configuration
    └── pyvenv.cfg
```

---

## Folder & Module Documentation

### 1. Laboratory Experiments ([`Lab/`](file:///d:/Desktop/Backend%20Development/Lab/))

* **[Experiment 1: HTML5 Elements Demonstration](file:///d:/Desktop/Backend%20Development/Lab/Experiment_1_Readme.md)**
  * **File:** [`Experiment-1.html`](file:///d:/Desktop/Backend%20Development/Lab/Experiment-1.html)
  * **Topics:** Semantic structuring (`<header>`, `<nav>`, `<section>`, `<article>`, `<aside>`, `<footer>`), advanced `<form>` elements (date, tel, search, radio, checkboxes, select), tabular layout, `<canvas>` 2D graphics context, and native `<audio>`/`<video>` multimedia controls.

* **[Experiment 12A: REST APIs & EJS Views in Express.js](file:///d:/Desktop/Backend%20Development/Lab/Experiment_12A/Readme.md)**
  * **Directory:** [`Experiment_12A/nodejs-express-lab/`](file:///d:/Desktop/Backend%20Development/Lab/Experiment_12A/nodejs-express-lab/)
  * **Topics:** Express HTTP routing, request parameters (`req.params.id`), query parsing (`req.query` for search & calculation operations), POST body parsing (`express.json()`), mock authentication (`/login`, `/register`), and dynamic template rendering with EJS (`home.ejs`, `users.ejs`, `profile.ejs`).

* **[Experiment 12B: State Management (Cookies & Sessions)](file:///d:/Desktop/Backend%20Development/Lab/Experiment12_B/Readme.md)**
  * **Files:** [`Cookies_example.js`](file:///d:/Desktop/Backend%20Development/Lab/Experiment12_B/Cookies_example.js) & [`session_example.js`](file:///d:/Desktop/Backend%20Development/Lab/Experiment12_B/session_example.js)
  * **Topics:** Statelessness of HTTP protocol, client-side cookies with `cookie-parser` (setting, reading, clearing with TTL maxAge), and server-side sessions with `express-session` (visit counters, secret-signed session cookies, session destruction).

* **[Lab Assessment B: Eisenhower Matrix Todo Application](file:///d:/Desktop/Backend%20Development/Lab/lab_Assessment_B/Readme.md)**
  * **Directory:** [`Lab/lab_Assessment_B/`](file:///d:/Desktop/Backend%20Development/Lab/lab_Assessment_B/)
  * **Topics:** Production-style CRUD backend using Node.js, Express.js, MongoDB native driver, and EJS. Implements the Eisenhower Decision Matrix (Do, Schedule, Delegate, Eliminate), search, filtering, sorting, priority calculation, and dark mode.

---

### 2. Theory Practical Tasks ([`Theory/`](file:///d:/Desktop/Backend%20Development/Theory/Readme.md))

* **[Task 2: Flask REST API](file:///d:/Desktop/Backend%20Development/Theory/task-2/Readme.md)**
  * **File:** [`Theory/task-2/app.py`](file:///d:/Desktop/Backend%20Development/Theory/task-2/app.py)
  * **Features:** Microframework routing, student collection endpoint (`GET /students`), parameterized single lookup (`GET /students/<int:student_id>`), and structured 404 JSON error handling.

* **[Task 3: FastAPI & Uvicorn REST API](file:///d:/Desktop/Backend%20Development/Theory/Task_3/Readme.md)**
  * **File:** [`Theory/Task_3/main.py`](file:///d:/Desktop/Backend%20Development/Theory/Task_3/main.py)
  * **Features:** High-performance asynchronous REST API running on Uvicorn ASGI server with automated Swagger UI documentation at `http://127.0.0.1:8000/docs`.

* **[Task 4: Nodemon Developer Workflow](file:///d:/Desktop/Backend%20Development/Theory/Task_4/Readme.md)**
  * **Features:** File system process watching, auto-reloading Node.js server scripts upon file modifications, and `nodemon.json` configuration strategies.

* **[Task 5: Server-Side Rendering with FastAPI & Jinja2](file:///d:/Desktop/Backend%20Development/Theory/ssr_demmo_Task_5/Readme.md)**
  * **Files:** [`Theory/ssr_demmo_Task_5/main.py`](file:///d:/Desktop/Backend%20Development/Theory/ssr_demmo_Task_5/main.py) & [`Templates/`](file:///d:/Desktop/Backend%20Development/Theory/ssr_demmo_Task_5/Templates/)
  * **Features:** SSR architecture, Jinja2 template interpolation, conditional logic, and looping through dynamic student arrays inside server-rendered HTML.

* **[Task 6 / Lecture 7: Web Storage API (localStorage & sessionStorage)](file:///d:/Desktop/Backend%20Development/Theory/Task-6/lecture7/Readme.md)**
  * **Directory:** [`Theory/Task-6/lecture7/`](file:///d:/Desktop/Backend%20Development/Theory/Task-6/lecture7/)
  * **Features:** Client-side data persistence without a database, differences between `localStorage` (persistent across sessions) and `sessionStorage` (tab lifecycle), JSON stringification, and DOM manipulation.

* **[Theory Express Demo](file:///d:/Desktop/Backend%20Development/Theory/express-demo/Readme.md)**
  * **File:** [`Theory/express-demo/server.js`](file:///d:/Desktop/Backend%20Development/Theory/express-demo/server.js)
  * **Features:** Introductory Express application demonstrating route registration and port binding.

---

### 3. Standalone Applications & Demos

* **[Express Demo (`express-demo/`)](file:///d:/Desktop/Backend%20Development/express-demo/Readme.md)**: Standalone Express server located at the repository root.
* **[Node.js Express Lab (`nodejs-express-lab/`)](file:///d:/Desktop/Backend%20Development/nodejs-express-lab/Readme.md)**: Complete full-featured Express + EJS lab application located at the repository root.

---

### 4. Database Environments ([`postgres/`](file:///d:/Desktop/Backend%20Development/postgres/Readme.md) & [`psql/`](file:///d:/Desktop/Backend%20Development/psql/Readme.md))

* **[`postgres/`](file:///d:/Desktop/Backend%20Development/postgres/Readme.md)**: Dedicated Python virtual environment configured for connecting to PostgreSQL instances using Python database adapters (`psycopg2-binary`, `asyncpg`, `SQLAlchemy`).
* **[`psql/`](file:///d:/Desktop/Backend%20Development/psql/Readme.md)**: Dedicated Python environment and documentation reference for PostgreSQL command-line administration tools and schema migration workflows.

---

### 5. Root Files & Assets

* [`package.json`](file:///d:/Desktop/Backend%20Development/package.json): Root project descriptor specifying dependencies (e.g. Express 5.x).
* `mongodb-compass_1.45.4_amd64.deb`: Debian package installer for the MongoDB Compass GUI client.
* `.gitignore`: Configured to exclude operating system artifacts and sensitive files from git tracking.

---

## Prerequisites & Global Setup

### Node.js Setup
Ensure Node.js (version 18+ or 20+ recommended) is installed on your system:
```bash
node -v
npm -v
```

### Python Setup
Ensure Python 3.10+ (current system uses Python 3.14) is installed:
```bash
python --version
```

---

## Quick-Start Execution Cheat Sheet

| Task / Experiment | Folder Path | Command to Execute | Access URL |
| :--- | :--- | :--- | :--- |
| **HTML5 Demo** | `Lab/` | `Start-Process Experiment-1.html` | In browser |
| **Express Lab 12A** | `Lab/Experiment_12A/nodejs-express-lab` | `npm install && node app.js` | `http://localhost:3000` |
| **Cookies Demo** | `Lab/Experiment12_B` | `node Cookies_example.js` | `http://localhost:3000/set-cookie` |
| **Sessions Demo** | `Lab/Experiment12_B` | `node session_example.js` | `http://localhost:3000` |
| **Eisenhower Todo** | `Lab/lab_Assessment_B` | `npm install && node app.js` | `http://localhost:3000` |
| **Flask API (Task 2)** | `Theory/task-2` | `pip install flask && python app.py` | `http://127.0.0.1:5000/students` |
| **FastAPI REST (Task 3)** | `Theory/Task_3` | `pip install fastapi uvicorn && python main.py` | `http://127.0.0.1:8000/docs` |
| **FastAPI SSR (Task 5)** | `Theory/ssr_demmo_Task_5` | `pip install fastapi uvicorn jinja2 && python main.py` | `http://127.0.0.1:8000/` |
| **To-Do Web Storage** | `Theory/Task-6/lecture7` | `Start-Process index.html` | In browser |
