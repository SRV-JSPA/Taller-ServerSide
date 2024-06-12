from flask import Flask
from routes.carros import carros
from routes.roles import roles
from routes.estados import estados
from utils.db import db
from config import DATABASE_CONNECTION_URI

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


app.register_blueprint(carros)
app.register_blueprint(roles)
app.register_blueprint(estados)
