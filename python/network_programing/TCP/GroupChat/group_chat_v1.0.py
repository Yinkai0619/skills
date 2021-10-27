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

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()

        # 在一个子线程中启动accept，避免阻塞主线程
        threading.Thread(target=self.accept, name='accept').start()
        # self.accept()

    def accept(self):
        count = 1
        # 在单独的工作线程中接收客户端发来的数据，避免阻塞accept线程和实现多个客户端的连接
        while True:
            sock, raddr = self.sock.accept()
            threading.Thread(target=self.recv, args=(sock,), name='recv-{}'.format(count)).start()
            count += 1
            # self.recv(sock)

    def recv(self, sock: socket.socket):
        while True:
            data = sock.recv(1024).decode()
            logging.info(data)

            msg = 'Your message: {}'.format(data).encode()
            sock.send(msg)

    def stop(self):
        self.sock.close()


cs = ChatServer(ip='127.0.0.1')
cs.start()

while True:
    cmd = input('>>>')
    if cmd == 'quit':
        logging.info('Quit')
        cs.stop()
        break
    print(threading.enumerate())
