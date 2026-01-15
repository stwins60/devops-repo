# Microservice with Gin

Microservice built using Gin web framework.

## Features

- Gin HTTP router
- JSON binding
- Middleware
- Error handling
- Health checks

## Project Structure

```
04-microservice-gin/
├── api/
│   ├── handlers/
│   │   └── user.go
│   └── routes.go
├── models/
│   └── user.go
├── middleware/
│   └── auth.go
├── main.go
├── go.mod
└── README.md
```

## Running

```bash
go run main.go
```

Access at: http://localhost:8080
