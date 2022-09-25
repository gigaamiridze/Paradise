import os

class Config(object):
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    DB_NAME = 'paradise.db'

    SECRET_KEY = 'fagparadisegaf'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(PROJECT_ROOT, DB_NAME)}'