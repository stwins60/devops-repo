# WebSocket Server

Real-time WebSocket server using Gorilla WebSocket.

## Features

- WebSocket connections
- Broadcasting
- Client management
- Room/channel support

## Project Structure

```
05-websocket-server/
├── internal/
│   ├── hub/
│   │   └── hub.go
│   ├── client/
│   │   └── client.go
│   └── message/
│       └── message.go
├── main.go
├── go.mod
└── README.md
```

## Running

```bash
go run main.go
```

Connect via: ws://localhost:8080/ws
