import selectors
import socket
import threading


def accept(sock:socket.socket):
    # print("~~~~~~~~~~~")
    # print(sock)
    conn, raddr = sock.accept()
    conn.setblocking(False)
    key = selector.register(conn, selectors.EVENT_READ, data=recv)
    # print(conn)
    # print(raddr)
    conn.send(b'Hello World!')
    # print("~~~~~~~~~~~")


def recv(conn:socket.socket):
    print('-' * 50)
    data = conn.recv(1024)
    msg = "Your message = {}".format(data.decode())
    conn.send(msg.encode())
    print('-' * 50)



def select(e:threading.Event):
    while not e.is_set():
        events = selector.select()
        # print(events, "----------------------------")
        for key, mask in events:
            print(key)
            print(key.data)
            print(mask)
            key.data(key.fileobj)

if __name__ == "__main__":
    selector = selectors.DefaultSelector()
    event = threading.Event()

    server = socket.socket()
    server.bind(("127.0.0.1", 9999))
    server.listen()
    server.setblocking(False)
    key = selector.register(server, selectors.EVENT_READ, data=accept)

    threading.Thread(target=select, name="select", args=(event,)).start()


    while True:
        cmd = input(">>>")
        if cmd.strip() == "quit":
            event.set()
            fobjs = []
            for key in selector.get_map().values():
                fobjs.append(key.fileobj)
            for fobj in fobjs:
                selector.unregister(fobj)
                fobj.close()
            selector.close()
            break
        print(list(selector.get_map().keys()))
        print(list(selector.get_map().values()))