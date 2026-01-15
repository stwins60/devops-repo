const User = require('../models/userModel');

class Database {
  constructor() {
    this.users = new Map();
    this.nextId = 1;
    this.seedData();
  }

  seedData() {
    this.createUser('John Doe', 'john@example.com', 30);
    this.createUser('Jane Smith', 'jane@example.com', 25);
    this.createUser('Bob Johnson', 'bob@example.com', 35);
  }

  createUser(name, email, age) {
    const user = new User(this.nextId, name, email, age);
    this.users.set(this.nextId, user);
    this.nextId++;
    return user;
  }

  getUser(id) {
    return this.users.get(id);
  }

  getAllUsers() {
    return Array.from(this.users.values());
  }

  updateUser(id, name, email, age) {
    const user = this.users.get(id);
    if (!user) {
      return null;
    }
    user.update(name, email, age);
    return user;
  }

  deleteUser(id) {
    return this.users.delete(id);
  }

  userExists(id) {
    return this.users.has(id);
  }
}

// Singleton instance
const db = new Database();

module.exports = db;
