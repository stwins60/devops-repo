const express = require("express");
const cors = require("cors");
const morgan = require("morgan");

const userRoutes = require("./routes/users");
const fakeRoutes = require("./routes/fake");

const app = express();

// ✅ Prevent 304 caching
app.disable("etag");
app.use((req, res, next) => {
  res.set("Cache-Control", "no-store");
  next();
});

app.use(cors());
app.use(morgan("dev"));
app.use(express.json());

// ✅ Root Guide Route
app.get("/", (req, res) => {
  res.json({
    message: "Welcome to Express REST API ✅",
    endpoints: {
      health: "GET /health",
      users: {
        getAll: "GET /api/users",
        getById: "GET /api/users/:id",
        create: "POST /api/users",
      },
      fakeUsers: "GET /api/fake?count=10",
    },
  });
});

// ✅ Routes
app.use("/api/users", userRoutes);
app.use("/api/fake", fakeRoutes);

// ✅ Health Check
app.get("/health", (req, res) => {
  res.json({ status: "healthy" });
});

module.exports = app;
