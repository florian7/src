#!/usr/bin/python3 

from itertools import permutations

solutions = set()
for p in permutations(range(10), 5):
    u = p[0]
    n = p[1]
    d = p[2]
    e = p[3]
    x = p[4]

    un = u * 10 + n
    deux = d * 1000 + e * 100 + u * 10 + x

    if un * un + un == deux:
        print("solution :\n\tu : {}\n\tn : {}\n\td : {}\n\te : {}\n\tx : {}\ndeux = {}, un = {}".format(u, n, d, e, x, deux, un))

        print("{} * {} = {}".format(un, un, un * un))
        print("{} + {} = {}".format(un * un, un, un * un + un))
        solutions.add(deux)

print(solutions)

