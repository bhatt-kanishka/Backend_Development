# Express.js Demo Server

## Overview
This directory contains a quick-start demonstration of an **Express.js** web application running on Node.js. It illustrates foundational HTTP request dispatching, route definition, and server initialization.

**Location:** [`express-demo/`](file:///d:/Desktop/Backend%20Development/express-demo/)

---

## Files

* [`server.js`](file:///d:/Desktop/Backend%20Development/express-demo/server.js): The core entry script setting up an Express application instance and registering route listeners.
* `package.json`: Manages the project manifest, dependencies (`express`), and scripts.
* `package-lock.json`: Locks dependency versions for reproducible builds.

---

## Routes

| Method | Path | Response Type | Description |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Text (`text/html`) | Root greeting: `"Welcome to the Student Management API"` |
| `GET` | `/students` | Text (`text/html`) | Index response: `"List of all students"` |
| `GET` | `/students/1` | Text (`text/html`) | Detail response: `"Student: Aarav, Roll No: 1"` |

---

## How to Run

1. Open a terminal in this folder:
   ```bash
   cd "d:\Desktop\Backend Development\express-demo"
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the Express server:
   ```bash
   node server.js
   ```
4. Access via browser or curl:
   ```bash
   curl http://localhost:3000/
   curl http://localhost:3000/students
   curl http://localhost:3000/students/1
   ``` ***
