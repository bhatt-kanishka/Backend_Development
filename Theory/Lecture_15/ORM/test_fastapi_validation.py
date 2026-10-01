"""
Validation tests for FastAPI & Pydantic.
Verifies HTTP 201 on valid input and HTTP 422 on invalid input.
"""

from fastapi.testclient import TestClient
from fastapi_pydantic_validation import app

client = TestClient(app)

def test_validation():
    # 1. Valid payload test
    valid_payload = {
        "name": "Rahul",
        "email": "rahul@example.com",
        "branch": "CSE",
        "enrollment_date": "2026-09-29"
    }
    response = client.post("/students", json=valid_payload)
    if response.status_code == 201:
        data = response.json()
        print(f"Created student {data['name']} (ID: {data['id']}, Branch: {data['branch']}) successfully.")

    # 2. Invalid payload test
    invalid_payload = {
        "name": "",                 # Empty string
        "email": "invalid-email",   # Bad email
        "branch": "BCA",            # Unsupported branch
        "enrollment_date": "invalid-date"
    }
    response_invalid = client.post("/students", json=invalid_payload)
    if response_invalid.status_code == 422:
        print("Pydantic caught invalid fields and returned 422 Unprocessable Entity successfully:")
        for err in response_invalid.json().get("detail", []):
            field = err["loc"][-1]
            print(f"  - {field}: {err['msg']}")

    # 3. GET all students
    get_res = client.get("/students")
    if get_res.status_code == 200:
        print(f"Fetched all students from database successfully: {len(get_res.json())} record(s) found.")


if __name__ == "__main__":
    test_validation()
