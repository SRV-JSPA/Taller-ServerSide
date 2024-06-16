from utils.db import db
class Persona(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    dpi=db.Column(db.Integer)
    nombre=db.Column(db.String(200))
    apellido=db.Column(db.String(200))
    edad=db.Column(db.Integer)
    nit=db.Column(db.String(100))

    def __init__(self,dpi,nombre,apellido,edad,nit):
        self.dpi=dpi
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.nit=nit

    def to_dict(self):
        return {
            'id':self.id,
            'dpi':self.dpi,
            'nombre':self.nombre,
            'apellido':self.apellido,
            'edad':self.edad,
            'nit':self.nit
        }
    
