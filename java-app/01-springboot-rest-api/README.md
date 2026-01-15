# Spring Boot REST API

RESTful API using Spring Boot framework.

## Features

- Spring Boot 3.x
- REST controllers
- JPA/Hibernate
- Exception handling
- Validation

## Project Structure

```
01-springboot-rest-api/
├── src/
│   ├── main/
│   │   ├── java/com/example/api/
│   │   │   ├── ApiApplication.java
│   │   │   ├── controller/
│   │   │   │   └── UserController.java
│   │   │   ├── model/
│   │   │   │   └── User.java
│   │   │   ├── service/
│   │   │   │   └── UserService.java
│   │   │   └── repository/
│   │   │       └── UserRepository.java
│   │   └── resources/
│   │       └── application.properties
│   └── test/
├── pom.xml
└── README.md
```

## Running

```bash
mvn spring-boot:run
```

## API Endpoints

- GET /api/users
- GET /api/users/{id}
- POST /api/users
- PUT /api/users/{id}
- DELETE /api/users/{id}
