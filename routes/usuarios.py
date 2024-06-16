# rutas/usuarios.py
from flask import Blueprint, request, jsonify
from models.usuarios import Usuarios
from utils.db import db

usuarios = Blueprint("usuarios", __name__)

@usuarios.route("/usuarios", methods=["GET"])
def get_usuarios():
    usuarios = Usuarios.query.all()
    if not usuarios:
        return jsonify({"mensaje": "No se encontraron usuarios"}), 404
    usuarios_list = [usuario.to_dict() for usuario in usuarios]
    return jsonify(usuarios_list), 200

@usuarios.route("/usuarios/<int:id>", methods=["GET"])
def get_usuario(id):
    usuario = Usuarios.query.get(id)
    if usuario is None:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404
    return jsonify(usuario.to_dict()), 200

@usuarios.route("/usuarios", methods=["POST"])
def crear_usuario():
    datos = request.get_json()
    username = datos.get("username")
    password = datos.get("password")
    id_rol = datos.get("id_rol")

    if not (username and password and id_rol):
        return jsonify({"mensaje": "Todos los campos son requeridos"}), 400

    new_usuario = Usuarios(username=username, password=password, id_rol=id_rol)

    db.session.add(new_usuario)
    db.session.commit()

    return jsonify({"mensaje": "Usuario guardado"}), 200

@usuarios.route("/usuarios/<int:id>", methods=["PUT"])
def actualizar_usuario(id):
    usuario = Usuarios.query.get(id)
    if usuario is None:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    datos = request.get_json()
    if not datos:
        return jsonify({"mensaje": "No se proporcionaron datos para actualizar"}), 400

    username = datos.get("username")
    password = datos.get("password")
    id_rol = datos.get("id_rol")

    if username is not None:
        usuario.username = username
    if password is not None:
        usuario.password = password
    if id_rol is not None:
        usuario.id_rol = id_rol

    db.session.commit()

    return jsonify(usuario.to_dict()), 200

@usuarios.route("/usuarios/<int:id>", methods=["DELETE"])
def eliminar_usuario(id):
    usuario = Usuarios.query.get(id)
    if usuario is None:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    db.session.delete(usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario eliminado"}), 200
