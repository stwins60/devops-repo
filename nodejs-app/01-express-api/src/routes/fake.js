const express = require("express");
const router = express.Router();

// GET /api/fake?count=10
router.get("/", async (req, res) => {
  const { faker } = await import("@faker-js/faker");

  const count = parseInt(req.query.count, 10) || 10;

  const users = Array.from({ length: count }, () => ({
    id: faker.string.uuid(),
    name: faker.person.fullName(),
    email: faker.internet.email(),
    address: faker.location.streetAddress(),
    phone: faker.phone.number(),
    avatar: faker.image.avatar(),
  }));

  res.json({ users });
});

module.exports = router;
