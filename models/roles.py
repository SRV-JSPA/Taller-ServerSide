from utils.db import db

class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Rol = db.Column(db.String)
    
    def __init__(self, Rol):
        self.Rol = Rol
        
    def to_dict(self):
        return {
            'id': self.id,
            'Rol': self.Rol
        }