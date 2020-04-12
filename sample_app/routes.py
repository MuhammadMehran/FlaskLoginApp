"""Logged-in page routes."""
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from flask import current_app as app
from flask_login import login_required, logout_user


# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@main_bp.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    """Serve logged-in Dashboard."""
    return render_template('dashboard.jinja2',
                           title='Flask-Login Tutorial.',
                           template='dashboard-template',
                           current_user=current_user,
                           body="You are now logged in!")


@main_bp.route('/', methods=['GET'])
def home():
    """Serve logged-in Dashboard."""
    return render_template('index.jinja2',
                           title='Flask-Login Tutorial.',
                           template='index-template')


@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))
