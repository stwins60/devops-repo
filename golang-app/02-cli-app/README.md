# CLI Application

Command-line tool built with Cobra framework.

## Features

- Subcommands
- Flags and arguments
- Configuration file support
- Interactive prompts

## Project Structure

```
02-cli-app/
├── cmd/
│   ├── root.go
│   ├── user.go
│   └── config.go
├── internal/
│   └── utils/
│       └── helpers.go
├── main.go
├── go.mod
└── README.md
```

## Installation

```bash
go build -o mycli
```

## Usage

```bash
./mycli --help
./mycli user list
./mycli user add --name "John"
./mycli config show
```
