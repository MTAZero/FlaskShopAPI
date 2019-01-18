from flask import Flask
from flask.ext.cors import CORS

server = Flask(__name__)

CORS(
    server,
    resources={r"/*": {"origins": "*"}},
    headers=['Content-Type', 'X-Requested-With', 'Authorization']
)

@server.route("/")
def hello():
    return "Hello! I am API service!"

from route.item import item_blueprint
server.register_blueprint(item_blueprint, url_prefix='/items/')

if __name__ == '__main__':
    server.debug = True
    server.run(port=5000)