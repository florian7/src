#!/usr/bin/python3 

from itertools import permutations

dates = set()
for n in range(1, 5):
    for p in permutations(range(10), n):
        date = 0
        for m in range(n):
            date += p[m] * 10 ** m
        if date <= 2013:
            dates.add(date)

dates.discard(0)
print("Dates : {}".format(dates))
print("a) {}".format(len(dates)))

dates = list(dates)
diffs = [dates[i + 1] - dates[i] for i in range(len(dates) - 1)]
print(diffs)
print("b) {}".format(max(diffs)))
print("a) * b) = {}".format(len(dates) * max(diffs)))
