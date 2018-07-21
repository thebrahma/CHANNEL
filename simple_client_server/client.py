import socket
s = socket.socket()

port = 12345

s.connect(('100.112.168.110',port))

print(s.recv(1024))

s.close()