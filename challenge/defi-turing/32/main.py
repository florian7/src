#!/usr/bin/python3 

from itertools import permutations

def dec_to_n(dec):
    value = 0
    for i in range(len(dec)):
        value += dec[i] * 10 ** i
    return value

products = set()
for p in permutations(range(1, 10)):
    for i in range(1, 8):
        for j in range(1, 9 - i):
            a = dec_to_n(p[:i])
            b = dec_to_n(p[i:i + j])
            c = dec_to_n(p[i + j:9])

            if a * b == c:
                print("{} * {} == {}".format(a, b, c))
                products.add(c)

print("products = {}".format(products))
print("sum = {}".format(sum(products)))
