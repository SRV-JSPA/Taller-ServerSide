from flask import Blueprint, request, jsonify
from models.carro import Carro
from utils.db import db

carros = Blueprint("carros", __name__)


@carros.route("/carros", methods=["GET"])
def get_carros():
    carros = Carro.query.all()
    if not carros:
        return jsonify({"mensaje": "No se encontraron carros"}), 404
    carros_list = [carro.to_dict() for carro in carros]
    return jsonify(carros_list), 200


@carros.route("/carros/<int:id>", methods=["GET"])
def get_carro(id):
    carro = Carro.query.get(id)
    if carro is None:
        return jsonify({"mensaje": "Carro no encontrado"}), 404
    return jsonify([carro.to_dict()]), 200


@carros.route("/carros", methods=["POST"])
def crear_carro():
    datos = request.get_json()

    marca = datos.get("Marca")
    modelo = datos.get("Modelo")
    linea = datos.get("Linea")
    edicion = datos.get("Edicion")

    new_carro = Carro(marca, modelo, linea, edicion)

    db.session.add(new_carro)
    db.session.commit()

    return jsonify({"mensaje": "Carro guardado"}), 200


@carros.route("/carros/<int:id>", methods=["PUT"])
def actualizar_carro(id):
    carro = Carro.query.get(id)
    if carro is None:
        return jsonify({"mensaje": "Carro no encontrado"}), 404

    datos = request.get_json()
    if not datos:
        return jsonify({"mensaje": "No se proporcionaron datos para actualizar"}), 400

    marca = datos.get("Marca")
    modelo = datos.get("Modelo")
    linea = datos.get("Linea")
    edicion = datos.get("Edicion")

    if marca:
        carro.Marca = marca
    if modelo:
        carro.Modelo = modelo
    if linea:
        carro.Linea = linea
    if edicion:
        carro.Edicion = edicion

    db.session.commit()

    return jsonify(carro.to_dict()), 200


@carros.route("/carros/<int:id>", methods=["DELETE"])
def eliminar_carro(id):
    carro = Carro.query.get(id)
    db.session.delete(carro)
    db.session.commit()
    return jsonify({"mensaje": "Carro eliminado"}), 200
