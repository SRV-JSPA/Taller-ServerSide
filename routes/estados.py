from flask import Blueprint, request, jsonify
from models.estados import Estados
from utils.db import db

estados = Blueprint("estados", __name__)


@estados.route("/estados", methods=["GET"])
def get_estados():
    estados = Estados.query.all()
    if not estados:
        return jsonify({"mensaje": "No se encontraron estados"}), 404
    estados_list = [estado.to_dict() for estado in estados]
    return jsonify(estados_list), 200


@estados.route("/estados/<int:id>", methods=["GET"])
def get_estado(id):
    estado = Estados.query.get(id)
    if estado is None:
        return jsonify({"mensaje": "Estado no encontrado"}), 404
    return jsonify([estado.to_dict()]), 200


@estados.route("/estados", methods=["POST"])
def crear_estado():
    datos = request.get_json()

    estado = datos.get("Estado")

    new_estado = Estados(estado)

    db.session.add(new_estado)
    db.session.commit()

    return jsonify({"mensaje": "Estado guardado"}), 200


@estados.route("/estados/<int:id>", methods=["PUT"])
def actualizar_estado(id):
    estado = Estados.query.get(id)
    if estado is None:
        return jsonify({"mensaje": "Estado no encontrado"}), 404

    datos = request.get_json()
    if not datos:
        return jsonify({"mensaje": "No se proporcionaron datos para actualizar"}), 400

    estado_info = datos.get("Estado")

    if estado_info:
        estado.Estado = estado_info

    db.session.commit()

    return jsonify(estado.to_dict()), 200


@estados.route("/estados/<int:id>", methods=["DELETE"])
def eliminar_estado(id):
    estado = Estados.query.get(id)
    db.session.delete(estado)
    db.session.commit()
    return jsonify({"mensaje": "Estado eliminado"}), 200
