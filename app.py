from flask import Flask
from config import DevelopmentConfig, TestingConfig, ProductionConfig
from db import create_database
from routes.auth_routes import auth_bp
from routes.productos_routes import productos_bp

def create_app(config=None):
    app = Flask(__name__)
    if config is None:
        config =  DevelopmentConfig
    app.config.from_object(config)

    # Crear base de datos
    create_database()

    # Registrar blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(productos_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

