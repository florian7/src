import random, copy, time

class GameOfLife():

    def __init__(self, grid_width):
        self.width = grid_width
        self.grid = [[random.randint(0, 1) for i in range(grid_width)] for i in range(grid_width)]

    def step(self):
        self.normalize()
        new_grid = copy.deepcopy(self.grid)

        for x in range(self.width):
            for y in range(self.width):
                s = self.sum_neighbors(x, y)
                e = self.grid[x][y]

                if s == 3 or (e == 1 and s == 2):
                    new_grid[x][y] += 1

                else:
                    new_grid[x][y] -= 1

        self.grid = new_grid

    def normalize(self):
        for x in range(self.width):
            for y in range(self.width):
                if self.grid[x][y] <= 0:
                    self.grid[x][y] = 0
                else:
                    self.grid[x][y] = 1

    def iterate(self, n = 1, verbose = True, wait_for_input = False):

        for i in range(n):

            self.print()

            if (wait_for_input):
                time.sleep(0.1)

            self.step()
        
    def sum_neighbors(self, x, y):
        n = 0

        for i in range(-1, 2):
            xi = (x + i) % self.width
            for j in range(-1, 2):
                yj = (y + j) % self.width
                n += self.grid[xi][yj]

        return n - self.grid[x][y]


    def print(self):
        print('-'.join(['-' for i in range(self.width)]))
        for x in range(self.width):
            print(' '.join(map(str, self.grid[x])).replace('-1', '□').replace('0','▫').replace('1', '▪').replace('2', '■'))
