from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.brand import Brand
    from app.models.manufacturer import Manufacturer
    from app.admin import setup_admin

    
    setup_admin(app)
    
    from app.routes.brand_api import brand_bp
    from app.routes.manufacturer_api import manufacturer_bp
    from app.routes.admin_client import admin_bp
    from app.routes.auth import auth_bp

    
    app.register_blueprint(auth_bp)

    app.register_blueprint(admin_bp, url_prefix='/client')

    app.register_blueprint(brand_bp, url_prefix='/api/v1/brands')
    app.register_blueprint(manufacturer_bp, url_prefix='/api/v1/manufacturers')

    return app
