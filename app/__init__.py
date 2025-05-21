from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importa e registra as rotas
    from .routes.main import main
    from .routes.views import crypto

    app.register_blueprint(main)
    app.register_blueprint(crypto)

    return app