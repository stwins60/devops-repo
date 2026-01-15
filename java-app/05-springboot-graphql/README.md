# Spring Boot GraphQL

GraphQL API with Spring Boot.

## Features

- GraphQL schema
- Queries and mutations
- DataLoader
- GraphiQL interface

## Project Structure

```
05-springboot-graphql/
├── src/
│   ├── main/
│   │   ├── java/com/example/graphql/
│   │   │   ├── GraphqlApplication.java
│   │   │   ├── resolver/
│   │   │   └── model/
│   │   └── resources/
│   │       └── graphql/
│   │           └── schema.graphqls
│   └── test/
├── pom.xml
└── README.md
```

## Running

```bash
mvn spring-boot:run
```

Access GraphiQL: http://localhost:8080/graphiql
