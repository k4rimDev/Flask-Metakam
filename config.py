import os


class Config:
    # General Config
    SECRET_KEY = os.getenv('SECRET_KEY', 'fdffe0638dae8eae935e562d2adfeb94')
    DEBUG = True

    # Database Config
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-WTF Config
    WTF_CSRF_ENABLED = True
