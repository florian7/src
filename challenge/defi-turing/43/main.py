#!/usr/bin/python3 

from itertools import combinations_with_replacement
from math import sqrt

def dec_to_n(dec):
    value = 0
    for i in range(len(dec)):
        value += dec[i] * 10 ** i
    return value

l_max = 13
palins = set([(1, 1), (2, 4),(3, 9)])

for r in range(0, l_max // 2 + 1):
    for p in combinations_with_replacement(range(10), r):

        if len(p) == 0 or p[0] == 0:
            continue

        palin = dec_to_n(p + p[::-1])
        root = sqrt(palin)
        if root == int(root):
            palins.add((int(root), palin))

        if 2 * r + 1 > l_max:
            continue

        for i in range(10):
            palin = dec_to_n(p + tuple([i]) + p[::-1])
            root = sqrt(palin)
            if root == int(root):
                palins.add((int(root), palin))

print("palins = {}".format(palins))
print("sum(palins) = {}".format(sum([palin[0] for palin in palins])))

palins = set()

for i in range(int(sqrt(10 ** l_max))):
    n = str(i ** 2)
    if n == n[::-1]:
        palins.add((i, n))

print("palins = {}".format(palins))
print("sum(palins) = {}".format(sum([palin[0] for palin in palins])))
