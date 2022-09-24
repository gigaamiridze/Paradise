from flask import render_template
from . import home_blueprint
from src.resources import pages, navbar_menu

@home_blueprint.route('/')
def home_page():
    return render_template('index.html', pages=pages, navbar_menu=navbar_menu)