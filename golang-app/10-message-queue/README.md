# Message Queue Consumer

Kafka/RabbitMQ consumer application.

## Features

- Message consumption
- Error handling
- Retry logic
- Dead letter queue
- Graceful shutdown

## Project Structure

```
10-message-queue/
├── internal/
│   ├── consumer/
│   │   └── consumer.go
│   ├── handler/
│   │   └── handler.go
│   └── config/
│       └── config.go
├── main.go
├── go.mod
└── README.md
```

## Running

```bash
go run main.go
```
