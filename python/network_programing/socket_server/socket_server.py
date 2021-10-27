#!/usr/bin/env python

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        print(self.request)
        print(self.client_address)
        print(self.server)

        while True:
            data = self.request.recv(1024).strip()
            print("{} wrote: {}".format(self.client_address[0], data))
            self.request.sendall(data.upper())


HOST, PORT = "127.0.0.1", 9999
# server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
server.serve_forever()


server.server_close()



# if __name__ == "__main__":
#     HOST, PORT = "127.0.0.1", 9999

#     with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
#         server.serve_forever()

