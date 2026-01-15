# Python Flask REST API Application

A RESTful API built with Flask framework demonstrating CRUD operations, error handling, and API best practices.

## 📋 Features

- RESTful API endpoints
- CRUD operations for user management
- JSON request/response handling
- Error handling and validation
- Configuration management
- Logging
- Unit tests

## 🏗️ Project Structure

```
python-app/
├── src/
│   ├── __init__.py
│   ├── app.py              # Main application file
│   ├── models.py           # Data models
│   ├── routes.py           # API routes
│   └── utils.py            # Utility functions
├── tests/
│   ├── __init__.py
│   └── test_api.py         # Unit tests
├── config/
│   ├── __init__.py
│   └── config.py           # Configuration settings
├── requirements.txt        # Python dependencies
├── .gitignore
└── README.md
```

## 🚀 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 📦 Installation

1. **Clone the repository:**
```bash
cd python-app
```

2. **Create a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

The application uses environment-based configuration. You can modify settings in `config/config.py`.

Default configuration:
- Host: `0.0.0.0`
- Port: `5000`
- Debug: `True` (development)

## 🏃 Running the Application

**Development mode:**
```bash
python src/app.py
```

**Production mode:**
```bash
export FLASK_ENV=production
gunicorn -w 4 -b 0.0.0.0:5000 src.app:app
```

The API will be available at `http://localhost:5000`

## 📡 API Endpoints

### Health Check
```
GET /health
```
Returns the health status of the API.

### Users

**Get all users:**
```
GET /api/users
```

**Get user by ID:**
```
GET /api/users/<id>
```

**Create new user:**
```
POST /api/users
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 30
}
```

**Update user:**
```
PUT /api/users/<id>
Content-Type: application/json

{
  "name": "John Updated",
  "email": "john.updated@example.com"
}
```

**Delete user:**
```
DELETE /api/users/<id>
```

## 🧪 Testing

Run unit tests:
```bash
python -m pytest tests/
```

Run with coverage:
```bash
python -m pytest --cov=src tests/
```

## 📝 Example Usage

```bash
# Health check
curl http://localhost:5000/health

# Get all users
curl http://localhost:5000/api/users

# Create a user
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com","age":25}'

# Get specific user
curl http://localhost:5000/api/users/1

# Update user
curl -X PUT http://localhost:5000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice Updated","email":"alice.updated@example.com"}'

# Delete user
curl -X DELETE http://localhost:5000/api/users/1
```

## 📚 Dependencies

- Flask: Web framework
- Flask-CORS: Cross-Origin Resource Sharing
- pytest: Testing framework
- gunicorn: WSGI HTTP Server

## 🔧 Development

To add new endpoints:
1. Define the route in `src/routes.py`
2. Add business logic in appropriate modules
3. Update tests in `tests/`

## 📄 License

This project is for educational purposes.
