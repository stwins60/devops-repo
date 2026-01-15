const express = require('express');
const router = express.Router();

const users = [];

router.get('/', (req, res) => {
  res.json(users);
});

router.get('/:id', (req, res) => {
  const user = users.find(u => u.id === req.params.id);
  if (!user) return res.status(404).json({ error: 'User not found' });
  res.json(user);
});

router.post('/', (req, res) => {
  const user = { id: Date.now().toString(), ...req.body };
  users.push(user);
  res.status(201).json(user);
});

module.exports = router;
