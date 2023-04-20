import os
import time
import sys,webbrowser
import ctypes
from tqdm import tqdm
from pprint import pprint
from messente_api import OmnimessageApi, SMS, Omnimessage, Configuration, ApiClient
from messente_api.rest import ApiException
from colored import fg, bg, attr


reset = attr('reset')

os.system('mode con: cols=80 lines=25')

def check_admin():
    
    try:
        isAdmin = ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        isAdmin = False
    if not isAdmin:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()

def logo():
    print("\033[1;35;40m           █▀▀▀ █  █ █▀▀█ █▀▀█ █▀▀ █  █ █▀▀█ █▀▀ █▀▀ █▀▀█   ▀█ █▀ ▄█ ")
    print("\033[1;35;40m           █ ▀█ █  █ █▄▄█ █  █ █   █▀▀█ █▄▄█ ▀▀█ █▀▀ █▄▄▀    █▄█   █ ")
    print("\033[1;35;40m           ▀▀▀▀  ▀▀▀ ▀  ▀ █▀▀▀ ▀▀▀ ▀  ▀ ▀  ▀ ▀▀▀ ▀▀▀ ▀ ▀▀     ▀   ▄█▄")

def start():
    print("")
    print("")
    print("")
    print("")
    print("")
    logo()
    print("")
    print("")
    print("")
    print("\033[1;35;40m                        ╔══════════════════════════════╗")
    print("\033[1;35;40m                        ║                              ║")
    print("\033[1;35;40m                        ║    [1]: Send SMS with ID     ║")
    print("\033[1;35;40m                        ║                              ║")
    print("\033[1;35;40m                        ║    [2]: Credits              ║")
    print("\033[1;35;40m                        ║                              ║")
    print("\033[1;35;40m                        ╚══════════════════════════════╝")
    print("")
    t = input("\033[1;35;40m                             Choose an option > ")

    if t == "1":
        os.system('cls')
        time.sleep(1)
        input1()
    if t == "2":
        os.system('cls')
        time.sleep(1)
        credits()
    else:
        os.system('cls')
        print("")
        print("")
        print("")
        print("")
        print("")
        print("\033[1;35;40m          Please fill in the blanks with the correct answer!")
        print("")
        print("")
        print("\033[1;35;40m                          Like this: 1 or 2")
        time.sleep(4)
        os.system('cls')
        start()


def credits():
    os.system('cls')
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("\033[1;36;40m               █▀▀ █▀▀█ █▀▀ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀▄    █▀▀▄ █  █ ▄ ")
    print("\033[1;36;40m               █   █▄▄▀ █▀▀ █▄▄█   █   █▀▀ █  █    █▀▀▄ █▄▄█   ")
    print("\033[1;36;40m               ▀▀▀ ▀ ▀▀ ▀▀▀ ▀  ▀   ▀   ▀▀▀ ▀▀▀     ▀▀▀  ▄▄▄█ ▀ ")
    print("")
    print("")
    print("")
    print("\033[1;36;40m                █▀▀▀  █        █▀▀█  █  █  █▀▀█  █▀▀█  █▀▀▀█ ")
    print("\033[1;36;40m                █▀▀▀  █        █ ▄▄  █  █  █▄▄█  █▄▄█  █   █ ")
    print("\033[1;36;40m                █▄▄▄  █▄▄█     █▄▄█  ▀▄▄▀  █  █  █     █▄▄▄█ ")
    time.sleep(5)
    os.system('cls')
    start()


def sendtext(t,p,n):
    # Input code here for api to send sms.
    # t = sender id
    # p = text u want to send
    # n = number you want to send to
    # example from = t, text = p, reciever = n    

def answer2(t,p):
        print("")
        print("")
        print("")
        print("")
        print("")
        logo()
        print("")
        print("")
        print("\033[1;35;40m                        ╔══════════════════════════════╗")
        print("\033[1;35;40m                        ║                              ║")
        print("\033[1;35;40m                        ║   Choose a number you want   ║")
        print("\033[1;35;40m                        ║   to send the message to!    ║")
        print("\033[1;35;40m                        ║                              ║")
        print("\033[1;35;40m                        ║    Example: +31715374955     ║")
        print("\033[1;35;40m                        ║                              ║")
        print("\033[1;35;40m                        ╚══════════════════════════════╝")
        print("")
        n = input("\033[1;35;40m                             Enter Number > ")
        if p == "":
            os.system('cls')
            print("")
            print("")
            print("")
            print("")
            print("")
            print("\033[1;35;40m                    Please fill in the blanks with a Number!")
            print("")
            print("")
            print("\033[1;35;40m                            Like this: +31715374955")
            time.sleep(2)
            os.system('cls')
            answer2()
        else:
            os.system('cls')
            sendtext(t,p,n)

def answer(t):
    print("")
    print("")
    print("")
    print("")
    print("")
    logo()
    print("")
    print("")
    print("\033[1;35;40m                        ╔══════════════════════════════╗")
    print("\033[1;35;40m                        ║                              ║")
    print("\033[1;35;40m                        ║ Choose a text u want to send ║")
    print("\033[1;35;40m                        ║                              ║")
    print("\033[1;35;40m                        ╚══════════════════════════════╝")
    print("")
    p = input("\033[1;35;40m                             Enter Text > ")
    if p == "":
        os.system('cls')
        print("")
        print("")
        print("")
        print("")
        print("")
        print("\033[1;35;40m                    Please fill in the blanks with text!")
        print("")
        print("")
        print("\033[1;35;40m                       Like this: John was a good man")
        time.sleep(2)
        os.system('cls')
        answer()
    else:
        os.system('cls')
        answer2(t,p)

def input1():
    print("")
    print("")
    print("")
    print("")
    print("")
    logo()
    print("")
    print("")
    print("\033[1;35;40m                        ╔══════════════════════════════╗")
    print("\033[1;35;40m                        ║                              ║")
    print("\033[1;35;40m                        ║      Choose a Sender id      ║")
    print("\033[1;35;40m                        ║                              ║")
    print("\033[1;35;40m                        ║       Example: John Do       ║")
    print("\033[1;35;40m                        ║                              ║")
    print("\033[1;35;40m                        ╚══════════════════════════════╝")
    print("")
    t = input("\033[1;35;40m                        Enter a Sender ID > ")
    if t == "":
        os.system('cls')
        print("")
        print("")
        print("")
        print("")
        print("")
        print("\033[1;35;40m                    Please fill in the blanks with a Sender ID!")
        print("")
        print("")
        print("\033[1;35;40m                                    Like this: John")
        time.sleep(2)
        os.system('cls')
        input1()
    else:
        os.system('cls')
        answer(t)


check_admin()

print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
for i in tqdm(range(25),desc="\033[1;35;40m    Loading Application", ncols=75):
    time.sleep(0.1)
time.sleep(1)
os.system('cls')
start()
