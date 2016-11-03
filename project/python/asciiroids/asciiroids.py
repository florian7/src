import random as rn
import numpy as np


class Grid():

    def __init__(self, size):
        self.size = size
        self.grid = [[' ' for i in range(size)] for j in range(size)]

    def draw(self, pattern):
        for point in pattern.get_points():
            self.grid[point[0]][point[1]] = pattern.get_char()

    def print(self):
        for i in self.grid:
            print(' '.join(i))



class Pattern():

    def __init__(self, pos, matrix, char):
        self.char = char
        self.matrix = matrix
        self.pos = pos

    def get_points(self):
        points = []

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):

                if self.matrix[i][j] == 0:
                    continue

                points += [self.pos + np.array([i, j])]

        return points

    def get_char(self):
        return self.char


class Player():

    def __init__(self):
        self.name = 'Undefined Player'
        self.direction = 7

    def set_position(self, pos):
        self.pos = pos

    def get_pattern(self):
        
        if self.direction % 2:
            points = [[0, 0, 0], [1, 0, 1], [0, 1, 0]]
            return Pattern(self.pos, points, 'X')


class Bot(Player):

    nb_bot = 0

    def __init__(self):
        super().__init__()

        Bot.nb_bot += 1
        self.name = 'Bot {}'.format(Bot.nb_bot)


class Human(Player):

    nb_human = 0 

    def __init__(self):
        super().__init__()

        Human.nb_human += 1
        self.name = input("Player {}: ".format(Human.nb_human))


class Game():

    def __init__(self, size = 32, nb_human = 1, nb_bot = 0):
        humans = [Human() for i in range(nb_human)]
        bots = [Bot() for i in range(nb_bot)]
        self.players = humans + bots

        self.grid = Grid(size)

    def start(self):
        self.grid.print()

        for player in self.players:
            player.set_position(np.array([rn.randint(0, self.grid.size - 1), rn.randint(0, self.grid.size - 1)]))
            self.grid.draw(player.get_pattern())

        self.grid.print()
