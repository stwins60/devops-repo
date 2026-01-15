# CLI Tool with Typer

Command-line interface application using Typer and Click.

## Features

- CLI commands and subcommands
- Argument parsing
- Interactive prompts
- Colored output
- Progress bars

## Project Structure

```
07-cli-tool/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── config.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
pip install -e .
```

## Usage

```bash
# Show help
python src/main.py --help

# Run commands
python src/main.py user list
python src/main.py user add --name "John" --email "john@example.com"
python src/main.py config show
```
