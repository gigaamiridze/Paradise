from flask import render_template
from flask_login import login_required
from . import dashboard_blueprint
from src.resources import pages

@dashboard_blueprint.route('/home')
@login_required
def dash_home():
    return render_template('home.html', pages=pages)