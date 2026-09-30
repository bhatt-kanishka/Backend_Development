# Theory: Express.js Student Management Demo

## Overview
This directory demonstrates basic web server setup and route configuration using **Express.js**, the standard web application framework for Node.js. It implements a simple routing structure for a Student Management API.

**Location:** [`Theory/express-demo/`](file:///d:/Desktop/Backend%20Development/Theory/express-demo/)

---

## Directory Structure

```text
express-demo/
├── Readme.md
├── server.js          # Express server with basic routing
├── package.json       # Project dependencies (express)
├── package-lock.json  # Dependency tree lockfile
└── node_modules/      # Installed dependencies
```

---

## Code Breakdown: [`server.js`](file:///d:/Desktop/Backend%20Development/Theory/express-demo/server.js)

```javascript
const express = require("express");
const app = express();

app.get("/", (req, res) => {
    res.send("Welcome to the Student Management API");
});

app.get("/students", (req, res) => {
    res.send("List of all students");
});

app.get("/students/1", (req, res) => {
    res.send("Student: Aarav, Roll No: 1");
});

app.listen(3000, () => {
    console.log("Server started at http://localhost:3000");
});
```

---

## Endpoints

| Method | Endpoint | Return Value | Description |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Plain text | Welcome message |
| `GET` | `/students` | Plain text | Student directory placeholder |
| `GET` | `/students/1` | Plain text | Specific student detail |

---

## Setup and Running

1. **Install Dependencies**:
   ```bash
   npm install
   ```

2. **Start the Server**:
   ```bash
   node server.js
   ```

3. **Test in Browser or Terminal**:
   - `http://localhost:3000/`
   - `http://localhost:3000/students`
   - `http://localhost:3000/students/1`
