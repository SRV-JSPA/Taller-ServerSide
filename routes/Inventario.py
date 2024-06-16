# rutas/inventarios.py
from flask import Blueprint, request, jsonify
from models.Inventario import Inventario
from utils.db import db

inventarios = Blueprint("inventarios", __name__)

@inventarios.route("/inventarios", methods=["GET"])
def get_inventarios():
    inventarios = Inventario.query.all()
    if not inventarios:
        return jsonify({"mensaje": "No se encontraron inventarios"}), 404
    inventarios_list = [inventario.to_dict() for inventario in inventarios]
    return jsonify(inventarios_list), 200

@inventarios.route("/inventarios/<int:id>", methods=["GET"])
def get_inventario(id):
    inventario = Inventario.query.get(id)
    if inventario is None:
        return jsonify({"mensaje": "Inventario no encontrado"}), 404
    return jsonify(inventario.to_dict()), 200

@inventarios.route("/inventarios", methods=["POST"])
def crear_inventario():
    datos = request.get_json()
    id_carro = datos.get("id_carro")
    codigo_producto = datos.get("codigo_producto")
    categoria = datos.get("categoria")
    fabricante = datos.get("fabricante")
    stock = datos.get("stock")
    dimension = datos.get("dimension")
    precio_unitario = datos.get("precio_unitario")
    estado = datos.get("estado")
    bodega = datos.get("bodega")

    if not (id_carro and codigo_producto and categoria and fabricante and stock and dimension and precio_unitario and estado and bodega):
        return jsonify({"mensaje": "Todos los campos son requeridos"}), 400

    new_inventario = Inventario(id_carro, codigo_producto, categoria, fabricante, stock, dimension, precio_unitario, estado, bodega)

    db.session.add(new_inventario)
    db.session.commit()

    return jsonify({"mensaje": "Inventario guardado"}), 200

@inventarios.route("/inventarios/<int:id>", methods=["PUT"])
def actualizar_inventario(id):
    inventario = Inventario.query.get(id)
    if inventario is None:
        return jsonify({"mensaje": "Inventario no encontrado"}), 404

    datos = request.get_json()
    if not datos:
        return jsonify({"mensaje": "No se proporcionaron datos para actualizar"}), 400

    id_carro = datos.get("id_carro")
    codigo_producto = datos.get("codigo_producto")
    categoria = datos.get("categoria")
    fabricante = datos.get("fabricante")
    stock = datos.get("stock")
    dimension = datos.get("dimension")
    precio_unitario = datos.get("precio_unitario")
    estado = datos.get("estado")
    bodega = datos.get("bodega")

    if id_carro is not None:
        inventario.id_carro = id_carro
    if codigo_producto is not None:
        inventario.codigo_producto = codigo_producto
    if categoria is not None:
        inventario.categoria = categoria
    if fabricante is not None:
        inventario.fabricante = fabricante
    if stock is not None:
        inventario.stock = stock
    if dimension is not None:
        inventario.dimension = dimension
    if precio_unitario is not None:
        inventario.precio_unitario = precio_unitario
    if estado is not None:
        inventario.estado = estado
    if bodega is not None:
        inventario.bodega = bodega

    db.session.commit()

    return jsonify(inventario.to_dict()), 200

@inventarios.route("/inventarios/<int:id>", methods=["DELETE"])
def eliminar_inventario(id):
    inventario = Inventario.query.get(id)
    if inventario is None:
        return jsonify({"mensaje": "Inventario no encontrado"}), 404

    db.session.delete(inventario)
    db.session.commit()
    return jsonify({"mensaje": "Inventario eliminado"}), 200
