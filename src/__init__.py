from flask import Flask
from .config import Config
from .extensions import db, migrate, login_manager
from .models import User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    login_manager.login_view = 'user.sign_in'
    return app

def register_extensions(app):
    # Setup Flask-SQLAlchemy
    db.init_app(app)

    # Setup Flask-Migrate
    migrate.init_app(app, db)

    # Setup Flask-Login
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

def register_blueprints(app):
    from src.home.views import home_blueprint
    app.register_blueprint(home_blueprint)

    from src.user.views import user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')

    from src.dashboard.views import dashboard_blueprint
    app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')