# Express.js in Docker Container

## Purpose
A lightweight **Express.js API server** configured to run inside a Docker container (Ubuntu/Node.js environment), listening on all network interfaces (`0.0.0.0`).

---

## What This Code Does
This application creates a minimal web server using Express.js that:
- Listens on port `3000` across all container interfaces (`0.0.0.0`) so that Docker can forward traffic from your host machine
- Serves a welcome greeting at `GET /`
- Returns a list of enrolled students as JSON at `GET /api/students`
- Uses `nodemon` in development mode for live reload upon code changes

---

## Concepts Covered

| Concept | Where It Appears |
|:--------|:-----------------|
| **Express Server Initialization** | `const app = express();` |
| **Binding Host `0.0.0.0`** | `app.listen(PORT, "0.0.0.0")` — critical for container networking |
| **REST JSON Endpoint** | `app.get("/api/students", ...)` returning JSON array |
| **Process Management & DX** | `nodemon` in `devDependencies` for auto-restart |
| **Docker Containerization** | Designed to run inside an isolated Ubuntu / Alpine Node container |

---

## Prerequisites and Dependencies

- **Node.js** (v18+ or inside container)
- **Dependencies** (from `package.json`):
  - `express`: `^5.1.0`
- **Dev Dependencies**:
  - `nodemon`: `^3.1.0`

---

## Installation and Run Steps

### Local Execution (without Docker)
```bash
# Navigate to directory
cd Theory/Express-in-Docker

# Install dependencies
npm install

# Start with nodemon (auto-reload)
npm run dev

# Or start directly with node
npm start
```

### Running inside Docker
```bash
# Build Docker image
docker build -t express-docker-demo .

# Run container mapping host port 3000 to container port 3000
docker run -p 3000:3000 express-docker-demo
```
Access the endpoints at `http://localhost:3000/` and `http://localhost:3000/api/students`.

---

## File Structure

```text
Express-in-Docker/
├── README.md        # This documentation file
├── app.js           # Express server setup and route handlers
└── package.json     # Node.js dependencies and run scripts
```

---

## Code Walkthrough

```javascript
// 1. Import Express
const express = require("express");
const app = express();
const PORT = 3000;

// 2. Root route: returns text confirming container status
app.get("/", (req, res) => {
    res.send("Hello! Express is running inside Docker.");
});

// 3. API endpoint: returns student collection in JSON
app.get("/api/students", (req, res) => {
    res.json([
        { id: 1, name: "Rahul", course: "BCA" },
        { id: 2, name: "Amit", course: "MCA" }
    ]);
});

// 4. Listen on 0.0.0.0 (all interfaces) rather than 127.0.0.1
// Inside Docker, listening on localhost (127.0.0.1) restricts traffic to container internals only.
app.listen(PORT, "0.0.0.0", () => {
    console.log(`Server running on port ${PORT}`);
});
```

---

## Example Requests and Responses

### Root Health Check
```bash
curl http://localhost:3000/
```
**Response (200 OK):**
```text
Hello! Express is running inside Docker.
```

### Students API
```bash
curl http://localhost:3000/api/students
```
**Response (200 OK):**
```json
[
  { "id": 1, "name": "Rahul", "course": "BCA" },
  { "id": 2, "name": "Amit", "course": "MCA" }
]
```

---

## Common Errors and Fixes

| Error | Cause | Fix |
|:------|:------|:----|
| `Connection refused` when curling from host | App listened on `localhost` (`127.0.0.1`) instead of `0.0.0.0` | Bind host must be `"0.0.0.0"` in `app.listen()` |
| `Port already in use` | Another process is using port 3000 | Stop conflicting process or change `PORT` variable |
| Docker container exits immediately | No foreground process | Ensure CMD or ENTRYPOINT runs `node app.js` in foreground |

---

## Key Takeaways

1. In containerized applications, servers must bind to **`0.0.0.0`** instead of default `localhost` so the Docker bridge network can route host traffic into the container.
2. Port mapping syntax `-p <host_port>:<container_port>` exposes internal container services to your local machine.
3. Keeping dependencies lightweight and cleanly separating `devDependencies` (like `nodemon`) prepares applications for production container builds.
