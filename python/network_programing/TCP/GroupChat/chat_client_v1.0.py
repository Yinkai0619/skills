import socket
import threading

class ChatClient:
    def __init__(self, ip="127.0.0.1", port=9999):
        self.sock = socket.socket()
        self.raddr = (ip, port)
        self.event = threading.Event()

    def start(self):
        self.sock.connect(self.raddr)
        threading.Thread(target=self.recv).start()
        self.send("Hello, I am ready.")

    def recv(self):
        while self.event.is_set():
            data = self.sock.recv(1024)
            print(data)

    def send(self, msg:str):
        msg = '{}'.format(msg).encode()
        self.sock.send(msg)

    def stop(self):
        self.sock.close()
        self.event.set()


def main():
    cc = ChatClient()
    cc.start()

    while True:
        cmd = input(">>")
        if cmd.strip() == 'quit':
            cc.send("quit")
            cc.stop()
        cc.send(cmd)


if __name__ == '__main__':
    main()
