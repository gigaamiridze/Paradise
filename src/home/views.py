from flask import render_template
from . import home_blueprint

@home_blueprint.route('/')
def home_page():
    return render_template('index.html')