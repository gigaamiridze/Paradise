from flask import render_template, redirect, url_for, request
from flask_login import login_user
from . import user_blueprint
from .forms import Signup, Signin
from src.resources import pages
from src.models import User

@user_blueprint.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = Signup()

    if form.validate_on_submit():
        role = form.role.data
        username = form.username.data
        name = form.name.data
        email = form.email.data
        password = form.password.data
        birth_date = form.birth_date.data
        gender = form.gender.data

        user = User(role=role, username=username, name=name, email=email, password=password,
                    birth_date=birth_date, gender=gender)
        user.save_to_db()

        return redirect(url_for('user.sign_in'))

    return render_template('signup.html', form=form, pages=pages)

@user_blueprint.route('/signin', methods=['GET', 'POST'])
def sign_in():
    form = Signin()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.find_by_username(username)

        if user is not None and user.check_password(password):
            login_user(user)

            next = request.args.get('next')

            if next is None:
                next = url_for('dashboard.dash_home')

            return redirect(next)

    return render_template('signin.html', form=form, pages=pages)