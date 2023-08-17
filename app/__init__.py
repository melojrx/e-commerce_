from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
app.config["SECRET_KEY"] = '73dfabaf6aac21b1f0fcd782'
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager.init_app(app)
login_manager.login_view = "page_login"
#login_manager.login_message = "Para acessar as funcionalidades realize o login."
#login_manager.login_message_category = 'info'

from app import routes




