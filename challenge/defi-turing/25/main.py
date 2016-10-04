#!/usr/bin/python3 

import code

fib_memo = {0: 0, 1 : 1, 2 : 1}

def fib(n):
    global fib_memo

    if not n in fib_memo:
        if n % 2 == 1:
            fib_memo[n] = fib(n // 2 + 1) ** 2 + fib(n // 2) ** 2
        else:
            fib_memo[n] = fib(n // 2 + 1) ** 2 - fib(n // 2 - 1) ** 2

    return fib_memo[n]

def test(n):
    f = fib(n)
    print("f = {}\nlen(f) = {}".format(f, len(str(f))))
code.interact(local=locals())
