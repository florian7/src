#!/usr/bin/python3


import sys
from gmpy2 import mpz


def collatz_rec(n, max_steps, steps):
    steps += 1

    #print("{} : {}".format(steps, n))

    if n == 1:
        return steps

    elif steps == max_steps:
        return -1

    elif n % 2 == 0:
        return collatz_rec(n // 2, max_steps, steps)

    else:
        return collatz_rec(n * 3 + 1, max_steps, steps)


def collatz(n0, max_steps):
    return collatz_rec(n0, max_steps, -1)


def main(argv):

    max_steps = 1000000
    sys.setrecursionlimit(max_steps)

    if len(argv) != 2:
        print("Usage {} <n0>".format(argv[0]))
        return -1

    try:
        n0 = mpz(argv[1])

    except:
        print("Provide a valide integer")
        return -1

    steps = collatz(n0, max_steps)

    if steps < 0:
        print("collatz({}) did not end in {} steps".format(n0, max_steps))

    else:
        print("collatz({}) ended in {} steps".format(n0, steps))

    return 0


main(sys.argv)
