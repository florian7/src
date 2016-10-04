#!/usr/bin/python3

from sympy.ntheory import factorint
from sys import argv

d_memo = {}

def d(n):
    global d_memo

    if n in d_memo:
        return d_memo.get(n)

    factors = factorint(n)

    d_sum = 1
    for p, m in factors.items():
       d_sum *= ((p ** (m + 1) - 1)  // (p - 1))

    d_sum -= n
    d_memo[n] = d_sum
    return d_sum

def main(n_max):
    
    amicable_sum = 0

    for n in range(1, n_max + 1):
        m = d(n)
        if m == n:
            continue
        d_m = d(m)

        if d_m == n:
            print(  "Amicable numbers :\n"
                    "d(d({})) = d({}) = {}".format(n, m, d_m))
            amicable_sum += m

    print("Amicable sum = {}".format(amicable_sum))


if __name__ == "__main__":

    if len(argv) >= 2:
        n_max = int(argv[1])
    else:
        n_max = 1000
        
    main(n_max)
