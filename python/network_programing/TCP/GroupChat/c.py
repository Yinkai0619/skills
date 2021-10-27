#!/usr/bin/env python

import logging
import datetime
import threading
import socket

FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)


class ChatClient:
    def __init__(self, ip="127.0.0.1", port=9999):
        self.sock = socket.socket()
        self.ip = ip
        self.port = port
        self.raddr = (ip, port)
        self.event = threading.Event()

    def start(self):
        self.sock.connect(self.raddr)
        self.send("I'm ready.")
        threading.Thread(target=self.recv, name="recv").start()

    def recv(self):
        while not self.event.is_set():
            try:
                data = self.sock.recv(1024)
            except Exception as e:
                logging.error(e)
                break
            # msg = "{:%Y/%m/%d %H:%M:%S} {}:{}\n{}\n".format(datetime.datetime.now(), *self.raddr, data.strip().decode())
            # logging.info(msg)
            print(data.decode())

    def send(self, msg: str):
        data = "{}".format(msg.strip()).encode()
        self.sock.send(data)

    def stop(self):
        self.sock.close()
        self.event.wait(3)
        self.event.set()
        logging.info("Client stop.")


def main():
    cc = ChatClient()
    cc.start()
    while True:
        cmd = input('>>>')
        if cmd == "quit":
            cc.send(cmd)
            cc.stop()
            break
        cc.send(cmd)


if __name__ == "__main__":
    main()
