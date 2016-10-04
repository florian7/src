#!/usr/bin/python3 

from itertools import permutations

p = list(permutations(range(10)))
print(p[2 * 10 ** 6 - 1])
