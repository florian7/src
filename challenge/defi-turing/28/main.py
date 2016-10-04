#!/usr/bin/python3 


k_memo = {(0, 0) : 1, (0, 1) : 1, (0, 2) : 1, (0, 3) : 1}

def k(x, d):

    if not (x, d) in k_memo:
        k_memo[(x, d)] = 8 * x - 2 * d + k(x - 1, d)

    return k_memo[(x, d)]


diag_sum = 1

for x in range(1, 2013 // 2 + 1):
    for d in range(4):
        diag_sum += k(x, d)

print(diag_sum)
