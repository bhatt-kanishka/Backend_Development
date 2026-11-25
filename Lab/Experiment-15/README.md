# Lecture 15 Lab: Django To-Do Application with External API Integration

## Purpose
A full-stack **Django** To-Do application that demonstrates the Django ORM, function-based views, template rendering, URL routing, and consuming an external REST API — all in one project.

---

## What This Code Does
This is a server-side rendered To-Do app built with Django where you can:
- **View** all tasks in a styled list (sorted by newest first)
- **Add** new tasks via a form page
- **Toggle** task completion status (mark as done / undo)
- **Delete** tasks permanently
- **Fetch external data** from the JSONPlaceholder API (`/api/external/<post_id>/`)

Unlike the in-memory ES6 To-Do (Lab 7-8), this app stores tasks in a **SQLite database** using Django's ORM, so tasks persist across server restarts.

---

## Concepts Covered

| Concept | Where It Appears |
|:--------|:-----------------|
| **Django Project Structure** | `todo_project/` (settings, root URLs) vs `todo/` (app logic) |
| **Django ORM & Models** | `Task` model with `CharField`, `BooleanField`, `DateTimeField` |
| **Migrations** | `0001_initial.py` — auto-generated schema migration |
| **Function-Based Views** | `task_list`, `add_task`, `toggle_task`, `delete_task` |
| **Django Templates** | `base.html` (layout), `task_list.html`, `add_task.html`, `navbar.html` (partial) |
| **Template Inheritance** | `{% extends "todo/base.html" %}` and `{% block content %}` |
| **URL Routing** | `path('toggle/<int:task_id>/', ...)` with integer path converters |
| **HTTP Method Restriction** | `@require_POST` decorator on toggle and delete views |
| **External API Consumption** | `utils.py` calls JSONPlaceholder with `requests.get()` and handles timeouts |
| **Error Handling** | Try/except for timeout, invalid JSON, and general request errors |
| **Static Files** | Custom CSS served from `todo/static/todo/css/style.css` |

---

## Prerequisites and Dependencies

- **Python** ≥ 3.14
- **Django** (install via pip)
- **requests** library (for external API calls)
- **uv** build system (defined in `pyproject.toml`, optional — pip works fine)

---

## Installation and Run Steps

```bash
# Navigate to the lab folder
cd "Lab/Experiment-15"

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies
pip install django requests

# Apply database migrations (creates SQLite database)
python manage.py migrate

# Start the development server
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

---

## File Structure

```text
Experiment-15/
├── README.md                           # This documentation file
├── manage.py                           # Django management CLI
├── pyproject.toml                      # Project metadata (Python ≥3.14)
├── db.sqlite3                          # SQLite database (auto-created)
│
├── todo_project/                       # Django project configuration
│   ├── __init__.py
│   ├── settings.py                     # Installed apps, middleware, DB config
│   ├── urls.py                         # Root URL dispatcher (includes todo.urls)
│   ├── wsgi.py                         # WSGI entry point
│   └── asgi.py                         # ASGI entry point
│
├── todo/                               # Django application
│   ├── __init__.py
│   ├── models.py                       # Task model (title, completed, created_at)
│   ├── views.py                        # View functions (CRUD + external API)
│   ├── urls.py                         # App URL patterns
│   ├── admin.py                        # Admin site registration
│   ├── apps.py                         # App configuration
│   ├── utils.py                        # External API helper (JSONPlaceholder)
│   ├── tests.py                        # Test placeholder
│   │
│   ├── templates/
│   │   ├── partials/
│   │   │   └── navbar.html             # Reusable navigation bar
│   │   └── todo/
│   │       ├── base.html               # Base layout (extends pattern)
│   │       ├── task_list.html           # Main task list page
│   │       └── add_task.html           # Add task form page
│   │
│   ├── static/
│   │   └── todo/css/
│   │       └── style.css               # Custom styling
│   │
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py             # Initial Task table migration
│
└── src/lecture_15/
    └── __init__.py                     # Package init (for uv build)
```

---

## Code Walkthrough

### `todo/models.py` — The Data Model
```python
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```
A simple model with three fields. Django automatically adds an `id` primary key. `auto_now_add=True` records the creation timestamp.

### `todo/views.py` — View Functions

| View | Method | What It Does |
|:-----|:-------|:-------------|
| `task_list` | GET | Fetches all tasks ordered by `-created_at`, renders `task_list.html` |
| `add_task` | GET/POST | Shows the form (GET) or creates a new Task (POST), then redirects |
| `toggle_task` | POST only | Flips `task.completed`, saves, redirects to list |
| `delete_task` | POST only | Deletes the task by ID, redirects to list |
| `external_data_view` | GET | Calls JSONPlaceholder API, returns JSON response or error |

### `todo/utils.py` — External API Integration
```python
def get_external_data(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url, timeout=5)
    return {"data": response.json(), "error": None}
```
Demonstrates consuming a third-party REST API with proper error handling for timeouts, invalid JSON, and network failures.

### `todo/urls.py` — URL Patterns
```python
urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('api/external/<int:post_id>/', views.external_data_view, name='external_data'),
]
```

---

## Example Usage

### Adding a Task
1. Navigate to `http://127.0.0.1:8000/add/`
2. Type a task title and submit the form
3. You are redirected to the task list with your new task visible

### Toggling Completion
Click the toggle button next to any task — it marks it as completed (or undoes it).

### Fetching External Data
```bash
curl http://127.0.0.1:8000/api/external/1/
```
**Response:**
```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit..."
}
```

---

## Common Errors and Fixes

| Error | Cause | Fix |
|:------|:------|:----|
| `No such table: todo_task` | Migrations not applied | Run `python manage.py migrate` |
| `ModuleNotFoundError: No module named 'django'` | Django not installed | Run `pip install django` |
| `TemplateDoesNotExist` | Template folder structure wrong | Ensure templates are in `todo/templates/todo/` |
| External API returns 503 | JSONPlaceholder is down or no internet | Check your internet connection; the error is handled gracefully |

---

## Key Takeaways

1. **Django's ORM** lets you define database tables as Python classes — no raw SQL needed
2. **Migrations** automatically track and apply schema changes (`makemigrations` → `migrate`)
3. **Template inheritance** (`{% extends %}` / `{% block %}`) keeps HTML DRY across pages
4. **`@require_POST`** protects state-changing endpoints from accidental GET requests
5. **External API integration** with proper error handling (timeouts, bad JSON, network failures) is essential for real-world apps
6. Django's **MTV pattern** (Model-Template-View) separates concerns: data, presentation, and logic
