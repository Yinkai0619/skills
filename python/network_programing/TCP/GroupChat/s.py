import socket
import threading
import datetime
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(thread)d %(message)s")


class ChatServer:
    def __init__(self, ip="127.0.0.1", port=9999):
        self.sock = socket.socket()
        self.addr = (ip, port)
        self.clients = {}
        self.event = threading.Event()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        threading.Thread(target=self.accept, name="Thread-accept").start()

    def accept(self):
        while not self.event.is_set():
            sock, client = self.sock.accept()
            self.clients[client] = sock

            threading.Thread(target=self.recv, name="Thread-recv", args=(sock, client)).start()

    def recv(self, sock: socket.socket, client):
        while not self.event.is_set():
            try:
                data = sock.recv(1024).decode()
            except Exception as e:
                logging.error(e)
                data = "quit"

            msg = data.strip()
            if msg == "quit":
                self.clients.pop(client)
                sock.close()
                logging.info("{} quit.".format(client))
                break
            msg = "{:%Y/%m/%d %H:%M:%S} {}:{} ==> {}\n\n".format(datetime.datetime.now(), *client,
                                                                 data.strip())
            logging.info(msg)
            msg = "{}".format(msg).encode()
            for s in self.clients.values():
                try:
                    s.send(msg)
                except OSError as ose:
                    logging.error(ose)
                    sock.close()

    # def send(self):
    #     pass

    def stop(self):
        for s in self.clients.values():
            s.close()
        self.sock.close()
        self.event.set()


def main():
    cs = ChatServer()
    cs.start()

    while True:
        cmd = input(">>>").strip()
        print(cmd)
        if cmd == "quit":
            cs.stop()
            threading.Event().wait(3)
            break
        else:
            logging.info(threading.enumerate())


if __name__ == '__main__':
    main()
