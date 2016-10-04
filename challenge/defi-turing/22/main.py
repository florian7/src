#!/usr/bin/python3 

from itertools import product

def list_to_n(t):
    n = 0
    for k in range(len(t)):
        n += t[len(t) - k - 1] * 10 ** k

    return n

def n_to_list(n):
    t = []
    for k in reversed(range(6)):
       m = n // (10 ** k) 
       n -= m * 10 ** k
       t += [m]

    return t


for p in product(range(10), repeat=6):
    if p[0] == 0:
        continue

    p = list(p)
    n = list_to_n(p)
    m = n * 8
    q = n_to_list(m)

    p.sort()
    q.sort()

    if p == q:
        print("n = {}\tm = {}".format(n, m))
