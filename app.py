from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin

from websocket.socket import FootprintWebSocket


app = Flask(__name__)

cors = CORS(app, resources={r"/foo": {"origins": "*"}})

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['CORS_HEADERS'] = 'Content-Type'


def set_app(app: object):
    """Faz a inicialização da aplicação

    Args:
        app (object): servidor flask
    """
    footprint_websocket = FootprintWebSocket(app)
    footprint_websocket.run_websocket()



if __name__ == '__main__':
    set_app(app)
    