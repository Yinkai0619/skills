#!/usr/bin/env python

import socket
import datetime
import threading
import logging

FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatServer:
    def __init__(self, ip='0.0.0.0', port=9999) -> None:
        self.sock = socket.socket()
        self.addr = (ip, port)
        self.clients = {}
        self.event = threading.Event()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()

        # 在一个子线程中启动accept，避免阻塞主线程
        threading.Thread(target=self.accept, name='accept').start()
        # self.accept()

    def accept(self):
        count = 1
        # 在单独的工作线程中接收客户端发来的数据，避免阻塞accept线程和实现多个客户端的连接
        # while True:
        while not self.event.is_set():
            sock, raddr = self.sock.accept()    # 阻塞
            f = sock.makefile('rw')
            self.clients[raddr] = f     #sock

            # threading.Thread(target=self.recv, args=(sock, raddr), name='recv-{}'.format(count)).start()
            threading.Thread(target=self.recv, args=(sock, f, raddr), name='recv-{}'.format(count)).start()
            count += 1
            # self.recv(sock)

    # def recv(self, sock: socket.socket, raddr):
    def recv(self, s, f, raddr):
        # while True:
        while not self.event.is_set():
            # data = sock.recv(1024).decode()
            data = f.readline()
            logging.info(data)
            print('{}+++++++++++++++++++='.format(data))

            if data.strip() == 'quit':
                self.clients.pop(raddr)
                # sock.close()
                f.close()
                s.close()
                break

            msg = 'Ack: {}'.format(data)
            # msg = msg.encode()
            for client in self.clients.values():
                # client.send(msg)
                client.write(msg)
                client.flush()

    def stop(self):
        for c in self.clients.values():
            c.close()
        self.sock.close()
        self.event.set()


cs = ChatServer(ip='127.0.0.1')
cs.start()

while True:
    cmd = input('>>>')
    if cmd == 'quit':
        logging.info('Quit')
        cs.stop()
        break
    print(threading.enumerate())
