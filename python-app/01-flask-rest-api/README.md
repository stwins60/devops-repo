# Flask REST API Application

A RESTful API built with Flask for user management with CRUD operations.

## Features

- User CRUD operations
- JSON request/response handling
- Error handling and validation
- SQLite database
- Unit tests

## Project Structure

```
01-flask-rest-api/
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── models.py
│   ├── routes.py
│   └── database.py
├── tests/
│   ├── __init__.py
│   └── test_api.py
├── config/
│   ├── __init__.py
│   └── config.py
├── requirements.txt
└── README.md
```

## Installation

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running

```bash
python src/app.py
```

## API Endpoints

- GET /api/users - List all users
- GET /api/users/:id - Get user by ID
- POST /api/users - Create new user
- PUT /api/users/:id - Update user
- DELETE /api/users/:id - Delete user

## Testing

```bash
pytest tests/
```
