# inventario.py
from utils.db import db


class Inventario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_carro = db.Column(db.Integer, db.ForeignKey('carro.id'))
    codigo_producto = db.Column(db.String(100))
    categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    fabricante = db.Column(db.String(100))
    stock = db.Column(db.Integer)
    dimension = db.Column(db.String(100))
    precio_unitario = db.Column(db.Float)
    estado = db.Column(db.Integer, db.ForeignKey('estados.id'))
    bodega = db.Column(db.Integer, db.ForeignKey('bodega.id'))

    # Relaciones
    carro = db.relationship('Carro', backref='inventarios')
    categoria_rel = db.relationship('Categoria', backref='inventarios')
    estado_rel = db.relationship('Estados', backref='inventarios')
    bodega_rel = db.relationship('Bodega', backref='inventarios')
    
    def __init__(self,id_carro,codigo_producto,categoria,fabricante,stock,dimension,precio_unitario,estado,bodega):
        self.id_carro=id_carro
        self.codigo_producto=codigo_producto
        self.categoria=categoria
        self.fabricante=fabricante
        self.stock=stock
        self.dimension=dimension
        self.precio_unitario=precio_unitario
        self.estado=estado
        self.bodega=bodega

    def to_dict(self):
        return{
            'id':self.id,
            'id_carro':self.id_carro,
            'categoria':self.categoria,
            'fabricante':self.fabricante,
            'stock':self.stock,
            'dimension':self.dimension,
            'precio_unitario':self.precio_unitario,
            'estado':self.estado,
            'bodega':self.bodega
        }

