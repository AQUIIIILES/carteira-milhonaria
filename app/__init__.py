from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Importa e registra as rotas
    from .routes.main import main
    from .routes.views import crypto

    app.register_blueprint(main)
    app.register_blueprint(crypto)

    return app