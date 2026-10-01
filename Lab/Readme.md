# Backend Development: Laboratory Experiments & Assessments

> **Course:** Backend Web Development Laboratory  
> **Repository Hub:** [`Lab/`](file:///d:/Desktop/Backend%20Development/Lab/)

Welcome to the **Laboratory** section of the Backend Development repository. This directory contains hands-on experiments, practical implementations, and assessment projects designed to build practical mastery of modern web architecture, client-server communication, server-side rendering, session management, and full-stack database-backed applications.

---

## Laboratory Curriculum Overview

```text
Lab/
├── Readme.md                          # Master Laboratory Guide (this file)
├── Experiment-1.html                  # Experiment 1: Semantic HTML5 & Web Forms
├── Experiment_1_Readme.md             # Experiment 1: Detailed Lab Documentation
│
├── Experiment_12A/                    # Experiment 12A: Express REST API & EJS SSR
│   ├── Readme.md                      # Experiment 12A Overview
│   └── nodejs-express-lab/            # Full Express + EJS Application
│       ├── Readme.md                  # Node.js Express Lab Guide
│       ├── app.js                     # Express server & route definitions
│       ├── package.json               # Dependencies (express, ejs)
│       └── views/                     # Dynamic EJS views (home, users, profile)
│
├── Experiment12_B/                    # Experiment 12B: State Management
│   ├── Readme.md                      # Cookies & Sessions Documentation
│   ├── Cookies_example.js             # Client-side cookie handling (cookie-parser)
│   └── session_example.js             # Server-side session tracking (express-session)
│
└── lab_Assessment_B/                  # Lab Assessment: Eisenhower Matrix App
    ├── Readme.md                      # Assessment Specification & Architecture
    ├── app.js                         # Production full-stack Express + MongoDB application
    ├── package.json                   # Dependencies (express, ejs, mongodb)
    ├── public/                        # Client assets & CSS styling
    └── views/                         # Interactive EJS matrix dashboard templates
```

---

## Experiments & Projects Directory

### 1. [Experiment 1: Semantic HTML5 Elements & Web Forms](file:///d:/Desktop/Backend%20Development/Lab/Experiment_1_Readme.md)
* **Files:** [`Experiment-1.html`](file:///d:/Desktop/Backend%20Development/Lab/Experiment-1.html), [`Experiment_1_Readme.md`](file:///d:/Desktop/Backend%20Development/Lab/Experiment_1_Readme.md)
* **Core Concepts:**
  - Semantic HTML5 layout tags (`<header>`, `<nav>`, `<section>`, `<article>`, `<aside>`, `<footer>`).
  - Advanced form validation (`tel`, `date`, `radio`, `checkbox`, `select`, `textarea`).
  - Multimedia embedding with native HTML5 `<audio>` and `<video>` players.
  - Interactive HTML5 2D `<canvas>` rendering.
* **Testing:** Open [`Experiment-1.html`](file:///d:/Desktop/Backend%20Development/Lab/Experiment-1.html) in any modern web browser.

---

### 2. [Experiment 12A: Express.js REST API & Server-Side Rendering](file:///d:/Desktop/Backend%20Development/Lab/Experiment_12A/Readme.md)
* **Directory:** [`Lab/Experiment_12A/nodejs-express-lab/`](file:///d:/Desktop/Backend%20Development/Lab/Experiment_12A/nodejs-express-lab/)
* **Core Concepts:**
  - Initializing an Express.js web server and configuring HTTP routes.
  - Parameterized routing (`req.params.id`) and query string handling (`req.query`).
  - Request body parsing with `express.json()` and `express.urlencoded()`.
  - Dynamic Server-Side Rendering (SSR) using the EJS templating engine.
* **Execution:**
  ```powershell
  cd "Lab/Experiment_12A/nodejs-express-lab"
  npm install
  node app.js
  ```
  Access application at: `http://localhost:3000`

---

### 3. [Experiment 12B: State Management — Cookies & Sessions](file:///d:/Desktop/Backend%20Development/Lab/Experiment12_B/Readme.md)
* **Files:** [`Cookies_example.js`](file:///d:/Desktop/Backend%20Development/Lab/Experiment12_B/Cookies_example.js), [`session_example.js`](file:///d:/Desktop/Backend%20Development/Lab/Experiment12_B/session_example.js)
* **Core Concepts:**
  - Understanding the stateless nature of HTTP and mechanisms for state preservation.
  - Client-side cookies with `cookie-parser`: Setting, reading, and clearing cookies with TTL options (`maxAge`).
  - Server-side sessions with `express-session`: Session IDs stored in signed HTTP cookies, tracking visit counts, and secure session destruction upon logout.
* **Execution:**
  ```powershell
  cd "Lab/Experiment12_B"
  # Run Cookies Demonstration
  node Cookies_example.js
  # Run Sessions Demonstration
  node session_example.js
  ```

---

### 4. [Lab Assessment B: Eisenhower Matrix Task Management Application](file:///d:/Desktop/Backend%20Development/Lab/lab_Assessment_B/Readme.md)
* **Directory:** [`Lab/lab_Assessment_B/`](file:///d:/Desktop/Backend%20Development/Lab/lab_Assessment_B/)
* **Core Concepts:**
  - Full-stack CRUD architecture integrating Express.js, EJS templates, and a native MongoDB driver.
  - Implementation of the **Eisenhower Decision Matrix** (categorizing tasks into Urgent & Important quadrants).
  - Search, filtering, priority scoring, task status toggling, and clean responsive user interface with dark mode.
* **Execution:**
  ```powershell
  cd "Lab/lab_Assessment_B"
  npm install
  node app.js
  ```
  Access application at: `http://localhost:3000`

---

## Lab Execution Quick-Reference

| Experiment | Focus Area | Technology | Command | Port |
| :--- | :--- | :--- | :--- | :--- |
| **Exp 1** | Semantic Markup & Forms | HTML5, CSS3, Canvas | `Start-Process Experiment-1.html` | Browser |
| **Exp 12A** | REST APIs & SSR | Express.js, EJS | `node app.js` | 3000 |
| **Exp 12B (Cookies)** | Client Cookies | Express, cookie-parser | `node Cookies_example.js` | 3000 |
| **Exp 12B (Sessions)** | Server Sessions | Express, express-session | `node session_example.js` | 3000 |
| **Assessment B** | Full-Stack Database CRUD | Express, EJS, MongoDB | `node app.js` | 3000 |
