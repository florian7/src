#!/usr/bin/python3 

from itertools import permutations 

grid = list(range(1,10))
min_grid = []
max_grid = []
min_value = 999999
max_value = 0

for grid in permutations(grid):
    value = 0

    for i in range(3):
        value += grid[3 * i] * grid[3 * i + 1] * grid[3 * i + 2]
    for i in range(3):
        value += grid[i] * grid[i + 3] * grid[i + 6]

    if value > max_value:
        max_grid = grid
        max_value = value
    if value < min_value:
        min_grid = grid
        min_value = value

product_value = min_value * max_value
print("{} * {} = {}".format(min_value, max_value, product_value))
print("min_grid : {}\nmax_grid : {}".format(min_grid, max_grid))
