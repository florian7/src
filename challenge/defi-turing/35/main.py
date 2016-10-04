#!/usr/bin/python3 

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

def is_circular(p):

    str_p = str(p)

    for i in range(len(str_p)):

        n = int(str_p[i:] + str_p[:i])
        if not is_prime(n):
            return False

    return True


circulars = set()

for n in range(100000):
    if is_circular(n):
        print("{} is circular".format(n))
        circulars.add(n)

print("{} circular primes".format(len(circulars)))
