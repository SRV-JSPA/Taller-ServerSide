from flask import Blueprint, request, jsonify
from models.roles import Roles
from utils.db import db

roles = Blueprint("roles", __name__)


@roles.route("/roles", methods=["GET"])
def get_roles():
    roles = Roles.query.all()
    if not roles:
        return jsonify({"mensaje": "No se encontraron roles"}), 404
    roles_list = [rol.to_dict() for rol in roles]
    return jsonify(roles_list), 200


@roles.route("/roles/<int:id>", methods=["GET"])
def get_rol(id):
    rol = Roles.query.get(id)
    if rol is None:
        return jsonify({"mensaje": "Rol no encontrado"}), 404
    return jsonify([rol.to_dict()]), 200


@roles.route("/roles", methods=["POST"])
def crear_rol():
    datos = request.get_json()

    rol = datos.get("Rol")

    new_rol = Roles(rol)

    db.session.add(new_rol)
    db.session.commit()

    return jsonify({"mensaje": "Rol guardado"}), 200


@roles.route("/roles/<int:id>", methods=["PUT"])
def actualizar_rol(id):
    rol = Roles.query.get(id)
    if rol is None:
        return jsonify({"mensaje": "Rol no encontrado"}), 404

    datos = request.get_json()
    if not datos:
        return jsonify({"mensaje": "No se proporcionaron datos para actualizar"}), 400

    rol_info = datos.get("Rol")

    if rol_info:
        rol.Rol = rol_info

    db.session.commit()

    return jsonify(rol.to_dict()), 200


@roles.route("/roles/<int:id>", methods=["DELETE"])
def eliminar_carro(id):
    rol = Roles.query.get(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify({"mensaje": "Rol eliminado"}), 200
