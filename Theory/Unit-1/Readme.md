# Unit 1: Foundations of Backend Web Development

> **Course Unit:** Unit 1 — Core Architecture & Web Protocols  
> **Location:** [`Theory/Unit-1/`](file:///d:/Desktop/Backend%20Development/Theory/Unit-1/)

Unit 1 lays the architectural and conceptual foundation for backend web development. It explores how client-server systems communicate over standard network protocols, how HTTP governs web transactions, and how backend services are organized to process requests and deliver data.

---

## Unit 1 Learning Objectives

1. **Client-Server Architecture:**
   - Understanding the division of responsibility between the presentation layer (client/frontend) and the business logic/data persistence layer (server/backend).
   - Stateless request-response cycle and stateless protocol design.

2. **Hypertext Transfer Protocol (HTTP/1.1 & HTTP/2):**
   - Anatomy of an HTTP Request: Method, URL, Protocol Version, Headers, Body.
   - Anatomy of an HTTP Response: Status Code, Reason Phrase, Headers, Body.
   - Idempotency & Safety of HTTP methods (`GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `HEAD`, `OPTIONS`).

3. **HTTP Status Code Classifications:**
   - **`1xx` Informational:** Protocol switching (`101 Switching Protocols`).
   - **`2xx` Success:** Standard completion (`200 OK`, `201 Created`, `204 No Content`).
   - **`3xx` Redirection:** Location forwarding (`301 Moved Permanently`, `302 Found`, `304 Not Modified`).
   - **`4xx` Client Errors:** Bad input or auth failure (`400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `422 Unprocessable Entity`).
   - **`5xx` Server Errors:** Backend failures (`500 Internal Server Error`, `502 Bad Gateway`, `503 Service Unavailable`).

4. **REST Architectural Style (Representational State Transfer):**
   - Resource-based URI design (e.g. `/api/students`, `/api/courses`).
   - Using standard HTTP verbs for operations (CRUD mapping).
   - Uniform interface, statelessness, cacheability, and layered system principles.

---

## Unit 1 Related Implementations in Repository

Practical demonstrations supporting Unit 1 concepts are implemented across:

* [`Theory/task-2/`](file:///d:/Desktop/Backend%20Development/Theory/task-2/) — Microframework REST API implementation using Python Flask with JSON serialization and dynamic route variables.
* [`Theory/Task_3/`](file:///d:/Desktop/Backend%20Development/Theory/Task_3/) — High-performance asynchronous API service built with FastAPI and Uvicorn with auto-generated OpenAPI documentation.
* [`Theory/express-demo/`](file:///d:/Desktop/Backend%20Development/Theory/express-demo/) — Node.js & Express.js server bootstrapping and route registration.
