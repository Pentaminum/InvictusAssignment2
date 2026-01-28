# Backend Design (FastAPI)

## Overview
The backend is a FastAPI service that:
1) returns stored company profile data, and  
2) validates user-selected inputs (company + period) and generates a normalized output payload.

## API Endpoints
- `GET /api/companies`  
  Returns all company profiles (seeded into SQLite).

- `POST /api/output/generate`  
  Accepts `{ company_id, period }` and returns the selected company profile plus computed reporting fields
  (e.g., report type, quarter, reporting period end).

## Structure
Routes are intentionally thin and delegate work to a service layer:
- **Routes**: request/response + dependency wiring
- **Services**: business logic (period calculation, formatting, etc.)
- **Repository**: database access via SQLAlchemy

This keeps logic testable and makes it easy to expand endpoints without mixing concerns.

## Validation
Request validation is done with Pydantic schemas (e.g., `Period` enum), so invalid inputs are rejected at the API boundary consistently.

## Exception Handling
Custom application errors are handled centrally via an exception handler.
Right now the only required case is **404 Not Found** (invalid `company_id`), but the same pattern can be extended later for
other error types without changing individual routes.
