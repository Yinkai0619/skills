#!/usr/bin/env python

import socket
import threading
import logging
import datetime

FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)


class ChatUdpServer:
    def __init__(self, ip="127.0.0.1", port=9999, interval=10) -> None:
        self.sock = socket.socket(type=socket.SOCK_DGRAM)
        self.addr = (ip, port)
        self.clients = dict()
        self.event = threading.Event()
        self.interval = interval

    def start(self):
        self.sock.bind(self.addr)

        threading.Thread(target=self.recv, name="recv").start()

    def recv(self):
        while not self.event.is_set():
            data, raddr = self.sock.recvfrom(1024)
            localkeys = set()
            logging.info(data.decode())
            # logging.info(raddr)

            if data.strip() == b"^hb^":
                self.clients[raddr] = datetime.datetime.now().timestamp()
                print("hb" * 20)
                continue

            if data.strip() == b'quit':
                if raddr in self.clients.keys():
                    self.clients.pop(raddr)
                continue

            self.clients[raddr] = datetime.datetime.now().timestamp()

            current = datetime.datetime.now().timestamp()
            msg = "{}:{} ==> {}\n".format(*raddr, data.decode().strip()).encode()
            for r, ts in self.clients.items():
                if current - ts > self.interval:
                    localkeys.add(r)
                self.sendto(msg, r)

            for k in localkeys:
                print(k, "kkkkkkkkkkkkkkkk")
                self.clients.pop(k)

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
        print(threading.enumerate())
        print(cs.clients)
        

if __name__ == "__main__":
    main()
