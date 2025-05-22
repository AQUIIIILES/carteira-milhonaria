from flask import Flask, Blueprint
from views import crypto

app = Flask(__name__)
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Hello, World!"

app.register_blueprint(main)
app.register_blueprint(crypto)

if __name__ == '__main__':
    app.run(debug=True, port=5001)