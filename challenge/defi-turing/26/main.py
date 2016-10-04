#!/usr/bin/python3 

from itertools import permutations

def dec_to_n(d):

    n = 0
    for i in range(len(d)):
        n += d[i] * 10 ** (len(d) - i - 1)

    return n

k = 9

for p in permutations(range(1, k + 1)):

    divisible = True
    for i in range(1, k + 1):
        n = dec_to_n(p[:i])
        if n % i != 0:
            divisible = False

    if divisible:
        print(dec_to_n(p))
