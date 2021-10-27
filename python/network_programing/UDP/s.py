import socket
import threading

# 1. UDP Socket
server = socket.socket(type=socket.SOCK_DGRAM)

# 2. bind
addr = ("127.0.0.1", 9999)
server.bind(addr)

# 3. receive
while True:
    # data = server.recv(1024).decode()
    data, info = server.recvfrom(1024)
    data = data.decode()
    if data.strip() == "quit":
        break
    print(data, info)

    msg = "{}:{} ==> {}".format(*info, data).encode()
    server.sendto(msg, info)

server.close()

