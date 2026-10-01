# Experiment 12A: Node.js Express Lab

> **Lab Assignment:** Experiment 12A  
> **Topic:** Building REST APIs and Server-Side Rendering with Express.js and EJS  
> **Location:** [`Lab/Experiment_12A/nodejs-express-lab/`](file:///d:/Desktop/Backend%20Development/Lab/Experiment_12A/nodejs-express-lab/)

This project demonstrates core backend web application development with **Express.js** and the **EJS** templating engine. It implements HTTP routing, request parameters, query string parsing, JSON APIs, form handling, and server-side view rendering.

---

## Directory Structure

```text
nodejs-express-lab/
├── Readme.md            # Lab guide & endpoint documentation (this file)
├── app.js               # Express application server and route definitions
├── package.json         # Project metadata and dependencies (express, ejs, nodemon)
├── script.js            # Client-side helper script
└── views/               # EJS dynamic UI templates
    ├── home.ejs         # Landing page template
    ├── users.ejs        # User list rendering template
    └── profile.ejs      # User profile view template
```

---

## Features & Endpoints Implemented

### 1. Basic Responses
* `GET /` — Welcome string message.
* `GET /text` — Plain text response (`res.send()`).
* `GET /html` — Inline HTML markup response.
* `GET /json` — Formatted JSON response with status and data payload.

### 2. Parameterized Routing & Query Handling
* `GET /user/:id` — Extracts dynamic route parameter `req.params.id`.
* `GET /search?q=query&page=1&limit=10` — Parses query string using `req.query`.
* `GET /calculate?num1=10&num2=5&operation=add` — Server-side calculator performing addition, subtraction, multiplication, and division.

### 3. POST Request Handling (Body Parsing)
* `POST /login` — Processes form login credentials (`username`, `password`) using `express.urlencoded()`.
* `POST /register` — Handles user registration with validation.
* `POST /api/users` — REST endpoint receiving JSON payload with `express.json()`.

### 4. Server-Side Rendering with EJS
* `GET /home` — Renders `views/home.ejs` with dynamic page title and welcome data.
* `GET /users` — Renders `views/users.ejs` passing an array of user objects to iterate over in EJS.
* `GET /profile` — Renders `views/profile.ejs` displaying authenticated user attributes.

---

## How to Install & Run

1. Navigate to the project directory:
   ```powershell
   cd "d:\Desktop\Backend Development\Lab\Experiment_12A\nodejs-express-lab"
   ```

2. Install dependencies:
   ```powershell
   npm install
   ```

3. Start the Express server:
   ```powershell
   # Standard start:
   node app.js

   # Or using nodemon for auto-reload:
   npm run dev
   ```

4. Open your browser or API client (Postman/curl) at:
   ```text
   http://localhost:3000
   ```

---

## Testing the Endpoints

| Method | Endpoint | Example Request / URL |
| :--- | :--- | :--- |
| `GET` | `/json` | `http://localhost:3000/json` |
| `GET` | `/user/:id` | `http://localhost:3000/user/101` |
| `GET` | `/calculate` | `http://localhost:3000/calculate?num1=20&num2=4&operation=divide` |
| `GET` | `/home` | `http://localhost:3000/home` |
| `GET` | `/users` | `http://localhost:3000/users` |
