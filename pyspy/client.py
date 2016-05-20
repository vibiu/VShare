#!/usr/bin/env python
# coding: utf-8

import socket

BUF_SIZE = 1024
server_addr = ('127.0.0.1',8888)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_addr)
while True:
    data = raw_input('please inpu some string >')
    client.sendall(data)
    data = client.recv(BUF_SIZE)
    print data
client.close()
