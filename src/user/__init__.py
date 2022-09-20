from flask import Blueprint

user_blueprint = Blueprint('user',
                           __name__,
                           template_folder='templates',
                           static_folder='static',
                           static_url_path='/src/user/static'
                           )