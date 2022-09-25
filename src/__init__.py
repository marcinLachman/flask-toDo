from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from src.config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    
    login_manager.login_view = 'users.login'


    from src.main.routes import main
    from src.tasks.routes import tasks
    from src.users.routes import users
    from src.errors.routes import errors

    app.register_blueprint(main)
    app.register_blueprint(tasks)
    app.register_blueprint(users)
    app.register_blueprint(errors)

    return app