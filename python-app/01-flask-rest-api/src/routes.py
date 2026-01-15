from flask import Blueprint, request, jsonify
from models import User
from datetime import datetime

api_bp = Blueprint('api', __name__)

# In-memory database
users_db = {}
user_id_counter = 1

@api_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify([user.to_dict() for user in users_db.values()])

@api_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users_db.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict())

@api_bp.route('/users', methods=['POST'])
def create_user():
    global user_id_counter
    data = request.get_json()
    
    user = User(
        id=user_id_counter,
        name=data.get('name'),
        email=data.get('email'),
        created_at=datetime.now()
    )
    users_db[user_id_counter] = user
    user_id_counter += 1
    
    return jsonify(user.to_dict()), 201

@api_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = users_db.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.get_json()
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    
    return jsonify(user.to_dict())

@api_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users_db:
        return jsonify({'error': 'User not found'}), 404
    
    del users_db[user_id]
    return '', 204
