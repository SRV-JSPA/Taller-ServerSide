from utils.db import db

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Categoria = db.Column(db.String(100))
    
    def __init__(self, Categoria):
        self.Categoria = Categoria
        
    def to_dict(self):
        return {
            'id': self.id,
            'Categoria': self.Categoria
        }