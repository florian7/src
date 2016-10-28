import numpy as np
import math

class Instructions():

    R = np.matrix([[0, 1], [-1, 0]])
    L = np.matrix([[0, -1], [1, 0]])
    
    def __init__(self, steps = 4):
        self.steps = steps
        self.step = 0
        self.instructions = ''

    def __str__(self):
        return self.instructions

    def __repr__(self):
        return str(self)

    def generate(self):
        while self.step < self.steps:
            self.generationStep()

    def generationStep(self):
        self.instructions += 'R' + self.flip()
        self.step += 1

    def flip(self):
        copy = ''.join(list(reversed(self.instructions)))
        return copy.replace('R', 'l').replace('L', 'R').replace('l', 'L')

class Line():

    def __init__(self, instructions):
        self.instructions = instructions.instructions
        self.line = np.matrix([0, 0])
        self.direction = np.array([1, 0])

    def __str__(self):
        return str(self.line)

    def __repr__(self):
        return str(self)

    def generate(self):
        #for instruction in self.instructions:
        #    self.generationStep(instruction)

        for i in range(1, len(self.instructions) + 1):
            self.generationStep(i)

    def generationStep(self, i):
        if getInstruction(i) == 1:
            instruction = 'R'
        else:
            instruction = 'L'

        self.rotate(instruction)
        self.line = np.append(self.line, self.line[-1] + self.direction, axis = 0)

    def rotate(self, instruction):
        if instruction == 'R':
            rotation = Instructions.R

        elif instruction == 'L':
            rotation = Instructions.L

        self.direction = self.direction * rotation


def getInstruction(index):

    if index <= 2:
        return 1

    majorant = 2 ** math.ceil(math.log(index, 2))
    source = majorant - index

    if source == 0:
        return 1

    return -getInstruction(source)

