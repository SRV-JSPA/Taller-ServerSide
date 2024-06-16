from flask import Blueprint, request, jsonify
from models.bodega import Bodega
from utils.db import db

bodegas = Blueprint("bodegas", __name__)

@bodegas.route("/bodegas", methods=["GET"])
def get_bodegas():
    bodegas = Bodega.query.all()
    if not bodegas:
        return jsonify({"mensaje": "No se encontraron bodegas"}), 404
    bodegas_list = [bodega.to_dict() for bodega in bodegas]
    return jsonify(bodegas_list), 200

@bodegas.route("/bodegas/<int:id>", methods=["GET"])
def get_bodega(id):
    bodega = Bodega.query.get(id)
    if bodega is None:
        return jsonify({"mensaje": "Bodega no encontrada"}), 404
    return jsonify(bodega.to_dict()), 200

@bodegas.route("/bodegas", methods=["POST"])
def crear_bodega():
    datos = request.get_json()
    nombre_descriptivo = datos.get("nombre_descriptivo")

    if not nombre_descriptivo:
        return jsonify({"mensaje": "El nombre descriptivo es requerido"}), 400

    new_bodega = Bodega(nombre_descriptivo)

    db.session.add(new_bodega)
    db.session.commit()

    return jsonify({"mensaje": "Bodega guardada"}), 200

@bodegas.route("/bodegas/<int:id>", methods=["PUT"])
def actualizar_bodega(id):
    bodega = Bodega.query.get(id)
    if bodega is None:
        return jsonify({"mensaje": "Bodega no encontrada"}), 404

    datos = request.get_json()
    if not datos:
        return jsonify({"mensaje": "No se proporcionaron datos para actualizar"}), 400

    nombre_descriptivo = datos.get("nombre_descriptivo")

    if nombre_descriptivo:
        bodega.nombre_descriptivo = nombre_descriptivo

    db.session.commit()

    return jsonify(bodega.to_dict()), 200

@bodegas.route("/bodegas/<int:id>", methods=["DELETE"])
def eliminar_bodega(id):
    bodega = Bodega.query.get(id)
    if bodega is None:
        return jsonify({"mensaje": "Bodega no encontrada"}), 404

    db.session.delete(bodega)
    db.session.commit()
    return jsonify({"mensaje": "Bodega eliminada"}), 200
