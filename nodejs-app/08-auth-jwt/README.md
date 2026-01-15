# Authentication API with JWT

Authentication service with JWT tokens.

## Features

- User registration
- Login with JWT
- Token refresh
- Password hashing
- Protected routes

## Project Structure

```
08-auth-jwt/
├── src/
│   ├── routes/
│   │   └── auth.js
│   ├── middleware/
│   │   └── auth.js
│   ├── models/
│   │   └── User.js
│   ├── utils/
│   │   └── jwt.js
│   └── server.js
├── package.json
└── README.md
```

## Installation

```bash
npm install
```

## Running

```bash
npm start
```

## Endpoints

- POST /auth/register
- POST /auth/login
- GET /auth/profile (protected)
