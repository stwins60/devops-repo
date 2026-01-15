# HTTP REST API Server

Go REST API server using Gorilla Mux router.

## Features

- RESTful endpoints
- JSON handling
- Middleware support
- CORS enabled
- Structured logging

## Project Structure

```
01-rest-api-server/
├── cmd/
│   └── main.go
├── internal/
│   ├── handlers/
│   │   └── user.go
│   ├── models/
│   │   └── user.go
│   └── middleware/
│       └── logger.go
├── go.mod
└── README.md
```

## Installation

```bash
go mod download
```

## Running

```bash
go run cmd/main.go
```

## API Endpoints

- GET /api/users - List users
- GET /api/users/{id} - Get user
- POST /api/users - Create user
- PUT /api/users/{id} - Update user
- DELETE /api/users/{id} - Delete user
