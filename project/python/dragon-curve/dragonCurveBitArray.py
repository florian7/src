from bitstring import BitArray

class Instructions():

    R = BitArray(bin='0b0')
    
    def __init__(self, steps = 4):

        # R and L are represented this way:
        #   R:  0
        #   L:  1

        self.steps = steps
        self.step = 1
        self.instructions = Instructions.R.copy()

    def generate(self):
        while self.step < self.steps:
            self.generationStep()

    def generationStep(self):
        flip = self.flip()
        self.instructions.append(Instructions.R)
        self.instructions.append(flip)
        self.step += 1

    def flip(self):
        copy = self.instructions.copy()
        copy.reverse()
        copy.invert()
        return copy
