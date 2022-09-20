from flask import render_template
from . import user_blueprint

@user_blueprint.route('/signup')
def sign_up():
    return render_template('signup.html')