#!/usr/bin/python3 

import operator

coprimes = set()
coprimes_max = 10000

def expand_coprimes(m, n):
    global coprimes_max, coprimes

    stack = [(m, n)]
    while len(stack) > 0:

        m, n = stack.pop(0)
        if m > coprimes_max or n > coprimes_max:
            return

        coprimes.add((m, n))
        stack += [(2 * m - n, m)]
        stack += [(2 * m + n, m)]
        stack += [(m + 2 * n, n)]

expand_coprimes(2, 1)
expand_coprimes(3, 1)

perimeters = {}

for coprime in coprimes:
    m, n = coprime

    if (m - n) % 2 == 0:
        continue

    k = 0
    while k == 0 or p < 10000:
        k += 1
        a = k * (m ** 2 - n ** 2)
        b = k * 2 * m * n
        c = k * (m ** 2 + n ** 2)
        p = a + b + c
        
        if p not in perimeters:
            perimeters[p] = 1
        else:
            perimeters[p] += 1

sorted_perimeters = list(reversed(sorted(perimeters.items(), key=operator.itemgetter(1))))
print(sorted_perimeters[:10])
