from utils.db import db

class Bodega(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_descriptivo=db.Column(db.String(150))

    def __init__(self,nombre_descriptivo):
        self.nombre_descriptivo=nombre_descriptivo

    def to_dict(self):
        return {
            'id':self.id,
            'nombre_descriptivo':self.nombre_descriptivo
        }
