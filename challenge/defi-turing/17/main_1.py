#!/usr/bin/python3 

import math, sys

if len(sys.argv) < 2:
    n_max = 1000
else:
    n_max = int(sys.argv[1])

d_memo = [None] * 2 * n_max

def d(n):
    global d_memo

    if d_memo[n] != None:
        return d_memo[n]

    d_sum = 0
    for i in range(1, n // 2 + 1):   
        if n % i == 0:
            d_sum += i

    d_memo[n] = d_sum

    return d_sum

amicable_sum = 0

for n in range(n_max + 1):

    d_n = d(n)
    if d_n == n:
        continue

    dd_n = d(d_n)

    if dd_n == n:
        print(  "Amicable numbers :\n"
                "d(d({})) = d({}) = {}".format(n, d_n, dd_n))
        amicable_sum += n

print(amicable_sum)
