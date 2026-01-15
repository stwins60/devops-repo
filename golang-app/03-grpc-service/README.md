# gRPC Service

gRPC server and client implementation.

## Features

- Protocol Buffers
- Bidirectional streaming
- Service definitions
- Client/server implementation

## Project Structure

```
03-grpc-service/
├── proto/
│   └── service.proto
├── server/
│   └── main.go
├── client/
│   └── main.go
├── go.mod
└── README.md
```

## Generate Proto

```bash
protoc --go_out=. --go-grpc_out=. proto/*.proto
```

## Running

```bash
# Server
go run server/main.go

# Client
go run client/main.go
```
