#!/usr/bin/python3 

from itertools import permutations 

# Symbols to index table
#
# T : 0
# H : 1
# R : 2
# E : 3
# N : 4
# U : 5
# F : 6
# O : 7
# I : 8
# S : 9

symbols = {"T" : 0, "H" : 1, "R" : 2, "E" : 3, "N" : 4, "U" : 5, "F" : 6, "O" : 7, "I" : 8, "S" : 9}
index = list(range(0, 10))


def word_to_n(word, index):
    global symbols
    
    value = 0
    for n, char in enumerate(reversed(word)):
        value += index[symbols[char]] * 10 ** n

    return value


for i in permutations(index):

    three =  word_to_n("THREE", i)
    if three % 9 != 0:
        continue

    neuf =  word_to_n("NEUF", i)
    if neuf % 9 != 0:
        continue

    trois =  word_to_n("TROIS", i)
    if trois % 3 != 0:
        continue

    nine =  word_to_n("NINE", i)
    if nine % 3 != 0:
        continue

    if three * nine == trois * neuf:
        print("{} * {} == {} == {} * {}".format(three, nine, trois * neuf, trois, neuf))

    else:
        pass
        #print("{} * {} != {} * {}".format(three, nine, trois, neuf))


