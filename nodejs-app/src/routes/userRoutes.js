const express = require('express');
const router = express.Router();
const userController = require('../controllers/userController');
const { validateUserInput } = require('../middleware/validator');

// User routes
router.get('/users', userController.getAllUsers);
router.get('/users/:id', userController.getUserById);
router.post('/users', validateUserInput, userController.createUser);
router.put('/users/:id', validateUserInput, userController.updateUser);
router.delete('/users/:id', userController.deleteUser);

module.exports = router;
