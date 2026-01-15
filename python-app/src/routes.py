"""
API routes for the Flask application
"""

from flask import Blueprint, request, jsonify
from src.models import db
from src.utils import validate_user_data
import logging

logger = logging.getLogger(__name__)

api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/users', methods=['GET'])
def get_users():
    """Get all users"""
    try:
        users = db.get_all_users()
        return jsonify({
            'success': True,
            'count': len(users),
            'data': [user.to_dict() for user in users]
        }), 200
    except Exception as e:
        logger.error(f"Error getting users: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@api_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user by ID"""
    try:
        user = db.get_user(user_id)
        if not user:
            return jsonify({
                'success': False,
                'error': f'User with ID {user_id} not found'
            }), 404
        
        return jsonify({
            'success': True,
            'data': user.to_dict()
        }), 200
    except Exception as e:
        logger.error(f"Error getting user {user_id}: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@api_bp.route('/users', methods=['POST'])
def create_user():
    """Create a new user"""
    try:
        data = request.get_json()
        
        # Validate input data
        is_valid, error_message = validate_user_data(data)
        if not is_valid:
            return jsonify({
                'success': False,
                'error': error_message
            }), 400
        
        # Create user
        user = db.create_user(
            name=data['name'],
            email=data['email'],
            age=data.get('age')
        )
        
        logger.info(f"Created user: {user.id}")
        return jsonify({
            'success': True,
            'message': 'User created successfully',
            'data': user.to_dict()
        }), 201
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@api_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update user"""
    try:
        if not db.user_exists(user_id):
            return jsonify({
                'success': False,
                'error': f'User with ID {user_id} not found'
            }), 404
        
        data = request.get_json()
        
        # Update user
        user = db.update_user(
            user_id,
            name=data.get('name'),
            email=data.get('email'),
            age=data.get('age')
        )
        
        logger.info(f"Updated user: {user_id}")
        return jsonify({
            'success': True,
            'message': 'User updated successfully',
            'data': user.to_dict()
        }), 200
    except Exception as e:
        logger.error(f"Error updating user {user_id}: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@api_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete user"""
    try:
        if not db.user_exists(user_id):
            return jsonify({
                'success': False,
                'error': f'User with ID {user_id} not found'
            }), 404
        
        db.delete_user(user_id)
        
        logger.info(f"Deleted user: {user_id}")
        return jsonify({
            'success': True,
            'message': f'User {user_id} deleted successfully'
        }), 200
    except Exception as e:
        logger.error(f"Error deleting user {user_id}: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500
