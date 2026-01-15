# FastAPI Application

Modern, high-performance FastAPI application with automatic API documentation.

## Features

- FastAPI framework
- Automatic OpenAPI documentation
- Async/await support
- Pydantic data validation
- Type hints
- CORS support

## Project Structure

```
03-fastapi-app/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── users.py
│   └── database.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── requirements.txt
└── README.md
```

## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- OpenAPI JSON: http://localhost:8000/openapi.json

## Testing

```bash
pytest tests/
```
