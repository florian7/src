#!/usr/bin/python3 

def decompose(total, coins):

    decompositions = 0
    for i in range(len(coins)):
        n_total = total - coins[i]
        if n_total == 0:
            decompositions += 1
        elif n_total > 0:
            decompositions += decompose(n_total, coins[i:])

    return decompositions

print(decompose(1000, (5,10,20,50,100,200,500)))
