from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin

import time
import random

app = Flask(__name__)

cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['CORS_HEADERS'] = 'Content-Type'


io = SocketIO(app, cors_allowed_origins='*')

@io.on('getData')
def handle_getdata_event():
    """
        Retona os dados para client
    """
    count = 0
    while True:
        count+=1
        time.sleep(2)
        msg = {"x": count, "y": random.randint(1, 100) }
        io.emit('getData', msg)

@io.on('newConnect')
def handle_newconnect_event(json):
    print("\n\n " + json['data'] + "\n\n")
    handle_getdata_event()

if __name__ == '__main__':
    io.run(app, debug=False)