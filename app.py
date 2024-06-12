from flask import Flask
from routes.carros import carros
from routes.roles import roles
from flask_sqlalchemy import SQLAlchemy
from utils.db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:16022004@localhost:5432/taller'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


app.register_blueprint(carros)
app.register_blueprint(roles)