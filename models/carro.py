from utils.db import db


class Carro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Marca = db.Column(db.String(100))
    Modelo = db.Column(db.Integer)
    Linea = db.Column(db.String(100))
    Edicion = db.Column(db.String(100))

    def __init__(self, Marca, Modelo, Linea, Edicion):
        self.Marca = Marca
        self.Modelo = Modelo
        self.Linea = Linea
        self.Edicion = Edicion
        
    def to_dict(self):
        return {
            'id': self.id,
            'Marca': self.Marca,
            'Modelo': self.Modelo,
            'Linea': self.Linea,
            'Edicion': self.Edicion,
        }