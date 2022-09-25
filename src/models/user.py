from src.extensions import db
from src.models import Base

class User(Base):

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
        self.password_hash = password
        self.birth_date = birth_date
        self.gender = gender

    def __repr__(self):
        return f"User: {self.username}"