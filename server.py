import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = ''  #Enter the same IP adress here and in the client.py file

PORT = 5050

s.bind((IP, PORT))

s.listen()
client, addr = s.accept()
print(f"Got a connection from {str(addr)}")
while True:
    data = client.recv(1024)
    if data:
        print(data.decode('utf-8'))


