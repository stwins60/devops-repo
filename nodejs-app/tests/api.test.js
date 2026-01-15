const request = require('supertest');
const app = require('../src/app');

describe('API Tests', () => {
  describe('GET /health', () => {
    it('should return health status', async () => {
      const res = await request(app).get('/health');
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('status', 'healthy');
    });
  });

  describe('GET /api/users', () => {
    it('should return all users', async () => {
      const res = await request(app).get('/api/users');
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('success', true);
      expect(res.body).toHaveProperty('data');
      expect(Array.isArray(res.body.data)).toBe(true);
    });
  });

  describe('GET /api/users/:id', () => {
    it('should return a user by ID', async () => {
      const res = await request(app).get('/api/users/1');
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('success', true);
      expect(res.body.data).toHaveProperty('id', 1);
    });

    it('should return 404 for non-existent user', async () => {
      const res = await request(app).get('/api/users/9999');
      expect(res.statusCode).toBe(404);
      expect(res.body).toHaveProperty('success', false);
    });

    it('should return 400 for invalid ID', async () => {
      const res = await request(app).get('/api/users/invalid');
      expect(res.statusCode).toBe(400);
      expect(res.body).toHaveProperty('success', false);
    });
  });

  describe('POST /api/users', () => {
    it('should create a new user', async () => {
      const newUser = {
        name: 'Test User',
        email: 'test@example.com',
        age: 28
      };

      const res = await request(app)
        .post('/api/users')
        .send(newUser);

      expect(res.statusCode).toBe(201);
      expect(res.body).toHaveProperty('success', true);
      expect(res.body.data).toHaveProperty('name', 'Test User');
      expect(res.body.data).toHaveProperty('email', 'test@example.com');
    });

    it('should return 400 for missing name', async () => {
      const newUser = {
        email: 'test@example.com',
        age: 28
      };

      const res = await request(app)
        .post('/api/users')
        .send(newUser);

      expect(res.statusCode).toBe(400);
      expect(res.body).toHaveProperty('success', false);
    });

    it('should return 400 for invalid email', async () => {
      const newUser = {
        name: 'Test User',
        email: 'invalid-email',
        age: 28
      };

      const res = await request(app)
        .post('/api/users')
        .send(newUser);

      expect(res.statusCode).toBe(400);
      expect(res.body).toHaveProperty('success', false);
    });
  });

  describe('PUT /api/users/:id', () => {
    it('should update a user', async () => {
      const updateData = {
        name: 'Updated Name',
        email: 'updated@example.com'
      };

      const res = await request(app)
        .put('/api/users/1')
        .send(updateData);

      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('success', true);
      expect(res.body.data).toHaveProperty('name', 'Updated Name');
    });

    it('should return 404 for non-existent user', async () => {
      const updateData = {
        name: 'Updated Name'
      };

      const res = await request(app)
        .put('/api/users/9999')
        .send(updateData);

      expect(res.statusCode).toBe(404);
      expect(res.body).toHaveProperty('success', false);
    });
  });

  describe('DELETE /api/users/:id', () => {
    it('should delete a user', async () => {
      const res = await request(app).delete('/api/users/1');
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('success', true);
    });

    it('should return 404 for non-existent user', async () => {
      const res = await request(app).delete('/api/users/9999');
      expect(res.statusCode).toBe(404);
      expect(res.body).toHaveProperty('success', false);
    });
  });
});
