#!/usr/bin/python3 

from math import factorial
from itertools import product

def dec_to_n(dec):
    value = 0
    for i in range(len(dec)):
        value += dec[i] * 10 ** i
    return value
 
f_product = 1
for r in range(2, 8):
    print("range = {}".format(r))
    for p in product(range(10), repeat=r):
        if p[-1] == 0:
            continue
        n = dec_to_n(p)         
        f = sum([factorial(i) for i in p])
        if n == f:
            print("{} = {}!".format(n, p))
            f_product *= n

print("f_product = {}".format(f_product))
