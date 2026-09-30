# Experiment 12A: Building RESTful APIs and Dynamic Views with Node.js, Express, and EJS !!

## Overview
This experiment demonstrates building backend web applications using **Node.js** and the **Express.js** framework. It covers request-response handling, RESTful routing, URL route parameters, query string parsing, HTTP request body handling, and Server-Side Rendering (SSR) using the **EJS (Embedded JavaScript)** template engine.

**Location:** [`Lab/Experiment_12A/nodejs-express-lab/`](file:///d:/Desktop/Backend%20Development/Lab/Experiment_12A/nodejs-express-lab/)

---

## Project Structure

```text
Experiment_12A/
├── Readme.md
└── nodejs-express-lab/
    ├── app.js             # Main Express server and route handlers
    ├── script.js          # Independent Node.js script demonstration
    ├── package.json       # Project dependencies and metadata
    ├── package-lock.json  # Dependency lockfile
    ├── node_modules/      # Installed npm packages
    └── views/             # EJS view templates
        ├── home.ejs       # Home template with variable interpolation
        ├── users.ejs      # Dynamic table iteration using EJS loops
        └── profile.ejs    # Card component with object property bindings
```

---

## Key Learning Concepts

1. **Express Server Initialization**: Configuring listening ports and middleware.
2. **Middleware Usage**:
   - `express.json()`: Parses incoming JSON payload requests.
   - `express.urlencoded({ extended: true })`: Parses URL-encoded form data.
3. **Template Engine Configuration**:
   - Setting `view engine` to `'ejs'`.
   - Setting the views directory using `app.set('views', './views')`.
4. **Different Response Types**:
   - `res.send()`: Plain text and direct HTML strings.
   - `res.json()`: JSON formatted responses with status codes.
   - `res.render()`: Dynamic HTML views compiled with EJS templates and context data.
5. **Route Parameters & Query Parsing**:
   - Path variables via `req.params.id`.
   - Query strings via `req.query` (`q`, `page`, `limit`, `num1`, `num2`, `operation`).

---

## API Endpoints Reference

| Method | Endpoint | Description | Sample Request / Output |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Basic welcome response | `"Welcome to Express Server!"` |
| `GET` | `/text` | Plain text response | Plain text output |
| `GET` | `/html` | Direct HTML snippet response | `<h1>HTML Response</h1>` |
| `GET` | `/json` | JSON response payload | `{"status": "success", "data": {...}}` |
| `GET` | `/user/:id` | Path parameter extraction | `GET /user/42` -> `{ "userId": "42" }` |
| `GET` | `/search` | Query parameter extraction | `GET /search?q=nodejs&page=2&limit=5` |
| `GET` | `/calculate` | Query-based math operations | `GET /calculate?num1=10&num2=5&operation=add` |
| `POST` | `/register` | JSON body registration demo | Receives `{ username, email, password }` |
| `POST` | `/login` | Mock authentication | Validates against sample credentials |
| `GET` | `/home` | EJS rendered home page | Compiles [`home.ejs`](file:///d:/Desktop/Backend%20Development/Lab/Experiment_12A/nodejs-express-lab/views/home.ejs) with page title and message |
| `GET` | `/users` | EJS rendered user table | Compiles [`users.ejs`](file:///d:/Desktop/Backend%20Development/Lab/Experiment_12A/nodejs-express-lab/views/users.ejs) iterating through user array |
| `GET` | `/profile/:id` | EJS rendered profile card | Compiles [`profile.ejs`](file:///d:/Desktop/Backend%20Development/Lab/Experiment_12A/nodejs-express-lab/views/profile.ejs) with user object |

---

## Setup and Running

### 1. Install Dependencies
Navigate into the project directory and install the required npm packages:
```bash
cd "Lab/Experiment_12A/nodejs-express-lab"
npm install
```

### 2. Run the Express Application
```bash
node app.js
```
The server will start on port `3000`:
```text
Server running on http://localhost:3000
```

### 3. Run the Standalone Script
To execute the basic Node.js test script:
```bash
node script.js
```
Output:
```text
Hello from Node.js!
Welcome Student to Backend Development
Sum of numbers: 15
```
