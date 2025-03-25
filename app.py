from flask import Flask
from routes.contact import contacts
from routes.users import users
from flask_sqlalchemy import SQLAlchemy
from config import database_uri

app = Flask(__name__)

app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(contacts)
app.register_blueprint(users)