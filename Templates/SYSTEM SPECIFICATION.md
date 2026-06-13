# SYSTEM SPECIFICATION: [Project Name]

## 1. EXECUTIVE SUMMARY & TARGET STATE
* **Context**: [1-2 sentences on what this system solves]
* **Core Objective**: [Primary business/technical goal]
* **Agent Operational Rule**: Do not write code outside the boundaries defined in this document. Prioritize type safety and test coverage.

---

## 2. SYSTEM ARCHITECTURE & SCOPE
* **Stack**: [e.g., Next.js, FastAPI, PostgreSQL, TypeScript]
* **Deployment**: [e.g., Docker, AWS ECS, Vercel]
* **Security Requirements**: [e.g., JWT Auth, Role-Based Access Control (RBAC)]

---

## 3. DATA ARCHITECTURE & API SCHEMA
AI Agent: Implement the exact schemas below. Use strict runtime validation (e.g., Zod, Pydantic) matching this model structural logic.

### 3.1 Primary Entity Schema
```json
{
  "\$schema": "https://json-schema.org",
  "title": "PrimaryEntity",
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "name": { "type": "string", "maxLength": 100 },
    "status": { "type": "string", "enum": ["active", "inactive", "pending"] },
    "createdAt": { "type": "string", "format": "date-time" }
  },
  "required": ["id", "name", "status"]
}
```

### 3.2 Endpoint Registry

| Method | Path | Payload | Response Code | Description |
| :--- | :--- | :--- | :--- | :--- |
| `POST` | `/api/v1/resource` | `PrimaryEntity` | `201 Created` | Creates a new entity |
| `GET` | `/api/v1/resource/:id` | None | `200 OK` | Fetches an entity by UUID |

---

## 4. FUNCTIONAL CAPABILITIES (ACCEPTANCE CRITERIA)
AI Agent: Use these exact Gherkin scenarios to auto-generate functional unit and integration tests.

### Feature: [Core Feature Name]

  Scenario: Successful Execution of Core Feature
    Given the database is initialized and empty
    When an authenticated user sends a valid payload to the system
    Then the system should save the entry with a status of "active"
    And the system should return a 201 HTTP status code

  Scenario: Validation Failure Handling
    Given an authenticated user session
    When the user sends a payload missing the "name" parameter
    Then the system must reject the transaction without writing to the database
    And return a 400 Bad Request error containing a validation array

---

## 5. REFACTORING & EXTENSION GUIDELINES
* **Style Guide**: Follow strict linting rules. Use clean architecture patterns (separation of routes, controllers, and services).
* **Dependencies**: Minimize external packages. Only add dependencies explicitly approved in the architecture block.
* **Error Handling**: Every module must catch runtime exceptions, log them securely, and return user-friendly, non-leaking errors.
