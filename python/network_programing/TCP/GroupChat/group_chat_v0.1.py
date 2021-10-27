import socket

# 1. Create server socket
server = socket.socket()

# 2. Bind
ip = '127.0.0.1'
port = 9999
addr = (ip, port)
server.bind(addr)

# 3. Listen
server.listen()

# 4. Accept 阻塞，等待客户端连接
s1, info = server.accept()
print(s1)    # New Socket
print(info)     # remote addr

data1 = s1.recv(1024)     # 阻塞，等待客户端的数据
print(data1)

msg1 = 'Your message: {}'.format(data1.decode())
s1.send(msg1.encode())    # send info to client

# s2, _ = server.accept()
# print(s2)
# data2 = s2.recv(1024)
# print(data2)
# msg2 = 'msg2: ' + data2.decode()
# s2.send(msg2.encode())




# 5. Close
server.close()
