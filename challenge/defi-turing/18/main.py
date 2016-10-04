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

def is_abundant(n):
    return d(n) > n

def main(n_max):
    
    summable = [False] * (n_max + 1)
    abundants = []
    
    non_summable_sum = n_max * (n_max + 1) // 2

    for n in range(1, n_max + 1):
        if is_abundant(n):
            print("Abundant : {}".format(n))
            abundants += [n]
            for m in abundants:
                if n + m <= n_max and not summable[n + m]:
                    summable[n + m] = True
                    non_summable_sum -= n + m

    print("Summables : {}".format(summable))
    print("Non summable sum : {}".format(non_summable_sum))





if __name__ == "__main__":

    if len(argv) >= 2:
        n_max = int(argv[1])
    else:
        n_max = 1000
        
    main(n_max)
