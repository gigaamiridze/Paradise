from flask import Flask

def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app):
    from src.home.views import home_blueprint
    app.register_blueprint(home_blueprint)

    from src.user.views import user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')