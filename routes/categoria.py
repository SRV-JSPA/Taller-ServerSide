from flask import Blueprint, request, jsonify
from models.categoria import Categoria
from utils.db import db

categorias = Blueprint("categorias", __name__)


@categorias.route("/categorias", methods=["GET"])
def get_categorias():
    categorias = Categoria.query.all()
    if not categorias:
        return jsonify({"mensaje": "No se encontraron categorias"}), 404
    categorias_list = [categoria.to_dict() for categoria in categorias]
    return jsonify(categorias_list), 200


@categorias.route("/categorias/<int:id>", methods=["GET"])
def get_categoria(id):
    categoria = Categoria.query.get(id)
    if categoria is None:
        return jsonify({"mensaje": "Categoria no encontrada"}), 404
    return jsonify([categoria.to_dict()]), 200


@categorias.route("/categorias", methods=["POST"])
def crear_categoria():
    datos = request.get_json()

    categoria = datos.get("Categoria")

    new_categoria = Categoria(categoria)

    db.session.add(new_categoria)
    db.session.commit()

    return jsonify({"mensaje": "Categoria guardada"}), 200


@categorias.route("/categorias/<int:id>", methods=["PUT"])
def actualizar_categoria(id):
    categoria = Categoria.query.get(id)
    if categoria is None:
        return jsonify({"mensaje": "Categoria no encontrada"}), 404

    datos = request.get_json()
    if not datos:
        return jsonify({"mensaje": "No se proporcionaron datos para actualizar"}), 400

    categoria_info = datos.get("Categoria")

    if categoria_info:
        categoria.Categoria = categoria_info

    db.session.commit()

    return jsonify(categoria.to_dict()), 200


@categorias.route("/categorias/<int:id>", methods=["DELETE"])
def eliminar_categoria(id):
    categoria = Categoria.query.get(id)
    db.session.delete(categoria)
    db.session.commit()
    return jsonify({"mensaje": "Categoria eliminada"}), 200
