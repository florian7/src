#!/usr/bin/python3 

def constant_step(l):
    d = l[1] - l[0]
    for i in range(1, len(l) - 1):
        if d != l[i + 1] - l[i]:
            return False

    return True

def main():
    nb_cars = int(input())

    for i in range(nb_cars):
        nb_pillars = int(input())
        pillars = [int(pillar) for pillar in input().split(" ")]

        result = "no"
        if constant_step(pillars):
            result = "yes"

        print("Case #{}: {}".format(i + 1, result))


if __name__ == "__main__":
    main()
