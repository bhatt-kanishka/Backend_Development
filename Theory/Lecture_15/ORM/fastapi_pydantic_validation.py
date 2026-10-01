"""
Lecture 15 - Section 5.1: Data Model Validation with Pydantic & FastAPI
Implements request validation, schema constraints, and response models.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import date

app = FastAPI(
    title="Lecture 15: Student Management API with Pydantic Validation",
    description="Demonstrates strict request validation, data integrity, and response modeling using Pydantic.",
    version="1.0.0"
)

# In-memory database storage for demo purposes
db_students = []

# ------------------------------------------------------------------------------
# 1. Pydantic Model for Incoming Student Data (Request Validation)
# ------------------------------------------------------------------------------
class StudentCreate(BaseModel):
    # Required string: min_length=1 prevents empty strings, max_length=100 restricts length
    name: str = Field(..., min_length=1, max_length=100, description="Full name of student")

    # EmailStr validates that the value is an RFC compliant email address
    email: EmailStr = Field(..., description="Valid institutional or personal email")

    # Regex pattern restricts branch to allowed enum values
    # Valid: CSE, ECE, IT, ME, CE (case-sensitive)
    branch: str = Field(
        ...,
        pattern=r"^(CSE|ECE|IT|ME|CE)$",
        description="Engineering branch: CSE, ECE, IT, ME, or CE"
    )

    # Optional field: if omitted, defaults to None (handled by server default)
    enrollment_date: Optional[date] = Field(default=None, description="Date of enrollment (YYYY-MM-DD)")

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Rahul Sharma",
                "email": "rahul@example.com",
                "branch": "CSE",
                "enrollment_date": "2026-09-29"
            }
        }
    }


# ------------------------------------------------------------------------------
# 2. Pydantic Model for API Response
# ------------------------------------------------------------------------------
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    branch: str
    enrollment_date: date


# ------------------------------------------------------------------------------
# 3. Example Database Model (In-Memory or ORM)
# ------------------------------------------------------------------------------
class StudentRecord:
    _id_counter = 0

    def __init__(self, name: str, email: str, branch: str, enrollment_date: Optional[date] = None):
        StudentRecord._id_counter += 1
        self.id = StudentRecord._id_counter
        self.name = name
        self.email = email
        self.branch = branch
        self.enrollment_date = enrollment_date or date.today()


# ------------------------------------------------------------------------------
# 4. API Endpoints
# ------------------------------------------------------------------------------
@app.get("/")
def root():
    return {
        "message": "Lecture 15: FastAPI Data Validation API is running.",
        "docs_url": "/docs",
        "endpoints": ["POST /students", "GET /students"]
    }


@app.post("/students", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate):
    """
    FastAPI automatically validates the request body against StudentCreate before
    this function executes. If validation fails, FastAPI automatically responds
    with HTTP 422 Unprocessable Entity.
    """
    # Check for email uniqueness among in-memory records
    for existing in db_students:
        if existing.email == student.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Email '{student.email}' is already registered."
            )

    student_data = student.model_dump()
    db_student = StudentRecord(**student_data)
    db_students.append(db_student)
    return db_student


@app.get("/students", response_model=List[StudentResponse])
def get_students():
    """Retrieve all registered students"""
    return db_students


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("fastapi_pydantic_validation:app", host="127.0.0.1", port=8000, reload=True)
