# JUnit Testing Application

Comprehensive testing with JUnit 5.

## Features

- JUnit 5 tests
- Mockito mocking
- Test coverage
- Integration tests

## Project Structure

```
06-junit-testing/
├── src/
│   ├── main/
│   │   └── java/com/example/testing/
│   │       ├── Calculator.java
│   │       └── UserService.java
│   └── test/
│       └── java/com/example/testing/
│           ├── CalculatorTest.java
│           └── UserServiceTest.java
├── pom.xml
└── README.md
```

## Running Tests

```bash
mvn test
# With coverage
mvn verify
```
