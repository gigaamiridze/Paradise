from flask import render_template, redirect, url_for
from flask_login import login_required
from . import dashboard_blueprint
from src.resources import pages, sidebar_menu
from .forms import Music

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
    form = Music()

    if form.validate_on_submit():
        music_img = form.music_img.data
        music_name = form.music_name.data
        music_file = form.music_file.data
        artist = form.artist.data
        composer = form.composer.data
        lyricist = form.lyricist.data
        music_director = form.music_director.data
        category = form.category.data
        lyrics = form.lyrics.data
        free_or_paid = form.free_or_paid.data
        music_price = form.music_price.data

        return redirect(url_for('dashboard.musics'))

    return render_template('add-music.html', pages=pages, sidebar_menu=sidebar_menu, form=form)