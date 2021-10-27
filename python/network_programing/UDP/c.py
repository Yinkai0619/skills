#!/usr/bin/env python

import socket

sock = socket.socket(type=socket.SOCK_DGRAM)
raddr = "127.0.0.1", 9999
# sock.connect(raddr)

while True:
    cmd = input(">>>")
    if cmd == "quit":
        break
    if cmd == 'lss':
        print(sock)
    sock.sendto(cmd.encode(), raddr)
    # sock.send(cmd.encode())

    data, info = sock.recvfrom(1024)
    print(data.decode())

sock.close()

