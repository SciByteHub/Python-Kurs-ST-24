#libs
import random

#defining classes
class Cell:
    def __init__(self, alive):
        self.alive = alive
        
    def update_status(self, alive_neighbors):
        if self.alive:
            if alive_neighbors < 2 or alive_neighbors > 3:
                self.alive = False
        else:
            if alive_neighbors == 3:
                self.alive = True

    def __str__(self):
        return "*" if self.alive else "."
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Cell(random.choice([True, False])) for _ in range(self.width)] for _ in range(self.height)]
    
    def display(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))

    def __str__(self):
        return '\n'.join(' '.join(str(cell) for cell in row) for row in self.grid)

