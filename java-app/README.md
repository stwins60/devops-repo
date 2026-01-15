# Java Spring Boot REST API Application

A RESTful API built with Spring Boot framework, demonstrating modern Java development practices, dependency injection, and REST controller patterns.

## 📋 Features

- RESTful API endpoints
- Spring Boot framework
- Dependency injection
- Exception handling
- JSON serialization/deserialization
- In-memory data storage
- Unit and integration tests
- Lombok for boilerplate reduction

## 🏗️ Project Structure

```
java-app/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── devops/
│   │   │           └── api/
│   │   │               ├── Application.java
│   │   │               ├── controller/
│   │   │               │   └── UserController.java
│   │   │               ├── model/
│   │   │               │   └── User.java
│   │   │               ├── service/
│   │   │               │   └── UserService.java
│   │   │               ├── repository/
│   │   │               │   └── UserRepository.java
│   │   │               └── exception/
│   │   │                   └── ResourceNotFoundException.java
│   │   └── resources/
│   │       └── application.properties
│   └── test/
│       └── java/
│           └── com/
│               └── devops/
│                   └── api/
│                       └── ApplicationTests.java
├── pom.xml
├── .gitignore
└── README.md
```

## 🚀 Prerequisites

- Java 17 or higher
- Maven 3.6 or higher

## 📦 Installation

1. **Clone the repository:**
```bash
cd java-app
```

2. **Build the project:**
```bash
mvn clean install
```

## ⚙️ Configuration

Configuration is in `src/main/resources/application.properties`:

```properties
server.port=8080
spring.application.name=java-rest-api
```

## 🏃 Running the Application

**Using Maven:**
```bash
mvn spring-boot:run
```

**Using JAR:**
```bash
mvn clean package
java -jar target/java-app-1.0.0.jar
```

The API will be available at `http://localhost:8080`

## 📡 API Endpoints

### Health Check
```
GET /health
```
Returns the health status of the API.

### Users

**Get all users:**
```
GET /api/users
```

**Get user by ID:**
```
GET /api/users/{id}
```

**Create new user:**
```
POST /api/users
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 30
}
```

**Update user:**
```
PUT /api/users/{id}
Content-Type: application/json

{
  "name": "John Updated",
  "email": "john.updated@example.com"
}
```

**Delete user:**
```
DELETE /api/users/{id}
```

## 🧪 Testing

Run tests:
```bash
mvn test
```

Run tests with coverage:
```bash
mvn test jacoco:report
```

## 📝 Example Usage

```bash
# Health check
curl http://localhost:8080/health

# Get all users
curl http://localhost:8080/api/users

# Create a user
curl -X POST http://localhost:8080/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com","age":25}'

# Get specific user
curl http://localhost:8080/api/users/1

# Update user
curl -X PUT http://localhost:8080/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice Updated","email":"alice.updated@example.com"}'

# Delete user
curl -X DELETE http://localhost:8080/api/users/1
```

## 🐳 Docker Support

Build Docker image:
```bash
docker build -t java-spring-boot-api .
```

Run container:
```bash
docker run -p 8080:8080 java-spring-boot-api
```

## 📚 Dependencies

- Spring Boot Starter Web
- Spring Boot Starter Test
- Lombok
- JUnit 5

## 🔧 Development

To add new endpoints:
1. Create model in `model/` package
2. Create service in `service/` package
3. Create controller in `controller/` package
4. Add tests in `test/` directory

## 📄 License

This project is for educational purposes.
