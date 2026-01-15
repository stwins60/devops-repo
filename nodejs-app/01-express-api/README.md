# Express REST API

Node.js REST API using Express framework.

## Features

- Express.js framework
- RESTful endpoints
- Middleware
- Error handling
- CORS support

## Project Structure

```
01-express-api/
├── src/
│   ├── routes/
│   │   └── users.js
│   ├── controllers/
│   │   └── userController.js
│   ├── middleware/
│   │   └── errorHandler.js
│   └── app.js
├── server.js
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
# or development mode
npm run dev
```

## API Endpoints

- GET /api/users
- GET /api/users/:id
- POST /api/users
- PUT /api/users/:id
- DELETE /api/users/:id
