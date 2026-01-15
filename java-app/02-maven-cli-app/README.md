# Maven Console Application

Command-line application using Maven.

## Features

- Maven project structure
- Command-line arguments
- File I/O operations
- Configuration management

## Project Structure

```
02-maven-cli-app/
├── src/
│   ├── main/
│   │   ├── java/com/example/cli/
│   │   │   ├── Main.java
│   │   │   ├── CommandHandler.java
│   │   │   └── FileProcessor.java
│   │   └── resources/
│   │       └── config.properties
│   └── test/
├── pom.xml
└── README.md
```

## Build

```bash
mvn clean package
```

## Running

```bash
java -jar target/maven-cli-app-1.0.0.jar --help
```
