from utils.db import db

class Estados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Estado = db.Column(db.String(100))
    
    def __init__(self, Estado):
        self.Estado = Estado
        
    def to_dict(self):
        return {
            'id': self.id,
            'Estado': self.Estado
        }