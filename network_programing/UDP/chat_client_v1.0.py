#!/usr/bin/env python

import socket
import threading
import logging
import datetime

FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)

class ChatUdpClient:
    def __init__(self, ip="127.0.0.1", port=9999) -> None:
        self.sock = socket.socket(type=socket.SOCK_DGRAM)
        self.raddr = (ip, port)
        self.event = threading.Event()

    def start(self):
        self.sock.connect(self.raddr)
        self.send("Hello. I'm {}".format(self.sock.getsockname()))
        threading.Thread(target=self.recv, name="recv").start()
        print(self.sock,"~~~~~~~~~")

    def send(self, msg:str):
        msg = "{}: {}\n".format(datetime.datetime.now(), msg).encode()
        self.sock.send(msg)

    def recv(self):
        while not self.event.is_set():
            data, server = self.sock.recvfrom(1024)
            logging.info(data.decode())
            # logging.info(server)
        

    def stop(self):
        self.sock.close()

def main():
    cc = ChatUdpClient()
    cc.start()
    cc1 = ChatUdpClient()
    cc1.start()
    while True:
        cmd = input(">>")
        if cmd.strip() == "quit":
            cc.stop()
            cc1.stop()
            break
        
        if cmd.strip() == "lss":
            # print(threading.enumerate)
            print(cc.sock)

        cc.send(cmd)
        cc1.send(cmd)
        

if __name__ == "__main__":
    main()
