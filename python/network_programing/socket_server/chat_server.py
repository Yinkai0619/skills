#!/usr/bin/env python

import socketserver
import threading
import logging

FORMAT="%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)

class ChatServer(socketserver.BaseRequestHandler):
    clients = {}

    def setup(self) -> None:
        super().setup()
        self.event = threading.Event()
        self.clients[self.client_address] = self.request
        # return super().setup()

    def finish(self) -> None:
        super().finish()
        self.event.set()
        self.clients.pop(self.client_address)
        # return super().finish()

    def handle(self) -> None:
        while not self.event.is_set():
            sock = self.request
            raddr = self.client_address

            data = sock.recv(1024)
            logging.info("{}".format(data.decode()))

            if data.strip() == b"quit" or data == b"":
                print(data,"~~~~~~~~")
                break

            msg = "Ack: {}".format(data.decode()).encode()
            # sock.send(msg)
            for client in self.clients.values():
                client.send(msg)


        # return super().handle()


server = socketserver.ThreadingTCPServer(("127.0.0.1", 9999), ChatServer)
threading.Thread(target=server.serve_forever, name="server").start()

while True:
    cmd = input(">>>")
    if cmd.strip() == "quit":
        logging.info(cmd)
        server.server_close()
        threading.Event().wait(2)
        break
    print(threading.enumerate())