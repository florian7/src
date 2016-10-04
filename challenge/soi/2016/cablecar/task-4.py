#!/usr/bin/python3

from sys import argv
import random

def possible_optimums(pillars):
    optimums = []

    for i in range(len(pillars)):
        
        for j in range(i + 1, len(pillars)):
            optimum = [i, j]
            step = pillars[j] - pillars[i]
            expected = pillars[j] + step

            for k in range(j + 1, len(pillars)):
                if pillars[k] == expected:
                    optimum += [k]
                    expected += step

            optimums += [optimum]

    return optimums


def solve(pillars):

    optimums = possible_optimums(pillars)
    optimums.sort(key=lambda x: len(x))
    optimum = optimums[-1]

    nb_delete = len(pillars) - len(optimum)

    return nb_delete


def test():
    nb_cars = 100

    for i in range(nb_cars):

        nb_pillars = random.randint(2, 1000)
        pillars = []

        for j in range(nb_pillars):
            pillars += [random.randint(1, 10 ** 9)]

        nb_delete = solve(pillars)
        print("Case #{}: {}".format(i + 1, nb_delete))


def interactive():
    nb_cars = int(input())

    for i in range(nb_cars):
        nb_pillars = int(input())
        pillars = [int(pillar) for pillar in input().split(" ")]

        nb_delete = solve(pillars)
        print("Case #{}: {}".format(i + 1, nb_delete))


def main():

    if len(argv) > 1 and argv[1] == "test":
        test()

    else:
        interactive()

if __name__ == "__main__":
    main()
