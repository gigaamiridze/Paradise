from flask import render_template
from . import user_blueprint
from .forms import Signup, Signin

@user_blueprint.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = Signup()
    return render_template('signup.html', form=form)