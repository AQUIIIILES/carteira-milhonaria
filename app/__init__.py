from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Importa e registra os blueprints
    from .main import main as main_blueprint
    from .routes import crypto as crypto_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(crypto_blueprint)

    return app
