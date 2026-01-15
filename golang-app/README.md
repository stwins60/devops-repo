# Golang Web Server Application

A high-performance web server built with Go's standard library and the Gorilla Mux router, demonstrating RESTful API design, middleware, and best practices.

## 📋 Features

- RESTful API endpoints
- HTTP routing with Gorilla Mux
- Middleware for logging and CORS
- JSON request/response handling
- Error handling
- Graceful shutdown
- Unit tests
- Structured logging

## 🏗️ Project Structure

```
golang-app/
├── cmd/
│   └── server/
│       └── main.go         # Application entry point
├── pkg/
│   ├── handlers/
│   │   └── user.go         # HTTP handlers
│   ├── models/
│   │   └── user.go         # Data models
│   └── middleware/
│       └── middleware.go   # HTTP middleware
├── internal/
│   └── database/
│       └── database.go     # In-memory database
├── api/
│   └── routes.go           # Route definitions
├── go.mod                  # Go module file
├── go.sum                  # Go dependencies
├── .gitignore
└── README.md
```

## 🚀 Prerequisites

- Go 1.20 or higher
- Git

## 📦 Installation

1. **Clone the repository:**
```bash
cd golang-app
```

2. **Install dependencies:**
```bash
go mod download
```

3. **Build the application:**
```bash
go build -o bin/server cmd/server/main.go
```

## ⚙️ Configuration

The application uses environment variables for configuration:

- `PORT`: Server port (default: 8080)
- `HOST`: Server host (default: 0.0.0.0)
- `ENV`: Environment (development/production)

## 🏃 Running the Application

**Development mode:**
```bash
go run cmd/server/main.go
```

**Production mode (after building):**
```bash
./bin/server
```

The API will be available at `http://localhost:8080`

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
GET /api/users/{id}
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
PUT /api/users/{id}
Content-Type: application/json

{
  "name": "John Updated",
  "email": "john.updated@example.com"
}
```

**Delete user:**
```
DELETE /api/users/{id}
```

## 🧪 Testing

Run unit tests:
```bash
go test ./...
```

Run tests with coverage:
```bash
go test -cover ./...
```

Run tests with verbose output:
```bash
go test -v ./...
```

Generate coverage report:
```bash
go test -coverprofile=coverage.out ./...
go tool cover -html=coverage.out
```

## 📝 Example Usage

```bash
# Health check
curl http://localhost:8080/health

# Get all users
curl http://localhost:8080/api/users

# Create a user
curl -X POST http://localhost:8080/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com","age":25}'

# Get specific user
curl http://localhost:8080/api/users/1

# Update user
curl -X PUT http://localhost:8080/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice Updated","email":"alice.updated@example.com"}'

# Delete user
curl -X DELETE http://localhost:8080/api/users/1
```

## 📚 Dependencies

- `github.com/gorilla/mux`: HTTP router and URL matcher
- `github.com/gorilla/handlers`: HTTP middleware

## 🔧 Development

To add new endpoints:
1. Define the handler in `pkg/handlers/`
2. Add the route in `api/routes.go`
3. Update tests

## 🚀 Performance

This application is built with Go's excellent concurrency model and can handle thousands of concurrent requests efficiently.

## 📄 License

This project is for educational purposes.
