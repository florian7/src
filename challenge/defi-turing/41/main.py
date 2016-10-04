#!/usr/bin/python3 

import code
from itertools import permutations

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

def dec_to_n(dec):
    value = 0
    for i in range(len(dec)):
        value += dec[i] * 10 ** i
    return value


max_pandigital = 0
for p in permutations(range(1, 10)):

    n = dec_to_n(p)

    if not is_prime(n):
        continue

    print("{} is prime".format(n))
    if max_pandigital < n:
        max_pandigital = n
        print("{} is max".format(n))

print("max_pandigital = {}".format(max_pandigital))
