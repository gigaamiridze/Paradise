from src.extensions import db
from src.models import Base
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(Base, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(25), nullable=False, unique=True, index=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.String, nullable=False)
    gender = db.Column(db.String(10), nullable=False)

    def __init__(self, role, username, name, email, password, birth_date, gender):
        self.role = role
        self.username = username
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.birth_date = birth_date
        self.gender = gender

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def find_by_username(cls, temp_username):
        username = cls.query.filter_by(username=temp_username).first()
        if username:
            return username

    @classmethod
    def find_by_email(cls, temp_email):
        email = cls.query.filter_by(email=temp_email).first()
        if email:
            return email

    def __repr__(self):
        return f"User: {self.username}"