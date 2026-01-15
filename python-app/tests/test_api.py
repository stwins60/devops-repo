"""
Unit tests for the Flask API
"""

import pytest
import json
from src.app import create_app
from config.config import TestingConfig


@pytest.fixture
def client():
    """Create test client"""
    app = create_app(TestingConfig)
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        yield client


def test_health_check(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'


def test_get_all_users(client):
    """Test getting all users"""
    response = client.get('/api/users')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True
    assert 'data' in data
    assert isinstance(data['data'], list)


def test_get_user_by_id(client):
    """Test getting user by ID"""
    response = client.get('/api/users/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True
    assert 'data' in data


def test_get_nonexistent_user(client):
    """Test getting non-existent user"""
    response = client.get('/api/users/9999')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['success'] is False


def test_create_user(client):
    """Test creating a new user"""
    new_user = {
        'name': 'Test User',
        'email': 'test@example.com',
        'age': 28
    }
    response = client.post(
        '/api/users',
        data=json.dumps(new_user),
        content_type='application/json'
    )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['success'] is True
    assert data['data']['name'] == 'Test User'


def test_create_user_invalid_email(client):
    """Test creating user with invalid email"""
    new_user = {
        'name': 'Test User',
        'email': 'invalid-email',
        'age': 28
    }
    response = client.post(
        '/api/users',
        data=json.dumps(new_user),
        content_type='application/json'
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] is False


def test_create_user_missing_name(client):
    """Test creating user without name"""
    new_user = {
        'email': 'test@example.com',
        'age': 28
    }
    response = client.post(
        '/api/users',
        data=json.dumps(new_user),
        content_type='application/json'
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] is False


def test_update_user(client):
    """Test updating a user"""
    update_data = {
        'name': 'Updated Name',
        'email': 'updated@example.com'
    }
    response = client.put(
        '/api/users/1',
        data=json.dumps(update_data),
        content_type='application/json'
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True


def test_update_nonexistent_user(client):
    """Test updating non-existent user"""
    update_data = {
        'name': 'Updated Name'
    }
    response = client.put(
        '/api/users/9999',
        data=json.dumps(update_data),
        content_type='application/json'
    )
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['success'] is False


def test_delete_user(client):
    """Test deleting a user"""
    response = client.delete('/api/users/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True


def test_delete_nonexistent_user(client):
    """Test deleting non-existent user"""
    response = client.delete('/api/users/9999')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['success'] is False
