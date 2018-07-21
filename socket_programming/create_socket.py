import socket
import sys
try :
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print("SUCCESS")
except socket.error as err :
	print("FAILED")
	sys.exit()
port = 80

try :
	host_ip = socket.gethostbyname('www..com')
except socket.gaierror :
	print("ERROR IN HOST ")


s.connect((host_ip,port))

print("SOCKET CONNECTED on port == %s" %(host_ip))