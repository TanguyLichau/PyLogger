import socket

# initializing the socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = "192.168.1.54"  # the ip of the server.
PORT = 5050  # the port of the server.

soc.connect((IP, PORT))  # connecting to the server.

print(soc.recv(1024).decode('ascii'))
