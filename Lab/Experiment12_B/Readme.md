# Experiment 12B: State Management in Express.js (Cookies & Sessions)

## Overview
HTTP is a stateless protocol, meaning each request from a client is treated as completely independent with no inherent memory of previous requests. This experiment demonstrates two fundamental mechanisms for maintaining state across HTTP requests in Express.js:
1. **Client-Side Cookies** using `cookie-parser`.
2. **Server-Side Sessions** using `express-session`.

**Location:** [`Lab/Experiment12_B/`](file:///d:/Desktop/Backend%20Development/Lab/Experiment12_B/)

---

## File Structure

```text
Experiment12_B/
├── Readme.md
├── Cookies_example.js  # Demonstration of setting, reading, and clearing cookies
└── session_example.js  # Demonstration of session tracking and session destruction
```

---

## Part 1: Cookie Management (`Cookies_example.js`)

Cookies are small pieces of data sent by a web server and stored on the client's browser. With each subsequent request to the server, the browser transmits the cookie back.

### Implementation Details
* **Middleware**: `cookieParser()` parses the `Cookie` header on incoming requests and populates `req.cookies`.
* **Setting a Cookie**:
  ```javascript
  res.cookie('username', 'JohnDoe', { maxAge: 900000 }); // Expiration: 15 minutes
  ```
* **Reading a Cookie**:
  ```javascript
  const user = req.cookies['username'];
  ```
* **Deleting a Cookie**:
  ```javascript
  res.clearCookie('username');
  ```

### Endpoints
| Route | Method | Description |
| :--- | :--- | :--- |
| `/set-cookie` | `GET` | Creates a cookie named `username` with value `JohnDoe` and 15-minute validity |
| `/get-cookie` | `GET` | Reads and returns the value of `username` stored in browser cookies |
| `/delete-cookie` | `GET` | Instructs the client browser to remove the `username` cookie |

### Running the Cookie Example
```bash
# Install dependencies if not already present in the workspace
npm install express cookie-parser

# Run the cookie server
node Cookies_example.js
```
Open your browser and visit:
1. `http://localhost:3000/set-cookie`
2. `http://localhost:3000/get-cookie` (inspect cookie via DevTools > Application > Storage > Cookies)
3. `http://localhost:3000/delete-cookie`

---

## Part 2: Session Management (`session_example.js`)

Unlike cookies where data resides on the client, sessions store sensitive user data on the server. The client is only issued a signed, unique session ID cookie (typically `connect.sid`).

### Implementation Details
* **Middleware**: `express-session` initializes session handling:
  ```javascript
  app.use(session({
      secret: 'mysecretkey',     // Key used to sign the session ID cookie
      resave: false,             // Prevents saving session if unmodified
      saveUninitialized: true    // Forces a session that is new to be saved
  }));
  ```
* **Session Storage & Counter**:
  ```javascript
  if (req.session.views) {
      req.session.views++;
      res.send(`Welcome back! You visited ${req.session.views} times.`);
  } else {
      req.session.views = 1;
      res.send('Welcome to the session demo. Refresh to count visits.');
  }
  ```
* **Session Destruction**:
  ```javascript
  req.session.destroy(err => { ... });
  ```

### Endpoints
| Route | Method | Description |
| :--- | :--- | :--- |
| `/` | `GET` | Increments and displays the visit counter stored in the server session |
| `/destroy` | `GET` | Terminates and purges the active session |

### Running the Session Example
```bash
# Install express-session if needed
npm install express express-session

# Run the session server
node session_example.js
```
Open your browser and visit:
1. `http://localhost:3000/` (Refresh repeatedly to see the visit counter increment: 1, 2, 3...)
2. `http://localhost:3000/destroy` to clear your active session.
3. Refresh `http://localhost:3000/` again to verify the counter resets to 1.

---

## Comparison: Cookies vs. Sessions

| Feature | Cookies (`Cookies_example.js`) | Sessions (`session_example.js`) |
| :--- | :--- | :--- |
| **Storage Location** | Client Browser | Server Memory (or DB store) |
| **Capacity** | ~4 KB | Limited only by server memory |
| **Security** | Susceptible to client tampering / theft if unencrypted | High (client only holds opaque session ID) |
| **Use Cases** | UI preferences, theme selection, remember-me tokens | User authentication, shopping carts, sensitive workflows |
