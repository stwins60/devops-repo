class User:
    users_db = {}
    id_counter = 1
    
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
    
    @classmethod
    def create(cls, name, email):
        user = cls(cls.id_counter, name, email)
        cls.users_db[cls.id_counter] = user
        cls.id_counter += 1
        return user
    
    @classmethod
    def get_all(cls):
        return list(cls.users_db.values())
    
    @classmethod
    def get_by_id(cls, id):
        return cls.users_db.get(id)
