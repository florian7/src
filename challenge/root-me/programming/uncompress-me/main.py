#!/usr/bin/python3 

import sys
import socket
import time
import base64
import zlib


def s_send(msg):
    global s
    s.send("{}\r\n".format(msg).encode("utf-8"))

def s_recv(buf):
    global s
    buf += s.recv(1024).decode("utf-8")
    return buf


host = "irc.root-me.org"
port = 6667
nickname = "Helvethor"
identity = "helvethor"
realname = "HelvethorBot"
bot = "Candy"
challenge = "!ep4"
readbuffer = ""


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
                compressed = base64.b64decode(encoded)
                decompressed = zlib.decompress(compressed).decode("utf-8")
                print(decompressed)
                s_send("PRIVMSG {} {} -rep {}".format(bot, challenge, decompressed))
                response_sent = True

    if not query_sent:
        s_send("PRIVMSG {} :{}".format(bot, challenge))
        query_sent = True
