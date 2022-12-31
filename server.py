import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = '192.168.1.54'

PORT = 5050

s.bind((IP, PORT))


s.listen()
print('IP : ' + IP)
while True:
    client, addr = s.accept()
    print(f"Got a connection from {str(addr)}")
    msg = 'Thanks for the connection'
    client.send(msg.encode('ascii'))
    client.close()


