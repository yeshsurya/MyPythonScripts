from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
s.sendto(b'Hello UPP client here !', ('localhost', 20000))
s.recvfrom(8192)