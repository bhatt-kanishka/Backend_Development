# Lecture 7: Web Storage API (localStorage & sessionStorage)

## Overview
This lecture demonstrates state management and client-side data persistence using the **HTML5 Web Storage API**. It implements a complete, interactive **To-Do List** application that stores tasks persistently across browser sessions using `localStorage` and tracks session-specific interaction using `sessionStorage`.

**Location:** [`Theory/Task-6/lecture7/`](file:///d:/Desktop/Backend%20Development/Theory/Task-6/lecture7/)

---

## Directory Structure

```text
lecture7/
├── Readme.md
├── index.html   # Semantic UI markup with container, input, and task list
├── style.css    # Responsive styles and button layout
└── script.js    # Logic for Web Storage operations and DOM rendering
```

---

## Web Storage API Fundamentals

| Feature | `localStorage` | `sessionStorage` |
| :--- | :--- | :--- |
| **Lifetime** | Persists indefinitely until cleared by user or script | Cleared when browser tab/window is closed |
| **Scope** | Shared across all tabs/windows of the same origin | Accessible only within the specific tab that opened it |
| **Capacity** | ~5MB - 10MB per origin | ~5MB per origin |
| **Data Format** | Key-value pairs of **Strings** | Key-value pairs of **Strings** |

---

## Key Functions in [`script.js`](file:///d:/Desktop/Backend%20Development/Theory/Task-6/lecture7/script.js)

1. **Initialization**:
   Retrieves and parses saved tasks from `localStorage` on initial page load:
   ```javascript
   let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
   displayTasks();
   ```

2. **Adding a Task (`addTask`)**:
   - Validates input to ensure it is not empty.
   - Pushes new task string into the `tasks` array.
   - Saves array as a JSON string: `localStorage.setItem("tasks", JSON.stringify(tasks))`.
   - Records the most recent task into session storage: `sessionStorage.setItem("lastTask", task)`.

3. **Rendering (`displayTasks`)**:
   - Clears existing `<ul>` elements.
   - Loops over `tasks` and dynamically appends `<li>` elements with an inline "Delete" button.

4. **Deleting a Task (`deleteTask(index)`)**:
   - Removes the selected index via `tasks.splice(index, 1)`.
   - Updates `localStorage` and re-renders the list.

5. **Clearing All Tasks (`clearTasks`)**:
   - Resets the `tasks` array to `[]`.
   - Cleans up storage via `localStorage.removeItem("tasks")` and `sessionStorage.removeItem("lastTask")`.

---

## How to Run & Test

1. Open [`index.html`](file:///d:/Desktop/Backend%20Development/Theory/Task-6/lecture7/index.html) in your browser:
   ```bash
   Start-Process "index.html"
   ```
2. Add several tasks and observe them appearing in the list.
3. Open **Browser Developer Tools** (`F12` or `Ctrl + Shift + I`):
   - Navigate to the **Application** (Chrome/Edge) or **Storage** (Firefox) tab.
   - Expand **Local Storage** -> see the `tasks` JSON string update.
   - Expand **Session Storage** -> see `lastTask` value.
4. Close the browser tab and re-open the file: observe that your tasks are still there (persisted by `localStorage`).
