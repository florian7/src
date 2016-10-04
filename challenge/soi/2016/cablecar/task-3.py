#!/usr/bin/python3

def longest_optimum(pillars):
    l_max = 0
    l = 1
    last_delta = -99999

    for i in range(len(pillars) - 1):

        delta = pillars[i + 1] - pillars[i]

        if delta != last_delta:
            l = 2

        else:
            l += 1

        if l > l_max:
            l_max = l
            
        last_delta = delta
    
    return l_max



def main():
    nb_cars = int(input())

    for i in range(nb_cars):
        nb_pillars = int(input())
        pillars = [int(pillar) for pillar in input().split(" ")]

        max_l = longest_optimum(pillars)

        print("Case #{}: {}".format(i + 1, max_l))


if __name__ == "__main__":
    main()
