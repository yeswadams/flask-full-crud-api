# Flask Full CRUD API — Professional Project Overview

## Project Summary

This repository contains a lightweight Flask application that demonstrates a complete CRUD API for managing event resources. It is built to showcase core backend development skills including RESTful routing, JSON request handling, in-memory data modeling, error handling, and automated test coverage.

The API is designed as a clean portfolio project for recruiters and technical evaluators, with an emphasis on practical backend capabilities that are reusable in real-world applications.

## What I Built

- `POST /events` — create a new event with JSON input
- `PATCH /events/<id>` — update an event title by ID
- `DELETE /events/<id>` — remove an event by ID
- `GET /` — base route confirming the server is running

The implementation uses:
- Flask routing and request lifecycle
- `jsonify()` responses for consistent JSON output
- in-memory resource storage with a custom `Event` class
- status codes for success and error cases
- request validation for JSON format and required fields

## Key Skills Demonstrated

- Python backend development with Flask
- RESTful API design and CRUD operations
- JSON request parsing and response formatting
- Error handling using Flask `abort()` and HTTP status codes
- Unit testing API endpoints with `pytest`
- Writing maintainable and recruiter-friendly documentation

## Why This Project Matters

This repository is a strong example of how I approach backend work:

- I build APIs with clear route semantics and resource-oriented design
- I validate input and handle invalid requests gracefully
- I document setup, usage, and testing so others can evaluate the project quickly
- I include tests that demonstrate the API works and responds correctly

## Setup & Run

1. Clone the repository

```bash
git clone https://github.com/<your-username>/flask-full-crud-api.git
cd flask-full-crud-api
```

2. Install dependencies

```bash
pip install flask pytest
```

3. Run the application

```bash
python app.py
```

4. Open `http://localhost:5555` in your browser or call the endpoints with Postman / curl.

## Example API Requests

Create an event

```bash
curl -X POST http://localhost:5555/events \
  -H "Content-Type: application/json" \
  -d '{"title": "Hackathon"}'
```

Update an event title

```bash
curl -X PATCH http://localhost:5555/events/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Hackathon 2025"}'
```

Delete an event

```bash
curl -X DELETE http://localhost:5555/events/2
```

## Automated Tests

This repository includes `pytest` tests covering the API behavior.

Run tests with:

```bash
pytest
```

Covered scenarios:
- creating a new event
- updating an existing event
- handling update requests for missing IDs
- deleting events successfully
- returning `404 Not Found` for invalid deletions

## Project Files

- `app.py` — Flask application and endpoints
- `tests/test_app.py` — automated tests for API routes
- `Pipfile` — dependency management (if using pipenv)
- `README.md` — recruiter-focused project summary

## What Recruiters Should Notice

- real API endpoint implementation in Flask
- well-structured request validation and error messaging
- test coverage to verify actual behavior
- easy setup instructions for reviewers
- strong focus on backend fundamentals and maintainability

## Next Steps for Growth

This lab-style project is intentionally compact, and I can extend it into a production-ready API by adding:
- database persistence with SQLAlchemy or PostgreSQL
- authentication and authorization
- comprehensive request/response schemas
- modular project structure for scalability
- API documentation with Swagger / OpenAPI

---

If you are reviewing this project, the code is intentionally simple and clear to demonstrate the backend fundamentals I can bring to your team.