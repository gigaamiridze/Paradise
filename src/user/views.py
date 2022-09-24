from flask import render_template
from . import user_blueprint
from .forms import Signup, Signin
from src.resources import pages

@user_blueprint.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = Signup()
    return render_template('signup.html', form=form, pages=pages)

@user_blueprint.route('/signin', methods=['GET', 'POST'])
def sign_in():
    form = Signin()
    return render_template('signin.html', form=form, pages=pages)