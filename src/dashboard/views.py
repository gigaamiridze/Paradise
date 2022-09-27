from flask import render_template
from flask_login import login_required
from . import dashboard_blueprint
from src.resources import pages, sidebar_menu

@dashboard_blueprint.route('/home')
@login_required
def dash_home():
    return render_template('home.html', pages=pages, sidebar_menu=sidebar_menu)

@dashboard_blueprint.route('/musics')
def musics():
    return render_template('musics.html', pages=pages, sidebar_menu=sidebar_menu)

@dashboard_blueprint.route('/albums')
def albums():
    return render_template('albums.html', pages=pages, sidebar_menu=sidebar_menu)

@dashboard_blueprint.route('/artists')
def artists():
    return render_template('artists.html', pages=pages, sidebar_menu=sidebar_menu)

@dashboard_blueprint.route('/favourites')
def favourites():
    return render_template('favourites.html', pages=pages, sidebar_menu=sidebar_menu)

@dashboard_blueprint.route('/analytics')
def analytics():
    return render_template('analytics.html', pages=pages, sidebar_menu=sidebar_menu)

@dashboard_blueprint.route('/events')
def events():
    return render_template('events.html', pages=pages, sidebar_menu=sidebar_menu)

@dashboard_blueprint.route('/add-music', methods=['GET', 'POST'])
def add_music():
    return render_template('add-music.html', pages=pages, sidebar_menu=sidebar_menu)