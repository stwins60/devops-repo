"""
Data models for the application
"""

from datetime import datetime

class User:
    """User model"""
    
    def __init__(self, id, name, email, age=None):
        self.id = id
        self.name = name
        self.email = email
        self.age = age
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
    
    def to_dict(self):
        """Convert user object to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'age': self.age,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    def update(self, name=None, email=None, age=None):
        """Update user attributes"""
        if name:
            self.name = name
        if email:
            self.email = email
        if age is not None:
            self.age = age
        self.updated_at = datetime.utcnow()
    
    def __repr__(self):
        return f"<User {self.id}: {self.name}>"


# In-memory database (for demonstration purposes)
class UserDatabase:
    """Simple in-memory database for users"""
    
    def __init__(self):
        self.users = {}
        self.next_id = 1
        self._seed_data()
    
    def _seed_data(self):
        """Add some initial data"""
        self.create_user("John Doe", "john@example.com", 30)
        self.create_user("Jane Smith", "jane@example.com", 25)
        self.create_user("Bob Johnson", "bob@example.com", 35)
    
    def create_user(self, name, email, age=None):
        """Create a new user"""
        user = User(self.next_id, name, email, age)
        self.users[self.next_id] = user
        self.next_id += 1
        return user
    
    def get_user(self, user_id):
        """Get user by ID"""
        return self.users.get(user_id)
    
    def get_all_users(self):
        """Get all users"""
        return list(self.users.values())
    
    def update_user(self, user_id, name=None, email=None, age=None):
        """Update user"""
        user = self.users.get(user_id)
        if user:
            user.update(name, email, age)
            return user
        return None
    
    def delete_user(self, user_id):
        """Delete user"""
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
    
    def user_exists(self, user_id):
        """Check if user exists"""
        return user_id in self.users


# Global database instance
db = UserDatabase()
