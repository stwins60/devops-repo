# GraphQL Server

GraphQL API using gqlgen.

## Features

- GraphQL schema
- Queries and mutations
- Resolvers
- DataLoader
- GraphQL playground

## Project Structure

```
08-graphql-server/
├── graph/
│   ├── schema.graphqls
│   ├── resolver.go
│   └── generated/
├── server.go
├── go.mod
└── README.md
```

## Generate Code

```bash
go run github.com/99designs/gqlgen generate
```

## Running

```bash
go run server.go
```

Access playground: http://localhost:8080/
