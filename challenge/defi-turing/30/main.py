#!/usr/bin/python3 

from itertools import combinations_with_replacement

k = 5
k_sum = 0

for r in range(2, k + 2):
    for dec in combinations_with_replacement(range(10), r):
        n = 0
        for d in dec:
            n += d ** k

        m = n
        new_dec = []
        for u in reversed(range(0, k + 2)):
            v = m // 10 ** u 
            if v <= 0:
                continue
            m -= v * 10 ** u
            new_dec += [v]
        
        old_dec = sorted(list(dec))
        new_dec.sort()

        if old_dec == new_dec:
            k_sum += n

print(k_sum)
