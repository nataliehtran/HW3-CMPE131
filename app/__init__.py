from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# Initialize Flask app
myapp_obj = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Configuration
myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
)

# Initialize extensions
db = SQLAlchemy(myapp_obj)
login_manager = LoginManager(myapp_obj)
login_manager.login_view = 'login'  # Redirect to 'login' when @login_required fails

# Import models AFTER db init
from app.models import User, Recipe

# Register user loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Import routes AFTER login manager
from app import routes

# Create tables if they don't exist
with myapp_obj.app_context():
    db.create_all()
