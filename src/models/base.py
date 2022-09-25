from src.extensions import db

class Base(db.Model):
    """
    This Class describes SQLAlchemy DB model with basic CRUD functionality

    methods:
        - Create
        - Read
        - Read All
        - Update
        - Delete
        - Save
    """

    __abstract__ = True

    def create(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def read(cls, param):
        return cls.query.filter_by(param=param).first()

    @classmethod
    def read_all(cls):
        return cls.query.all()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()