# Student Management REST API — FastAPI + SQLAlchemy + Pydantic

## Purpose
A production-style **REST API** for managing students, courses, departments, and enrollments. Built with **FastAPI**, **SQLAlchemy ORM**, and **Pydantic** validation, it demonstrates full CRUD operations, pagination, filtering, search, and request validation with proper HTTP status codes.

---

## What This Code Does
This API lets you:
- **Create, Read, Update, Delete (CRUD)** students with validated input
- **Create and list courses** filtered by department or credits
- **Enroll students** in courses and manage those enrollments
- **Search** students by name or email with **pagination** support
- **Filter** students by branch (CSE, ECE, IT, ME, CE) or department
- Automatically **validate** all input using Pydantic schemas (returns HTTP 422 for bad data)
- Use **dependency injection** for database sessions (clean, testable architecture)

---

## Concepts Covered

| Concept | Where It Appears |
|:--------|:-----------------|
| **FastAPI Framework** | `main.py` — route decorators, automatic OpenAPI/Swagger docs |
| **SQLAlchemy ORM** | `models.py` — Python classes mapped to database tables |
| **Pydantic Schemas** | `schemas.py` — request/response validation with type safety |
| **Dependency Injection** | `get_db()` generator yields a database session per request |
| **CRUD Operations** | Full Create, Read, Update, Delete for Students, Courses, Enrollments |
| **Pagination** | `page` and `limit` query params with total count and total pages |
| **Search & Filtering** | `ilike` search on name/email, enum-based branch filtering |
| **HTTP Status Codes** | 200 OK, 201 Created, 204 No Content, 404 Not Found, 409 Conflict, 422 Validation Error |
| **Enum Validation** | `BranchEnum` restricts branch values to CSE, ECE, IT, ME, CE |
| **Email Validation** | Pydantic `EmailStr` validates email format automatically |
| **Relationship Mapping** | `back_populates` for bidirectional ORM relationships |
| **Cascade Deletion** | Deleting a student auto-deletes their enrollment records |
| **Environment Variables** | `.env` file with `DATABASE_URL` loaded via `python-dotenv` |

---

## Prerequisites and Dependencies

- **Python** 3.10+
- **pip packages** (listed in `requirements.txt`):
  - `fastapi` — web framework
  - `uvicorn` — ASGI server
  - `sqlalchemy` — ORM
  - `python-dotenv` — loads `.env` variables
  - `pydantic[email]` — validation with email support

---

## Installation and Run Steps

```bash
# Navigate to the project folder
cd Lab/student_api

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API server
python main.py
```

The API will be available at: `http://127.0.0.1:8000`
Interactive Swagger UI docs: `http://127.0.0.1:8000/docs`

---

## File Structure

```text
student_api/
├── README.md           # This documentation file
├── main.py             # FastAPI application with all route handlers
├── database.py         # SQLAlchemy engine, session factory, and get_db dependency
├── models.py           # SQLAlchemy ORM models (Department, Student, Course, Enrollment)
├── model.py            # (Duplicate of models.py — same content)
├── schemas.py          # Pydantic request/response schemas with validation rules
├── requirements.txt    # Python dependencies
├── requirement.txt     # (Duplicate of requirements.txt)
└── .env                # Environment variable: DATABASE_URL=sqlite:///./students.db
```

---

## Code Walkthrough

### `database.py` — Database Configuration
```python
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./students.db")
engine = create_engine(DATABASE_URL, ...)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```
- Loads the database URL from `.env` (defaults to SQLite)
- `get_db()` is a **dependency injection generator** — FastAPI calls it automatically for every request that needs a database session, and closes the session when the request is done

### `models.py` — ORM Models
Four interconnected models:

| Model | Table | Key Fields | Relationships |
|:------|:------|:-----------|:--------------|
| `Department` | `departments` | `id`, `name`, `created_at` | Has many Students, Courses |
| `Student` | `students` | `id`, `name`, `email`, `branch`, `enrollment_date`, `department_id` | Belongs to Department, has many Enrollments |
| `Course` | `courses` | `id` (string, e.g. "CS101"), `title`, `credits`, `department_id` | Belongs to Department, has many Enrollments |
| `Enrollment` | `enrollments` | `student_id`, `course_id` (composite PK), `semester`, `grade` | Belongs to Student and Course |

