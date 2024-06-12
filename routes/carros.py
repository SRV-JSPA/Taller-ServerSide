from flask import Blueprint, request, jsonify
from models.carro import Carro
from utils.db import db

carros = Blueprint('carros', __name__)

@carros.route('/carros')
def get_carros():
    return 'Lista de carros'

@carros.route('/carros/:id')
def get_carro():
    return 'carro'

@carros.route('/carros', methods=['POST'])
def crear_carro():
    datos = request.get_json()
    
    marca = datos.get('Marca')
    modelo = datos.get('Modelo')
    linea = datos.get('Linea')
    edicion = datos.get('Edicion')
    
    new_carro = Carro(marca, modelo, linea, edicion)
    
    db.session.add(new_carro)
    db.session.commit()
    
    return jsonify({'mensaje': 'Carro guardado'}), 200

@carros.route('/carros/:id')
def actualizar_carro():
    return 'actualizando carro'

@carros.route('/carros/:id')
def eliminar_carro():
    return 'eliminando carro'