#!/usr/bin/python3 

n_max = 2013
b_digits = 7
g_digits = 8


b_rings_1 = {2 * (b_digits - 1) * b + 2 for b in range(n_max // ((b_digits - 1) * 2) + 1)}
b_rings_2 = {2 * (b_digits - 1) * b for b in range(n_max // ((b_digits - 1) * 2) + 1)}
b_rings = b_rings_1.union(b_rings_2)

g_rings_1 = {2 * (g_digits - 1) * g + 2 for g in range(n_max // ((g_digits - 1) * 2) + 1)}
g_rings_2 = {2 * (g_digits - 1) * g for g in range(n_max // ((g_digits - 1) * 2) + 1)}
g_rings = g_rings_1.union(g_rings_2)

rings = g_rings.intersection(b_rings)


b_rings = list(b_rings)
b_rings.sort()
print("b_rings = {}\n".format(b_rings))

g_rings = list(g_rings)
g_rings.sort()
print("g_rings = {}\n".format(g_rings))

rings = list(rings)
rings.sort()
print("rings = {}".format(rings))
print("sum(rings) = {}".format(sum(rings)))
