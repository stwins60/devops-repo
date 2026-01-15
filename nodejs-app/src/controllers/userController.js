const db = require('../utils/database');

// Get all users
const getAllUsers = (req, res) => {
  try {
    const users = db.getAllUsers();
    res.status(200).json({
      success: true,
      count: users.length,
      data: users
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
};

// Get user by ID
const getUserById = (req, res) => {
  try {
    const id = parseInt(req.params.id);
    
    if (isNaN(id)) {
      return res.status(400).json({
        success: false,
        error: 'Invalid user ID'
      });
    }

    const user = db.getUser(id);
    
    if (!user) {
      return res.status(404).json({
        success: false,
        error: `User with ID ${id} not found`
      });
    }

    res.status(200).json({
      success: true,
      data: user
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
};

// Create new user
const createUser = (req, res) => {
  try {
    const { name, email, age } = req.body;
    
    const user = db.createUser(name, email, age);
    
    console.log(`Created user: ${user.id}`);
    
    res.status(201).json({
      success: true,
      message: 'User created successfully',
      data: user
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
};

// Update user
const updateUser = (req, res) => {
  try {
    const id = parseInt(req.params.id);
    
    if (isNaN(id)) {
      return res.status(400).json({
        success: false,
        error: 'Invalid user ID'
      });
    }

    if (!db.userExists(id)) {
      return res.status(404).json({
        success: false,
        error: `User with ID ${id} not found`
      });
    }

    const { name, email, age } = req.body;
    const user = db.updateUser(id, name, email, age);
    
    console.log(`Updated user: ${id}`);
    
    res.status(200).json({
      success: true,
      message: 'User updated successfully',
      data: user
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
};

// Delete user
const deleteUser = (req, res) => {
  try {
    const id = parseInt(req.params.id);
    
    if (isNaN(id)) {
      return res.status(400).json({
        success: false,
        error: 'Invalid user ID'
      });
    }

    if (!db.userExists(id)) {
      return res.status(404).json({
        success: false,
        error: `User with ID ${id} not found`
      });
    }

    db.deleteUser(id);
    
    console.log(`Deleted user: ${id}`);
    
    res.status(200).json({
      success: true,
      message: `User ${id} deleted successfully`
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
};

module.exports = {
  getAllUsers,
  getUserById,
  createUser,
  updateUser,
  deleteUser
};
