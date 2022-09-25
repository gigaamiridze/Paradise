from flask import Flask
from .config import Config
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    # Setup Flask-SQLAlchemy
    db.init_app(app)

    # Setup Flask-Migrate
    migrate.init_app(app, db)

def register_blueprints(app):
    from src.home.views import home_blueprint
    app.register_blueprint(home_blueprint)

    from src.user.views import user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')