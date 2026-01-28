# Frontend Design (React)

## Overview
The frontend is a lightweight React application that:
1) guide the user through valid selections,
2) submit inputs to the API,
3) display validated output clearly, and
4) surface backend errors without duplicating business logic.

## Userflow
1) On load, the app fetches available companies from ```GET /api/companies```
2) The user selects:
- a company
- a reporting period (Q1, Q2, Q3, Annual)
3) Clicking Generate output submits the selection to ```POST /api/output/generate```
4_ If successful:
- the normalized output JSON is rendered in an Output Preview
- the user can download the JSON file
5) If an error occurs, the backend error message is displayed consistently in the UI

## Structure
- **API layer**: type-safe API client + centralizes error handling + endpoint specific modules 
- **Components**: ErrorBanner + OutputPreview
- **Application State**: handles initial data loading + selection state + loading and error states

This keeps logic testable and makes it easy to expand endpoints without mixing concerns.

## Validation
Request validation is done with Pydantic schemas (e.g., `Period` enum), so invalid inputs are rejected at the API boundary consistently.

## Exception Handling
Custom application errors are handled centrally via an exception handler.
Right now the only required case is **404 Not Found** (invalid `company_id`), but the same pattern can be extended later for
other error types without changing individual routes.
