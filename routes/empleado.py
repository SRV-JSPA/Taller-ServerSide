# rutas/empleados.py
from flask import Blueprint, request, jsonify
from models.empleado import Empleado
from utils.db import db

empleados = Blueprint("empleados", __name__)

@empleados.route("/empleados", methods=["GET"])
def get_empleados():
    empleados = Empleado.query.all()
    if not empleados:
        return jsonify({"mensaje": "No se encontraron empleados"}), 404
    empleados_list = [empleado.to_dict() for empleado in empleados]
    return jsonify(empleados_list), 200

@empleados.route("/empleados/<int:id>", methods=["GET"])
def get_empleado(id):
    empleado = Empleado.query.get(id)
    if empleado is None:
        return jsonify({"mensaje": "Empleado no encontrado"}), 404
    return jsonify(empleado.to_dict()), 200

@empleados.route("/empleados", methods=["POST"])
def crear_empleado():
    datos = request.get_json()
    id_persona = datos.get("id_persona")
    id_usuario = datos.get("id_usuario")

    if not id_persona or not id_usuario:
        return jsonify({"mensaje": "id_persona y id_usuario son requeridos"}), 400

    new_empleado = Empleado(id_persona=id_persona, id_usuario=id_usuario)

    db.session.add(new_empleado)
    db.session.commit()

    return jsonify({"mensaje": "Empleado guardado"}), 200

@empleados.route("/empleados/<int:id>", methods=["PUT"])
def actualizar_empleado(id):
    empleado = Empleado.query.get(id)
    if empleado is None:
        return jsonify({"mensaje": "Empleado no encontrado"}), 404

    datos = request.get_json()
    if not datos:
        return jsonify({"mensaje": "No se proporcionaron datos para actualizar"}), 400

    id_persona = datos.get("id_persona")
    id_usuario = datos.get("id_usuario")

    if id_persona:
        empleado.id_persona = id_persona
    if id_usuario:
        empleado.id_usuario = id_usuario

    db.session.commit()

    return jsonify(empleado.to_dict()), 200

@empleados.route("/empleados/<int:id>", methods=["DELETE"])
def eliminar_empleado(id):
    empleado = Empleado.query.get(id)
    if empleado is None:
        return jsonify({"mensaje": "Empleado no encontrado"}), 404

    db.session.delete(empleado)
    db.session.commit()
    return jsonify({"mensaje": "Empleado eliminado"}), 200
