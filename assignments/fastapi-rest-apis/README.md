# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple RESTful API using the FastAPI framework, including routing, request/response validation with Pydantic, and basic automated testing.

## 📝 Tasks

### 🛠️ Build a Tasks API

#### Description
Implement a small REST API that allows clients to create, read, update, and delete "tasks". The API should use Pydantic models for input/output validation and offer clear, documented endpoints.

#### Requirements
Completed program should:

- Provide the following endpoints for a `Task` resource:
  - `GET /tasks` — list all tasks
  - `GET /tasks/{id}` — retrieve a specific task
  - `POST /tasks` — create a new task
  - `PUT /tasks/{id}` — update an existing task
  - `DELETE /tasks/{id}` — delete a task
- Use a Pydantic model for request validation and response schemas (e.g., id, title, description, completed)
- Maintain tasks in-memory (a Python list or dict is fine for this assignment)
- Return appropriate HTTP status codes (200/201/404/400 as applicable)
- Include OpenAPI docs available at `/docs` (FastAPI provides this by default)
- Provide clear run instructions in the README

#### Example
```http
POST /tasks
Content-Type: application/json

{"title": "Write tests", "description": "Add tests for API"}

Response 201 Created
{
  "id": 1,
  "title": "Write tests",
  "description": "Add tests for API",
  "completed": false
}
```


### 🛠️ Enhancements (optional)

#### Description
Add optional features to improve the API or developer experience.

#### Requirements
Completed program may:

- Persist data to an SQLite database using `SQLModel` or `SQLAlchemy`
- Add simple authentication (API key or token)
- Add pagination or filtering to `GET /tasks`
- Provide more comprehensive test coverage (e.g., error cases)

---

## 🔧 How to run (local)

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Start the app with Uvicorn:

```bash
uvicorn starter-code:app --reload
```

3. Open `http://127.0.0.1:8000/docs` to explore the API using the interactive docs.

---

## 📎 Starter files

- `starter-code.py` — Minimal FastAPI app with in-memory CRUD for `Task` objects
- `requirements.txt` — package dependencies
- `tests/test_api.py` — basic pytest tests using `httpx`
