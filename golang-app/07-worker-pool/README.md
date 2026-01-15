# Worker Pool Pattern

Concurrent worker pool for background job processing.

## Features

- Worker pool implementation
- Job queue
- Concurrent processing
- Graceful shutdown

## Project Structure

```
07-worker-pool/
├── internal/
│   ├── worker/
│   │   └── worker.go
│   ├── job/
│   │   └── job.go
│   └── pool/
│       └── pool.go
├── main.go
├── go.mod
└── README.md
```

## Running

```bash
go run main.go
```
