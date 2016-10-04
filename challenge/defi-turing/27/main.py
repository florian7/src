#!/usr/bin/python3 

sieve = [False, False, True]

def fill_sieve(n):
    global sieve
    
    sieve += [True] * (n - len(sieve) + 1)
    for i in range(len(sieve)):
        if not sieve[i]:
            continue
        for m in range(2 * i, n + 1, i):
            sieve[m] = False

def is_prime(n):
    global sieve
    
    if n < 2:
        return False
    if len(sieve) < n + 1 or sieve[n] == None:
        fill_sieve(n)

    return sieve[n]

r = 3000
max_n = 0
max_ab = 0

for a in range(-r + 1, r):
    for b in range(-r + 1, r):
        n = 0

        while is_prime(n ** 2 + a * n + b):
            n += 1

        if n > max_n:
            max_n = n
            max_ab = a * b
            print("a = {}, b = {}".format(a, b))
            print("max_n = {}, max_ab = {}".format(max_n, max_ab))
