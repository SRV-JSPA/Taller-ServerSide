from utils.db import db

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_persona=db.Column(db.Integer,db.ForeignKey('persona.id'))
    id_usuario=db.Column(db.Integer,db.ForeignKey('usuarios.id'))



    persona = db.relationship('Persona', backref='empleado')  # Define la relación
    usuario = db.relationship('Usuarios', backref='empleado')  # Define la relación
