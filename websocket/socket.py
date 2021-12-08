from flask_socketio import SocketIO

import time
import random


class FootprintWebSocket():

    def __init__(self, app: object) -> object:
        """Função construtora do serviço de websocket

        Args:
            app (object): servidor flask

        Returns:
            object: Instância do serviço
        """
        self.app = app


    def run_websocket(self):
        """Funções do websocket e servidor websocket
        """
        io = SocketIO(self.app, cors_allowed_origins='*')
        
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



        return io.run(self.app, debug=True)





    