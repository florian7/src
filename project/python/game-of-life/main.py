#!/usr/bin/python3 


import sys
from game_of_life import *


def main():

    grid_width = 50
    if len(sys.argv) > 1:
        grid_width = int(sys.argv[1])

    game = GameOfLife(grid_width)

    game.iterate(300, True, True)


if __name__ == '__main__':
    main()
