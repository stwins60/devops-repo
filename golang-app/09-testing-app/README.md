# Testing Application

Comprehensive testing examples with table-driven tests.

## Features

- Unit tests
- Table-driven tests
- Benchmarks
- Mock testing
- Test coverage

## Project Structure

```
09-testing-app/
├── pkg/
│   ├── calculator/
│   │   ├── calculator.go
│   │   └── calculator_test.go
│   └── utils/
│       ├── string.go
│       └── string_test.go
├── go.mod
└── README.md
```

## Running Tests

```bash
# Run all tests
go test ./...

# With coverage
go test -cover ./...

# Verbose
go test -v ./...

# Benchmarks
go test -bench=. ./...
```
