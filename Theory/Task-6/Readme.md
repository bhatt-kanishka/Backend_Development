# Task 6: Client-Side State Management & Web Storage Architecture

> **Unit:** Theory Practical Tasks  
> **Topic:** Browser Storage Mechanisms and Client-Side State  
> **Location:** [`Theory/Task-6/`](file:///d:/Desktop/Backend%20Development/Theory/Task-6/)

Task 6 examines modern client-side data persistence mechanisms that allow backend developers to design responsive web applications without making unnecessary round-trip database queries for ephemeral or client-scoped state.

---

## Directory Modules

```text
Task-6/
├── Readme.md            # Task 6 overview & theory (this file)
└── lecture7/            # Lecture 7: Interactive To-Do List Application
    ├── Readme.md        # Lecture 7 implementation details
    ├── index.html       # Semantic HTML layout with task input & list
    ├── style.css        # Responsive styling & button controls
    └── script.js        # Web Storage API logic (localStorage vs sessionStorage)
```

---

## Key Theoretical Concepts

### 1. Web Storage API vs HTTP Cookies

| Feature | `localStorage` | `sessionStorage` | HTTP Cookies |
| :--- | :--- | :--- | :--- |
| **Capacity** | ~5 MB - 10 MB per origin | ~5 MB per origin | ~4 KB total per cookie |
| **Server Transmission** | Never automatically sent to server | Never automatically sent to server | Sent automatically in HTTP `Cookie` header on every request |
| **Lifetime** | Persists until explicitly cleared | Cleared when browser tab closes | Configured via `Expires` or `Max-Age` |
| **Accessibility** | Any window/tab of the same origin | Same tab only | Accessible via JavaScript (unless `HttpOnly` flag is set) |
| **Typical Use Case** | User theme, cached UI state, offline drafts | Single-session wizard form, temporary filters | Authentication tokens, session IDs |

### 2. Practical Implementation in [`lecture7/`](file:///d:/Desktop/Backend%20Development/Theory/Task-6/lecture7/)
- Implements a To-Do application demonstrating:
  - Long-term persistence across browser restarts with `localStorage.setItem("tasks", JSON.stringify(tasks))`.
  - Session-specific tracking with `sessionStorage.setItem("lastTask", task)`.
  - Synchronization with the DOM on dynamic add, delete, and clear actions.

---

## How to Test

To test the practical demonstration in this module:
```powershell
cd "Theory/Task-6/lecture7"
Start-Process "index.html"
```
Open **Browser Developer Tools** (<kbd>F12</kbd>) $\rightarrow$ **Application** or **Storage** tab $\rightarrow$ inspect `Local Storage` and `Session Storage` live as you add tasks.
