#/usr/bin/python3 

from itertools import product
import string, subprocess

for length in range(12):
    for p in product(string.ascii_letters + string.digits, repeat = length):
        password = "".join(p)
        proc = subprocess.Popen(["./ch25.bin", password], shell = False, stdout = subprocess.PIPE)
        
        stdout = proc.communicate()[0].decode("ascii")
        if "incorrect" in stdout:
            continue

        print("{} : {}".format(stdout, password))
        break
