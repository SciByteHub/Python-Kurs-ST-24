class Cell:
    def __init__(self, alive, dead):
        self.alive = alive
        self.dead = dead

    def __str__(self):
        return "*" if self.alive else "."
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Cell(True, False) for _ in range(self.width)] for _ in range(self.height)]
    
    def display(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))

    def __str__(self):
        return '\n'.join(' '.join(str(cell) for cell in row) for row in self.grid)
