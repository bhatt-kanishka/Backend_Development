"""
Test Client for Lecture 15 FastAPI & Pydantic Validation.
Executes both valid and invalid payloads demonstrating automatic HTTP 422 validation handling.
"""

import json
from fastapi.testclient import TestClient
from fastapi_pydantic_validation import app

client = TestClient(app)

def test_validation():
    print("=" * 70)
    print("LECTURE 15: FASTAPI + PYDANTIC VALIDATION TEST SUITE")
    print("=" * 70)

    # --------------------------------------------------------------------------
    # Test Case 1: Valid Student Creation
    # --------------------------------------------------------------------------
    print("\n[TEST 1] Submitting VALID student payload:")
    valid_payload = {
        "name": "Rahul",
        "email": "rahul@example.com",
        "branch": "CSE",
        "enrollment_date": "2026-09-29"
    }
    print("Request Body:")
    print(json.dumps(valid_payload, indent=2))

    response = client.post("/students", json=valid_payload)
    print(f"\nResponse Status Code: {response.status_code}")
    print("Response JSON:")
    print(json.dumps(response.json(), indent=2))
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    print("[PASS] Successfully created student with 201 Created!")

    # --------------------------------------------------------------------------
    # Test Case 2: Deliberately Invalid Student Data (Testing 422 Validation)
    # --------------------------------------------------------------------------
    print("\n" + "-" * 70)
    print("[TEST 2] Submitting DELIBERATELY INVALID payload to trigger Pydantic validation:")
    invalid_payload = {
        "name": "",                 # Fails min_length=1
        "email": "invalid-email",   # Fails EmailStr
        "branch": "BCA",            # Fails regex pattern ^(CSE|ECE|IT|ME|CE)$
        "enrollment_date": "invalid-date" # Fails date parsing
    }
    print("Request Body:")
    print(json.dumps(invalid_payload, indent=2))

    response_invalid = client.post("/students", json=invalid_payload)
    print(f"\nResponse Status Code: {response_invalid.status_code} (Expected: 422 Unprocessable Entity)")
    print("Pydantic Validation Errors Caught by FastAPI:")
    print(json.dumps(response_invalid.json(), indent=2))

    assert response_invalid.status_code == 422, f"Expected 422, got {response_invalid.status_code}"
    print("\n[PASS] Verified 422 Unprocessable Entity! All invalid fields were rejected:")
    for err in response_invalid.json().get("detail", []):
        field = " -> ".join(str(loc) for loc in err["loc"])
        msg = err["msg"]
        err_type = err["type"]
        print(f"  * Field [{field}]: {msg} (Type: {err_type})")

    # --------------------------------------------------------------------------
    # Test Case 3: Fetching All Registered Students
    # --------------------------------------------------------------------------
    print("\n" + "-" * 70)
    print("[TEST 3] GET /students")
    get_res = client.get("/students")
    print(f"Status Code: {get_res.status_code}")
    print("Registered Students List:")
    print(json.dumps(get_res.json(), indent=2))

    print("\n" + "=" * 70)
    print("ALL PYDANTIC VALIDATION TESTS COMPLETED SUCCESSFULLY!")
    print("=" * 70)


if __name__ == "__main__":
    test_validation()
