# Python program to implement client side of chat room.
import socket
import select
import sys
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# if len(sys.argv) != 3:
#     print ("Correct usage: script, IP address, port number")
#     exit()
#IP_address = str(sys.argv[1])
IP_address = ""
print(IP_address)
#Port = int(sys.argv[2])
Port = 12345
print(Port)
#print(server.if_nameindex())
server.connect((IP_address, Port))


while True:
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
    for socks in read_sockets:
        if socks == server:
        
            message = socks.recv(2048)
            
            message = message.decode('utf-8')
            print(type(message))
            print(message)
        else:
            message = sys.stdin.readline()
            message = message.encode('utf-8')
            server.send(message)
            sys.stdout.write('<You>')
            message = message.decode('utf-8')
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()