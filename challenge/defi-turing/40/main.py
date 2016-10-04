#!/usr/bin/python3 

def d(n):
    n -= 1
    min_r = 1
    max_r = 9
    digits_n = 1

    while True:
        a = n // digits_n
        if a > max_r:
            a = max_r
        
        n -= a * digits_n

        if n < digits_n:
            return int(str(min_r + a)[n])

        min_r *= 10
        max_r *= 10
        digits_n += 1
        
product = 1
for i in range(9):
    product *= d(10 ** i)

print("product = {}".format(product))
