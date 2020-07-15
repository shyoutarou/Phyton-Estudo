import numpy as np
import random

##from 1 to N
grid_size = 10
grid_open_chance = .65


class percolation_grid:

    def __init__(self, size):
        self.grid = np.zeros((size, size), dtype=int)
        self.union_field = np.arange(1, size ** 2 + 1)
        self.size = size

    ##x is the row in the matrix and y is the colum in matrix
    ##going from 1 to size
    def open(self, x, y):

        ##open up site on grid if it is not open
        if self.grid[x - 1][y - 1] == 0:
            self.grid[x - 1][y - 1] = 1
        else:
            return

        self.maintain_connections(x, y)

    def maintain_connections(self, x, y):
        elem = self.getElemNum(x, y)

        # check left
        if self.isOpen(x - 1, y - 2):
            pid = self.union_field[elem]
            q = 0
            for number in self.union_field:
                if self.union_field[q] == pid:
                    self.union_field[q] = elem
                q += 1

        # check above
        if self.isOpen(x - 2, y - 1):
            pid = self.union_field[elem]
            q = 0
            for number in self.union_field:
                if self.union_field[q] == pid:
                    self.union_field[q] = elem - self.size + 1
                q += 1

    def isOpen(self, x, y):
        try:
            if self.grid[x][y] == 1:
                return True
            else:
                return False
        except:
            return

    def getElemNum(self, x, y):
        # pass this function row and column in 1 to N
        return (x - 1) * self.size + (y - 1)

    def getCoordinates(self, elem):
        return elem / self.size + 1, elem % self.size + 1

    def isFull(self, x, y):
        elem = self.getElemNum(x, y)
        pointer = self.union_field[elem] - 1

        if elem != pointer:
            print(elem, pointer)
            print(self.getCoordinates(pointer))

            if self.getCoordinates(pointer)[0] == 1:
                print("IS FULL")
                return

            self.isFull(self.getCoordinates(pointer)[0], \
                        self.getCoordinates(pointer)[1])


t_grid = percolation_grid(grid_size)

for i in range(1, grid_size + 1):
    for j in range(1, grid_size + 1):
        if random.random() < grid_open_chance: t_grid.open(i, j)

print("\n", t_grid.grid)
print("\n\n", t_grid.union_field.reshape(grid_size, grid_size))
t_grid.isFull(10, 4)