#!/usr/bin/python3 

import base64, sys, re, datetime

def get_timestamp(time_string):
    return -datetime.datetime.strptime(time_string, '%H:%M:%S').timestamp()

def revbits(x):
    return int(bin(x)[2:].zfill(7)[::-1], 2)

if len(sys.argv) < 2:
    print("Usage: {} <file>".format(sys.argv[0]))
    exit()


with open(sys.argv[1], 'r') as f:
    lines = f.read().split('\n')

timestamp = 0
last_timestamp = 0
value = 0
password = []
for i, line in enumerate(lines):

    time_string = re.sub('.*:(\d{2}:\d{2}:\d{2}).*', r'\1', line)

    if len(time_string) != 8:
        continue


    if i == 0:
        timestamp = get_timestamp(time_string)
        print("[{}] = {}".format(time_string, timestamp))
        continue


    last_timestamp = timestamp
    timestamp = get_timestamp(time_string)
    difference = int(last_timestamp - timestamp)
    value += difference // 2

    print("[{}] = {} +{} {:#010b}".format(time_string, timestamp, difference, value))

    if i % 4 == 0:
        value //= 2
        password += [chr(value)]
        
        print("value: 0x{:07X} = {:#07b}".format(value, value))

        value = 0


    else:
        value *= 4

print(''.join(password))
print(len(password))
