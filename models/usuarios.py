from utils.db import db

class Usuarios(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100))
    password=db.Column(db.String(100))
    id_rol=db.Column(db.Integer,db.ForeignKey('roles.id'))
    rol = db.relationship('Roles', backref='usuarios')  # Define la relación

    def __init__(self,username,password,id_rol):
        self.username=username
        self.password=password
        self.id_rol=id_rol

    def to_dict(self):
        return {
            'id': self.id,
            'username':self.username,
            'password':self.password,
            'id_rol':self.id_rol
        }


        