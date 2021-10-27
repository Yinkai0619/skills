#!/usr/bin/env python

import socket
import threading
import logging

FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)


class ChatUdpServer:
    def __init__(self, ip="127.0.0.1", port=9999) -> None:
        self.sock = socket.socket(type=socket.SOCK_DGRAM)
        self.addr = (ip, port)
        self.clients = set()
        self.event = threading.Event()

    def start(self):
        self.sock.bind(self.addr)

        threading.Thread(target=self.recv, name="recv").start()

    def recv(self):
        while not self.event.is_set():
            data, raddr = self.sock.recvfrom(1024)
            logging.info(data.decode())
            # logging.info(raddr)
            if data.strip() == b'quit':
                if raddr in self.clients:
                    self.clients.remove(raddr)
                continue

            self.clients.add(raddr)

            msg = "{}:{} ==> {}\n".format(*raddr, data.decode().strip()).encode()
            for r in self.clients:
                self.sendto(msg, r)

    def sendto(self, msg: str, addr):
        self.sock.sendto(msg, addr)

    def stop(self):
        self.sock.close()
        self.event.set()


def main():
    cs = ChatUdpServer()
    cs.start()
    while True:
        cmd = input(">>>")
        if cmd == "quit":
            cs.stop()
            break
        


if __name__ == "__main__":
    main()
