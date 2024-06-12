from flask import Blueprint

carros = Blueprint('carros', __name__)

@carros.route('/carros')
def get_carros():
    return 'Lista de carros'

@carros.route('/carros/:id')
def get_carro():
    return 'carro'

@carros.route('/carros')
def crear_carro():
    return 'guardando carro'

@carros.route('/carros/:id')
def actualizar_carro():
    return 'actualizando carro'

@carros.route('/carros/:id')
def eliminar_carro():
    return 'eliminando carro'