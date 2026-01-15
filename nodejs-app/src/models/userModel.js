class User {
  constructor(id, name, email, age = null) {
    this.id = id;
    this.name = name;
    this.email = email;
    this.age = age;
    this.createdAt = new Date();
    this.updatedAt = new Date();
  }

  update(name, email, age) {
    if (name) this.name = name;
    if (email) this.email = email;
    if (age !== undefined) this.age = age;
    this.updatedAt = new Date();
  }

  toJSON() {
    return {
      id: this.id,
      name: this.name,
      email: this.email,
      age: this.age,
      createdAt: this.createdAt,
      updatedAt: this.updatedAt
    };
  }
}

module.exports = User;
