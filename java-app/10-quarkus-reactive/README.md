# Quarkus Reactive Application

Reactive REST API with Quarkus framework.

## Features

- Quarkus framework
- Reactive programming
- Native compilation
- Fast startup time

## Project Structure

```
10-quarkus-reactive/
├── src/
│   ├── main/
│   │   ├── java/com/example/quarkus/
│   │   │   ├── GreetingResource.java
│   │   │   └── GreetingService.java
│   │   └── resources/
│   │       └── application.properties
│   └── test/
├── pom.xml
└── README.md
```

## Running

```bash
mvn quarkus:dev
```

## Native Build

```bash
mvn package -Pnative
```
