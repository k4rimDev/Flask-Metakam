from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask import redirect, url_for, request

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from app import db
from app.models.brand import Brand
from app.models.manufacturer import Manufacturer
from app.models.user import User


class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))


admin = Admin(name='Admin Panel', template_mode='bootstrap3')


def setup_admin(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    admin.add_view(AdminView(Brand, db.session))
    admin.add_view(AdminView(Manufacturer, db.session))
    admin.init_app(app)
