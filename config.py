"""App configuration."""
from os import environ

import os
class Config:
    """Set Flask configuration vars from environment variables."""

    SECRET_KEY = environ.get('SECRET_KEY') or os.urandom(24)
    FLASK_APP = environ.get('FLASK_APP')
    STATIC_FOLDER = '/sample_app/static'
    TEMPLATES_FOLDER = '/sample_app/templates'

    # SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/flask_test'
    # SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
