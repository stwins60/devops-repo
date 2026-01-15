# API Application with GraphQL

GraphQL API using Graphene and Flask/FastAPI.

## Features

- GraphQL schema definition
- Queries and mutations
- GraphQL playground
- DataLoader for N+1 optimization
- Authentication

## Project Structure

```
10-graphql-api/
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── schema.py
│   ├── resolvers.py
│   └── models.py
├── tests/
│   ├── __init__.py
│   └── test_schema.py
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Running

```bash
python src/app.py
```

## GraphQL Playground

Access the GraphQL playground at: http://localhost:5000/graphql

## Example Queries

```graphql
query {
  users {
    id
    name
    email
  }
}

mutation {
  createUser(name: "John", email: "john@example.com") {
    user {
      id
      name
      email
    }
  }
}
```
