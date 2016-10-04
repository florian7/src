#!/usr/bin/python3 

from sympy.ntheory import factorint
import code

numbers = set()

a_max = 1000
b_max = 1000

for a in range(2, a_max + 1):
    for b in range(2, b_max + 1):
        f = factorint(a)
        n = [(p, k * b) for p, k in f.items()]
        n.sort()
        n = tuple(n)
        numbers.add(n)

print(len(numbers))
code.interact(local=locals())
