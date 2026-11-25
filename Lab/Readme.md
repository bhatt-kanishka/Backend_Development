# Backend Development: Laboratory Experiments & Assessments

> **Course:** Backend Web Development Laboratory  
> **Repository Hub:** [`Lab/`](file:///d:/Desktop/Backend%20Development/Lab/)

Welcome to the **Laboratory** section of the Backend Development repository. This directory contains hands-on experiments, practical implementations, and assessment projects designed to build practical mastery of modern web architecture, client-server communication, server-side rendering, session management, and full-stack database-backed applications.

---

## Laboratory Curriculum Overview

```text
Lab/
├── Readme.md                          # Master Laboratory Guide (this file)
│
├── Experiment-1/                      # Experiment 1: Semantic HTML5 & Web Forms
│   ├── Experiment-1.html
│   └── README.md
│
├── Experiment-7-8/                    # Experiment 7-8: ES6 Client-Side Task Manager
│   ├── app.js
│   ├── index.html
│   └── Readme.md
│
├── Experiment-12A/                    # Experiment 12A: Express REST API & EJS SSR
│   ├── Readme.md                      # Experiment 12A Overview
│   └── nodejs-express-lab/            # Full Express + EJS Application
│       ├── Readme.md                  # Node.js Express Lab Guide
│       ├── app.js                     # Express server & route definitions
│       ├── package.json               # Dependencies (express, ejs)
│       └── views/                     # Dynamic EJS views (home, users, profile)
│
├── Experiment-12B/                    # Experiment 12B: State Management
│   ├── Readme.md                      # Cookies & Sessions Documentation
│   ├── Cookies_example.js             # Client-side cookie handling (cookie-parser)
│   └── session_example.js             # Server-side session tracking (express-session)
│
├── Experiment-15/                     # Experiment 15: Django To-Do Application
│   ├── README.md
│   ├── manage.py
│   ├── pyproject.toml
│   ├── todo/
│   └── todo_project/
│
├── Lab-Assessment-B/                  # Lab Assessment: Eisenhower Matrix App
│   ├── Readme.md                      # Assessment Specification & Architecture
│   ├── app.js                         # Production full-stack Express + MongoDB application
│   ├── package.json                   # Dependencies (express, ejs, mongodb)
│   ├── public/                        # Client assets & CSS styling
│   └── views/                         # Interactive EJS matrix dashboard templates
│
└── Student-API/                       # FastAPI + SQLAlchemy Student Management API
    ├── README.md
    ├── main.py
    ├── database.py
    ├── models.py
    ├── schemas.py
    └── requirements.txt
```

---

## Experiments & Projects Directory

### 1. [Experiment 1: Semantic HTML5 Elements & Web Forms](file:///d:/Desktop/Backend%20Development/Lab/Experiment-1/README.md)
* **Files:** [`Experiment-1.html`](file:///d:/Desktop/Backend%20Development/Lab/Experiment-1/Experiment-1.html), [`README.md`](file:///d:/Desktop/Backend%20Development/Lab/Experiment-1/README.md)
* **Core Concepts:**
  - Semantic HTML5 layout tags (`<header>`, `<nav>`, `<section>`, `<article>`, `<aside>`, `<footer>`).
  - Advanced form validation (`tel`, `date`, `radio`, `checkbox`, `select`, `textarea`).
  - Multimedia embedding with native HTML5 `<audio>` and `<video>` players.
  - Interactive HTML5 2D `<canvas>` rendering.
* **Testing:** Open [`Experiment-1.html`](file:///d:/Desktop/Backend%20Development/Lab/Experiment-1/Experiment-1.html) in any modern web browser.

---

### 2. [Experiment 12A: Express.js REST API & Server-Side Rendering](file:///d:/Desktop/Backend%20Development/Lab/Experiment-12A/Readme.md)
* **Directory:** [`Lab/Experiment-12A/nodejs-express-lab/`](file:///d:/Desktop/Backend%20Development/Lab/Experiment-12A/nodejs-express-lab/)
* **Core Concepts:**
  - Initializing an Express.js web server and configuring HTTP routes.
  - Parameterized routing (`req.params.id`) and query string handling (`req.query`).
  - Request body parsing with `express.json()` and `express.urlencoded()`.
  - Dynamic Server-Side Rendering (SSR) using the EJS templating engine.
* **Execution:**
  ```powershell
  cd "Lab/Experiment-12A/nodejs-express-lab"
  npm install
  node app.js
  ```
  Access application at: `http://localhost:3000`

---

### 3. [Experiment 12B: State Management — Cookies & Sessions](file:///d:/Desktop/Backend%20Development/Lab/Experiment-12B/Readme.md)
* **Files:** [`Cookies_example.js`](file:///d:/Desktop/Backend%20Development/Lab/Experiment-12B/Cookies_example.js), [`session_example.js`](file:///d:/Desktop/Backend%20Development/Lab/Experiment-12B/session_example.js)
* **Core Concepts:**
  - Understanding the stateless nature of HTTP and mechanisms for state preservation.
  - Client-side cookies with `cookie-parser`: Setting, reading, and clearing cookies with TTL options (`maxAge`).
  - Server-side sessions with `express-session`: Session IDs stored in signed HTTP cookies, tracking visit counts, and secure session destruction upon logout.
* **Execution:**
  ```powershell
  cd "Lab/Experiment-12B"
  # Run Cookies Demonstration
  node Cookies_example.js
  # Run Sessions Demonstration
  node session_example.js
  ```

---

### 4. [Lab Assessment B: Eisenhower Matrix Task Management Application](file:///d:/Desktop/Backend%20Development/Lab/Lab-Assessment-B/Readme.md)
* **Directory:** [`Lab/Lab-Assessment-B/`](file:///d:/Desktop/Backend%20Development/Lab/Lab-Assessment-B/)
* **Core Concepts:**
  - Full-stack CRUD architecture integrating Express.js, EJS templates, and a native MongoDB driver.
  - Implementation of the **Eisenhower Decision Matrix** (categorizing tasks into Urgent & Important quadrants).
  - Search, filtering, priority scoring, task status toggling, and clean responsive user interface with dark mode.
* **Execution:**
  ```powershell
  cd "Lab/Lab-Assessment-B"
  npm install
  node app.js
  ```
  Access application at: `http://localhost:3000`

---

### 5. [Experiment 7-8: ES6 Client-Side Task Manager](file:///d:/Desktop/Backend%20Development/Lab/Experiment-7-8/Readme.md)
* **Directory:** [`Lab/Experiment-7-8/`](file:///d:/Desktop/Backend%20Development/Lab/Experiment-7-8/)
* **Core Concepts:**
  - ES6 classes, arrow functions, destructuring, and template literals.
  - Immutable state updates with the spread operator and `Array.filter()` / `Array.map()`.
  - Event delegation with a single listener on the task list.
* **Execution:** Open [`index.html`](file:///d:/Desktop/Backend%20Development/Lab/Experiment-7-8/index.html) in a browser.

---

### 6. [Experiment 15: Django To-Do Application](file:///d:/Desktop/Backend%20Development/Lab/Experiment-15/README.md)
* **Directory:** [`Lab/Experiment-15/`](file:///d:/Desktop/Backend%20Development/Lab/Experiment-15/)
* **Core Concepts:**
  - Django MVT architecture with SQLite ORM models and migrations.
  - Function-based CRUD views, template inheritance, and form handling.
  - External REST API consumption with timeout and error handling.
* **Execution:**
  ```powershell
  cd "Lab/Experiment-15"
  python manage.py migrate
  python manage.py runserver
  ```
  Access application at: `http://127.0.0.1:8000`

---

### 7. [Student API: FastAPI + SQLAlchemy](file:///d:/Desktop/Backend%20Development/Lab/Student-API/README.md)
* **Directory:** [`Lab/Student-API/`](file:///d:/Desktop/Backend%20Development/Lab/Student-API/)
* **Core Concepts:**
  - FastAPI route handlers with Pydantic v2 request/response schemas.
  - SQLAlchemy ORM models, session dependency injection, and cascade deletes.
  - Pagination, filtering, search, and automatic Swagger documentation.
* **Execution:**
  ```powershell
  cd "Lab/Student-API"
  pip install -r requirements.txt
  python main.py
  ```
  Access application at: `http://127.0.0.1:8000/docs`

---

## Lab Execution Quick-Reference

| Experiment | Focus Area | Technology | Command | Port |
| :--- | :--- | :--- | :--- | :--- |
| **Exp 1** | Semantic Markup & Forms | HTML5, CSS3, Canvas | `Start-Process Experiment-1.html` | Browser |
| **Exp 7-8** | ES6 Client-Side State | Vanilla JavaScript (ES6+) | `Start-Process index.html` | Browser |
| **Exp 12A** | REST APIs & SSR | Express.js, EJS | `node app.js` | 3000 |
| **Exp 12B (Cookies)** | Client Cookies | Express, cookie-parser | `node Cookies_example.js` | 3000 |
| **Exp 12B (Sessions)** | Server Sessions | Express, express-session | `node session_example.js` | 3000 |
| **Exp 15** | Django MVT & ORM | Django, SQLite | `python manage.py runserver` | 8000 |
| **Assessment B** | Full-Stack Database CRUD | Express, EJS, MongoDB | `node app.js` | 3000 |
| **Student API** | Production REST API | FastAPI, SQLAlchemy | `python main.py` | 8000 |
