from werkzeug.security import generate_password_hash, check_password_hash

from app.models.user import User
from app import db


class UserController:
    @staticmethod
    def add_user(username, password):
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def authenticate(username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return user
        return None
