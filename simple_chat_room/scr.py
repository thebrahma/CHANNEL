# Python program to implement server side of chat room.
import socket
import select
import sys
from _thread import *
 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
# if len(sys.argv) != 3:
#     print("Correct usage: script, IP address, port number")
#     exit()
 
#IP_address = str(sys.argv[1])
IP_address = ""
print (IP_address)
 
#Port = int(sys.argv[2])
Port = 12345
print(Port)



server.bind((IP_address, Port))
print("1") 
server.listen(100)
 
list_of_clients = []
 
def clientthread(conn, addr):
 
    conn.send(b'Welcome to this chatroom!')
 
    while True:
            try:
                message = conn.recv(2048)
                message = message.decode('utf-8')
                if message:
                    print('<' + addr[0] + '>' + message)
                    # print("<" + addr[0] + "> " + message)
                    output = addr[0].encode('utf-8')
                    message = message.encode('utf-8')
                    # message_to_send = "<" + addr[0] + "> " + message
                    message_to_send = b'<' + output + b'>'+ message
                    broadcast(message_to_send, conn)
 
                else:
                    remove(conn)
 
            except:
                continue
 
def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message)
            except:
                clients.close()
 
                # if the link is broken, we remove the client
                remove(clients)
 
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)
 
while True:
    conn, addr = server.accept()

    list_of_clients.append(conn)
    
    #output = addr[0].decode('utf-8')
    print(addr[0] + ' connected')
 
    start_new_thread(clientthread,(conn,addr))    
 
conn.close()
server.close()
