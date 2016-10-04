#!/usr/bin/python3 

import code

sieve = [False, False, True]

def fill_sieve(n):
    global sieve
    
    sieve += [True] * (n - len(sieve) + 1)
    for i in range(len(sieve)):
        if not sieve[i]:
            continue
        for m in range(2 * i, n + 1, i):
            sieve[m] = False

def is_prime(n):
    global sieve
    
    if n < 2:
        return False
    if len(sieve) < n + 1 or sieve[n] == None:
        fill_sieve(n)

    return sieve[n]

left_prod = set()

def extend_left(n):
    global left_prod
    if n > 1000000:
        return

    for i in range(1, 10):
        new_n = int(str(i) + str(n))
        if not is_prime(new_n):
            continue
        left_prod.add(new_n)
        extend_left(new_n)

right_prod = set()

def extend_right(n):
    global right_prod
    if n > 1000000:
        return

    for i in range(1, 10):
        new_n = int(str(n) + str(i))
        if not is_prime(new_n):
            continue
        right_prod.add(new_n)
        extend_right(new_n)


for i in range(10):
    if not is_prime(i):
        continue
    extend_left(i)
    extend_right(i)

tronc = right_prod.intersection(left_prod)

print("tronc = {}".format(tronc))
print("len(tronc) = {}".format(len(tronc)))
print("sum(tronc) = {}".format(sum(tronc)))

code.interact(local=locals())
