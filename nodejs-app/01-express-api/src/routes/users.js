const express = require("express");
const router = express.Router();

// ✅ Sample users data (so GET returns something)
const users = [
  { id: "1", name: "John Doe", email: "john@example.com", role: "Admin" },
  { id: "2", name: "Jane Smith", email: "jane@example.com", role: "User" },
  { id: "3", name: "Michael Brown", email: "michael@example.com", role: "User" },
];

// GET /api/users
router.get("/", (req, res) => {
  res.json(users);
});

// GET /api/users/:id
router.get("/:id", (req, res) => {
  const user = users.find((u) => u.id === req.params.id);

  if (!user) {
    return res.status(404).json({ error: "User not found" });
  }

  res.json(user);
});

// POST /api/users
router.post("/", (req, res) => {
  const user = {
    id: Date.now().toString(),
    ...req.body,
  };

  users.push(user);

  res.status(201).json(user);
});

module.exports = router;
