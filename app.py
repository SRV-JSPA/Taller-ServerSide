from flask import Flask
from routes.carros import carros
from routes.roles import roles
from routes.bodega import bodegas
from routes.empleado import empleados
from routes.Inventario import inventarios
from routes.persona import personas
from routes.usuarios import usuarios
from routes.estados import estados
from routes.categoria import categorias
from utils.db import db
from config import DATABASE_CONNECTION_URI
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


app.register_blueprint(carros)
app.register_blueprint(roles)
app.register_blueprint(estados)
app.register_blueprint(categorias)
app.register_blueprint(bodegas)
app.register_blueprint(personas)
app.register_blueprint(usuarios)
app.register_blueprint(empleados)
app.register_blueprint(inventarios)


