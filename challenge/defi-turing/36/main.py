#!/usr/bin/python3 

from math import log, ceil
from itertools import product

def is_palindrome(l):
    return l == l[::-1]

def n_to_b(n, b):
    p_max = ceil(log(n, b))
    base_repr = []
    started = False
    for p in reversed(range(p_max + 1)):
        c = n // b ** p 
        if c < 0:
            continue
        elif c == 0 and not started:
            continue
        started = True
        n -= c * b ** p
        base_repr += [c] 

    return tuple(base_repr)


n_max = 10000000
palins = set()
        
for n in range(1, n_max, 2):

    b10 = n_to_b(n, 10)
    if not is_palindrome(b10):
        continue

    b2 = n_to_b(n, 2)
    if not is_palindrome(b2):
        continue

    print("{} - {}".format(b2, b10))
    palins.add(n)

print("Number of palindromes : {}".format(len(palins)))
print("Sum of palindromes {}".format(sum(palins)))

