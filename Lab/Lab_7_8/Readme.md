# Lab 7 & 8: ES6 To-Do Application

## Purpose
A simple browser-based To-Do list that demonstrates modern **ES6+ JavaScript** features. No backend server is needed — everything runs in the browser.

---

## What This Code Does
This is a client-side To-Do app where you can:
- **Add** tasks by typing in a text box and clicking "Add" (or pressing Enter)
- **Toggle** a task as completed (click the task text — it gets a strikethrough)
- **Delete** tasks individually with a "Delete" button

The app keeps an in-memory array of tasks and re-renders the entire list whenever something changes. There is no database or server — when you refresh the page, the tasks are gone.

---

## Concepts Covered

| Concept | Where It Appears |
|:--------|:-----------------|
| **ES6 Classes** | `class Task { constructor(title) { ... } }` creates task objects with `id`, `title`, and `completed` |
| **Arrow Functions** | `const renderTasks = () => { ... }` — concise function syntax used throughout |
| **Spread Operator** | `tasks = [...tasks, new Task(title)]` — creates a new array instead of mutating the old one |
| **Destructuring** | `tasks.forEach(({ id, title, completed }) => ...)` — pulls properties out of each task object |
| **Template Literals** | Used for string interpolation (backtick strings) |
| **`const` / `let`** | Block-scoped variable declarations replacing `var` |
| **Event Delegation** | A single `click` listener on the `<ul>` handles both toggle and delete for all `<li>` items |
| **`Array.filter()` / `Array.map()`** | Immutable array operations for deleting and toggling tasks |
| **`Date.now()`** | Generates a unique numeric ID for each task |
| **DOM Manipulation** | `document.createElement()`, `classList.add()`, `appendChild()`, `innerHTML = ""` |

---

## Prerequisites and Dependencies

- **Any modern web browser** (Chrome, Firefox, Edge, Safari)
- **No npm packages required** — this is pure HTML + JavaScript
- **No Node.js needed** — open the HTML file directly

---

## Installation and Run Steps

```bash
# Navigate to the lab folder
cd Lab/Lab_7_8

# Option 1: Open directly in the browser (Windows PowerShell)
Start-Process index.html

# Option 2: Use a simple HTTP server (Python)
python -m http.server 8080
# Then open http://localhost:8080 in your browser

# Option 3: Use npx serve
npx serve .
```

---

## File Structure

```text
Lab_7_8/
├── Readme.md       # This documentation file
├── index.html      # HTML page with inline CSS and a script tag loading app.js
└── app.js          # All JavaScript logic (ES6 To-Do app)
```

---

## Code Walkthrough

### `index.html` — The User Interface
A minimal HTML page with:
- An `<input>` field for typing new tasks (`id="taskInput"`)
- An "Add" `<button>` (`id="addBtn"`)
- An empty `<ul>` (`id="taskList"`) that gets populated dynamically
- Inline CSS for basic styling (strikethrough for completed tasks, red delete button)
- A `<script src="app.js">` tag at the bottom to load the JavaScript

### `app.js` — The Application Logic

**1. State & DOM References (Lines 1–7)**
```javascript
let tasks = [];
const input = document.getElementById("taskInput");
const addBtn = document.getElementById("addBtn");
const list = document.getElementById("taskList");
```
The `tasks` array holds all task objects. DOM elements are cached once at startup.

**2. Task Class (Lines 10–16)**
```javascript
class Task {
    constructor(title) {
        this.id = Date.now();     // unique numeric ID
        this.title = title;
        this.completed = false;
    }
}
```
Each task gets a unique timestamp ID, a title, and starts as not completed.

**3. Render Function (Lines 19–36)**
Clears the entire list, then loops through every task using destructuring. For each task it creates an `<li>` with a `<span>` (task text) and a delete `<button>`. If a task is completed, the span gets a `.done` CSS class (strikethrough).

**4. Add Task (Lines 39–45)**
```javascript
const addTask = () => {
    const title = input.value.trim();
    if (!title) return;
    tasks = [...tasks, new Task(title)]; // spread operator — immutable update
    input.value = "";
    renderTasks();
};
```
Uses the spread operator to create a new array rather than pushing to the existing one (a functional programming pattern).

**5. Event Delegation (Lines 55–68)**
Instead of attaching a listener to every individual button and span, a single listener on the `<ul>` handles all clicks:
- If the click target has class `delete-btn` → filter that task out
- Otherwise → toggle the `completed` property using `map()` and spread

---

## Expected Output

When you open `index.html` in a browser:
1. You see a heading "My To-Do List", a text input, and an "Add" button
2. Type "Learn ES6 Classes" and click Add → the task appears in the list
3. Click the task text → it gets a strikethrough (completed)
4. Click "Delete" → the task is removed
5. Press Enter in the input box → also adds a task

---

## Common Errors and Fixes

| Error | Cause | Fix |
|:------|:------|:----|
| Nothing happens when clicking Add | `app.js` not loading | Make sure `index.html` and `app.js` are in the same folder |
| `Cannot read properties of null` | Script runs before DOM loads | The `<script>` tag must be at the bottom of `<body>`, not in `<head>` |
| Tasks disappear on refresh | Expected — there's no persistence | This lab intentionally uses in-memory state; see Task 6 (Web Storage) for persistence |

---

## Key Takeaways

1. **ES6 Classes** give JavaScript a clean, familiar syntax for creating objects with shared structure
2. **The spread operator** (`...`) lets you create new arrays/objects without mutating the originals — a key concept in React and modern JS
3. **Event delegation** is more efficient than attaching individual listeners — especially important when list items are added/removed dynamically
4. **`Array.filter()` and `Array.map()`** are the functional alternatives to loops for transforming and filtering data
5. This lab is a foundation for understanding frontend state management before moving to server-side storage (databases, sessions)
