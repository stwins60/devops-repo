"""
Utility functions for the application
"""

import re


def validate_email(email):
    """
    Validate email format
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_user_data(data):
    """
    Validate user data for creation/update
    Returns: (is_valid, error_message)
    """
    if not data:
        return False, "No data provided"
    
    # Check required fields for creation
    if 'name' not in data:
        return False, "Name is required"
    
    if 'email' not in data:
        return False, "Email is required"
    
    # Validate name
    if not data['name'] or len(data['name'].strip()) == 0:
        return False, "Name cannot be empty"
    
    if len(data['name']) > 100:
        return False, "Name is too long (max 100 characters)"
    
    # Validate email
    if not validate_email(data['email']):
        return False, "Invalid email format"
    
    # Validate age if provided
    if 'age' in data and data['age'] is not None:
        try:
            age = int(data['age'])
            if age < 0 or age > 150:
                return False, "Age must be between 0 and 150"
        except (ValueError, TypeError):
            return False, "Age must be a valid number"
    
    return True, None


def sanitize_string(text):
    """
    Sanitize string input
    """
    if not text:
        return ""
    return text.strip()


def format_response(success, data=None, message=None, error=None):
    """
    Format API response
    """
    response = {'success': success}
    
    if data is not None:
        response['data'] = data
    
    if message:
        response['message'] = message
    
    if error:
        response['error'] = error
    
    return response
