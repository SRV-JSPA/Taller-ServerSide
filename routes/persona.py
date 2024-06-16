# rutas/personas.py
from flask import Blueprint, request, jsonify
from models.persona import Persona
from utils.db import db

personas = Blueprint("personas", __name__)

@personas.route("/personas", methods=["GET"])
def get_personas():
    personas = Persona.query.all()
    if not personas:
        return jsonify({"mensaje": "No se encontraron personas"}), 404
    personas_list = [persona.to_dict() for persona in personas]
    return jsonify(personas_list), 200

@personas.route("/personas/<int:id>", methods=["GET"])
def get_persona(id):
    persona = Persona.query.get(id)
    if persona is None:
        return jsonify({"mensaje": "Persona no encontrada"}), 404
    return jsonify(persona.to_dict()), 200

@personas.route("/personas", methods=["POST"])
def crear_persona():
    datos = request.get_json()
    dpi = datos.get("dpi")
    nombre = datos.get("nombre")
    apellido = datos.get("apellido")
    edad = datos.get("edad")
    nit = datos.get("nit")

    if not (dpi and nombre and apellido and edad and nit):
        return jsonify({"mensaje": "Todos los campos son requeridos"}), 400

    new_persona = Persona(dpi, nombre, apellido, edad, nit)

    db.session.add(new_persona)
    db.session.commit()

    return jsonify({"mensaje": "Persona guardada"}), 200

@personas.route("/personas/<int:id>", methods=["PUT"])
def actualizar_persona(id):
    persona = Persona.query.get(id)
    if persona is None:
        return jsonify({"mensaje": "Persona no encontrada"}), 404

    datos = request.get_json()
    if not datos:
        return jsonify({"mensaje": "No se proporcionaron datos para actualizar"}), 400

    dpi = datos.get("dpi")
    nombre = datos.get("nombre")
    apellido = datos.get("apellido")
    edad = datos.get("edad")
    nit = datos.get("nit")

    if dpi is not None:
        persona.dpi = dpi
    if nombre is not None:
        persona.nombre = nombre
    if apellido is not None:
        persona.apellido = apellido
    if edad is not None:
        persona.edad = edad
    if nit is not None:
        persona.nit = nit

    db.session.commit()

    return jsonify(persona.to_dict()), 200

@personas.route("/personas/<int:id>", methods=["DELETE"])
def eliminar_persona(id):
    persona = Persona.query.get(id)
    if persona is None:
        return jsonify({"mensaje": "Persona no encontrada"}), 404

    db.session.delete(persona)
    db.session.commit()
    return jsonify({"mensaje": "Persona eliminada"}), 200
