#Python has built in support for TCP sockets 
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#STREAM for a stream of characters
mysock.connect( ('data.pr4e.org', 80) )
#domain to connect to, and port 


telnet www.nba.com 80

GET http://www.nba.com HTTP/1.0


import socket

mysock = socket.socket(socket.af_inet, SOCKET.sock_stream)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET'
mysock.send(cmd)

while True:
	data = mysock.recv(512)
	if (len(data) < 1):
		break
	print(data.decode())
mysock.close()

# GET http://data.pr4e.org/romeo.txt HTTP/1.0

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
	data = mysock.recv(512)
	if (len(data) < 1) :
		break
	print(data.decode())
mysock.close() 
