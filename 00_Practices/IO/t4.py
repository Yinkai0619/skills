import asyncio

# TCP Echo Server
async def handle(reader, writer):
    while True:
        data = await reader.read(1024)
        print(dir(reader))
        print(dir(writer))
        client = writer.get_extra_info("peername")
        message = "{} Your msg {}".format(client, data.decode()).encode()
        writer.write(message)
        await writer.drain()


loop = asyncio.get_event_loop()
ip = "127.0.0.1"
port = 9999
crt = asyncio.start_server(handle, ip, port, loop=loop)

server = loop.run_until_complete(crt)
print(server)
try:
    print('-' * 30)
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
