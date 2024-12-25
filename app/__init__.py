from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import config

load_dotenv()

db=SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])
    #initializing objects
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    #attach blueprints
    from .main import bp
    app.register_blueprint(bp)
    from .admin import admin 
    app.register_blueprint(admin)

    login_manager.login_view='admin.admin_home'
    login_manager.login_message='Please login to get access.'
    login_manager.login_message_category='info'
    return app