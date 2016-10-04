#!/usr/bin/python3 

import sys
import socket
import time
import base64


host = "irc.root-me.org"
port = 6667
nickname = "Helvethor"
identity = "helvethor"
realname = "HelvethorBot"
readbuffer = ""

def s_send(msg):
    global s
    s.send("{}\r\n".format(msg).encode("utf-8"))

def s_recv(buf):
    global s
    buf += s.recv(1024).decode("utf-8")
    return buf


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s_send("NICK {}".format(nickname))
s_send("USER {} {} bla :{}".format(identity, host, realname))
time.sleep(2)

query_sent = False
response_sent = False
result_received = False

while True:

    readbuffer = s_recv(readbuffer)
    tmp = readbuffer.split("\n")
    readbuffer = tmp.pop()

    for line in tmp:
        print(line)

        if query_sent and not response_sent:
            if "PRIVMSG {}".format(nickname) in line:
                encoded = line.split(":")[-1]
                decoded = base64.b64decode(encoded).decode("utf-8")
                print(decoded)
                s_send("PRIVMSG Candy !ep2 -rep {}".format(decoded))
                response_sent = True

    if not query_sent:
        s_send("PRIVMSG Candy :!ep2")
        time.sleep(1)
        query_sent = True

