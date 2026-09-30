# Node.js & Express.js Laboratory Application

## Overview
A comprehensive backend application built with **Node.js**, **Express.js**, and **EJS (Embedded JavaScript)** templating. This project showcases essential server-side patterns including:
- Serving multiple response formats (plain text, raw HTML, structured JSON).
- Route parameters (`/user/:id`) and query string handling (`/search`, `/calculate`).
- Body parsing for incoming POST requests (`/register`, `/login`).
- Dynamic Server-Side Rendering (SSR) using EJS templates.

**Location:** [`nodejs-express-lab/`](file:///d:/Desktop/Backend%20Development/nodejs-express-lab/)

---

## Directory Layout

```text
nodejs-express-lab/
├── Readme.md          # Documentation for this lab
├── app.js             # Main application server with routes and middleware
├── script.js          # Standalone demonstration Node.js script
├── package.json       # Node.js dependencies (express, ejs)
├── package-lock.json  # Dependency tree lock
└── views/             # Server-rendered EJS templates
    ├── home.ejs       # Home view with title, heading, and date
    ├── users.ejs      # Tabular user roster using iteration
    └── profile.ejs    # Card-based single user profile
```

---

## Available Endpoints

### Informational & Data Endpoints
* `GET /` - Base greeting.
* `GET /text` - Plain text response via `res.send()`.
* `GET /html` - HTML tags sent directly via `res.send()`.
* `GET /json` - Structured JSON response via `res.json()`.
* `GET /user/:id` - Extracts URL parameter (`req.params.id`).
* `GET /search?q={query}&page={page}&limit={limit}` - Query parameter extraction with fallback defaults.
* `GET /calculate?num1={n1}&num2={n2}&operation={add|subtract|multiply|divide}` - Performs calculation based on query inputs.

### Authentication & Mutation Endpoints
* `POST /register` - Consumes JSON body containing `{ username, email, password }` and returns confirmation.
* `POST /login` - Validates credentials (`test@example.com` / `password123`) and issues a mock token.

### Server-Side Rendered Views (EJS)
* `GET /home` - Renders [`views/home.ejs`](file:///d:/Desktop/Backend%20Development/nodejs-express-lab/views/home.ejs).
* `GET /users` - Renders [`views/users.ejs`](file:///d:/Desktop/Backend%20Development/nodejs-express-lab/views/users.ejs) displaying an array of users.
* `GET /profile/:id` - Renders [`views/profile.ejs`](file:///d:/Desktop/Backend%20Development/nodejs-express-lab/views/profile.ejs) displaying user card details.

---

## Getting Started

1. **Install Dependencies**:
   ```bash
   npm install
   ```

2. **Launch the Server**:
   ```bash
   node app.js
   ```
   The server listens at `http://localhost:3000`.

3. **Run Helper Script**:
   ```bash
   node script.js
   ```
