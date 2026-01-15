# Node.js Express REST API Application

A modern REST API built with Express.js, demonstrating best practices for Node.js backend development including routing, middleware, error handling, and testing.

## 📋 Features

- RESTful API endpoints
- Express.js framework
- Middleware for logging, CORS, and error handling
- JSON request/response handling
- Input validation
- Structured error handling
- Unit and integration tests
- Environment-based configuration

## 🏗️ Project Structure

```
nodejs-app/
├── src/
│   ├── controllers/
│   │   └── userController.js    # Request handlers
│   ├── routes/
│   │   └── userRoutes.js        # Route definitions
│   ├── middleware/
│   │   ├── errorHandler.js      # Error handling middleware
│   │   ├── logger.js            # Logging middleware
│   │   └── validator.js         # Input validation
│   ├── models/
│   │   └── userModel.js         # Data models
│   ├── utils/
│   │   └── database.js          # In-memory database
│   └── app.js                   # Express app configuration
├── tests/
│   └── api.test.js              # API tests
├── server.js                    # Application entry point
├── package.json                 # Dependencies and scripts
├── .gitignore
└── README.md
```

## 🚀 Prerequisites

- Node.js 16.x or higher
- npm or yarn

## 📦 Installation

1. **Clone the repository:**
```bash
cd nodejs-app
```

2. **Install dependencies:**
```bash
npm install
```

## ⚙️ Configuration

Create a `.env` file in the root directory:

```env
PORT=3000
NODE_ENV=development
```

## 🏃 Running the Application

**Development mode (with auto-reload):**
```bash
npm run dev
```

**Production mode:**
```bash
npm start
```

The API will be available at `http://localhost:3000`

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
GET /api/users/:id
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
PUT /api/users/:id
Content-Type: application/json

{
  "name": "John Updated",
  "email": "john.updated@example.com"
}
```

**Delete user:**
```
DELETE /api/users/:id
```

## 🧪 Testing

Run tests:
```bash
npm test
```

Run tests with coverage:
```bash
npm run test:coverage
```

Run tests in watch mode:
```bash
npm run test:watch
```

## 📝 Example Usage

```bash
# Health check
curl http://localhost:3000/health

# Get all users
curl http://localhost:3000/api/users

# Create a user
curl -X POST http://localhost:3000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com","age":25}'

# Get specific user
curl http://localhost:3000/api/users/1

# Update user
curl -X PUT http://localhost:3000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice Updated","email":"alice.updated@example.com"}'

# Delete user
curl -X DELETE http://localhost:3000/api/users/1
```

## 📚 Dependencies

### Production
- `express`: Web framework
- `cors`: CORS middleware
- `dotenv`: Environment variable management
- `morgan`: HTTP request logger

### Development
- `nodemon`: Auto-reload during development
- `jest`: Testing framework
- `supertest`: HTTP testing

## 🔧 Development

To add new endpoints:
1. Create controller in `src/controllers/`
2. Define routes in `src/routes/`
3. Register routes in `src/app.js`
4. Add tests in `tests/`

## 📊 Scripts

- `npm start`: Start production server
- `npm run dev`: Start development server with auto-reload
- `npm test`: Run tests
- `npm run test:coverage`: Run tests with coverage report
- `npm run test:watch`: Run tests in watch mode
- `npm run lint`: Run ESLint

## 📄 License

This project is for educational purposes.
