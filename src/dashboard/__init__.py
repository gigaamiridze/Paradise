from flask import Blueprint

dashboard_blueprint = Blueprint('dashboard',
                                __name__,
                                template_folder='templates',
                                static_folder='static',
                                static_url_path='/src/dashboard/static'
                                )