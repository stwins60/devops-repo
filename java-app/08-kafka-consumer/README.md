# Kafka Consumer Application

Kafka message consumer with Spring Kafka.

## Features

- Kafka integration
- Message consumption
- Error handling
- Offset management

## Project Structure

```
08-kafka-consumer/
├── src/
│   ├── main/
│   │   ├── java/com/example/kafka/
│   │   │   ├── KafkaApplication.java
│   │   │   ├── consumer/
│   │   │   └── config/
│   │   └── resources/
│   └── test/
├── pom.xml
└── README.md
```

## Running

Requires Kafka server running.

```bash
mvn spring-boot:run
```
