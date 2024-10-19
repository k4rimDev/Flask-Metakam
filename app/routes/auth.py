from flask import Blueprint, render_template, redirect, url_for, request, flash

from flask_login import login_user, logout_user, login_required

from app.controllers.user_controller import UserController


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = UserController.authenticate(username, password)
        if user:
            login_user(user)
            return redirect(url_for('admin.index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
