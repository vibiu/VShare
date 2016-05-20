import socket
import commands

BUG_SIZE = 1024
server_addr = ('127.0.0.1', 8888)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(server_addr)
server.listen(5)
while True:
    client, client_addr = server.accept()
    print 'Connected by', client_addr
    while True:
        data = client.recv(BUG_SIZE)
        print data
        client.sendall(data)
server.close()