### `schemas.py` — Pydantic Validation
```python
class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr                    # validates email format
    branch: BranchEnum                 # must be CSE, ECE, IT, ME, or CE
```
- Separate schemas for Create, Update, and Response (follows FastAPI best practices)
- `StudentUpdate` uses `Optional` fields so you can update only what you need
- `StudentListResponse` includes pagination metadata (`total`, `page`, `total_pages`)

### `main.py` — API Routes

#### Student Endpoints
| Method | Route | Description | Status |
|:-------|:------|:------------|:-------|
| `GET` | `/students` | List students with pagination, search, filters | 200 |
| `GET` | `/students/{id}` | Get single student | 200 / 404 |
| `POST` | `/students` | Create student | 201 / 409 / 422 |
| `PUT` | `/students/{id}` | Update student | 200 / 404 |
| `DELETE` | `/students/{id}` | Delete student (cascades to enrollments) | 204 / 404 |

#### Course Endpoints
| Method | Route | Description | Status |
|:-------|:------|:------------|:-------|
| `GET` | `/courses` | List courses (filter by department, credits) | 200 |
| `POST` | `/courses` | Create course | 201 / 409 |

#### Enrollment Endpoints
| Method | Route | Description | Status |
|:-------|:------|:------------|:-------|
| `GET` | `/students/{id}/enrollments` | List student's enrollments | 200 / 404 |
| `POST` | `/students/{id}/enrollments` | Enroll student in course | 201 / 404 / 409 |
| `DELETE` | `/students/{id}/enrollments/{course_id}` | Drop enrollment | 204 / 404 |

---

## Example Requests and Responses

### Create a Student
```bash
curl -X POST http://127.0.0.1:8000/students \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Kanishka Bhatt",
    "email": "kanishka@upes.ac.in",
    "branch": "CSE",
    "department_id": 1,
    "enrollment_date": "2024-08-01"
  }'
```
**Response (201 Created):**
```json
{
  "id": 1,
  "name": "Kanishka Bhatt",
  "email": "kanishka@upes.ac.in",
  "branch": "CSE",
  "enrollment_date": "2024-08-01",
  "department_id": 1,
  "created_at": "2026-11-24T14:00:00Z",
  "updated_at": null
}
```

### List Students with Search and Pagination
```bash
curl "http://127.0.0.1:8000/students?search=kanishka&page=1&limit=5"
```
**Response (200 OK):**
```json
{
  "data": [{ "id": 1, "name": "Kanishka Bhatt", "email": "kanishka@upes.ac.in", ... }],
  "total": 1,
  "page": 1,
  "limit": 5,
  "total_pages": 1
}
```

### Invalid Request (422 Validation Error)
```bash
curl -X POST http://127.0.0.1:8000/students \
  -H "Content-Type: application/json" \
  -d '{"name": "", "email": "not-an-email", "branch": "INVALID"}'
```
**Response (422 Unprocessable Entity):**
```json
{
  "detail": [
    { "loc": ["body", "name"], "msg": "String should have at least 1 character", "type": "string_too_short" },
    { "loc": ["body", "email"], "msg": "value is not a valid email address", "type": "value_error" },
    { "loc": ["body", "branch"], "msg": "Input should be 'CSE', 'ECE', 'IT', 'ME' or 'CE'", "type": "enum" }
  ]
}
```

---

## Common Errors and Fixes

| Error | Cause | Fix |
|:------|:------|:----|
| `ModuleNotFoundError: No module named 'fastapi'` | Dependencies not installed | Run `pip install -r requirements.txt` |
| `409 Conflict` on student creation | Email already exists in the database | Use a different email address |
| `422 Unprocessable Entity` | Request body fails Pydantic validation | Check field types, required fields, enum values |
| `OperationalError: no such table` | Database tables not created | Tables are auto-created on startup via `Base.metadata.create_all()` |
| `.env` not loading | `python-dotenv` not installed | Run `pip install python-dotenv` |

---

## Key Takeaways

1. **FastAPI + Pydantic** automatically validates every request — invalid data never reaches your database
2. **Dependency injection** (`Depends(get_db)`) keeps database session management clean and testable
3. **Separate schemas** for Create, Update, and Response gives you fine-grained control over what data goes in and out
4. **Pagination** prevents loading thousands of records into memory at once
5. **Cascade deletion** (`ondelete="CASCADE"`) ensures referential integrity — no orphaned enrollment records
6. **Swagger UI** at `/docs` gives you a free interactive API playground for testing
7. This architecture (FastAPI + SQLAlchemy + Pydantic) is production-ready and used in real-world applications
